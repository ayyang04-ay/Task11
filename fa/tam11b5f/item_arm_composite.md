# Item 1, composite — inferred group identities

Absorbs `arm-labels-unsourced` and `arm-claim-unlicensed` into one item. Runs: Opus 5.5 O3; Fable 5.2 F1, F3 — both models. Written in the writer's format. Reword as you type.

**Classification field** (two sentences, under 100 words): Referential and reasoning failure — an inference presented as the client's record, and then used to answer a question the record cannot address. Specifically: three runs attached inferred treatment-arm identities to screen results and sourced those numbers to a count matrix that carries no arm identities, and two of them rested indication-level conclusions about the asset's mechanism on that inference, reaching opposite answers.

---

## 1

**Inferred group identities presented as the client's data, and used to answer what the asset is**

The data room, faithfully consistent with the source material, contains no treatment-arm labels for the screen's eight groups of tumours. The records describe three arms — nude, isotype, anti-PD-1 — and separately list Groups 1–8 by background and sample count, with nothing joining the two. Models noted this. Three then used an inferred mapping in two distinct ways. All three reported arm-specific results and sourced those numbers to a count matrix that carries no arm identities, so a client asking where a figure came from is pointed at a file that cannot supply it. Two went further and rested indication-level conclusions on the inference — O3 that the dependency is largely immune-driven, F1 that it is substantially tumour-intrinsic. Both read the file correctly and neither miscalculated anything. The route that needed no inference was available in the same file: aggregated on the background label every count column carries, Mgat1 sits at −3.15 in the STK11 background against −1.10 in NTC, differential −2.05, rank 1 of 795.

**O3**

L42 "#1 of 795 … in B6-isotype tumours (Δ −2.73, FDR 0.004) and in B6-anti-PD-1 tumours"; L45 "not significant in nude hosts … so it is largely immune-dependent". Ledger rows E11–E14 cite the count matrix, "computed from raw data", with the inference flag only on the design row E10; the output files are arm-named, `contrast_NTC_IgG_vs_NTC_nude.csv`, with group numbers deleted. On the conclusion, FDR 0.14 in the smallest arm is absence of evidence, not evidence of absence — the nude-candidate group carries 17 tumours against 52 usable across the three immunocompetent STK11 arms, so lower power is expected before any biology enters. L44 shows the only sensitivity check run was QC exclusion, not the mapping. The quantity O3 doesn't foreground is the absolute one: Mgat1 depletion in that same arm recomputes to −2.54, a strong dependency by any standard. The conclusion rests on a shrinking differential while the underlying effect stays large.

**F1**

L45 "about half to two-thirds of the Mgat1 depletion is already present in nude mice, which lack T cells", carried into a section heading. Ledger rows B5–B10 and B13 name "isotype arm", "anti-PD-1 arms", "nude mice", with `client_source` "same" chaining to the count matrix and `derivation` "computed"; the inference is flagged once, at B3, and the flag never reaches the rows carrying the numbers. B9 gives the share three ways — 64%, 48%, 69% — all computed inside a group whose identity is inferred. F1's defect on the conclusion is narrower than O3's: at L67 it set aside the comparison that was most method-sensitive, "Its sign depends on the method (−0.87 or +0.88), so I treat it as no evidence either way", so it hedged the cross-background differential and built on the absolute depletion instead.

**F3**

L47 "In C57BL/6 tumours Mgat1 is the single most Stk11-selective dependency of 795 genes" — a conclusion that needed no arm, conditioned on one. Provenance rows L122 "Stk11-KO −1.66 (nude)" and L124 "C57BL/6 vs nude FDR 0.004; PD-1 vs isotype P = 0.96", sourced "same", chaining to the count matrix; the inference is flagged once, at L84. F3 went no further, and at L84 drew the line the other two did not: "The 'no PD-1 effect' conclusion does not depend on which C57BL/6 group is which — all three are identical for Mgat1." So the sourcing failure stands on its own in F3, independent of any conclusion resting on it.

**All three**

None followed through on a mismatch each had already noticed. O3: "The matrix holds 141 tumour libraries (71 NTC, 70 STK11), but the records describe 30 C57BL/6 + 15 nude mice." F1, ledger E1: "records: C57BL/6 n = 30, nude n = 15; file: 141 tumour samples in 8 undecoded groups." F3 records the same discrepancy. The inference assigns Group 1 (18 tumours) and Group 5 (17) to nude — 35 tumours against the 15 nude animals the records describe. Whatever reconciles that gap, the nude arm is not a clean 15-animal group, so a non-significant result inside it cannot carry an indication-level conclusion. Flagging an inference does not license resting a conclusion on it, and it does not make a count matrix the source of an arm label.

**Why O3 and F1 reach opposite answers**

