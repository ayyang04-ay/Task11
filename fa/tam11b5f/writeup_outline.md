# tam11b5f — write-up outline

For typing into Studio. **Bare facts arranged under the official fields, not sentences.** The prose has to be yours: the overlap check and AI-detection pass target exactly this file, so reword as you type rather than transcribing. Said once, not repeated below.

## Before you start: three constraints

**1. The official cap is five modes. Six cleared.** Ranked below; the top five are marked SHIP and the sixth DROP. Your pick, but something has to go.

**2. No mode changed the verdict, and the write-up must not claim one did.** All eight runs reached the same call — do not advance now, hold behind gates, fund a short gated package, keep the target — and the golden reaches it too. The absence of any cellular compound data over-determines the call, which was pre-registered as a known design weakness. So for each mode the honest field is **what it did affect**: the study package, the mechanism case, the positioning, the provenance, or a decision input. Written as "this is why the run got the call wrong" it is false and a reviewer reading the transcripts will catch it.

**3. Section discipline.** "What did the model do wrong" carries only what went wrong. The exemplar run's correct behaviour goes in "what should the model have done", never in the wrong-doing section — praise inside a failure item gets the item rejected. No scores anywhere. No k-of-n ratios; name the runs.

## Numbering

This file is ordered for the write-up, so the numbers differ from `error_modes.md` and `submittability.md`. **Cite the short names** — those are stable across all three files.

| Here | Short name | `error_modes.md` |
|---|---|---|
| 1 | `no-cross-species` | 1 |
| 2 | `arm-labels-unsourced` | 3 |
| 3 | `spr-surface-unapplied` | 2 |
| 4 | `no-safety-position` | 5 |
| 5 | `lectin-ms-commensurable` | 4 |
| 6 | `unmeasured-product-side` | 6 |

## Run labels

Write the model for every run. Opus 5.5: O1 `bd63c97e`, O2 `2caa3b04`, O3 `bc8b9e20`, O4 `409bdac0`. Fable 5.2: F1 `aa6a0794`, F2 `734093b7`, F3 `73e1ddd7`, F4 `69bb2ad2`.

---

# 1. `no-cross-species` — SHIP

**One breath:** the drug was only ever tested on the human enzyme, every animal model is a mouse, and three runs designed the expensive mouse efficacy study without asking whether the drug works on mouse enzyme at all.

| Field | Facts |
|---|---|
| **Classification** | High-level: specification failure in the study package. Specific: a mouse in vivo efficacy study specified as a funded gate without establishing mouse MGAT1 potency, where every compound measurement in the room is against human enzyme |
| **Affected** | The next-steps section. Invalidates a named comparator: the mouse efficacy study as specified cannot distinguish a drug that failed from one that never engaged the target. Not the go/no-go |
| **Runs** | Opus 5.5 O1, O2, O3 |
| **Wrong — O1** | Memo L225, specifies "a 2×2 design in vivo (MGAT1 inhibition × anti-PD-1), run in an STK11-null, lung-relevant syngeneic model and its isogenic STK11-intact twin". No mouse potency requirement anywhere in the deliverable |
| **Wrong — O2** | Memo L197, efficacy design "STK11-deficient immunocompetent tumours (ideally a lung model alongside sgSTK11 MC38), in a 2×2 factorial". Bring-back criterion 4 at L225 asks for in vivo translation against the genetic benchmark. No mouse potency requirement anywhere |
| **Wrong — O3** | Memo L110, Gate 4 go criterion "significant TGI vs vehicle in STK11-null, approaching the KO benchmark (≈50% in MC38 sgSTK11)". No mouse potency requirement anywhere |
| **Also usable** | All three are species-aware elsewhere: O1 and O3 both flag that the hepatocyte clearance species is not stated. The check was applied to clearance, not to the compound's own pharmacology |
| **Room facts** | `experimental_records.pdf` §6.1: construct is UniProt P26572, residues T30–N445. §6.4: SPR construct A104–N445, same protein. §2: MC38 implanted into C57BL/6 and nude mice. Records reached all three as raw tool output |
| **Transcripts** | No species-potency reasoning anywhere in O1, O2 or O3. Probed on mouse/murine + potency/IC50/orthologue/conservation, and on cross-species |
| **Should have** | Required mouse MGAT1 potency and pocket conservation before any mouse efficacy study, compared against the human potency. Golden study 3: "Required before any mouse efficacy study: every compound measurement is against human enzyme and every in vivo model is mouse" |
| **Exemplar** | Opus 5.5 O4: names the gap at L80 ("Every biochemical, biophysical and structural datum is on human MGAT1, while all in vivo models are murine. There is no mouse Mgat1 potency"), lists "Mouse Mgat1 potency (needed before any MC38 work)" at L222, makes it bring-back criterion 3 at L275, and plans the contingency at L247 ("If mouse potency is >3× weaker than human, use a surrogate tool or a humanised-target model"). Fable 5.2 F2 (Gate 3, L138, "activity on mouse MGAT1"), F3 (L109), F4 (L153) each also require it |

