# MGAT1 programme assessment — pilot package

Category: program decisions (writer's classification).
Phase 1, lead optimisation and candidate selection. Decision shape: go/no-go on an asset.

RLS short ID: tam11b5f
RLS URL: https://studio.mercor.com/annotator/tasks/task_e55870a045744a9e932736ae7ca1822f/?campaignId=camp_0589d1e96758477586df0e43dd8eeec1

| File | What it is |
|---|---|
| `prompt.txt` | The prompt as actually run, verbatim including typos |
| `grader.txt` | Internal reference only. Studio offered no grader field for this task, so this was not submitted. Retained because it makes the predicted modes visible in transcripts and is the fastest lookup during the FA |
| `golden_response.md` | Goes to Reviewer Facing Golden Response |
| `failure_modes.md` | Pre-registered modes plus pre-pilot validation evidence |
| `../room/` | The data room — mount all of it |

## Data room contents

Screens: `crispr_invivo_guide_counts.csv.gz` (3,580 guides x 159 samples, 141 per-animal
tumours), `crispr_invivo_ngs_demux.csv.gz`, `coculture_screen_umi_counts.csv.gz` (7.96M UMI
rows). Glycoproteomics: `glycoproteomics_site_quant.xlsx` (three sheets, raw intensity
channels only). Compounds: `compound_properties.csv`, `spr_binding.csv`,
`spr_competition.csv`, `dsf_thermal_shift.csv`. Figures: `assay_figures.pdf` (5 pp.),
`phenotype_figures.pdf` (11 pp.). Methods: `experimental_records.pdf` (6 pp.).
Structures: `structures/` (five mmCIF files).

## Build provenance

Source publication is not mounted and is not in this repository. Author-computed ratio,
p-value and normalised-intensity columns were removed from the glycoproteomics, along with
the summary sheet carrying the differential analysis. Structure metadata categories, entry
identifiers, ligand code, collection dates and beamline identifiers were stripped. Figure
panels were relabelled, with significance annotations and two interpretive in-plot phrases
removed; added ink across all sixteen panels is zero pixels. Compound codes, sponsor and
accessions are renamed throughout per `../build/rename_map.csv`.

Seven source inconsistencies are reproduced unremarked, by design: two differing values for
the same dissociation constant in two places, two differing antibody dose levels, stated
cohort sizes against observed sample counts, a stated top assay concentration against the
plotted series, a 1,000-fold unit inconsistency, and a reaction volume that does not close.

## Audit status

Seven independent audits. Six passed. The companion document failed on first pass
(two mis-transcribed guide sequences, a wrong reagent volume, a misattributed clone
provenance, and an unsourced claim) and was corrected and re-verified. Groundability passes
across all twenty golden claims. Three pre-pilot solver attempts confirm the ceiling.
