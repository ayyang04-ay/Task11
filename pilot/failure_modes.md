# Pre-registered failure modes and validation evidence

Carry this table into the FA session. Checking predicted modes against transcripts is the
fastest route to the write-ups. **Naming what counts as a failure mode is the writer's call,
not Claude's** — what follows is a hypothesis set and a count, nothing more.

Panel: two models x eight attempts = sixteen trajectories.

## Validation evidence

Three independent attempts were run against the shipped prompt and room before pilot.
**Caveat that matters: these were subagent fan-outs from one parent session, which the
guidance says is not a substitute for independent attempts.** Treat the rates below as
indicative of direction, not as prevalence estimates.

All three reached a verdict close to the golden (do not commit to IND-enabling work; fund a
bridge package). The ceiling is met. The modes below are what they got wrong on the way.

## Observed, ranked by rate

| Short name | What was not checked, measured or corrected for | Rate | Bears on |
|---|---|---|---|
| `lectin-ms-commensurable` | Treated a surface lectin signal ratio and a whole-lysate glycopeptide intensity ratio as directly comparable magnitudes, and read their disagreement as evidence one assay is defective. The readouts differ in compartment, in linearity and in what they measure | 3 of 3 | Right conclusion, invalid basis |
| `spr-cooperativity` | Did not account for the records' statement that each competition experiment used a freshly prepared surface at a differing immobilisation level before reading a two-fold dissociation-constant shift as thermodynamic cooperativity | 2 of 3 | The mechanism case, not the verdict |
| `no-cross-species` | Proposed a mouse in vivo efficacy study without establishing mouse MGAT1 potency, where every compound measurement in the room is against human enzyme | 2 of 3 | **The study package — invalidates a named comparator** |
| `selectivity-unrobust` | Asserted the genotype-selectivity magnitude without testing whether it survives a different correction. The three attempts reached "not selective", "strongly selective" and "context-enhanced" on the same file | 1 of 3 | **Asset positioning** |
| `no-safety-position` | Listed the absence of toxicology data without taking a position from known target biology | 1 of 3 | Partly |

## Counterfactuals

- `lectin-ms-commensurable` — the dataset is ruled out as a product-side reference because 16 complex-sialylated sites were quantified against 317 high-mannose, not because its magnitudes disagree with flow cytometry.
- `spr-cooperativity` — non-competitive binding is established by the additive thermal shifts and the ternary structure; the competition constants add nothing and assert a result the surfaces cannot support.
- `no-cross-species` — a mouse efficacy study run with a compound of unknown mouse potency is uninterpretable whatever it shows.
- `selectivity-unrobust` — the differential is 2.28 log2 control-guide centred, 2.22 median centred, 1.43 uncorrected. The direction is stable; the magnitude is not, and the asset's positioning turns on it.
- `no-safety-position` — cardiac and autoimmune risk are nameable from target biology with no toxicology data in hand.

## Pre-registered but not observed in three attempts

These were the original Stage 4 predictions. None fired cleanly. Retained because three
correlated attempts is a thin window, and weaker trajectories may still produce them.

| Short name | Prediction |
|---|---|
| `channel-normalised` | Normalises the quantitative channels to equal total or median, shrinking the real substrate accumulation and manufacturing a ~1.7-fold product depletion |
| `unmeasured-product-side` | Draws a product-side conclusion without establishing how many complex sites were quantified |
| `fitted-potency` | Quotes a fitted potency for a compound whose dose-response never approaches full inhibition |

## Known design weakness

The verdict is over-determined. The absence of any cellular compound data is stark enough
that every route reaches "not yet, fund the bridge". Two of the three observed modes do not
change the call — they change whether it was earned. If the FA needs a mode that explains a
wrong answer rather than a flawed route, `selectivity-unrobust` is the only candidate, and
making it load-bearing would mean reopening Stage 1 so that the positioning call depends on
the selectivity magnitude.
