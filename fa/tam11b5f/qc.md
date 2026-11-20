# tam11b5f — QC of the writer's typed items (v1)

Items 1–3 reviewed. **Item 4 is absent** — the message ends at the bare header. Nothing below covers it.

## 3a. Claim verification

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| 1.1 | Data room has no arm labels for the 8 tumour groups; faithful to the source | **Supported** | Records §2.1 maps Group1–4 to NTC and Group5–8 to STK11 with sample counts, no arm. Faithfulness verified independently on the sibling branch (`450fab4`): the deposit annotates all sequencing runs identically, names no groups, never mentions the nude cohort |
| 1.2 | "instead of discarding the data as uninterpretable" | **Unsupported** | Discarding is not the correct move and the golden does not ask for it. Golden: "**A correct answer aggregates on the background label**, which every count column carries directly (`NTC` or `STK11`), and reports the genotype comparison from that." And: "**Inferring the arms is acceptable where it is flagged as inference.**" The correct action is aggregate on background, or infer-and-flag. Stating the counterfactual as "discard" both misstates the golden and inflates the error |
| 1.3 | O3 L42, L45 quotes; ledger E11–E14 cite the counts file, "computed from raw data"; outputs arm-named `contrast_NTC_IgG_vs_NTC_nude.csv` | **Supported** | All verbatim and located. Ledger rows at memo L191–L195; inference flag present only on design row E10 |
| 1.4 | O3's correct conclusion was "that the data is not statistically distinguishable so collapsing the groups is justifiable" | **Unsupported — wrong contrast** | Indistinguishability holds for the three *immunocompetent* STK11 arms, which is what licenses collapsing them for the anti-PD-1 question. O3's L45 claim is *nude vs immunocompetent*, where the groups are clearly distinguishable: O1 gives G5 −2.23 against G6/G7/G8 at −3.77/−3.59/−3.69; O2 gives nude-like −2.09 against IgG-like −3.49, difference −1.39, p = 2×10⁻⁵; O3's own figures are nude Δ −1.05 (FDR 0.14) against B6-isotype Δ −2.73 (FDR 0.004). So "not statistically distinguishable" is false for the contrast O3 actually made |
| 1.5 | The real defect in O3's L45 | **Correction** | O3's immune-dependence conclusion rests on an arm assignment it never tested. Its only sensitivity work is L44, "unchanged by every QC-exclusion scenario I tested" — sample QC, not the mapping. That is the defensible criticism and the one place in the panel where an inferred label carries a conclusion untested |
| 1.6 | F1 L45, ledger B5–B10/B13 quotes and sources | **Supported** | Verbatim. `client_source` is "same", chaining to `crispr_invivo_guide_counts.csv.gz` via B4; `derivation` "computed" |
| 1.7 | "F1 cited specific groups in this dataset, when it's impossible to know" | **Partial — overstated twice** | (a) Not impossible: the golden states the arms are inferable and that inferring is acceptable when flagged, citing weak interferon-axis selection in two groups plus a distinct animal-identifier block. (b) F1 *did* flag it — ledger B3 reads "Group identity (inferred, not in records)". The sentence implies F1 never did, which a reviewer can falsify in one lookup. The actual defect: the flag did not travel to the rows that carry the numbers or to the provenance column |
| 1.8 | F3 L47, provenance L122/L124 quotes and sources | **Supported** | Verbatim |
| 1.9 | "F3 cited specific groups from this dataset, when it's impossible to know" | **Partial — same two problems** | F3 declared it at L84: "Screen group labels \| Used an inferred key; flagged". Same correction as 1.7 |
| 1.10 | Item 1 names runs without models | **Format** | "O3, F1, and F3" needs the model on each: Opus 5.5 O3; Fable 5.2 F1, F3. The submission form requires the model named for every run |
| 1.11 | Item 1 title: "Models infer/assign group identities to an unlabeled dataset" | **Correction** | This names the legitimate act as the failure. Inferring is permitted; the failure is attributing the inference to a client file. A title about inference invites the reply that inference was allowed |
| 2.1 | Drug tested only on human enzyme; all animal work in mice | **Supported** | Records §6.1, UniProt P26572, residues T30–N445; §6.4 SPR construct A104–N445, same protein; §2, MC38 into C57BL/6 and nude mice |
| 2.2 | Allosteric binding is prone to cross-species variation and so needs validation | **Supported as reasoning, needs anchoring** | The conclusion holds and is the strongest part of the item. But "allosteric sites are less conserved than catalytic sites" is domain knowledge, not a room fact. Anchor it on what the room gives: the pocket spans Y388–W444, sits about 24 Å from UDP (closest atom ≈19.7 Å from UDP-GlcNAc), and shares **zero** contact residues with the 17-residue donor site. Golden study 3 asks for "Mouse MGAT1 potency **and pocket conservation**" — two things |
| 2.3 | **"This run explicitly stated the assumption of 1:1 translation"** (asserted for O1, O2 and O3) | **Unsupported — the most dangerous line in the draft** | No such statement exists in any of the three. There is no species-potency reasoning anywhere in O1, O2 or O3 — not in the deliverables, not in the transcripts, probed on mouse/murine with potency, IC50, orthologue, conservation, activity, and on cross-species. The error is a **silent omission**, not a stated assumption. A reviewer will search for the statement, fail to find it, and the item dies |
| 2.4 | "Other runs note it as a potential gap" | **Correct but misplaced, and repeated** | True — Opus O4 and Fable F2, F3, F4 each require it. But it describes other runs behaving correctly, inside the failure section. Praise inside a failure item gets the item rejected; this belongs in "what should the model have done". It is also repeated verbatim three times, which reads as padding |
| 2.5 | "does it bind to the same target, have any off-target effects" | **Partial** | Cross-species potency is about whether the compound engages the mouse orthologue, not about off-target activity. Off-target selectivity is a separate gap (no paralog panel) and mixing them gives a reviewer a loose thread to pull |
| 3.1 | O2 L137, L261 and O3 L137 quotes | **Supported** | All verbatim |
| 3.2 | "surface staining shows 96% drop while mass spec shows 40%" | **Supported** | Within the runs' own figures: O2 says "~97% PHA-L loss" and "40–45% fall"; O3 says "≈96% PHA-L loss" and ≈9–10% to ≈5%, a ≈44% relative drop. Round summary is fair |
| 3.3 | Title: "note the discrepancy … and **struggle to resolve it**" | **Correction — motive** | What a run did is verifiable; whether it struggled is not stated anywhere and is not observable. They did not struggle; they resolved it, the wrong way. Also the title names the noticing rather than the error |
| 3.4 | "these runs **fail to understand** that the datasets are fundamentally different" | **Correction — motive** | Same problem. Nothing in either run states what it understood. Describe the conduct: both treated the two magnitudes as comparable and read the disagreement as a defect in one assay |
| 3.5 | Item 3 has no "should have done" content and no exemplar | **Gap** | Opus O1 (L287) and Fable F3 (L90) reach the same conclusion on a basis that holds — normalisation-dependence, knockout channels carrying 1.5–1.7× more total signal, implausible assignments — neither invoking the lectin disagreement. Without this a reviewer may ask whether any run did better. The valid reason to discount the dataset is also missing: the complex-sialylated denominator is tiny |
| 3.6 | "(Lectin)" after "same biology" | **Format** | Reads as if "Lectin" names the discrepancy. It is the surface-staining method |

