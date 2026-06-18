# Marketing Second Brain Demo Design

Date: 2026-06-19
Status: approved design
Owner: Seth

## Product Shape

`marketing-second-brain-demo` is a public, polished clone of the Seth Second Brain system narrowed to marketing materials only. It should feel like a small open-source product: clear thesis, quick start, workflows, architecture, examples, and a GitHub Pages front door.

The core claim:

> A retrieval-first marketing intelligence wiki for agents: capture raw market signal, preserve evidence, compile reusable marketing knowledge, and query it with QMD.

The demo keeps the full Second Brain operating model visible: immutable `raw/`, compiled `wiki/`, `staging/` for noisy or incomplete sources, `state/source-map.json`, append-only `wiki/log.md`, QMD search and embedding docs, lint scripts, Last30Days sweeps, and exact X-link capture. The corpus is marketing-only: AI marketing workflows, SEO/AEO/GEO, performance creative ops, lifecycle/CRM, autonomous landing pages, content ops, analytics, and Stripe-style Forward Deployed AI enablement.

The GitHub Pages site is a simple public front door. The repo itself remains the proof artifact.

## Audience And Positioning

The primary audience is a Stripe Forward Deployed AI Accelerator, Marketing reviewer or interviewer. The artifact should show that Seth understands how to turn messy social, web, and market signal into reusable marketing workflows with provenance, review gates, and retrieval.

The repo should not position Seth as a generic marketer. It should position him as a GTM/operator-builder who can sit with marketers, identify repeated workflows, build AI tools around real inputs, preserve evidence, and turn one-off wins into reusable playbooks.

The README tone should resemble `nanocoai/nanoclaw`: direct, product-like, and self-explanatory. It should explain why the repo exists, what it supports, how to run or inspect it, and how the architecture works.

## Architecture

The demo preserves the three-layer wiki pattern:

```text
raw/       immutable source evidence
staging/   noisy, incomplete, or not-yet-promoted research
wiki/      agent-maintained compiled marketing knowledge
```

`raw/intentional/` holds high-trust captures: pasted X posts, web articles, YouTube transcripts, repo snapshots, and selected marketing source material. `raw/sweeps/last30days/` holds Last30Days runs, clearly marked as recent-signal research rather than canonical truth. `staging/last30days/` holds digests that summarize sweeps, identify promising signals, and recommend whether anything should graduate into `wiki/`.

`wiki/` contains marketing-facing synthesis pages:

- `agentic-marketing-workflows`
- `seo-aeo-geo-content-systems`
- `performance-marketing-creative-ops`
- `autonomous-websites-and-landing-pages`
- `content-ops-and-editorial-systems`
- `lifecycle-crm-and-marketing-ops`
- `marketing-analytics-and-fda-enablement`

`wiki/index.md` routes readers and agents. `wiki/log.md` shows operational history. `state/source-map.json` keeps provenance auditable.

## Flagship Workflows

The two showcase workflows are:

```text
X URL -> x-capture script -> raw/intentional/x -> wiki update -> QMD refresh
Last30Days topic -> raw/sweeps -> staging digest -> selective wiki promotion
```

QMD sits across the whole repo as the retrieval layer. The README and GitHub Pages front door should explicitly show example commands:

```bash
qmd search "performance marketing creative ops"
qmd query $'intent: Find marketing workflow examples with source-backed claims.\nlex: performance marketing creative ops ads Last30Days X capture\nvec: marketing workflows that turn captured signal into campaign assets'
qmd get './wiki/marketing/agentic-marketing-workflows.md'
scripts/qmd-refresh.sh --embed
```

The public demo prompt can be:

```text
What do I know about AI performance marketing workflows?
```

A good answer should cite both compiled wiki pages and raw/staging evidence.

## Public Repo Content

The repo should be curated, not copied wholesale from Seth Second Brain.

Include:

- `README.md`: product README with title, pitch, quick start, why this exists, philosophy, supported workflows, usage examples, architecture, key files, and FAQ.
- `docs/`: concise docs for X capture, Last30Days, QMD retrieval, maintenance, and GitHub Pages.
- `wiki/`: marketing-only compiled pages plus `index.md` and `log.md`.
- `raw/`: selected marketing raw captures cited by the marketing pages.
- `staging/`: Last30Days marketing digests and incomplete captures that demonstrate trust lanes.
- `scripts/`: demo-safe wrappers for X capture, Last30Days staging, QMD refresh, linting, source-map checks, and raw capture creation.
- `state/source-map.json`: trimmed to only included sources.
- `.github/workflows/`: optional GitHub Pages deployment and link/lint checks.
- `docs/index.html` or equivalent GitHub Pages entrypoint.
- `examples/x-capture-to-wiki/`: before/after walkthrough for exact X capture.
- `examples/last30days-to-wiki/`: before/after walkthrough for sweep, digest, and promotion.

