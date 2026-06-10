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

## Capture Exact X Links

Use the authenticated exact-link capture wrapper:

```bash
scripts/x-capture-to-raw.sh "https://x.com/user/status/123"
```

For a text blob or clipboard full of links:

```bash
pbpaste | scripts/x-capture-to-raw.sh
```

This uses the same auth idea as `mvanhorn/last30days-skill`: Chrome Profile 3 cookies (`AUTH_TOKEN` and `CT0`) feed Bird/TweetDetail, with X Article field toggles enabled, so exact normal posts and supported long-form X Articles can be captured with full text.

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
LAST30DAYS_MEMORY_DIR="$PWD/raw/sweeps/last30days" \
python3 /Users/sethlim/Documents/gtm-workspace/.agents/skills/last30days/scripts/last30days.py "<topic>"
```

If X browser auth via the GTM wrapper is desired:

```bash
cd /Users/sethlim/Documents/gtm-workspace
LAST30DAYS_MEMORY_DIR="/Users/sethlim/Documents/Seth Second Brain/raw/sweeps/last30days" \
scripts/last30days-x-profile3.sh "<topic>" --search x,web,youtube
```

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
scripts/maintenance-report.sh
```

This creates a proposed report under `staging/maintenance/`. Agents can then use the upstream LLM wiki lint rules to merge duplicate pages, propose missing synthesis pages, and flag stale or contradictory claims. Raw files remain immutable.

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
