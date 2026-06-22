# AI Engineering Six-Month Chronology HTML Goal

## Decision / Outcome

Create a polished standalone HTML chronology of what changed in AI software development over the last six months, grounded first in Seth Second Brain and then extended with current external research.

The finished artifact should help Seth scan the evolution of AI engineering month by month: what was hot, what shipped, what practices changed, and why each moment mattered for builders using coding agents, specs, skills, harnesses, sandboxes, verification loops, and visual artifact workflows.

Default date window for the first pass: January 1, 2026 through June 12, 2026, with December 2025 allowed only as a short prelude if a source is necessary context. If Seth prefers a strict rolling six-month window, use December 12, 2025 through June 12, 2026 instead.

## Evidence Surface

Strong evidence:

- Local compiled wiki articles, especially:
  - `wiki/ai-coding/agentic-engineering-practices.md`
  - `wiki/ai-coding/ai-engineering-talks-on-agentic-coding.md`
  - `wiki/ai-coding/agent-skill-libraries-and-requirements.md`
  - `wiki/ai-coding/devin-managed-agent-workflows.md`
  - `wiki/ai-coding/vercel-agent-templates-and-sandboxes.md`
  - `wiki/ai-knowledge-work/agentic-artifact-surfaces.md`
  - `wiki/personal-systems/agent-goals-and-dynamic-workflows.md`
  - `wiki/personal-systems/agent-platforms-and-work-surfaces.md`
- Raw Second Brain sources cited by those pages, especially intentional web, X, YouTube, and pasted captures under `raw/intentional/`.
- External primary or near-primary sources per month: official changelogs, product docs, launch posts, conference talks, GitHub repos/releases, company engineering posts, and authoritative transcripts.
- A local research ledger listing every important claim, month, source URL, source type, confidence, and whether it was already captured in Second Brain.
- Rendered HTML checked in a browser at desktop and mobile widths.

Proxy evidence:

- Community X posts, roundups, newsletters, and commentary that identify "hot topics" or developer sentiment, only when paired with at least one stronger source or explicitly labeled as sentiment.
- Search result frequency or social buzz, only as a weak ranking signal.

Weak or excluded evidence:

- Link cards, failed captures, login/captcha pages, or incomplete captures from `staging/incomplete-captures/` cannot support confident factual claims.
- Rumors, unreleased leaks, benchmark-only discourse, or uncited "everyone was talking about" claims should be omitted or labeled as uncertain.

## Scope And Boundaries

In scope:

- AI engineering as AI software development, not general AI news.
- Coding agents and agentic SDLC: Claude Code, Codex, Cursor-style agents, Devin, OpenCode/OpenClaw-style ecosystems, managed coding agents, background agents, agent review/autofix loops, spec-driven development, context engineering, harness engineering, skills, MCP/tooling, sandboxes, visual/browser verification, AI-generated artifacts, and agent-readable documentation.
- Month-by-month narrative with a small number of high-signal moments per month rather than an exhaustive news feed.
- A visual, scannable, single-page HTML artifact that can be opened locally without a build step.
- Supporting source ledger in Markdown or JSON next to the HTML artifact.

Out of scope:

- General model leaderboard coverage unless it materially changed AI software development workflows.
- Consumer chatbot features, image/video model launches, or enterprise AI strategy unless they affected developer workflows or agentic engineering practice.
- Updating wiki synthesis pages unless Seth explicitly asks to file the chronology back into the wiki.
- Treating incomplete captures as evidence.
- Building a web app with a framework unless the static HTML ceiling is insufficient.

## Constraints

