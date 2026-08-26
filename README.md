# Rare Disease, Real Kid: MVA Hackathon 2026 — Track 1 (Team bigbag)

Phenotype-anchored candidate-gene panel scan with evidence-ranked compound-heterozygote
prediction for the SageBio / MVA Society / Hugging Face / BEACON challenge
("Rare Disease, Real Kid: MVA Hackathon 2026"). Proband: PROBAND01 (male, MVA syndrome;
rhabdomyosarcoma, nephrocalcinosis, severe IUGR, FTT, prematurity 32 wk, parental recurrent abortions).

## Prediction (primary)

**BUB1B compound heterozygous pair (MVA1, OMIM 257300):**

| Allele | Locus (GRCh38) | HGVS (NM_001211.6) | Evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | ClinVar VCV000533901.9 Pathogenic/Likely pathogenic · gnomAD AF 7.9e-05 · het PASS AD 21/25 GQ 99 |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | gnomAD AF 6.8e-07 (singleton) · SIFT 0.01 · PolyPhen 0.997 · AlphaMissense 0.9229 · kinase domain (CDD cd14029) · het PASS AD 15/13 GQ 99 |

Matches the canonical MVA1 genotype class (truncating + kinase-domain hypomorphic missense;
Matsuura 2006; Rio Frio, NEJM 2010) and the proband's signature phenotype (embryonal RMS + universal IUGR).

## Repository layout

- `analysis/` — pipeline code:
  - `scan_panel2.py` — gene-panel variant extraction from the provided VCF (GENCODE spans, merged-interval bisect)
  - `annotate_panel.py` — local MANE-transcript consequence classifier (GTF + FASTA, VEP-REST cross-verified)
  - `af_lookup.py` + `netutil.py` — rate-limit-aware (429/Retry-After/backoff/cache) Ensembl VEP + gnomAD + ClinVar lookups
  - `baf_screen.py` — whole-genome BAF mosaic-aneuploidy screen (MoChA-substitute from the provided VCF)
  - `submission_sim.py` — submission format validator + score simulator (imports the challenge's own evaluator)
  - SpliceAI runner outputs in `analysis/candidates/spliceai_out.vcf`
- `analysis/candidates/` — derived candidate tables (no raw genomic data)
- `research/` — full methodology dossier: CAGI6/7 lessons, MVA gene-variant landscape
  (Malumbres 2024), tool landscape, re-analysis strategy, Track-2 drug-repurposing research,
  experiment plan + execution log, and the evidence chain for this prediction
  (`research/09_candidate_findings.md`).
- `challenge_src/` — reference copy of the public challenge Space source (scoring logic).

## Method summary

Five-pillar evidence (per CAGI6 RGP assessment, Stenton et al. 2024):
call quality (PASS, balanced AD, GQ 99) + population AF (gnomAD v4) + deleteriousness
(ClinVar / AlphaMissense / SIFT / PolyPhen / SpliceAI) + segregation logic (recessive
architecture; ~1000-fold AF divergence of the two alleles; PGT/PID trans-screen) +
phenotype match (MVA1 signature). Confounders screened: whole-genome BAF mosaic screen
(negative ≥~10% cell fraction), splice-disruption screen (SpliceAI D=1000, all candidates
≤0.03), competing panel candidates excluded by frequency (FANCD2/MCM7/TUBGCP6/CENATAC/CEP57).

## Data use

All genomic data are accessed under the hackathon's gated dataset terms and will be
deleted within 30 days of challenge close. No raw or individual-level data is included
in this repository.

## License

Analysis code and derived outputs: CC BY 4.0 (per hackathon submission terms).
