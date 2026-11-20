# Run audit — task tam11b5f, 8 trajectories

Scope: all 8 deliverables read in full; all 8 transcripts traversed (171–244 tool calls each,
116–156 thinking blocks). Every numeric claim below was recomputed from `room/` or read from the
source figure/structure. Thinking blocks are **summarised, not raw** (`thinking_summary_status:
ready`), so no claim here rests on what a run "considered internally"; ToolUse and ToolResult are
raw and are what establish retrieval.

Classification is the exploration's, for the writer's adjudication. Tier assignment is not a
failure-mode naming.

## Ground truth established for this audit

| Quantity | Value | Source |
|---|---|---|
| Library | 3,580 guides = 795 genes x 4 + 400 BRDN control guides | `crispr_invivo_guide_counts.csv.gz` |
| Tumours | 141 (71 NTC bg, 70 STK11 bg); G1–G4 are **all** NTC bg, G5–G8 **all** STK11 bg | same |
| Mgat1 STK11-selective rank | **#1 of 795**; differential −2.32 (plasmid ref) / −2.19 (matched-baseline, median) | recomputed |
| Mgat1 by group | G1 −1.40, G2 −1.21, G3 −0.83, G4 −0.37; G5 −2.39, G6 −3.48, G7 −3.26, G8 −3.16 | recomputed |
| Arm signature | G1/G5: Cd274 +0.73/+0.63, Ptpn2 +0.39/−0.19, Stat1 +0.76/+0.41 (no immune selection) | recomputed |
| Glyco (A375 / AM) | KO 1.5231e10 / NTC 9.3026e9 = **1.6373**; 909 sites; **245 up >2x (27.0%)**, **6 down**, **658 unchanged**; non-mover centre 1.1198 → **1/1.1198 = 0.893**; 1/1.6373 = **0.611** | recomputed |
| Glyco channels | AM = A375, NH = NCI-H1703 — two cell lines, not two fractions | `experimental_records.pdf` L159–165 |
| C3744–UDP | **23.93 Å**; C3744–Mn 25.82 Å; C3744–D289 **16.11 Å**; C3744–D211 27.36 Å | `MGAT1_C3744_UDP.cif` |
| C3744 pocket | **16 residues, Y388–W444, zero shared with the 17-residue UDP site** | same |
| 315–332 loop | ordered 31/31 in ternary; missing 316–332 apo; 315–331 compound-only; 320–324 UDP-only | all 5 CIFs |
| SPR | binding UDP 31, ANT-3744 0.4; competition UDP 32→20, ANT-3744 0.4→0.2 | `spr_binding/competition.csv` |
| DSF | ΔTm +2 UDP, +6 ANT-3744, +8 both (apo 49 °C) | `dsf_thermal_shift.csv` |
| Immobilisation | ~9000 RU (binding), ~3600 RU, ~3500 RU (competition); records state levels **differed** | records §6.4 |
| Potency assay | top final concentration **100 µM**; enzyme MGAT1(T30–N445); crystal/SPR A104–N445 | records §6.2–6.4 |
| Compounds | 0592 purchased, IC50 197, KD 32.2*, sol 11.8; 1938 acquired >100 (40%, n=2); 2214 acquired 74 (60%, n=2); 3744 synthesised 0.814; 4267 synthesised 0.043, sol 96.4 | `compound_properties.csv`, `assay_figures.pdf` p2 |

**The golden's own arithmetic checks out.** 658 non-movers exact; 0.893 and 0.611 are the
reciprocals of the measured 1.1198 and 1.6373, consistently in NTC/KO orientation; 23.93 Å,
16-residue pocket and zero site overlap all exact.

---

## TIER 1 — deviations, discrepancies and gaps

