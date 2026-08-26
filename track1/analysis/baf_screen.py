#!/usr/bin/env python3
"""E3: Mosaic aneuploidy screen from the provided VCF (MoChA-substitute).

Per chromosome: het-SNP alt-allele-fraction distribution vs diploid expectation (0.5).
Mosaic trisomy f => BAF modes at (1-f)/3±, (2+f)/3± style shifts; LOH => drift to 0/1.
Metrics: mean|BAF-0.5|, fraction of hets in tails (0.15-0.35 / 0.65-0.85), het:hom ratio.
Output: analysis/candidates/mosaic_baf_screen.tsv
"""
import gzip
from collections import defaultdict

VCF = "data/WGS_EX2312012_HGWCNDSX7.vcf.gz"
OUT = "analysis/candidates/mosaic_baf_screen.tsv"

stats = defaultdict(lambda: {"n_het": 0, "n_hom": 0, "sum_abs_dev": 0.0,
                             "tail_lo": 0, "tail_hi": 0, "dp_sum": 0, "bins": defaultdict(int)})
with gzip.open(VCF, "rt") as f:
    for line in f:
        if line[0] == "#":
            continue
        p = line.split("\t")
        chrom = p[0]
        s = stats.get(chrom)
        if s is None:
            s = stats[chrom]
        fmt = p[8].split(":")
        try:
            gi = fmt.index("GT"); di = fmt.index("AD"); qi = fmt.index("GQ")
        except ValueError:
            continue
        d = p[9].split(":")
        gt = d[gi]
        try:
            gq = int(d[qi])
        except ValueError:
            continue
        if gq < 20:
            continue
        ad = d[di].split(",")
        try:
            ref, alt = int(ad[0]), int(ad[1]) if len(ad) > 1 else 0
        except ValueError:
            continue
        if gt in ("0/1", "0|1", "1|0"):
            dp = ref + alt
            if dp < 10 or ref + alt == 0:
                continue
            baf = alt / (ref + alt)
            s["n_het"] += 1
            s["sum_abs_dev"] += abs(baf - 0.5)
            if 0.15 <= baf <= 0.35:
                s["tail_lo"] += 1
            if 0.65 <= baf <= 0.85:
                s["tail_hi"] += 1
            s["dp_sum"] += dp
            s["bins"][round(baf, 1)] += 1
        elif gt in ("1/1", "1|1"):
            s["n_hom"] += 1

order = [str(c) for c in range(1, 23)] + ["X", "Y", "M"]
genome_hets = sum(s["n_het"] for c, s in stats.items() if c in order[:23])
genome_tail = sum(s["tail_lo"] + s["tail_hi"] for c, s in stats.items() if c in order[:23])
genome_dev = sum(s["sum_abs_dev"] for c, s in stats.items() if c in order[:23])
base_tail_frac = genome_tail / genome_hets if genome_hets else 0
base_dev = genome_dev / genome_hets if genome_hets else 0

with open(OUT, "w") as out:
    out.write("chrom\tn_het\tn_hom\thet_hom_ratio\tmean_abs_dev\tdelta_dev\ttail_frac\t"
              "delta_tail\tmean_dp\tbins(0.0-1.0)\n")
    for c in order:
        s = stats.get(c)
        if not s or s["n_het"] < 500:
            continue
        tf = (s["tail_lo"] + s["tail_hi"]) / s["n_het"]
        out.write("\t".join(map(str, [
            c, s["n_het"], s["n_hom"], round(s["n_het"] / max(s["n_hom"], 1), 2),
            round(s["sum_abs_dev"] / s["n_het"], 4),
            round(s["sum_abs_dev"] / s["n_het"] - base_dev, 4),
            round(tf, 4), round(tf - base_tail_frac, 4),
            round(s["dp_sum"] / s["n_het"], 1),
            ",".join(f"{b:.1f}:{n}" for b, n in sorted(s["bins"].items()))])) + "\n")
print("baseline: het hets =", genome_hets, "tail_frac =", round(base_tail_frac, 4),
      "mean|dev| =", round(base_dev, 4))
print("wrote", OUT)
