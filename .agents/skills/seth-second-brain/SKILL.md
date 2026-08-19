---
name: seth-second-brain
description: "Use inside Seth Second Brain for retrieval-first capture, query, Last30Days staging, exact X link capture, provenance updates, and wiki maintenance. This augments the installed karpathy-llm-wiki baseline."
---

# Seth Second Brain

This project is a Seth-specific overlay on the installed `karpathy-llm-wiki` skill from `Astro-Han/karpathy-llm-wiki`.

Use the upstream skill for the durable LLM wiki pattern:

- `raw/` is immutable evidence.
- `wiki/` is compiled memory.
- `wiki/index.md` and `wiki/log.md` must stay current.
- Agents maintain and prune the wiki over time.

This overlay defines Seth's operational lanes.

## Retrieval Priority

For "find that thing I read":

1. Search `raw/` first.
2. Return the original URL and raw file path.
3. Mention related wiki pages if useful.

For "what do I know about X":

1. Read `wiki/index.md`.
2. Search `wiki/`.
3. Search `raw/`.
4. Answer with links to wiki pages and raw source files.

Prefer `qmd search` or `qmd query --no-rerank` when available; use `rg` as the fallback.

## Capture Lanes

Manual, intentional sources go under `raw/intentional/<source-type>/`.

Use these lanes:

- X/Twitter: `raw/intentional/x/`
- Web articles/docs: `raw/intentional/web/`
- YouTube/video transcripts: `raw/intentional/youtube/`
- Papers/PDFs: `raw/intentional/papers/`
- Book notes/excerpts: `raw/intentional/books/`
- Pasted material: `raw/intentional/pasted/`

For pasted or already-extracted source text, use:

```bash
scripts/new-raw-capture.sh <source-type> "<title>" "<url-or-Unknown>" < source.txt
```

Then compile lightly into 1-3 relevant wiki pages using the upstream wiki rules.

## LinkedIn Capture

When Seth asks to scrape, capture, ingest, or read LinkedIn content, use the already authenticated LinkedIn browser session:

1. Use Chrome browser control first.
2. Fall back to Computer Use when Chrome browser control is unavailable or the required interaction cannot be completed through it.
3. Open the exact URL and expand all relevant `…more` / `see more` controls before extracting.
4. Verify that the post or article body is complete. Preserve the author, date, headline/title, visible engagement counts, and original URL when available.
5. Save complete captures under `raw/intentional/web/`. Save previews, truncated text, login walls, and other incomplete results under `staging/incomplete-captures/web/`.

Do not use anonymous fetches or Last30Days as the first choice for exact LinkedIn URLs. Last30Days' optional LinkedIn source is useful for topic/person discovery, but it uses ScrapeCreators and Google-indexed public content rather than Seth's logged-in session. It is not a completeness guarantee.

## Exact X Links

For pasted X links, use the authenticated exact-link capture lane:

```bash
scripts/x-capture-to-raw.sh "https://x.com/user/status/123"
```

This wraps:

```text
scripts/x-capture-authenticated.py
```

The wrapper reuses Last30Days' Bird/TweetDetail approach with authenticated Chrome cookies and X Article field toggles. It defaults to Chrome `Profile 3`; use `SECOND_BRAIN_X_CHROME_PROFILE` or `--chrome-profile` on another machine. Complete normal posts and complete X Articles write to `raw/intentional/x/`. Title-only, preview-only, failed, or otherwise incomplete captures write to `staging/incomplete-captures/x/`.

The scripts discover Last30Days from common repo/global skill locations. If it is installed elsewhere, set `LAST30DAYS_SCRIPTS_DIR` to the skill's `scripts` directory.

Legacy `x-kb-capture` notes can still be imported with `scripts/import-x-kb-captures.sh`, but new exact X captures should use this repo's authenticated wrapper.

## Last30Days Sweeps

Last30Days is a noisy research lane, not durable wiki memory.

Run sweeps into:

```text
raw/sweeps/last30days/
```

Use:

```bash
scripts/last30days-to-sweeps.sh --x-profile3 "<topic>" --search x,web,youtube
scripts/stage-last30days-digest.sh raw/sweeps/last30days/<file>.md
```

Do not promote sweep material into `wiki/` unless Seth asks or the signal is clearly high-value and approved.

## Provenance

When a source is compiled, staged, promoted, archived, skipped, or superseded, update:

```text
state/source-map.json
```

Markdown files remain the source of truth; the source map is an audit trail.

## Maintenance

Use:

```bash
scripts/lint-second-brain.sh
scripts/maintenance-report.sh
```

Maintenance may propose merges, prunes, stale claims, or broken links. It may edit wiki pages, but it must never rewrite raw captures.