| # | Run(s) | n | Class | What the audit found | Verification |
|---|---|---|---|---|---|
| 1 | all 8 | 8/8 | Deviation, substantive | Safety is reported as an absence of client data and deferred to a tolerability readout inside a later study. No run takes a position on on-target risk; none names cardiomyocyte deletion, dilated cardiomyopathy, embryonic lethality, the autoimmunity overlap with intended pharmacology, or bronchial epithelium. O2 carries no safety sentence at all. Golden pre-registers this exact shape as not taking a position. | Sentence-level sweep of all 8 memos |
| 2 | all 8 | 8/8 | Deviation, upstream cause of #1 | Six declare as a positive commitment that no outside knowledge was used as evidence (F1, F2, F3, O2, O3, O4 — e.g. O3 "No outside data or literature was used as evidence"). The golden's safety section is the one marked "Named domain knowledge, not from the package." The commitment rules out the only basis for that pillar. | Direct quotes, all 6 |
| 3 | all 8 | 8/8 | Deviation, headline only | Opens "do not advance" / "hold"; golden opens "advance, but not into IND-enabling work." Substance underneath is identical in all 8 (no IND-enabling spend, gated cell-and-mechanism package, keep the target). | §1 of each memo |
| 4 | all 8 | 8/8 | Analysis gap | None performs the golden's bulk-centre test. No run reports 0.893, 0.611, the 245/658 split, 27.0%, or 317-vs-16. Seven report the ~1.6x channel imbalance and then decline the magnitudes instead of using them. The three runs matching `0.89` match other quantities (F3 permutation Δ, O4 tumour-volume ratio, O3 guide log2FC). | Regex sweep + recomputation |
| 5 | all 8 | 8/8 | Coverage gap | Golden study 7, cardiac safety pharmacology, absent. O3's only cardiac token is `hERG` inside a generic developability list, not an on-target position. | Next-steps sections |
| 6 | O3 | 1 | **Foreclosed inference** | "It binds together with UDP and cooperatively: each ligand raises the other's affinity 1.6–2x, and the DSF shifts add (2 + 6 = 8 °C)." Golden forecloses: the shifts are two-fold across separately prepared surfaces at differing immobilisation. Compounding it, **additive ΔTm is the signature of independent binding, not cooperativity** — O3's cited evidence argues against its own conclusion. O3's own citation (records §6.4) is the section carrying the foreclosure. | records §6.4; dsf CSV; arithmetic 32/20=1.6, 0.4/0.2=2.0 |
| 7 | O2, O3 | 2 (both Opus) | **Foreclosed inference** | Reads the lectin/mass-spec magnitude disagreement as bearing on whether the MS is sound. O2: "This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference." O3: "This conflicts with the ≈96% PHA-L loss and fits TMT ratio compression or misassignment." Golden: the readouts are not commensurable and "the disagreement is not evidence that either is wrong." Near-identical constructions; no Fable run makes the move. | Sentence sweep, both memos |
| 8 | F2 | 1 | **Factual error + transcript contradiction** | Deliverable: "Immobilisation levels per run are not recorded, so I raise it as a query, not a finding." Records §6.4 state all three levels (~9000, ~3600, ~3500 RU) **and** "protein immobilization levels differed." F2's own transcript reasons explicitly "...or ~29% if that run used the ~3600 RU surface", and its evidence ledger cites both the ~9,000 and ~3,500 RU surfaces. Retrieved, used, then asserted absent. | records §6.4; F2 transcript; F2 ledger |
| 9 | O3, F1 | 2 | Deviation | Rest a substantive conclusion on the inferred arm mapping. O3 concludes the dependency is largely immune-dependent from the STK11-minus-NTC differential per inferred arm; F1 computes per-arm contrasts (G5−G1, G6−G2, G7+8−G3+4) and concludes substantially T-cell-independent. Golden: aggregate on the background label, which every column carries; no conclusion should rest on inferred arms. Both estimands are arithmetically reproducible — the divergence is the choice, not the maths. | Recomputation; G6−G2 = −2.27 matches O3 exactly |
| 10 | O1, O2, O3 | 3 | Coverage gap | Mouse-enzyme potency not named as a required study. Every compound measurement is against human enzyme and every in vivo model is mouse. All 4 Fable runs raise it; O4 raises it. Their species-word hits are the unstated hepatocyte species, a different point. | Next-steps sweep, all 8 |
| 11 | O2 | 1 | Retrieval scope | Never names A375 (0 occurrences; H1703 x6), so the A375 half of the glycoproteomics — the half carrying the golden's foreclosure evidence — is not visibly in scope. | String count, all 8 |
| 12 | O3, O4, F3 | 3 | Retrieval scope | Do not state that the glycoproteomics is two cell lines rather than two fractions, though the records map AM→A375 and NH→NCI-H1703 explicitly. | records L159–165 |
| 13 | 7 of 8 | 7/8 | Scope addition | A client-facing section the prompt did not request: questions to put, or data-integrity issues to resolve (F1 §7, F2 §7, F3 §6, F4 §6, O1 §8, O2 §8, O3 §7). O4 substitutes Appendix C. Three also open a scorecard (O1, O2, F2). Golden has neither. | Heading extraction |
| 14 | all 8 | 8/8 | Level | 3,996–8,722 words against the golden's 1,770 (2.3x–4.9x). Fable the longer side (median 5,828 vs 4,107). Protocol content stays low (0–4 sentences per run in next-steps), so the drift is volume, not altitude. | Word counts; protocol regex |

