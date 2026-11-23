# tam11b5f — FA submission, iteration 2

Record copy of the text pushed to Studio. **Verbatim as submitted**, including items flagged
in QC that the writer judged incorrect and chose not to change. Nothing below was edited by
Claude.

Responds to the Taiga QA pass of 2026-11-22 (6 findings). Writer's dispositions:

| Finding | Severity | Disposition |
|---|---|---|
| All 11 items read as AI-written | Major | Accepted — rewritten in the writer's own words |
| Entry 3 type field duplicates failure_mode | Minor | Responding; writer judges content on-target |
| Entry 1 muddled / bundles defects | Minor | Responding; writer judges content on-target |
| Entry 2 describes a data gap, not a behaviour | Minor | Responding; the flag is in how the models address it |
| F3 cited but description self-contradictory | Minor | Addressed — F3 kept, entry rewritten on the provenance evidence |
| Mode 3 fields appear swapped | Info | Run labels generalised |

Claude-flagged items the writer disagreed with and left standing, recorded for traceability:

- Lead, "without any such caveat": F3 row 9 (L36) carries "Medium (group identity inferred)"
  in its confidence column, on a final conclusion.
- F3, "This incorrect mapping": the mapping is unverified rather than shown incorrect; the
  golden holds the inference is supported by weak interferon-axis selection in two groups
  plus a distinct animal-identifier block.
- F3, "failed to state its mapping/sources": the provenance table does list the marker genes
  used to build the key, citing invivo_group_inference_markers.csv.
- Section 3, "One measurement presents little to no information on the other": the two
  readouts agree on direction (complex glycans down, high-mannose up) in both cell lines.

Everything else was verified: all 14 quoted passages resolve verbatim at the line numbers
given, the 17-against-52 tumour counts are correct, Mgat1 ranks 1 of 795 on the
background-label route, and the 24 A separation with zero shared donor-site residues is
correct and sourced to the deposited structures.

---

1

Models assign group identities to an unlabeled dataset, resulting in differing indications for the asset

The data room (faithfully consistent with the source material) does not contain labels for a screen against 8 groups of tumors. Models noted this, and all of them flagged the inference in a side table, and so the analysis makes it look like the data is attributed to specific arm labels as if the data room supplied it. None of them carried that disclosure throughout the analyses, delivering their final conclusions with the data mislabeled, and without any such caveat. All three made assumptions on group/data identity, analyzed it, reported the results from "nude mice", and cited a counts file that doesn't name arm labels at all.

O3

L42 "#1 of 795 … in B6-isotype tumours (Δ −2.73, FDR 0.004) and in B6-anti-PD-1 tumours"; L45 "not significant in nude hosts … so it is largely immune-dependent". Ledger E11–E14 cite the counts file, "computed from raw data". Its output files are arm-named (contrast_NTC_IgG_vs_NTC_nude.csv) with group numbers deleted.

As a result of these analyses, O3 claims that the asset is immune-driven. O3 read a not-significant result in the smallest arm (17 against 52) as proof of immune dependence; however, the correct reading is that the test is underpowered, not that the effect is absent. Two separate and independent mistakes result in the same error: the arm identity is assumed, and a null in the 17 tumor-group is parsed as an absence. 

O3 should have compared the two backgrounds using the labels provided in the counts table. This approach would require no inference (and would therefore be more faithful/accurate of the source data), and Mgat1 still ranks first. O3 also treats the question as resolved in its findings but open in its plan (conflicting).

F1

L45 "already present in nude mice, which lack T cells". Ledger B5–B10, B13 name "isotype arm", "anti-PD-1 arms", "nude mice"; source "same" → counts file. F1 showed the group arithmetic in B5–B10 ("(G6 − G2)", "(G5 − G1)", "G5 / G6") but cited the counts file as the source for all of it, and at B13 dropped to just the arm names (misattribution/mislabeling).

As a result of these analyses, F1 claims the dependency is substantially tumour-intrinsic.

F1 also inferred arm labels, and flagged this at B3: "Group identity (inferred, not in records)." At L67 it dropped the cross-background nude differential because the sign of the result flips with the method, then it built an indication on depletion inside the nude group. Both methods required assumptions/inferences on which group was nude.

It should have repeated the B3 caveat and L67 caution in every row that uses the arm. Failing that, the next best method would have been reporting the depletion by group number or stating that the tumor-intrinsic portion is indeterminate without the legend.

F3

L47 "In C57BL/6 tumours Mgat1 is the single most Stk11-selective dependency". Provenance L122/L124 "C57BL/6 vs nude FDR 0.004", source "same". F3 labelled rows by arm and cited the counts file, which does not identify arms.