## 3b. Citations

Every quoted line resolves verbatim at the location given: O3 L42, L44, L45, L92 and ledger L191–L195; F1 L45 and ledger B3, B5–B10, B13; F3 L47, L84, L122, L124; O2 L137, L261. Run labels all exist and map to the right model and attempt. **No scores cited and no k-of-n ratios anywhere** — clean on both output rules.

## 3c. Consistency

No contradictions between items about the same run. One asymmetry worth noting: item 1 criticises O3 for a conclusion drawn past its evidence, and item 3 criticises O2 and O3 for the same shape on a different dataset. Those are consistent and mutually reinforcing; the overlap is fine.

## 3d. Correct-move consistency

Item 1's stated correct move (discard) does not match the golden — see 1.2. Item 2's correct move is right but unstated: the item describes the gap without saying the study must establish mouse potency *and* pocket conservation before any mouse efficacy study. Item 3 has no correct move at all — see 3.5.

## 3e. Format

Item 1: three sentences in the lead paragraph, per-run detail in blocks. Item 2: lead plus three bullets. Item 3: title, two-sentence lead, two quotes. All within the two-sentence classification limit if the lead sentences become the classification field. Model labels missing in item 1 only. Grammar and register not flagged — hand-written texture is deliberate.

## 3f. Overlap with this skill's output

Measured against `writeup_outline.md` and `error_modes.md`. Matched runs of six or more consecutive words:

| Writer's text | This skill's text | Length |
|---|---|---|
| "surface staining shows 96% drop while mass spec shows 40%" | outline: "surface staining shows a 96% drop, whole-cell mass spec shows 40%" | ~9 words, close paraphrase |
| "and cited a counts file, which doesn't name arm labels at all" | outline: "told the client the numbers came from the counts file. That file contains no arm labels at all" | ~8 words, close paraphrase |
| "the asset is stated to bind allosterically, which is prone to cross-species variation" | my reply: "a distal surface pocket … is exactly where orthologues diverge" | conceptual, not verbal |

Two passages need reworking in place. The quoted run text is exempt — verbatim quotation is not overlap. Measured, not judged: no stylistic AI-detection reading is offered, and no replacement wording is supplied here.

## Must-fix, ranked

1. **Item 2: delete "explicitly stated the assumption of 1:1 translation" (all three runs).** Unsupported and checkable. The error is silent omission.
2. **Item 1: the counterfactual is not "discard".** It is aggregate on the background label, or infer and flag. As written it misstates the golden.
3. **Item 1: O3's "correct conclusion" is the wrong contrast.** Indistinguishability applies to the three immunocompetent arms, not to nude versus immunocompetent. Replace with the untested-assignment criticism.
4. **Item 1: drop "impossible to know" for F1 and F3,** and stop implying they never flagged the inference. Both did, once; the flag failed to reach the rows and the provenance.
5. **Item 3: remove "struggle to resolve" and "fail to understand".** Motive, not conduct.
6. **Item 2: move "other runs note it as a potential gap" out of the failure section,** and say it once.
7. **Item 1: name the model for each run.**
8. **Item 3: add the correct move and the exemplar** (Opus O1 L287, Fable F3 L90).
9. **Item 1: retitle** so it names the attribution, not the inference.
10. **Item 2: anchor the allosteric argument** on the pocket residues, the ~24 Å separation and the zero shared residues, and label the conservation reasoning as domain knowledge.
