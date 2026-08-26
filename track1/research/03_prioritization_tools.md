# Variant Prioritization Tool Landscape 2024-2026 (scout: PrioritizationTools, 2026-08-26)

Citation classes: [L] journal · [A] arXiv/preprint · [G] GitHub · [H] Hugging Face · [W] web/docs.

## Master table (runnable, CPU-only)

| Tool | Category | Input | Comp-het | Local vs API | Effort | Repo/Source |
|---|---|---|---|---|---|---|
| **Exomiser 13.1** | Phenotype ranker (integrated) | VCF + HPO | ✅ native `AUTOSOMAL_RECESSIVE_COMP_HET` on singletons; AR MAF 2% default | Local Java jar, ~20GB data, 12GB RAM for 4.4M-variant WGS | Low-Med | exomiser/Exomiser 259★ AGPL active [G] |
| LIRICAL 2.4 | LR-based pheno ranker | HPO (+VCF) | Partial (per-model LR) | Local Java; uses Exomiser data ≥2406 | Low | TheJacksonLaboratory/LIRICAL 43★ |
| Phen2Gene | HPO→gene prior | HPO list | n/a | Local 0.94s + free REST API (no auth) | Very low | WGLab/Phen2Gene MIT |
| AMELIE 2 | NLP literature ranker | genes + HPO | n/a | Web amelie.stanford.edu | Very low | [W] |
| Phrank | IC/Bayesian pheno ranker | HPO + gene list | n/a | bitbucket bejerano/phrank; phrank-py PyPI 2026 | Low | Genet Med 29997393: disease top-1 26% vs Phenomizer 3.6% on 169 DDD exomes |
| ~~ParseFEP~~ | **PHANTOM** (name collision w/ VMD plugin jhenin/parseFEP) | — | — | — | — | do not hunt |
| **AlphaMissense** | missense DL | missense SNVs | n/a | hg38 TSV ~1.1GB; HF katielink/dm_alphamissense; CC BY 4.0; VEP plugin; thr 0.564 = 90% precision | Low | google-deepmind/alphamissense 633★ (archived 2026-04) [G][H] |
| REVEL v1.3 | missense ensemble(13) | missense | n/a | 1.3GB Zenodo 7072866; in dbNSFP | Very low | AJHG 99:877 |
| CADD v1.7 | all-types | any | n/a | 81GB table or REST API | Med/Low(API) | cadd.gs.washington.edu |
| EVE | evolutionary VAE | single-aa | n/a | precomputed evemodel.org (3,219 proteins); →popEVE in dbNSFP v5 | Very low | OATML-Markslab/EVE 202★ MIT |
| SpliceAI | splicing DL | VCF+FASTA | n/a | pip, CPU-viable; precomputed genome VCFs (Ensembl FTP MANE SNVs); cutoffs 0.2/0.5/0.8 | Low-Med | Illumina/SpliceAI (archived); models CC BY-NC |
| SpliceVault | mis-splicing atlas | VEP plugin + TSV | n/a | OUT_OF_FRAME_EVENTS≥3 = stringent | Low | Ensembl/VEP_plugins 113+ |
| MMSplice/MTSplice | splicing tissue-aware | VCF+GTF+FASTA | n/a | pip, deltaLogitPSI | Low | gagneurlab 43★ MIT |
| LOFTEE | HC LoF | VEP plugin | n/a | grch38 branch; needs human_ancestor.fa+PhyloCSF+GERP | Med | konradjk/loftee 200★ |
| **Ensembl VEP 116** | annotation engine | VCF | ✅ bundled **haplo (Haplosaurus)** consumes phased VCF → transcript haplotypes, resolved frameshifts | offline cache ~20GB + FASTA; Docker; REST | Med | Ensembl/ensembl-vep 566★ Apache-2.0 |
| **dbNSFP 4.9a** | mega-annotation | VCF join | n/a | ~50GB: REVEL+CADD+AM+EVE+conservation+**gnomAD v4/TOPMed AFs**, bgz+tabix VEP/SnpSift-ready | Med | zenodo.org/records/14419644 |
| **gnomAD v4** | AF | — | n/a | **do NOT download 742GB genomes**; free GraphQL API on candidate set; chr-wise exome sites 58GB; constraint TSV 4.2MB | Low (API) | gnomad.broadinstitute.org |
| bcftools csq | lightweight consequence | VCF+GFF | ✅ `--phase` uses PGT/PID haplotype-wise | local | Very low | samtools/bcftools |
| **WhatsHap 2.8** | read-backed phasing | VCF+BAM | ✅ core purpose: in-cis/in-trans; PS-tagged output; N50 stats | pip, CPU fine | Low-Med | whatshap/whatshap MIT |
| GATK PGT/PID | in-VCF phasing (present!) | — | ✅ same PID + 0|1 vs 1|0 = **in-trans comp-het**; short-range only | zero (parse tags) | Very low | GATK docs |
| OpenCRAVAT 2.4 | modular annotation | VCF | ❌ no MOI engine | pip/docker; **ships MCP server for LLMs** | Low | KarchinLab/open-cravat 153★ |
| ClinVar / DECIPHER / MME / VarSome | clinical DBs | gene/variant | n/a | all free; ClinVar bulk FTP ~1GB; MME GA4GH API v1.1 | Very low | |

