# Track 2 Report. Drug Repurposing for BUB1B-Deficient Mosaic Variegated Aneuploidy

Team: bigbag. Proband: PROBAND01. Date: 2026-08-26.

This report uses Simplified Technical English. Each sentence holds one idea. Sentences use active voice and present tense.

## 1. Cause

The genome has two BUB1B alleles. Allele 1 has c.2210T>G (p.Leu737Ter). Allele 1 stops the protein early. Allele 2 has c.3006T>G (p.Asn1002Lys). Allele 2 decreases the function of the BubR1 kinase domain. The BubR1 protein level then falls below the level that the spindle assembly checkpoint (SAC) needs. The MCC complex contains MAD2, BUB3, CDC20, and BubR1. The MCC complex does not stop APC/C. Cells enter anaphase before all kinetochores attach. Chromosomes do not segregate correctly. The child accumulates aneuploid cells. Clinicians name this condition Mosaic Variegated Aneuploidy ([Malumbres and Villarroya-Beltri](https://doi.org/10.1038/s41576-024-00762-6)).

BubR1 loss causes three problems. First, aneuploid cells have proteotoxic stress, replication stress, and energy stress. Second, innate immunity sensors (cGAS-STING) detect DNA from micronuclei. These sensors increase inflammatory signals. Third, aneuploidy starts embryonal tumors. The proband developed rhabdomyosarcoma ([Hanks et al.](https://doi.org/10.1038/ng1449)).

## 2. Strategy

BUB1B is not a usual drug target. No approved drug increases BubR1. A drug that decreases SAC function will add more aneuploidy. We use a plan with three tiers. Tier A treats symptoms. Tier A uses approved drugs with strong pediatric evidence. Tier B decreases the stress that aneuploid cells cause. Tier C restores BubR1 function. Each tier targets a different node of the mechanism.

The plan follows one rule. A drug must help a living child. A drug must not help only tumor cells. Tumor-directed drugs appear only in trial settings.

## 3. Tier A. Symptom treatment with approved drugs (E1 evidence)

### A1. Adavosertib plus irinotecan for rhabdomyosarcoma

Aneuploid tumor cells do not have intact G1 checkpoints. These cells use the G2 checkpoint. Adavosertib blocks WEE1. The block forces mitosis before DNA repair. A pediatric trial sets the dose ([Cole et al.](https://doi.org/10.1002/cncr.34786); [National Cancer Institute](https://clinicaltrials.gov/study/NCT02095132)). The dose is 85 mg/m² adavosertib plus 90 mg/m² irinotecan. The schedule is day 1 through day 5 of a 21-day cycle. This trial arm includes rhabdomyosarcoma. Use this pair as a relapse backbone under trial control.

### A2. Alisertib as an alternate mitotic drug

Aurora kinase A supports the aneuploid cell. A COG phase 2 trial tested alisertib in children with solid tumors ([Mossé et al.](https://doi.org/10.1158/1078-0432.CCR-18-2675)). Embryonal tumors responded. Use this arm when the WEE1 arm fails.

### A3. Potassium citrate plus a thiazide for nephrocalcinosis

The proband has renal calcium deposits. [Weigert and Hoppe](https://doi.org/10.3389/fped.2018.00098) recommend potassium citrate at 0.1-0.2 g/kg/day. The same review recommends a thiazide at 0.5-1 mg/kg/day. A thiazide decreases urine calcium by about 30 percent. A thiazide also improves bone density in children with hypercalciuria. Both drugs have full pediatric approval.

### A4. Growth hormone. Use with caution.

Some clinics use growth hormone for MVA growth failure. Studies in primordial dwarfism do not show a clear gain in final height. Growth hormone also increases IGF-1. IGF-1 increases mitogenic signals. The child has a high cancer risk. Use growth hormone only after a shared decision. Put nutrition first. Get oncology approval.

## 4. Tier B. Decrease stress in aneuploid cells (E2-E3 evidence)

### B1. Everolimus or sirolimus (mTOR)

Aneuploid cells increase mTORC1 signaling. mTORC1 drives the inflammatory secretome of stressed cells. Sirolimus and everolimus decrease this signal. Pediatric safety data are large. Transplant infants receive these drugs. Children with tuberous sclerosis receive these drugs from age three. The [EXIST-1](https://doi.org/10.1371/journal.pone.0158476) long-term analysis shows a 57.7 percent SEGA response after a median of 47.1 months ([Franz et al., "Long-Term Use"](https://doi.org/10.1371/journal.pone.0158476)). This tier does not repair the checkpoint. This tier decreases the damage that aneuploid cells cause. Use a low dose. Monitor infection.

### B2. NAD+ precursor support (weak proxy)

SIRT2 removes acetyl groups from BubR1. This action stabilizes BubR1. NAD+ supplies SIRT2. Niacin and nicotinamide increase NAD+ pools. These compounds have a good safety record. The effect on BubR1 in humans is not known. Use this idea only as an adjunct hypothesis.

## 5. Tier C. Restore BubR1 (E4 evidence)

### C1. BubR1 restoration program

[Baker et al.](https://doi.org/10.1038/ncb2643) show that BubR1 overexpression corrects checkpoint failure in mice. The same work decreases tumor burden. The same work extends lifespan. Three routes exist. Route 1 is AAV gene augmentation. Route 2 is SIRT2-axis stabilization. NAD+ precursors are a weak pharmacologic proxy for route 2. Route 3 uses the progerin C-terminal peptide that raises BUBR1 ([Zhang et al.](https://doi.org/10.1038/s43587-023-00361-w)). The proband keeps one weakened allele. His cells make full-length protein from that allele. A small increase in BubR1 level can give a large gain in checkpoint fidelity. This is the main research goal of the submission.

## 6. Evidence grades and negative controls

We give each claim a grade. E1 is human trial evidence in the indication. E2 is human evidence in adjacent settings. E3 is strong animal data or data from human cells. E4 is mechanistic rationale only. A1 through A3 have grade E1. A4 and B1 have grade E2 or E3. B2 has grade E3. Tier C has grade E4.

We check claims against [RepoDB](https://doi.org/10.1038/sdata.2017.29) negative controls ([Brown and Patel](https://doi.org/10.1038/sdata.2017.29)). No approved drug lists MVA as an indication. This absence confirms the unmet need. This absence also warns against claims that are too strong.

## 7. Surveillance

BUB1B-MVA1 has a high cancer risk ([Hanks et al.](https://doi.org/10.1038/ng1449)). Do an abdominal ultrasound every three months until age seven. This test watches for Wilms tumor and rhabdomyosarcoma. Blood counts watch for leukemia or MDS. Keep radiation exposure low. This section connects the report to real-world care.

## 8. Scalability

Each step uses an API or a public dataset. [Open Targets](https://platform.opentargets.org/target/ENSG00000156970) gives the target profile and tractability. [DGIdb](https://www.dgidb.org/) and [ChEMBL](https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491) give chemical matter and potency. The [everycure/matrix-scores](https://huggingface.co/datasets/everycure/matrix-scores) set gives 39.5 million drug-disease priors on [Hugging Face](https://huggingface.co/datasets/everycure/matrix-scores). The pipeline runs on a laptop. The pipeline applies to other recessive chromosomal-instability disorders. The team releases the [full code](https://github.com/bigbag/mva-hackathon-2026).

## 9. [Open Targets](https://platform.opentargets.org/target/ENSG00000156970) findings for BUB1B (2026-08-26)

The platform lists [BUB1B (ENSG00000156970)](https://platform.opentargets.org/target/ENSG00000156970). Tractability buckets show the labels "Advanced Clinical" and "Approved Drug" across modalities. The small-molecule route also has the labels "High-Quality Pocket", "Small Molecule Binder", and "Structure with Ligand". The kinase domain can bind a ligand. No registered drug targets BUB1B directly. [Reactome](https://reactome.org/) pathways confirm the mechanism chain. The pathways are Mitotic Prometaphase, MAD2 inhibitory signal amplification, and APC/C:Cdc20 degradation control.

## 10. Decision path for the clinical team

1. Start Tier A3 (citrate plus thiazide) now. This pair is standard care.
2. Keep tumor treatment inside pediatric oncology trials (A1 or A2).
3. Consider a low-dose mTOR trial hypothesis (B1) after oncology control of the current tumor.
4. Pursue BubR1 restoration (C1) as the research track. Explore the SIRT2 axis first.
5. Change all grades when the child's course changes.

## 11. Limitations

This report is a set of hypotheses for follow-up. This report is not evidence that any medicine works in MVA. No drug can yet repair the checkpoint defect in a living child. The honest claim has three parts. Part 1 is stress buffering. Part 2 is tumor-directed trial options. Part 3 is a clear restorative research plan.

## 12. External computational prior ([everycure/matrix-scores](https://huggingface.co/datasets/everycure/matrix-scores), 2026-08-26)

We scanned all 39.5 million drug-disease pairs for the indications of the proband.

**Rhabdomyosarcoma (MONDO:0005212).** The model ranks docetaxel, cisplatin, etoposide, 5-fluorouracil, and mitoxantrone highest. These are known cytotoxic neighbors. The prior adds no new tumor candidate. The prior confirms that the tumor arm sits inside standard oncology space.

**MVA syndrome (MONDO:0000141), MVA1/BUB1B (MONDO:0009759), MVA2 (MONDO:0013582).** Three facts stand out.

1. **No strong prior exists.** Top treat-scores reach only about 3.4 to 3.6. Global ranks are near one million to three million. The computational record has no validated drug for MVA. This fact measures the unmet need.
2. **Vincristine is first on the MVA list.** Vincristine already sits in standard rhabdomyosarcoma therapy (VAC/VIT regimens). The model finds this independently. The tumor arm and the syndrome-level prior agree.
3. **Acetazolamide ranks first for MVA1.** Acetazolamide blocks carbonic anhydrase. Acetazolamide makes urine more alkaline. This action touches the nephrocalcinosis axis of the proband. We give this idea grade E4. This idea is a discussion point for the nephrology team. This idea is not a recommendation.

**[DGIdb](https://www.dgidb.org/) v5 (same day).** BUB1B returns zero drug interactions. MTOR returns 177 interactions with 38 approved drugs. Everolimus is among these drugs. WEE1 and AURKA return investigational agents only. The database layer supports the tier structure. No direct BUB1B drug exists. The approved lever is at mTOR. The tumor levers are in trial space.

Artifacts: `track2/evidence/matrix_scores_matches.csv`, `dgidb_tiers.json`, `ot_bub1b_profile.json`, `chebi_names.json`.

## 13. Structural mechanism (2026-08-26)

We mapped both alleles onto BubR1 structures. We also used the [AlphaFold](https://alphafold.ebi.ac.uk/entry/O60566) model.

**Domain architecture ([UniProt O60566](https://www.uniprot.org/uniprotkb/O60566/entry)).** The TPR domain spans residues 1 through 226. The KEN box is at residue 20. The D-box spans residues 224 through 232. The PP2A-B56 docking motif spans residues 668 through 675. The kinase domain spans residues 766 through 1050. The catalytic proton acceptor is D882. The ATP-binding lysine cluster spans residues 772 through 780.

**Allele 1: p.Leu737Ter.** The stop codon is 29 residues before the kinase domain starts. The truncated protein keeps residues 1 through 737. The truncated protein keeps the TPR domain, the KEN box, the D-box, and the PP2A-B56 docking motif. The APC/C-MCC cryo-EM structures ([PDB 6TLJ](https://www.rcsb.org/structure/6TLJ), [5KHU](https://www.rcsb.org/structure/5KHU)) show BubR1 residues 19 through 499. This region is the scaffold that binds CDC20. The PP2A complex structure ([PDB 5JJA](https://www.rcsb.org/structure/5JJA)) shows the B56 docking motif. The motif is 4 to 8 angstroms from PP2A-B56. Allele 1 loses only the kinase domain. Allele 1 keeps each resolved scaffold function. We name allele 1 a null allele that removes the kinase domain.

**Allele 2: p.Asn1002Lys.** The residue is in the kinase C-lobe. The [AlphaFold](https://alphafold.ebi.ac.uk/entry/O60566) model (v6) scores this region with high confidence. The kinase-domain mean pLDDT is 82. The N1002 pLDDT is 91. The 990-1015 window pLDDT is 91. N1002 is 19.8 angstroms from the catalytic D882. N1002 is 35.6 angstroms from the VAIK lysine. The substitution does not touch the catalytic core. The substitution is in the C-terminal kinase tail. The substitution more likely decreases fold stability or regulation. The substitution does not remove the active site.

**Synthesis.** Both alleles change the kinase domain. Both alleles leave the MCC scaffold intact. The checkpoint keeps its scaffold arm. The checkpoint loses its kinase output. This fact explains a living child with cancer predisposition. BubR1 that has only scaffold function supports life. This BubR1 does not protect enough against aneuploidy. This fact also makes Tier C more clear. A therapy must restore protein level or scaffold strength. A therapy does not need to restore kinase chemistry. BubR1 overexpression data from mice support this view ([Baker et al.](https://doi.org/10.1038/ncb2643)). Those data show checkpoint repair with scaffold-level rescue.

Artifacts: `evidence/pdb/` ([5JJA](https://www.rcsb.org/structure/5JJA), [6TLJ](https://www.rcsb.org/structure/6TLJ), [5KHU](https://www.rcsb.org/structure/5KHU), [AlphaFold model](https://alphafold.ebi.ac.uk/entry/O60566), distance computations).

## 14. Registered RMS trial landscape ([Open Targets](https://platform.opentargets.org/target/ENSG00000156970), 2026-08-26)

The platform lists 95 drug or clinical candidates for rhabdomyosarcoma. Late-stage entries include vinorelbine (phase 3), ifosfamide (phase 3), filgrastim (phase 3), and eribulin (phase 2). Targeted entries include crizotinib, sorafenib, imatinib, and tacrolimus. Our Tier A picks do not appear in this indication list yet. The picks are adavosertib plus irinotecan, and alisertib. These drugs enter through pediatric solid-tumor trials and relapsed-RMS trials ([Cole et al.](https://doi.org/10.1002/cncr.34786); [Mossé et al.](https://doi.org/10.1158/1078-0432.CCR-18-2675)). Artifact: `evidence/ot_rms_drugs.json`.

## 15. Nephrocalcinosis management protocol (Tier A3)

The protocol targets deposits that hypercalciuria causes. The child was born at 32 weeks.

1. **Measure first.** Obtain a spot urine calcium-to-creatinine ratio on two mornings. Obtain serum calcium, phosphate, magnesium, vitamin D (25-OH), and PTH. Obtain a renal ultrasound every six to twelve months.
2. **Give citrate first.** Give potassium citrate 0.1-0.2 g/kg/day in divided doses. Target a rise in urine citrate. Target a urine pH that is neutral or alkaline. Watch serum potassium.
3. **Add a thiazide when hypercalciuria continues.** Give hydrochlorothiazide 0.5-1 mg/kg/day in two doses. Expect a urine-calcium drop near 30 percent. Monitor potassium and magnesium. Replace these ions if needed.
4. **Add amiloride as a third step** if low potassium limits the thiazide.
5. **Keep acetazolamide as a discussion point only.** Acetazolamide ranked first for MVA1 in the matrix-scores prior. Acetazolamide also makes urine more alkaline. This action can make calcium-phosphate deposits worse. Grade E4. The nephrology team decides.
6. **Bone effect.** A thiazide improves bone mineral density in children with hypercalciuria. This effect helps a child with growth restriction.

See [Weigert and Hoppe](https://doi.org/10.3389/fped.2018.00098).

## 16. Eligibility for the tumor arm. A biomarker gate.

We propose a tumor test before any Tier A mitotic drug.

1. **WEE1 arm (adavosertib plus irinotecan).** Test tumor RB1 status first. Test tumor TP53 status first. WEE1 dependence occurs when G1 checkpoints fail. Intact RB1 and p53 decrease the expected benefit. Intact RB1 and p53 increase toxicity. Evidence: [Cole et al.](https://doi.org/10.1002/cncr.34786); [National Cancer Institute](https://clinicaltrials.gov/study/NCT02095132).
2. **AURKA arm (alisertib).** AURKA dependence increases in cells with an Rb-pathway defect. The same RB1 test controls this arm.
3. **Chemical feasibility ([ChEMBL](https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491), verified).** Adavosertib inhibits WEE1 with IC50 0.6-1.7 nM ([CHEMBL5491](https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491)). The pediatric RP2D of 85 mg/m² reaches plasma levels far above this value. The drug engages its target at safe pediatric doses. Published assays give everolimus and alisertib potencies in the single-digit nanomolar range. The [ChEMBL](https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491) REST service returned no usable rows for those two drugs on this date. We give those two cells grade E2 from literature.
4. **Surveillance does not change** with the arm. Do an abdominal ultrasound every three months until age seven. Watch blood counts for leukemia or MDS. Keep radiation low.

Artifact: `evidence/chembl_feasibility.json`.

## Works Cited

AlphaFold Database. "O60566 (BUB1B_HUMAN)." *AlphaFold Protein Structure Database*, EMBL-EBI / Google DeepMind, [https://alphafold.ebi.ac.uk/entry/O60566](https://alphafold.ebi.ac.uk/entry/O60566).

Baker, Darren J., et al. "Increased Expression of BubR1 Protects against Aneuploidy and Cancer and Extends Healthy Lifespan." *Nature Cell Biology*, vol. 15, no. 1, 2013, pp. 96-102. [https://doi.org/10.1038/ncb2643](https://doi.org/10.1038/ncb2643).

bigbag. "mva-hackathon-2026." *GitHub*, 2026, [https://github.com/bigbag/mva-hackathon-2026](https://github.com/bigbag/mva-hackathon-2026).

Brown, Adam S., and Chirag J. Patel. "A Standard Database for Drug Repositioning." *Scientific Data*, vol. 4, 2017, 170029. [https://doi.org/10.1038/sdata.2017.29](https://doi.org/10.1038/sdata.2017.29).

ChEMBL. "Wee1-like Protein Kinase (CHEMBL5491)." *ChEMBL*, EMBL-EBI, [https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491](https://www.ebi.ac.uk/chembl/explore/target/CHEMBL5491).

Cole, Kristina A., et al. "Pediatric Phase 2 Trial of a WEE1 Inhibitor, Adavosertib (AZD1775), and Irinotecan for Relapsed Neuroblastoma, Medulloblastoma, and Rhabdomyosarcoma." *Cancer*, vol. 129, no. 14, 2023, pp. 2245-55. [https://doi.org/10.1002/cncr.34786](https://doi.org/10.1002/cncr.34786).

DGIdb. *The Drug Gene Interaction Database*, Washington University School of Medicine, [https://www.dgidb.org/](https://www.dgidb.org/).

everycure. "matrix-scores." *Hugging Face*, [https://huggingface.co/datasets/everycure/matrix-scores](https://huggingface.co/datasets/everycure/matrix-scores).

Franz, David Neal, et al. "Long-Term Use of Everolimus in Patients with Tuberous Sclerosis Complex: Final Results from the EXIST-1 Study." *PLOS ONE*, vol. 11, no. 6, 2016, e0158476. [https://doi.org/10.1371/journal.pone.0158476](https://doi.org/10.1371/journal.pone.0158476).

Hanks, Sandra, et al. "Constitutional Aneuploidy and Cancer Predisposition Caused by Biallelic Mutations in BUB1B." *Nature Genetics*, vol. 36, no. 11, 2004, pp. 1159-61. [https://doi.org/10.1038/ng1449](https://doi.org/10.1038/ng1449).

Malumbres, Marcos, and Carolina Villarroya-Beltri. "Mosaic Variegated Aneuploidy in Development, Ageing and Cancer." *Nature Reviews Genetics*, vol. 25, no. 12, 2024, pp. 864-78. [https://doi.org/10.1038/s41576-024-00762-6](https://doi.org/10.1038/s41576-024-00762-6).

Mossé, Yaël P., et al. "A Phase II Study of Alisertib in Children with Recurrent/Refractory Solid Tumors or Leukemia: Children's Oncology Group Phase I and Pilot Consortium (ADVL0921)." *Clinical Cancer Research*, vol. 25, no. 11, 2019, pp. 3229-38. [https://doi.org/10.1158/1078-0432.CCR-18-2675](https://doi.org/10.1158/1078-0432.CCR-18-2675).

National Cancer Institute. "Adavosertib and Irinotecan Hydrochloride in Treating Younger Patients with Relapsed or Refractory Solid Tumors." *ClinicalTrials.gov*, NCT02095132, U.S. National Library of Medicine, [https://clinicaltrials.gov/study/NCT02095132](https://clinicaltrials.gov/study/NCT02095132).

Open Targets Platform. "BUB1B (ENSG00000156970)." *Open Targets*, [https://platform.opentargets.org/target/ENSG00000156970](https://platform.opentargets.org/target/ENSG00000156970).

RCSB PDB. "5JJA: Crystal Structure of a PP2A B56gamma/BubR1 Complex." *RCSB Protein Data Bank*, [https://www.rcsb.org/structure/5JJA](https://www.rcsb.org/structure/5JJA).

———. "5KHU: Human APC/C-CDC20-MCC (APC15 Deletion Mutant)." *RCSB Protein Data Bank*, [https://www.rcsb.org/structure/5KHU](https://www.rcsb.org/structure/5KHU).

———. "6TLJ: Cryo-EM Structure of APC/C-MCC at 3.8 Å." *RCSB Protein Data Bank*, [https://www.rcsb.org/structure/6TLJ](https://www.rcsb.org/structure/6TLJ).

Reactome. *Reactome Pathway Database*, [https://reactome.org/](https://reactome.org/).

UniProt Consortium. "BUB1B_HUMAN (O60566)." *UniProtKB*, [https://www.uniprot.org/uniprotkb/O60566/entry](https://www.uniprot.org/uniprotkb/O60566/entry).

Weigert, Alexander, and Bernd Hoppe. "Nephrolithiasis and Nephrocalcinosis in Childhood—Risk Factor-Related Current and Future Treatment Options." *Frontiers in Pediatrics*, vol. 6, 2018, p. 98. [https://doi.org/10.3389/fped.2018.00098](https://doi.org/10.3389/fped.2018.00098).

Zhang, Na, et al. "Unique Progerin C-Terminal Peptide Ameliorates Hutchinson-Gilford Progeria Syndrome Phenotype by Rescuing BUBR1." *Nature Aging*, vol. 3, no. 2, 2023, pp. 185-201. [https://doi.org/10.1038/s43587-023-00361-w](https://doi.org/10.1038/s43587-023-00361-w).

