# CAGI6/7 Rare Genomes Project — What Won, What Zeroes Scores (scout: CagiLessons, 2026-08-26)

Citation classes: **[J]** journal · **[P]** preprint · **[G]** GitHub · **[H]** HF · **[W]** web/challenge docs.

## 1. Challenge design (the scoring template this hackathon adapts)

**Primary:** Stenton SL, et al. *Critical assessment of variant prioritization methods for rare disease diagnosis within the rare genomes project.* Hum Genomics 18:44 (2024). https://link.springer.com/article/10.1186/s40246-024-00604-w (PMID 38685113; medrxiv preprint 10.1101/2023.08.02.23293212v1)

- 175 individuals / 65 families; ~30× GS, GRCh38, GATK joint-called SNV/indel VCFs (no SVs, no mtDNA). Training: 35 solved families; Test: 30 (14 solved + 16 unsolved, split secret). Solved variants deliberately NOT already P/LP in ClinVar/HGMD.
- Up to 100 ranked predictions/proband, 6 models/team, GRCh38 coordinates mandatory, EPCR 0–1; compound-het as `VAR;VAR` single lines.
- Rank points: top5=100, top10=50, top20=25, top50=10, top100=5, else 0 (mean across probands). F-max: sweep every unique EPCR threshold; max F-measure.
- **Hard rule: biallelic line pairing a correct variant with a NON-causal partner = 0.** CAGI7 added partial credit for one-of-two biallelic variants (this hackathon has it: half points).
- Outcome: 16 teams, 52 models; 90% of lines single variants; team concordance in top-5 = 0.09 (no consensus).

## 2. Who won and why

| Rank | Team | Result | Method essence |
|---|---|---|---|
| 1 | **Invitae Moon** (1 model) | 13/14 top-5, 9 at rank 1; #1 rank pts, #2 F-max | Automated commercial pipeline + curated "Apollo" gene-phenotype DB (daily literature scan, HPO + onset + inheritance + mechanism), gnomAD AF, effect preds, ClinVar + internal Invitae classifications; only literature-associated genes submitted; ~1 variant/proband at F-max threshold |
| 2 | **Lichtarge/Baylor** | 12/14, 9 at rank 1; #1 F-max | Evolutionary Action missense scoring + quality + AF + segregation; ranked by P(LoF) not phenotype; excluded splice (missed CLTC splice-acceptor) |
| 3 | **enGenome** | 10–12/14 | ML ensemble on 35-family training set; eVai ACMG pathogenicity + segregation + phenotype; gated on MedGen/DO/Orphanet disease-DB genes (missed KCND2/GNAI1 — not in DBs yet); **found the ASNS deep-intronic + frameshift comp-het — only team to submit the pair, rank 1** |
| 4 | TCS | 10–11/14 | VPR (MAF+conservation+deleteriousness+prior assoc) + PRIORI-T (HPO→gene network) + GPrio (STRING interactors) |
| 5 | **Exomiser** (open source, fully automated) | 9–12/14 | PASS-only, rare, coding; MAF + pathogenicity + phenotype similarity (human+mouse+STRING); non-coding via Genomiser |

**Winner pattern = all five pillars integrated:** (i) call quality DP/GQ/AB, (ii) gnomAD/TOPMed AF, (iii) deleteriousness, (iv) segregation/inheritance mode, (v) phenotype relevance. Plus openness to phenotype expansion, non-coding/splice, compound-het, incomplete/sex-limited penetrance. Curated proprietary knowledge gave an unquantifiable edge.

**Bonus outcomes:** 2/16 unsolved families diagnosed from predictions — both non-coding, RNA-seq-confirmed: *TCF4* c.1228+3G>T de novo (Pitt-Hopkins); *ASNS* frameshift + deep-intronic 6bp del comp-het (actionable: oral asparagine).

**Hardest:** KCND2 (gene not in OMIM), PI4KA (comp-het in duo), CLTC (non-coding splice acceptor), TUBB8 (in-cis paternal, sex-limited).

## 3. Pitfall list (what silently kills a score)

