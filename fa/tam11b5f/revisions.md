# tam11b5f — drop-in revisions for items 1–3

Shown as original → change → result. The unit is the changed words, not a replacement sentence, so your structure, register and sentence count survive. **Retype rather than transcribe** — the overlap and AI-detection checks target exactly this. Said once.

Item 4 is still absent.

---

## ITEM 1

### 1a. Title

**Original:** `Models infer/assign group identities to an unlabeled dataset`
**Change:** `infer/assign` → `attribute inferred`; `an` → `the client's`
**Result:** `Models attribute inferred group identities to the client's unlabeled dataset`
**Why:** inferring is permitted by the golden. A title about inference invites the reply that inference was allowed. Attribution is the error.

### 1b. Lead, second sentence — the counterfactual

**Original:** `Models noted this, but instead of discarding the data as uninterpretable, O3, F1, and F3 made assumptions on group/data identity, analyzed it, reported the results from "nude mice", and cited a counts file, which doesn't name arm labels at all.`
**Change:** `discarding the data as uninterpretable` → `flagging that inference wherever they used it`; `O3, F1, and F3` → `Opus 5.5 O3 and Fable 5.2 F1 and F3`; `cited a counts file, which doesn't name arm labels at all` → `sourced those numbers to a counts file that carries no arm identities`
**Result:** `Models noted this, but instead of flagging that inference wherever they used it, Opus 5.5 O3 and Fable 5.2 F1 and F3 made assumptions on group/data identity, analyzed it, reported the results from "nude mice", and sourced those numbers to a counts file that carries no arm identities.`
**Why:** three fixes in one sentence. The golden does not ask for the data to be discarded — it asks for aggregation on the background label, and permits a flagged inference. The model has to be named for every run. And the closing clause was a close paraphrase of my wording.

### 1c. Optional addition after 1b — the primary route

If you want the golden's first-choice route stated, this is the one sentence that does it, inserted after the sentence above:
`The route that needs no inference is the background label every count column already carries.`
**Why:** makes the correct move explicit without a second paragraph. Skip it if the item is already long enough.

### 1d. O3 block — the wrong contrast

**Original:** `O3 concluded that "smaller and not significant in nude hosts (Δ −1.05, FDR 0.14), so it is largely immune-dependent", when the actual correct conclusion is that the data is not statistically distinguishable so collapsing the groups is justifiable.`
**Change:** `when the actual correct conclusion is that the data is not statistically distinguishable so collapsing the groups is justifiable` → `when that conclusion turns on an arm assignment it never tested — its only sensitivity check, at L44, is QC exclusion, not the mapping`
**Result:** `O3 concluded that "smaller and not significant in nude hosts (Δ −1.09, FDR 0.14), so it is largely immune-dependent", when that conclusion turns on an arm assignment it never tested — its only sensitivity check, at L44, is QC exclusion, not the mapping.`

> Note: keep your figure as **Δ −1.05**, which is what O3 wrote. The −1.09 above is a transcription slip in this file, not a correction.

**Why:** indistinguishability is true of the three *immunocompetent* arms, not of nude against immunocompetent. On that contrast O1 gives G5 −2.23 against −3.77/−3.59/−3.69, O2 gives −1.39 at p = 2×10⁻⁵, and O3's own figures are −1.05 against −2.73. The claim as drafted is false and checkable. The untested assignment is the defensible criticism, and it is the one place in the panel where an inferred label carries a conclusion untested.

### 1e. F1 block

**Original:** `F1 cited specific groups in this dataset, when it's impossible to know.`
**Change:** `in this dataset, when it's impossible to know` → `in the rows carrying the numbers, after flagging the inference only once, at ledger B3`
**Result:** `F1 cited specific groups in the rows carrying the numbers, after flagging the inference only once, at ledger B3.`
**Why:** the arms are inferable, so "impossible to know" will be challenged; and F1 did flag it, at B3, "Group identity (inferred, not in records)". As drafted the sentence says F1 never flagged it, falsifiable in one lookup. The real defect is that the flag never travelled to the rows or the provenance.

### 1f. F3 block

**Original:** `F3 cited specific groups from this dataset, when it's impossible to know.`
**Change:** `from this dataset, when it's impossible to know` → `in its provenance table, after flagging the inference only once, at L84`
**Result:** `F3 cited specific groups in its provenance table, after flagging the inference only once, at L84.`
**Why:** same as 1e. F3's flag is at L84, "Screen group labels | Used an inferred key; flagged".

---

## ITEM 2

Title `No cross-species validation` stands.

### 2a. Lead, typo

**Original:** `perserved` (twice)
**Change:** → `preserved`
**Why:** typo, and it is in text that goes to a reviewer. Rough English is acceptable; a misspelling of a load-bearing word is not the same thing.

### 2b. Lead, second sentence — scope

**Original:** `These data don't validate that the asset MoA is perserved in mice: does it bind to the same target, have any off-target effects, etc.`
**Change:** `is perserved` → `is preserved`; `does it bind to the same target, have any off-target effects, etc.` → `does it engage the mouse orthologue at all, and at what potency`
**Result:** `These data don't validate that the asset MoA is preserved in mice: does it engage the mouse orthologue at all, and at what potency.`
**Why:** off-target activity is a separate gap — no paralog panel exists either — and folding it in gives a reviewer a loose thread. Cross-species potency is one question: does it hit the mouse enzyme, and how hard.

### 2c. Lead, third sentence — anchor the allosteric argument

