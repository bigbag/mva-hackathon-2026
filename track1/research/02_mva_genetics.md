# MVA Syndrome Genetics — Definitive Gene/Variant Landscape (scout: MvaGenetics, 2026-08-26)

Classes: [J] journal · [O] OMIM · [G] GitHub · [H] HF · [W] web.

## 1. Corrected OMIM gene map (authoritative: Malumbres & Villarroya-Beltri, Nat Rev Genet 2024, 10.1038/s41576-024-00762-6 + OMIM)

⚠️ Numbering correction: **MVA4 = CENATAC, MVA5/6 = SLF2/SMC5 ("Atelis syndrome"), MVA7 = MAD1L1**. TUBGCP4/6 are γ-TuRC MVA-*overlap* (microcephaly-chorioretinopathy), not OMIM-numbered MVA.

| Gene | MVA# | Inherit | Hallmarks | Cancer | Variant classes | ~Cases |
|---|---|---|---|---|---|---|
| **BUB1B** (BubR1) | MVA1 #257300 | AR | Severe pre/postnatal growth retardation (**100% IUGR**), microcephaly 93%, ID 72%, Dandy-Walker, eye, CHD, multicystic kidneys | **Embryonal RMS (4mo & 7y)**, Wilms <1y, leukemia/MDS 9y, neuroblastoma, adult GI | Missense hypomorphs, nonsense, frameshift, canonical splice, **deep intronic cryptic splice c.2386-11A>G, c.1402-5A>G**, 2025 upstream regulatory | ~22 |
| **CEP57** | MVA2 #614114 | AR | Milder growth retardation, rhizomelia, triangular face, CHD, hypothyroidism | **None ever** | Frameshift/nonsense, splice; **founder c.915_925dup11** (recurrent incl. homozygous); 25-50% aneuploid cells | ~16 |
| **TRIP13** | MVA3 #617598 | AR | Growth retardation, microcephaly, café-au-lait | **Wilms 1-5y** | Nonsense c.1060C>T, splice c.673-1G>C | ~6 |
| **CENATAC** (CCDC238) | MVA4 #620153 | AR | **Mildest MVA**: microcephaly, mild DD, maculopathy; adults 33/47y | None | Biallelic truncating; **both create novel splice sites**; 7-9% aneuploid blood; minor (U12) spliceosome AT-AN retention in ~100 genes | 2 sibs |
| **SLF2** | MVA5 #620184 | AR | Atelis 1: segmented chromosomes, hyperploidy, growth retardation | not established | biallelic LoF | few |
| **SMC5** | MVA6 #620185 | AR | Atelis 2 + near-tetraploidy/MVA (2025) | not established | biallelic LoF | few |
| **MAD1L1** | MVA7 #620189 | AR | Growth retardation, microcephaly, café-au-lait | **ERMS, Wilms**, +>10 other tumor types in 1 patient | comp-het missense c.196C>T + c.1882G>T; 30-40% aneuploid | 1 |
| **MAD2L1BP** (p31comet) | unnumbered | AR | Microcephaly, brain malformations | **Juvenile granulosa cell tumors (ovary AND testis, 11-14mo)** | Homozygous nonsense; 54-62% aneuploid | 3 |
| **CEP192** | unnumbered | AR | Microcephaly, DD, limb dysplasia; het = male infertility | None | comp-het missense; 26% aneuploid + 24% tetraploid | 2 |
| **BUB1** | unnumbered | AR | Microcephaly, ID, choanal stenosis; 35-40% aneuploid | Biallelic tumor-free (3y, 16y); **het = CRC risk 31-45y** | comp-het (start-loss, splice, frameshift), 1.7Mb del | 9 |
| **TUBGCP4** | overlap MCCRP | AR | Microcephaly + chorioretinopathy, IUGR | None | comp-het frameshift + **synonymous splice founder c.1746G>T (exon-16 skip)**, ex16-18 del | ~5 |
| **TUBGCP6** | overlap MCCRP1 | AR | Microcephaly + chorioretinopathy + primordial dwarfism, lissencephaly | None | Read-through X1820G (**Mennonite founder, 0.99% carrier**), comp-het nonsense+missense, **deep intronic c.2066-6A>G recurrent ≥3 families**, 405bp del WGS-only | ~15 |
| CDC20 | candidate only | — | premature ageing | DB alleles | missense | — |
| BUB3 | rejected | — | — | CRC het | — | — |

**No human germline MVA status:** KIF2B, PLK4 (MCCRP2 not MVA), SASS6, HAUS/augmin, CEP63, MAD2L2 (=FANCV).

## 2. Phenotype cross-match for OUR case

