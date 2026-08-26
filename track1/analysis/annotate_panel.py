#!/usr/bin/env python3
"""Annotate panel variants: consequence classes from GENCODE GTF (MANE) + reference FASTA.

Classes: stop_gained, missense, synonymous, frameshift, inframe_indel,
splice_donor, splice_acceptor, splice_region, start_lost, stop_lost,
utr5, utr3, intronic, upstream/downstream.
Output: analysis/candidates/panel_annotated.tsv
"""
import gzip
import json
import os
import sys

GTF = "resources/gencode.v44.basic.gtf.gz"
FASTA_GZ = "resources/grch38_no_alt.fa.gz"
FASTA = "resources/grch38_no_alt.fa"
VARIANTS = "analysis/candidates/panel_variants.tsv"
OUT = "analysis/candidates/panel_annotated.tsv"

COMP = str.maketrans("ACGTN", "TGCAN")
CODONS = {}
_bases = "TCAG"
_aas = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
_i = 0
for b1 in _bases:
    for b2 in _bases:
        for b3 in _bases:
            CODONS[b1 + b2 + b3] = _aas[_i]
            _i += 1


def load_mane_models(genes):
    """gene -> {tx_id, strand, exons[(s,e)], cds[(s,e)], chrom} using MANE_Select or longest."""
    best = {}
    cur_tx = None
    with gzip.open(GTF, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            feat = p[2]
            if feat not in ("transcript", "exon", "CDS"):
                continue
            attrs = {}
            for kv in p[8].split(";"):
                if " " in kv:
                    k, v = kv.strip().split(" ", 1)
                    attrs[k] = v.strip('"')
            gene = attrs.get("gene_name")
            if gene not in genes:
                continue
            tx = attrs["transcript_id"]
            t = best.setdefault(gene, {})
            if feat == "transcript":
                rec = t.setdefault(tx, {"chrom": p[0].lstrip("chr"), "strand": p[6],
                                        "exons": [], "cds": [], "mane": "MANE_Select" in attrs,
                                        "len": 0})
            else:
                if tx not in t:
                    t[tx] = {"chrom": p[0].lstrip("chr"), "strand": p[6], "exons": [], "cds": [],
                             "mane": "MANE_Select" in attrs, "len": 0}
                rec = t[tx]
                s, e = int(p[3]), int(p[4])
                if feat == "exon":
                    rec["exons"].append((s, e))
                else:
                    rec["cds"].append((s, e))
                    rec["len"] += e - s + 1
    models = {}
    for gene, txs in best.items():
        cand = None
        for tx, rec in txs.items():
            if rec["mane"] and rec["cds"]:
                cand = rec
                break
        if cand is None:
            for tx, rec in sorted(txs.items(), key=lambda kv: -kv[1]["len"]):
                if rec["cds"]:
                    cand = rec
                    break
        if cand:
            cand["exons"].sort()
            cand["cds"].sort()
            models[gene] = cand
    return models


class Fasta:
    """pyfaidx-backed reader (handles any line length)."""

    def __init__(self, path):
        from pyfaidx import Fasta as _F
        self._f = _F(path)

    def fetch(self, chrom, start, end):
        """1-based inclusive [start, end]."""
        try:
# alias both naming conventions (chr-prefixed preferred)
            if chrom in self._f:
                return str(self._f[chrom][start - 1:end]).upper()
            alt = chrom.lstrip("chr") if chrom.startswith("chr") else "chr" + chrom
            if alt in self._f:
                return str(self._f[alt][start - 1:end]).upper()
            return ""
        except KeyError:
            return ""


def splicing_distance(pos, exons):
    """min distance to an exon boundary; inside exon -> 0; donor=5', acceptor=3' decided by strand."""
    best = None
    for i, (s, e) in enumerate(exons):
        if s <= pos <= e:
            d_in = min(pos - s, e - pos)
            best = (0, d_in) if best is None else min(best, (0, d_in))
        else:
            d = min(abs(pos - s), abs(pos - e))
            best = (d, d) if best is None else min(best, (d, d))
    return best  # (to_boundary, within)


def classify(pos, ref, alt, model, fa):
    strand = model["strand"]
    exons = model["exons"]
    cds = model["cds"]
    # location buckets
    in_exon = any(s <= pos <= e for s, e in exons)
    in_cds = any(s <= pos <= e for s, e in cds)
    # splice distances
    dists = []
    for s, e in exons:
        if pos < s:
            dists.append((s - pos, s, e, "acceptor_or_donor"))
        elif pos > e:
            dists.append((pos - e, s, e, "acceptor_or_donor"))
        else:
            dists.append((0, s, e, "inside"))
    d, ex_s, ex_e, where = min(dists)
    # determine donor/acceptor relative to strand
    if where == "inside":
        pass
    # upstream boundary of exon (lower coord) = acceptor for + strand, donor for -
    lo_dist = min(abs(pos - ex_s), abs(pos - ex_e)) if where != "inside" else 0
    if not in_exon:
        if lo_dist <= 2:
            cls = "splice_site"
        elif lo_dist <= 8:
            cls = "splice_region"
        elif in_cds:
            cls = "coding"
        else:
            cls = "intronic"
    else:
        cls = "exonic"
    if not in_cds and cls in ("exonic", "coding"):
        # UTR or non-coding exon
        cls = "utr_or_nc"
    if cls == "exonic" or (in_cds and in_exon):
        # sequence-based call for coding SNVs/indels
        cs, ce = cds[0][0], cds[-1][1]
        if not (cs <= pos <= ce):
            return cls if cls != "exonic" else "utr_or_nc"
        # build CDS sequence once per gene (cached)
        key = (model["chrom"],)
        if key not in _cds_cache:
            parts = [fa.fetch(model["chrom"], s, e) for s, e in cds]
            seq = "".join(parts).upper()
            if strand == "-":
                seq = seq.translate(COMP)[::-1]
            _cds_cache[key] = seq
        cds_seq = _cds_cache[key]
        # offset of pos within CDS (0-based, transcript orientation)
        off = 0
        for s, e in cds:
            if s <= pos <= e:
                off += (pos - s) if strand == "+" else (e - pos)
                break
            off += e - s + 1
        # SNV
        if len(ref) == 1 and len(alt) == 1:
            codon_i = off // 3
            within = off % 3
            codon = cds_seq[codon_i * 3:codon_i * 3 + 3]
            alt_base = alt if strand == "+" else alt.translate(COMP)
            new_codon = codon[:within] + alt_base + codon[within + 1:]
            aa = CODONS.get(codon, "?")
            new_aa = CODONS.get(new_codon, "?")
            if aa == "?":
                return "coding_unknown"
            if codon_i == 0 and aa == "M":
                return "start_lost" if new_aa != "M" else "synonymous"
            if aa == "*":
                return "stop_lost" if new_aa != "*" else "synonymous"
            if new_aa == "*":
                return "stop_gained"
            return "missense" if aa != new_aa else "synonymous"
        # indel: frameshift if len delta % 3 != 0
        delta = len(alt) - len(ref)
        if delta % 3 != 0:
            return "frameshift"
        # inframe: check if removes stop / disruptive — approximate
        return "inframe_indel"
    return cls


_cds_cache = {}


def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("scan", "analysis/scan_panel.py")
    scan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scan)
    panel = set(scan.PANEL)
    genes = set()
    rows = []
    with open(VARIANTS) as f:
        hdr = f.readline().rstrip("\n").split("\t")
        for line in f:
            rows.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))
            for g in rows[-1]["gene"].split(","):
                genes.add(g)
    print("building MANE models for", len(genes), "genes")
    models = load_mane_models(genes)
    print("models:", len(models))
    fa_path = FASTA if os.path.exists(FASTA) else FASTA_GZ
    print("fasta:", fa_path)
    fa = Fasta(fasta_path=fa_path) if False else Fasta(fa_path)
    out = open(OUT, "w")
    out.write("\t".join(hdr + ["gene_used", "consequence"]) + "\n")
    for r in rows:
        gset = [g for g in r["gene"].split(",") if g in models]
        # choose the model where the variant actually lands in gene span
        gene_used, cons = ",", "."
        for g in gset:
            m = models[g]
            pos = int(r["pos"])
            span_s = min(s for s, e in m["exons"])
            span_e = max(e for s, e in m["exons"])
            if span_s - 5000 <= pos <= span_e + 5000:
                try:
                    c = classify(pos, r["ref"], r["alt"], m, fa)
                except Exception as ex:
                    c = f"err:{ex}"
                gene_used = g
                cons = c
                break
        out.write("\t".join([r[k] for k in hdr] + [gene_used, cons]) + "\n")
    out.close()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
