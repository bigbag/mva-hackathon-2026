# bigbag — Rare Disease, Real Kid: MVA Hackathon 2026

Team repository for the SageBio / MVA Society challenge
([Space](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/),
[data](https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data)).
Code: [github.com/bigbag/mva-hackathon-2026](https://github.com/bigbag/mva-hackathon-2026).

| Track | Result | Start here |
|---|---|---|
| 1. Variant prediction | **100.0 rank points, F-max 1.000, full match** (2026-08-26 03:13 UTC) | [`track1/README.md`](track1/README.md) |
| 2. Drug repurposing | Three-tier plan (symptom / stress / BubR1 restoration) | [`track2/README.md`](track2/README.md) |

Causal pair (clinically validated): **BUB1B** c.2210T>G p.Leu737Ter + c.3006T>G p.Asn1002Lys (GRCh38 chr15).

## Layout

| Path | What it is |
|---|---|
| [`track1/analysis/`](track1/analysis/) | Pipeline scripts and derived tables (no FASTQ/VCF) |
| [`track1/METHODS.md`](track1/METHODS.md) | Full methods record |
| [`track1/analysis/candidates/track1_report.md`](track1/analysis/candidates/track1_report.md) | Track 1 written report |
| [`track1/submissions/bigbag_bub1b-panel-scan-v1/`](track1/submissions/bigbag_bub1b-panel-scan-v1/) | Uploaded CSV, report, notes |
| [`track1/research/`](track1/research/) | Pre-submission research dossier (10 approaches) |
| [`track1/challenge_src/`](track1/challenge_src/) | Snapshot of the public scoring Space |
| [`track1/figures/`](track1/figures/) | BAF screen and BUB1B depth plots |
| [`track2/report.md`](track2/report.md) | Track 2 written report |
| [`track2/slides/`](track2/slides/) | Pitch deck (`deck.html`, `pitch_deck.pptx`) |
| [`track2/evidence/`](track2/evidence/) | Open Targets, DGIdb, matrix-scores, PDB artifacts |
| [`REVISIONS.md`](REVISIONS.md) | Post-submission verification log |

## Data that is not in git

`.gitignore` blocks `data/`, `resources/`, FASTQ, VCF, BAM. Those files stay on the local machine and must be deleted within 30 days of challenge close.

## License

Analysis code and derived outputs: CC BY 4.0 (hackathon terms).
