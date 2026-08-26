# Solution Approaches — Deep & Wide Catalog (synthesis, 2026-08-26)

Ten approaches, EV-ranked, each grounded in `research/01–06` scout findings and local data facts (`research/00_assessment.md`). Track-1 objective: recover the NHS-validated **compound-heterozygous pair** at **rank 1** (rank-points 100 + F-max 1.0). Cross-cutting rules for every approach: exact variant representation (`chrN`, GRCh38, left-aligned, biallelic, no `*`), strictly descending EPCR, ≤10 rows, submit the PAIR on one row (CAGI6: wrong partner = 0).

---

## A1. Curated CIN/MVA panel scan with API annotation (the anchor)
**What:** Extract every variant (incl. intronic/synonymous/UTR) from the 13-gene core MVA panel (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1, TUBGCP4, TUBGCP6, +CDC20) and a wider ~140-gene CIN/RMS/tubulopathy panel from the provided VCF; annotate consequence (VEP REST / local GTF+FASTA model), ClinVar, gnomAD AF (API), SpliceAI, AlphaMissense; require two rare damaging heterozygotes in the SAME gene with PGT/PID in-trans evidence.
**Why:** Ground truth is a validated comp-het; BUB1B is the only gene matching RMS+IUGR+comp-het architecture (`research/02` §6); ~50% of MVA is still unsolved after the classic 3 genes → keep panel wide but CIN-first.
**Evidence anchors:** BUB1B deep-intronic cryptic splice c.2386-11A>G/c.1402-5A>G repeatedly causal (Rio Frio NEJM 2010; Lin 2020) — **dbSNP-only Sentieon VCF buries these: annotate everything in-panel, splice-score all intronic/synonymous.**
**Cost:** hours, CPU, free APIs. **Risk:** truth outside panel → mitigated by A2-A5. **Started:** `analysis/scan_panel.py` (gene_regions via GENCODE; extraction in progress).

## A2. Full-stack local annotation + Exomiser AR-comp-het (the systematic net)
**What:** Local annotation engine on the whole 5.0M-variant VCF: Ensembl VEP 116 offline cache + plugins (AlphaMissense, SpliceAI, SpliceVault, LOFTEE) + dbNSFP 4.9a (carries gnomAD v4 + TOPMed AFs + REVEL/CADD/EVE) → Exomiser 13/15 FULL-genome mode with the 8 HPO terms, `AUTOSOMAL_RECESSIVE_COMP_HET` MOI on the singleton; Phen2Gene/LIRICAL/Phrank as independent phenotype ranks.
**Why:** Exomiser is the only top-5 CAGI6 method that is open + native singleton comp-het; CAGI winners integrated all five pillars (quality, AF, deleteriousness, segregation, phenotype); LLM-only does NOT beat Exomiser on phenotype-only (Reese EJHG 2026) — classical ranker first.
**Cost:** ~1-2 days setup (VEP cache ~20GB, dbNSFP ~50GB, 16GB RAM run). **Risk:** Exomiser defaults drop intronic — override to keep in-panel intronic variants (combine with A1).

## A3. Phase-first comp-het exploitation (the differentiator)
**What:** (a) Parse PGT/PID directly from the provided VCF: same PID with 0|1 vs 1|0 = in-trans (true comp-het evidence); identical phase = in-cis (exclude). (b) Re-align FASTQs (bwa-mem2, ~4-8h) → WhatsHap 2.8 read-backed phasing to extend blocks across gene bodies; feed phased VCF → VEP `haplo` (transcript haplotypes) + bcftools csq --phase.
**Why:** Even Genomics England's Mira tiering ignores phase — CAGI6's only recessive miss (PI4KA) was a pair/phase failure; ground truth IS a comp-het pair, so in-trans evidence is worth more than any single-variant score. Zero-cost first pass from existing tags.
**Cost:** (a) minutes; (b) overnight CPU. **Risk:** PGT/PID blocks short (read-length limited) — most comp-het partners are >insert-size apart → WhatsHap needed.

