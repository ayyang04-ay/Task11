# Reviewer-facing golden response

**Advance, but not into IND-enabling work.** Fund a defined cell-and-mechanism bridge package. The target is validated and catalytically dependent, the chemical matter is real and structurally enabled, and nothing in the package connects the two: no compound has been tested in any cell.

---

## 1. Target validation is strong, and the phenotype depends on catalysis

**In vivo pooled screen.** `crispr_invivo_guide_counts.csv.gz`: 3,580 guides (795 genes x 4, plus 400 non-targeting), 141 per-animal tumours across two sgRNA backgrounds. Reduction: counts per million per sample, log2 against the pooled plasmid samples, centred on the 400 control guides, averaged within background.

- Genotype differential **2.28 log2** (control-guide centred), **2.22** (median-of-all-guides centred), **1.43** with no centring at all.
- The *conclusion* that MGAT1 depletes more in the STK11 background is stable to the choice of centring. The *magnitude* is not stable to omitting centring, and an answer that reports a selectivity figure without saying which correction produced it has not established it.

**Co-culture screen.** `coculture_screen_umi_counts.csv.gz`: 7,960,054 UMI rows, 77,079 guides, 19,373 genes, two unreplicated conditions. MGAT1 ranks **30 of 19,358** by summed UMI counts and **65** by distinct-UMI counting; Spearman between the two estimators is **0.53**, with 110 of 200 top genes shared. Cite the result as top-0.5% rather than as a position.

**Catalytic dependence** (`phenotype_figures.pdf`). Wild-type cDNA restores surface PHA-L to ~5.4e6 against ~6.7e6 parental; D289A and D211A+D289A stay at baseline. With T cells, relative viability is 0.70/0.68 (vector), **1.15/1.13 (wild-type)**, 0.53/0.56 (D289A), 0.48/0.52 (double mutant), across two donors. In vivo the same pair separates only when endogenous enzyme is removed.

This is the leg that makes a small molecule the right modality: the tumour needs catalytic turnover, not the protein.

## 2. The chemical matter is real

`compound_properties.csv`, `assay_figures.pdf`, `structures/`.

- **197 uM to 0.043 uM, 4,581-fold** (ANT-0592 to ANT-4267).
- **LipE 4.77** (ANT-4267) and **3.89** (ANT-3744), computed as pIC50 minus logD. Potency is being bought with binding, not lipophilicity.
- Five structures at 1.55-2.01 A. Computed from the deposited coordinates: the inhibitor sits **23.93 A** from UDP in chain A (24.23 A in chain B), in a 16-residue pocket spanning Y388-W444 that shares **zero** contact residues with the 17-residue UDP site. D211, mutated in the rescue experiments, is in the UDP site and nowhere near the inhibitor.
- Non-competitive binding is established by the **additive thermal shifts** (+2, +6, +8 C) and by the ternary structure with both ligands bound, not by the competition dissociation constants.

**Do not read the competition shifts as cooperativity.** The 32 to 20 uM and 0.4 to 0.2 uM shifts are two-fold across experiments the records state were run on freshly prepared surfaces at differing immobilisation levels (~9000, ~3600, ~3500 RU). That is within run-to-run variation. Calling it positive cooperativity asserts a thermodynamic result the data cannot carry.

**The two acquired compounds are not chemical matter.** ANT-1938 reaches 40% inhibition with a fitted potency of >100 uM; ANT-2214 reaches 60% with 74 uM. Both show flat, non-dose-dependent surface plasmon resonance against a UDP reference that titrates cleanly to 31 uM on the same assay. A fitted potency for a compound that never approaches full inhibition is not a potency.

## 3. The gating gap

No compound in this package has been applied to a cell. No cellular potency, no compound-treated lectin shift, no compound co-culture killing, no pharmacokinetics, no in vivo compound study. Every biological result is genetic; every chemical result is cell-free. The therapeutic hypothesis lives entirely in that gap.

## 4. The pharmacodynamic readout the programme needs does not yet exist

`glycoproteomics_site_quant.xlsx`, Site_quant, raw intensity channels.

- **245 of 909** analysable sites move more than two-fold up in the knockout (**27.0%**); **6** move down (**0.7%**).
- Of sites with an unambiguous single composition, **317** are high-mannose and **16** are complex-sialylated.
- Total intensity: knockout **1.5231e10** against control **9.3026e9**, a factor of **1.64**, with protein input equalised before labelling.

