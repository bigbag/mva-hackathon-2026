# Track 2 — Drug Repurposing Research (scout: DrugRepurposing, 2026-08-26)

## 0. Core framing
**The cancer–CIN paradox cuts both ways.** In oncology, CIN creates *exploitable* vulnerabilities (60–80% of cancers are CIN+; no approved CIN-targeting drug exists yet) [Nat Rev Clin Oncol 2024, s41571-024-00923-w]. In **constitutional CIN (MVA)**, the SAC/mitotic apparatus is already defective — so the oncology playbook of *further* inhibiting SAC/kinase nodes (MPS1/TTK, AURKA/B, PLK4, WEE1) would **worsen** aneuploidy systemically. Rational MVA repurposing splits into 3 tiers: **(A) symptom-directed, evidence-backed drugs** (RMS therapy, nephrocalcinosis, growth); **(B) adaptive/stress-buffering** (proteotoxic/ER stress, senescence/SASP, cGAS–STING inflammation); **(C) mechanism-restorative** (BubR1 augmentation, splice/readthrough correction — preclinical, the innovation lever).

MVA genes recap: BUB1B (MVA1, cancer ~75%), CEP57 (MVA2, no cancers reported), TRIP13 (MVA3, Wilms), CENATAC (minor spliceosome; de Wolf 2021 EMBO J 10.15252/embj.2020106536), MAD2L1BP/p31comet (JCI Insight 2023, PMID 37796616), TUBGCP6/TUBGCP4 (γ-TuRC; AJHG 2015, PMC4385181). Standard of care: surveillance + symptom management (renal US q3mo to age 7 for BUB1B, GH trial for growth, radiation avoidance) [Orphanet ORPHA:1052].

## 1. Methodology toolkit

| Resource | Gives what | Access |
|---|---|---|
| **Open Targets Platform** | Target–disease assoc scores, tractability, safety (FAERS), LOEUF, DepMap essentiality, known drugs + max clinical stage | GraphQL api.platform.opentargets.org/api/v4/graphql; google-deepmind/science-skills helpers |
| **CLUE/LINCS CMap (L1000)** | >3M perturbation profiles; query DE signature → reversal drugs; CRISPR KO connectivity | **clue.io retired 2026-01-31; data at GEO** (GSE92742); lincsproject.org workflows |
| **RepoDB** | Approved (TP) + suspended/terminated (TN) drug–indication pairs — negative controls | github.com/adam-sam-brown/repoDB |
| **DGIdb v5** | ~100k drug–gene interaction claims | GraphQL dgidb.org; `dgipy` pip client |
| **ChEMBL** | Bioactivity IC50/Ki for dose-feasibility (potency at new target >10× weaker than original ⇒ infeasible at safe dose) | REST ebi.ac.uk/chembl |
| **DrugBank open** | Approved-drug target/indication reference | go.drugbank.com |
| **SwissTargetPrediction** | Reverse-screening SMILES → ranked targets | swisstargetprediction.ch |
| **ToolUniverse (Harvard/MIMS)** | One-API orchestration of all above + codified repurposing rubric (0–100: target assoc 40, safety 30, lit 20, properties 10; E1–E4 evidence grades) | github.com/mims-harvard/ToolUniverse |
| **HF assets** | `everycure/matrix-scores` (39.5M drug–disease pairs, 1800 drugs × 22k MONDO); `Tassy24/K-Paths-inductive-reasoning-pharmaDB` (arXiv:2502.13344); `dn-gh/dti-merged-preprocessed` (arXiv:2411.15418); `ZemResearch/HippoTarget`; `liwenyuan99/AetherCell` | HF datasets/models |

**Best-practice n=1 pipeline:** (1) fix the gene (Track 1) → (2) Open Targets target profile → (3) DGIdb/ChEMBL pathway chemical matter → (4) LINCS L1000 signature-reversal (GEO-hosted) using MVA cell-model DE signature → (5) everycure/matrix-scores prior + ClinicalTrials.gov E1 check → (6) dose-feasibility vs pediatric Cmax. Judging alignment: Rigor 35% = E1–E4 grading + repoDB negative controls; Scalability 15% = fully API/dataset-driven.

## 2. Druggable-node table

