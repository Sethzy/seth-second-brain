# Marketing Second Brain Demo Goal

## Decision / Outcome

Build `/Users/sethlim/Documents/marketing-second-brain-demo` as a public-ready marketing-only clone of Seth Second Brain. The finished repo should showcase the full Second Brain functionality through marketing material: immutable raw captures, compiled wiki, staging trust lanes, source-map provenance, QMD retrieval, Last30Days sweeps, exact X capture, lightweight linting, walkthrough examples, and a GitHub Pages front door.

The repo should be understandable as a small open-source product and as a Stripe Forward Deployed AI Accelerator, Marketing proof artifact.

## Evidence Surface

Strong evidence:

- `/Users/sethlim/Documents/marketing-second-brain-demo/README.md` explains the product, quick start, philosophy, flagship workflows, architecture, and FAQ.
- `/Users/sethlim/Documents/marketing-second-brain-demo/docs/index.html` renders a GitHub Pages-ready landing page.
- `/Users/sethlim/Documents/marketing-second-brain-demo/wiki/index.md` routes only marketing wiki pages.
- Included wiki pages cite included raw/staging files.
- `state/source-map.json` only references files included in the demo repo.
- `examples/x-capture-to-wiki/` and `examples/last30days-to-wiki/` show the two flagship workflows.
- Verification commands pass from the demo repo.

Proxy evidence:

- `rg` leak scans for personal/career-only material return no matches beyond intentionally public source text.
- QMD commands are documented and can run when QMD is installed, but `.qmd/` state is not committed.

Weak or insufficient evidence:

- A copied subset of files without README/product framing.
- Wiki pages with broken raw links.
- A GitHub Pages page that explains the idea but omits Last30Days or exact X capture.
- Any private application packet, phone/email, outreach, or non-marketing corpus material in the public repo.

## Scope And Boundaries

In scope:

- Source repo: `/Users/sethlim/Documents/Seth Second Brain`.
- Target repo: `/Users/sethlim/Documents/marketing-second-brain-demo`.
- Marketing wiki pages under `wiki/marketing/`.
- Selected raw/staging sources cited by the marketing pages.
- Demo-safe scripts for raw capture, X capture, Last30Days staging, QMD refresh, and linting.
- Static docs, examples, and GitHub Pages front door.

Out of scope:

- Publishing to GitHub or enabling GitHub Pages remotely.
- Running authenticated X capture against live cookies.
- Running a live Last30Days sweep.
- Committing `.qmd/` index state.
- Copying private career-ops application packets, personal contact details, or broad personal notes.
- Reworking the original Seth Second Brain architecture.

## Constraints

- Preserve the public demo repo name: `marketing-second-brain-demo`.
- Keep raw captures immutable once copied.
- Do not overclaim that sweep outputs are canonical truth.
- Keep Last30Days and exact X capture visible as flagship capabilities.
- Keep QMD documented as the first-line retrieval layer, but do not require embeddings in CI.
- Prefer static files and shell scripts over a build system.
- Do not overwrite unrelated user changes in the original Second Brain repo.

## Iteration Policy

After each implementation pass:

1. Run the demo repo lint/check script.
2. Inspect broken links, missing source-map references, and leak-scan output.
3. Fix the highest-impact correctness issue first: broken provenance before visual polish, private leak before docs polish.
4. Record the current state in this goal file's iteration log if the work pauses.

## Continuation Prompt Loop

When you hit a stopping point, write one paragraph for the next improvement attempt. Include: current evidence, the strongest remaining gap, the next concrete action, and the verification surface to inspect afterward. Keep going until the Completion Audit is satisfied or the Blocked Condition is met.

## Blocked Condition

Progress is blocked if:

- the source marketing corpus lacks enough public-safe raw material to support the wiki pages;
- copied scripts cannot be made demo-safe without live credentials or private paths;
- the leak scan surfaces private material that cannot be removed without breaking the demo thesis;
- filesystem access to either the source repo or target repo fails.

Unblock by providing approved public sources, approving a narrower corpus, accepting docs-only script stubs, or restoring filesystem access.

## Completion Audit