Exclude or sanitize:

- private career application packet details;
- phone, email, legal, or candidate-controlled application details;
- private outreach or account-specific material;
- non-marketing personal notes;
- broad AI-coding pages unless directly needed to explain tool mechanics;
- raw data containing sensitive people or company context.

## GitHub Pages And README Story

The GitHub Pages site should explain the repo in one minute:

```text
Capture signal -> preserve evidence -> compile wiki -> query with QMD -> maintain provenance
```

Suggested page sections:

- Hero: `marketing-second-brain-demo`, one-sentence pitch, links to README, wiki index, and walkthroughs.
- Workflow strip: X capture, Last30Days sweep, staging digest, wiki promotion, QMD query.
- Demo corpus: cards for SEO/AEO/GEO, performance creative ops, autonomous landing pages, lifecycle/CRM, content ops, analytics/FDA enablement.
- Trust model: raw is immutable, staging is lower-trust, wiki is compiled, source-map/log make changes auditable.
- Why this matters for marketers: turn noisy posts and market research into reusable funnel workflows, not just saved links.

The README should carry the deeper self-description:

> This is a demo of an agent-maintained marketing intelligence wiki. It shows how raw social/web signal becomes source-backed marketing knowledge and repeatable funnel workflows.

Last30Days and exact X capture should appear as first-class capabilities, not buried scripts.

## Trust And Error Handling

Trust lanes are central to the proof.

For X capture:

- complete captures go into `raw/intentional/x/`;
- partial, title-only, auth-failed, or preview-only captures go into `staging/incomplete-captures/x/`;
- wiki pages only make confident claims from complete captures or clearly mark uncertainty.

For Last30Days:

- raw sweep files stay in `raw/sweeps/last30days/`;
- digests go to `staging/last30days/`;
- promotion into `wiki/` is selective and logged;
- sweep-derived claims remain lower-trust unless backed by exact captured sources.

For QMD:

- search snippets are leads, not final evidence;
- docs should instruct readers to fetch full sources with `qmd get` or `qmd multi-get`;
- embedding refresh can be documented as optional for reviewers because local model support may vary.

## Testing And Verification

The demo should keep tests lightweight but real.

Required verification:

- wiki raw references point to included raw/staging files;
- `state/source-map.json` entries match included sources;
- README quickstart commands point to existing scripts;
- GitHub Pages links point to existing files;
- `wiki/index.md` routes to included wiki pages;
- no private/career-only material appears in public files.

Suggested commands:

```bash
scripts/lint-second-brain.sh
scripts/qmd-refresh.sh --embed
qmd search "performance marketing creative ops"
qmd query $'intent: Find source-backed marketing workflow examples.\nlex: Last30Days X capture QMD marketing workflow raw wiki staging'
```

QMD embedding should not be required in CI. It can be documented as a local enhancement because embeddings may be environment-sensitive.

## Acceptance Criteria

The design is complete when:

1. A reviewer can read the README and understand the product in under two minutes.
2. A reviewer can open GitHub Pages and understand the workflow without running scripts.
3. The marketing wiki cites included raw and staging sources.
4. Last30Days and exact X capture are visible as flagship capabilities.
5. QMD is documented as the first-line retrieval layer.
6. Source-map and wiki log demonstrate provenance and maintenance.
7. No personal, private, or career-only material leaks into the public demo.
8. The repo is named `marketing-second-brain-demo`.

## Open Questions For Implementation Planning

1. Should the demo repo be created as a new sibling directory under `/Users/sethlim/Documents/marketing-second-brain-demo`, or under a different workspace path?
2. Should the public corpus use only already-complete raw captures, or include a few explicitly incomplete staging examples for trust-lane demonstration?
3. Should the GitHub Pages site be plain static HTML under `docs/`, or generated from a minimal build step?
4. Should QMD embeddings be generated before publishing, or should the public repo document the refresh command and avoid committing `.qmd/` state?
5. Which exact X capture should be the canonical walkthrough example?
6. Which Last30Days sweep should be the canonical walkthrough example?

