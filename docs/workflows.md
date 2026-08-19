# Workflows

## Capture An Intentional Source

Use when Seth pastes a URL, X post, article, transcript, or text and asks to save/capture/ingest it.

1. Identify source type: `x`, `web`, `youtube`, `papers`, `books`, or `pasted`.
2. Save a full verbatim raw snapshot under `raw/intentional/<source-type>/` only if the full source text was actually captured or pasted.
3. Keep the original URL and capture metadata at the top.
4. Lightly compile into 1-3 wiki articles.
5. Update `wiki/index.md`.
6. Append `wiki/log.md`.

Do not overwrite existing raw captures. Refreshes create new files.

If the result is a summary, URL-only note, oEmbed preview, login page, captcha page, or other incomplete capture, save it under:

```text
staging/incomplete-captures/<source-type>/
```

Incomplete captures preserve the lead, but they are not raw evidence and should not be compiled into confident wiki claims.

For pasted text that is already extracted, use:

```bash
scripts/new-raw-capture.sh --quality complete web "Article title" "https://example.com/article" < article.txt
scripts/new-raw-capture.sh pasted "Conversation notes" "Unknown" < notes.txt
scripts/new-raw-capture.sh --quality partial web "Blocked page lead" "https://example.com" < note.txt
```

Then compile the raw file into the wiki using the installed `karpathy-llm-wiki` skill rules.

## Capture LinkedIn Content

Use this workflow whenever Seth asks to scrape, capture, ingest, or read a LinkedIn post, article, or profile.

1. Use Chrome browser control with Seth's already logged-in LinkedIn session.
2. If Chrome browser control cannot attach or complete a required interaction, use Computer Use against the logged-in browser.
3. Open the exact URL. Expand every relevant `…more` / `see more` control and wait for any lazy-loaded content needed by the request.
4. Capture the full visible post/article body and the available author, date, headline/title, visible engagement counts, and original URL.
5. Verify that the saved body is not a preview or truncation.
6. Save a complete snapshot under `raw/intentional/web/`, compile it through the normal intentional-source workflow, update `state/source-map.json`, and refresh QMD.

For profile requests, capture only the requested sections. Do not inspect messages, export connections, or gather unrelated personal data unless Seth explicitly asks.

If the browser still yields only a preview, login wall, truncated body, or metadata:

```text
staging/incomplete-captures/web/
```

Preserve the exact URL and explain what is missing. Do not compile incomplete text into confident wiki claims.

Last30Days can be used for broad LinkedIn topic or person discovery after its LinkedIn source is configured, but it is not the exact-link capture path. Its upstream LinkedIn integration uses `SCRAPECREATORS_API_KEY` plus `--search linkedin` / `INCLUDE_SOURCES=linkedin`, searches Google-indexed public posts, and may enrich a matched person's public profile articles. It does not reuse Seth's authenticated LinkedIn session and does not guarantee a complete exact post.

## Capture Exact X Links

Use the authenticated exact-link capture wrapper:

```bash
scripts/x-capture-to-raw.sh "https://x.com/user/status/123"
```

For a text blob or clipboard full of links:

```bash
pbpaste | scripts/x-capture-to-raw.sh
```

This uses the same auth idea as `mvanhorn/last30days-skill`: Chrome cookies (`AUTH_TOKEN` and `CT0`) feed Bird/TweetDetail, with X Article field toggles enabled, so exact normal posts and supported long-form X Articles can be captured with full text. The default is `Profile 3`; set `SECOND_BRAIN_X_CHROME_PROFILE` or pass `--chrome-profile` on another machine.

The Last30Days skill may live inside this repo, in `~/.agents/skills`, in `~/.codex/skills`, or in the legacy GTM workspace. If it lives elsewhere, set:

```bash
export LAST30DAYS_SCRIPTS_DIR="/absolute/path/to/last30days/scripts"
```

Complete normal posts and complete X Articles write into:

```text
raw/intentional/x/
```

X Articles or posts where TweetDetail only returns a title/preview write into:

```text
staging/incomplete-captures/x/
```

After capture, inspect the note. If it is partial, preserve it as partial and do not make confident wiki claims from missing text.

To import existing captures from `~/Documents/Knowledge/x-posts`:

```bash
scripts/import-x-kb-captures.sh --dry-run
scripts/import-x-kb-captures.sh
```

The import script copies only missing files and updates `state/source-map.json`. It does not overwrite raw captures.

## Query The Knowledge Base

For broad knowledge questions:

```text
read wiki/index.md
search wiki/
search raw/
read top matches
answer with links
```

For source recall:

```text
search raw/
return original URL + raw file
mention related wiki page if useful
```

If the answer is reusable, ask whether to file it into the wiki. Use `templates/archive-template.md` for point-in-time query answers.

## Last30Days Run

Run Last30Days from this repo with the sweep save directory:

```bash
scripts/last30days-to-sweeps.sh "<topic>" --search x,web,youtube
```

If X browser auth is desired:

```bash
scripts/last30days-to-sweeps.sh --x-profile3 "<topic>" --search x,web,youtube
```

The wrapper passes `--save-dir raw/sweeps/last30days` to the upstream Last30Days CLI. Do not rely on `LAST30DAYS_MEMORY_DIR` alone for persistence.

## People Watchlist Sweeps

Use this when Seth wants periodic checks on high-signal people rather than broad topics.

People live in:

```text
config/people-watchlist.json
```

Run all configured people:

```bash
scripts/run-people-watchlist.sh
```

Run selected people:

```bash
scripts/run-people-watchlist.sh matt-pocock nicbstme
```

This uses Last30Days with `--x-handle <handle>` when a configured X handle exists, and otherwise runs a topic/web sweep. Each run is saved under `raw/sweeps/last30days/`, then scaffolded into a digest under `staging/last30days/`. Treat outputs as noisy watchlist signal. Promote only after manual capture or explicit approval.

After the run, create a staging digest from the saved raw file using `templates/last30days-digest-template.md`.

You can scaffold the digest with:

```bash
scripts/stage-last30days-digest.sh raw/sweeps/last30days/<file>.md
```

## Promote A Sweep To Wiki

Only promote sweep material when Seth asks or the signal is unusually strong.

1. Read the raw Last30Days output.
2. Read the staging digest.
3. Identify specific wiki pages to update.
4. Add source attribution back to the sweep raw file and original linked sources where present.
5. Update `wiki/index.md`.
6. Append `wiki/log.md`.

## Lint

Run:

```bash
scripts/lint-second-brain.sh
```

The lint is intentionally basic in v1: required files, expected folders, broken markdown links, and template presence.

For periodic self-improvement and pruning proposals:

```bash
scripts/wiki-health-report.sh
scripts/wiki-organize.sh --propose --limit 100
scripts/maintenance-report.sh
```

These create proposed reports under `staging/maintenance/`. `wiki-health-report.sh` reports raw-only counts, source-map hygiene, duplicate staging records, stale/orphan/large pages, and ranked next actions. `wiki-organize.sh --propose` creates a conservative proposal for clustering raw-only captures into existing medium synthesis pages before creating new wiki pages. Agents can then use the upstream LLM wiki lint rules to merge duplicate pages, propose missing synthesis pages, and flag stale or contradictory claims. Raw files remain immutable.

## qmd Retrieval

Initialize or refresh local retrieval:

```bash
scripts/init-qmd.sh
scripts/qmd-refresh.sh
```

For vector embeddings:

```bash
scripts/qmd-refresh.sh --embed
```

Useful query commands:

```bash
qmd search "remembered exact phrase" --format files
qmd query "what do I know about AI coding agents?" --no-rerank
qmd search "author handle or URL fragment" -c intentional --format files
```

## Provenance

Every raw source that has been compiled, staged, promoted, archived, or explicitly skipped should be represented in:

```text
state/source-map.json
```

The source map is an audit aid, not a database of truth. Markdown files remain the source of truth.
