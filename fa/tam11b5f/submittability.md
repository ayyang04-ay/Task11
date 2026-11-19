# tam11b5f — submittability

Task `e55870a045744a9e932736ae7ca1822f`. Panel: 4 Opus 5.5 (`de39df86`) + 4 Fable 5.2 (`c638eb2d`), 8/8 completed, 0 refused.
Mode: **trajectory-only**. `grading_config.json` carries `grader_guidance: null`, `rubric: null`, `grader_files: []` on both jobs — the runs were scored by the default grader, so no score is cited below and no run is ranked by one. `pilot/grader.txt` was never submitted and is used only as a candidate screen.

## 1. Verdict

**Submittable after golden edits.** Two modes clear every mechanical bar; three more are candidates the writer must rule on. One golden figure needs hedging and one pilot document needs a count corrected. Nothing requires a prompt or data-room edit, so no rerun.

## 2. Checks

| Check | Result | Reason |
|---|---|---|
| QA fixability | Pass | No QA report supplied with the export; nothing to triage, so nothing can block |
| Golden derivability | Pass, with one edit | Every golden figure I recomputed reproduces from the room as the runs saw it. One exception is scheme-dependent, not wrong — see §4 |
| At least one candidate | Pass | Modes 1 and 2 confirmed: present in 3 runs each, governing line located in prompt or room, load-bearing |

Room provenance: last room commit `2343381`, 2026-11-18 15:47Z; runs began 2026-11-19 02:54Z. No room file changed after the runs, so the working tree is the room they saw. `task_files/` was excluded from both exports; the room was taken from version control instead.

## 3. Modes

| # | Mode | Class | Runs | What happened | Why it is a mistake | Where visible | Status |
|---|---|---|---|---|---|---|---|
| 1 | Mouse efficacy study with no mouse potency | Adjudication | O1, O2, O3 | Each specifies a mouse efficacy study — O1 a 2×2 in a syngeneic model, O2 "sgSTK11 MC38", O3 efficacy against the "≈50% in MC38 sgSTK11" benchmark — and none asks anywhere for the compound's potency against mouse MGAT1. Every compound measurement in the room is on human enzyme (records §6.1, UniProt P26572); every in vivo model is MC38 in C57BL/6 or nude mice (records §2) | Prompt: next steps must state "what the next studies need to establish and relevant comparisons the data needs to include". A named comparator in the package is uninterpretable as specified | O1 memo L225; O2 L197 and bring-back L225; O3 gate table L110. Transcripts: no species-potency reasoning anywhere in the three runs | **Confirmed** |
| 2 | SPR surface convention read, then unapplied | Analytical | O2, O3, F2 | Records §6.4 states all three competition surfaces were freshly prepared at differing immobilisation levels (~9000, ~3600, ~3500 RU) and ends "protein immobilization levels differed". All three runs received that text as raw tool output and reasoned about it for the stoichiometry question. In the deliverable O3 asserts "cooperatively: each ligand raises the other's affinity 1.6–2×" and builds a product-complex-stabilising mechanism on it; O2 asserts "UDP *tightens* ANT-3744 binding" and calls the two surfaces "an equivalent surface"; F2 states "Immobilisation levels per run are not recorded" | Room states the convention outright; prompt requires claims be supported by the client's data. A two-fold shift in single values across separately prepared surfaces does not carry a thermodynamic result, and F2's deliverable misreports what the records contain | O3 memo L75, records read at transcript elems 22/28, reasoning at 246; O2 memo L102 and L260, read at elem 22, reasoning at 48/213; F2 memo L170, read at elem 31, reasoning at 48/321 | **Confirmed** |
| 3 | Readout disagreement read as assay defect | Synthesis | O2, O3 | Both set the glycoproteomics aside as a PD reference because its magnitude disagrees with the lectin result. O2: "only about a 40–45% fall ... This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference". O3: "falls only from ≈9–10% to ≈5% ... This conflicts with the ≈96% PHA-L loss and fits TMT ratio compression or misassignment" | Surface lectin avidity and whole-lysate glycopeptide abundance measure different things in different compartments; they have no reason to agree, so disagreement is not evidence either is defective. Right conclusion, basis that does not produce it | O2 memo L137 and L261; O3 memo L137 | **Confirmed present; defensibility contested** — see §6 |
| 4 | Safety treated only as a data gap | Reasoning | O1, O2, O3, O4, F1, F2, F3, F4 | Every run records safety as absent and schedules it as future work — O1 "Absent", O4 "Untested", F2 "**No data**", F3 "no data on T-cell function or tolerability" — and none names an on-target risk from MGAT1 biology. Across all eight deliverables: no mention of cardiac risk (one glancing hit in F2), autoimmunity, or germline loss | Golden §5 takes a position from target biology. But the prompt restricts claims to the client's data and the golden labels its own safety content "*Named domain knowledge, not from the package*" | O1 L47; O4 L38; F2 L53; F3 L37 | **Held — requirement basis contested** |
| 5 | Product-side magnitude with no denominator | Synthesis | O1, O2, O3, O4, F1, F2, F3, F4 | All eight quote a product-side magnitude (complex or sialylated signal falling by a stated amount). None states how many complex or sialylated sites were actually quantified. F1 comes closest with "125 of 164 sites" | Golden: what rules the dataset out as a product-side reference is the size of that denominator. The prompt requires each number's basis, but does not ask for a denominator in terms | F1 L158; O3 L137; O4 glyco section; F3 L37 | **Held — requirement basis generic** |

