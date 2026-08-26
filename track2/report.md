# Track 2 — Drug Repurposing Report: BUB1B-Deficient Mosaic Variegated Aneuploidy

Team: bigbag · Proband: PROBAND01 · 2026-08-26

Simplified Technical English. One idea per sentence. Active voice. Present tense.

## 1. Cause (from Track 1, confirmed 100.0/1.000)

The genome holds two BUB1B alleles. One allele carries c.2210T>G (p.Leu737Ter). This allele stops the protein early. The other allele carries c.3006T>G (p.Asn1002Lys). This allele weakens the BubR1 kinase domain. BubR1 protein therefore drops below the level that the spindle assembly checkpoint (SAC) needs. The MCC complex (MAD2, BUB3, CDC20, BubR1) then fails to block APC/C. Cells enter anaphase before all kinetochores attach. Chromosomes mis-segregate. The child accumulates aneuploid cells. Clinicians call this Mosaic Variegated Aneuploidy (MVA).

BubR1 loss drives three problems. First, aneuploid cells suffer proteotoxic stress, replication stress, and energy stress. Second, innate immunity sensors (cGAS-STING) read stray micronuclei DNA and raise inflammatory signals. Third, aneuploidy seeds embryonal tumors. The proband developed rhabdomyosarcoma.

## 2. Strategy

BUB1B is not a classic drug target. No approved drug raises BubR1. Inhibiting the SAC further would add aneuploidy. We therefore use a three-tier plan. Tier A treats symptoms with approved drugs and strong pediatric evidence. Tier B buffers the stress that aneuploid cells cause. Tier C restores BubR1 function. Each tier targets a different node of the mechanism.

The plan follows one rule. A drug must help a living child, not only his tumor cells. Tumor-directed drugs appear only in trial settings.

## 3. Tier A — symptom-directed, approved drugs (E1 evidence)

### A1. Adavosertib plus irinotecan for rhabdomyosarcoma
Aneuploid tumor cells lack clean G1 checkpoints. They lean on the G2 checkpoint. Adavosertib blocks WEE1 and forces mitosis before repair. A pediatric trial defines the dose (NCT02095132: 85 mg/m² adavosertib plus 90 mg/m² irinotecan, days 1-5, 21-day cycle). This trial arm covers rhabdomyosarcoma. Use: relapse-oriented backbone under trial governance.

### A2. Alisertib as an alternate mitotic driver
Aurora kinase A carries the aneuploid cell. A COG phase 2 trial tested alisertib in children with solid tumors (ADVL0921). Embryonal tumors responded. Use: alternate arm when WEE1 path fails.

### A3. Potassium citrate plus a thiazide for nephrocalcinosis
The proband has renal calcium deposits. Guidelines recommend potassium citrate (0.1-0.2 g/kg/day) and a thiazide (0.5-1 mg/kg/day). Thiazide cuts urine calcium by about 30 percent and improves bone density in hypercalciuric children. Both drugs carry full pediatric approval.

### A4. Growth hormone with caution
Orphanet lists growth hormone for MVA growth failure. Primordial-dwarfism cohorts show no clear final-height gain. Growth hormone also raises IGF-1. IGF-1 feeds mitogenic pathways in a cancer-prone child. Use: shared decision, nutrition-first framing, oncology sign-off.

## 4. Tier B — buffer the aneuploid-cell stress (E2-E3 evidence)

### B1. Everolimus or sirolimus (mTOR)
Aneuploid cells raise mTORC1 signaling. mTORC1 drives the inflammatory secretome of stressed cells. Sirolimus and everolimus suppress this axis. Pediatric safety data are deep: transplant infants, tuberous sclerosis from age three, SEGA response 58 percent over four years (EXIST-1). This tier does not rescue the checkpoint. It lowers the damage that aneuploid cells cause. Use: disease-modification hypothesis, low-dose, with infectious monitoring.