- **Rhabdomyosarcoma:** BUB1B (classic ERMS) [J: Kajii 2001 AJMG 104:57]; MAD1L1 (ERMS among >12 neoplasms). **No tumors ever for CEP57, CENATAC, CEP192.** Tumor rule: only SAC-component genes (BUB1B, BUB1, MAD1L1, TRIP13, MAD2L1BP) confer tumor risk; ERMS+Wilms dominate [Malumbres 2024].
- **Wilms:** BUB1B, TRIP13, MAD1L1.
- **Nephrocalcinosis: NO MVA gene has any published association** (verified, multiple searches). MVA renal findings: multicystic dysplastic kidney (BUB1B), cysts (CEP57), horseshoe (TUBGCP4), Wilms. → Treat as secondary to 32-wk prematurity/drugs, OR **dual molecular diagnosis** (tubulopathy genes: Bartter/CASR/CLCN5 — PanelApp "Nephrocalcinosis or nephrolithiasis" panel exists).
- **IUGR/SGA:** universal in MVA1-3; TUBGCP6/4.
- **Parental recurrent abortions in CIN:** Kuwaiti couple 14 miscarriages, both CEP57 carriers [Aljaser & Bahzad]; SAC-gene carrier screening in aneuploid fetal loss (Gorji 2025 PMC11865931); lethal affected sibs in PCS/MVA sibships (Kajii 2001); PCS trait 2-5% benign in population vs "total PCS" >50%.

## 3. Variant types causing MVA (what to look for in the VCF)

- **BUB1B dominant architecture = missense hypomorph + truncating/splice comp-het** (BubR1 dosage model) [Matsuura 2006].
- **Deep intronic cryptic splice REPEATEDLY PROVEN in BUB1B**: c.2386-11A>G (homozygous → adult GI cancer; Rio Frio 2010 NEJM 363:2628); comp-het c.1402-5A>G + c.2386-11A>G (Lin 2020); upstream regulatory (Qu 2025). **→ Sentieon dbSNP-only VCF will bury these: re-annotate ALL intronic/synonymous BUB1B variants + SpliceAI.**
- Synonymous-splice founders: TUBGCP4 c.1746G>T; CENATAC splice-site creators.
- TUBGCP6 deep intronic c.2066-6A>G recurrent.
- CNV/SV: BUB1 1.7Mb del; TUBGCP4 ex16-18 del; **TUBGCP6 405bp del + 11bp indel found ONLY by genome sequencing after exome missed them** [Pal 2024].
- **CEP57 copy-neutral inversion: NOT IN LITERATURE** (0 Europe PMC hits) — founder is c.915_925dup11. A copy-neutral SV ground truth would be novel vs published MVA → SV-aware re-analysis still warranted.
- No published Alu-insertion MVA case — check soft-clipped/discordant reads if panel is empty.

## 4. Diagnostics & yield

- Gold standard karyotype ≥2 tissues; aneuploid fractions: CEP57 25-50%, BUB1B 10-32%, TRIP13/MAD1L1 30-40%, CENATAC **7-9%** (may be missed), MAD2L1BP 54-62%, CEP192 26+24%.
- Pitfalls: aneuploid metaphases dismissed as artifacts (CEP57 case: 2 normal karyotype reports before WES); SNP-array detects NONE of the canonical MVA lesions.
- Interphase FISH = confirmatory; PCS assay (>50% = total PCS; 2-5% = benign carrier trait); prenatal dx published.
- **~50% of MVA molecularly unsolved after BUB1B/CEP57/TRIP13** [de Wolf 2021]; <100 total cases ever [Malumbres 2024]; 2025 case negative for all 7 genes + WES.

## 5. Frontier timeline

2021 CENATAC/MVA4 (minor spliceosome); 2022 MAD1L1/MVA7 (Sci Adv 8:eabq5914); 2022 SLF2/SMC5 Atelis; 2023 MAD2L1BP (JCI Insight 8:e170079); 2024 CEP192 (HGG Adv 5:100256), biallelic BUB1 (iPSC models, Ferreira 2024); 2025 BUB1B regulatory compound-het fetuses (Qu 2025); SMC5 tetraploidy (Yang 2025). **SNORD45–CENATAC link: NOT FOUND (0 hits) — distractor**; SNORD45 lit is oncology. PanelApp: BUB1B GREEN biallelic in "Familial rhabdomyosarcoma" panel 259.

## 6. Best-match flag for our case

**Primary: BUB1B (MVA1)** — only gene with all of: (a) documented comp-het architecture; (b) ERMS signature tumor; (c) 100% IUGR; (d) parental reproductive parallels. **Nephrocalcinosis unexplained by any MVA gene → secondary/prematurity or dual diagnosis (tubulopathy panel).** Secondary candidates: CEP57 (miscarriage signal, but NO cancer ever — conflicts with RMS), MAD1L1 (comp-het + ERMS, single published case), TRIP13 (if Wilms not RMS).

**Practical:** 10-gene core panel (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1 + TUBGCP4/6): biallelic/comp-het candidates with NO AF floor (founders up to ~0.1-1%); SpliceAI on all intronic/synonymous in these genes; PGT/PID phasing; Exomiser HPO screen; Manta/CNV callers on FASTQs.