**Do not channel-normalise.** A uniform loading difference scales every species equally and would place all ratios near 0.611; the unchanged bulk centres at **0.893**, and 245 sites move hard while 658 do not. A class-specific shift cannot be a loading artefact. Normalising to equal total shrinks the real accumulation and manufactures a ~1.7-fold product depletion that is not in the data.

**The lectin and mass-spectrometry readouts are not commensurable.** Lectin signal is avidity-driven, non-linear in glycan density and surface-restricted; the mass spectrometry is molar glycopeptide abundance across all compartments including untrafficked protein. Their magnitudes have no reason to agree, and the disagreement is not evidence that either is wrong. What rules the dataset out as a product-side reference is that 16 complex sites were quantified, not that it disagrees with flow cytometry.

## 5. Safety is unassessed, but not unknowable

*Named domain knowledge, not from the package.* Germline MGAT1 loss is embryonic lethal in mice while MGAT1-null cells are viable, so cell-autonomous essentiality is not the issue. Adult cardiomyocyte-specific deletion produces dilated cardiomyopathy and shortened lifespan through ion-channel glycosylation. Reduced N-glycan branching drives T-cell hyperactivity and autoimmunity, and hypomorphic MGAT1 variants carry human multiple sclerosis risk - mechanistically the same biology as the intended effect. Complex N-glycans are required cell-autonomously to form bronchial epithelium, which is directly relevant to a lung indication.

Position: a characterisable risk rather than a blocker, with cardiac safety pharmacology first and an autoimmunity read that cannot be separated from the intended pharmacology. An answer that reports only that no toxicology data exist has not taken a position.

---

## Next studies, and what each is compared against

| # | Study | Must establish | Compared against |
|---|---|---|---|
| 1 | Cellular target engagement | That inhibition reaches the enzyme in cells | The knockout lectin window as ceiling (PHA-L to 0.03-0.04, GNA to 8.2x), vehicle as floor, and the compound's own biochemical potency |
| 2 | Cellular potency for the nominated lead | Whether the surrogate-acceptor ranking transfers | The biochemical potency |
| 3 | **Cross-species potency** | Mouse MGAT1 potency and pocket conservation | Human potency. **Required before any mouse efficacy study**: every compound measurement is against human enzyme and every in vivo model is mouse |
| 4 | Mechanism of inhibition | Ki, modality against both substrates, and maximum achievable inhibition | The knockout's near-complete surface loss. A partial inhibitor may not phenocopy a null |
| 5 | Selectivity | Paralog and pathway selectivity | Lead potency, with attention to the nucleotide-sugar nodes that score alongside MGAT1 in the client's own screen |
| 6 | Mechanism confirmation on the lead | That the nominated lead engages the same pocket | The analogue that carries the existing structural and biophysical package |
| 7 | Cardiac safety pharmacology | Whether on-target cardiac risk is manageable | The known on-target phenotype |

Studies 1 and 4 are the kill gates. Nothing beyond them is worth funding until they read out.

---

## What was looked at and set aside

- **`Group7_STK11_82431`**, 349 total reads against a 2.46M median: a failed library, excluded before any normalisation.
- **Row P23193**, all eight A375 channels exactly zero. Present identically in the source, and the reason the analysable site count is 909 rather than 910.
- **Non-secretory proteins in the glycoproteomics** (HNRNPA1L3, SP9, PHOX2B, TUBB) carrying N-glycans with flat ratios: likely misassignments, excluded from class statistics.
- **Group-to-arm mapping**: the records give group, background and n, but no treatment arm. The mapping is not recoverable from the files and no pillar depends on it, so the backgrounds were aggregated.
- **Stated cohort sizes** of 30 and 15 against 141 observed tumour samples: noted, proceeded on observed counts.
- **Distinct-UMI estimator**: tested and set aside. It ranks core-essential genes among the top sensitisers at a 24-hour timepoint, which is a tell.
- **Potency protocol inconsistency**: the records specify a 100 uM top concentration, five of six dose-response panels run to 1000 uM, and ANT-0592's 197 uM potency cannot be determined from a series topping at 100 uM. Reported, not reconciled.

**Named domain knowledge used**: MGAT1's enzymatic reaction and glycan compositional nomenclature; lectin binding specificities; the mouse and human genetic safety literature; identity of core-essential genes. Everything else derives from the mounted files.
