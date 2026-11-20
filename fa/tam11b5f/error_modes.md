# tam11b5f — error-mode ledger (v1, 2026-11-20)

Task `e55870a045744a9e932736ae7ca1822f`, problem version `7d0fedb4`. Panel: Opus 5.5 `de39df86` attempts 1–4, Fable 5.2 `c638eb2d` attempts 1–4. Trajectory-only mode: both jobs ran under the default grader with `grader_guidance`, `rubric` and `grader_files` all null, so no mode rests on a score, no run is ranked by one, and the `Graded?` field is `n/a` throughout.

Change note, v1: first full ledger. Mode 6 of `submittability.md` was held below the floor and promoted after a wider screen; the reason is in `qa_triage.md`.

**Numbering changed.** This ledger is ordered by prevalence then consequence, so the numbers differ from `submittability.md`. Crosswalk:

| Ledger | Short name | Was |
|---|---|---|
| 1 | `no-cross-species` | 1 |
| 2 | `spr-surface-unapplied` | 2 |
| 3 | `arm-labels-unsourced` | 6 |
| 4 | `lectin-ms-commensurable` | 3 |
| 5 | `no-safety-position` | 4 |
| 6 | `unmeasured-product-side` | 5 |

Short names are stable; cite those, not the numbers.

## Reading coverage

| Run | Coverage |
|---|---|
| O3 `bc8b9e20` | Deliverable read in full; transcript read in full |
| F1 `aa6a0794` | Deliverable read in full; transcript read in full |
| O2 `2caa3b04` | Deliverable read in full; transcript searched for modes 1, 2, 3, 6 |
| O1 `bd63c97e`, O4 `409bdac0`, F2 `734093b7`, F3 `73e1ddd7`, F4 `69bb2ad2` | Deliverables read in full; transcripts searched for each candidate mode |

Chosen for full reading by visible errors in the headline output, one run per model: O3 carried candidates for four modes, F1 for three. No run was chosen or ordered by score.

Every prevalence count below was confirmed by reading the matched text in each run's deliverable, and every numeric probe was run in at least two spellings. Where a tight pattern gave the tidier answer it was wrong twice: F2 was briefly scored as missing the mouse-potency requirement because the pattern excluded table-cell pipes, and Mode 6 was briefly held at one instance because the pattern tested only the anti-PD-1 sentence. Both are corrected here.

**Thinking channel:** summarised, not raw (`thinking_summary_status: ready`); 116–156 blocks per run, 70–100% carrying text, median ≈550 characters. No claim about what a run weighed internally is supportable, so the raised-then-abandoned shape is excluded. Modes 2 and 6 rest on raw tool output and the deliverables; the thinking quotes corroborate only and are marked.

## Verdict map

| Run | Advance? | Positioning kept? | Gate 1 | Divergence |
|---|---|---|---|---|
| O1 | No — hold behind gates | Reframe; selectivity rests on one model | Cellular proof of mechanism | — |
| O2 | No — hold at lead stage | Reframe as PD-1-independent sensitiser | Cellular target engagement | — |
| O3 | No — hold, keep the target | Reframe as PD-1-independent sensitisation | Cellular target engagement and glycan PD | — |
| O4 | No — hold at late hit-to-lead | Not supported; effects additive | Cellular pharmacology | — |
| F1 | No — hold, fund a cell package | Not restored by MGAT1 loss | Target engagement in cells | — |
| F2 | No — gated hold | Not supported; drop the checkpoint claim | Cellular target inhibition | — |
| F3 | No — hold the series | "Overcomes checkpoint resistance" not shown | Cellular pharmacodynamics | — |
| F4 | No — hold the ANT series | Not supported; PD-1 blockade adds nothing | Cellular target engagement | — |

Unanimous on every decision the prompt asks for. The golden says "advance, but not into IND-enabling work; fund a bridge package" — the same gate with the word attached to the other side. **There is no verdict split to trace, so every mode below is a flawed route, not a wrong answer.** The pre-registered "known design weakness" is confirmed: the absence of any cellular compound data over-determines the call.

## Ledger index

Ordered by prevalence, then consequence. All six clear the floor of two.

