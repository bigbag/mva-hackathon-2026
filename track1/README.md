# Track 1 — Variant prediction (team bigbag)

Phenotype-anchored 122-gene panel scan for
[Rare Disease, Real Kid: MVA Hackathon 2026](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/).
Proband PROBAND01. Live score **100.0 rank points, F-max 1.000, full match** (2026-08-26 03:13 UTC).

Full methods: [`METHODS.md`](METHODS.md).
Written report: [`analysis/candidates/track1_report.md`](analysis/candidates/track1_report.md).
Uploaded packet: [`submissions/bigbag_bub1b-panel-scan-v1/`](submissions/bigbag_bub1b-panel-scan-v1/).

## Prediction

**BUB1B compound heterozygous pair** ([OMIM 257300](https://omim.org/entry/257300); [Hanks et al.](https://doi.org/10.1038/ng1449)):

| Allele | Locus (GRCh38) | HGVS (NM_001211.6) | Evidence |
|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G p.Leu737Ter | [ClinVar VCV000533901](https://www.ncbi.nlm.nih.gov/clinvar/variation/533901/) P/LP; [gnomAD](https://gnomad.broadinstitute.org/variant/15-40209701-T-G?dataset=gnomad_r4) AF 7.9e-05; het PASS AD 21/25 GQ 99 |
| 2 | chr15:40220612 T>G | c.3006T>G p.Asn1002Lys | [gnomAD](https://gnomad.broadinstitute.org/) singleton; SIFT 0.01; PolyPhen 0.997; [AlphaMissense](https://doi.org/10.1126/science.adg7492) 0.9229; kinase domain; het PASS AD 15/13 GQ 99 |

Architecture matches published MVA1 cases: one stop, one kinase-domain missense ([Hanks et al.](https://doi.org/10.1038/ng1449); [Rio Frio et al.](https://doi.org/10.1056/NEJMoa1006565)).

## Pipeline (run from `track1/`)

| Step | Script | Output |
|---|---|---|
| 122-gene panel | [`analysis/scan_panel.py`](analysis/scan_panel.py) | `PANEL` |
| Extract every allele in those spans ±5 kb | [`analysis/scan_panel2.py`](analysis/scan_panel2.py) | [`analysis/candidates/panel_variants.tsv`](analysis/candidates/panel_variants.tsv) — 11,835 alleles |
| MANE consequence | [`analysis/annotate_panel.py`](analysis/annotate_panel.py) | [`analysis/candidates/panel_annotated.tsv`](analysis/candidates/panel_annotated.tsv) |
| gnomAD / ClinVar / VEP | [`analysis/af_lookup.py`](analysis/af_lookup.py) + [`analysis/netutil.py`](analysis/netutil.py) | [`analysis/candidates/priority_annotated.tsv`](analysis/candidates/priority_annotated.tsv) |
| SpliceAI 1.3.1 | CLI | [`analysis/candidates/spliceai_out.vcf`](analysis/candidates/spliceai_out.vcf) |
| Whole-genome BAF mosaic screen | [`analysis/baf_screen.py`](analysis/baf_screen.py) | [`analysis/candidates/mosaic_baf_screen.tsv`](analysis/candidates/mosaic_baf_screen.tsv), [`figures/baf_deviation_per_chrom.png`](figures/baf_deviation_per_chrom.png) |
| Score against the official evaluator | [`analysis/submission_sim.py`](analysis/submission_sim.py) → [`challenge_src/evaluation.py`](challenge_src/evaluation.py) | 100 pts / F-max 1.000 on the primary pair |
| Open Targets (shared with Track 2) | [`analysis/ot_client.py`](analysis/ot_client.py) | [`analysis/candidates/ot_bub1b_profile.json`](analysis/candidates/ot_bub1b_profile.json) |

Post-submission checks (same day; CSV unchanged):

- Exomiser 15.1.0, no panel: [`analysis/exomiser/`](analysis/exomiser/) — BUB1B rank 1 / AR rank 2.
- mosdepth at BUB1B: [`figures/bub1b_depth_profile.png`](figures/bub1b_depth_profile.png) — exons diploid.
- WhatsHap on the mini-locus: alleles 10.9 kb apart stay unphased (`analysis/phasing/`; BAM not in git).
- Log: [`../REVISIONS.md`](../REVISIONS.md).

## Method

Five-pillar integration per the CAGI6 RGP assessment ([Stenton](https://gregorconsortium.org/node/120)):
call quality + population AF + deleteriousness + segregation logic + phenotype match.
Gene prior: MVA series in [Malumbres and Villarroya-Beltri](https://doi.org/10.1038/s41576-024-00762-6).

## Other folders

| Path | Content |
|---|---|
| [`research/`](research/README.md) | Pre-submission dossier (approaches, CAGI lessons, experiment plan) |
| [`challenge_src/`](challenge_src/README.md) | Snapshot of the public Space (scoring code) |
| [`submissions/`](submissions/README.md) | One directory per upload |

## Data use

Input FASTQ/VCF live in `data/` and are gitignored. Delete them within 30 days of challenge close.

## License

Analysis code and derived outputs: CC BY 4.0.
