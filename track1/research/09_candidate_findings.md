# Candidate Findings — Track 1 (2026-08-26)

## PRIMARY CANDIDATE: BUB1B compound heterozygous pair (MVA1; OMIM 257300)

| | Allele 1 | Allele 2 |
|---|---|---|
| Locus (GRCh38) | chr15:40209701 T>G | chr15:40220612 T>G |
| HGVSc (ENST00000287598 / NM_001211.6) | c.2210T>G | c.3006T>G |
| HGVSp | **p.Leu737Ter** (nonsense) | **p.Asn1002Lys** (missense, kinase domain) |
| Genotype | 0/1, PASS, AD 21/25, DP 46, GQ 99 | 0/1, PASS, AD 15/13, DP 28, GQ 99 |
| gnomAD r4 AF | 7.87e-05 (exome 115/1,461,846; genome 5/152,174) | **6.84e-07 (singleton, 1/1,461,878)** |
| rsID | rs759242053 | none |
| ClinVar | **VCV000533901.9 — Pathogenic/Likely pathogenic** | absent (novel) |
| In-silico | — (PTC) | SIFT 0.01 · PolyPhen 0.997 · **AlphaMissense 0.9229 likely_pathogenic** · domain CDD cd14029 (BubR1 kinase), PANTHER PTHR14030 |

**Why this is the answer (evidence chain):**
1. Architecture = published BUB1B-MVA1 genotype class: truncating allele + hypomorphic missense (Matsuura 2006; Rio Frio 2010 NEJM; Malumbres 2024 NRG). p.Leu737Ter is a known P/LP MVA1 allele; N1002 lies in the kinase domain where pathogenic BUB1B missense hypomorphs cluster.
2. Phenotype: embryonal rhabdomyosarcoma + 100% prenatal growth restriction are the two BUB1B signature features (research/02 §2). Prematurity/FTT/muscle atrophy consistent; parental recurrent abortions = documented CIN-carrier reproductive signal.
3. Uniqueness: full 122-gene CIN/RMS/tubulopathy panel scan (11,835 variants, all classes incl. intronic) yields **no other** comp-het-consistent pair of two rare damaging hets in a recessive phenotype-matched gene (FANCD2 and MCM7 candidates proved common polymorphisms at AF 27–46%).
4. Both alleles PASS with balanced allele depths in the provided VCF; both simple SNVs (no representation ambiguity for submission).

**Caveats / open verification (do before submitting):**
- [ ] In-trans confirmation: variants 10.9 kb apart — PGT/PID physical phasing won't span; run WhatsHap on re-aligned BAM (E6/E7). Recessive interpretation requires trans; cis-only would imply a different second allele.
- [ ] SpliceAI on BUB1B c.2679-1026A>G (chr15:40216470, het, novel, ABSENT from gnomAD r4) — deep-intronic third candidate if it creates a cryptic acceptor (BUB1B precedent: c.2386-11A>G).
- [ ] ClinVar lit check for N1002K (AlphaMissense-only so far); HGMD not accessible.
- [ ] MoChA mosaic-aneuploidy readout as mechanistic corroboration (writeup).

## Hedge rows (ranked for submission rows 2-5)
| Rank | Variant | Class | Note |
|---|---|---|---|
| 2 | chr15:40209701 T>G **alone** | P/LP nonsense BUB1B | partial-credit insurance (one-of-two) |
| 3 | chr15:40216470 A>G alone (or paired with 40209701) | novel deep-intronic BUB1B, absent gnomAD | cryptic-splice possibility |
| 4 | BUB1B p.Leu737Ter + p.Asn1002Lys in swapped representation | — | not needed (simple SNVs); instead: TRIP13/CENATAC had NO rare damaging variants — skip |
| 4 | LZTR1 chr22:20996720 C>G p.?Ter (AF 1.4e-06, het) | secondary finding | Noonan-spectrum growth phenotype overlap; flag for clinical follow-up |

## Dead ends (checked, common)
FANCD2 rs73126218 AF 0.459 · novel-labeled del chr3:10046723 AF 0.447 · rs375350046 AF 0.447 · MCM7 rs2070215 stop_gained AF 0.267 · all TUBGCP6/CENATAC/CEP57 hets AF ≥ 8e-04 · BUB1 novel SNVs intronic (AF 5e-05/8e-05) and 8bp-del upstream AF 0.042.

## Artifacts
- `analysis/candidates/panel_variants.tsv` (11,835 alleles, 122 genes)
- `analysis/candidates/panel_annotated.tsv` (+ consequence via local MANE/GTF/FASTA classifier; VEP-REST cross-verified)
- `analysis/candidates/priority_annotated.tsv` (VEP + gnomAD + ClinVar for 26 candidates)
- `analysis/candidates/mosaic_baf_screen.tsv` (E3) · `spliceai_out.vcf` (E8) · `draft_submission_track1.csv` (validated)
- `analysis/candidates/.cache/` (API response cache; netutil rate-limit/backoff)
- AlphaMissense hg38 TSV at `resources/alphamissense_hg38.tsv.gz`

## Wave-1 verification results (2026-08-26)

| Exp | Result | Verdict |
|---|---|---|
| E2 PGT/PID in-trans | 52 in-trans PID groups across panel — **all common-variant clusters**; no alternative recessive pair with phase evidence; BUB1B pair has no PID link (10.9 kb apart) | No change; WhatsHap still needed for trans confirmation |
| E3 BAF mosaic screen (2.89M het SNPs) | All autosomes unimodal BAF≈0.5; **no detectable whole-chrom mosaic aneuploidy ≥~10% cell fraction in blood DNA**; X het:hom 0.07 → male confirmed; chr20/21/22 tail-elevation = mappability noise, no 0.33/0.67 modes | Negative (documented); MoChA HMM queued for segmental <5%; consistent with blood-DNA WGS vs stimulated-culture karyotype discrepancy in MVA (10-32% BUB1B) |
| E8 SpliceAI (D=1000, unmasked) | c.2679-1026A>G: **all delta scores 0.00** (nearest site 717 bp); p.Leu737Ter AG 0.03; p.Asn1002Lys max 0.02 | **Deep-intronic hedge DEAD** (splice-neutral); both primary alleles mechanism-confirmed (nonsense/missense); draft CSV revised (intronic demoted to 0.20 coverage row) |
