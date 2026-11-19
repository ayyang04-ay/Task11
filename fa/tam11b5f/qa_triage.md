# tam11b5f — QA triage (Taiga export v1, problem version 7d0fedb4)

Freshness: **fresh.** QA ran against `7d0fedb4`, the version both run jobs used. Latest QA chain completed 2026-11-19 08:11Z; the Opus runs finished 04:22Z and the Fable runs 05:20Z, so every check could see the whole panel. No STALE findings. 9 items across 7 runs.

**Export gap, reported not explained:** the ClaudeScope job (`5a8326dd`) reports `findingCount: 6` ("6 clusters identified") against `itemCount: 2`. Only the two gated clusters are in this export. The other four clusters are not present in `qa_items.json`, `qa_report.md` or `qa_jobs.json` — only their count. They may hold mode candidates and cannot be read from what was supplied. Re-export or open the ClaudeScope job to see them.

## Triage

| # | Finding | Sev | Runs | Type | Affects golden? | Action |
|---|---|---|---|---|---|---|
| 5 | In vivo screen arm key missing; 141 tumour libraries against 45 mice | error | F1, F2, F4 | Ambiguity / missing resources | **Yes — already done** | Handled by `450fab4` on `claude/gallant-shannon-2u3m3g`, which added golden §"Expected treatment of the unmapped screen arms". That session verified the gap originates upstream in the deposit, not in package preparation. Edit confirmed present in the working copy. **Closed.** Sent to Phase 1 as a candidate; see below |
| 0 | Same gap, restated by env linter | info | O4 | Ambiguity | Duplicate of #5 | Closed by the same edit |
| 8 | Agentic grader holds no reference call, rubric or grader_guidance | error | — | Grader-only | No | **No grader edit** per the rule that the grader is not the product. Checked whether the same claim appears in the golden: it does not. `pilot/README.md` records that Studio offered no grader field for this task, so the writer could not configure one. `fix: env_author`. Does not block. **Deferred** |
| 2, 3 | Same grader gap, restated by env linter and reward-hacking check | info | O4 | Grader-only | No | Duplicates of #8. Both checks probed for mis-scoring and found none: 0.0 for an empty hand-in, 0.15 for a polished memo with the wrong call, 0.45–0.55 for hand-ins missing required parts. **Deferred** |
| 6 | No PDF rasteriser or renderer in the image | error | F1, F4 | Tooling | No | **Ignore** as a mode source. Note in the per-run profile: it affected every run, and at least two disclosed they could not visually verify their own deliverable. The env linter independently downgraded it to info after confirming pypdf recovers every figure page at full resolution |
| 1 | Same tooling gap, restated by env linter | info | — | Tooling | No | Duplicate of #6 |
| 7 | Problem too easy: 90% pass rate over 4 runs | warning | — | Difficulty | No | Not golden-fixable. Consistent with the submit gate: job means are 0.890 and 0.903 against a 0.55 ceiling. **Task-level, deferred** |
| 4 | `undisclosed_constraints` on the citation requirement | info | — | Self-dismissed | No | The finding dismisses itself: "this is a disclosed expectation, not a hidden constraint". **No action** |

No finding requires a prompt or data-room edit. No blocker.

## Finding 5 as a mode candidate — confirmed in transcripts, below the floor

The golden edit supplies the test: inferring the arms is acceptable where flagged as inference; what is not correct is presenting an inferred mapping as though the files supplied it, or resting the anti-PD-1 interaction claim on a screen that cannot address it as delivered. Checked against all eight deliverables.

| Run | Handling |
|---|---|
| O1 | Robust. "indistinguishable across the three immunocompetent-like Stk11-KO arms ... **whichever of them received anti-PD-1**" (L136) |
| O2 | Robust. "**No group assignment changes this**: three STK11 groups are indistinguishable" (L110) |
| O4 | Exemplary. "The screen's group→condition map ... is not documented, **so T-cell and anti-PD-1 dependence cannot be tested directly**" (L157); the inferred figure is stated conditionally, "Under that mapping" (L100) |
| F1 | Robust. Lists the mapping as an open question to the client (L82); the contrast carries a positive control (L143) |
| F2 | Robust and most thorough. † marks every inferred arm; "the screen result holds **whichever** of the three immunocompetent arms received anti-PD-1, across nine analysis variants" (L35) |
| F3 | Borderline. Declares "Used an inferred key; flagged" (L84), then states "PD-1 blockade did not deepen the Mgat1 dependency in the screen" (L34) with no robustness note at that point |
| F4 | No prominent screen-based anti-PD-1 claim |
| **O3** | **Instance.** Reports results in bare arm labels as though established — "#1 of 795 ... in **B6-isotype** tumours (Δ −2.73, FDR 0.004) and in **B6-anti-PD-1** tumours (Δ −3.11, FDR 2×10⁻⁷)" (L42), "smaller and not significant in **nude hosts**" (L45), "STK11 × immune interaction ranks #3 ... with anti-PD-1" (L45), "no greater with anti-PD-1 than with isotype" (L92). Its single disclosure (L136) immunises only the selectivity claim — "The STK11-vs-NTC conclusions only assume that groups pair across backgrounds" — and not the immune-dependence and anti-PD-1 claims, which do turn on the labels |

**Status: held, below the prevalence floor.** One clean instance (O3) and one borderline (F3). Counting F3 reaches two; an expert can defend declaring the inference once and then using short labels, so the writer decides whether F3 counts.

Two things worth saying plainly about this finding:

- The cluster names F1, F2 and F4 — on my reading, three of the runs that handled the gap **most** carefully, two of them with explicit robustness arguments. The run attribution marks where the issue is visible in a transcript, not which runs erred. Confirming in the transcripts reversed the direction the cluster pointed.
- The panel largely defeats the golden's own objection. Where all three candidate immunocompetent arms are statistically indistinguishable, the anti-PD-1 conclusion holds under every mapping, so for those runs the screen *can* address the question as delivered. Four runs made that argument. It is worth considering whether the golden should concede it.

## Effect on the existing ledger

No counterfactual changes. Modes 1, 2 and 3 are untouched by any finding. Modes 4 and 5 are untouched: no QA item bears on the safety position or the product-side denominator, so their contested requirement basis stands as the writer's call, not a QA question.
