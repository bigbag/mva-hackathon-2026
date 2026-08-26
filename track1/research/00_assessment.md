# Phase 0 — Task Assessment & Problem Decomposition

*Rare Disease, Real Kid: MVA Hackathon 2026* (Sage Bionetworks × MVA Society × Hugging Face × BEACON; $50k prizes).
Saved: 2026-08-26. Sources: challenge Space source (`challenge_src/`, fetched from HF Space repo), dataset README, clinical phenotype doc.

## 1. The task

Real clinical WGS case of a child with **Mosaic Variegated Aneuploidy (MVA) syndrome**. Two tracks:

- **Track 1 — Variant Prediction** (auto-scored). Predict the causal variant(s) from phenotype + WGS. Ground truth = **clinically validated (NHS) compound-heterozygous PAIR** (2 variants, recessive model). Scoring adapted from CAGI6 Rare Genomes Project Challenge (Stenton et al. 2024).
- **Track 2 — Drug Repurposing** (panel-judged). Report + GitHub + 3-min video. Criteria: Scientific Rigor 35%, Potential Impact 25%, Innovation 25%, Scalability 15%.

## 2. Optimization target (exact, from `evaluation.py`)

Submission CSV: `proband_id,chrom_1,pos_1,ref_1,alt_1,chrom_2,pos_2,ref_2,alt_2,epcr,finding_type,notes`; ≤10 rows; proband_id = `PROBAND01`.

**Metric 1 — Rank points.** Rows sorted by epcr desc. Full match = a row whose variant frozenset equals the 2-variant truth: rank 1 → **100 pts**, rank ≤3 → 50, ≤5 → 25, ≤10 → 10. Partial (row contains exactly one true variant) → **half** of the tier points at that row's rank.

**Metric 2 — F-max** (variant-level). Sweep thresholds over own epcr values; best F1 of predicted-variant-set vs 2-variant truth. If row 1 = the correct pair alone ⇒ precision 1, recall 1 ⇒ **F-max = 1.0**.

**Strategic consequences:**
1. A single correct compound-het row at rank 1 maxes both metrics. Everything else is hedge.
2. Hedging: additional rows with the same variants do NOT dilute F-max if epcr lower (threshold sweep protects), and partial-match credit requires the true variant to appear *in a row* (alone or wrong-paired).
3. Exact tuple match `(chrom_str, int(pos), ref, alt)` — **chrom format must be `chrN`** (fallback GT + instructions use `chr15` style; provided VCF uses bare `1` style → must convert). Representation must match truth: left-aligned, biallelic, no star alleles. VCF-standard normalization (bcftools norm) is the safest target.
4. epcr is only used for ordering + thresholds → relative calibration within own file matters, absolute values don't.
5. **6 submissions**, highest kept → can ladder strategies; zero cost to submit early.

## 3. Data inventory

| Item | Facts |
|---|---|
| Sample | `WGS_EX2312012` (single proband; no parents/trio) |
| FASTQ | 8 × paired-end, ~85 GB total, 4 lanes (L001–L004) |
| VCF | 5,012,204 records, GRCh38 (no-alt analysis set), tabix-indexed |
| Pipeline provenance | Sentieon 202308.02: BQSR → Haplotyper (GVCF) → GVCFtyper (dbSNP138); GATK VariantFiltration filters (QD2/MQ40/RPRS-8/FS60/MQRankSum-12.5) |
| Annotations present | **None external**: AC/AF/AN are sample-only; DB flag only; no gene annotation, no population frequencies |
| Phasing | FORMAT PGT/PID present (read-backed physical phasing blocks) |
| Missing (needs re-analysis) | SVs/CNVs, repeat expansions, MEIs, mosaic aneuploidy evidence, mitochondrial, pop-freq, functional annotation |

**Implication:** the VCF alone is not diagnosable without an annotation stack (VEP/ANNOVAR + gnomAD + effect predictors), or API-based annotation. FASTQs enable SV/CNV/aneuploidy re-calling (CPU-only, ~30x → feasible but hours).