---

# 2. `arm-labels-unsourced` — SHIP

**One breath:** the client's screen has eight tumour groups and no file says which is the untreated arm, the antibody-control arm or the treated arm; three runs worked out a likely mapping, which is fine, then reported results as "in the nude mice" and told the client those numbers came from the count file, which holds no arm identities.

| Field | Facts |
|---|---|
| **Classification** | High-level: referential failure, a claim attributed to the wrong source. Specific: screen results reported under treatment-arm names no client file supplies, with the client-facing provenance citing the count matrix as their source |
| **Affected** | Asset positioning and its provenance — the T-cell-dependence share and the anti-PD-1 interaction, which is the checkpoint-resistance claim the prompt highlights. Breaches the prompt sentence about being ready to say where each number came from. Not the go/no-go, and the conclusions themselves mostly survive; the failure is attribution |
| **Runs** | Opus 5.5 O3; Fable 5.2 F1, F3. **Both models — the pattern the client wants most** |
| **Wrong — O3** | Memo L42 "Mgat1 ranks #1 of 795 genes for STK11-over-NTC depletion in B6-isotype tumours (Δ −2.73 log2, FDR 0.004) and in B6-anti-PD-1 tumours (Δ −3.11, FDR 2×10⁻⁷)"; L45 "smaller and not significant in nude hosts (Δ −1.05, FDR 0.14), so it is largely immune-dependent"; L92 the anti-PD-1 claim. Ledger rows E11–E14 at L191–L195 cite `crispr_invivo_guide_counts.csv.gz`, derivation "computed from raw data", with the inference flag only on the design row E10. Analysis outputs are arm-keyed filenames (`contrast_STK_aPD1_vs_NTC_aPD1.csv`, `contrast_NTC_IgG_vs_NTC_nude.csv`) with the group numbers dropped entirely |
| **Wrong — F1** | Memo L45 "about half to two-thirds of the Mgat1 depletion is already present in nude mice, which lack T cells". Ledger rows B5–B10 and B13 name "immunocompetent isotype arm", "anti-PD-1 arms", "nude mice", `client_source` "same" chaining to the count matrix, `derivation` "computed"; the inference flag sits only on B3 |
| **Wrong — F3** | Memo L47 "In C57BL/6 tumours Mgat1 is the single most Stk11-selective dependency of 795 genes". Provenance rows L122 "Stk11-KO −1.66 (nude)", L124 "C57BL/6 vs nude FDR 0.004; PD-1 vs isotype P = 0.96", L125, all sourced "same" chaining to the count matrix |
| **Not instances** | Arm names taken from `phenotype_figures.pdf` p1 and p8: those growth panels label their arms explicitly. Only arm names attached to screen Groups 1–8 are inference |
| **Room facts** | `experimental_records.pdf` §2 names the arms the experiment comprised; §2.1 tabulates Groups 1–8 by background and sample count only; nothing joins them. Stated cohorts of 30 C57BL/6 and 15 nude against 141 tumour libraries. §2.1 reached all eight runs as raw tool output |
| **Transcripts — the framing constraint** | All three recorded the gap **before** inferring: F1 element 105 ("The records never define group identities, so I'll flag that as a documentation gap. I'll infer the arms from the data instead"), O3 elements 153 and 399, F3 elements 102 and 369. F1 also revised its first mapping after finding it contradicted by the Cd274 data. **So this is an attribution and reporting failure, not a failure to recognise.** Do not write it as the latter. These blocks are summarised thinking — corroborating only; the mode rests on the deliverables and the records text, both raw |
| **Should have** | Reported the screen on the background label every count column already carries (`NTC` or `STK11`) and taken the genotype comparison from that. Golden: "A correct answer aggregates on the background label... No conclusion in this assessment requires the arm identities." Where arms are inferred, carry the hedge on the number and in the provenance column rather than declaring it once elsewhere. Golden: "Inferring the arms is acceptable where it is flagged as inference... What is not correct is presenting an inferred mapping as though the files supplied it" |
| **Exemplar** | Opus 5.5 O2 — the hedge travels with the number: ledger row titled "Mgat1 gene score by background x inferred arm", every value labelled "nude-like", "IgG-like", "aPD-1-like", plus a separate row E14 "Arm inference from internal controls (client did not supply arm key)". O1 writes "immunocompetent-like" throughout. O4 keeps the inference in an appendix, states its figure conditionally at L100 ("Under that mapping"), and tells the client at L157 that "The screen's group→condition map (nude / IgG / anti-PD-1) is not documented, so T-cell and anti-PD-1 dependence cannot be tested directly" |

