# Research Index — MVA Hackathon 2026 (SageBio Rare Disease, Real Kid)

Session: `2026-08-26-mva-hackathon-research`. Deliverable: deep & wide solution research (10 approaches).

## Files
| File | Content |
|---|---|
| `00_assessment.md` | Phase 0: exact scoring mechanics (evaluation.py), data inventory, phenotype, constraints, FASTQ facts (NovaSeq X 2×149, ~52× raw) |
| `01_cagi_lessons.md` | CAGI6/7 RGP: who won (Invitae Moon 13/14), why (5 pillars), silent-zero pitfalls, CAGI7 partial credit |
| `02_mva_genetics.md` | Corrected MVA1-7 gene map (Malumbres 2024), phenotype cross-match, variant classes, BUB1B best-match flag, nephrocalcinosis = no MVA association |
| `03_prioritization_tools.md` | Tool landscape: Exomiser 13/15 comp-het MOI, VEP+dbNSFP+AlphaMissense/SpliceAI, PGT/PID+WhatsHap, LLM benchmarks |
| `04_genome_reanalysis.md` | Re-analysis: MoChA on provided VCF, SV ensemble, CNV trio, MELT, DeepVariant CPU runtimes, Solve-RD "beyond standard" 15.9% |
| `05_drug_repurposing.md` | Track 2: OpenTargets/DGIdb/L1000(GEO)/matrix-scores pipeline; 3-tier hypotheses (adavosertib+irinotecan, alisertib, citrate+thiazide, everolimus, BubR1 restoration) |
| `06_arxiv_github_hf.md` | AI-native: DeepRare (Nature 2026), DAVP, AIVARI prompts, AI-MARRVEL, LA-MARRVEL; HF downloads (AlphaMissense TSV, PATHOS embeddings, Carbon, exome_bench) |
| `07_approaches.md` | **THE 10 APPROACHES, EV-ranked** (A1-A10) |
| `08_experiment_plan.md` | Phase 2/3 plan: E1-E10, waves, scoring strategy, risks, human gate |
| `09_candidate_findings.md` | **PRIMARY RESULT: BUB1B comp-het p.Leu737Ter (ClinVar P/LP) + p.Asn1002Lys (AM 0.9229, gnomAD singleton)** + hedges + dead ends |
| (file) | `analysis/candidates/draft_submission_track1.csv` — validated draft (sim: 100 pts + F-max 1.0 if primary correct) |
- `analysis/candidates/panel_variants.tsv` — all panel variants w/ GT/AD/DP/GQ/PID/PGT
- `analysis/af_lookup.py` + `analysis/netutil.py` — rate-limit-aware VEP batch + gnomAD GraphQL (backoff, Retry-After, cache)
- `analysis/candidates/priority_annotated.tsv` — priority candidates w/ consequence + AF + ClinVar
- `analysis/annotate_panel.py` — local GTF+FASTA consequence classifier (all 11.8k)
- `analysis/submission_sim.py` — submission format validator + score simulator (imports challenge evaluation.py)
- `challenge_src/` — full Space source (evaluation.py, groundtruth.py, rules, submission templates)

## Key strategic facts (compressed)
1. Ground truth = clinically validated **compound-heterozygous PAIR**; exact row = (chrN, pos, ref, alt)×2; chr format `chrN`.
2. Top row correct pair ⇒ 100 pts + F-max 1.0. Partial (one-of-two) ⇒ half tier points. 6 submissions, best kept — **live oracle**.
3. BUB1B = strongest prior (comp-het architecture + ERMS + 100% IUGR); BUB1 also live (novel het frameshift + 2 novel SNVs). Nephrocalcinosis unexplained by MVA genes → secondary or dual diagnosis.
4. Provided VCF has NO population frequencies and NO annotations; intronic variants must be splice-scored (BUB1B deep-intronic precedents).
5. PGT/PID phasing tags present — free in-trans comp-het evidence even GE Mira ignores.
6. MoChA runs directly on the provided VCF → mosaic aneuploidy karyotype-from-WGS (writeup gold; nobody in any benchmark has done this).
7. CAGI6 winner pattern: call quality + AF + deleteriousness + segregation + phenotype; curated knowledge beat pure ML.
8. LLM-alone loses to Exomiser (Reese 2026); classical-ranker + LLM-rerank wins (DeepRare 69.1% vs 55.9%).
9. SV/CNV/MEI layer insurance: Solve-RD 15.9% of re-solved variants beyond standard calling.
10. Track 2: 3-tier hypothesis structure + E1-E4 evidence grading + repoDB negative controls = judging-aligned writeup.
