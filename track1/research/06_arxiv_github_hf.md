# arXiv + GitHub + Hugging Face: AI-Native Approaches (scout: CrossArxivHf, 2026-08-26)

Classes: [P] peer-reviewed · [A] arXiv/preprint · [G] GitHub · [H] HF · [W] web.

## 1. End-to-end agents (phenotype + VCF → ranked causal variants)

1. **DeepRare** — Nature 2026 (10.1038/s41586-025-10097-9) [P]. MCP-inspired 3-tier multi-agent (DeepSeek-V3 host, 40+ tools, self-reflection); ingests free text + HPO + **raw VCF**; ranked diagnoses with evidence chains. 6,401 cases: HPO Recall@1 57.18% (beats best reasoning LLM by 23.8pp); HPO+WES Recall@1 **69.1% vs Exomiser 55.9%** on 168 validated WES; 95.4% expert agreement. Code MAGIC-AI4Med/DeepRare [G]; DBs Angelakeke/DeepRare [H]; app deeprare.cn [W]. Strongest published evidence class.
2. **DAVP** (Deep Agentic Variant Prioritization) — medRxiv 2026.02.17.26346421 [A] + Muti-Kara/davp [G] Apache-2.0. Exomiser prefilter → top-256 genes → Gemini-2.5-Flash ranking → KG evidence → pairwise-elimination tournament → top-3. Gene Recall@1/@3 **70.3%/86.4%** vs Exomiser 57.0/66.6; UDN hard set 51.3/76.0 vs 47.7/54.3. Exactly our task shape; runnable code.
3. **AIVARI** — ICML'26 WS (openreview By0A3FZ4Tf) [A]. Gemini-3-Flash agent, one rollout per candidate gene, tools get_omim_entry/get_clinvar_detail/get_variant_detail; **explicit AR comp-het logic in prompts (P/LP+P/LP w/ phenotype → positive; in-cis → single-hit)**. Group sensitivity 0.905. Prompt skeleton directly copyable for our pair.
4. **AI-MARRVEL (AIM)** — NEJM AI 2024 (10.1056/AIoa2300009) [P]. RF over 3.5M variants, 103 features; **doubled solved cases vs Exomiser/LIRICAL/PhenIX/Xrare**; recessive-fine-tuned variant exists. Web API ai.marrvel.org — minimal effort. **LA-MARRVEL** (arXiv:2511.02263): LLM rerank over AIM + 10× ranked voting, +20-30pp over Exomiser; ablation: removing HPO text −20.2pp Recall@1. Replicate the pattern.
5. **MARRVEL-MCP** — AJHG 2026 (10.1016/j.ajhg.2026.04.012) [P]. MCP server over MARRVEL's 21 DBs; LLM composes rsID→coords→ClinVar→gnomAD→dbNSFP workflows. hyunhwan-bcm/MARRVEL_MCP [G]; benchmark on HF (10.57967/hf/7806) [H]; demo chat.marrvel.org.

**Counterweight (cite in report):** Reese et al. EJHG 2026 (10.1038/s41431-026-02054-5): 5,213 phenopackets, best LLM top-1 23.6% vs Exomiser 35.5% phenotype-only → **winning pattern = classical ranker + LLM reranker/orchestrator**, not LLM-alone.