## 4. Golden edits required

| Location | Change | Why |
|---|---|---|
| `golden_response.md` L42 | "Of sites with an unambiguous single composition, **317** are high-mannose and **16** are complex-sialylated" → state the classification scheme, or hedge the counts as scheme-dependent | The conclusion is robust; the figures are not. My classifier on the same 909 analysable sites gives 306 high-mannose and 26 complex-sialylated from 422 single-composition sites. The grader's own neutral list allows "any defensible glycan classification scheme", so two schemes disagreeing is expected — but Mode 5's counterfactual quotes this number, and it should not be quoted as exact |
| `failure_modes.md` L7 | "two models x eight attempts = sixteen trajectories" → four attempts per model, eight trajectories | The shipped panel is 4 + 4. Any prevalence language built on sixteen is wrong |

Everything else I checked reproduces: 909 analysable sites and row P23193 all-zero; 245 sites up >2-fold (27.0%) and 6 down (0.7%) in A375; total intensity 1.5231e10 against 9.3026e9, factor 1.64; records §6.4 immobilisation statement; human construct P26572; MC38/C57BL/6 in vivo.

## 5. Pre-registered modes that did not fire

| Mode | Outcome |
|---|---|
| `selectivity-unrobust` | **Did not fire.** All eight corrected for differential guide representation — O1 L326–328, O3 L167, O4 L300, F1 L66, F2 ledger A2/A5, F3 L119 — and five ran alternative corrections: O1 "57–72% across analysis variants", F1 four alternative scorings, F2 nine variants, F4 L101, O3 "robustness checks". This panel is materially stronger than the three validation attempts here |
| `channel-normalised` | **Did not fire.** No run normalised to equal total or median. O1 L287 and F3 L90 explicitly decline, naming the 1.5–1.7× channel difference |
| `fitted-potency` | **Did not fire.** All eight excluded ANT-1938 and ANT-2214 on correct grounds; O3 and F4 additionally flag the 74 µM figure as extrapolated |
| `lectin-ms-commensurable` | Fired in O2 and O3 only, not panel-wide (Mode 3) |
| `no-cross-species` | Fired in O1, O2, O3 (Mode 1). O4, F2, F3, F4 all handle it |
| `no-safety-position` | Fired in all eight (Mode 4), but on a contested basis |

## 6. For the writer to decide

**Mode 3 defensibility.** For: the error is structural — disagreement between non-commensurable readouts is used as the evidence, and O2 compounds it by also calling the surfaces equivalent. Against: TMT reporter-ion compression is real and an expert can defend invoking it; O3 hedges with "or misassignment"; both runs reach the correct conclusion. Two runs, both Opus — clears the floor of 2 but not the one-of-each pattern the client prefers.

**Mode 4 basis.** For: the prompt asks for the case "as strongly as the data allows" and for what would bring the asset back, and all eight imported outside knowledge elsewhere (MC38's tissue of origin, core-essential gene identity), so a blanket no-outside-knowledge defence does not hold. Against: the prompt says the client's files are "the only data they trust" and "all recommendations and claims must be supported by their data", and the golden flags its own safety paragraph as outside the package. A careful expert can defend declining to import a safety literature the client has not seen.

**Mode 5 basis.** Same shape as Mode 4, weaker: the requirement is an expert norm, not a prompt line.

## 7. Task notes

- **The verdict is over-determined, as pre-registered.** All eight runs land on the same call: do not advance now, hold behind gates, fund a short gated proof-of-pharmacology package, keep the target. The golden says "advance, but not into IND-enabling work; fund a bridge package" — the same gate with the word attached to the other side. There is no verdict split to trace, so every mode here is about a flawed route, not a wrong answer.
- **Coverage screen is clean.** Every run referenced all sixteen room files. No non-use candidate.
- **Thinking is summarised**, not raw (`thinking_summary_status: ready`). 116–156 blocks per run, 70–100% carrying text, median ~550 characters. Claims about what a run weighed internally are not supportable, so the raised-then-abandoned shape is ruled out. Mode 2 does not depend on it: the records text reached every run as raw tool output.
- `scipy` is absent from this container; any test is hand-implemented.
