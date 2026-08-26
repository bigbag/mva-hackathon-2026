# Genome Re-Analysis Beyond the Provided VCF (scout: GenomeRewrite, 2026-08-26)

Classes: [J] journal · [P] preprint · [G] GitHub · [W] web. [est.] = extrapolated runtime.

## 1. Re-calling worth it?

| Caller | Gain vs Sentieon | 30x WGS CPU runtime | Single-sample |
|---|---|---|---|
| Sentieon (provided) | Reference: SNV/indel F1 ≈ GATK HC ≈ DeepVariant at 30x (Pei 2020) | — | ✓ |
| **DeepVariant 1.8-1.10 WGS** | **Indel F1 0.94 vs GATK 0.90**; robust low-coverage (Supernat 2018 Sci Rep 8:17851) | **~8.5-17.5 h @16 threads CPU** (issue #960: make_examples CPU-bound ~466 min; call_variants 43 min) | ✓ docker google/deepvariant |
| GATK HaplotypeCaller | none | ~1-2 days | ✓ |
| bcftools mpileup | orthogonal error model at CIN loci | ~1-2 h | ✓ |

**Verdict:** Sentieon≈DV≈GATK on SNVs; DV's edge = indels + borderline low-AF alleles (the CEP57 failure mode). One overnight DV run = priority BELOW SV/CNV/mosaic work. Alignment prerequisite bwa-mem2 ~4-8 h [est.].

## 2. Germline SV callers

| Caller | Catches | Runtime (30x) | Repo |
|---|---|---|---|
| **Manta 1.6** | DEL/DUP/INV/BND + large indels; HG002 P 0.947/R 0.771; best open-source F1 0.41 (14-tool Genome Biol 2026 benchmark) | slow ~32GB | Illumina/manta |
| DELLY 1.x | PE+SR; INV recall 0.55 | ~6-8 h | dellytools/delly |
| smoove (LUMPY) + duphold | best INS recall 0.58; fastest | fast | brentp/smoove |
| GRIDSS | assembly-based top precision (Cameron 2019) | heavy | PapenfussLab/gridss |
| Dysgu | ML SV; tied-best open recall; fast | fast | kcleal/dysgu |
| **CHONK** | **Mosaic somatic SV down to 1% AF** | pysam | daverbuj/CHONK |

Benchmarks (Guo 2026 Genome Biol, 14 tools): DRAGEN best overall (F1 0.51); Manta best open F1; **ensembles beat any single tool**; frequency filtering halves burden. HG002 per-type: INV recall only 0.38-0.55, INS as low as 0.21 — systematic short-read blind spots. Copy-neutral inversion precedent: Pagnamenta 2023 JMG 60:505; complex SV under-ascertained (Collins 2017 Genome Biol 18:36). ⚠️ "CEP57 2.2Mb Mennonite founder inversion" NOT verifiable — don't rely; the verified CEP57 precedent = caller-missed 11-bp dup (below).

## 3. Mobile elements & repeats

- **MELT v2.2.2** (Gardner 2017): non-ref Alu/L1/SVA incl. TSDs/transductions; ~12.6 CPU-min/genome; MELT-Single mode. MEIs ≈25% of human SVs; documented missed-disease class.
- **ExpansionHunter v5**: PCR-free WGS BAM; DRAGEN default ~60 pathogenic repeats; 174,293-STR catalog (Illumina/RepeatCatalogs); minutes-1h.
- STRaglr: long-read only — N/A.

## 4. Single-sample CNV

| Tool | Notes |
|---|---|
| **CNVnator/CNVpytor** | 1kb-Mb; 100% recall >1Mb syndromic; ~1-2h; github.com/abyzovlab/CNVpytor |
| Canvas | clinical-grade, in 100kGP pipeline |
| Control-FREEC | RD+BAF, control-free |
| GATK gCNV | **cohort ≥30 required — NOT practical for singleton** |
| ConanVarvar | 1-5Mb syndromic, few FPs |

Cross-evidence: RD callers found ALL large CNVs while **Manta missed >50% of >1Mb dups** — complementary layers required.

## 5. Mosaic aneuploidy from WGS (the MVA phenotype itself)

- **MoChA (`bcftools +mocha`, freeseek/mocha; Loh 2018 Nature 559:350)** — HMM over phased BAF+LRR **directly runnable on the provided VCF** (has PGT/PID + AD!). UKB 484,081×30x → 43,617 mCAs; 2× SNP-array sensitivity; focal dels to **~2% cell fraction** (Nat Genet 2026 s41588-026-02592-0). Minutes/sample [est.]. Also a "second-hit detector": interstitial mosaic losses can unmask a recessive allele.
- **MADSEQ** (Genome Res 2018, Bioconductor) — Bayesian normal/monosomy/trisomy/CN-LOH model **estimating aneuploid cell fraction f**; purpose-built for constitutional mosaic aneuploidy; needs ≥2,000 het sites/chromosome (met by 30x).
- ichorCNA (3% TF at 0.1x), WisecondorX (needs ≥50 controls — N/A), QDNAseq/HMMcopy quick plots.
- **Minimum detectable mosaic fraction at 30x:** chromosome-scale BAF/LRR ≈2-5%; focal dels ≈2%; PE/SR SV <10% undetectable; karyotype 5-10%. MVA blood karyotypes typically **25-50% aneuploid cells** (Snape 2011; OMIM 614114) — comfortably within MoChA/MADSEQ range.
- Cheapest first-line screen: per-chromosome BAF cluster drift (0.5→0.33/0.67 trisomy; →1.0/0.0 LOH).

## 7. Documented misses (why re-analysis wins cases)

1. **CEP57 founder paper itself** (Snape 2011 Nat Genet 43:527): the pathogenic c.915_925dup11 was in 30-40% of exome reads but **NOT CALLED** (insertion near read end → AF below threshold); rescued by Sanger. Ground truth here is a comp-het pair — a second allele of exactly this class could be invisible in the provided VCF → DV re-call + manual read review at CIN loci.
2. 100kGP pilot (NEJM 2021): 25% yield; **14% of diagnoses needed research approaches (noncoding, SV, mtDNA)**; pipeline included Canvas+Manta+ExpansionHunter.
3. Exomiser reanalysis 24,015 unsolved 100kGP (Vestito 2024 npj Genom Med 9:65): 2% new diagnoses from reinterpretation; **109/725 top candidates were IGV-visible false calls**.
4. 100kGP second-hit reanalysis (Genet Med Open 2024 10.1016/j.gimo.2024.101834): 8 AR cases solved by missed second hits — CFTR **LINE1 insertion discounted as misalignment**; 346kb RAB3GAP1 deletion **mosaic (~44%) in the father**; 16.5kb Alu-mediated ABCC6 del; ENPP1 complex dup (needed Bionano); deep-intronic CFTR c.3874-4522A>G; "synonymous" DYNC2H1 exon-skipping variant.
5. Non-canonical splicing (Genome Med 2022 14:79): 35 extra 100kGP diagnoses from near-splice/branchpoint variants.
6. SV blind spots: INV recall 0.38-0.55, INS 0.21 (sv-bench); Manta misses >50% >1Mb CNVs.

## 8. Ranked re-analysis shortlist for THIS case

1. **MoChA on provided phased VCF** — zero FASTQ cost; direct MVA readout (mosaic aneuploidy, CN-LOH, segmental events + fraction).
2. **SV ensemble Manta+smoove+Delly(±Dysgu)** on fresh bwa-mem2 BAM — ~6-8h each, parallel.
3. **RD CNV trio: CNVpytor + Canvas + Control-FREEC.**
4. **MELT** — MEI as missed second hit (~1h).
5. **MADSEQ** — quantify aneuploidy type/fraction.
6. **ExpansionHunter v5** + 174k catalog — minutes.
7. **DeepVariant WGS re-call** (overnight 8-18h) — defends vs CEP57-dup11-class misses.
8. bcftools mpileup at CIN loci — orthogonal.
9. Optional heavy: GATK-SV single-sample w/ public panel; CHONK for 1% mosaic SV.
10. **Always: IGV/Samplot at BUB1B/CEP57/TRIP13 regardless of caller output.**

Unverified flags: CEP57 2.2Mb founder inversion (unconfirmed); TICRR as MVA3 (not confirmed). HF: nothing relevant for SV domain — SOTA lives on GitHub/journals.
