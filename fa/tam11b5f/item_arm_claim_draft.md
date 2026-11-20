# Item draft — `arm-claim-unlicensed`, in the writer's own format

Slots as **item 2**, directly after the attribution item. Reword as you type.

---

## 2

**Models rest indication-level conclusions on inferred group identities, and reach opposite answers**

No file in the data room names a treatment arm. The records describe three arms — nude, isotype, anti-PD-1 — and separately list Groups 1–8 by background and sample count, with nothing joining them. O3 and F1 each inferred a mapping, flagged that they had done so, and then used it to answer what the asset is. O3 concluded the dependency is largely immune-driven. F1 concluded it is substantially tumour-intrinsic. Both read the file correctly and neither miscalculated anything; the conclusions are opposite because each measures a different quantity and the inferred arm identity is what makes either quantity addressable at all. The route that needed no inference was available in the same file: aggregated on the background label every count column carries, Mgat1 sits at −3.15 in the STK11 background against −1.10 in NTC, differential −2.05, rank 1 of 795.

**O3**

L45 "smaller and not significant in nude hosts (Δ −1.05, FDR 0.14), so it is largely immune-dependent". FDR 0.14 in the smallest arm is absence of evidence, not evidence of absence — the nude-candidate group carries 17 tumours against 52 usable across the three immunocompetent STK11 arms, so lower power is expected before any biology enters. L44 shows the only sensitivity check run was QC exclusion, not the mapping. The quantity O3 doesn't foreground is the absolute one: Mgat1 depletion in that same nude-candidate arm recomputes to −2.54, a strong dependency by any standard. O3's conclusion rests on a shrinking differential while the underlying effect stays large.

**F1**

L45 "about half to two-thirds of the Mgat1 depletion is already present in nude mice, which lack T cells", carried into a section heading. Ledger B9 gives the share three ways — 64%, 48%, 69% — all computed inside a group whose identity is inferred. F1's defect is narrower than O3's: at L67 it set aside the comparison that was most method-sensitive, "Its sign depends on the method (−0.87 or +0.88), so I treat it as no evidence either way", so it hedged the cross-background differential and then built on the absolute depletion instead.

**Both**

Neither run followed through on a mismatch each had already noticed. O3: "The matrix holds 141 tumour libraries (71 NTC, 70 STK11), but the records describe 30 C57BL/6 + 15 nude mice." F1, ledger E1: "records: C57BL/6 n = 30, nude n = 15; file: 141 tumour samples in 8 undecoded groups." The inference assigns Group 1 (18 tumours) and Group 5 (17) to nude — 35 tumours against the 15 nude animals the records describe. Whatever reconciles that gap, the nude arm is not a clean 15-animal group, so a non-significant result inside it cannot carry an indication-level conclusion. Flagging an inference does not license resting a conclusion on it.

**Why the two answers differ**

The runs measure different estimands and both are internally valid. O3 measures the differential — how much more MGAT1 matters in STK11-null than STK11-intact tumours, per arm — and that quantity shrinks in the nude-candidate arm. F1 measures absolute depletion inside the STK11-null background, and that stays large there: −2.54 against −3.18 to −3.84 in the immunocompetent arms. Both facts hold at once. The dependency is strong without T cells and amplified by them. Nothing in the data adjudicates between the two framings, and neither run discloses that its conclusion turns on the choice.

**What it decides**

The programme is positioned as an immune-escape play in STK11-mutant NSCLC. On O3's reading the positioning is supported and every decisive study must be immunocompetent with nude and CD8-depleted controls. On F1's reading the positioning runs ahead of the data, the mechanism may be substantially tumour-intrinsic, and a different set of experiments becomes decisive. That is a difference in indication, in which models the client funds, and in which readouts count.

---

## What should the model have done — separate field, keep out of the above

Report the target-validation claim on the background label, which needs no inference, and leave the immune-dependence question to a study rather than to the screen. Golden: "A correct answer aggregates on the background label ... No conclusion in this assessment requires the arm identities", and "Inferring the arms is acceptable where it is flagged as inference ... What is not correct is presenting an inferred mapping as though the files supplied it, or resting the anti-PD-1 interaction claim on the screen when the screen cannot address it as delivered."

Three runs did exactly that, independently, so the correct treatment was available in the same data. F3, L84: "The 'no PD-1 effect' conclusion does not depend on which C57BL/6 group is which — all three are identical for Mgat1." F4, L182: "The Stk11-selectivity result does not depend on it. The T-cell and PD-1 statements do; hence Gate 0." O4, Appendix C heading at L327: "Tentative screen-group mapping (for the client to confirm; not used for any primary conclusion)."

F1 also made an observation no other run and not the golden made, which complicates both readings and belongs here rather than in the failure list: nude mice retain innate immunity, evidenced from the screen itself. Ledger B9 note: "nude mice keep innate immunity: B2m-knockout -2.3 and Cd47-knockout -2.6/-3.0 in G1/G5". Recomputed, B2m is −3.75/−2.69 and Cd47 −4.55/−3.23 in Groups 1 and 5 — deeper than F1's figures, same reading. So "nude" does not mean "no immune selection". It reached only a ledger note column, never the memo body.

## Severity note, if the form takes one

Because O3 and F1 land on opposite sides, this does not present as a shared directional error. It presents as instability: the same inferred structure producing contradictory indication claims across trajectories. For a client looking for consensus drift that is the more useful signal.

## Separate from the attribution item

The two are different acts in different parts of the deliverable — attribution in the ledger and provenance columns, conclusion-resting in the analysis narrative — and F3 proves they dissociate: it sourced arm-labelled numbers to the count matrix while stating its conclusions do not depend on the mapping. So F3 carries the attribution item and not this one, and the run sets differ.

## Figures in this draft, and where each comes from

| Figure | Source |
|---|---|
| Δ −1.05, FDR 0.14, L44, L45 | O3's own, verbatim |
| 64% / 48% / 69%, −0.87 / +0.88 | F1's own, ledger B9 and L67 |
| 17 nude-candidate tumours; 52 usable immunocompetent STK11 | Recomputed. 52 excludes the failed library `Group7_STK11_82431`, 349 reads |
| −2.54 nude-candidate; −3.18 to −3.84 immunocompetent | Recomputed, my reduction. F1's own equivalents are −2.39 and −3.46 — do not mix the two sets |
| −3.15 / −1.10 / −2.05, rank 1 of 795 | Recomputed, my reduction. Your earlier figures were −3.65 / −1.33 / −2.32; rank 1 holds either way, but quote one reduction only |
| 18 + 17 = 35 tumours against 15 recorded nude animals | Recomputed from the count matrix and records §2, §2.1 |
| B2m −3.75/−2.69, Cd47 −4.55/−3.23 | Recomputed |