| # | Short name | Class | Runs | Consequence |
|---|---|---|---|---|
| 1 | `no-cross-species` | Adjudication | O1, O2, O3 | Changes the study package: invalidates a named comparator |
| 2 | `spr-surface-unapplied` | Analytical | O2, O3, F2 | Changes the mechanism case and Gate 3 scope; not the verdict |
| 3 | `arm-labels-unsourced` | Referential | O3, F1, F3 | Changes asset positioning: the T-cell and anti-PD-1 claims |
| 4 | `lectin-ms-commensurable` | Synthesis | O2, O3 | Right conclusion, invalid basis. Benign for the verdict |
| 5 | `no-safety-position` | Reasoning | all eight | Omits a decision input the committee needs. **Basis contested** |
| 6 | `unmeasured-product-side` | Synthesis | all eight | Benign for the verdict; unsupported magnitude reaches the client. **Basis generic** |

---

## 1. `no-cross-species` — Adjudication

| Field | Content |
|---|---|
| **Runs** | O1, O2, O3 |
| **Not checked** | Whether any compound inhibits mouse MGAT1, before specifying a mouse efficacy study |
| **Description** | Every compound measurement in the room is against human enzyme: `experimental_records.pdf` §6.1 gives the construct as UniProt P26572, residues T30–N445, and §6.4 the SPR construct as A104–N445 of the same protein. Every in vivo model is mouse: §2 implants MC38 into C57BL/6 and nude mice. All three runs specify a mouse efficacy study as a funded gate and none asks for mouse potency anywhere in the deliverable. O1 specifies "a **2×2 design in vivo** (MGAT1 inhibition × anti-PD-1), run in an STK11-null, lung-relevant syngeneic model **and its isogenic STK11-intact twin**" (L225). O2's efficacy design is "STK11-deficient immunocompetent tumours (ideally a lung model alongside sgSTK11 MC38), in a 2×2 factorial" (L197), and its bring-back criterion 4 asks for "in vivo translation" against "the genetic benchmark" (L225). O3's Gate 4 requires "significant TGI vs vehicle in STK11-null, approaching the KO benchmark (≈50% in MC38 sgSTK11)" (L110). All three are species-aware elsewhere — O1 and O3 both flag that the hepatocyte clearance species is not stated — and none applies the same check to the compound's own pharmacology |
| **Counterfactual** | Require mouse MGAT1 potency and pocket conservation before any mouse efficacy study, compared against the human potency, as golden study 3 states: "**Required before any mouse efficacy study**: every compound measurement is against human enzyme and every in vivo model is mouse". A mouse efficacy study run with a compound of unknown mouse potency is uninterpretable whatever it shows, because a null result cannot be separated from failure to engage the target. O4 shows the full form, including the contingency: "If mouse potency is >3× weaker than human, use a surrogate tool or a humanised-target model" (L247) |
| **Exemplar** | O4. Names the gap — "**G4. Human enzyme only; no selectivity.** Every biochemical, biophysical and structural datum is on human MGAT1, while all in vivo models are murine. There is no mouse Mgat1 potency" (L80) — lists "Mouse Mgat1 potency (needed before any MC38 work)" as a Gate 0 item (L222), and makes it bring-back criterion 3 (L275). F2, F3 and F4 each also require it: F2 Gate 3 asks for "activity on mouse MGAT1" (L138), F4 states "Potency on mouse Mgat1, which every syngeneic experiment depends on, has not been measured" (L153) |
| **Evidence** | O1 memo L225 [transcript]; O2 memo L197 and L225 [transcript]; O3 memo L110 [transcript]. Records §6.1 and §2 reached every run as raw tool output [transcript]. No species-potency reasoning appears anywhere in the three transcripts, across patterns for mouse/murine + potency/IC50/orthologue/conservation and for cross-species [transcript] |
| **Graded?** | n/a |

**Plain language.** The drug was only ever tested against the human form of the enzyme, and every animal experiment uses mice. Three runs designed the expensive animal efficacy study without asking whether the drug blocks the mouse enzyme at all. If it doesn't, the study yields a tumour measurement that cannot be interpreted: you cannot tell a drug that failed from a drug that never reached its target.

---

## 2. `spr-surface-unapplied` — Analytical