- Preserve Second Brain rules: raw sources are immutable; wiki pages are not edited unless the work explicitly becomes a wiki filing task.
- Start with `wiki/index.md`, search `wiki/`, then search `raw/` before external web research.
- Use external research because the chronology is current and temporally unstable.
- Cite sources clearly in the HTML and ledger.
- Separate confirmed facts, interpretation, and "hot topic" signals.
- Do not overstate month boundaries; a topic can span multiple months, but each month should have a dominant theme.
- Keep the HTML artifact visually rich but useful: timeline first, explanation second.
- Use accessible colors, responsive layout, readable type, and no text overlap at mobile or desktop widths.
- Avoid a one-note palette and avoid decorative clutter that makes scanning harder.
- Verify the rendered HTML visually before calling the goal complete.

## Iteration Policy

1. Inventory local context:
   - Read `wiki/index.md`.
   - Read relevant AI Coding, AI Knowledge Work, and Personal Systems pages.
   - Search `raw/intentional/`, `raw/sweeps/`, and `staging/` for date-specific leads.
   - Create an initial local-source map by month and theme.

2. Build the month grid:
   - For each month, nominate 2-4 candidate themes.
   - Pick one primary theme and 2-3 secondary events, backed by evidence.
   - Record rejected candidates if they were plausible but weakly sourced.

3. External research:
   - Search the web month by month.
   - Prefer official docs, release notes, engineering blogs, GitHub repos, conference pages, and transcripts.
   - Use community posts only to explain salience or sentiment.
   - Update the research ledger as claims are accepted, revised, or rejected.

4. Narrative pass:
   - Convert the evidence grid into a chronology with concise month cards.
   - For each month, include: theme, why it mattered, key artifacts/releases/practices, practical takeaway for AI engineers, source links, and confidence.
   - Add cross-month arcs such as "from prompt tricks to agentic SDLC," "from agents to skills/harnesses," and "from generated code to verified loops."

5. HTML design/build:
   - Create a standalone HTML file, likely under `outputs/ai-engineering-chronology/index.html`.
   - Include a vertical or horizontal timeline, month cards, source chips, confidence markers, and a compact legend.
   - Add optional filters only if they improve scanning: models/tools, process/practice, infrastructure, verification, artifacts.
   - Keep CSS/JS inline unless external assets are clearly useful and local.

6. Verification:
   - Open the HTML locally in a browser.
   - Check desktop and mobile screenshots.
   - Confirm no layout overlap, unreadable contrast, broken links, blank sections, or missing citations.
   - Run a link/citation sanity pass against the ledger.

7. Final update:
   - Update this goal's completion audit and final result.
   - Report the artifact path, ledger path, verification performed, and known uncertainties.

## Blocked Condition

The goal is blocked if:

- Web research cannot access enough current sources to support at least four of six months.
- Local Second Brain sources are unavailable or unreadable.
- Browser verification cannot run and no credible alternative screenshot/render check is available.
- The timeline depends on claims that are mostly incomplete captures, rumors, or uncited community sentiment.
- Seth has not resolved the date-window choice and the difference materially changes the timeline.

Unblock by:

- Seth approving a narrower date range or theme.
- Seth pasting sources or pointing to preferred source lists.
- Running with a clearly labeled "local corpus only" or "draft, externally unverified" artifact.

## Completion Audit

| Deliverable | Evidence Required | Status | Evidence Link / Command |
| --- | --- | --- | --- |
| Local Second Brain inventory | Notes or ledger entries showing relevant wiki/raw pages searched before web research | Complete | `outputs/ai-engineering-chronology/research-ledger.md#local-inventory` |
| Month-by-month research ledger | One entry per accepted timeline claim with source URL/path, source type, month, confidence, and captured/not-captured status | Complete | `outputs/ai-engineering-chronology/research-ledger.md#accepted-monthly-claims` |
| External monthly research | At least 2 strong sources per month or explicit uncertainty notes where unavailable | Complete | `outputs/ai-engineering-chronology/research-ledger.md#accepted-monthly-claims` |
| Standalone HTML timeline | Local HTML file with timeline, month cards, sources, responsive styling, and no required build step | Complete | `outputs/ai-engineering-chronology/index.html` |
| Visual verification | Desktop and mobile browser checks, with screenshots or recorded notes | Complete | `outputs/ai-engineering-chronology/verification-notes.md`; screenshots in `outputs/ai-engineering-chronology/screenshots/` |
| Claim audit | Final pass separating confirmed facts, interpretation, proxy evidence, and blocked claims | Complete | `outputs/ai-engineering-chronology/research-ledger.md#claim-audit` |