---

## TIER 2 — verified correct

| # | Run(s) | n | What was done correctly | Verification |
|---|---|---|---|---|
| 1 | all 8 | 8/8 | **Full retrieval coverage.** Every run touched all 12 room artifacts. Lowest-touched is the structure set (16 refs, O4); figures dominate (phenotype 70–192 refs). No run worked from a subset. | Tool-call inventory across 1,576 calls |
| 2 | all 8 | 8/8 | **The channel-normalisation false optimum was avoided.** No run normalised the glycoproteomics channels to equal total. Seven state the ~1.6x imbalance and route around it six different ways. | Regex sweep + recomputation |
| 3 | all 8 | 8/8 | **The arm inference is flagged as inference** in every run. None presents the mapping as supplied by the files. | Established in the divergence pass |
| 4 | F1, O1, O3, F2 | 4 | **The arm inference is convergent and genuinely data-grounded** — all four independently reach G1/G5 nude, G2/G6 isotype, G3/G4/G7/G8 anti-PD-1. Recomputation confirms: G1/G5 show no IFN/PD-L1 selection (Cd274 +0.73/+0.63, Ptpn2 +0.39/−0.19), G2 shows Cd274 −4.01, G3/G4/G7/G8 show Cd274 ≈0. Not shared hallucination. | Recomputed per-group gene scores |
| 5 | F3, F4, O4 | 3 | **Explicitly quarantined the inference from primary conclusions** — matching the golden. F3: "The 'no PD-1 effect' conclusion does not depend on which C57BL/6 group is which." F4: "The Stk11-selectivity result does not depend on it. The T-cell and PD-1 statements do; hence Gate 0." O4: "not used for any primary conclusion." | Direct quotes |
| 6 | O4 | 1 | **Mgat1 #1 of 795 reproduces under O4's own stated pipeline.** O4 states −2.21 with z −8.1, BH-FDR 1e−13; re-running its stated recipe (per-tumour log2(CPM+1) vs matched baseline, centred on the 400 control guides, gene = mean of 4, median−median) gives **−2.194, rank 1/795**. | Full recomputation |
| 7 | F4 | 1 | **Forecloses the cooperativity reading, matching the golden**, and lists it as set aside: "'Cooperative with UDP' is not established. The shifts are ≤2-fold, reported as single values, on different sensor surfaces." The only run to get this foreclosure right explicitly. | records §6.4 |
| 8 | O4 | 1 | **Caught a genuine data-room inconsistency no other run reported**: assay_figures p4 legend reads "100 µM HTS ANT-3744" while the records state ANT-3744 was synthesised in house. Verified by extracting and reading the embedded PNG. | Figure image, p4 |
| 9 | O1 | 1 | **The IC50-vs-KD plot claim is exact**: ~25 plotted compounds, only 3 traceable to the registry. The plot carries ~26 points and labels exactly ANT-4267, ANT-3744, ANT-0592* — the only three registry entries with both an IC50 and an SPR KD. | Figure image, p5 |
| 10 | O1 | 1 | **Correct biochemistry, unprompted**: flags the rise of HexNAc(2)Hex(5)Fuc(1) in knockouts as implausible because core fucosylation requires MGAT1's product. FUT8 does require the MGAT1-added GlcNAc. Sound mechanistic inference used to triage an assignment. | Domain check |
| 11 | O3 | 1 | **Loop-ordering claim exact**: "the 315–332 loop is fully ordered [in the ternary], while it is disordered in apo and compound-only crystals." Ternary 31/31 present; apo missing 316–332; compound-only missing 315–331. | All 5 CIFs |
| 12 | O3 | 1 | **Two further exact retrievals**: ANT-0592's IC50 (197 µM) is above the assay's stated 100 µM top concentration; and every construct tested lacks the transmembrane helix (T30–N445 for assays, A104–N445 for crystal/SPR). | records §6.2–6.4 |
| 13 | O2 | 1 | **Structure numbers exact**: pocket Y388–W444 (16 residues, verified) and 16 Å from the catalytic base D289 (measured 16.11 Å). | CIF recomputation |
| 14 | F2 | 1 | **Structure numbers exact**: 388–444, 24 Å from UDP (23.93), 26 Å from Mn (25.82). | CIF recomputation |
| 15 | F3 | 1 | **"Shares no residue with the donor site" is exactly right** — the 16-residue C3744 pocket and the 17-residue UDP site have zero intersection. | CIF recomputation |
| 16 | O4 | 1 | **Ligand rebuilt from the CIF and reconciled to the registry**: C23H25N5O3 (CIF heavy atoms C23 N5 O3), MW 419.5 vs registry 419, TPSA 110 vs 110. | CIF + compound CSV |
| 17 | O4 | 1 | **SPR and DSF transcribed exactly**: "KD 0.4→0.2 µM with 5 mM UDP; UDP KD 32→20 µM with ANT-3744; DSF ΔTm +2 (UDP), +6 (ANT-3744), +8 °C (both)" — every value matches the CSVs. | Both CSVs |
| 18 | all 8 | 8/8 | **The acquired compounds are correctly discounted.** Figure p2 confirms ANT-1938 IC50 >100 µM / 40% inhibition / n=2 with flat, dose-independent SPR, and ANT-2214 74 µM / 60% / n=2 with non-saturating dose-independent SPR, against UDP titrating cleanly to KD 31 µM on the same assay. Runs citing catechol/hydrazone motifs are reading the drawn structures correctly. | Figure image, p2 |
| 19 | all 8 | 8/8 | **ANT-0592 correctly held as unusable quantitatively.** 197/11.8 = 16.7x solubility (O1 "16.7x", F3 "17x" both correct); 32.2/11.8 = 2.7x (O1 correct); the KD asterisk is undefined anywhere in the room. | compound CSV |
| 20 | F2 | 1 | **Cell-line attribution sourced, not assumed**: maps AM→A375 and NH→NCI-H1703 and reports per line. The records supply exactly this mapping. | records L159–165 |
| 21 | F2 | 1 | **Gate arithmetic exact**: "10 µM ... about 230 times the biochemical IC50 of ANT-4267 and about a tenth of its kinetic solubility" — 10/0.043 = 232.6; 10/96.4 = 10.4%. | compound CSV |
| 22 | F4 | 1 | **Potency-ratio arithmetic exact**: ANT-2118 "roughly 600-fold weaker than ANT-4267" — 25.6/0.043 = 595. | compound CSV |
| 23 | F3, O4 | 2 | **Powering derived from the client's own variability** rather than asserted: F3 "about 17 mice per arm ... about 36 for two-thirds of it, more if they are SEM"; O4 "≈11–20 per arm". Both state the SD/SEM dependency rather than hiding it. | Next-steps sections |
| 24 | 5 of 8 | 5/8 | **Independently found the duplicate library pair** with closely agreeing statistics: r = 0.988 (F3), 0.98 (F4), log-CPM 0.984 / raw 0.995 (O3), against a next-best pairing of 0.76 (F3) or median 0.67 (O3). F3 draws "effective n for Group 3 is 14"; F4 reads the IDs as a digit transposition. Not in the golden's set-aside list. | Set-aside sections |
| 25 | all 8 | 8/8 | **Original analysis throughout — no run reported numbers it did not compute.** Co-culture MGAT1 ranks reproduce exactly under each run's stated pipeline (−0.816 rank 10 attempt-1 style; rank 7 mean+5; −0.852 rank 12 median+0.5 ≥3 guides). 1,576 tool calls, 118–192 bash invocations per run. | Recomputation under each stated recipe |