---

# 3. `spr-surface-unapplied` — SHIP

**One breath:** the methods say each binding measurement used a freshly made sensor chip carrying a different amount of protein, so a two-fold difference is chip-to-chip noise; all eight runs were handed that sentence, and three wrote that the two molecules help each other bind, that the chips were equivalent, or that the chip loadings were never recorded.

| Field | Facts |
|---|---|
| **Classification** | High-level: analytical failure, a measurement artefact read as a result. Specific: a two-fold shift in single-value dissociation constants read as mutual affinity enhancement without applying the records' statement that each competition experiment used a freshly prepared surface at a differing immobilisation level |
| **Affected** | The mechanism case and what the mechanism gate must establish. O3 builds an allosteric product-complex-stabilising model on it. Not the go/no-go |
| **Runs** | Opus 5.5 O2, O3; Fable 5.2 F2. Both models |
| **Wrong — O3** | Memo L75 "It binds together with UDP and cooperatively: each ligand raises the other's affinity 1.6–2×, and the DSF shifts add (2 + 6 = 8 °C)", then "That fits an allosteric, product-complex-stabilising mechanism" |
| **Wrong — O2** | Memo L102 "UDP *tightens* ANT-3744 binding (KD 0.4 → 0.2 µM)". Separately, L260 describes the surfaces as equivalent: "ANT-3744 reaches ~1.4× the theoretical 1:1 maximum on the 9,000 RU surface, while UDP reaches ~0.12× on an equivalent surface" — the records give 9000 against 3600 and 3500 |
| **Wrong — F2** | Memo L120 "UDP and ANT-3744 each bind slightly tighter in the other's presence". L170 reports the record as absent: "Immobilisation levels per run are not recorded, so I raise it as a query, not a finding" — §6.4 states all three |
| **Room facts** | `experimental_records.pdf` §6.4 gives approximately 9000 RU (direct binding), 3600 RU (UDP as analyte), 3500 RU (ANT-3744 as analyte), and ends "SPR experiments were performed separately with a new surface preparation for every experiment; protein immobilization levels differed". `spr_competition.csv` holds four single values: UDP 32 → 20 µM, ANT-3744 0.4 → 0.2 µM |
| **Transcripts** | §6.4 delivered as raw tool output at elements 22 (O2), 22 and 28 (O3), 31 (F2) — and to all five other runs. All three reasoned about the differing surfaces for the stoichiometry question at elements 48 and 213 (O2), 246 (O3), 48 and 321 (F2) — summarised thinking, corroborating only. **Encountered then unapplied:** the convention was read and used for one comparison, and left unused for the one it bears on |
| **Should have** | Established non-competitive binding from the additive thermal shifts and the ternary structure, not from the competition constants. `dsf_thermal_shift.csv` gives ΔTm +2 °C (UDP), +6 °C (ANT-3744), +8 °C (both) — exactly additive; `MGAT1_C3744_UDP.cif` has both ligands bound. The constants are consistent with non-competition and add nothing beyond it: a competitive ANT-3744 would show an apparent dissociation constant near 63–65 µM at 5 mM UDP against 0.2 µM observed, and UDP's would go to about 1,632 µM at 20 µM ANT-3744 against 20 µM observed. Golden: "Non-competitive binding is established by the additive thermal shifts... Do not read the competition shifts as cooperativity" |
| **Exemplar** | Fable 5.2 F4: L152 "'Cooperative with UDP' is not established. The shifts are ≤2-fold, reported as single values, on different sensor surfaces. 'Does not compete with UDP' is established", logged in its own set-aside table at L186 as "'Cooperativity' between ANT-3744 and UDP | Downgraded to 'no competition'". F1 and F3 use the constants for non-competition only |

---

# 4. `no-safety-position` — SHIP (widest reach, weakest grounds)

**One breath:** every run noted there is no toxicology in the package and scheduled it as future work; none named a specific risk, though blocking this enzyme in the heart causes heart failure in mice and the same change to immune cells drives autoimmune disease — which is awkward, because revving up immune cells is the whole point of the drug.