| Field | Content |
|---|---|
| **Runs** | O2, O3, F2 |
| **Not corrected for** | The records' statement that each SPR competition experiment used a freshly prepared surface at a differing immobilisation level, before reading a two-fold shift in dissociation constants as a result |
| **Description** | `experimental_records.pdf` §6.4 gives three immobilisation levels — approximately 9000 RU for the direct binding run, 3600 RU for the UDP-as-analyte competition and 3500 RU for the ANT-3744-as-analyte competition — and ends: "SPR experiments were performed separately with a new surface preparation for every experiment; protein immobilization levels differed." `spr_competition.csv` holds four single values: UDP 32 → 20 µM with ANT-3744 present, ANT-3744 0.4 → 0.2 µM with UDP present. That text reached all eight runs as raw tool output. Three then wrote claims inconsistent with it. O3: "It binds together with UDP **and cooperatively: each ligand raises the other's affinity 1.6–2×**, and the DSF shifts add (2 + 6 = 8 °C)", and builds on it — "That fits an allosteric, product-complex-stabilising mechanism" (L75). O2: "UDP *tightens* ANT-3744 binding (KD 0.4 → 0.2 µM)" (L102), and separately describes the two surfaces as equivalent — "ANT-3744 reaches ~1.4× the theoretical 1:1 maximum on the 9,000 RU surface, while UDP reaches ~0.12× **on an equivalent surface**" (L260) — which the records contradict. F2: "UDP and ANT-3744 each bind **slightly tighter** in the other's presence" (L120), and reports that the record is absent — "**Immobilisation levels per run are not recorded**, so I raise it as a query, not a finding" (L170) — when §6.4 states all three |
| **Counterfactual** | Establish non-competitive binding from the additive thermal shifts and the ternary structure, not from the competition constants. Recomputed from the room: `dsf_thermal_shift.csv` gives ΔTm +2 °C (UDP), +6 °C (ANT-3744), +8 °C (both) — exactly additive — and `MGAT1_C3744_UDP.cif` has both ligands bound. The competition constants are consistent with non-competition and add nothing beyond it: were ANT-3744 competitive with UDP, 5 mM UDP would drive its apparent dissociation constant to about 63–65 µM against 0.2 µM observed, and 20 µM ANT-3744 would drive UDP's to about 1,632 µM against 20 µM observed. A two-fold difference in single values across separately prepared surfaces at 9000, 3600 and 3500 RU is within run-to-run variation, so it cannot carry a thermodynamic result. Golden §2: "Non-competitive binding is established by the **additive thermal shifts** ... **Do not read the competition shifts as cooperativity**" |
| **Exemplar** | F4, which reaches the same place and records the downgrade: "'Cooperative with UDP' is not established. The shifts are ≤2-fold, reported as single values, on different sensor surfaces. 'Does not compete with UDP' is established" (L152), logged in its own set-aside table as "'Cooperativity' between ANT-3744 and UDP | Downgraded to 'no competition'" (L186). F1 and F3 also use the constants for non-competition only |
| **Evidence** | O3 memo L75 [transcript]; O2 memo L102 and L260 [transcript]; F2 memo L170 [transcript]. Records §6.4 delivered as raw `ToolResult` at elements 22 (O2), 22 and 28 (O3), 31 (F2) [transcript]. All three reasoned about the differing surfaces for the stoichiometry question at elements 48 and 213 (O2), 246 (O3), 48 and 321 (F2) [summarised thinking, corroborating only]. DSF additivity and both competition expectations recomputed [computed] |
| **Graded?** | n/a |

**Plain language.** The client measured how tightly the drug binds, once alone and once with the enzyme's natural partner present. The second number was about twice as tight. The methods state plainly that each measurement used a freshly made sensor chip carrying a different amount of protein, so a two-fold difference is chip-to-chip noise. All eight runs were handed that sentence. Three read it, used it for a different question, and then wrote that the two molecules help each other bind, that the chips were equivalent, or that the chip loadings were never recorded.

---

## 3. `arm-labels-unsourced` — Referential

