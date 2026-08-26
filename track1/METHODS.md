# Track 1 — Full Methods Record (for judging)

Team bigbag · Proband PROBAND01 · Result: **full match, 100.0 rank points, F-max 1.000** (2026-08-26 03:13 UTC)

## Pipeline (all code in `analysis/`, runs on a laptop)

1. **Phenotype → gene prior.** HPO terms from the clinical document matched to the curated MVA gene series (Malumbres & Villarroya-Beltri, Nat Rev Genet 2024: BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1, TUBGCP4/6) plus a wider 122-gene chromosomal-instability / RMS-predisposition / nephrocalcinosis panel. BUB1B was the only gene carrying both embryonal RMS and universal prenatal growth restriction as signature features with documented compound-heterozygous architecture.
2. **Exhaustive panel extraction** (`scan_panel2.py`): all variant classes (incl. intronic/synonymous/UTR) across full gene spans ±5 kb from the provided single-sample Sentieon VCF; GENCODE v44 spans; merged-interval bisect lookup; 11,835 non-ref alleles in 11 s.
3. **Local consequence annotation** (`annotate_panel.py`): MANE-transcript classifier (GTF + GRCh38 no-alt FASTA, pyfaidx) labeling stop-gain/frameshift/splice/missense; VEP-REST cross-verified on every final candidate (canonical ENST00000287598.11).
4. **Frequency + clinical status** (`af_lookup.py` + `netutil.py`): gnomAD v4, ClinVar, AlphaMissense with a rate-limit-aware client (429/Retry-After/backoff/jitter, response cache).
5. **Splice assessment**: SpliceAI 1.3.1, distance 1000, unmasked — all BUB1B candidates ≤0.03; the novel deep-intronic c.2679-1026A>G scored 0.00.
6. **Confounder screens**:
   - PGT/PID physical-phasing mining — 52 read-backed in-trans groups genome-wide in-panel, all common-variant clusters; no competing recessive pair.
   - Whole-genome BAF mosaic-aneuploidy screen (`baf_screen.py`, 2.89M het SNPs): all autosomes unimodal BAF≈0.5 → no blood-DNA whole-chromosome mosaicism ≥~10% cell fraction; male karyotype confirmed.
7. **Independent read-level verification**: fresh minimap2 2.31 (`-ax sr`) alignment of all four lanes to a chr15:40.05-40.28 Mb mini-reference (93.9M mapped reads); MAPQ≥20 pileup shows p.Leu737Ter at ~48% VAF (DP 46) and p.Asn1002Lys at ~52% VAF (DP 29) — exact match to the Sentieon genotype; no artifacts.
8. **Phasing evidence**: WhatsHap 2.x on the mini-locus BAM — the two coding alleles remain unlinkable (10.9 kb apart, 2×149 bp reads). Trans configuration is argued statistically (~1000-fold AF divergence of the two alleles; both parents unaffected; recessive disease in the proband). Direct proof requires parental genotypes or long-read sequencing.
9. **Submission calibration** (`submission_sim.py` imports the challenge's own evaluator): primary pair simulated at 100 pts + F-max 1.000 before upload; alternate-truth scenarios ≥50 pts. The submitted file matched the simulation exactly.

## Prediction (confirmed ground truth)

| Allele | Locus (GRCh38) | HGVS (NM_001211.6) | Evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | ClinVar VCV000533901.9 P/LP; gnomAD AF 7.9e-05 |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | gnomAD singleton (1/1.46M); SIFT 0.01; PolyPhen 0.997; AlphaMissense 0.9229; BubR1 kinase domain |

## Method-design rationale (CAGI lessons applied)

Five-pillar integration per the CAGI6 RGP assessment (Stenton et al. 2024): call quality + population AF + deleteriousness + segregation logic + phenotype match. We submitted the compound-het PAIR on row 1 (wrong-partner = zero in CAGI6), kept single-allele rows for CAGI7-style partial credit, flagged the incidental LZTR1 finding as `secondary`, and normalized representation exactly as the provided VCF (chrN, GRCh38, biallelic SNVs).
