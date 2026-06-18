# Marketing Second Brain Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `/Users/sethlim/Documents/marketing-second-brain-demo` as a public-ready marketing-only Second Brain demo with README, GitHub Pages, curated corpus, examples, scripts, provenance, and verification.

**Architecture:** Use a static markdown-first repo with the same `raw/`, `staging/`, `wiki/`, `scripts/`, and `state/` shape as Seth Second Brain. Copy and curate public-safe marketing material from the source repo, then add product-facing docs and lightweight shell verification. Avoid a build system and do not commit `.qmd/`.

**Tech Stack:** Markdown, POSIX shell, static HTML/CSS, git, QMD CLI documentation.

---

## File Structure

- Create target repo: `/Users/sethlim/Documents/marketing-second-brain-demo/`
- Create: `README.md` for NanoClaw-style product framing.
- Create: `AGENTS.md` with public demo operating rules.
- Create: `docs/index.html` as the GitHub Pages front door.
- Create: `docs/capture-x.md`, `docs/last30days.md`, `docs/qmd-retrieval.md`, `docs/maintenance.md`, `docs/github-pages.md`.
- Create: `examples/x-capture-to-wiki/README.md` and `examples/last30days-to-wiki/README.md`.
- Copy and curate: `wiki/marketing/*.md`, `wiki/index.md`, `wiki/log.md`.
- Copy selected cited files under `raw/` and `staging/`.
- Create: `state/source-map.json` with demo-only entries.
- Create/modify scripts: `scripts/lint-second-brain.sh`, `scripts/qmd-refresh.sh`, `scripts/new-raw-capture.sh`, `scripts/x-capture-to-raw.sh`, `scripts/last30days-to-sweeps.sh`, `scripts/stage-last30days-digest.sh`.
- Create: `.github/workflows/pages.yml` and `.github/workflows/lint.yml`.
- Create: `.gitignore`, `LICENSE`.

### Task 1: Prepare Target Repo

**Files:**
- Create: `/Users/sethlim/Documents/marketing-second-brain-demo/`
- Create: `/Users/sethlim/Documents/marketing-second-brain-demo/.gitignore`
- Create: `/Users/sethlim/Documents/marketing-second-brain-demo/LICENSE`

- [ ] **Step 1: Create the target directory**

Run:

```bash
mkdir -p /Users/sethlim/Documents/marketing-second-brain-demo
```

Expected: directory exists.