## 4. Phenotype (proband, from `Challenge_Clinical_Phenotype_1.docx`)

Rhabdomyosarcoma (HP:0002859) · Nephrocalcinosis (HP:0000121) · Short stature (HP:0004322) · Failure to thrive (HP:0001508) · Skeletal muscle atrophy (HP:0003202) · Premature birth 32 wk (HP:0001622) · SGA/IUGR ~1 kg (HP:0001518) · **Parental recurrent spontaneous abortions (HP:0200067)**.

Organizer hints: "co-occurrence of cancer predisposition, growth restriction, renal anomalies, adverse perinatal history, parental reproductive loss" + "chromosomal instability disorders". ⇒ Prior: recessive CIN/MVA gene panel first (BUB1B, CEP57, TRIP13, CENATAC, TUBGCP4/6, MAD1L1, BUB1, …), but stay open to non-MVA mimics.

## 5. Constraints

- Deadline 2026-10-24 23:59 UTC; winners Nov 25. ~9 weeks.
- 6 Track-1 submissions / 1 Track-2 submission.
- Privacy: no recontact of family/MVA Society; no data resharing; delete within 30d post-close; outputs CC-BY. Public family blog = published boundary.
- Local compute: 16 threads, 28 GB RAM, 2.1 TB disk, AMD iGPU (no CUDA). Alignment/calling feasible but multi-hour; cloud optional.
- Submissions need public GitHub repo + methods report (template: `methods_description_form.xlsx` in Space).

## 6. Baseline & archaeology state

- No submissions made yet. Baseline = 0.
- Leaderboard dataset `SageBio/mva-hackathon-2026-leaderboard` — accessibility TBD (probe running).
- CAGI6 RGP writeups = prior art for what wins (scout in flight).
- Family/Society public communications (permitted boundary) may contain diagnostic hints — TBD ethically-inside-rules only.

## 7. Degrees of freedom

1. Annotation stack (VEP local vs REST APIs vs OpenCRAVAT cloud).
2. Phenotype→gene ranking (Exomiser/LIRICAL vs LLM-guided).
3. Comp-het inference (phase-by-gene, PGT/PID exploit, WhatsHap read-backed from re-aligned BAM).
4. Re-calling & SV/CNV/mosaic layer (DeepVariant-CPU?, Manta, CNVnator, BAF karyotype).
5. EPCR/ranking strategy (calibration ladder across 6 submissions).
6. Track-2 mechanism map + repurposing candidates.

## 8. Session log

- Session ID: `2026-08-26-mva-hackathon-research`
- 2026-08-26: Space source fetched; Phase 0 complete; 6 research scouts launched (MVA genetics, CAGI lessons, prioritization tools, genome re-analysis, drug repurposing, arXiv/GitHub/HF cross-cut). Local VCF candidate scan starting.
- 2026-08-26 (later): E1/E2 complete. **PRIMARY PAIR: BUB1B chr15:40209701 T>G p.Leu737Ter (ClinVar VCV000533901.9 P/LP, AF 7.9e-05) + chr15:40220612 T>G p.Asn1002Lys (gnomAD singleton, SIFT 0.01/PolyPhen 0.997/AlphaMissense 0.9229)** — classic MVA1 comp-het; phenotype match (ERMS+IUGR). Hedges: BUB1B c.2679-1026A>G (novel, absent gnomAD) as alt 2nd allele; LZTR1 ultra-rare nonsense secondary. Dead ends verified common (FANCD2 45%, MCM7 27%, TUBGCP6/CENATAC/CEP57). Draft submission validated vs challenge evaluator: 100 pts + F-max 1.0 primary; ≥50 alternates. **HUMAN GATE: no real submission until reviewed.** Next: WhatsHap trans-phase (E6), SpliceAI 40216470, MoChA (E3), Exomiser (E4), AI-MARRVEL (E5).