From CAGI6 assessment + cited literature:
1. **Wrong biallelic partner = zero.** Ground truth here IS a comp-het → submit the exact phased PAIR (use PGT/PID from the VCF), not LoF allele + random rare variant.
2. **Burying truth past rank thresholds** — rank decay is brutal; put best pair at rank 1 (9/13 Moon hits at rank 1).
3. **Filter-exclusion failures:** missense-only filtering lost splice acceptors; hard REVEL/MVP thresholds missed real variants; OMIM-only gene gating lost literature-only genes; ignoring non-coding lost ASNS/TCF4; ignoring penetrance lost TUBB8.
4. **Sequence artifacts** from not weighting DP/GQ/allele balance.
5. **Over-confident EPCR destroys F-max** — needs consistent separation of causal from non-causal. CAGI7 adds explicit EPCR-calibration scoring; assessors re-review only EPCR ≥ 0.1.
6. **Format errors:** assessors "corrected formatting" — risky; strict descending EPCR order, EPCR ∈ (0,1].
7. **Genome-build mismatches** GRCh37↔38 (He et al. AJHG 2021) — mixing AF sources across builds zeroes matches.
8. **Normalization:** bcftools norm -f GRCh38 + split multiallelics (`-m -any`); handle `*` alleles (Tan et al. Bioinformatics 2015; Lincoln et al. Genet Med 2021 — 1/7 pathogenic variants hard to detect).
9. **Metadata errata happen** (CAGI7 Dec 2025 erratum) — re-check challenge errata/discussions before final.

## 4. Code archaeology

- **No public CAGI6-RGP participant repos exist** (verified GitHub search 0 results) — winners were commercial/in-house.
- **Exomiser = only top-5 fully open-source reproducible:** github.com/exomiser/Exomiser; Jacobsen et al. Hum Mutat 2022; PhEval framework monarch-initiative.
- Adjacent: LIRICAL (AJHG 2020), Phen2Gene github.com/WGLab/Phen2Gene (live), AMELIE, Xrare (Genet Med 2019).
- HF: DeepRare LLM agent (HF papers/2506.20430); RareBench LLM benchmark + open RD dataset (HF datasets/johnfebry/RareBench, KDD 2024); cerebras/exome_bench; RARE-PHENIX (2602.20324).

## 5. Sibling-challenge evidence

- **CAGI7 RGP-VCF/CRAM** (closed Apr 2026, no assessment yet): DRAGEN-called, phenopackets, EPCR-calibration scoring, partial credit one-of-two biallelic. genomeinterpretation.org/cagi7-rgp-vcf.html
- **CAGI4/5 SickKids** (Kasak 2019 Hum Mutat): undiagnosed-by-clinic cohorts brutally hard.
- **100kG pilot** (Smedley NEJM 2021): 25% diagnostic yield; PanelApp tiering + Exomiser genome-wide; research/automated analyses contributed 14% (non-coding, SV, mtDNA).
- **Solve-RD reanalysis** (Laurie et al. Nat Med 2025, 10.1038/s41591-024-03420-w): 6,004 families reanalyzed → 12.6% new diagnoses; **15.9% of causal variants "beyond standard"** (CNVs incl. single-exon APC deletion, non-canonical splice ARID1A, mtDNA, RNU4-2, 13%-mosaic PIK3CA) — canonical argument for multi-variant-type reanalysis.
- **Tool benchmarks:** Tosco-Herrera 2022 (Exomiser best rank-1, LIRICAL best top-5, Xrare top-10; 8.2% causatives not capturable by WES); Fan 2022 ensemble (Exomiser+Xrare+DeepPVP 78% top-3 vs 63% single); Jacobsen 2022.
- No DREAM germline rare-disease variant challenge exists (negative finding).

## 6. Direct implications for this hackathon

1. Submit the **phased PAIR on one row** at **rank 1**; CAGI6's only recessive miss (PI4KA) = pair-submission failure; partial credit exists here as fallback.
2. Build the five pillars: quality, AF, deleteriousness, segregation (PGT/PID; parental-miscarriage signal), HPO phenotype match to CIN/MVA gene panel.
3. Moon-style manual curation beat pure ML — literature check on candidate genes pays.
4. EPCR honest, high-confidence top (~0.5–0.9), strictly descending, calibrated separation.
5. Normalize representation exactly to the provided VCF (GRCh38, left-aligned, split, no star alleles); chrom as `chrN` per template.
6. Parental recurrent abortions (HP:0200067) = segregation signal (gonadal mosaicism / meiotic nondisjunction carrier state) — use in gene-level reasoning.