## Category verdicts

1. **Phenotype rankers:** Exomiser backbone (only tool combining HPO match + filtering + frequency + native singleton comp-het MOI + REVEL/MVP/LOEUF); Phen2Gene/LIRICAL/Phrank cross-checks.
2. **Effect predictors:** all precomputed/CPU-friendly; dbNSFP shortcut carries nearly everything incl. gnomAD v4 AFs.
3. **Annotation/frequency:** VEP offline cache anchor; haplo plugin uses phasing; gnomAD via API on filtered candidates.
4. **Comp-het (THE lever here):** provided VCF's PGT/PID = GATK physical phasing. Same PID, opposite phase (0|1 vs 1|0) = in-trans. Even Genomics England Mira tiering ignores phase → phase-aware ranking is a genuine differentiator. Blocks are short → WhatsHap after re-alignment extends them. Exclude "comp-het" pairs proven in-cis.
5. **LLM interpreters:** evidence synthesizers, not rankers — use on shortlist. GPT-4 on 5,267 phenopackets: 19.2% rank-1, 32.5% top-10 [A: medRxiv 2024.07.22.24310816]. RareBench (arXiv 2402.06341): KG few-shot > zero-shot; GPT-4 ≈ senior specialists. VariantBench (ACL 2025): AF cues mastered, high-impact ACMG rules underused. AI-CURA (Sci Transl Med adz4172): DeepSeek-R1 100% specificity on literature rules. **DiagAI (medRxiv 2025.02.04.25321641): 74% top-rank with HPO, beats Exomiser v13 & AI-MARRVEL on 966 exomes.** OpenCRAVAT MCP → LLM grounding. HF: cerebras/exome_bench + STRAND; weijiang99/clinvarbert Apache-2.0.
6. **Databases:** all free tiers sufficient; DECIPHER functional-similarity matching; MME for gene-level case matching (incl. parental-miscarriage angle).

## Recommended phase-first pipeline (scout's, mirrored in approaches doc)

1. Parse PGT/PID first — zero-cost in-cis/in-trans tagging per gene.
2. WhatsHap on re-aligned FASTQs to extend phase blocks.
3. VEP offline + AlphaMissense/SpliceAI/SpliceVault/LOFTEE; dbNSFP or gnomAD API for AF.
4. Exomiser AR-COMP_HET on phased VCF with the 8 HPO terms; Phen2Gene/LIRICAL cross-check.
5. LLM pass on top ~20 genes with ACMG evidence bundles, grounded via OpenCRAVAT-MCP/RAG over ClinVar/OMIM/DECIPHER.
