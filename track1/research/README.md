# Research dossier — Track 1 (pre-submission)

Session `2026-08-26-mva-hackathon-research`. This folder is the design record that led to the panel scan. The executed pipeline and live score live one directory up: [`../README.md`](../README.md), [`../METHODS.md`](../METHODS.md).

Track 2 writeup moved to [`../../track2/`](../../track2/README.md). `05_drug_repurposing.md` is the earlier research note, not the submission.

## Files

| File | Content |
|---|---|
| [`00_assessment.md`](00_assessment.md) | Scoring mechanics, data inventory, phenotype, FASTQ facts |
| [`01_cagi_lessons.md`](01_cagi_lessons.md) | CAGI6/7 RGP lessons ([Stenton](https://gregorconsortium.org/node/120)) |
| [`02_mva_genetics.md`](02_mva_genetics.md) | MVA gene map ([Malumbres and Villarroya-Beltri](https://doi.org/10.1038/s41576-024-00762-6)) |
| [`03_prioritization_tools.md`](03_prioritization_tools.md) | Exomiser, VEP, SpliceAI, phasing tools |
| [`04_genome_reanalysis.md`](04_genome_reanalysis.md) | Mosaic BAF, SV/CNV, re-analysis options |
| [`05_drug_repurposing.md`](05_drug_repurposing.md) | Early Track 2 notes (superseded by [`../../track2/report.md`](../../track2/report.md)) |
| [`06_arxiv_github_hf.md`](06_arxiv_github_hf.md) | External models and public datasets |
| [`07_approaches.md`](07_approaches.md) | Ten ranked approaches |
| [`08_experiment_plan.md`](08_experiment_plan.md) | Experiment waves E1–E10 |
| [`09_candidate_findings.md`](09_candidate_findings.md) | Primary BUB1B pair and rejected rivals |
| [`SUBMIT.md`](SUBMIT.md) | Upload checklist |

Derived tables from those experiments are in [`../analysis/candidates/`](../analysis/candidates/), not in this folder.

## What this dossier got right

1. Ground truth is a compound-heterozygous pair in `chrN` GRCh38 form.
2. Top-row correct pair → 100 rank points and F-max 1.0. That is what uploaded.
3. BUB1B was the strongest prior (truncation + kinase missense; embryonal RMS + IUGR).
4. The provided VCF has no AF and no consequence; those had to be added ([`../analysis/af_lookup.py`](../analysis/af_lookup.py)).
5. PGT/PID tags and a VCF-only BAF screen were worth running ([`../analysis/baf_screen.py`](../analysis/baf_screen.py)).
6. Curated five-pillar ranking beat a gene-agnostic first pass; Exomiser later confirmed the same pair ([`../analysis/exomiser/`](../analysis/exomiser/)).