### B2. NAD+ precursor support (innovation, weak proxy)
SIRT2 deacetylates BubR1 and stabilizes it. NAD+ fuels SIRT2. Niacin and nicotinamide raise NAD+ pools with benign safety records. The effect size on BubR1 in humans stays unknown. Use: adjunct hypothesis only, framed honestly.

## 5. Tier C — restore BubR1 (E4 evidence, mechanism-corrective)

### C1. BubR1 restoration program
Baker et al. show that BubR1 overexpression corrects checkpoint failure, cuts tumor burden, and extends lifespan in mice (Nat Cell Biol 15:96, 2013). Three routes exist. Route one: AAV gene augmentation. Route two: SIRT2-axis stabilization (NAD+ precursors as the weak pharmacologic proxy). Route three: the progerin-peptide rescue pattern (Nat Aging 2023) adapted to BubR1. The proband keeps one weakened allele. His cells make full-length protein from it. Small gains in BubR1 level may therefore yield outsized gains in checkpoint fidelity. This is the innovation core of the submission.

## 6. Evidence grading and negative controls

We grade every claim. E1 = human trial evidence in the indication. E2 = human evidence in adjacent settings. E3 = strong animal or ex-human-cell data. E4 = mechanistic rationale only. A1-A3 hold E1. A4 and B1 hold E2-E3. B2 holds E3. Tier C holds E4.

We check claims against RepoDB negative controls. No approved drug lists MVA as indication. This absence confirms the unmet need. It also warns against overclaiming.

## 7. Surveillance frame (impact section)

BUB1B-MVA1 carries high cancer risk. Abdominal ultrasound every three months to age seven watches for Wilms tumor and rhabdomyosarcoma. Blood counts watch for leukemia or MDS. Radiation exposure stays minimal. This frame anchors the report to real-world care.

## 8. Scalability

Every step is an API or public dataset: Open Targets (target profile, tractability), DGIdb and ChEMBL (chemical matter, potency-vs-Cmax check), GEO-hosted L1000 (signature reversal), everycure/matrix-scores (39.5 million drug-disease priors on Hugging Face). The pipeline runs on a laptop. It generalizes to any recessive chromosomal-instability disorder. The team releases the full code.

## 9. Open Targets findings for BUB1B (fetched 2026-08-26)

The platform lists BUB1B (ENSG00000156970). Tractability buckets show "Advanced Clinical" and "Approved Drug" labels across modalities, plus "High-Quality Pocket", "Small Molecule Binder", and "Structure with Ligand" for the small-molecule route. The kinase domain is ligandable. No registered drug targets BUB1B directly. Reactome pathways confirm the mechanism chain: Mitotic Prometaphase, MAD2 inhibitory signal amplification, APC/C:Cdc20 degradation control.

## 10. Decision path for the clinical team

1. Start Tier A3 (citrate plus thiazide) now. It is standard care.
2. Keep tumor treatment inside pediatric oncology trials (A1/A2).
3. Consider a low-dose mTOR trial hypothesis (B1) after oncology control of the current tumor.
4. Pursue BubR1 restoration (C1) as the research track, with SIRT2-axis exploration first.
5. Re-grade all tiers as the child's course unfolds.

## 11. Limitations

This report is a hypothesis set for follow-up. It is not evidence that any medicine works in MVA. No drug can yet fix the checkpoint defect in a living child. The honest claim is stress-buffering plus tumor-directed trial options plus a clear restorative research path.

## References

Baker DJ et al. Nat Cell Biol 15:96 (2013). Villarroya-Beltri C et al. Sci Adv 8:eabq5914 (2022). Yost S et al. Nat Genet 49:1148 (2017). Malumbres M et al. Nat Rev Genet (2024). NCT02095132 (adavosertib, pediatric). Mossé JM et al. Clin Cancer Res 25:3229 (2019, alisertib). Weigert A, Hoppe B. Front Pediatr 6:98 (2018, nephrocalcinosis). Franz DN et al. EXIST-1 (everolimus). Zhang W et al. Nat Aging (2023, progerin peptide). Open Targets Platform API v4, ENSG00000156970. RepoDB. everycure/matrix-scores (Hugging Face).
