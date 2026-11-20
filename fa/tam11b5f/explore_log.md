# Exploration log — task tam11b5f

Panel: 8 runs, 4 Opus 5.5 and 4 Fable 5.2. Map taken from the export's `job_info.json` and
`all_runs.csv`, not constructed.

| | Opus 5.5 (job de39df86) | Fable 5.2 (job c638eb2d) |
|---|---|---|
| A1 | `bd63c97e` | `aa6a0794` |
| A2 | `2caa3b04` | `734093b7` |
| A3 | `bc8b9e20` | `73e1ddd7` |
| A4 | `409bdac0` | `69bb2ad2` |

All 8 completed, none refused. Scores 0.88-0.91. The grading config records
`grader_guidance: None` and `rubric: None`, so the agentic grader ran unguided.

**Reading coverage.** All 8 deliverable memos: opening recommendation and section structure read;
searched in full for the unmapped-arm decision point, the seven golden next-studies, the safety
position, the glycoproteomics normalisation, the lectin/mass-spectrometry comparison, the set-aside
sections and section structure. Transcripts: not yet read.

## Step 1 — Decision points, from the prompt

Each is taken from a line the prompt states. Edit this list before the divergence table is built,
so the components come from the prompt rather than from the skill.

| # | Decision point | Prompt line it comes from |
|---|---|---|
| 1 | The recommendation on the asset | "Give me your recommendation on what they should do with this asset" |
| 2 | The case behind the call | "build out the case behind your call as strongly as the data allows" |
| 3 | What the next studies need to establish | "A strong recommendation should also detail next steps: what the next studies need to establish" |
| 4 | Comparisons the data needs to include | "and relevant comparisons the data needs to include" |
| 5 | The not-advance branch | "If your call is not advance, then what data would need to be demonstrated to bring it back" |
| 6 | Which claims are cited, and the analysis behind them | "When relevant, your recommendation should cite the original data and the analysis that supports your conclusions" |
| 7 | What was set aside or discounted | "Tell me anything you set aside or discounted, and why" |
| 8 | Level of the answer | "Let's keep this high level: focus on design, specification, and interpretation. We don't need protocols or assay methodology" |

### Writer's note on scope of the request

The writer asked for divergence across pillars and steps, not only the verdict. Decision point 2
covers the case as a whole; the golden carries named components within it. Whether those become
their own rows, or stay inside row 2, is the writer's call. The golden's components are:

- target validation and its genotype comparison
- catalytic dependence of the phenotype
- the chemical matter, including the acquired compounds
- absence of cellular pharmacology
- the state of the pharmacodynamic readout
- the safety position
- treatment of the unmapped screen arms

## Step 2 — Divergence table (in progress)

### Decision point 1 — The recommendation on the asset

| Approach | Runs | Model split | Golden | Matches golden? | Where |
|---|---|---|---|---|---|
| Opens "do not advance" / "hold", then describes a gated bridge package and states the asset is not being killed | O1, O2, O3, O4, F1, F2, F3, F4 | all 8 | Opens "Advance, but not into IND-enabling work", then describes a bridge package | **Same substance, opposite opening word** | each memo, section 1 |

Every run's substance matches the golden's: no IND-enabling or candidate-enabling spend, fund a
gated cell-and-mechanism package first, keep the target. The difference is which word carries the
headline. O1: "Hold it where it is... This is a hold, not a kill". O2: "This is a 'not yet', not a
'no'". F1: "By 'advance' I mean in vivo efficacy work, candidate nomination". Several define the
term before using it, which the golden does not.

### Decision point 2 — within the case: treatment of the unmapped screen arms

| Approach | Runs | Model split | Golden | Matches golden? | Where |
|---|---|---|---|---|---|
| Inferred arm identities from control-gene behaviour, flagged as inference, then used the labels to compute a mechanism conclusion | O1, O2, O3, O4, F1, F2, F3, F4 | all 8 | States the mapping is unrecoverable, aggregates on the background label, notes inference is acceptable where flagged and no conclusion rests on it | **No** — all 8 rest a conclusion on the inferred labels | see below |