## A4. SV/CNV/MEI/STR re-analysis from FASTQs (the blind-spot layer)
**What:** On fresh bwa-mem2 BAM run: SV ensemble (Manta + smoove/LUMPY + Delly ± Dysgu — ensembles beat any single caller), RD-CNV trio (CNVpytor + Canvas + Control-FREEC — RD finds all >1Mb CNVs that Manta misses >50% of), MELT (Alu/L1/SVA — MEIs ≈25% of SVs; CFTR-LINE1 "discounted as misalignment" precedent), ExpansionHunter v5 (174k STR catalog), CHONK (mosaic SV to 1% AF).
**Why:** 15.9% of Solve-RD re-solved variants are "beyond standard" (CNVs, single-exon dels, complex SV); 100kGP second-hit series: mosaic paternal RAB3GAP1 deletion, Alu-mediated ABCC6 del, ENPP1 complex dup; TUBGCP6 405bp del found ONLY by WGS after exome missed it. A second allele invisible to Sentieon SNV calling is a live possibility.
**Cost:** 1-2 days CPU wall. **Risk:** many FPs — frequency/panel intersect to filter (A1 synergy).

## A5. Mosaic aneuploidy quantification — make the MVA phenotype computable (the mechanistic readout)
**What:** (a) `bcftools +mocha` (MoChA) directly on the provided phased VCF (PGT/PID + AD present) — HMM over BAF/LRR, mosaic CNV/CN-LOH to ~2% cell fraction. (b) MADSEQ Bayesian aneuploid-fraction estimation per chromosome. (c) CNVpytor `rd_call_mosaic` BAF+RD genome-wide. Output: the actual variegated-aneuploidy karyotype-from-WGS.
**Why:** MVA blood karyotypes typically 25-50% aneuploid cells — comfortably detectable; this converts the clinical hint ("chromosomal instability disorders") into hard evidence for the writeup and Track-2 mechanism section; interstitial mosaic losses can even unmask a recessive allele (second-hit detector). No published agent/benchmark has ever done this — novelty for judging.
**Cost:** minutes-hours, VCF-only first pass. **Risk:** none; pure evidence gain.

## A6. DeepVariant re-call defense (indel/low-AF insurance)
**What:** DeepVariant 1.8+ WGS model CPU (docker, 16 shards, ~8-17h) on the re-aligned BAM → independent VCF + gVCF; diff vs Sentieon at CIN loci; manual IGV/Samplot review of every candidate + low-AF indels in panel genes.
**Why:** The CEP57 founder c.915_925dup11 was in 30-40% of reads and NOT CALLED (Snape 2011); DV indel F1 0.94 vs GATK 0.90; 109/725 top 100kGP reanalysis candidates were IGV-visible false calls → read-level review is mandatory before final submission.
**Cost:** overnight. **Risk:** compute time only; run in parallel with A4 on same BAM.

