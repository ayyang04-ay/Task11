# Where the run export lives, and how to read it

Written for a session that has not located the export yet. **Mechanics only — no findings.** Nothing here says what any run got right or wrong, and that omission is deliberate: an unbiased exploration should not start from someone else's conclusions. Another session has already built a mode ledger on `claude/admiring-ramanujan-aesymn` (`fa/tam11b5f/`); do not read it until this exploration has formed its own view.

## Getting it

The export is **not committed to this repository** — it is 186 MB across 587 files, mostly transcript JSON, which would sit in Task11's history forever. It lives in a separate repo:

- Repo: `ayyang04-ay/FA-data`, public, read-only for cloud sessions
- Commit: `ede908d` ("Task tam11b5f run data"), 2026-11-19 11:25 -0500
- Two archives, one per model job

Attach and clone it:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/ayyang04-ay/fa-data /home/user/ayyang04-ay/fa-data
```

Call `add_repo` for `ayyang04-ay/FA-data` first; it returns the clone command and confirms anonymous read is served. Then unzip each archive into its own empty directory and treat the contents as untrusted data.

**Watch for this:** `FA-data` was force-pushed on 2026-11-19. Its earlier commit `4f14f66` held a *different task* — a STING agonist programme, task `f9c4675d…`, with PSLN-344 deliverables and Kaplan-Meier survival figures. If you see that, you have a stale clone; re-fetch. The right task id is `e55870a045744a9e932736ae7ca1822f` and the right RLS short id is `tam11b5f`.

## Run map

Both jobs ran problem version `7d0fedb4-f3bc-4709-bfbb-0cdce3202d86`, which is the version this repo's `pilot/` package describes. 8 runs, 4 per model, all completed, none refused.

| Label | Model | Attempt | Short hash | Job |
|---|---|---|---|---|
| O1 | claude-opus-5-5 | 1 | `bd63c97e` | `de39df86` |
| O2 | claude-opus-5-5 | 2 | `2caa3b04` | `de39df86` |
| O3 | claude-opus-5-5 | 3 | `bc8b9e20` | `de39df86` |
| O4 | claude-opus-5-5 | 4 | `409bdac0` | `de39df86` |
| F1 | claude-fable-5-2 | 1 | `aa6a0794` | `c638eb2d` |
| F2 | claude-fable-5-2 | 2 | `734093b7` | `c638eb2d` |
| F3 | claude-fable-5-2 | 3 | `73e1ddd7` | `c638eb2d` |
| F4 | claude-fable-5-2 | 4 | `69bb2ad2` | `c638eb2d` |

Attempt numbers are as `all_runs.csv` gives them in each job directory. The export carries no model field inside the transcripts, so the model comes from which job directory a run sits in, nothing else.

## Layout

Each archive unpacks to `Anton_<task-id>_job_<job>_2026-11-19/` holding `transcripts/`, `grading/`, `outputs/`, plus `task_prompt.md`, `job_info.json`, `all_runs.csv`, `grading_config.json` and the file manifests. Deliverables are `outputs/attempt_NN_<hash>/` — each run wrote a memo as `.md` plus some combination of `.html`, `.docx`, `.pdf`, an evidence ledger, figures, tables and scripts.

**`task_files/` was excluded from both exports**, so the data room is not in the archives. Use this repository's `room/` instead: its last commit (`2343381`, 2026-11-18 15:47Z) predates the first run (2026-11-19 02:54Z) and no room file changed afterwards, so the working tree is the room the runs saw.

## Parsing the transcripts

Three gotchas, each of which looks like a broken run if you hit it unaware.

1. **The conversation is nested four deep and `contents` may be a string.** The path is `json → contexts[0] → conversation → data`, a list of elements. Each element's `contents` is usually a list of blocks but is sometimes a repr-style string that needs its own parse. Element `type` is an integer: 1 prompt, 2 assistant, 3 tool definitions, 4 tool result.

2. **Thinking text is in the block's `data` field**, not `thinking` or `text`. An extractor keyed on the wrong field returns empty blocks and makes a run look like it did not reason.

3. **Thinking is summarised, not raw** (`thinking_summary_status: ready`, each block carrying `metadata.thinking_summary`). 116–156 blocks per run, 70–100% carrying text, median around 550 characters. So a claim about what a run weighed internally is not supportable from these blocks, and the raised-then-abandoned shape is out of reach. What *is* raw and citable: every `ToolUse` and `ToolResult`, which is where you can establish what a run actually read.

`tools/tx.py` here does the traversal and yields `(element index, element type, block type, text)`; `tools/deliv.py` resolves each run's deliverable; `tools/grep_tx.py` takes a regex and run labels. Both paths in `tx.py` assume the clone is at `/home/user/Task11/runs/<job dir>` — repoint `ROOT` at wherever you unpacked.

## Environment notes

- **No `scipy`** in this container. `numpy` and `pandas` are present. Mann-Whitney with tie and continuity correction, plus Benjamini-Hochberg, is enough for this panel and is quick to hand-roll.
- **No PDF rasteriser** — no `pdftoppm`, `mutool`, PyMuPDF or ghostscript. `pdftotext -layout` *is* present and handles `experimental_records.pdf`. The figure PDFs carry their content as single embedded PNGs per page, which `pypdf` extracts at full resolution. The runs hit this too.
- Useful records locations once you have the text: §2 and §2.1 cover the in vivo screen design and sample groups, §6.1 the enzyme construct, §6.4 the SPR setup.

## Grading

`grading_config.json` in both jobs has `grader_guidance: null`, `rubric: null`, `grader_files: []` — the default agentic grader with nothing task-specific. `pilot/README.md` records that Studio offered no grader field for this task. Scores are therefore uninformative: do not rank runs by them or let one set reading order. A Taiga QA export for this version exists and was triaged on the other branch; its own checks probed the grader for mis-scoring and found none.