- [ ] **Step 2: Initialize git if needed**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
git init
```

Expected: `.git/` exists.

- [ ] **Step 3: Add base ignore and license**

Create `.gitignore` with:

```gitignore
.DS_Store
.qmd/
node_modules/
tmp/
*.log
```

Create `LICENSE` with MIT license text for `2026 Seth Lim`.

- [ ] **Step 4: Verify**

Run:

```bash
test -d /Users/sethlim/Documents/marketing-second-brain-demo/.git
test -f /Users/sethlim/Documents/marketing-second-brain-demo/.gitignore
test -f /Users/sethlim/Documents/marketing-second-brain-demo/LICENSE
```

Expected: all commands exit 0.

### Task 2: Copy Marketing Corpus

**Files:**
- Copy: source `wiki/marketing/*.md` into target `wiki/marketing/`
- Create: target `wiki/index.md`, `wiki/log.md`
- Copy selected public raw/staging sources under target `raw/` and `staging/`

- [ ] **Step 1: Create corpus directories**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
mkdir -p wiki/marketing raw/intentional/{pasted,web,x,youtube} raw/sweeps/last30days staging/last30days staging/incomplete-captures/web state scripts docs examples/x-capture-to-wiki examples/last30days-to-wiki .github/workflows
```

Expected: directories exist.

- [ ] **Step 2: Copy marketing wiki pages**

Run from source repo:

```bash
cd /Users/sethlim/Documents/Seth\ Second\ Brain
cp wiki/marketing/*.md /Users/sethlim/Documents/marketing-second-brain-demo/wiki/marketing/
```

Expected: eight marketing wiki files exist in target.

- [ ] **Step 3: Copy selected raw/staging evidence**

Copy all raw/staging files referenced by the marketing pages that are public-safe:

```bash
cd /Users/sethlim/Documents/Seth\ Second\ Brain
cp raw/intentional/pasted/2026-06-17-stripe-forward-deployed-ai-accelerator-marketing-job-posting.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/
cp raw/intentional/pasted/2026-06-17-jet-seo-atlas-seo-content-pipeline-local-project.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/
mkdir -p /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/sunder-sync-2026-06-11
cp raw/intentional/pasted/sunder-sync-2026-06-11/395-flint-custom-pages-per-prospect-validation.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/sunder-sync-2026-06-11/
cp raw/intentional/pasted/sunder-sync-2026-06-11/146-michellelim-how-apps-dont-get-killed-by-claude-full.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/sunder-sync-2026-06-11/
cp raw/intentional/pasted/sunder-sync-2026-06-11/094-how-to-generate-ai-influencers-that-actually-look-real-twitter-alexcooldev-2020883184922324994-full.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/pasted/sunder-sync-2026-06-11/
cp raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/web/
cp raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/web/
cp raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/web/
cp raw/intentional/web/2026-06-11-agency-agents-readme.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/web/
cp raw/intentional/web/2026-06-18-ivangfalco-ads-skills-repository-snapshot.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/web/
cp raw/intentional/youtube/2026-06-18-how-to-get-unlimited-leads-using-claude-code-for-paid-ads-tr.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/youtube/
cp raw/intentional/x/2026-06-18-bryant-chou-ploy-launch-x-post.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/x/
cp raw/intentional/x/2031497289617883451-hesamation-anthropic-s-entire-growth-marketing-team-has-been-one-person-for-10-months-the.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/intentional/x/
cp raw/sweeps/last30days/*marketing*raw.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/sweeps/last30days/
cp raw/sweeps/last30days/*seo-aeo-geo*raw.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/sweeps/last30days/
cp raw/sweeps/last30days/*autonomous-landing-pages*raw.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/sweeps/last30days/
cp raw/sweeps/last30days/*ai-ugc*raw.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/sweeps/last30days/
cp raw/sweeps/last30days/*ai-content-operations*raw.md /Users/sethlim/Documents/marketing-second-brain-demo/raw/sweeps/last30days/
cp staging/last30days/2026-06-17-*marketing* /Users/sethlim/Documents/marketing-second-brain-demo/staging/last30days/
cp staging/last30days/2026-06-17-*seo-aeo-geo* /Users/sethlim/Documents/marketing-second-brain-demo/staging/last30days/
cp staging/last30days/2026-06-17-*autonomous-landing-pages* /Users/sethlim/Documents/marketing-second-brain-demo/staging/last30days/
cp staging/last30days/2026-06-17-*ai-ugc* /Users/sethlim/Documents/marketing-second-brain-demo/staging/last30days/
cp staging/last30days/2026-06-17-*ai-content-operations* /Users/sethlim/Documents/marketing-second-brain-demo/staging/last30days/
cp staging/incomplete-captures/web/2026-06-17-linkedin-post-lead-anthropic-guide-on-using-claude-for-marke.md /Users/sethlim/Documents/marketing-second-brain-demo/staging/incomplete-captures/web/
```

Expected: copied files exist; missing glob matches should be investigated, not ignored.

- [ ] **Step 4: Create a marketing-only index and log**

Create `wiki/index.md` with the marketing domain table and page entries. Create `wiki/log.md` with a concise demo history.

- [ ] **Step 5: Verify**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
find wiki/marketing -type f -name '*.md' | wc -l
find raw staging -type f -name '*.md' | wc -l
```

Expected: `wiki/marketing` count is 8; raw/staging count is greater than 20.

### Task 3: Add Docs, Examples, And Pages

**Files:**
- Create: `README.md`, `AGENTS.md`, docs files, examples, `docs/index.html`

- [ ] **Step 1: Write product docs**

Create the README and docs using the approved design. The README must include:

- one-sentence pitch;
- why this exists;
- quick start;
- flagship workflows;
- QMD retrieval examples;
- trust lanes;
- architecture;
- key files;
- FAQ.

- [ ] **Step 2: Write example walkthroughs**

Create `examples/x-capture-to-wiki/README.md` around the Bryant Chou/Ploy X capture. Create `examples/last30days-to-wiki/README.md` around the AI marketing workflow Last30Days sweep.

- [ ] **Step 3: Write GitHub Pages static front door**

Create `docs/index.html` with a compact landing page that links to README, wiki index, example walkthroughs, and docs.

- [ ] **Step 4: Verify docs links exist**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
test -f README.md
test -f AGENTS.md
test -f docs/index.html
test -f docs/capture-x.md
test -f docs/last30days.md
test -f docs/qmd-retrieval.md
test -f examples/x-capture-to-wiki/README.md
test -f examples/last30days-to-wiki/README.md
```

Expected: all commands exit 0.

### Task 4: Add Demo-Safe Scripts And Provenance

**Files:**
- Create: `scripts/lint-second-brain.sh`, `scripts/qmd-refresh.sh`, `scripts/new-raw-capture.sh`, `scripts/x-capture-to-raw.sh`, `scripts/last30days-to-sweeps.sh`, `scripts/stage-last30days-digest.sh`
- Create: `state/source-map.json`

- [ ] **Step 1: Add scripts**

Use demo-safe scripts. `x-capture-to-raw.sh` and `last30days-to-sweeps.sh` should explain required external tooling and exit with a helpful message if the private/local dependency is unavailable. `lint-second-brain.sh` should run local checks without network.

- [ ] **Step 2: Generate demo source-map**

Create `state/source-map.json` with entries only for included raw and staging files. Each entry should include `id`, `title`, `source_type`, `trust_lane`, `capture_quality`, `raw_path` or `staging_path`, `status`, and `wiki_paths`.

- [ ] **Step 3: Verify source map and scripts**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
python3 -m json.tool state/source-map.json >/dev/null
chmod +x scripts/*.sh
scripts/lint-second-brain.sh
```

Expected: JSON parses, scripts are executable, lint passes.

### Task 5: Add GitHub Workflows And Final Checks

**Files:**
- Create: `.github/workflows/pages.yml`
- Create: `.github/workflows/lint.yml`

- [ ] **Step 1: Add workflows**

Create GitHub Pages and lint workflow YAML files. Pages should publish `docs/`. Lint should run `scripts/lint-second-brain.sh`.

- [ ] **Step 2: Run leak scan**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
rg -n "sethlimzy|9799|candidate-controlled|work authorization|sponsorship|Greenhouse|application form|final submit|WhatsApp recruiting|voluntary gender" . || true
```

Expected: no output.

- [ ] **Step 3: Run final verification**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
scripts/lint-second-brain.sh
git status --short -- .qmd
git status --short
```

Expected: lint passes; `.qmd` has no tracked or staged files; repo changes are expected new demo files.

- [ ] **Step 4: Commit demo repo**

Run:

```bash
cd /Users/sethlim/Documents/marketing-second-brain-demo
git add .
git commit -m "feat: create marketing second brain demo"
```

Expected: commit succeeds.

### Task 6: Update Goal Audit

**Files:**
- Modify: `/Users/sethlim/Documents/Seth Second Brain/docs/goals/marketing-second-brain-demo-goal.md`

- [ ] **Step 1: Update Completion Audit and Final Result**

Update statuses to Complete and add evidence commands/paths from the finished demo repo.

- [ ] **Step 2: Commit goal and plan in source repo**

Run:

```bash
cd /Users/sethlim/Documents/Seth\ Second\ Brain
git add docs/goals/marketing-second-brain-demo-goal.md docs/superpowers/plans/2026-06-19-marketing-second-brain-demo-implementation-plan.md
git commit -m "docs: add marketing second brain demo goal"
```

Expected: commit succeeds with only the goal and plan docs staged.

## Self-Review

Spec coverage:

- Product README and GitHub Pages: Task 3.
- Marketing-only raw/wiki/staging corpus: Task 2.
- Last30Days and X capture: Tasks 2, 3, 4.
- QMD documentation and no `.qmd`: Tasks 3 and 5.
- Source-map/log/provenance: Tasks 2 and 4.
- Verification and leak scan: Task 5.
- Goal audit: Task 6.

Placeholder scan: no unresolved placeholder markers are intentional in this plan.

Type/path consistency: target path is consistently `/Users/sethlim/Documents/marketing-second-brain-demo`.
