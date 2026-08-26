# Track 1. Full Methods Record

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

## Post-submission deep verification (2026-08-26)

### A. Genome-wide triangulation without the panel (Exomiser 15.1.0)

We ran Exomiser genome-wide on the full 5.0M-variant VCF with only the eight HPO terms (hiPhive, PASS_ONLY, no gene panel). Runtime: 94 seconds.

- **Rank 1: BUB1B (combined 0.650); Rank 2: BUB1B AR (0.550, phenotype score 0.813).** OMIM:257300 matched, including `Premature birth -> Premature chromatid separation` and `Rhabdomyosarcoma -> Embryonal rhabdomyosarcoma`.
- The contributing variants are exactly our pair: `15-40209701-T-G` (ClinVar whitelist) and `15-40220612-T-G` (variant score 0.85).
- Rank 3: FANCD2 — the common-polymorphism cluster our scan already excluded (AF 0.45). Rank 11: LZTR1 — our flagged secondary finding, independently surfaced.

Three independent approaches converge: curated-panel reasoning, phenotype-driven genome-wide prioritisation, and clinical databases. Artifacts: `analysis/exomiser/`.

### B. Copy-number and mappability at BUB1B (mosdepth, MAPQ>=30 dedup mini-BAM)

All BUB1B exonic bins sit in the diploid 34-75x band; depth spikes map to repeat elements only (figure `figures/bub1b_depth_profile.png`). No exon-level or whole-gene CNV exists. Both causal alleles sit in uniquely mappable sequence; the two SNVs are the complete allelic story.

### C. Bayesian phase assessment (trans vs cis)

Under linkage equilibrium at the observed allele frequencies, prior odds of trans vs cis are 1:1 — "independent origins imply trans" is wrong on its own. Conditioning on the proband's affected status under a recessive model (penetrance ratio 0.9 : 0.01) gives **posterior P(trans) = 0.989**. The phenotype, not the frequencies, carries the phase information. Read-backed phasing cannot span the 10.9 kb gap (WhatsHap-verified unlinked); parental genotypes or long reads would close it.

### D. Secondary findings sweep (ACMG SF v3.1 subset)

All damaging hets in the 15 SF-panel genes we cover are common polymorphisms (AF 4-46%: rs6180, rs1801195, rs1346044, rs766173, rs1799944). No reportable ACMG secondary finding. The LZTR1 ultra-rare nonsense remains the only incidental flag.

### E. Figures

- `figures/baf_deviation_per_chrom.png`. Whole-genome BAF deviation. No aneuploidy mode shift. 2.89 million heterozygous SNPs.
- `figures/bub1b_depth_profile.png`. BUB1B locus depth. Exons sit in the diploid band. Depth spikes map to repeat elements.

## Works Cited

Chen, Siwei, et al. "A Genomic Mutational Constraint Map Using Variation in 76,156 Human Genomes." *Nature*, vol. 625, 2024. https://doi.org/10.1038/s41586-023-06045-0. https://pubmed.ncbi.nlm.nih.gov/38057664/.

Cheng, Jun, et al. "Accurate Proteome-Wide Missense Variant Effect Prediction with AlphaMissense." *Science*, vol. 381, no. 6664, 2023, eadg7492. https://doi.org/10.1126/science.adg7492. https://pubmed.ncbi.nlm.nih.gov/37733863/.

ClinVar. "VCV000533901." NCBI, https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/.

Hanks, Sandra, et al. "Constitutional Aneuploidy and Cancer Predisposition Caused by Biallelic Mutations in BUB1B." *Nature Genetics*, vol. 36, no. 11, 2004, pp. 1159-61. https://doi.org/10.1038/ng1449. https://pubmed.ncbi.nlm.nih.gov/15475955/.

Jaganathan, Kishore, et al. "Predicting Splicing from Primary Sequence with Deep Learning." *Cell*, vol. 176, no. 3, 2019, pp. 535-48. https://doi.org/10.1016/j.cell.2018.12.015. https://pubmed.ncbi.nlm.nih.gov/30661751/.

Malumbres, Marcos, and Carolina Villarroya-Beltri. "Mosaic Variegated Aneuploidy in Development, Ageing and Cancer." *Nature Reviews Genetics*, vol. 25, 2024, pp. 864-78. https://doi.org/10.1038/s41576-024-00762-6. https://pubmed.ncbi.nlm.nih.gov/39169218/.

Rio Frio, Thomas, et al. "Homozygous BUB1B Mutation and Susceptibility to Gastrointestinal Neoplasia." *The New England Journal of Medicine*, vol. 363, no. 27, 2010, pp. 2628-37. https://doi.org/10.1056/NEJMoa1006565. https://pubmed.ncbi.nlm.nih.gov/21190457/.

Sage Bionetworks. "mva-hackathon-2026-data." *Hugging Face Datasets*, 2026, https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data.

Sage Bionetworks. "Rare Disease, Real Kid: MVA Hackathon 2026." *Hugging Face Spaces*, 2026, https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/.

Stenton, Sarah L. "Performance of Diagnostic Methods in Identifying Disease-Causing Variants: Assessment of the Rare Genomes Project CAGI Challenge." GREGoR Consortium / ASHG, 2022, https://gregorconsortium.org/node/120.

Yost, Shawn, et al. "Biallelic TRIP13 Mutations Predispose to Wilms Tumor and Chromosome Missegregation." *Nature Genetics*, vol. 49, no. 7, 2017, pp. 1148-51. https://doi.org/10.1038/ng.3883. https://pubmed.ncbi.nlm.nih.gov/28553959/.
