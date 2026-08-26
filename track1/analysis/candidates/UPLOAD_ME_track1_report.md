# Track 1 Report. BUB1B Compound Heterozygous Pair

Team: bigbag. Date: 2026-08-26. Proband: PROBAND01.

This report uses Simplified Technical English. Each sentence holds one idea.

## 1. Task

The challenge supplies one genome and one phenotype table. The task is to find the two causal variants. The ground truth is a clinically validated compound heterozygous pair.

## 2. Phenotype

The proband has rhabdomyosarcoma (HP:0002859). He has nephrocalcinosis (HP:0000121). He has short stature (HP:0004322). He fails to thrive (HP:0001508). He has muscle atrophy (HP:0003202). He was born at 32 weeks (HP:0001622). His birth weight was about 1 kg (HP:0001518). His parents report recurrent pregnancy loss (HP:0200067).

This cluster indicates a recessive chromosomal instability disorder. The genes for Mosaic Variegated Aneuploidy (MVA) syndrome cause this cluster ([OMIM](https://omim.org/entry/257300); [Malumbres and Villarroya-Beltri](https://doi.org/10.1038/s41576-024-00762-6)). [Hanks et al.](https://doi.org/10.1038/ng1449) show that BUB1B causes MVA1. BUB1B has the strongest cancer signal and the strongest growth signal. Only BUB1B combines rhabdomyosarcoma with full prenatal growth failure.

## 3. Method

### 3.1 Gene panel

We build a 122-gene panel. The panel holds the MVA series from [Malumbres and Villarroya-Beltri](https://doi.org/10.1038/s41576-024-00762-6) (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1). It also holds gamma-tubulin genes (TUBGCP4, TUBGCP6). It also holds DNA damage genes, cancer predisposition genes, and renal calcium genes.

### 3.2 Variant extraction

We scan the full gene span plus 5 kb on both sides. We keep all variant classes. We keep intronic, synonymous, and UTR variants. We extract 11,835 non-reference alleles. The scan runs in 11 seconds on one CPU core set.

### 3.3 Consequence annotation

We write a local classifier. It uses MANE transcripts from GENCODE v44 and the GRCh38 reference FASTA. It labels stop-gain, frameshift, splice, and missense variants. We verify all final calls against the Ensembl Variant Effect Predictor (VEP) REST API. Both tools agree on all final calls.

### 3.4 Frequency and clinical status

We query the [Genome Aggregation Database](https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4) for each candidate allele. We query [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/) for each candidate allele. We query [AlphaMissense](https://doi.org/10.1126/science.adg7492) for each missense allele ([Cheng et al.](https://doi.org/10.1126/science.adg7492)). The client respects rate limits. The client retries on HTTP 429 and 5xx. It obeys Retry-After headers. It caches all responses.

### 3.5 Splice test

We run [SpliceAI](https://doi.org/10.1016/j.cell.2018.12.015) 1.3.1 on the BUB1B candidates ([Jaganathan et al.](https://doi.org/10.1016/j.cell.2018.12.015)). We set the distance window to 1000 base pairs. We disable masking. All scores stay at or below 0.03. No BUB1B candidate disrupts splicing.

### 3.6 Confounder screens

We use the PGT and PID phase tags in the VCF. We find 52 read-backed in-trans groups. All 52 groups hold common variants only. No second recessive pair exists in the panel.

We run a B-allele frequency screen over 2.89 million heterozygous SNPs. Every autosome shows one mode near 0.5. The screen finds no whole-chromosome mosaicism above about 10 percent of blood cells. The X chromosome heterozygote ratio confirms a male genome.

## 4. Prediction

We predict a BUB1B compound heterozygous pair.

| Allele | Locus (GRCh38) | HGVS | Key evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | Stop-gain. [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/) lists Pathogenic/Likely pathogenic (VCV000533901). [gnomAD](https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4) frequency is 7.9e-05. Genotype is heterozygous, PASS, allele depth 21/25, GQ 99. |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | Missense. The [Genome Aggregation Database](https://gnomad.broadinstitute.org/) holds one allele in 1.46 million exomes. SIFT scores 0.01. PolyPhen-2 scores 0.997. [AlphaMissense](https://doi.org/10.1126/science.adg7492) scores 0.9229 (likely pathogenic) ([Cheng et al.](https://doi.org/10.1126/science.adg7492)). The residue sits in the BubR1 kinase domain. Genotype is heterozygous, PASS, allele depth 15/13, GQ 99. |

## 5. Reasoning

The pair matches the published MVA1 architecture ([Hanks et al.](https://doi.org/10.1038/ng1449)). One allele stops the protein. One allele decreases kinase function. Published MVA1 cases carry this same class pair.

The two allele frequencies differ by about 1000-fold. This difference supports two independent origin events. An affected child then holds them in trans.

The phenotype fits. The usual BUB1B tumor is embryonal rhabdomyosarcoma ([Hanks et al.](https://doi.org/10.1038/ng1449); [Rio Frio et al.](https://doi.org/10.1056/NEJMoa1006565)). Severe prenatal growth failure occurs in all published BUB1B cases.

No other panel gene holds two rare damaging heterozygotes. We verify each rival against the [Genome Aggregation Database](https://gnomad.broadinstitute.org/). All rivals are common. FANCD2 candidates reach 0.45 frequency. The MCM7 stop allele reaches 0.27. All CEP57, CENATAC, and TUBGCP6 heterozygotes exceed 0.0008.

## 6. Reserve rows

Row 2 pairs p.Leu737Ter with a new deep-intronic variant (chr15:40216470 A>G, c.2679-1026A>G). The [Genome Aggregation Database](https://gnomad.broadinstitute.org/) does not hold this variant. [SpliceAI](https://doi.org/10.1016/j.cell.2018.12.015) gives it zero scores ([Jaganathan et al.](https://doi.org/10.1016/j.cell.2018.12.015)). Row 3 and row 4 hold each coding allele alone. These rows earn partial credit if only one allele is correct.

## 7. Secondary finding

LZTR1 chr22:20996720 C>G is a stop-gain variant. The [Genome Aggregation Database](https://gnomad.broadinstitute.org/) holds two alleles in 1.46 million exomes. We flag it as an incidental finding. It overlaps the RASopathy growth phenotype. We recommend clinical review.

## 8. Limitations

The dataset has no parent samples. Read-backed phasing cannot span the 10.9 kb between the two alleles with 2x149 bp reads. The trans argument is therefore statistical. A parental test or long-read sequencing can confirm the phase directly.

## 9. Reproducibility

Each step is a file in this repository. Paths are from the repository root. Click a path to open the file.

| Step | File | Writes |
|---|---|---|
| Gene panel (122 symbols) | [`track1/analysis/scan_panel.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/scan_panel.py) | `PANEL` used by the extractor |
| Panel extraction | [`track1/analysis/scan_panel2.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/scan_panel2.py) | [`track1/analysis/candidates/panel_variants.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/panel_variants.tsv) (11,835 alleles) |
| Consequence labels | [`track1/analysis/annotate_panel.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/annotate_panel.py) | [`track1/analysis/candidates/panel_annotated.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/panel_annotated.tsv) |
| gnomAD / ClinVar / VEP | [`track1/analysis/af_lookup.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/af_lookup.py), [`track1/analysis/netutil.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/netutil.py) | [`track1/analysis/candidates/priority_annotated.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/priority_annotated.tsv), [`gnomad_priority.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/gnomad_priority.tsv) |
| SpliceAI 1.3.1 | CLI on [`spliceai_input.vcf`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/spliceai_input.vcf) | [`spliceai_out.vcf`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/spliceai_out.vcf) |
| BAF mosaic screen | [`track1/analysis/baf_screen.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/baf_screen.py) | [`mosaic_baf_screen.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/candidates/mosaic_baf_screen.tsv), [`track1/figures/baf_deviation_per_chrom.png`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/figures/baf_deviation_per_chrom.png) |
| Score check | [`track1/analysis/submission_sim.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/submission_sim.py) imports [`track1/challenge_src/evaluation.py`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/challenge_src/evaluation.py) | format OK; 100 rank points and F-max 1.000 on the primary pair |
| Submitted CSV | [`track1/submissions/bigbag_bub1b-panel-scan-v1/predictions.csv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/submissions/bigbag_bub1b-panel-scan-v1/predictions.csv) | live score 100.0 / 1.000, full match |
| Genome-wide check | [`track1/analysis/exomiser/proband_analysis.yml`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/exomiser/proband_analysis.yml) | [`PROBAND01_genomewide.genes.tsv`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/analysis/exomiser/PROBAND01_genomewide.genes.tsv) |
| Depth at BUB1B | mosdepth on the mini-locus BAM (BAM not in git) | [`track1/figures/bub1b_depth_profile.png`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/figures/bub1b_depth_profile.png) |
| Full methods | [`track1/METHODS.md`](https://github.com/bigbag/mva-hackathon-2026/blob/main/track1/METHODS.md) | this report plus post-submission checks |

The input VCF and FASTQ stay outside git ([`.gitignore`](https://github.com/bigbag/mva-hackathon-2026/blob/main/.gitignore)). We delete all genomic data within 30 days after the challenge closes.

## Works Cited

Cheng, Jun, et al. "Accurate Proteome-Wide Missense Variant Effect Prediction with AlphaMissense." *Science*, vol. 381, no. 6664, 2023, eadg7492. [https://doi.org/10.1126/science.adg7492](https://doi.org/10.1126/science.adg7492).

ClinVar. "VCV000533901. NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter)." *ClinVar*, National Center for Biotechnology Information, [https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/).

Genome Aggregation Database. "15-40209701-T-G." *gnomAD*, version 4, Broad Institute, [https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4](https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4).

Hanks, Sandra, et al. "Constitutional Aneuploidy and Cancer Predisposition Caused by Biallelic Mutations in BUB1B." *Nature Genetics*, vol. 36, no. 11, 2004, pp. 1159-61. [https://doi.org/10.1038/ng1449](https://doi.org/10.1038/ng1449).

Jaganathan, Kishore, et al. "Predicting Splicing from Primary Sequence with Deep Learning." *Cell*, vol. 176, no. 3, 2019, pp. 535-48. [https://doi.org/10.1016/j.cell.2018.12.015](https://doi.org/10.1016/j.cell.2018.12.015).

Malumbres, Marcos, and Carolina Villarroya-Beltri. "Mosaic Variegated Aneuploidy in Development, Ageing and Cancer." *Nature Reviews Genetics*, vol. 25, no. 12, 2024, pp. 864-78. [https://doi.org/10.1038/s41576-024-00762-6](https://doi.org/10.1038/s41576-024-00762-6).

OMIM. "Mosaic Variegated Aneuploidy Syndrome 1; MVA1." *OMIM*, Johns Hopkins University, [https://omim.org/entry/257300](https://omim.org/entry/257300).

Rio Frio, Thomas, et al. "Homozygous BUB1B Mutation and Susceptibility to Gastrointestinal Neoplasia." *The New England Journal of Medicine*, vol. 363, no. 27, 2010, pp. 2628-37. [https://doi.org/10.1056/NEJMoa1006565](https://doi.org/10.1056/NEJMoa1006565).
