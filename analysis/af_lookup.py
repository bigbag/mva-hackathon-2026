#!/usr/bin/env python3
"""Annotate priority candidates: Ensembl VEP (batch, consequence+colocated) + gnomAD (AF+ClinVar).

Usage: .venv/bin/python analysis/af_lookup.py
Writes: analysis/candidates/priority_annotated.tsv
"""
import json
import sys

sys.path.insert(0, "analysis")
from netutil import fetch_json

# (gene, chrom_nochr, pos, ref, alt, tag)
CANDS = [
    ("BUB1", "2", 110668376, "C", "T", "novel"),
    ("BUB1", "2", 110671177, "G", "A", "novel"),
    ("BUB1", "2", 110681625, "GAGAGAGAA", "G", "novel 8bp del"),
    ("BUB1", "2", 110681631, "GAA", "G", "alt-repr 2bp del"),
    ("BUB1", "2", 110680852, "CT", "C", "rs201735899"),
    ("BUB1B", "15", 40209701, "T", "G", "novel"),
    ("BUB1B", "15", 40216470, "A", "G", "novel"),
    ("BUB1B", "15", 40220612, "T", "G", "novel"),
    ("BUB1B", "15", 40192892, "C", "T", "rs185599777"),
    ("CEP57", "11", 95786495, "G", "A", "rs144140679"),
    ("CEP57", "11", 95786791, "T", "C", "rs139949893"),
    ("CEP57", "11", 95801248, "G", "A", "rs117154762"),
    ("CEP57", "11", 95830582, "C", "T", "rs144598445"),
    ("TRIP13", "5", 902436, "A", "G", "rs142950691"),
    ("CENATAC", "11", 119014984, "T", "C", "rs190557381"),
    ("CENATAC", "11", 118995257, "G", "T", "rs190719613"),
    ("CENATAC", "11", 118995866, "C", "T", "rs137879106"),
    ("TUBGCP4", "15", 43395933, "T", "C", "novel"),
    ("TUBGCP6", "22", 50212759, "ACG", "A", "novel 3bp del"),
    ("TUBGCP6", "22", 50235009, "C", "T", "novel"),
    ("TUBGCP6", "22", 50221169, "C", "T", "rs149231425"),
    ("TUBGCP6", "22", 50227684, "C", "T", "rs188370549"),
    ("TUBGCP6", "22", 50229407, "G", "C", "rs199690816"),
    ("TUBGCP6", "22", 50247942, "C", "T", "rs34402301"),
    ("TUBGCP6", "22", 50244603, "A", "AT", "rs3841005"),
    ("TUBGCP6", "22", 50249226, "A", "AG", "rs3830749"),
]

GNOMAD_Q = """
query v($vid: String!) {
  variant(variantId: $vid, dataset: gnomad_r4) {
    variantId
    genome { ac an af }
    exome { ac an af }
  }
}
"""


def ensembl_batch(cands):
    variants = [f"{c} {p} . {r} {a} . . ." for _, c, p, r, a, _ in cands]
    body = json.dumps({"variants": variants}).encode()
    return fetch_json("https://rest.ensembl.org/vep/homo_sapiens/region", data=body,
                      cache_key="vep_batch_priority")


def gnomad(chrom, pos, ref, alt):
    vid = f"{chrom}-{pos}-{ref}-{alt}"
    try:
        res = fetch_json("https://gnomad.broadinstitute.org/api",
                         data=json.dumps({"query": GNOMAD_Q, "variables": {"vid": vid}}).encode(),
                         cache_key=f"gnomad_{vid}")
        return res.get("data", {}).get("variant")
    except Exception as e:
        return {"error": str(e)}


def main():
    vep = ensembl_batch(CANDS)
    vep_by = {}
    for entry in vep:
        vep_by[entry.get("input", "")] = entry
    rows = []
    for gene, chrom, pos, ref, alt, tag in CANDS:
        key = f"{chrom} {pos} . {ref} {alt} . . ."
        v = vep_by.get(key, {})
        if not v:
            for k, entry in vep_by.items():
                if k.startswith(f"{chrom} {pos} "):
                    v = entry
                    break
        cons = hgvsc = hgvsp = aa = ""
        for t in v.get("transcript_consequences", []):
            if t.get("gene_symbol") == gene:
                cons = ",".join(t.get("consequence_terms", []))
                hgvsc = t.get("hgvsc", "")
                hgvsp = t.get("hgvsp", "")
                aa = t.get("amino_acids", "")
                break
        freqs = []
        for cv in v.get("colocated_variants") or []:
            fq = cv.get("frequencies") or {}
            for allele, d in fq.items():
                if isinstance(d, dict):
                    g = d.get("gnomadg")
                    e = d.get("gnomade")
                    top = d.get("af")
                    parts = [x for x in (f"gnomadg={g}", f"gnomade={e}", f"af={top}") if "None" not in x]
                    if parts:
                        freqs.append(f"{allele}:" + ",".join(parts))
                else:
                    freqs.append(f"{allele}={d}")
        g = gnomad(chrom, pos, ref, alt)
        if g is None:
            gnote = "absent_from_gnomAD_r4"
        elif "error" in g:
            gnote = f"gnomAD_err:{g['error'][:80]}"
        else:
            gn, ex = g.get("genome") or {}, g.get("exome") or {}
            gnote = (f"AF={max(gn.get('af') or 0, ex.get('af') or 0):.3g} "
                     f"(g {gn.get('ac')}/{gn.get('an')} e {ex.get('ac')}/{ex.get('an')})")
        rows.append([gene, f"chr{chrom}", str(pos), ref, alt, tag, cons, hgvsc, hgvsp, aa,
                     ";".join(freqs), gnote])
    hdr = ["gene", "chrom", "pos", "ref", "alt", "tag", "vep_consequence", "hgvsc", "hgvsp",
           "amino_acids", "ensembl_freqs", "gnomad_r4"]
    with open("analysis/candidates/priority_annotated.tsv", "w") as f:
        f.write("\t".join(hdr) + "\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    print("\t".join(hdr))
    for r in rows:
        print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    main()