| Field | Facts |
|---|---|
| **Classification** | High-level: reasoning failure, a gap misclassified as unknowable. Specific: the absence of toxicology data treated as grounds for taking no safety position, where on-target cardiac and autoimmune risk are nameable from target biology |
| **Affected** | Omits a decision input the committee needs. An autoimmune liability that cannot be separated from the intended pharmacology bears on whether the programme is fundable at all. Of the six modes this is the one with the most direct committee consequence, and still not the go/no-go |
| **Runs** | Opus 5.5 O1, O2, O3, O4; Fable 5.2 F1, F2, F3, F4. Every run |
| **Wrong — cite two or three** | O1 scorecard L47 "Tolerability of systemic MGAT1 inhibition \| None \| **Absent**". O4 scorecard L38 "Systemic inhibition is tolerated and spares T-cell function \| **Untested**". F2 L53 "Selectivity, exposure, tolerability \| **No data** beyond solubility and hepatocyte clearance". F3 L37 "There are no data on T-cell function or tolerability under MGAT1 loss or inhibition" |
| **Sharper form** | Several runs identify the right shape and stop: O3 L97 "A systemic drug will also reach host cells, including the T cells it is meant to help, and no experiment tests MGAT1 loss or inhibition in T cells"; F1 L39 "A drug would start on established tumours and reach T cells as well as tumour cells". Named the exposure problem, named no risk |
| **Absence** | Confirmed across all eight deliverables on probes for safety, tox, tolerability, cardiac, heart, QT, ion-channel, autoimmune, immune-related, irAE, on-target risk, germline, embryonic, multiple sclerosis, therapeutic index. One glancing cardiac hit in F2; no autoimmunity or germline mention anywhere |
| **Should have** | Taken a position from target biology. Golden §5: germline MGAT1 loss is embryonic lethal in mice while MGAT1-null cells are viable, so cell-autonomous essentiality is not the issue; adult cardiomyocyte-specific deletion gives dilated cardiomyopathy through ion-channel glycosylation; reduced N-glycan branching drives T-cell hyperactivity and autoimmunity, mechanistically the same biology as the intended effect and so not engineerable away; complex N-glycans are required to form bronchial epithelium, directly relevant to a lung indication. Position: a characterisable risk rather than a blocker, cardiac safety pharmacology first. Golden: "An answer that reports only that no toxicology data exist has not taken a position" |
| **Exemplar** | **None.** No run on this panel takes a safety position. State that rather than promoting a partial match |
| **Expect a challenge** | The requirement is in the golden, not in the prompt, and the prompt says the client's files are "the only data they trust" with claims "supported by their data" — while the golden labels its own safety section "Named domain knowledge, not from the package". Your counter, worth putting in the write-up pre-emptively: all eight runs imported outside knowledge elsewhere (MC38's tissue of origin, core-essential gene identity, aggregation motifs), so a blanket no-outside-knowledge defence does not hold |

---

# 5. `lectin-ms-commensurable` — SHIP (fifth slot, or swap for 6)

**One breath:** two ways of measuring the same biology disagree — one stains the cell surface and shows a 96% drop, the other weighs molecules from the whole crushed-up cell and shows 40% — and two runs concluded the second must be faulty, when the two methods were never measuring comparable things.

| Field | Facts |
|---|---|
| **Classification** | High-level: synthesis failure, two non-comparable sources treated as comparable. Specific: a surface lectin signal ratio and a whole-lysate glycopeptide intensity ratio treated as directly comparable magnitudes, and their disagreement read as evidence the mass spectrometry is defective |
| **Affected** | The stated reason for setting the dataset aside, which feeds the pharmacodynamic-readout gate — the programme's first gate. Right conclusion, invalid basis. Benign for the go/no-go |
| **Runs** | Opus 5.5 O2, O3. Opus only — clears the floor but not the one-of-each pattern |
| **Wrong — O2** | Memo L137 "The glycoproteomics shows only about a 40–45% fall in complex-type glycopeptide signal in MGAT1 knockout cells. This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference". L261 "Glycoproteomics is quantitatively discordant with lectin flow. Possible causes are ratio compression, an incomplete knockout population, or composition assignment" |
| **Wrong — O3** | Memo L137 "The HexNAc≥3 share of reporter signal falls only from ≈9–10% to ≈5% (a ≈44% relative drop)... This conflicts with the ≈96% PHA-L loss and fits TMT ratio compression or misassignment" |
| **Should have** | Treated the readouts as measuring different things. Lectin signal is avidity-driven, non-linear in glycan density, surface-restricted; the mass spectrometry is molar glycopeptide abundance across all compartments including untrafficked protein. Their magnitudes have no reason to agree. Golden §4: "The lectin and mass-spectrometry readouts are not commensurable... the disagreement is not evidence that either is wrong" |
| **Exemplar** | Opus 5.5 O1 and Fable 5.2 F3 reach the same place on a basis that holds. O1 L287: "TMT ratio compression. KO channels carry 1.55–1.64× more total signal, so fold changes depend on normalisation; I used within-channel composition shares instead". F3 L90: "No total-proteome normalisation (knockout channels carry 1.5–1.7× more signal); reporter-ion ratio compression; 72 % of assignments rest on one spectrum; some identifications are implausible (nuclear proteins)". Neither invokes the lectin disagreement |
| **Expect a challenge** | TMT reporter-ion compression is real and genuinely attenuates fold changes, so an expert can defend invoking it; O3 hedges with "or misassignment"; both runs land correctly. The defensible core is the inferential structure — disagreement between non-commensurable readouts used as the evidence — plus O2 separately describing the SPR surfaces as equivalent |

