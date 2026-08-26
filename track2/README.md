# Track 2 — Drug repurposing (team bigbag)

Three-tier plan for the child with BUB1B-MVA1. The genome result is in [`../track1/`](../track1/README.md).

| Deliverable | File |
|---|---|
| Written report | [`report.md`](report.md) |
| 3-minute script | [`video_script.md`](video_script.md) |
| HTML deck | [`slides/deck.html`](slides/deck.html) |
| PowerPoint | [`slides/pitch_deck.pptx`](slides/pitch_deck.pptx) |
| Deck builder | [`slides/build_assets.py`](slides/build_assets.py) |
| Methods form | [`methods_form_answers.xlsx`](methods_form_answers.xlsx) |

## Tiers (see the report for evidence grades)

1. **A — treat signs now.** Adavosertib + irinotecan ([Cole et al.](https://doi.org/10.1002/cncr.34786); [NCT02095132](https://clinicaltrials.gov/study/NCT02095132)). Citrate + thiazide ([Weigert and Hoppe](https://doi.org/10.3389/fped.2018.00098)). Alisertib ([Mossé et al.](https://doi.org/10.1158/1078-0432.CCR-18-2675)).
2. **B — decrease aneuploid-cell stress.** Everolimus / sirolimus ([Franz et al., "Long-Term Use"](https://doi.org/10.1371/journal.pone.0158476)).
3. **C — restore BubR1.** Mouse overexpression ([Baker et al.](https://doi.org/10.1038/ncb2643)); peptide route ([Zhang et al.](https://doi.org/10.1038/s43587-023-00361-w)).

## How the evidence was built

| Step | File | Writes |
|---|---|---|
| Open Targets GraphQL | [`../track1/analysis/ot_client.py`](../track1/analysis/ot_client.py) | [`evidence/ot_bub1b_profile.json`](evidence/ot_bub1b_profile.json), [`evidence/ot_rms_drugs.json`](evidence/ot_rms_drugs.json) |
| HTTP client (429 / Retry-After) | [`../track1/analysis/netutil.py`](../track1/analysis/netutil.py) | cache under `.netutil_cache/` (gitignored) |
| DGIdb / matrix-scores scan | artifacts checked into [`evidence/`](evidence/) | [`dgidb_tiers.json`](evidence/dgidb_tiers.json), [`matrix_scores_matches.csv`](evidence/matrix_scores_matches.csv) |
| ChEMBL feasibility | [`evidence/chembl_feasibility.json`](evidence/chembl_feasibility.json) | WEE1 IC50 for adavosertib |
| Structures | [`evidence/pdb/`](evidence/pdb/) | 5JJA, 5KHU, 6TLJ, AlphaFold O60566 distances |
| Figures | [`slides/build_assets.py`](slides/build_assets.py) | `fig_evidence.png`, `fig_mechanism.png`, `fig_domainmap.png`, `fig_exomiser.png` |

Shared genotype pipeline: [`../track1/analysis/`](../track1/analysis/).

## License

CC BY 4.0 (hackathon terms).
