# Experiment Plan — Ranked, Costed (Phase 2/3 synthesis, 2026-08-26)

Metric: **rank points** (100 max; tiers 100/50/25/10 at rank 1/≤3/≤5/≤10; half for one-of-two) + **F-max** (1.0 max). Budget: **6 Track-1 submissions** (best kept), 1 Track-2 submission. Deadline **2026-10-24 23:59 UTC** (~9 wks). Abort criteria: 3 consecutive dead ends without candidate-list change.

Hardware: 16 threads / 28 GB RAM / 2.1 TB disk, CPU-only. Downloads in progress: GRCh38 FASTA (~900MB), GENCODE v44 basic GTF (done, 29.6MB).

| # | Experiment | Hypothesis | Expected Δ | Cost | Screening | Depends |
|---|---|---|---|---|---|---|
| E1 | Panel scan + VEP/gnomAD annotation (`analysis/scan_panel2.py`, `af_lookup.py`) — DONE in draft; extend to all 11.8k panel variants | Causal comp-het pair sits in 122-gene CIN/RMS/tubulopathy panel; both alleles PASS hets | Base evidence; candidate list today | 2-3 h (API-paced) | yes | — |
| E2 | PGT/PID in-trans mining + PID-pair table (`analysis/scan_panel2.py` output has pid/pgt columns) | At least one gene shows two hets in-trans via physical phasing | Upgrades pair confidence; CAGI6 PI4KA lesson | 30 min | yes | E1 |
| E3 | MoChA (`bcftools +mocha`) on provided VCF + MADSEQ | MVA phenotype = detectable mosaic aneuploidy ≥2-5% cells in blood WGS | Writeup/mechanism evidence; possible 2nd-hit unmasking | 1-2 h install+run | yes | — |
| E4 | Local full-stack annotation of ALL 5.0M variants (VEP offline + dbNSFP; or REST batch chunks) + Exomiser AR-comp-het FULL mode | Truth may lie outside panel (50% of MVA unsolved after classic genes) | Catches panel misses; systematic net | 1-2 d (downloads ~70GB) | no | E1 shortlist |
| E5 | AI-MARRVEL web upload (VCF+HPO) + DeepRare second opinion | LLM-ensemble beats single classical ranker (NEJM AI 2024 doubled solved cases) | Independent candidate ranking cross-check | 1 h | yes | E4 (VCF+pheno bundle) |
| E6 | bwa-mem2 alignment (16 t) → SV ensemble (Manta+smoove+Delly) + CNVpytor + MELT + ExpansionHunter | Second allele is SV/MEI/STR invisible to SNV VCF (Solve-RD: 15.9% "beyond standard") | Insurance vs missed allele | 1.5-2 d wall | no | FASTA (done soon) |
| E7 | DeepVariant CPU re-call + diff at CIN loci + IGV/Samplot manual review | Sentieon missed borderline indel (CEP57 dup11 precedent) | Insurance vs miscall | overnight+2 h review | no | E6 BAM |
| E8 | Final-pair deep dive: SpliceAI-Lookup, AlphaMissense, ESM-1v, EVE, RaSP, GPN-MSA | Converts VUS→defensible; refines EPCR ordering | Ranking polish for submission | 2-4 h | yes | E1-E5 |
| E9 | Submission ladder (6 slots): S1 early best-pair → oracle feedback; S2-S3 refine; S4-S5 hedge rows; S6 final | Live scoring = free oracle; best-of-6 kept | Converts evidence → leaderboard score | 6 submissions over weeks | — | E1+ |
| E10 | Track-2: Open Targets→DGIdb→L1000(GEO)→matrix-scores→tiered hypotheses + report + video | Mechanism-first repurposing wins panel judging | 2nd competition entry | 3-5 d | no | gene fixed (E1/E4) |

## Sequencing (waves)

- **Wave 1 (today, VCF-only):** E1 → E2 → E3 in parallel. FASTA completes meanwhile.
- **Wave 2 (this week):** E4 downloads + Exomiser run; E5 uploads; E6 alignment overnight.
- **Wave 3 (week 2):** E6 callers; E7 re-call; E8 deep dive; **E9 S1 submission once a defensible pair exists.**
- **Wave 4 (weeks 3-8):** iterate E8/E9 with oracle feedback; E10 report+video; S6 final submission ≤ Oct 24.

## Scoring-strategy details (from evaluation.py analysis)

- Top row = the single best comp-het PAIR, epcr ~0.9 (exact pair ⇒ 100 pts + F-max 1.0).
- Rows 2-3 = alternate pairs (different genes/recessive models).
- Rows 4-5 = single-variant forms of top alleles (partial credit: half tier points).
- Last row(s) = secondary findings (finding_type=secondary; not auto-scored, judged qualitatively).
- Chrom format `chrN`; GRCh38; left-aligned biallelic (bcftools norm) — verify against provided VCF representation exactly.
- 6 submissions ladder: each returns rank points + F-max live → treat as oracle: if S1 pair scores partial (50 = one-of-two at rank 1), the partner variant is wrong → focus second-allele hunt (E6/E7).

## Risks & mitigations

- **Truth outside panel/CDS** → E4 genome-wide, E6 SV layer, splice-score all intronic panel variants.
- **Allele representation mismatch zeroes the match** → normalize exactly as the provided VCF; submit the pair also as singles in hedge rows.
- **API flakiness** (gnomAD 429, Ensembl 503) → `analysis/netutil.py` (backoff+cache); batch endpoints; local dbNSFP as final fallback.
- **LLM-API data rules unsettled** (Discussion #2) → send only de-identified variant-level data; track organizer answer.
- **Privacy** → no raw genomic data in public repo; only scripts + aggregated candidate tables minus identifiers per rules.

## HUMAN GATE
Plan approval: submissions are irreversible (6 max). Wave 1-3 work is free; first submission (E9/S1) should wait for explicit go-ahead with the candidate table reviewed.


## Execution log

| Exp | Status | Result | Artifact |
|---|---|---|---|
| E1 panel scan + annotation | **done** 2026-08-26 | PRIMARY PAIR: BUB1B p.Leu737Ter (ClinVar P/LP VCV000533901) + p.Asn1002Lys (AlphaMissense 0.9229, gnomAD singleton); all rivals common | `panel_annotated.tsv`, `priority_annotated.tsv`, `09_candidate_findings.md` |
| E2 PGT/PID in-trans | **done** | 52 in-trans groups, all common-variant clusters; no competing recessive pair | findings §Wave-1 |
| E3 BAF mosaic screen | **done** | Negative ≥~10% (blood DNA); male confirmed; MoChA HMM queued for segmental | `mosaic_baf_screen.tsv` |
| E8 SpliceAI + AlphaMissense | **done** | c.2679-1026A>G splice-neutral (hedge dead); N1002K AM 0.9229 LP; coding alleles mechanism-confirmed | `spliceai_out.vcf` |
| E9 draft ladder | **ready** | 5 rows validated: 100 pts + F1.0 primary; 50 pts alternate. **HUMAN GATE — awaiting review before S1 upload** | `draft_submission_track1.csv` |
| E4 Exomiser / E5 AI-MARRVEL / E6 alignment+SV+WhatsHap / E7 DeepVariant | pending | next wave; E6 includes in-trans WhatsHap confirmation of the pair | — |