| Deliverable | Evidence Required | Status | Evidence Link / Command |
| --- | --- | --- | --- |
| Goal contract written | This file exists and defines outcome, evidence, constraints, and audit | Complete | `docs/goals/marketing-second-brain-demo-goal.md` |
| Implementation plan written | Plan exists with task-by-task implementation steps | Complete | `docs/superpowers/plans/2026-06-19-marketing-second-brain-demo-implementation-plan.md` |
| Demo repo created | Target path exists and is a git repo | Complete | `/Users/sethlim/Documents/marketing-second-brain-demo/.git`; demo commit `cf27d32` |
| Product README written | README explains thesis, quick start, workflows, architecture, and FAQ | Complete | `/Users/sethlim/Documents/marketing-second-brain-demo/README.md` |
| Marketing corpus curated | Wiki/raw/staging subset exists and links resolve | Complete | 8 marketing wiki pages, 33 raw/staging evidence files; `scripts/lint-second-brain.sh` passed |
| Flagship workflows documented | X capture and Last30Days examples exist | Complete | `/Users/sethlim/Documents/marketing-second-brain-demo/examples/x-capture-to-wiki/README.md`; `/Users/sethlim/Documents/marketing-second-brain-demo/examples/last30days-to-wiki/README.md` |
| GitHub Pages front door created | Static `docs/index.html` exists and links resolve | Complete | `/Users/sethlim/Documents/marketing-second-brain-demo/docs/index.html`; Playwright loaded `http://127.0.0.1:8765/docs/index.html?v=2` with title `marketing-second-brain-demo` |
| QMD documented | QMD docs and refresh command are present; `.qmd/` not committed | Complete | `/Users/sethlim/Documents/marketing-second-brain-demo/docs/qmd-retrieval.md`; `git status --short -- .qmd` produced no output |
| Leak scan passed | Personal/career-only terms absent from public repo | Complete | `rg -n "sethlimzy|9799|candidate-controlled|work authorization|Greenhouse|application form|final submit|WhatsApp recruiting|voluntary gender" .` produced no output |
| Final verification passed | Demo lint/check commands pass | Complete | `scripts/lint-second-brain.sh` passed; `python3 -m json.tool state/source-map.json` passed |

## Goal Prompt

```text
/goal Build /Users/sethlim/Documents/marketing-second-brain-demo as a public-ready marketing-only clone of Seth Second Brain, verified by a product README, GitHub Pages front door, curated marketing wiki/raw/staging corpus, source-map provenance, QMD documentation, Last30Days and exact X capture walkthroughs, demo-safe scripts, passing lint/link/source-map/leak checks, and a git commit in the demo repo. Preserve raw/source trust lanes, do not commit .qmd state, avoid private/career-only material, and do not overwrite unrelated changes in /Users/sethlim/Documents/Seth Second Brain. Between iterations, inspect lint output and leak scans, write a continuation prompt if pausing, and choose the next correction based on current evidence. If blocked, report attempted paths, evidence gathered, blocker, and what would unlock progress.
```

## Iteration Log

- 2026-06-19: Goal drafted from approved design spec `docs/superpowers/specs/2026-06-19-marketing-second-brain-demo-design.md`.
- 2026-06-19: Implemented and committed demo repo at `/Users/sethlim/Documents/marketing-second-brain-demo`, commit `cf27d32`.

## Final Result

Built `/Users/sethlim/Documents/marketing-second-brain-demo` as a public-ready marketing-only Second Brain demo. The repo includes a product README, public AGENTS guide, GitHub Pages front door, 8 compiled marketing wiki pages, 33 raw/staging evidence files, demo-only source map, QMD docs, exact X and Last30Days walkthroughs, demo-safe scripts, GitHub workflows, and a local lint/check script.

Verification passed:

- `scripts/lint-second-brain.sh`
- `python3 -m json.tool state/source-map.json`
- `rg -n "sethlimzy|9799|candidate-controlled|work authorization|Greenhouse|application form|final submit|WhatsApp recruiting|voluntary gender" .`
- `git status --short -- .qmd`
- Playwright loaded `http://127.0.0.1:8765/docs/index.html?v=2` with page title `marketing-second-brain-demo`.

Known limitations:

- The public X capture wrapper documents the authenticated flow but does not ship browser cookies or private auth tooling.
- The Last30Days wrapper documents the live flow and uses included sweep examples unless Last30Days is installed locally.
- GitHub remote creation and Pages activation are not done; the repo is ready for Seth to push.