| Field | Content |
|---|---|
| **Runs** | O3, F1, F3 |
| **Not checked** | Whether the arm identities attached to the screen results exist in any client file, before citing those files as the source of arm-specific numbers |
| **Description** | `experimental_records.pdf` §2 names the arms the experiment comprised and §2.1 tabulates Groups 1–8 by background and sample count; nothing joins the two, and the stated cohorts of 30 C57BL/6 and 15 nude mice do not reconcile with the 141 tumour libraries in `crispr_invivo_guide_counts.csv.gz`. §2.1 reached all eight runs as raw tool output. All three runs recorded the gap and inferred the arms from control-gene behaviour, then reported screen results under bare arm names and attributed those numbers, in the client-facing provenance, to the count matrix alone. O3: "Mgat1 ranks #1 of 795 genes for STK11-over-NTC depletion in **B6-isotype** tumours (Δ −2.73 log2, FDR 0.004) and in **B6-anti-PD-1** tumours (Δ −3.11, FDR 2×10⁻⁷)" (L42), "smaller and not significant in **nude hosts** (Δ −1.05, FDR 0.14), so it is largely immune-dependent" (L45); its ledger rows E11–E14 cite `crispr_invivo_guide_counts.csv.gz`, "computed from raw data", with the inference flag only on the design row E10 (L191–L195); its analysis outputs are arm-keyed filenames — `contrast_STK_aPD1_vs_NTC_aPD1.csv`, `contrast_NTC_IgG_vs_NTC_nude.csv` — with the group numbers dropped. F1: "about half to two-thirds of the Mgat1 depletion is already present in **nude mice, which lack T cells**" (L45); ledger rows B5–B10 and B13 name "immunocompetent isotype arm", "anti-PD-1 arms", "nude mice", `client_source` "same" chaining to the count matrix, `derivation` "computed", with the flag only on B3. F3: "In **C57BL/6** tumours Mgat1 is the single most Stk11-selective dependency of 795 genes" (L47); provenance rows "Stk11-KO −1.66 (**nude**)" (L122), "**C57BL/6 vs nude** FDR 0.004; **PD-1 vs isotype** P = 0.96" (L124), source "same" chaining to the count matrix. Arm names drawn from the growth panels on `phenotype_figures.pdf` p1 and p8 are not instances: those panels label their arms explicitly |
| **Counterfactual** | Report the screen on the background label every count column already carries, `NTC` or `STK11`, and take the genotype comparison from that, as golden §"Expected treatment of the unmapped screen arms" states: "**A correct answer aggregates on the background label** ... No conclusion in this assessment requires the arm identities." Where arms are inferred, carry the hedge on the number and in the provenance column rather than declaring it once elsewhere: "**Inferring the arms is acceptable where it is flagged as inference** ... **What is not correct** is presenting an inferred mapping as though the files supplied it". Each conclusion the arms would bear on has a labelled route elsewhere in the room — checkpoint-refractoriness from the p8 growth panel, T-cell dependence from the adoptive-transfer and co-culture panels, catalytic dependence from the construct-labelled rescue panels |
| **Exemplar** | O2, where the hedge travels with the number: the ledger row is titled "Mgat1 gene score by background x **inferred arm**" and every value is labelled "nude-like", "IgG-like", "aPD-1-like" (E10), with a separate row E14 "Arm inference from internal controls (client did not supply arm key)". O1 writes "immunocompetent-like" throughout and carries E28 "In vivo screen: arm inference ... (presumptive nude arms)". O4 keeps the inference in an appendix, states its figure conditionally — "**Under that mapping**, about 70% of the sgStk11-background effect ... would be T-cell-independent" (L100) — and tells the client "The screen's group→condition map (nude / IgG / anti-PD-1) is not documented, **so T-cell and anti-PD-1 dependence cannot be tested directly**" (L157) |
| **Evidence** | O3 memo L42, L45, L92 and ledger L191–L195 [transcript]; F1 memo L45 and ledger rows B5–B10, B13 [transcript]; F3 memo L47 and provenance L122, L124, L125 [transcript]. Records §2.1 delivered as raw `ToolResult` at elements 22–31 across the panel [transcript]. Each run recorded the missing key before inferring: F1 element 105, O3 elements 153 and 399, F3 elements 102 and 369 [summarised thinking, corroborating only] |
| **Graded?** | n/a |

**Plain language.** The client's screen has eight groups of tumours. The records say the experiment had nude mice, an antibody-control arm and a treated arm, and separately list the eight groups — but nothing says which group is which. Three runs worked out a likely mapping from the data, which is fine, and then wrote their results as "in the nude mice" and "in the anti-PD-1 arm", and told the client those numbers came from the count file. The count file holds no arm identities. The prompt specifically warns that the client will be asked where each number came from; on these numbers the answer given points at a file that cannot supply them.

**Framing constraint for the write-up.** All three runs identified the gap before inferring anything, and F1 revised its first mapping after finding it contradicted by the Cd274 data. This is an attribution and reporting failure, not a failure to recognise, and must not be written as the latter.

