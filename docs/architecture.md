# Seth Second Brain V1 Architecture

## Decision

Build a retrieval-first personal durable wiki, not a personal operating system.

The repository should help Seth find things he intentionally saved, ask questions across what he has learned, and compound source material into durable idea pages. It should not track contacts, tasks, CRM state, or broad life operations.

## Inspirations

- GTM workspace architecture: plain markdown operating memory, qmd-ready search, wiki/index/log discipline.
- `Astro-Han/karpathy-llm-wiki`: light Agent Skill model with `raw/` plus `wiki/`.
- `mvanhorn/last30days-skill`: separate social/recent-signal research lane with fixed raw outputs.

## Source Of Truth

| Layer | Role | Mutability |
|---|---|---|
| `raw/intentional/` | Full readable snapshots Seth explicitly chose | Immutable |
| `raw/sweeps/` | Automated or semi-automated candidate intelligence | Immutable per run |
| `staging/` | Digests, promotion candidates, review queues | Mutable |
| `wiki/` | Compiled durable knowledge | Mutable |
| `outputs/` | One-off generated artifacts | Mutable |

## Retrieval Strategy

Default retrieval searches both raw and wiki.

- Source-recall questions are raw-first.
- Knowledge questions are wiki-first, raw-second.
- Audit/exploration questions search both and group results.

qmd is the intended local search layer. Until qmd is installed, use `rg` and direct file reads.

## Manual Capture Flow

Manual captures are high-trust. Most things Seth saves are assumed relevant.

```text
URL or pasted source
  -> full raw snapshot under raw/intentional/<type>/
  -> light wiki update
  -> index/log update
```

Raw captures must remain pleasant to reread and must keep the original link at the top.

## Last30Days Flow

Last30Days is useful but noisy. It should be kept separate.

```text
last30days run
  -> raw/sweeps/last30days/<date-topic>-raw.md
  -> staging/last30days/<date-topic>-digest.md
  -> optional promotion to wiki after review
```

Last30Days outputs are candidate intelligence, not durable memory by default.

## Completion Criteria For V1

- The repo has a clear raw/wiki/staging scaffold.
- Templates exist for raw captures, X captures, wiki articles, and Last30Days digests.
- Agent instructions encode retrieval behavior.
- qmd configuration exists and is ready to copy/install.
- Last30Days can be pointed at the repo's sweep directory.
- Basic lint/check script validates expected files and broken markdown links.

