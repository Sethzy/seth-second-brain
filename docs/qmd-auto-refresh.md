# QMD Auto Refresh

## Pattern From GTM Workspace

GTM Workspace does not use a native QMD file watcher. It keeps QMD fresh through two command-driven layers:

1. A repo script (`scripts/sync-drive-to-local.sh`) updates local Markdown cache files, then runs `qmd update` and `qmd embed`.
2. A Codex cron automation runs that script on weekday mornings.
3. GTM's agent rules say to use QMD first for content questions and to run `qmd update && qmd embed` after material Markdown writes.

That pattern is useful here, but the data must stay separate. Second Brain should not point at GTM collections or reuse GTM files.

## Second Brain Setup

Second Brain uses a project-local QMD config at `.qmd/index.yml`. When `qmd` is run anywhere inside this repo, QMD discovers that file and writes the generated SQLite index to `.qmd/index.sqlite` instead of the global default index.

Tracked:

- `.qmd/index.yml` - collection definitions and retrieval context.

Ignored:

- `.qmd/*.sqlite`
- `.qmd/*.sqlite-*`

The indexed collections are repo-local only:

- `wiki` -> `wiki/**/*.md`
- `intentional` -> `raw/intentional/**/*.md`
- `sweeps` -> `raw/sweeps/**/*.md`
- `staging` -> `staging/**/*.md`

## Refresh Commands

Use this for fast lexical freshness:

```bash
scripts/qmd-refresh.sh
```

Use this when semantic/vector search should be fresh too:

```bash
scripts/qmd-refresh.sh --embed
```

The refresh script calls `scripts/init-qmd.sh` first, so a missing local `.qmd` index is initialized before collections are updated.

## Automation Contract

The GTM-style automation for this repo is `second-brain-qmd-refresh`. It should:

- run from `/Users/sethlim/Documents/Seth Second Brain`;
- run `scripts/qmd-refresh.sh --embed`;
- write only the local `.qmd` index files and QMD model/cache state;
- not read, write, link, or sync GTM Workspace;
- report indexed file count, embedded chunk count, and any failures;
- rerun embedding once if it times out, because QMD embedding is incremental.

It is intentionally weekly, not frequent. Agent refresh-after-write is the main freshness path; the automation is only a safety net for manually added Markdown.

This gives Second Brain the same "kept warm" behavior as GTM without coupling the repos or running an expensive watcher.
