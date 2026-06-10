# Seth Second Brain

Retrieval-first personal knowledge base.

This repo is a markdown substrate for full raw captures, compiled durable wiki pages, and agent-friendly retrieval. It uses `Astro-Han/karpathy-llm-wiki` as the installed baseline skill and adds Seth-specific lanes for exact X capture, Last30Days staging, qmd search, and provenance.

## Mental Model

```text
intentional captures -> raw/intentional -> light compile -> wiki/
last30days sweeps    -> raw/sweeps      -> staging digest -> optional wiki promotion
queries              -> search wiki + raw, answer with links back to both
```

## Start Here

- [AGENTS.md](AGENTS.md) - operating instructions for agents.
- [.agents/skills/karpathy-llm-wiki/SKILL.md](.agents/skills/karpathy-llm-wiki/SKILL.md) - installed upstream baseline.
- [.agents/skills/seth-second-brain/SKILL.md](.agents/skills/seth-second-brain/SKILL.md) - Seth-specific overlay.
- [.agents/skills/qmd/SKILL.md](.agents/skills/qmd/SKILL.md) - local retrieval/search skill.
- [docs/architecture.md](docs/architecture.md) - v1 architecture and decisions.
- [docs/workflows.md](docs/workflows.md) - capture, query, Last30Days, and lint workflows.
- [wiki/index.md](wiki/index.md) - compiled knowledge index.
- [wiki/log.md](wiki/log.md) - append-only operation log.

## Directory Map

```text
raw/intentional/       full immutable captures chosen by Seth
raw/sweeps/            automated or semi-automated research outputs
staging/               digest and promotion queue for messy inputs
wiki/                  durable compiled knowledge articles
templates/             raw, wiki, and staging templates
config/                retrieval and sweep configuration
scripts/               thin wrappers around external tools
docs/                  architecture and runbooks
outputs/               one-off generated briefs, study guides, and essays
```

## Current V1 Choices

- Baseline: `Astro-Han/karpathy-llm-wiki`, augmented for Seth's workflow.
- One global wiki.
- `raw/` preserves full readable source snapshots.
- `wiki/` is organized by emergent idea domains.
- Intentional captures compile into wiki immediately, but lightly.
- Last30Days outputs are kept separate and staged before promotion.
- Retrieval searches both `raw/` and `wiki/`, with wiki privileged for synthesis questions.
- qmd is the intended local search layer once installed.

## Core Commands

```bash
# lint repo structure, links, and source-map shape
scripts/lint-second-brain.sh

# initialize/update qmd collections
scripts/init-qmd.sh

# refresh qmd and optionally build vector embeddings
scripts/qmd-refresh.sh
scripts/qmd-refresh.sh --embed

# save pasted source text into raw/intentional/<source-type>
scripts/new-raw-capture.sh web "Article title" "https://example.com/article" < article.txt

# capture exact X links into raw/intentional/x
scripts/x-capture-to-raw.sh "https://x.com/user/status/123"

# import old x-kb-capture notes without overwriting
scripts/import-x-kb-captures.sh --dry-run
scripts/import-x-kb-captures.sh

# run Last30Days into raw/sweeps/last30days
scripts/last30days-to-sweeps.sh --x-profile3 "AI coding agents" --search x,web,youtube

# scaffold a staging digest from a Last30Days raw output
scripts/stage-last30days-digest.sh raw/sweeps/last30days/<file>.md

# generate a proposed maintenance/pruning report
scripts/maintenance-report.sh
```
