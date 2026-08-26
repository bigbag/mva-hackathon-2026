#!/usr/bin/env python3
"""Extract all variants (incl. intronic) in a curated gene panel from the proband VCF.

Panel: MVA/CIN genes + rhabdomyosarcoma-predisposition + nephrocalcinosis/IUGR genes.
Output: analysis/candidates/panel_variants.tsv + per-gene counts.
"""
import gzip, json, os, sys, time
import urllib.request

VCF = "data/WGS_EX2312012_HGWCNDSX7.vcf.gz"
OUT_DIR = "analysis/candidates"
os.makedirs(OUT_DIR, exist_ok=True)

# Curated panel. MVA/CIN core first; then RMS/cancer predisposition; then renal-calc/IUGR.
PANEL = {
    # --- MVA / mosaic aneuploidy / mitotic checkpoint / centrosome ---
    "BUB1B": "MVA1; SAC checkpoint; RMS+Wilms+leukemia",
    "CEP57": "MVA2; centrosome; IUGR",
    "TRIP13": "MVA3; Wilms, gonadal dysgenesis",
    "CENATAC": "MVA/SNORD45 splicing; primordial dwarfism",
    "CCDC238": "alias CENATAC",
    "TUBGCP4": "MVA4; gamma-TuRC",
    "TUBGCP6": "MVA5; gamma-TuRC",
    "MAD1L1": "SAC; NDD with MVA",
    "MAD2L1": "SAC (mouse lethal; human?)",
    "MAD2L2": "REV7; SAC/TS",
    "BUB1": "SAC kinase",
    "BUB3": "SAC",
    "KIF2B": "chromokinesin",
    "SASS6": "centriole",
    "CEP63": "centriole",
    "CEP152": "centriole/MCPH",
    "PLK4": "centriole biogenesis",
    "CDK5RAP2": "MCPH centrosome",
    "PCNT": "MCPH/primordial dwarfism",
    "HAUS1": "augmin", "HAUS2": "augmin", "HAUS3": "augmin",
    "HAUS4": "augmin", "HAUS5": "augmin", "HAUS6": "augmin",
    "HAUS7": "augmin", "HAUS8": "augmin",
    "CEP44": "centrosome",
    # --- DNA damage response / Fanconi (RMS predisposition) ---
    "FANCA": "Fanconi", "FANCB": "Fanconi", "FANCC": "Fanconi", "FANCD2": "Fanconi",
    "FANCE": "Fanconi", "FANCF": "Fanconi", "FANCG": "Fanconi", "FANCI": "Fanconi",
    "FANCL": "Fanconi", "FANCM": "Fanconi",
    "BRCA2": "FANCD1; RMS predisposition", "BRCA1": "FANCS",
    "PALB2": "FANCN", "BRIP1": "FANCJ", "RAD51C": "FANCO", "SLX4": "FANCP",
    "RAD51": "FANCR", "XRCC2": "FANCU", "XRCC3": "RAD51 paralog",
    "ATM": "AT", "ATR": "ATR-Seckel-like", "NBN": "Nijmegen",
    "BLM": "Bloom", "WRN": "Werner", "RECQL4": "Rothmund-Thomson; RMS/osteosarcoma",
    # --- RMS / cancer predisposition syndromes ---
    "TP53": "Li-Fraumeni", "DICER1": "DICER1; renal/RMS",
    "NF1": "NF1; RMS", "HRAS": "Costello", "KRAS": "Noonan",
    "PTPN11": "Noonan; JMML", "RAF1": "Noonan", "BRAF": "CARD/Noonan",
    "SOS1": "Noonan", "SOS2": "Noonan", "LZTR1": "Noonan",
    "RIT1": "Noonan", "MAP2K1": "RASopathy", "MAP2K2": "RASopathy",
    "PTEN": "Cowden", "POT1": "glioma/RMS?", "TERF1": "DC",
    # --- nephrocalcinosis / renal calcium ---
    "CLCN5": "X-linked hypercalciuria", "SLC34A1": "hypophosphatemia; nephrocalcinosis",
    "SLC34A3": "HHRH; nephrocalcinosis", "CASR": "FHH/hypocalcemia",
    "VDR": "vitamin D resistant", "CYP24A1": "idiopathic infantile hypercalcemia",
    "SLC2A9": "hypouricemia", "SLC22A12": "hypouricemia",
    "ADCY10": "absorptive hypercalciuria", "SLC29A1": "ENT1; ectopic calcification",
    "CLDN16": "HHH; renal Mg wasting", "CLDN19": "HHH",
    "OCRL": "Lowe; renal Fanconi", "CTNS": "cystinosis",
    # --- endocrine/growth ---
    "GHR": "GH insensitivity", "IGF1": "IGF-1 def", "IGFALS": "ALS def",
    "STAT5B": "IGF dysregulation", "POLD1": "MDPL; lipodystrophy",
    "POU1F1": "CPHD", "PROP1": "CPHD",
    # --- replication stress / misc CIN ---
    "DONSON": "microcephaly/SMS-like", "FANCM2": None,
    "MCM2": "licensing", "MCM3": "licensing", "MCM4": "NKCD",
    "MCM5": "licensing", "MCM6": "licensing", "MCM7": "licensing",
    "GINS1": "licensing", "GINS2": "licensing", "GINS3": "licensing",
    "CDC45": "licensing", "CDC6": "licensing", "CDT1": "licensing",
    "ORC1": "MGS", "ORC2": "licensing", "ORC4": "MGS",
    "ESCO2": "SC phocomelia; mosaic variegated? no - Roberts",
    "SGO1": "cohesin/SAC", "SGO2": "cohesin/SAC",
    "STAG2": "cohesin; X-linked ID",
    "SMC1A": "cohesinopathy", "SMC3": "cohesinopathy", "NIPBL": "CdLS",
    "RAD21": "cohesinopathy", "HDAC8": "CdLS",
    "MRE11": "ATLD", "RAD50": "Nijmegen-like", "RBBP8": "Jawad",
    "CHEK2": "CHK2", "CHEK1": "CHK1", "RNF168": "RIDDLE",
    "RNF168B": None, "POLL": None, "MAD2L2BP": None,
}
PANEL = {k: v for k, v in PANEL.items() if v is not None and k != "FANCM2"}

