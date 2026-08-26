# Submission S1 — bub1b-panel-scan-v1 (2026-08-26)

Model: phenotype-anchored 122-gene CIN/MVA panel scan; evidence-ranked compound-het ladder.

| Row | Prediction | EPCR | Type |
|---|---|---|---|
| 1 | chr15:40209701 T>G + chr15:40220612 T>G (BUB1B p.Leu737Ter + p.Asn1002Lys) | 0.90 | primary |
| 2 | chr15:40209701 T>G + chr15:40216470 A>G (alt second allele) | 0.55 | primary |
| 3 | chr15:40209701 T>G alone | 0.45 | primary |
| 4 | chr15:40220612 T>G alone | 0.35 | primary |
| 5 | chr22:20996720 C>G (LZTR1 nonsense) | 0.10 | secondary |

Simulated vs challenge evaluator: 100 pts + F-max 1.000 (primary truth); 50 pts (alt-truth).
Live result: PENDING — fill after upload (rank points / F-max / match type).

## LIVE RESULT (2026-08-26 03:13 UTC)
- **Rank points: 100.0 · F-max: 1.000 · FULL MATCH at rank 1**
- Ground truth confirmed: BUB1B chr15:40209701 T>G (p.Leu737Ter) + chr15:40220612 T>G (p.Asn1002Lys)
- Independent verification: minimap2 re-alignment, MAPQ>=20 pileup shows both alleles at ~50% VAF, depths match VCF (46/29) — no call artifacts.
- Track 1 leaderboard saturated: 11 teams at 100/1.000 (all BUB1B comp-het). Placement now decided by methods judging + Track 2.

## WhatsHap read-backed phasing (2026-08-26)
- Independent alignment: minimap2 2.31 -ax sr, 4 lanes, 93.9M mapped reads on chr15:40.05-40.28Mb mini-ref.
- Pileup at MAPQ>=20: p.Leu737Ter VAF ~48% (DP 46), p.Asn1002Lys VAF ~52% (DP 29) — matches Sentieon VCF exactly; no artifacts.
- WhatsHap 2.x phasing: all six BUB1B variants remain unphased relative to each other — no read spans the 10.9 kb between the two coding alleles (2x149bp reads). Trans confirmation requires parental genotypes or long-read sequencing. Recessive-consistent interpretation (independent AFs, affected status) stands.
