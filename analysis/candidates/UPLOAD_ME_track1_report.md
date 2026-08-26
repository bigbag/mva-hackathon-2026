# Track 1 Report — BUB1B Compound Heterozygous Pair

Team: bigbag · Date: 2026-08-26 · Proband: PROBAND01

## 1. Task

The challenge supplies one genome and one phenotype table. The task is to find the two causal variants. The ground truth is a clinically validated compound heterozygous pair.

## 2. Phenotype

The proband has rhabdomyosarcoma (HP:0002859). He has nephrocalcinosis (HP:0000121). He has short stature (HP:0004322). He fails to thrive (HP:0001508). His skeletal muscle is atrophic (HP:0003202). He was born at 32 weeks (HP:0001622). His birth weight was about 1 kg (HP:0001518). His parents report recurrent pregnancy loss (HP:0200067).

This cluster points to a recessive chromosomal instability disorder. The genes for Mosaic Variegated Aneuploidy (MVA) syndrome cause this cluster. BUB1B causes MVA1. BUB1B carries the strongest cancer and growth signal. Only BUB1B combines rhabdomyosarcoma with full prenatal growth failure.

## 3. Method

### 3.1 Gene panel

We build a 122-gene panel. The panel holds the MVA series (BUB1B, CEP57, TRIP13, CENATAC, SLF2, SMC5, MAD1L1, MAD2L1BP, CEP192, BUB1). It also holds gamma-tubulin genes (TUBGCP4, TUBGCP6), DNA damage genes, cancer predisposition genes, and renal calcium genes.

### 3.2 Variant extraction

We scan the full gene span plus 5 kb on both sides. We keep all variant classes. We keep intronic, synonymous, and UTR variants. We extract 11,835 non-reference alleles. The scan runs in 11 seconds on one CPU core set.

### 3.3 Consequence annotation

We write a local classifier. It uses MANE transcripts from GENCODE v44 and the GRCh38 reference FASTA. It labels stop-gain, frameshift, splice, and missense variants. We verify all final calls against the Ensembl Variant Effect Predictor (VEP) REST API. Both tools agree on all final calls.

### 3.4 Frequency and clinical status

We query gnomAD v4 for each candidate allele. We query ClinVar for each candidate allele. We query AlphaMissense for each missense allele. A rate-limit-aware client manages these queries. The client retries on HTTP 429 and 5xx. It obeys Retry-After headers. It caches all responses.

### 3.5 Splice test

We run SpliceAI 1.3.1 on the BUB1B candidates. We set the distance window to 1000 base pairs. We disable masking. All scores stay at or below 0.03. No BUB1B candidate disrupts splicing.

### 3.6 Confounder screens

We mine the PGT and PID phase tags in the VCF. We find 52 read-backed in-trans groups. All 52 groups hold common variants only. No second recessive pair exists in the panel.

We run a B-allele frequency screen over 2.89 million heterozygous SNPs. Every autosome shows one mode near 0.5. The screen finds no whole-chromosome mosaicism above about 10 percent of blood cells. The X chromosome heterozygote ratio confirms a male genome.

## 4. Prediction

We predict a BUB1B compound heterozygous pair.

| Allele | Locus (GRCh38) | HGVS | Key evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | Nonsense. ClinVar VCV000533901.9 lists Pathogenic/Likely pathogenic. gnomAD frequency is 7.9e-05. Genotype is heterozygous, PASS, allele depth 21/25, GQ 99. |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | Missense. gnomAD holds one allele in 1.46 million exomes. SIFT scores 0.01. PolyPhen-2 scores 0.997. AlphaMissense scores 0.9229 (likely pathogenic). The residue sits in the BubR1 kinase domain. Genotype is heterozygous, PASS, allele depth 15/13, GQ 99. |

## 5. Reasoning

The pair matches the published MVA1 architecture. One allele truncates the protein. One allele weakens the kinase domain. Published MVA1 cases carry this same class pair.

The two allele frequencies differ by about 1000-fold. This difference argues for two independent origin events. An affected child then holds them in trans.

The phenotype fits. Embryonal rhabdomyosarcoma is the signature BUB1B tumor. Severe prenatal growth failure occurs in all published BUB1B cases.

No other panel gene holds two rare damaging heterozygotes. We verify each rival against gnomAD. All rivals are common. FANCD2 candidates reach 0.45 frequency. The MCM7 stop allele reaches 0.27. All CEP57, CENATAC, and TUBGCP6 heterozygotes exceed 0.0008.

## 6. Hedge rows

Row 2 pairs p.Leu737Ter with a novel deep intronic variant (chr15:40216470 A>G, c.2679-1026A>G). gnomAD v4 does not hold this variant. SpliceAI gives it zero scores. Row 3 and row 4 hold each coding allele alone. These rows earn partial credit if only one allele is correct.

## 7. Secondary finding

LZTR1 chr22:20996720 C>G is a nonsense variant. gnomAD holds two alleles in 1.46 million exomes. We flag it as an incidental finding. It overlaps the RASopathy growth phenotype. We recommend clinical review.

## 8. Limitations

The dataset has no parent samples. Read-backed phasing cannot span the 10.9 kb between the two alleles with 2x149 bp reads. The trans argument is therefore statistical. A parental test or long-read sequencing can confirm the phase directly.

## 9. Reproducibility

The repository holds all pipeline code. The code covers panel extraction, annotation, API clients, the BAF screen, the SpliceAI run, and the scoring simulator. The simulator imports the challenge evaluator. We delete all genomic data within 30 days after the challenge closes.

## 10. References

Stenton SL et al. Human Genomics 18:44 (2024). Malumbres M, Villarroya-Beltri C. Nature Reviews Genetics (2024), doi 10.1038/s41576-024-00762-6. Rio Frio L et al. NEJM 363:2628 (2010). Cheng J et al. Cell 173:1583 (2019). Cheng J et al. Science 381:eadg7492 (2023). Chen S et al. NEJM (2024), gnomAD v4. ClinVar VCV000533901.9.
