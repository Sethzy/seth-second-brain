---
type: wiki_health_report
created_at: 2026-06-20T03:26:26Z
status: proposed
---

# Wiki Health Report - 2026-06-20

## Counts

- Source-map entries: 3051
- Wiki articles: 35
- Raw-only sources: 2092

### Raw-Only By Source Type

| Source Type | Raw-Only Count |
|---|---:|
| x | 1997 |
| web | 91 |
| pasted | 2 |
| papers | 2 |

### Status By Source Type

| Source Type | Status Counts |
|---|---|
| data | compiled: 68 |
| last30days | compiled: 8, staged: 4 |
| last30days_digest | compiled: 8 |
| linkedin | staged_uncompiled: 1, compiled: 1 |
| manifest | compiled: 4 |
| papers | raw: 2, partial: 1 |
| pasted | compiled: 225, raw: 2 |
| web | compiled: 331, raw: 91, partial: 21, skipped: 2, superseded: 1 |
| x | raw: 1997, compiled: 197, failed: 50, partial: 7 |
| x_profile_timeline | staged: 7 |
| x_profile_timeline_digest | compiled: 2 |
| youtube | compiled: 19, partial: 2 |

## QMD Snapshot

```text
QMD Status

Index: /Users/sethlim/Documents/Seth Second Brain/.qmd/index.sqlite
Size:  224.5 MB

Documents
  Total:    3140 files indexed
  Vectors:  31257 embedded
  Updated:  10h ago

AST Chunking
  Status:   active
  Languages: typescript, tsx, javascript, python, go, rust

Collections
  wiki (qmd://wiki/)
    Pattern:  **/*.md
    Files:    37 (updated 13h ago)
    Contexts: 1
      /: Compiled durable knowledge articles, index, log, and arch...
  intentional (qmd://intentional/)
    Pattern:  **/*.md
    Files:    2981 (updated 10h ago)
    Contexts: 1
      /: Full immutable source snapshots intentionally saved by Se...
  sweeps (qmd://sweeps/)
    Pattern:  **/*.md
    Files:    24 (updated 2d ago)
```

## Wiki Shape

### Huge / Junk-Drawer Candidates

| Page | Words | Raw Refs |
|---|---:|---:|
| `wiki/archive/2026-06-11-sunder-sync-source-captures.md` | 7811 | 1018 |
| `wiki/ai-coding/agentic-engineering-practices.md` | 5567 | 188 |
| `wiki/ai-coding/vendor-agentic-engineering-blogs-2026.md` | 4851 | 322 |
| `wiki/gtm-sales/agentic-gtm-campaign-workflows.md` | 2891 | 92 |
| `wiki/ai-coding/ai-engineering-talks-on-agentic-coding.md` | 2884 | 34 |
| `wiki/ai-coding/agent-skill-libraries-and-requirements.md` | 2507 | 112 |
| `wiki/archive/2026-06-11-desktop-archive-saved-inputs.md` | 2369 | 153 |
| `wiki/personal-systems/agent-platforms-and-work-surfaces.md` | 2238 | 108 |
| `wiki/ai-knowledge-work/agentic-artifact-surfaces.md` | 2072 | 120 |
| `wiki/personal-systems/agent-goals-and-dynamic-workflows.md` | 1502 | 84 |

### Orphan Wiki Pages

- `wiki/agent-frameworks/agent-framework-landscape.md`
- `wiki/ai-coding/vendor-agentic-engineering-blogs-2026.md`
- `wiki/finance-ops/agentic-finance-workflows.md`
- `wiki/job-apps/startup-funding-signal-job-search.md`
- `wiki/openclaw/openclaw-architecture-and-operating-model.md`

### Stale / Missing Lifecycle Metadata

| Page | Status | Updated |
|---|---|---|
| `wiki/ai-coding/vendor-agentic-engineering-blogs-2026.md` | active | <missing> |

## Source Map Hygiene

- Raw markdown files missing from source map: 118
- Staging markdown files missing from source map: 2