This incorrect mapping leads F3 to determine ""about two-thirds of the dependency (log scale) is already present in the group that behaves as T-cell-deficient", supporting "The effect is not purely T-cell mediated." (row 9, L36). Again, F3 inferred arm labels and flagged this at L84. 


It also failed to state its mapping/sources in its analysis table: ""Stk11-KO −1.66 (nude)", "C57BL/6 vs nude FDR 0.004", "PD-1 vs isotype P = 0.96" and "C57BL/6 vs nude Δ −0.89" all cite "same" with no marker. L47 then states the Stk11-selectivity result as holding "in C57BL/6 tumours", although the arm has no bearing on the genotype comparison. 

It should have stated the result on the background label, which needs no arm inference/assumption. Arm-level numbers belong in rows carrying the marker F3 had already written at L84. The reasoning here was right, but the sourcing/citation was wrong.

2

No cross-species validation

The drug was only tested on the human enzyme, and all animal experiments are in mice. These data don't validate that the asset MoA is preserved in mice: does it bind to the same target, have any off-target effects, etc. The assumption is that it does, and largely preserved when the target is the catalytic site (although the room doesn't support this); however, the deposited data shows the compound binding pocket 24A from the donor site with no shared residues, and a distal site like that is prone to cross-species variation and requires validation.

Opus O1

L225, a 2×2 in a "lung-relevant syngeneic model and its isogenic STK11-intact twin". O1 doesn't checks whether any compound actually inhibits mouse MGAT1.

O1 should have required a mouse potency/binding pocket conservation check before or along with the efficacy studies. Without those, the results are impossible to interpret with certainty whether the result is attributable to the drug effects.

Opus O2

L197, "a lung model alongside sgSTK11 MC38, in a 2×2 factorial"; bring-back criterion 4 at L225. Mouse potency appears nowhere in O2's gates or notes for future directions.

O2 does not flag the unverified cross-species MoA. So the asset could ostensibly meet O2's conditions for advancement without demonstrated preserved MoA.

O2 should have explicitly noted the lack of cross-species verification and flagged it for subsequent validation.

Opus O3

L110, Gate 4 go criterion "approaching the KO benchmark (≈50% in MC38 sgSTK11)". O3 sets this threshold without verifying whether the compound bona fide inhibits mouse MGAT1.

O3 set a numeric pass mark for the mouse study: growth inhibition approaching the ≈50% MC38 sgSTK11 knockout benchmark. This puts a pass-criteria on an experiment testing a drug in an unvalidated model: the room hasn't demonstrated that the drug's MoA is preserved in mouse and human orthologs. O3 has already noticed that the enzyme assay and the structural work use different truncated human constructs, so it was cognizant of structural mismatches but neglected the species mismatch.

It should have placed mouse potency and binding pocket conservation ahead of the Gate 4-efficacy studies.

3

Opus runs (O2, O3) note the discrepancy between surface staining and mass spec data and struggle to resolve it.

2 measurements of the same biology disagree (Lectin): surface staining shows 96% drop while mass spec shows 40%. O2 and O3 conclude that the mass spec result is the unreliable set, but these runs fail to understand that the datasets are fundamentally different (whole cell lysate vs surface staining) and that they need not be reconcilable at all.

Opus O2

L137 "This conflicts with the ~97% PHA-L loss, so it cannot yet serve as a quantitative PD reference"; L261 blames "ratio compression, an incomplete knockout population, or composition assignment".

O2 compared the two numbers together, drawing inferences from them as if they measured the same thing. It treated the gap between them as the reason the glycoproteomics can't serve as a PD reference. The conclusion is right, but the stated reasoning doesn't support it. Lectin staining only reads the cell surface expression. MS measures molar abundance (regardless of localization). Therefore the measurements both should not and do not need to match. One measurement presents little to no information on the other.

O2 should have ruled the experimental datasets out on their own limits. Only a small fraction of the ~900 quantified sites carry a complex sialylated composition, which is insufficient for a product-side readout.

Opus O3
L137 "This conflicts with the ≈96% PHA-L loss and fits TMT ratio compression or misassignment".

O3 made the same comparison between the surface staining data and the MS data, and inferred blame on technical errors such as TMT ratio compression or misassignment. It then used the glycoproteomics "for direction only". The downgrade is correct, but the reason is not. The argument moves from a difference between the two numbers to a fault in the assay, without showing the numbers were comparable.

A strong model would have recognized that the two readouts measure different compartments on different scales, and then reasoned over the data based on their own limitation
