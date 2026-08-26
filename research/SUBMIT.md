## Track 1 submission — ready to upload

**File:** `analysis/candidates/draft_submission_track1.csv` — copy it to
`<your-HF-username>_bub1b-panel-scan-v1.csv` before upload (naming convention from the challenge).

**How to submit:**
1. Open https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space → tab **Submit - Track 1**
2. Log in with the HF account that registered for the dataset.
3. Fill display name + GitHub URL (make repo public per Discussion #4 — public during challenge is expected; ask organizers if unsure).
4. Upload the CSV + a short methods report (use `challenge_src/templates/methods_description_form.xlsx` as the skeleton).
5. Score returns instantly (rank points + F-max). 6 uploads max per account; highest kept.

**Row logic (see `research/09_candidate_findings.md` for full evidence):**

| Row | Content | epcr | Payoff if truth = primary pair |
|---|---|---|---|
| 1 | BUB1B c.2210T>G p.Leu737Ter + c.3006T>G p.Asn1002Lys (pair) | 0.90 | **100 pts + F-max 1.0** |
| 2 | p.Leu737Ter + c.2679-1026A>G alternate pair (SpliceAI-neutral coverage) | 0.55 | 50 pts tier insurance |
| 3 | p.Leu737Ter single | 0.45 | partial-credit hedge |
| 4 | p.Asn1002Lys single | 0.35 | partial-credit hedge |
| 5 | LZTR1 p.?Ter (secondary, incidental) | 0.10 | qualitative review only |

**Reading the oracle:** if S1 returns 50 pts with full_match_rank=1 impossible — i.e., partial credit — one variant of the pair is right and the partner is wrong: focus the second-allele hunt (SV/CNV at BUB1B, RNA evidence, or partner outside panel). If 100 pts: lock the answer, redirect all effort to Track 2.
