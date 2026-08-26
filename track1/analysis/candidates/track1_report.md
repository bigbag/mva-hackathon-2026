# Track 1 Report. BUB1B Compound Heterozygous Pair

Team: bigbag. Date: 2026-08-26. Proband: PROBAND01.

This report uses Simplified Technical English. Each sentence holds one idea.

## 1. Task

The challenge supplies one genome and one phenotype table. The task is to find the two causal variants. The ground truth is a clinically validated compound heterozygous pair.

## 2. Phenotype

The proband has rhabdomyosarcoma (HP:0002859). He has nephrocalcinosis (HP:0000121). He has short stature (HP:0004322). He fails to thrive (HP:0001508). He has muscle atrophy (HP:0003202). He was born at 32 weeks (HP:0001622). His birth weight was about 1 kg (HP:0001518). His parents report recurrent pregnancy loss (HP:0200067).

This cluster indicates a recessive chromosomal instability disorder. The genes for Mosaic Variegated Aneuploidy (MVA) syndrome cause this cluster. BUB1B causes MVA1. BUB1B has the strongest cancer signal and the strongest growth signal. Only BUB1B combines rhabdomyosarcoma with full prenatal growth failure.

## 3. Method

### 3.1 Gene panel

We build a 122-gene panel. The panel holds the MVA series (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1). It also holds gamma-tubulin genes (TUBGCP4, TUBGCP6). It also holds DNA damage genes, cancer predisposition genes, and renal calcium genes.

### 3.2 Variant extraction

We scan the full gene span plus 5 kb on both sides. We keep all variant classes. We keep intronic, synonymous, and UTR variants. We extract 11,835 non-reference alleles. The scan runs in 11 seconds on one CPU core set.

### 3.3 Consequence annotation

We write a local classifier. It uses MANE transcripts from GENCODE v44 and the GRCh38 reference FASTA. It labels stop-gain, frameshift, splice, and missense variants. We verify all final calls against the Ensembl Variant Effect Predictor (VEP) REST API. Both tools agree on all final calls.

### 3.4 Frequency and clinical status

We query gnomAD v4 for each candidate allele. We query ClinVar for each candidate allele. We query AlphaMissense for each missense allele. The client respects rate limits. The client retries on HTTP 429 and 5xx. It obeys Retry-After headers. It caches all responses.

### 3.5 Splice test

We run SpliceAI 1.3.1 on the BUB1B candidates. We set the distance window to 1000 base pairs. We disable masking. All scores stay at or below 0.03. No BUB1B candidate disrupts splicing.

### 3.6 Confounder screens

We use the PGT and PID phase tags in the VCF. We find 52 read-backed in-trans groups. All 52 groups hold common variants only. No second recessive pair exists in the panel.

We run a B-allele frequency screen over 2.89 million heterozygous SNPs. Every autosome shows one mode near 0.5. The screen finds no whole-chromosome mosaicism above about 10 percent of blood cells. The X chromosome heterozygote ratio confirms a male genome.

## 4. Prediction

We predict a BUB1B compound heterozygous pair.

| Allele | Locus (GRCh38) | HGVS | Key evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | Stop-gain. ClinVar VCV000533901.9 lists Pathogenic/Likely pathogenic. gnomAD frequency is 7.9e-05. Genotype is heterozygous, PASS, allele depth 21/25, GQ 99. |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | Missense. gnomAD holds one allele in 1.46 million exomes. SIFT scores 0.01. PolyPhen-2 scores 0.997. AlphaMissense scores 0.9229 (likely pathogenic). The residue sits in the BubR1 kinase domain. Genotype is heterozygous, PASS, allele depth 15/13, GQ 99. |

## 5. Reasoning

The pair matches the published MVA1 architecture. One allele stops the protein. One allele decreases kinase function. Published MVA1 cases carry this same class pair.

The two allele frequencies differ by about 1000-fold. This difference supports two independent origin events. An affected child then holds them in trans.

The phenotype fits. The usual BUB1B tumor is embryonal rhabdomyosarcoma. Severe prenatal growth failure occurs in all published BUB1B cases.

No other panel gene holds two rare damaging heterozygotes. We verify each rival against gnomAD. All rivals are common. FANCD2 candidates reach 0.45 frequency. The MCM7 stop allele reaches 0.27. All CEP57, CENATAC, and TUBGCP6 heterozygotes exceed 0.0008.