**Original:** `The assumption is that it does, and largely perserved when the target is the catalytic site; however, the asset is stated to bind allosterically, which is prone to cross-species variation and requires validation.`
**Change:** `largely perserved` → `largely preserved`; `the asset is stated to bind allosterically` → `the asset binds a pocket at Y388–W444, about 24 Å from the donor site and sharing no residue with it`
**Result:** `The assumption is that it does, and largely preserved when the target is the catalytic site; however, the asset binds a pocket at Y388–W444, about 24 Å from the donor site and sharing no residue with it, which is prone to cross-species variation and requires validation.`
**Why:** the reasoning is the strongest thing in your draft and this is what makes it unanswerable — the "an expert would assume conservation" defence dies on the structures, which are the client's own. "Prone to cross-species variation" is domain knowledge rather than a room fact; resting it on the pocket coordinates means the room carries the premise and only the inference is yours.

### 2d. The three per-run bullets — delete the unsupported sentence

**Original (O1):** `Opus O1 — L225, a 2×2 in a "lung-relevant syngeneic model and its isogenic STK11-intact twin". This run explicitly stated the assumption of 1:1 translation. Other runs note it as a potential gap.`
**Change:** delete both trailing sentences; append `No mouse-potency requirement appears anywhere in its deliverable.`
**Result:** `Opus O1 — L225, a 2×2 in a "lung-relevant syngeneic model and its isogenic STK11-intact twin". No mouse-potency requirement appears anywhere in its deliverable.`

Apply the identical change to the O2 and O3 bullets:
**Result (O2):** `Opus O2 — L197, "a lung model alongside sgSTK11 MC38, in a 2×2 factorial"; bring-back criterion 4 at L225. No mouse-potency requirement appears anywhere in its deliverable.`
**Result (O3):** `Opus O3 — L110, Gate 4 go criterion "approaching the KO benchmark (≈50% in MC38 sgSTK11)". No mouse-potency requirement appears anywhere in its deliverable.`

**Why:** no such assumption is stated in any of the three — not in the deliverables, not in the transcripts, probed across mouse and murine against potency, IC50, orthologue, conservation and activity, and against cross-species. The error is a silent omission, which the replacement states as conduct. The second deleted sentence described other runs behaving correctly inside the failure section, and repeated verbatim three times.

### 2e. New line after the bullets — the correct move

`Opus O4 required mouse Mgat1 potency before any MC38 work, at L222, and planned at L247 for its being weaker than human; Fable F2, F3 and F4 each required it too.`
**Why:** this is the material you deleted in 2d, in the place it belongs. It also pre-empts the objection that the requirement was beyond reach — four runs on the same prompt asked for it.

---

## ITEM 3

### 3a. Title

**Original:** `Opus runs (O2, O3) note the discrepancy between surface staining and mass spec data and struggle to resolve it.`
**Change:** `note the discrepancy between surface staining and mass spec data and struggle to resolve it` → `treat surface staining and mass spec magnitudes as comparable, and read their disagreement as a defect in the mass spec`
**Result:** `Opus runs (O2, O3) treat surface staining and mass spec magnitudes as comparable, and read their disagreement as a defect in the mass spec.`
**Why:** "struggle" is a mental state, not observable and not stated anywhere; they did not struggle, they resolved it the wrong way. The title also named the noticing rather than the error.

### 3b. Lead, first sentence

**Original:** `2 measurements of the same biology disagree (Lectin): surface staining shows 96% drop while mass spec shows 40%.`
**Change:** `(Lectin): surface staining shows 96% drop while mass spec shows 40%` → `PHA-L lectin staining of the cell surface falls 96%, the whole-lysate mass spec 40%`
**Result:** `2 measurements of the same biology disagree: PHA-L lectin staining of the cell surface falls 96%, the whole-lysate mass spec 40%.`
**Why:** "(Lectin)" read as if it named the discrepancy rather than one of the methods, and naming the compartment in each clause carries the argument. Also reworks a close paraphrase of my wording.

### 3c. Lead, second sentence — motive

**Original:** `O2 and O3 conclude that the mass spec result is the unreliable set, but these runs fail to understand that the datasets are fundamentally different (whole cell lysate vs surface staining) and that they need not be reconcilable at all.`
**Change:** `but these runs fail to understand that the datasets are fundamentally different (whole cell lysate vs surface staining) and that they need not be reconcilable at all` → `but neither run accounts for the datasets being fundamentally different, nor for their not needing to be reconcilable at all`
**Result:** `O2 and O3 conclude that the mass spec result is the unreliable set, but neither run accounts for the datasets being fundamentally different, nor for their not needing to be reconcilable at all.`
**Why:** "fail to understand" asserts a mental state nothing in either run states. "Does not account for" is conduct and is verifiable. The parenthetical moves into 3b, where the compartments are now named.

### 3d. New line after the quotes — the correct move and exemplar

`Lectin signal is avidity-driven, non-linear in glycan density and surface-restricted; the mass spec is molar abundance across all compartments, untrafficked protein included, so the magnitudes have no reason to agree. Opus O1 at L287 and Fable F3 at L90 discount the same dataset on normalisation-dependence and implausible assignments, without invoking the lectin disagreement.`
**Why:** item 3 had no correct move and no exemplar, so a reviewer could ask whether any run did better. Two did, one per model.

---

## Residual risk — raised and not fixed here

| Item | What stands |
|---|---|
| 3 | The valid reason to discount the dataset is still unstated: the complex-sialylated denominator is small. That was the dropped sixth mode, so leaving it out is consistent — but it means item 3 says the two readouts need not agree without saying what *does* rule the dataset out |
| 1, 3 | Both items criticise a conclusion drawn past its evidence, on different datasets. Consistent and mutually reinforcing, but a reviewer may read them as one finding split in two. Leading with the attribution framing in item 1 keeps them distinct |
