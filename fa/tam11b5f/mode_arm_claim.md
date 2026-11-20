# Candidate mode: `arm-claim-unlicensed`

Prepped in the outline's block format. **Distinct from `arm-labels-unsourced`** — that one is attribution (presenting the inference as sourced to a client file; O3, F1, F3). This one is resting an indication-level conclusion on the inference (O3, F1). The golden names both failures in the same sentence, separated by "or", so the split is the golden's own.

---

# `arm-claim-unlicensed` — SHIP

**Opus 5.5 O3 · Fable 5.2 F1** — one per model

**One breath:** nobody knows which of the eight tumour groups were the T-cell-deficient mice. Two runs each decided, then used that decision to answer what the asset *is* — and reached opposite answers. O3 concluded the dependency is largely immune-driven; F1 concluded it is substantially tumour-intrinsic. Both read the same file correctly. Neither conclusion was licensed.

| Field | Facts |
|---|---|
| **Classification** | High-level: reasoning failure, a conclusion drawn past what the data licenses. Specific: an indication-level claim about the asset's mechanism rested on an inferred arm identity that the files do not supply and the stated animal counts do not reconcile with |
| **Affected** | **What the asset is.** The programme is positioned as an immune-escape play in STK11-mutant NSCLC. If O3 is right the positioning is supported and every decisive study must be immunocompetent with nude and CD8-depleted controls. If F1 is right the positioning runs ahead of the data, the mechanism may be substantially tumour-intrinsic, and a different set of experiments becomes decisive. That is a difference in indication, in which models the client funds, and in which readouts count |
| **Runs** | Opus 5.5 O3; Fable 5.2 F1 |
| **Wrong — O3** | Converts an underpowered null into a positive claim. L45: "smaller and not significant in nude hosts (Δ −1.05, FDR 0.14), so it is largely immune-dependent". FDR 0.14 in the smallest arm is absence of evidence. The nude-candidate group carries 17 tumours against 52 usable across the three immunocompetent STK11 arms, so lower power is expected before any biology enters. Its only sensitivity check, at L44, is QC exclusion, not the mapping. And the quantity it does not foreground is the absolute one: Mgat1 depletion in the nude-candidate STK11 arm recomputes to −2.54, a strong dependency by any standard. The conclusion rests on a shrinking differential while the underlying effect stays large |
| **Wrong — F1** | L45: "about half to two-thirds of the Mgat1 depletion is already present in nude mice, which lack T cells", carried into a section heading. An indication-level claim on the same inferred identity. F1 is the more guarded of the two: it set the most method-sensitive comparison aside explicitly at L67 — "Its sign depends on the method (−0.87 or +0.88), so I treat it as no evidence either way" — so its defect is narrower, the absolute-depletion framing rather than the cross-background differential |
| **Why neither claim was licensed** | Three independent problems, each sufficient. (1) **The arm labels are inferred.** No file names an arm. Both runs flagged this, but flagging an inference does not license resting a conclusion on it, and the golden draws exactly that line. (2) **The inferred arms do not reconcile with the stated animals.** Both runs noticed the mismatch — O3: "The matrix holds 141 tumour libraries (71 NTC, 70 STK11), but the records describe 30 C57BL/6 + 15 nude mice"; F1 ledger E1: "records: C57BL/6 n = 30, nude n = 15; file: 141 tumour samples in 8 undecoded groups" — and neither followed it through. The inference assigns Group 1 (18 tumours) and Group 5 (17) to nude: **35 tumours against 15 recorded nude animals.** Whatever reconciles that gap, the nude "arm" is not a clean 15-animal group, so a non-significant result inside it cannot carry an indication-level conclusion. (3) **The golden's route avoids all of it.** Aggregate on the background label every count column carries and the target-validation claim needs no inference at all: recomputed, Mgat1 sits at −3.15 in the STK11 background against −1.10 in NTC, differential −2.05, **rank 1 of 795** |
| **Mechanism of the divergence** | The two runs measure different estimands and both are internally valid. O3 measures the **differential** — how much more MGAT1 matters in STK11-null than STK11-intact tumours, per arm — and that quantity shrinks in the nude-candidate arm. F1 measures **absolute depletion** inside the STK11-null background, and that quantity stays large there (−2.54 against −3.18 to −3.84 in the immunocompetent arms; F1's own ledger B9 gives the share as 64%, 48% and 69% by three methods). Both facts are true at once: the dependency is strong without T cells and amplified by them. O3's framing yields "largely immune-dependent", F1's yields "substantially T-cell-independent", and nothing in the data adjudicates, because the choice of estimand is the answer |
| **Should have** | Reported the target-validation claim on the background label, which needs no inference, and left the immune-dependence question to a study rather than to the screen. Golden: "**A correct answer aggregates on the background label** ... No conclusion in this assessment requires the arm identities", and "**Inferring the arms is acceptable where it is flagged as inference** ... **What is not correct** is presenting an inferred mapping as though the files supplied it, or resting the anti-PD-1 interaction claim on the screen when the screen cannot address it as delivered" |
| **Exemplar** | Three runs quarantined the mapping from their conclusions, independently, so the correct treatment was available in the same data. Fable 5.2 **F3**, L84: "The 'no PD-1 effect' conclusion does not depend on which C57BL/6 group is which — all three are identical for Mgat1". Fable 5.2 **F4**, L182: "The Stk11-selectivity result does not depend on it. The T-cell and PD-1 statements do; hence Gate 0." Opus 5.5 **O4**, Appendix C heading at L327: "Tentative screen-group mapping (for the client to confirm; **not used for any primary conclusion**)" |
| **Severity note** | Because O3 and F1 land on opposite sides, this does not present as a shared directional error. It presents as **instability**: the same inferred structure producing contradictory indication claims across trajectories. For a client looking for consensus drift that is the more useful signal, and it is worth saying so in the item |
| **Credit, not for the failure section** | F1 made an observation no other run and not the golden made: nude mice retain innate immunity, evidenced from the screen itself. Its ledger B9 note reads "nude mice keep innate immunity: B2m-knockout -2.3 and Cd47-knockout -2.6/-3.0 in G1/G5". I recompute B2m at −3.75/−2.69 and Cd47 at −4.55/−3.23 in Groups 1 and 5 — deeper than F1's figures, same reading. So "nude" does not mean "no immune selection", which complicates both readings. **This belongs in the should-have field, not the failure field**, and note that it reached only a ledger note column, never the memo body |

---

## One objection to the draft argument — fix before typing

The draft says the mode is **"not defensible by a careful expert — because the disagreement between O3 and F1 is itself the proof that the inference cannot support the weight."**

That inference does not hold, and it is the sentence a reviewer will pull.

By the draft's own diagnosis the divergence is driven by **estimand choice**, not by the mapping. Both runs used the *same* mapping: Groups 1 and 5 as nude. Hand them a verified arm key tomorrow and they would still disagree, because the differential shrinks in the nude arm while the absolute depletion stays large — that is a property of the data, not of the labelling. So the disagreement proves the **positioning question is underdetermined by the estimand choice**. It does not prove the arm inference cannot bear weight.

The mode survives without that step, on evidence that is independently strong and verified: the golden draws the line; the mapping is unverified; 35 tumours are assigned to 15 recorded animals; three runs quarantined it. Use the estimand analysis as the **mechanism** that explains why neither claim was licensed, not as the proof.

## A second candidate hiding inside this one

The estimand finding stands on its own and is the more novel science: **neither run disclosed that its positioning claim turns on a choice of estimand, and the two estimands give opposite answers from identical data.** It is method-based, confirmable, and appears in neither the golden nor the pre-registered mode set.

Its requirement basis is weaker — no prompt line asks a responder to declare an estimand — so it is closer to the territory where a careful expert defends either choice. Two framings, writer's call:

- **Ship `arm-claim-unlicensed`** as above, estimand analysis inside it as mechanism. Stronger basis, golden-licensed.
- **Ship the estimand mode instead**, arm inference as context. Sharper science, weaker basis.

Shipping both as separate items is not advisable: they cite the same two runs on the same passage.

## Overlap with `arm-labels-unsourced`

O3 and F1 appear in both modes. The acts are different — attribution versus resting a conclusion — and the counterfactuals differ, but a reviewer may read them as one finding split in two. Two ways to handle it:

1. **Re-cut the boundary (recommended).** `arm-labels-unsourced` becomes attribution, whose clearest case is F3 — which quarantined its conclusions but still sourced arm-labelled numbers to the count matrix. `arm-claim-unlicensed` takes O3 and F1. The escalation then reads as deliberate.
2. **Merge into one item with two tiers**, severity rising from attribution to conclusion. One item, loses the one-per-model pattern on the attribution tier.

## Numbers to correct before typing

| Draft figure | Correction |
|---|---|
| "17 tumours against 53 across the three immunocompetent STK11 arms" | **52** usable. 53 counts the failed library `Group7_STK11_82431`, 349 reads, which every run excluded |
| "Mgat1 at −3.65 in the STK11 background against −1.33 in NTC, differential −2.32" | Reduction-dependent. My reduction gives −3.15, −1.10 and −2.05. **Rank 1 of 795 holds either way.** Quote your own reduction's figures, not both |
| "F1's 'half to two-thirds' sits against my 72%" | F1's own ledger B9 gives 64%, 48% and 69% by three methods. Cite F1's range when the claim is about F1; keep 72% as your independent check |
| "nude STK11 arm −2.39 against a B6 STK11 mean of −3.30" | −2.39 and −3.46 are F1's own figures from B9. My reduction gives −2.54 against −3.18 to −3.84. Same reading; keep the two sets separate |
| O3's "Δ −1.05" and NTC contrasts "+0.38 and +1.25" | Verified as O3's own. My independent G5−G1 is **−0.99**, and the NTC-background contrasts differ with reference choice as the draft says. Nothing miscalculated in either run — worth stating, because it rules out a computation mode |
