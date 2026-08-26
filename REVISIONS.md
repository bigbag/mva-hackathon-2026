# Revision Log

## 2026-08-26 (post-submission verification — same day as S1)

The Track 1 prediction (`track1/submissions/bigbag_bub1b-panel-scan-v1/`) scored **100.0 rank points / F-max 1.000, full match at rank 1** (submitted 2026-08-26 03:13 UTC).

After the submission, we added deep-verification evidence to this repository:

1. **Genome-wide triangulation (Exomiser 15.1.0).** No gene panel, only the eight HPO terms, full 5.0M-variant VCF. Runtime 94 s. Result: BUB1B rank 1 (AD) and rank 2 (AR, phenotype score 0.813), OMIM:257300 matched. Contributing variants equal the submitted pair. Artifacts: `track1/analysis/exomiser/`.
2. **CNV exclusion at BUB1B.** MAPQ≥30 deduplicated mini-locus BAM + mosdepth: all exonic bins diploid 34-75×. Figure: `track1/figures/bub1b_depth_profile.png`.
3. **Bayesian phase assessment.** Prior trans:cis odds 1:1; posterior P(trans) = 0.989 after conditioning on affected status under the recessive model.
4. **ACMG SF v3.1 subset sweep.** No reportable secondary findings (all AF 4-46%).
5. **Independent read-level verification.** minimap2 re-alignment; allele fractions and depths match the provided VCF exactly.

The submission CSV is unchanged; this log documents verification work only. See `track1/METHODS.md` for the full integrated methods record.