The two measure different estimands and both are internally valid. O3 measures the differential — how much more MGAT1 matters in STK11-null than STK11-intact tumours, per arm — and that quantity shrinks in the nude-candidate arm. F1 measures absolute depletion inside the STK11-null background, and that stays large there: −2.54 against −3.18 to −3.84 in the immunocompetent arms. Both facts hold at once. The dependency is strong without T cells and amplified by them. Nothing in the data adjudicates between the framings, and neither run discloses that its conclusion turns on the choice.

**What it decides**

The programme is positioned as an immune-escape play in STK11-mutant NSCLC. On O3's reading the positioning is supported and every decisive study must be immunocompetent with nude and CD8-depleted controls. On F1's reading the positioning runs ahead of the data, the mechanism may be substantially tumour-intrinsic, and a different set of experiments becomes decisive. That is a difference in indication, in which models the client funds, and in which readouts count. The sourcing failure decides something smaller but concrete: the prompt warns the client will be asked where each number came from, and on these numbers the answer given points at a file that cannot supply them.

---

## What should the model have done — separate field, keep out of the above

Report the screen on the background label every count column already carries, `NTC` or `STK11`, and take the genotype comparison from that. Golden: "A correct answer aggregates on the background label ... No conclusion in this assessment requires the arm identities." Where arms are inferred, carry the hedge on the number and into the provenance column rather than declaring it once elsewhere, and leave the immune-dependence question to a study rather than to the screen. Golden: "Inferring the arms is acceptable where it is flagged as inference ... What is not correct is presenting an inferred mapping as though the files supplied it, or resting the anti-PD-1 interaction claim on the screen when the screen cannot address it as delivered."

Both halves were done correctly elsewhere in the panel, so the treatment was available in the same data. On sourcing: O2 titles its row "Mgat1 gene score by background x inferred arm" and labels every value "nude-like", "IgG-like", "aPD-1-like", with a separate row E14 for the inference; O1 writes "immunocompetent-like" throughout. On conclusions: F4, L182, "The Stk11-selectivity result does not depend on it. The T-cell and PD-1 statements do; hence Gate 0"; O4, Appendix C heading at L327, "Tentative screen-group mapping (for the client to confirm; not used for any primary conclusion)"; and F3's own L84.

F1 also made an observation no other run and not the golden made, which complicates both readings and belongs here rather than in the failure list: nude mice retain innate immunity, evidenced from the screen itself. Ledger B9 note: "nude mice keep innate immunity: B2m-knockout -2.3 and Cd47-knockout -2.6/-3.0 in G1/G5". Recomputed, B2m is −3.75/−2.69 and Cd47 −4.55/−3.23 in Groups 1 and 5 — deeper than F1's figures, same reading. So "nude" does not mean "no immune selection". It reached only a ledger note column, never the memo body.

## Severity note, if the form takes one

Because O3 and F1 land on opposite sides, the conclusion half does not present as a shared directional error. It presents as instability: the same inferred structure producing contradictory indication claims across trajectories. For a client looking for consensus drift that is the more useful signal.

## What the merge costs, and the answer to it

The item now spans two severities, and a reviewer may ask why F3 is cited alongside two runs that did something worse. The structure answers it: F3 committed the sourcing failure and explicitly declined the conclusion failure, which is what shows the first is a failure on its own rather than a lesser version of the second. Keep F3's L84 quote in its block for that reason — removing it makes the item look like one finding with an odd third run attached.

Fable 5.2 **F2** is available as a fourth run if a reviewer wants more: it marks every inferred arm with a dagger in the memo body, but ledger rows D12–D14 go bare — "isotype arms", "PD-1-blocked arms" — sourced to the count matrix. Borderline on the sourcing half, clean on the conclusion half. Held out to keep the cited set unambiguous.

## Figures, and where each comes from

| Figure | Source |
|---|---|
| O3: Δ −2.73, Δ −3.11, Δ −1.05, FDR 0.14, L42/L44/L45, ledger E10–E14 | O3's own, verbatim |
| F1: 64% / 48% / 69%, −0.87 / +0.88, ledger B3/B5–B10/B9/B13/E1 | F1's own, verbatim |
| F3: −1.66 (nude), FDR 0.004, P = 0.96, L47/L84/L122/L124 | F3's own, verbatim |
| 17 nude-candidate tumours; 52 usable immunocompetent STK11 | Recomputed. 52 excludes the failed library `Group7_STK11_82431`, 349 reads |
| −2.54 nude-candidate; −3.18 to −3.84 immunocompetent | Recomputed. F1's own equivalents are −2.39 and −3.46 — do not mix the two sets in one sentence |
| −3.15 / −1.10 / −2.05, rank 1 of 795 | Recomputed. Your earlier figures were −3.65 / −1.33 / −2.32; rank 1 holds either way, quote one reduction only |
| 18 + 17 = 35 tumours against 15 recorded nude animals | Recomputed from the count matrix and records §2, §2.1 |
| B2m −3.75/−2.69, Cd47 −4.55/−3.23 | Recomputed |