## Goal Prompt

```text
/goal Create a polished standalone HTML chronology of the last six months in AI engineering / AI software development, verified by a local Second Brain inventory, a month-by-month source ledger, external current research with citations, and desktop/mobile browser checks of the rendered HTML, while preserving Seth Second Brain provenance rules and avoiding unsupported hype. Use wiki/index.md, relevant wiki pages, raw/intentional sources, staging only as weak leads, and current external web research. Between iterations, update the research ledger, choose each month's primary theme from evidence, inspect the rendered artifact, and revise the design until it is scannable and visually solid. If blocked or no valid paths remain, report the attempted sources, weak months, blocker, and what would unlock progress.
```

## Design Notes For Seth Review

Recommended artifact shape:

- Title: `AI Engineering Changed Fast`
- Subtitle: `A six-month chronology of agentic software development`
- Structure: six month cards on a timeline, plus a top-level "big arcs" strip.
- Big arcs to test against the evidence:
  - Prompting became process: specs, goals, plans, and task contracts.
  - Coding agents became harnesses: tools, skills, permissions, sandboxes, and memory.
  - Verification became the differentiator: tests, browser/computer-use checks, reviewer agents, and CI/autofix loops.
  - Artifacts became richer: HTML pages, decks, videos, diagrams, and inspectable side-panel outputs.
  - Human leverage moved upward: requirements, architecture, taste, risk, and judgment.
- Tone: analytical and builder-facing, not breathless.
- Visual style: modern technical editorial, dense enough to scan, but nicer than a memo.

Open design choices:

- Date range: January-June 2026 monthly chronology, or strict rolling window from December 12, 2025-June 12, 2026.
- Audience: personal learning artifact, interview/conversation aid, public-shareable industry timeline, or all three with restrained wording.
- Citation density: visible source chips on every card, or cleaner cards with a source drawer/appendix.
- Output location: keep inside this repo under `outputs/`, or place beside the interview artifacts under `/Users/sethlim/Documents/career-ops/interview-prep/`.

## Iteration Log

- 2026-06-12: Created the goal contract and chose the January 1 through June 12, 2026 window.
- 2026-06-12: Inventoried local Second Brain wiki pages and raw/staging lanes before external research.
- 2026-06-12: Built `outputs/ai-engineering-chronology/research-ledger.md` with accepted monthly claims, source types, confidence, uncertainty, cross-month arcs, weak/rejected leads, and claim audit.
- 2026-06-12: Built standalone `outputs/ai-engineering-chronology/index.html` with inline CSS/JS, source chips, evidence profile, big arcs, timeline cards, and filter controls.
- 2026-06-12: Ran static HTML/link checks and browser verification through a local `127.0.0.1` static server at desktop and mobile widths. Saved screenshots and notes under `outputs/ai-engineering-chronology/`.

## Final Result

Shipped the chronology artifact:

- HTML timeline: `outputs/ai-engineering-chronology/index.html`
- Research ledger: `outputs/ai-engineering-chronology/research-ledger.md`
- Verification notes: `outputs/ai-engineering-chronology/verification-notes.md`
- Screenshots:
  - `outputs/ai-engineering-chronology/screenshots/desktop.jpg`
  - `outputs/ai-engineering-chronology/screenshots/mobile-fullpage.jpg`
  - `outputs/ai-engineering-chronology/screenshots/mobile-viewport.jpg`

Known boundary: the chronology is source-grounded and current through 2026-06-12, but "hot topic" labels and cross-month arcs remain editorial synthesis rather than quantitative trend measurement.