All 8 flagged the inference as theirs rather than the client's. Representative: O1 "arm identity
inferred; no key was supplied"; O4 "Marker-gene inference (Appendix C) places the nude cohorts at
Groups 1 and 5"; F2 marks every inferred arm with a dagger; F3 records "Medium (group identity
inferred)"; F4 "the records do not label the arms".

**The runs then divide on which quantity they computed from those labels, and reach opposite
conclusions about T-cell dependence.**

| Estimand computed | Runs | Result reported | Conclusion drawn | Recomputed here |
|---|---|---|---|---|
| Absolute Mgat1 depletion within the STK11 background, putative nude arm vs the others | O1, O4, F1, F4 | O1 "about 60%"; F1 "half to two-thirds"; F4 "74% ... and 44% by a pooled-count model" | A large fraction of the dependency does not require T cells | nude G5 -1.71 vs G6-8 mean -3.28; nude retains **52%** |
| STK11-minus-NTC differential, within each putative arm | O3 | "smaller and not significant in nude hosts (delta -1.05, FDR 0.14)" | The dependency is largely immune-dependent | nude G5-G1 **+0.37**; B6 pairs -1.61, -2.27, -2.91 |

Both families of number reproduce from the raw counts. They are different quantities, not
competing estimates of one quantity, and each supports the reading its run gives it. O3 is the only
run in this group; within Opus it is the one whose approach no other Opus run shares.

### Decision point 3/4 — Next studies, and what each is compared against

Coverage of the golden's seven studies. `Y` = the run names the study as a required next step.

| Golden study | O1 | O2 | O3 | O4 | F1 | F2 | F3 | F4 | n |
|---|---|---|---|---|---|---|---|---|---|
| 1 Cellular target engagement | Y | Y | Y | Y | Y | Y | . | Y | 7 |
| 2 Cellular potency for the lead | . | Y | Y | Y | . | . | . | Y | 4 |
| 3 **Cross-species: mouse enzyme potency** | . | . | . | Y | Y | Y | Y | Y | 5 |
| 4 Mechanism of inhibition / maximum achievable | Y | Y | Y | Y | Y | . | Y | Y | 7 |
| 5 Selectivity, paralog and pathway | Y | Y | Y | Y | Y | Y | Y | Y | 8 |
| 6 Lead engages the same pocket | Y | Y | Y | . | Y | Y | . | Y | 6 |
| 7 **Cardiac safety pharmacology** | . | . | . | . | . | . | . | . | **0** |

Study 5 is unanimous. Studies 1, 4 and 6 are near-unanimous.

**Study 3 runs on model lines.** All four Fable runs name mouse-enzyme potency, three of them as a
precondition on any mouse study. F4: "Potency on mouse Mgat1, which every syngeneic experiment
depends on, has not been measured." F3 states the interpretive consequence: "An in vivo study run
today could not be interpreted whichever way it came out: a negative result could be exposure,
permeability, mechanism, species or biology." Of the Opus runs only O4 names it ("There is no mouse
Mgat1 potency, no panel against related glycosyltransferases"). O1, O2 and O3 do not; their
species-word hits are the unstated hepatocyte species in the compound properties, a different point.
So: 5 of 8, and 4 of 4 within Fable against 1 of 4 within Opus.

**Study 7 is absent from all 8.** O3's only cardiac word is `hERG` inside a generic
developability list ("Permeability, PPB, species-defined clearance, CYP/hERG"), not an on-target
cardiac position. No run names cardiomyocyte-specific deletion, dilated cardiomyopathy, ion-channel
glycosylation, embryonic lethality, the autoimmunity overlap with the intended pharmacology, or the
bronchial-epithelium point for a lung indication.

### Decision point 2, component: the safety position