## 6. Reserve rows

Row 2 pairs p.Leu737Ter with a new deep-intronic variant (chr15:40216470 A>G, c.2679-1026A>G). gnomAD v4 does not hold this variant. SpliceAI gives it zero scores. Row 3 and row 4 hold each coding allele alone. These rows earn partial credit if only one allele is correct.

## 7. Secondary finding

LZTR1 chr22:20996720 C>G is a stop-gain variant. gnomAD holds two alleles in 1.46 million exomes. We flag it as an incidental finding. It overlaps the RASopathy growth phenotype. We recommend clinical review.

## 8. Limitations

The dataset has no parent samples. Read-backed phasing cannot span the 10.9 kb between the two alleles with 2x149 bp reads. The trans argument is therefore statistical. A parental test or long-read sequencing can confirm the phase directly.

## 9. Reproducibility

The repository holds all pipeline code. The code covers panel extraction, annotation, API clients, the BAF screen, the SpliceAI run, and the scoring simulator. The simulator imports the challenge evaluator. We delete all genomic data within 30 days after the challenge closes.

## Works Cited

Chen, Siwei, et al. "A Genomic Mutational Constraint Map Using Variation in 76,156 Human Genomes." *Nature*, vol. 625, 2024. https://doi.org/10.1038/s41586-023-06045-0. https://pubmed.ncbi.nlm.nih.gov/38057664/.

Cheng, Jun, et al. "Accurate Proteome-Wide Missense Variant Effect Prediction with AlphaMissense." *Science*, vol. 381, no. 6664, 2023, eadg7492. https://doi.org/10.1126/science.adg7492. https://pubmed.ncbi.nlm.nih.gov/37733863/.

ClinVar. "VCV000533901. NM_001211.6(BUB1B):c.2210T>G (p.Leu737Ter)." NCBI, https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/.

gnomAD. "15-40209701-T-G." *Genome Aggregation Database*, v4, https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4.

Hanks, Sandra, et al. "Constitutional Aneuploidy and Cancer Predisposition Caused by Biallelic Mutations in BUB1B." *Nature Genetics*, vol. 36, no. 11, 2004, pp. 1159-61. https://doi.org/10.1038/ng1449. https://pubmed.ncbi.nlm.nih.gov/15475955/.

Jaganathan, Kishore, et al. "Predicting Splicing from Primary Sequence with Deep Learning." *Cell*, vol. 176, no. 3, 2019, pp. 535-48. https://doi.org/10.1016/j.cell.2018.12.015. https://pubmed.ncbi.nlm.nih.gov/30661751/.

Malumbres, Marcos, and Carolina Villarroya-Beltri. "Mosaic Variegated Aneuploidy in Development, Ageing and Cancer." *Nature Reviews Genetics*, vol. 25, 2024, pp. 864-78. https://doi.org/10.1038/s41576-024-00762-6. https://pubmed.ncbi.nlm.nih.gov/39169218/.

OMIM. "257300. Mosaic Variegated Aneuploidy Syndrome 1; MVA1." https://omim.org/entry/257300.

Rio Frio, Thomas, et al. "Homozygous BUB1B Mutation and Susceptibility to Gastrointestinal Neoplasia." *The New England Journal of Medicine*, vol. 363, no. 27, 2010, pp. 2628-37. https://doi.org/10.1056/NEJMoa1006565. https://pubmed.ncbi.nlm.nih.gov/21190457/.

Sage Bionetworks. "mva-hackathon-2026-data." *Hugging Face Datasets*, 2026, https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data.

Sage Bionetworks. "Rare Disease, Real Kid: MVA Hackathon 2026." *Hugging Face Spaces*, 2026, https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/.

Stenton, Sarah L. "Performance of Diagnostic Methods in Identifying Disease-Causing Variants: Assessment of the Rare Genomes Project CAGI Challenge." GREGoR Consortium / ASHG, 2022, https://gregorconsortium.org/node/120.

UniProt Consortium. "BUB1B_HUMAN (O60566)." https://www.uniprot.org/uniprotkb/O60566/entry.

Yost, Shawn, et al. "Biallelic TRIP13 Mutations Predispose to Wilms Tumor and Chromosome Missegregation." *Nature Genetics*, vol. 49, no. 7, 2017, pp. 1148-51. https://doi.org/10.1038/ng.3883. https://pubmed.ncbi.nlm.nih.gov/28553959/.
