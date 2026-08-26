#!/usr/bin/env python3
"""Fast panel extraction v2: GENCODE GTF gene spans + merged-interval bisect scan."""
import bisect
import gzip
import importlib.util
import json
import os

spec = importlib.util.spec_from_file_location("scan", "analysis/scan_panel.py")
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)
PANEL = scan.PANEL

VCF = "data/WGS_EX2312012_HGWCNDSX7.vcf.gz"
GTF = "resources/gencode.v44.basic.gtf.gz"
OUT = "analysis/candidates/panel_variants.tsv"


def gtf_gene_spans():
    regions = {}
    with gzip.open(GTF, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.split("\t")
            feat = parts[2]
            if feat != "gene":
                continue
            attrs = dict(
                kv.strip().split(" ", 1)
                for kv in parts[8].rstrip("\n").split(";")
                if " " in kv
            )
            name = attrs.get("gene_name", "").strip('"')
            if name in PANEL:
                chrom = parts[0].lstrip("chr")
                s, e = int(parts[3]), int(parts[4])
                if name in regions:
                    c0, s0, e0 = regions[name]
                    regions[name] = (c0, min(s0, s), max(e0, e))
                else:
                    regions[name] = (chrom, s, e)
    return regions


def main():
    regions = gtf_gene_spans()
    missing = [s for s in PANEL if s not in regions]
    print(f"GTF spans for {len(regions)}/{len(PANEL)} genes; missing: {missing}")
    # merged disjoint intervals per chrom
    bychrom = {}
    for sym, (c, s, e) in regions.items():
        bychrom.setdefault(c, []).append((max(1, s - 5000), e + 5000, sym))
    merged = {}
    for c, ivs in bychrom.items():
        ivs.sort()
        out = []
        for s, e, sym in ivs:
            if out and s <= out[-1][1]:
                out[-1] = (out[-1][0], max(out[-1][1], e), out[-1][2] | {sym})
            else:
                out.append((s, e, {sym}))
        merged[c] = ([s for s, _, _ in out], out)
    total = 0
    out = open(OUT, "w")
    out.write("\t".join(["gene", "chrom", "pos", "ref", "alt", "qual", "filter", "gt",
                         "ad_ref", "ad_alt", "dp", "gq", "pid", "pgt", "dbsnp", "info"]) + "\n")
    with gzip.open(VCF, "rt") as f:
        for line in f:
            if line[0] == "#":
                continue
            parts = line.rstrip("\n").split("\t")
            m = merged.get(parts[0])
            if not m:
                continue
            starts, ivs = m
            pos = int(parts[1])
            i = bisect.bisect_right(starts, pos) - 1
            if i < 0:
                continue
            s, e, syms = ivs[i]
            if pos > e:
                continue
            ref, alts = parts[3], parts[4].split(",")
            fmt = parts[8].split(":")
            d = dict(zip(fmt, parts[9].split(":")))
            if d.get("GT") in ("0/0", "0|0", "./.", "0", "."):
                continue
            ad = d.get("AD", "").split(",")
            for k, alt in enumerate(alts):
                if alt == "*":
                    continue
                out.write("\t".join([
                    ",".join(sorted(syms)), f"chr{parts[0]}", parts[1], ref, alt,
                    parts[5], parts[6], d.get("GT", ""), ad[0] if ad else "",
                    ad[k + 1] if len(ad) > k + 1 else "", d.get("DP", ""),
                    d.get("GQ", ""), d.get("PID", ""), d.get("PGT", ""),
                    parts[2], parts[7]]) + "\n")
                total += 1
    out.close()
    print(f"Wrote {total} non-ref panel variant alleles -> {OUT}")


if __name__ == "__main__":
    main()