Benchmarks: **RareBench** (arXiv:2402.06341 KDD'24; HF chenxz/RareBench) GPT-4 ≈ senior specialists, dynamic few-shot +20.2pp; RareSeek-R1 (arXiv:2511.14638) 70B GPU — ideas only; GraphRareBench MRR 0.740; STARVar (BMC Bioinf 24:294); GP-GPT (arXiv:2409.09825).

## 2. GitHub tooling beyond the standard stack

- **exomiser/Exomiser v15.0.0 (Feb 2026)** active; WGS FULL mode ~16GB RAM. Base stage of every winning agent.
- **abyzovlab/CNVpytor** 217★ — read-depth + BAF segmentation, `rd_call_mosaic` mode → **karyotype-from-WGS to quantify variegated aneuploidy** (CIN phenotype made computable).
- **XiaoxuYangLab/DeepMosaic** 52★ — CNN mosaic SNV caller from pileup images, hg38, CPU-feasible (if VAF skew appears).
- **ichorCNA** — aneuploidy fraction from low-pass (needs PoN); GATK gCNV needs 30-sample cohort (bad fit); Canvas archived (avoid).
- **CAGI precedents:** genomeinterpretation/CAGI50; **gagneurlab/cagi6_sickkids** (genome+transcriptome+HPO → XGBoost over VEP/CADD/SpliceAI/EVE features) — closest published precedent; read Methods.pdf.
- **google-deepmind/alphamissense** 633★ (predictions CC-BY; repo archived); mtmorgan/AlphaMissenseR.
- **ntranoslab/esm-variants** 88★ + HF Space (genome-wide ESM-1b/1v catalog, Brandes Nat Genet 2023).
- **OATML-Markslab/EVE** + **popEVE** (proteome-wide constraint; >100 novel RD genes medRxiv 2023.11.27.23299062).
- **RaSP** — precomputed ΔΔG for **all single-AA substitutions across 23,391 human proteins on AlphaFold structures** (ERDA vaex) — zero-compute stability readout. eLife 12:e82593.
- **bw2/SpliceAI** (maintained fork) + **tkzeng/Pangolin** 88★; gnomAD v4 itself annotated with CADD v1.6 + masked SpliceAI + Pangolin (gs://gnomad-insilico).
- **ArcInstitute/evo2** 3,988★ Apache — DNA LM; needs GPU → use free NVIDIA hosted API (build.nvidia.com/arc/evo2-40b).
- **GPN-MSA** (`pip install gpn`; bioRxiv 2023.10.10.561776) — log-likelihood ratio beats CADD/phyloP/ESM-1b on ClinVar-vs-gnomAD **and OMIM regulatory-vs-common** — strongest for noncoding candidates.

## 3. Hugging Face directly downloadable

- **katielink/dm_alphamissense** — AlphaMissense_hg38.tsv.gz (71M missense predictions) + gene means; join by CHROM/POS/REF/ALT.
- **DSIMB/PATHOS-PLM-EMBEDDINGS** — 7.15TB parquet PLM embeddings (ESM-C 600M, ESM-2 650M, Ankh2) for every missense substitution in 20,416 SwissProt proteins; DuckDB shard fetch = 2 HTTP requests per protein.
- **HuggingFaceBio/Carbon-3B/8B** + clinvar-vep-final + dna-benchmarks — HF DNA LM family, zero-shot ClinVar VEP; Carbon-3B "matches or beats Evo2 7B".
- **arcinstitute/evo2_*** Apache checkpoints; **InstaDeepAI/nucleotide-transformer-v2-250m** (CPU-practical); **multimolecule/spliceai** (3.49M params, CPU-trivial).
- Benchmarks: chenxz/RareBench, Angelakeke/DeepRare, MARRVEL-MCP hf/7806. Protein LM standard: ESM-1v ensemble-of-5 (Livesey & Marsh 2023: top VEF rank on DMS).

## 4. Agent evidence-quality table

| System | Input→Output | Evidence | Verdict |
|---|---|---|---|
| DeepRare (Nature 2026) | text/HPO/VCF → ranked dx + traced evidence | 6,401 cases, 2 WES cohorts, r=0.87 vs 8 physicians | Strongest; reproducible |
| DAVP (medRxiv 2026) | Exomiser-filtered VCF + HPO → top-3 | 646 cases, head-to-head wins | Good; clone code |
| AIVARI (ICML'26 WS) | HPO + candidates → reportability | 300 cases vs signed reports | Copy comp-het prompts |
| LA-MARRVEL | AIM top-N → rerank + ACMG trace | beats Exomiser 20-30pp | Reimplement pattern |
| MARRVEL-MCP (AJHG 2026) | NL → multi-DB workup | HF benchmark | Tool layer |

**No published agent validated on constitutional mosaic aneuploidy — CIN angle is novel territory.**

## 5. CPU recipe for the final 2 missense variants

1. **SpliceAI Lookup** (spliceailookup.broadinstitute.org) — SpliceAI + Pangolin + AlphaMissense + PrimateAI-3D + PromoterAI in one query.
2. AlphaMissense TSV lookup (HF mirror).
3. ESM-1v 5-model mean via ntranoslab CLI (CPU minutes) or PATHOS embeddings.
4. EVE (evemodel.org) + popEVE constraint.
5. RaSP precomputed ΔΔG (>2 kcal/mol destabilization supports pathogenicity).
6. GPN-MSA LLR — best for any noncoding candidate.
7. Map on AlphaFold DB model (AlphaMissenseR vignette); skip AlphaFold3 for point effects.

## Top-10 AI-native approaches by (impact × prob)/effort

| # | Approach | I | P | E |
|---|---|---|---|---|
| 1 | Exomiser 15 AR-mode comp-het base ranker | H | H | L |
| 2 | AI-MARRVEL web (recessive model) | H | H | VL |
| 3 | DAVP-style LLM tournament over top-256 | H | M-H | M |
| 4 | AIVARI per-gene rollout prompts (AR logic) | H | H | L-M |
| 5 | AlphaMissense annotation layer | M-H | H | VL |
| 6 | DeepRare second opinion | H | M | M |
| 7 | SpliceAI+Pangolin (fork local + Lookup web) | M | H | VL |
| 8 | Phen2Gene + LIRICAL consensus | M | M | VL |
| 9 | CNVpytor mosaic profile → feed CIN evidence into agent prompt | M-H | H(narrative) | L |
| 10 | 2-variant deep dive: ESM-1v+EVE+RaSP+GPN-MSA | M | H | L |

Kill-list for this CPU box: Evo2 local, RareSeek-R1 70B, MedFound-176B, GATK gCNV cohort, Canvas.
