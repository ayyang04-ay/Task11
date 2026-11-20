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
searched in full for the unmapped-arm decision point. Transcripts: not yet read. Remaining decision
points: not yet surveyed.

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