---

## 4. `lectin-ms-commensurable` — Synthesis

| Field | Content |
|---|---|
| **Runs** | O2, O3 |
| **Not measured** | Whether the two readouts are commensurable at all, before treating their disagreement as evidence that one is defective |
| **Description** | Both runs set the knockout glycoproteomics aside as a pharmacodynamic reference because its magnitude disagrees with the lectin flow result, and attribute the disagreement to a defect in the mass spectrometry. O2: "The glycoproteomics shows only about a 40–45% fall in complex-type glycopeptide signal in MGAT1 knockout cells. **This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference**" (L137), with "Possible causes are ratio compression, an incomplete knockout population, or composition assignment" (L261). O3: "The HexNAc≥3 share of reporter signal falls only from ≈9–10% to ≈5% ... **This conflicts with the ≈96% PHA-L loss and fits TMT ratio compression or misassignment**" (L137) |
| **Counterfactual** | Treat the two readouts as measuring different things and do not read their disagreement as a defect. Lectin signal is avidity-driven, non-linear in glycan density and restricted to the cell surface; the mass spectrometry is molar glycopeptide abundance across all compartments, untrafficked protein included. Their magnitudes have no reason to agree. What rules the dataset out as a product-side reference is the size of the complex-sialylated denominator, not the disagreement — see Mode 6. Golden §4: "**The lectin and mass-spectrometry readouts are not commensurable** ... the disagreement is not evidence that either is wrong" |
| **Exemplar** | O1 and F3 reach the same place on a basis that holds. O1 discounts the glyco magnitudes for normalisation-dependence and implausible compositions: "TMT ratio compression. KO channels carry 1.55–1.64× more total signal, so fold changes depend on normalisation; I used within-channel composition shares instead" (L287). F3: "No total-proteome normalisation (knockout channels carry 1.5–1.7× more signal); reporter-ion ratio compression; 72 % of assignments rest on one spectrum; some identifications are implausible (nuclear proteins)" (L90). Neither invokes the lectin disagreement |
| **Consequence** | Benign for the verdict. Both runs reach the correct conclusion — the dataset cannot serve as the product-side reference — and both propose a replacement readout, which is what the decision needs |
| **Evidence** | O2 memo L137 and L261 [transcript]; O3 memo L137 [transcript]. Knockout-to-control total intensity recomputed at 1.5231e10 against 9.3026e9, a factor of 1.64 for A375 and 1.55 for NCI-H1703 [computed] |
| **Graded?** | n/a |

**Defensibility — both sides, writer decides.** For: the inferential structure is wrong, disagreement between non-commensurable readouts is used as the evidence, and O2 compounds it by also describing the SPR surfaces as equivalent. Against: TMT reporter-ion compression is a real phenomenon that genuinely attenuates fold changes, an expert can defend invoking it, O3 hedges with "or misassignment", and both runs land on the right conclusion. Two runs, both Opus, so it clears the floor but not the one-of-each pattern.

**Plain language.** Two ways of measuring the same biology: one stains the cell surface and shows a 96% drop, the other weighs molecules from the whole crushed-up cell and shows a 40% drop. Both runs concluded the second must be faulty because it disagrees with the first. But one sees only the surface and the other sees everything inside too, and they respond differently to how densely packed the sugars are. There is no reason for them to match.

---

## 5. `no-safety-position` — Reasoning