| Approach | Runs | Model split | Golden | Matches golden? |
|---|---|---|---|---|
| Safety treated as an absence of client data; deferred to a tolerability readout inside a later in vivo study | O1, O2, O3, O4, F1, F2, F3, F4 | all 8 | A position: characterisable risk rather than a blocker, cardiac safety pharmacology first, autoimmunity read inseparable from the intended effect | **No overlap** |

Representative: F1 "There are no data on the mouse enzyme, on selectivity against related enzymes,
or on tolerability." O4 "There are no data on T-cell function or tolerability under MGAT1
inhibition." O3's entry is the parenthetical "Tolerability (weight, blood counts, immune
phenotype)." O2 carries no safety sentence at all. The golden pre-registers this shape explicitly:
"An answer that reports only that no toxicology data exist has not taken a position."

**A stated methodological commitment sits upstream of this.** Six of the eight declare, as a
positive choice, that no outside knowledge was used as evidence:

- F1: "Anything from outside the package, including published MGAT1 biology and public cell-line genotypes." (set aside)
- F2: "Outside knowledge. I did not use published cell-line genotypes, MGAT1 literature or target-class precedent as evidence."
- F3: "No outside data are used as evidence; where I rely on general reasoning rather than a client measurement, I say so."
- O2: "No external data were used for any claim."
- O3: "No outside data or literature was used as evidence."
- O4: "No external data supports any conclusion."

O1 and F4 make no blanket declaration and also produce no safety position. The golden's safety
section is the one section it marks "*Named domain knowledge, not from the package.*"

### Decision point 2, component: the glycoproteomics normalisation

| Approach | Runs | Model split | Golden | Matches golden? |
|---|---|---|---|---|
| Normalise the channels to equal total signal | — | none | Forecloses it | **0 of 8 took this route** |
| Decline the absolute magnitudes; substitute within-channel composition shares | O1, F1 | 1+1 | Uses the absolute ratios | Conclusion same, route different |
| Centre on Man7-9 glycopeptides upstream of MGAT1 as an internal reference | F4 | 1 | Uses the absolute ratios | Conclusion same, route different |
| Magnitudes "directional only" / "used for direction" | O2, F3 | 1+1 | Uses the absolute ratios | Conclusion same, route different |
| Not used; cites absent proteome normalisation and composition assignments | O4 | 1 | Uses the absolute ratios | Conclusion same, route different |
| Does not address channel loading | O3 | 1 | — | — |

Every run recognises the unequal channel totals: seven of eight state the ~1.6x figure. None
normalises to equal total. The divergence from the golden is that the golden's quantitative
foreclosure evidence does not appear in any run: **no run reports the 0.893 bulk centre**, the
245-up / 658-unchanged split, the 27.0% figure, the 317 high-mannose against 16 complex-sialylated
count, or the 6 down-moving sites. The three runs matching `0.89` are matching other quantities
(F3 a nude-versus-B6 permutation difference, O4 a tumour-volume ratio, O3 a median guide log2FC).

### Decision point 2, component: lectin against mass spectrometry

| Approach | Runs | Model split | Golden | Matches golden? |
|---|---|---|---|---|
| Reads the magnitude disagreement with PHA-L as bearing on whether the mass spectrometry is sound | O2, O3 | 2 Opus, 0 Fable | "The disagreement is not evidence that either is wrong"; the two readouts are not commensurable | **Foreclosed inference entered** |
| Cites TMT ratio compression as a general reason to set magnitudes aside, without the comparison | O1 | 1 Opus | — | Adjacent |
| Does not raise the comparison | O4, F1, F2, F3, F4 | 1 Opus, 4 Fable | — | — |

O2: "This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference."
O3: "This conflicts with the =96% PHA-L loss and fits TMT ratio compression or misassignment." The
two sentences are near-identical in construction. Both are Opus; no Fable run makes the move.

### Decision point 7 — What was set aside or discounted

All 8 carry a dedicated section. Items by prevalence:

| Item set aside | Runs | n |
|---|---|---|
| ANT-1938 and ANT-2214, the acquired compounds | all 8 | 8 |
| ANT-0592 potency and KD, against its kinetic solubility | all 8 | 8 |
| Screen library Group7_STK11_82431 (349 reads) | all 8 | 8 |
| Glycoproteomic magnitudes, in some form | O1, O2, O3, O4, F1, F2, F3 | 7 |
| NY-ESO-1 CCLE panel, as not client-generated | O1, O2, O3, O4, F2, F3, F4 | 7 |
| **The Group3_NTC duplicate library pair** | O3, O4, F2, F3, F4 | 5 |
| Group-to-arm mapping, held as inferred | O1, O4, F2, F3, F4 | 5 |
| Significance of the tumour-growth figures | O1, O2, F1, F2, F4 | 5 |
| Guide Mgat1_3 / MGAT1_3 | O2, F2, F4 | 3 |
| Cross-background comparison p-values | O2, F1, F2 | 3 |

Counts are scoped to each run's set-aside section, not to the memo as a whole: several items are
discussed elsewhere by runs that do not list them here. Section size ranges from 1.7 kB (F1, O4)
to 4.5 kB (F3), and the three longest are Fable.

Five runs list a near-duplicate pair among the in vivo libraries, with correlations in close
agreement: r = 0.988 (F3), 0.98 (F4), log-CPM r = 0.984 and raw-count r = 0.995 (O3), against a
stated next-best tumour pairing of 0.76 (F3) or median 0.67 (O3). F3 draws the consequence
"effective n for Group 3 is 14"; F4 reads the two animal IDs as "a digit transposition". F1 reports
four excluded libraries in its set-aside entry without naming the pair. The golden's set-aside
section does not carry this item. Whether it belongs there is the writer's call.

### Decision point 8 — Level of the answer

| | O1 | O2 | O3 | O4 | F1 | F2 | F3 | F4 | golden |
|---|---|---|---|---|---|---|---|---|---|
| words | 3996 | 4067 | 4147 | 4533 | 5802 | 8722 | 4045 | 5853 | 1770 |

All 8 exceed the golden, by 2.3x to 4.9x. Fable is the longer side (median 5828 against 4107).
On the prompt's own exclusion the runs largely hold: protocol-level content inside the next-steps
sections is 0 to 4 sentences per run, and two runs mark the boundary in a heading or aside
(O4 section 5 "a gated plan (design and comparisons, not protocols)"). The two runs that go
furthest give a powered n per arm from the client's own error bars (F3 "about 17 mice per arm...
about 36 for two-thirds of it, more if they are SEM"; O4 "=11-20 per arm"), which sits on the
design side of that line.

**Scope the runs added that the prompt did not request.** Seven of eight carry a section
addressed to the client, separate from the recommendation: questions to put to the client, or
data-integrity and documentation issues to resolve (F1 s7, F2 s7, F3 s6, F4 s6, O1 s8, O2 s8,
O3 s7). O4 has no such section but carries Appendix C, a tentative screen-group mapping for the
client to confirm. Three runs also open with a scorecard of claims against evidence (O1 s2,
O2 s2, F2 s2). The golden has neither.

## Step 3 — Patterns

### All runs differ from the golden

| Decision point | What every run does | What the golden does |
|---|---|---|
| 1. The recommendation | Opens with "do not advance" or "hold" | Opens with "advance, but not into IND-enabling work" |
| 2. Unmapped screen arms | Infers arm identities and rests a mechanism conclusion on them | Aggregates on the background label; no conclusion rests on inferred arms |

### Unique in model

| Run | Approach no other run of its model shares | Also differs from golden |
|---|---|---|
| Opus A3 (`bc8b9e20`) | Computes the STK11-minus-NTC differential per inferred arm rather than absolute depletion, and reports the dependency as largely immune-dependent | Yes |

### Cross-model pairs, same verdict different route, deliverable vs transcript

Not yet surveyed. Transcripts unread.