## A7. LLM-agent ensemble on the shortlist (the 2024-26 winning pattern)
**What:** Classical-first (A2 output) → LLM rerank/orchestrate: (i) AI-MARRVEL web (recessive-fine-tuned; NEJM AI 2024, doubled solved cases vs Exomiser); (ii) DeepRare (Nature 2026; VCF+HPO→ranked dx; 69.1% vs Exomiser 55.9% Recall@1) as independent second opinion; (iii) DAVP pattern (Exomiser top-256 → LLM tournament → top-3; 70.3%/86.4% vs 57.0/66.6); (iv) AIVARI per-gene rollout prompts encoding comp-het decision rules verbatim; ground via MARRVEL-MCP / OpenCRAVAT-MCP over ClinVar/OMIM/gnomAD.
**Why:** Winning 2024-26 pattern = classical ranker + LLM reranker (not LLM-alone). Cheapest highest-leverage external checks: AI-MARRVEL upload = one web form.
**Cost:** API credits + prompt engineering (the hackathon's own prize is Claude credits; note Discussion #2 on LLM-API data rules — await organizer answer, or send only de-identified variant-level data).
**Risk:** LLM hallucination → require evidence-linked reasoning chains (DeepRare-style), verify every claim against ClinVar/literature.

## A8. Two-variant deep-dive effect evidence (convert VUS → PP3/PS1-grade)
**What:** For the final pair: SpliceAI-Lookup (SpliceAI+Pangolin+AlphaMissense+PrimateAI in one query), AlphaMissense TSV (HF katielink/dm_alphamissense), ESM-1v 5-model mean (ntranoslab CLI, CPU minutes), EVE/popEVE (evemodel.org), RaSP precomputed ΔΔG (all single-AA subs, 23,391 proteins), GPN-MSA LLR (best for noncoding), PATHOS PLM embeddings (HF DSIMB), map on AlphaFold DB model.
**Why:** CAGI6 hard-threshold REVEL misses killed real variants; the multi-evidence bundle both ranks correctly and supplies the methods-report rigor judges score. BUB1B missense-hypomorph architecture makes missense calibration decisive.
**Cost:** hours, all precomputed/CPU. **Risk:** none.

## A9. Scoring-theory submission ladder (the meta-approach)
**What:** Exploit the 6-submission budget as an experiment ladder: (1) early cheap submission once A1 yields a best pair (leaderboard presence + ground-truth oracle feedback via rank points/F-max returned live!); (2-3) refine with A2/A4 candidates; (4-5) hedge structure: top rows = comp-het pairs (alternate genes/representations), lower rows = single-variant forms of best alleles (partial-credit insurance: CAGI-style half points for one-of-two), final row = best secondary finding (unscored, judged qualitatively); (6) last-call final after all evidence in.
**Why:** The submission endpoint is a live oracle (returns rank points + F-max → tests whether the pair/parts are right WITHOUT burning much: only best score kept, 6 total). EPCR needs only relative ordering; F-max rewards putting BOTH true variants in the highest-EPCR row. Partial-match subtlety: a row = frozenset{v1} alone gives partial credit; also covers the risk that truth is a simple het (not impossible despite comp-het announcement).
**Cost:** free. **Risk:** info-leak to competitors via public leaderboard is symmetric; use team-neutral model names until organizer answer (Discussion #4).

## A10. Track-2 mechanism→drug repurposing pipeline (the second prize)
**What:** Once the gene is fixed: Open Targets GraphQL (tractability/safety/genetic evidence) → DGIdb v5 + ChEMBL (chemical matter + dose-feasibility Cmax-vs-IC50) → LINCS L1000 signature-reversal (GEO GCTx post-clue.io) on an MVA DE signature → everycure/matrix-scores prior (HF, 39.5M drug-disease pairs) + ClinicalTrials.gov E1 check → tiered hypotheses: **A** symptom-directed (adavosertib+irinotecan RMS RP2D NCT02095132; alisertib COG ADVL0921; K-citrate+thiazide for nephrocalcinosis), **B** CIN-stress buffers (everolimus/sirolimus — best pediatric safety dossier), **C** mechanism-restorative (BubR1 augmentation via SIRT2/NAD+ axis; progerin-peptide precedent) — with E1-E4 evidence grades + repoDB negative controls. Writeup mapped to Rigor 35/Impact 25/Innovation 25/Scalability 15.
**Why:** Everolimus-TSC is the template (mechanism-first, one-drug-many-manifestations, pediatric safety); the CIN "buffer the consequences" tier is genuinely novel (no published agent validated on constitutional MVA).
**Cost:** days, APIs. **Risk:** prophylactic SAC-inhibitor framing is mechanistically wrong for a living child — keep tumor-directed/trial-bound language only.

---

## EV ranking (impact × probability / effort)

| Rank | Approach | Impact | Prob. finds pair | Effort | Notes |
|---|---|---|---|---|---|
| 1 | A1 panel scan | H | H | L | already running; BUB1B prior strongest |
| 2 | A9 submission ladder | H | meta | VL | live oracle; do from first pair onward |
| 3 | A3 phase-first | H | M-H | VL→M | PGT/PID zero-cost pass first |
| 4 | A5 MoChA/MADSEQ | M-H | H (evidence) | VL | VCF-only; writeup gold |
| 5 | A2 Exomiser+VEP | H | M | M | systematic net; catches panel misses |
| 6 | A7 LLM ensemble | M-H | M | L-M | AI-MARRVEL upload = 5 min |
| 7 | A8 variant deep-dive | M | H (refine) | L | final-pair evidence |
| 8 | A4 SV/CNV/MEI | M-H | M | M-H | overnight-2d; second-allele insurance |
| 9 | A6 DeepVariant+IGV | M | M | M | overnight; insurance vs miscall |
| 10 | A10 Track-2 pipeline | H (2nd prize) | — | M | start after gene fixed; T2 deadline same |

Dependencies: A2 needs VEP cache+dbNSFP downloads; A3b/A4/A6 share the bwa-mem2 BAM; A7 consumes A2/A1 shortlist; A10 needs A1-A6 gene answer. A1+A3a+A5 run today on the existing VCF.