| Field | Content |
|---|---|
| **Runs** | O1, O2, O3, O4, F1, F2, F3, F4 |
| **Not measured** | Any on-target safety risk inferable from MGAT1 biology, as against the absence of toxicology data |
| **Description** | Every run records safety as an absence and schedules it as future work, and none names a specific on-target risk. O1's scorecard: "Tolerability of systemic MGAT1 inhibition | None | **Absent**" (L47). O4's: "Systemic inhibition is tolerated and spares T-cell function | **Untested**" (L38). F2's: "Selectivity, exposure, tolerability | **No data** beyond solubility and hepatocyte clearance" (L53). F3: "There are no data on T-cell function or tolerability under MGAT1 loss or inhibition" (L37). Across all eight deliverables there is no mention of cardiac risk beyond one glancing hit in F2, none of autoimmunity, and none of germline loss. Several runs do identify the right *shape* of the problem — O3 "A systemic drug will also reach host cells, including the T cells it is meant to help" (L97), F1 "A drug would start on established tumours and reach T cells as well as tumour cells" (L39) — without naming what the risk is |
| **Counterfactual** | Take a position from target biology rather than reporting the absence. Golden §5, which labels itself "*Named domain knowledge, not from the package*": germline MGAT1 loss is embryonic lethal in mice while MGAT1-null cells are viable, so cell-autonomous essentiality is not the issue; adult cardiomyocyte-specific deletion produces dilated cardiomyopathy through ion-channel glycosylation; reduced N-glycan branching drives T-cell hyperactivity and autoimmunity, which is mechanistically the same biology as the intended effect and therefore cannot be engineered away; complex N-glycans are required to form bronchial epithelium, directly relevant to a lung indication. Position: a characterisable risk rather than a blocker, with cardiac safety pharmacology first. Golden: "An answer that reports only that no toxicology data exist has not taken a position" |
| **Exemplar** | **None.** No run on this panel takes a safety position. Reported rather than promoting a partial match |
| **Consequence** | Omits a decision input the committee needs: an autoimmune liability that cannot be separated from the intended pharmacology bears directly on whether the programme is fundable at all |
| **Evidence** | O1 L47, O4 L38, F2 L53, F3 L37 [transcript]. Absence confirmed across all eight deliverables on nine probe spellings covering safety, tox, tolerability, cardiac, heart, QT, ion-channel, autoimmune, immune-related, irAE, on-target risk, germline, embryonic, multiple sclerosis and therapeutic index [transcript] |
| **Graded?** | n/a |

**Requirement basis — contested, writer decides.** The requirement is in the golden, not in the prompt. Against shipping: the prompt says the client's files are "the only data they trust" and "All recommendations and claims must be supported by their data", and the golden flags its own safety section as outside the package, so a careful expert can defend declining to import a safety literature the client has not seen. For shipping: the prompt asks for the case "as strongly as the data allows" and for what would bring the asset back, and all eight runs imported outside knowledge elsewhere — MC38's tissue of origin, core-essential gene identity, aggregation motifs — so a blanket no-outside-knowledge defence does not hold. This is the most prevalent mode available and the most likely to be pinged on basis.

**Plain language.** Every run noted there is no toxicology in the package and scheduled it as future work. None named a specific risk. There are known ones: blocking this enzyme in the heart causes heart failure in mice, and the same change to immune cells drives autoimmune disease — awkward, because revving up immune cells is the whole point of the drug. Several runs saw that a systemic drug will reach the patient's own T cells, and stopped there.

---

## 6. `unmeasured-product-side` — Synthesis

| Field | Content |
|---|---|
| **Runs** | O1, O2, O3, O4, F1, F2, F3, F4 |
| **Not measured** | How many complex or sialylated sites the dataset actually quantified, before quoting a product-side magnitude |
| **Description** | All eight quote a fall in complex or sialylated signal in the knockout as a magnitude, and none states the denominator those percentages rest on. O3: "The HexNAc≥3 share of reporter signal falls only from ≈9–10% to ≈5% (a ≈44% relative drop)" (L137). O2: "only about a 40–45% fall in complex-type glycopeptide signal" (L137). O4: the MGAT1-dependent share falling 16.5% to 9.6% in A375 and 19.1% to 9.4% in NCI-H1703. F3: "sialylated complex down on 42 % / 50 %" against a stated "910 sites on 524 proteins quantified" (L37), which is the all-sites denominator, not the complex-sites one. F1 comes closest with a real denominator — "complex share fell at 125 of 164 sites in each line (sign test p = 1e-11); median site keeps 66% (A375) / 74% (H1703)" (L158) — and still does not say how many of those carry a single unambiguous complex-sialylated composition |
| **Counterfactual** | Establish the denominator before drawing the product-side conclusion, and make the small denominator the reason for ruling the dataset out as a product-side reference. Recomputed from `glycoproteomics_site_quant.xlsx`, sheet `Site_quant`: 910 rows, of which row P23193 has all eight A375 channels at exactly zero, leaving 909 analysable; of these, 422 carry exactly one composition; among those, high-mannose sites outnumber complex-sialylated sites by better than ten to one. **The exact split is classification-scheme dependent and should not be quoted as settled** — the golden gives 317 against 16, my own classifier gives 306 against 26, and the grader's neutral list allows "any defensible glycan classification scheme". The conclusion is robust to the scheme; the figures are not. Golden §4: "What rules the dataset out as a product-side reference is that [a small number of] complex sites were quantified, not that it disagrees with flow cytometry" |
| **Exemplar** | **None clean.** F1 is the closest, giving a 164-site denominator for its site-level statistic, and is a partial match rather than an exemplar. Reported as such |
| **Consequence** | Benign for the verdict. An unsupported magnitude reaches the client, and the correct reason for setting the dataset aside goes unstated, which matters because the replacement readout is the programme's first gate |
| **Evidence** | O3 L137, O2 L137, F3 L37, F1 L158 [transcript]; O4's glycoproteomics section [transcript]. Absence of a complex-site denominator confirmed across all eight on five probe spellings covering counted sites, "how many", few/handful/scarce, under-represented and limited coverage [transcript]. 909 analysable sites, P23193, 422 single-composition sites and the class split recomputed [computed] |
| **Graded?** | n/a |