def ensembl_get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json",
                                                       "Content-Type": "application/json"})
            with urllib.request.urlopen(req) as r:
                return json.load(r)
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(1 + 2 * i)

def get_gene_regions():
    """gene symbol -> (chrom_no_prefix, start, end), GRCh38, full gene span; cached."""
    cache_path = f"{OUT_DIR}/gene_regions.json"
    if os.path.exists(cache_path):
        return {k: tuple(v) for k, v in json.load(open(cache_path)).items()}
    regions = {}
    syms = list(PANEL)
    # bulk POST first (fast path)
    for i in range(0, len(syms), 50):
        chunk = {"symbols": syms[i:i+50]}
        try:
            req = urllib.request.Request(
                "https://rest.ensembl.org/lookup/symbol/homo_sapiens",
                data=json.dumps(chunk).encode(),
                headers={"Accept": "application/json", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.load(r)
            for sym, entry in res.items():
                if entry and entry.get("start"):
                    regions[sym] = [entry["seq_region_name"], entry["start"], entry["end"]]
        except Exception as e:
            print(f"bulk chunk failed ({e})", file=sys.stderr)
    # per-gene fallback for missing
    for sym in syms:
        if sym in regions:
            continue
        try:
            entry = ensembl_get(
                f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{sym}?expand=0")
            if entry and entry.get("start"):
                regions[sym] = [entry["seq_region_name"], entry["start"], entry["end"]]
            else:
                print(f"WARN: no Ensembl record for {sym}", file=sys.stderr)
        except Exception as e:
            print(f"WARN: {sym}: {e}", file=sys.stderr)
        time.sleep(0.35)
    json.dump(regions, open(cache_path, "w"))
    return {k: tuple(v) for k, v in regions.items()}

def main():
    regions = get_gene_regions()
    print(f"Resolved {len(regions)} genes")
    # index by chrom
    bychrom = {}
    for sym, (c, s, e) in regions.items():
        bychrom.setdefault(c, []).append((s, e, sym))
    # merge overlaps per chrom into sorted interval list with symbols
    hits = 0
    out = open(f"{OUT_DIR}/panel_variants.tsv", "w")
    out.write("\t".join(["gene", "chrom", "pos", "ref", "alt", "qual", "filter", "gt",
                         "ad_ref", "ad_alt", "dp", "gq", "pid", "pgt", "dbsnp", "info"]) + "\n")
    with gzip.open(VCF, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            chrom = parts[0]
            ivs = bychrom.get(chrom)
            if not ivs:
                continue
            pos = int(parts[1])
            # binary search via sorted starts — simple scan is fine w/ pre-check
            ref, alts = parts[3], parts[4].split(",")
            rec_syms = [sym for (s, e, sym) in ivs if s - 5000 <= pos <= e + 5000]
            if not rec_syms:
                continue
            fmt = parts[8].split(":")
            smp = parts[9].split(":")
            d = dict(zip(fmt, smp))
            gt = d.get("GT", "./.")
            if gt in ("0/0", "0|0", "./."):
                continue
            info = parts[7]
            filt = parts[6]
            dbsnp = parts[2]
            ad = d.get("AD", "").split(",")
            ad_ref = ad[0] if ad else ""
            for k, alt in enumerate(alts):
                if alt == "*":
                    continue
                ad_alt = ad[k + 1] if len(ad) > k + 1 else ""
                out.write("\t".join([",".join(rec_syms), f"chr{chrom}", parts[1], ref, alt,
                                     parts[5], filt, gt, ad_ref, ad_alt,
                                     d.get("DP", ""), d.get("GQ", ""),
                                     d.get("PID", ""), d.get("PGT", ""), dbsnp,
                                     info]) + "\n")
                hits += 1
    out.close()
    print(f"Wrote {hits} non-ref panel variant alleles -> {OUT_DIR}/panel_variants.tsv")

if __name__ == "__main__":
    main()