First raw misses:
- `raw/intentional/pasted/sunder-sync-2026-06-11/005-2023843493765157235.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/006-2024197229548839268.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/007-nicbustamante-every-saas-is-now-an-api-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/009-nicolasbustamante-10-years-vertical-software-selloff-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/017-01-alexgilev-agent-intake-flow-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/019-04-pbteja-mission-control-guide-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/020-05-dhravyashah-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/021-06-rauchg-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/022-07-nityeshaga-full.md`
- `raw/intentional/pasted/sunder-sync-2026-06-11/023-08-dani-avila7-full.md`

First staging misses:
- `staging/incomplete-captures/x/2026-06-11-bloggersarvesh-2036068241936896421.md`
- `staging/last30days/2026-06-15-developer-portfolio-tech-projects-open-source-template-digest.md`

### Duplicate X capture/staging records

| Status ID | Records |
|---|---|
| 2036068241936896421 | `raw/intentional/x/2036068241936896421-bloggersarvesh-top-20-claude-prompts-for-seo-the-only-stack-you-ll-ever-need-this-is-the-a.md`<br>`staging/incomplete-captures/x/2026-06-11-bloggersarvesh-2036068241936896421.md` |
| 2044453102703841645 | `raw/intentional/x/2044453102703841645-av1dlive-ai-agent-stack-everyone-must-use-in-2026-builder-s-guide-here-is-the-truth-nobody.md`<br>`staging/incomplete-captures/x/2026-06-11-av1dlive-vercel-sandbox-agent-lead.md` |
| 2047145274200768969 | `raw/intentional/x/2047145274200768969-trae-ai-the-definitive-guide-to-harness-engineering-harness-engineering-is-simply-a-more-e.md`<br>`staging/incomplete-captures/x/2026-06-11-trae-ai-harness-engineering-lead.md` |
| 2053127519872614419 | `raw/intentional/x/2053127519872614419-garrytan-meta-meta-prompting-the-secret-to-making-ai-agents-work-people-keep-asking-me-why.md`<br>`staging/incomplete-captures/x/2026-06-10-garry-tan-interesting-skills-lead.md` |
| 2054564519280804028 | `raw/intentional/x/2054564519280804028-akshay-pachaar-hermes-agent-masterclass-everything-you-need-to-understand-and-customize-he.md`<br>`staging/incomplete-captures/x/2026-06-10-akshay-pachaar-agent-lead.md` |

## Staging Ready For Promotion

| Staging Digest | Recommendation |
|---|---|
| `staging/last30days/2026-06-17-ai-content-operations-editorial-quality-brand-voice-product-marketing-workflows-digest.md` | promote; use jet-seo, Anthropic, and Eric Siu captures for operational claims. |
| `staging/last30days/2026-06-17-ai-marketing-workflow-transformation-stripe-anthropic-claude-code-marketers-agents-skills-digest.md` | promote as trend evidence; use Stripe and Anthropic exact captures for named-company claims. |
| `staging/last30days/2026-06-17-ai-ugc-creator-generation-influencer-videos-tiktok-reels-product-ads-digest.md` | promote as trend evidence with compliance cautions. |
| `staging/last30days/2026-06-17-marketing-analytics-attribution-dashboards-experiment-measurement-ai-workflows-digest.md` | partial; promote measurement-loop concepts, but verify named-tool claims before use. |
| `staging/last30days/2026-06-17-performance-marketing-ai-ad-generation-google-ads-meta-ads-creative-variants-digest.md` | promote as trend evidence; use Anthropic official marketing capture for exact performance workflow claims. |
| `staging/last30days/2026-06-17-seo-aeo-geo-llm-search-ai-search-visibility-marketing-workflows-digest.md` | promote as repeated trend evidence; use jet-seo and Claude SEO captures for workflow claims. |

## Ranked Next Actions

1. Run `scripts/wiki-organize.sh --propose --limit 100` to generate a raw-only X promotion queue.
2. Approve one proposal cluster, then compile it into existing medium wiki pages before creating new pages.
3. Resolve duplicate X staging records after their raw captures are confirmed in source-map.
4. Split or tighten huge pages only when a cluster has a clear reusable concept boundary.
5. Run `scripts/qmd-refresh.sh --embed` after approved wiki/source-map changes.