**Requirement basis — generic, writer decides.** The prompt requires each number's basis — "I will be asked where each number came from" — but does not ask for a denominator in terms, so the requirement is closer to an expert norm than to a stated line. Weaker on basis than Mode 3, which breaches the same prompt sentence directly by naming a file that cannot supply the number.

**Plain language.** All eight runs reported how much the relevant sugar structures dropped in the knockout cells. None said how many of those structures were actually measured. The answer is: very few — a few dozen out of hundreds — which is exactly why that dataset cannot be the programme's yardstick. The percentage looks solid until you ask what it is a percentage of.

---

## Held

| Candidate | Why held |
|---|---|
| `selectivity-unrobust` | **Did not fire.** All eight corrected for differential guide representation, and five tested alternative corrections: O1 "57–72% across analysis variants", F1 two or three methods per in vivo contrast (ledger B7 "by log-mean method; +0.88 (z +1.0) by edgeR", B9 giving 64% / 48% / 69% by three methods), F2 nine variants (ledger D13), F4 L101, O3 "robustness checks" (L167). This panel is materially stronger on this axis than the three pre-pilot validation attempts |
| `channel-normalised` | **Did not fire.** No run normalised the quantitative channels to equal total or median. O1 L287 and F3 L90 explicitly decline, both naming the 1.5–1.7× channel difference |
| `fitted-potency` | **Did not fire.** All eight excluded ANT-1938 and ANT-2214 as unvalidated chemical matter on correct grounds; O3 and F4 additionally flag the 74 µM figure as extrapolated from 60% inhibition |
| Partial inhibition left uninterpreted | All eight identify the ≈8–10% residual-activity floor across the potent analogues, and several note ANT-2118 reaching near zero as evidence the floor is real. The handling is defensible across the panel; no mode |
| Deliverable layout unverifiable | Tooling, not a mode. The image carries no PDF rasteriser, which affected every run; at least two disclosed that their deliverable layout could not be visually checked. Recorded as a task note, per `qa_triage.md` |

## Per-trajectory profile

| Run | Modes carried | Unique | Poor exemplar? |
|---|---|---|---|
| O1 | 1, 5, 6 | — | No. Best citation for Mode 1's design form |
| O2 | 1, 2, 4, 5, 6 | — | No. Carries the most modes, and is the Mode 3 exemplar |
| O3 | 1, 2, 3, 4, 5, 6 | — | No. Carries every mode; the clearest instance of Modes 2 and 3 |
| O4 | 5, 6 | — | No. Exemplar for Modes 1 and 3 |
| F1 | 3, 5, 6 | — | No. Mode 3's ledger form is clearest here |
| F2 | 2, 5, 6 | — | Partly. Its Mode 2 instance is the factual-misreport variant rather than the shared inferential one; cite O3 or O2 for the shared form |
| F3 | 3, 5, 6 | — | No |
| F4 | 5, 6 | — | Yes for Modes 1–4: F4 handles all four correctly and is the Mode 2 exemplar. Cite it as the correct comparison, not as an instance |

No run's profile is driven by truncation or tooling friction. All eight completed, none refused, and the one tooling gap had a workaround every run found.

## Submission shortlist

Three modes clear every bar with an uncontested basis: **1, 2 and 3.** Mode 3 is the only one of those spanning both models, which is the pattern the client asks for most. Modes 5 and 6 are the most prevalent and the weakest on requirement basis; Mode 4 is sound but contested on defensibility and is Opus-only. The writer picks.