| Node | MVA evidence | Chemical matter | Pediatric safety | Source |
|---|---|---|---|---|
| **BUB1B/BubR1** | Biallelic LoF = MVA1; RMS/Wilms/leukemia ~75%; progeroid features | No approved modulator; BubR1 *overexpression* corrects checkpoint in mice; **SIRT2-dependent stabilization** → NAD+/sirtuin axis; progerin-Cterm peptide rescued BUBR1 in HGPS cells | None (protective target) | Baker 2013 NCB 15:96; Pun 2024 Semin Cancer Biol; Zhang 2023 Nat Aging |
| **TRIP13** | MVA3 + Wilms; oocyte maturation arrest | DCZ0415 (Kd 2.4 µM but 2025 ATPase re-eval inactive ≤500 µM), DCZ5417/8, TI17; HTS 2025: **anlotinib** binds TRIP13 IC50 5 µM (CETSA) | None in clinic; anlotinib adult NSCLC only | Yost 2017 Nat Genet 49:1148; Wang 2019 Cancer Res 79:536; Sammons 2025 SLAS Discov 33:100233 |
| **MPS1/TTK** | SAC amplifier (not MVA gene) | CFI-402257 (phase 1/2 adult; neutropenia DLT) | Adult only; **conceptually contraindicated in SAC-defective MVA** | NCT02792465; NCT05251714 |
| **AURKA** | Synthetic-lethal partner of TRIP13 loss in Rb-deficient tumors | Alisertib — COG ADVL0921 pediatric phase II incl. RMS (responses seen) | **Yes — dedicated pediatric PhI/II** | Mossé 2019 CCR 25:3229 |
| **WEE1** | G2 checkpoint; SAC-defective tumors are G2-dependent | **Adavosertib (AZD1775) + irinotecan**: pediatric Ph1/2, RMS expansion arm D, RP2D 85 mg/m² + 90 mg/m² irinotecan d1–5 q21d | **Yes — pediatric RP2D/PK** (NCT02095132, n=76) | NCT02095132 |
| **PLK4** | Mutations → microcephaly/primordial dwarfism (phenotypic neighbor) | Centrinone (probe); CFI-400945 adult trials — *centriole-depleting: wrong direction* | No | Martin 2014 Nat Genet 46:1283 |
| **CEP57 / γ-TuRC** | MVA2 / microcephaly+chorioretinopathy | None — scaffolding proteins, no pocket chemistry; expression rescue only | n/a | Snape 2011 Nat Genet ng.822; AJHG 2015 |
| **CENATAC / minor spliceosome** | AT-AN minor-intron retention in ~100 cell-cycle genes | Splice-correcting concepts only | n/a | de Wolf 2021 EMBO J 40:e106536 |
| **Aneuploidy stress (HSF1/HSP90, UPR, mTOR, cGAS–STING)** | Downstream consequences of CIN | HDAC6, HSP90, IRE1α (ORIN1001 Ph1), PERK (HC-5404), glutaminase (telaglenastat+everolimus ENTRATA); sirolimus/everolimus widely used in children | **Yes for mTOR** (TSC SEGA from ~3y, transplant infants) | Nat Rev Clin Oncol 2024 |

## 3. Repurposing hypotheses shortlist (child with active RMS + nephrocalcinosis + growth failure)

1. **Adavosertib + irinotecan** as relapse-oriented RMS backbone — pediatric RP2D defined (NCT02095132). *Tier A, E1.*
2. **Alisertib** — pediatric COG PhII activity in embryonal tumors incl. RMS; AURKA×TRIP13-loss synthetic lethality if RB1-deficient. *Tier A, E1.*
3. **Regorafenib/pazopanib + VIT/VIR chemo** — being tested in relapsed pediatric RMS (FaR-RMS VIRR arm, NCT04625907, n≈1672). *Tier A, E1.*
4. **Nephrocalcinosis bundle: K-citrate + thiazide (± amiloride)** — pediatric standard for hypercalciuric NC; thiazide also improves lumbar BMD z-score in hypercalciuric children → kidney + bone benefit. *Tier A, E2–E3.* [Weigert & Hoppe 2018 Front Pediatr 6:98]
5. **GH trial for growth failure** — Orphanet lists as MVA management; MOPD II precedent shows no final-height gain (n=11) → frame as QoL optimization; caution GH/IGF1 mitogenicity in cancer-predisposed child. *Tier A, E3.* [Bober 2012 AJMG 158A:2719]
6. **Sirolimus/everolimus (mTOR) as CIN-stress buffer + RMS adjunct** — aneuploid-cell SASP/metabolic stress; strongest pediatric safety dossier (EXIST-1 SEGA 58% RR 4y); position as stress-buffering, NOT checkpoint rescue. *Tier B, E3–E4.*
7. **(Innovation) BubR1-restoration program** — SIRT2–BubR1 stabilization (NAD+ precursors as weak proxy), progerin-peptide-type rescue (Nat Aging 2023), AAV-BubR1 augmentation; uniquely mechanism-corrective if BUB1B variant is hypomorphic (Baker 2013: overexpression corrects checkpoint, cuts tumorigenesis, extends lifespan). HSCT precedent (Laberko 2019). *Tier C, E4.*

## 4. Model writeup (everolimus–TSC template)
Mechanism-first → one drug multiple manifestations → long pediatric safety record. Structure by judging criteria: Rigor = gene→target→drug chain with E1–E4 grades + dose-feasibility (Cmax vs IC50) + repoDB negative controls; Impact = quantified unmet need (prevalence <1/1M; 75% cancer mortality in BUB1B) + concrete surveillance protocol; Innovation = Tier-B "buffer the consequences" + Tier-C restoration; Scalability = all-API pipeline rerunnable for any rare CIN disorder.

## 5. Caveats
- clue.io retired 2026-01-31 — use GEO GCTx directly.
- DCZ0415 potency contested; anlotinib–TRIP13 best current (still preclinical, and it's an *inhibitor* — wrong direction for TRIP13-LoF).
- All SAC/kinase inhibitors mechanistically wrong for prophylaxis in a living MVA child — tumor-directed trial use only.
- GH: no proven final-height benefit in primordial dwarfism; oncologic caution.