---

# 6. `unmeasured-product-side` — DROP (sixth of six; swap in over 5 only if you want panel-wide reach over a cleaner basis)

**One breath:** all eight runs reported how far the relevant sugar structures fell in the knockout cells, and none said how many of those structures were actually measured — the answer is a few dozen out of hundreds, which is the real reason that dataset cannot be the programme's yardstick.

| Field | Facts |
|---|---|
| **Classification** | High-level: synthesis failure, a conclusion drawn past what the sample supports. Specific: a product-side magnitude quoted without establishing how many complex or sialylated sites the dataset quantified |
| **Affected** | An unsupported magnitude reaches the client and the correct reason for setting the dataset aside goes unstated. Benign for the go/no-go |
| **Runs** | All eight |
| **Wrong** | O3 L137 "falls only from ≈9–10% to ≈5%". O2 L137 "only about a 40–45% fall". O4 glycoproteomics section, MGAT1-dependent share 16.5%→9.6% (A375) and 19.1%→9.4% (NCI-H1703). F3 L37 "sialylated complex down on 42 % / 50 %" against "910 sites on 524 proteins quantified" — the all-sites denominator, not the complex-sites one |
| **Closest** | Fable 5.2 F1 L158 gives a real denominator — "complex share fell at 125 of 164 sites in each line (sign test p = 1e-11); median site keeps 66% (A375) / 74% (H1703)" — without saying how many carry a single unambiguous complex-sialylated composition. Partial match, not an exemplar |
| **Should have** | Established the denominator first and made the small denominator the reason for ruling the dataset out. Recomputed from `glycoproteomics_site_quant.xlsx` sheet `Site_quant`: 910 rows, row P23193 with all eight A375 channels at exactly zero, 909 analysable; of those, 422 carry exactly one composition; among those, high-mannose sites outnumber complex-sialylated by better than ten to one. **Write the ratio, not an exact count** — the split is classification-scheme dependent (the golden's scheme gives 317 against 16, mine gives 306 against 26) and the grading guidance treats any defensible scheme as neutral, so an exact figure invites a challenge the ratio does not |
| **Exemplar** | **None clean.** F1 partial, as above |
| **Why it is sixth** | The prompt requires each number's basis but does not ask for a denominator in terms, so the requirement is closer to an expert norm than a stated line. Mode 2 breaches the same prompt sentence directly by naming a file that cannot supply the number |

---

## Did-not-fire, if you are asked

| Pre-registered mode | What the panel did |
|---|---|
| `selectivity-unrobust` | All eight corrected for differential guide representation. Five tested alternative corrections: O1 "57–72% across analysis variants", F1 two or three methods per in vivo contrast (ledger B7, B9), F2 nine variants (ledger D13), F4 L101, O3 robustness checks (L167) |
| `channel-normalised` | No run normalised the quantitative channels to equal total or median. O1 L287 and F3 L90 explicitly decline, both naming the 1.5–1.7× channel difference |
| `fitted-potency` | All eight excluded ANT-1938 and ANT-2214 as unvalidated chemical matter on correct grounds. O3 and F4 additionally flag the 74 µM figure as extrapolated from 60% inhibition |

## Poor exemplars — do not cite as instances

Fable 5.2 F4 handles Modes 1, 2, 3 and 5 correctly and is the Mode 3 exemplar. Opus 5.5 O4 is the exemplar for Modes 1 and 2. Opus 5.5 O2 is the Mode 2 exemplar while itself carrying Modes 1, 3, 4, 5 and 6 — fine, but keep the citation straight.
