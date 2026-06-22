---
type: raw_capture
source_type: web
title: "AgricIDaniel claude-seo repository snapshot June 2026"
url: "https://github.com/AgricIDaniel/claude-seo"
collected_at: 2026-06-18T17:03:39Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# AgricIDaniel claude-seo repository snapshot June 2026

Source: https://github.com/AgricIDaniel/claude-seo

## Capture Text

# Repository Snapshot

Repository: https://github.com/AgricIDaniel/claude-seo
Captured commit: d830cdb2ad339bb7f062339fe82228b072e98061
Commit date: 2026-06-13T20:30:25+03:00
Commit subject: Update README.md
Prior local raw capture: raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md
Snapshot note: This is an immutable evidence snapshot of repository metadata, file tree, and selected docs/excerpts at the captured commit. It is not a full Git mirror. Use the commit hash and upstream URL for full repository reconstruction.

## File Tree
```text
.claude-plugin/marketplace.json
.claude-plugin/plugin.json
.devcontainer/devcontainer.json
.github/CODEOWNERS
.github/FUNDING.yml
.github/ISSUE_TEMPLATE/bug_report.yml
.github/ISSUE_TEMPLATE/config.yml
.github/ISSUE_TEMPLATE/feature_request.yml
.github/ISSUE_TEMPLATE/task.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/dependabot.yml
.github/release.yml
.github/workflows/ci.yml
.github/workflows/v2.yml
.gitignore
AGENTS.md
CHANGELOG.md
CITATION.cff
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTORS.md
LICENSE
PRIVACY.md
README.md
SECURITY.md
agents/seo-backlinks.md
agents/seo-cluster.md
agents/seo-content.md
agents/seo-dataforseo.md
agents/seo-drift.md
agents/seo-ecommerce.md
agents/seo-flow.md
agents/seo-geo.md
agents/seo-google.md
agents/seo-image-gen.md
agents/seo-local.md
agents/seo-maps.md
agents/seo-performance.md
agents/seo-schema.md
agents/seo-sitemap.md
agents/seo-sxo.md
agents/seo-technical.md
agents/seo-visual.md
assets/cover.svg
assets/framework.svg
assets/growth-3-months.png
assets/signal-flow.svg
assets/sub-skills.svg
data/google-updates.json
docs/ARCHITECTURE.md
docs/COMMANDS.md
docs/INSTALLATION.md
docs/MCP-INTEGRATION.md
docs/MIGRATION-v1-to-v2.md
docs/TROUBLESHOOTING.md
docs/WORKFLOW-public-private.md
extensions/ahrefs/docs/AHREFS-SETUP.md
extensions/ahrefs/install.ps1
extensions/ahrefs/install.sh
extensions/ahrefs/skills/seo-ahrefs/SKILL.md
extensions/ahrefs/uninstall.sh
extensions/banana/README.md
extensions/banana/agents/seo-image-gen.md
extensions/banana/docs/BANANA-SETUP.md
extensions/banana/install.sh
extensions/banana/references/cost-tracking.md
extensions/banana/references/gemini-models.md
extensions/banana/references/mcp-tools.md
extensions/banana/references/post-processing.md
extensions/banana/references/presets.md
extensions/banana/references/prompt-engineering.md
extensions/banana/references/seo-image-presets.md
extensions/banana/scripts/batch.py
extensions/banana/scripts/cost_tracker.py
extensions/banana/scripts/edit.py
extensions/banana/scripts/generate.py
extensions/banana/scripts/presets.py
extensions/banana/scripts/setup_mcp.py
extensions/banana/scripts/validate_setup.py
extensions/banana/skills/seo-image-gen/LICENSE.txt
extensions/banana/skills/seo-image-gen/SKILL.md
extensions/banana/uninstall.sh
extensions/bing-webmaster/docs/BING-WEBMASTER-SETUP.md
extensions/bing-webmaster/install.ps1
extensions/bing-webmaster/install.sh
extensions/bing-webmaster/skills/seo-bing/SKILL.md
extensions/bing-webmaster/uninstall.sh
extensions/dataforseo/README.md
extensions/dataforseo/agents/seo-dataforseo.md
extensions/dataforseo/docs/DATAFORSEO-SETUP.md
extensions/dataforseo/field-config.json
extensions/dataforseo/install.ps1
extensions/dataforseo/install.sh
extensions/dataforseo/skills/seo-dataforseo/LICENSE.txt
extensions/dataforseo/skills/seo-dataforseo/SKILL.md
extensions/dataforseo/uninstall.ps1
extensions/dataforseo/uninstall.sh
extensions/firecrawl/README.md
extensions/firecrawl/docs/FIRECRAWL-SETUP.md
extensions/firecrawl/install.ps1
extensions/firecrawl/install.sh
extensions/firecrawl/skills/seo-firecrawl/LICENSE.txt
extensions/firecrawl/skills/seo-firecrawl/SKILL.md
extensions/firecrawl/uninstall.ps1
extensions/firecrawl/uninstall.sh
extensions/profound/docs/PROFOUND-SETUP.md
extensions/profound/install.ps1
extensions/profound/install.sh
extensions/profound/skills/seo-profound/SKILL.md
extensions/profound/uninstall.sh
extensions/seranking/docs/SERANKING-SETUP.md
extensions/seranking/install.ps1
extensions/seranking/install.sh
extensions/seranking/skills/seo-seranking/SKILL.md
extensions/seranking/uninstall.sh
extensions/unlighthouse/docs/UNLIGHTHOUSE-SETUP.md
extensions/unlighthouse/install.ps1
extensions/unlighthouse/install.sh
extensions/unlighthouse/skills/seo-unlighthouse/SKILL.md
extensions/unlighthouse/uninstall.sh
hooks/hooks.json
hooks/run-python-hook.js
hooks/validate-schema.py
install.ps1
install.sh
pdf/google-seo-reference.md
pyproject.toml
requirements.txt
schema/templates.json
screenshots/seo-audit-demo.gif
screenshots/seo-command-demo.gif
scripts/agent_ux_check.py
scripts/analyze_visual.py
scripts/backlinks_auth.py
scripts/bing_webmaster.py
scripts/capture_screenshot.py
scripts/commoncrawl_graph.py
scripts/content_humanize.py
scripts/content_quality.py
scripts/content_verify.py
scripts/crux_history.py
scripts/dataforseo_costs.py
scripts/dataforseo_merchant.py
scripts/dataforseo_normalize.py
scripts/domain_history.py
scripts/drift_baseline.py
scripts/drift_compare.py
scripts/drift_history.py
scripts/drift_report.py
scripts/fetch_page.py
scripts/ga4_report.py
scripts/gbp_deprecation_lint.py
scripts/google_auth.py
scripts/google_report.py
scripts/gsc_inspect.py
scripts/gsc_query.py
scripts/indexing_notify.py
scripts/indexnow_submit.py
scripts/iptc_ai_label.py
scripts/keyword_planner.py
scripts/lcp_subparts.py
scripts/moz_api.py
scripts/nlp_analyze.py
scripts/pagespeed_check.py
scripts/parasite_risk.py
scripts/parse_html.py
scripts/portability_check.py
scripts/preload_check.py
scripts/release_sign.py
scripts/render_page.py
scripts/schema_ecommerce_validate.py
scripts/schema_generate.py
scripts/seo_updates.py
scripts/sync_flow.py
scripts/ucp_check.py
scripts/unlighthouse_run.py
scripts/url_safety.py
scripts/validate_backlink_report.py
scripts/verify_backlinks.py
scripts/verify_release.py
scripts/youtube_search.py
skills/seo-audit/LICENSE.txt
skills/seo-audit/SKILL.md
skills/seo-backlinks/LICENSE.txt
skills/seo-backlinks/SKILL.md
skills/seo-cluster/SKILL.md
skills/seo-cluster/references/execution-workflow.md
skills/seo-cluster/references/hub-spoke-architecture.md
skills/seo-cluster/references/serp-overlap-methodology.md
skills/seo-cluster/templates/cluster-map.html
skills/seo-competitor-pages/LICENSE.txt
skills/seo-competitor-pages/SKILL.md
skills/seo-content-brief/LICENSE.txt
skills/seo-content-brief/SKILL.md
skills/seo-content-brief/references/excluded-domains.md
skills/seo-content-brief/references/keyword-density.md
skills/seo-content-brief/references/page-type-templates.md
skills/seo-content/LICENSE.txt
skills/seo-content/SKILL.md
skills/seo-dataforseo/LICENSE.txt
skills/seo-dataforseo/SKILL.md
skills/seo-dataforseo/references/cost-tiers.md
skills/seo-dataforseo/references/tool-catalog.md
skills/seo-drift/SKILL.md
skills/seo-drift/references/comparison-rules.md
skills/seo-ecommerce/SKILL.md
skills/seo-ecommerce/references/marketplace-endpoints.md
skills/seo-ecommerce/references/ucp-universal-commerce-protocol.md
skills/seo-flow/SKILL.md
skills/seo-flow/references/bibliography.md
skills/seo-flow/references/flow-framework.md
skills/seo-flow/references/flow-prompts.lock
skills/seo-flow/references/prompts/README.md
skills/seo-flow/references/prompts/find/content-planning-for-topical-relevance-prompt.md
skills/seo-flow/references/prompts/find/content-prioritization-prompt.md
skills/seo-flow/references/prompts/find/keyword-research-prompt.md
skills/seo-flow/references/prompts/find/keyword-variations-for-topical-relevance-prompt.md
skills/seo-flow/references/prompts/find/prompt-audience-avatar.md
skills/seo-flow/references/prompts/leverage/backlink-competition-prompt.md
skills/seo-flow/references/prompts/local/ai-homepage-rewrite-prompt.md
skills/seo-flow/references/prompts/local/claude-deep-research-prompt.md
skills/seo-flow/references/prompts/local/gbp-categories-prompt.md
skills/seo-flow/references/prompts/local/gbp-description-claude-prompt-1.md
skills/seo-flow/references/prompts/local/gbp-description-claude-prompt-2.md
skills/seo-flow/references/prompts/local/gbp-description-claude-prompt-3.md
skills/seo-flow/references/prompts/local/gbp-services-prompt.md
skills/seo-flow/references/prompts/local/prompt-generating-a-meta-description.md
skills/seo-flow/references/prompts/local/prompt-generating-a-title-tag.md
skills/seo-flow/references/prompts/local/prompt-rewriting-existing-homepage.md
skills/seo-flow/references/prompts/local/prompt-rewriting-existing-service-page.md
skills/seo-flow/references/prompts/optimize/ai-detector-test-follow-up-prompt.md
skills/seo-flow/references/prompts/optimize/ai-supporting-pages-rewrite-prompt.md
skills/seo-flow/references/prompts/optimize/basic-prompt.md
skills/seo-flow/references/prompts/optimize/blog-post-outline-prompt.md
skills/seo-flow/references/prompts/optimize/blog-post-writing-prompt.md
skills/seo-flow/references/prompts/optimize/claude-prompt-1.md
skills/seo-flow/references/prompts/optimize/claude-prompt-2.md
skills/seo-flow/references/prompts/optimize/ctr-audit-prompt.md
skills/seo-flow/references/prompts/optimize/follow-up-prompt-1.md
skills/seo-flow/references/prompts/optimize/follow-up-prompt-2.md
skills/seo-flow/references/prompts/optimize/follow-up-prompt.md
skills/seo-flow/references/prompts/optimize/paa-question-rewording-prompt.md
skills/seo-flow/references/prompts/optimize/prompt-core-30-content-audit.md
skills/seo-flow/references/prompts/optimize/property-content-with-authority-audit-prompt.md
skills/seo-flow/references/prompts/optimize/reddit-claude-prompt.md
skills/seo-flow/references/prompts/optimize/schema-prompt-1.md
skills/seo-flow/references/prompts/optimize/step-1-the-chatgpt-discovery-prompt.md
skills/seo-flow/references/prompts/optimize/step-2-the-follow-up-qualifying-prompt.md
skills/seo-flow/references/prompts/optimize/technical-audit-prompt.md
skills/seo-flow/references/prompts/optimize/visibility-follow-up-prompt.md
skills/seo-flow/references/prompts/optimize/visiblity-prompt.md
skills/seo-flow/references/prompts/win/bofu-page-brief-generator.md
skills/seo-flow/references/prompts/win/conversion-audit-prompt.md
skills/seo-flow/references/prompts/win/dual-surface-content-scorecard.md
skills/seo-geo/LICENSE.txt
skills/seo-geo/SKILL.md
skills/seo-geo/references/google-ai-optimization-guide.md
skills/seo-geo/references/llmstxt-evidence.md
skills/seo-google/LICENSE.txt
skills/seo-google/SKILL.md
skills/seo-google/assets/templates/cwv-audit-report.md
skills/seo-google/assets/templates/gsc-performance-report.md
skills/seo-google/assets/templates/indexation-status-report.md
skills/seo-google/references/auth-setup.md
skills/seo-google/references/dma-consent-mode-v2.md
skills/seo-google/references/ga4-data-api.md
skills/seo-google/references/indexing-api.md
skills/seo-google/references/keyword-planner-api.md
skills/seo-google/references/nlp-api.md
skills/seo-google/references/pagespeed-crux-api.md
skills/seo-google/references/rate-limits-quotas.md
skills/seo-google/references/search-console-api.md
skills/seo-google/references/supplementary-apis.md
skills/seo-google/references/youtube-api.md
skills/seo-hreflang/LICENSE.txt
skills/seo-hreflang/SKILL.md
skills/seo-hreflang/references/content-parity.md
skills/seo-hreflang/references/cultural-profiles.md
skills/seo-hreflang/references/locale-formats.md
skills/seo-hreflang/references/machine-translation-qa.md
skills/seo-image-gen/LICENSE.txt
skills/seo-image-gen/SKILL.md
skills/seo-image-gen/references/cost-tracking.md
skills/seo-image-gen/references/gemini-models.md
skills/seo-image-gen/references/mcp-tools.md
skills/seo-image-gen/references/post-processing.md
skills/seo-image-gen/references/presets.md
skills/seo-image-gen/references/prompt-engineering.md
skills/seo-image-gen/references/seo-image-presets.md
skills/seo-images/LICENSE.txt
skills/seo-images/SKILL.md
skills/seo-local/LICENSE.txt
skills/seo-local/SKILL.md
skills/seo-maps/LICENSE.txt
skills/seo-maps/SKILL.md
skills/seo-page/LICENSE.txt
skills/seo-page/SKILL.md
skills/seo-plan/LICENSE.txt
skills/seo-plan/SKILL.md
skills/seo-plan/assets/agency.md
skills/seo-plan/assets/ecommerce.md
skills/seo-plan/assets/generic.md
skills/seo-plan/assets/local-service.md
skills/seo-plan/assets/publisher.md
skills/seo-plan/assets/saas.md
skills/seo-programmatic/LICENSE.txt
skills/seo-programmatic/SKILL.md
skills/seo-schema/LICENSE.txt
skills/seo-schema/SKILL.md
skills/seo-schema/references/deprecated-types-2024-2026.md
skills/seo-sitemap/LICENSE.txt
skills/seo-sitemap/SKILL.md
skills/seo-sxo/SKILL.md
skills/seo-sxo/references/page-type-taxonomy.md
skills/seo-sxo/references/persona-scoring.md
skills/seo-sxo/references/user-story-framework.md
skills/seo-sxo/references/wireframe-templates.md
skills/seo-technical/LICENSE.txt
skills/seo-technical/SKILL.md
skills/seo-technical/references/agent-friendly-pages.md
skills/seo/LICENSE.txt
skills/seo/SKILL.md
skills/seo/references/backlink-quality.md
skills/seo/references/cwv-thresholds.md
skills/seo/references/eeat-framework.md
skills/seo/references/free-backlink-sources.md
skills/seo/references/local-schema-types.md
skills/seo/references/local-seo-signals.md
skills/seo/references/maps-api-endpoints.md
skills/seo/references/maps-free-apis.md
skills/seo/references/maps-gbp-checklist.md
skills/seo/references/maps-geo-grid.md
skills/seo/references/quality-gates.md
skills/seo/references/schema-types.md
skills/seo/references/thinking-framework.md
tests/test_audit_instructions.py
tests/test_banana_api_key_safety.py
tests/test_content_quality.py
tests/test_cross_platform_hooks.py
tests/test_drift_portability.py
tests/test_extension_installer_injection.py
tests/test_fetch_page_decoding.py
tests/test_gbp_lint_and_polish.py
tests/test_google_api_key_safety.py
tests/test_google_report_full_audit.py
tests/test_gsc_query.py
tests/test_gsc_totals_aggregate.py
tests/test_lazy_detection.py
tests/test_manifest_consistency.py
tests/test_moz_api.py
tests/test_nlp_analyze.py
tests/test_parasite_risk_and_extensions.py
tests/test_phase_j_executable.py
tests/test_portability.py
tests/test_pyproject_metadata.py
tests/test_render_page.py
tests/test_schema_hook_policy.py
tests/test_schema_v2.py
tests/test_sync_flow.py
tests/test_technical_depth.py
tests/test_url_safety.py
uninstall.ps1
uninstall.sh
```

## File: README.md

Excerpt: first 360 of 491 lines.

```markdown
![Claude SEO cover: a Claude Code command palette with /seo audit, schema, geo, content, and backlinks commands over a dark CRT panel](assets/cover.svg)

# Claude SEO: SEO Skill for Claude Code

**Claude SEO is an open-source SEO analysis plugin for [Claude Code](https://claude.ai/claude-code).** It runs 25 sub-skills and 18 specialist agents in parallel across technical SEO, content quality (E-E-A-T), Schema.org markup, AI search optimization (GEO), local SEO, e-commerce, and international SEO. Every audit produces a prioritized action plan with falsifiable recommendations grounded in primary-source guidance from Google.

[![CI](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml/badge.svg)](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-seo)](https://github.com/AgriciDaniel/claude-seo/releases)
[![Tests](https://img.shields.io/badge/tests-326%20passing-brightgreen)](tests/)
[![Community](https://img.shields.io/badge/AI%20Marketing%20Hub-Pro%20community-purple)](https://www.skool.com/ai-marketing-hub-pro)

> **Two versions of this skill.**
> - 🌐 **Public open-source** → [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo): MIT, public releases, no membership. Use this if you want stable + downloadable.
> - 🔒 **Community private mirror** → [`AI-Marketing-Hub/claude-seo`](https://github.com/AI-Marketing-Hub/claude-seo): early access to upcoming features and direct collaboration with the [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) community. Requires membership.

### Why Claude SEO

- **AI-search first.** Aligned with [Google's AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). Question-based citability scoring, primary-source evidence on llms.txt, IPTC `TrainedAlgorithmicMedia` for AI-generated product images, agent-friendly page checks per [web.dev](https://web.dev/).
- **Parallel execution.** Full site audits spawn up to 15 specialist agents simultaneously. Site-level audits complete in minutes rather than hours.
- **Falsifiable, not promotional.** Every recommendation carries the first-principle observation it rests on, its dependency relationships, an explicit "how would we know this failed?" check, and a leading indicator. See [Methodology](#methodology).

### Real results

![Google Search Console clicks and impressions for a three-month-old site climbing from launch to steady organic growth between 23 March and 12 June 2026](assets/growth-3-months.png)

Google Search Console for a site started 23 March 2026 and run on this workflow: total clicks and impressions across its first three months, through 12 June 2026.

> Using Codex instead of Claude Code? Use [Codex SEO](https://github.com/AgriciDaniel/codex-seo), the Codex-first port with TOML agents, plugin packaging, deterministic runners, and the same SEO workflow surface.

## Who this is for

- **SEO agencies running 5+ client sites.** Replace quarterly deep audits with weekly automated runs. Same team capacity, 4× audit cadence, every recommendation comes with a falsifiability check the client can verify.
- **In-house SEO leads at SaaS / publisher / e-commerce companies.** Second-pair-of-eyes before executive reviews. Catches what GSC and Lighthouse hide: schema deprecation, AI-citability gaps, expired-domain heritage risk, parasite-SEO exposure, machine-translation drift.
- **Freelance SEO consultants.** Anchor day-one client scope with a 15-minute audit and a real 0-100 score. Win the engagement with concrete proof of value before you spend an hour writing the proposal.

![Claude SEO /seo command demo in Claude Code terminal](screenshots/seo-command-demo.gif)

Run a full audit and watch parallel agents fan out across the site:

![Claude SEO /seo audit demo: parallel subagents producing a prioritized action plan](screenshots/seo-audit-demo.gif)

[Watch the full demo on YouTube](https://www.youtube.com/watch?v=COMnNlUakQk)

## Table of Contents

- [Who this is for](#who-this-is-for)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [Features](#features)
- [Compared to manual / agency / commercial tools](#compared-to-manual--agency--commercial-tools)
- [Use cases](#use-cases)
- [Sample Output](#sample-output)
- [Architecture](#architecture)
- [Methodology](#methodology)
- [What's New in v2](#whats-new-in-v2)
- [Limitations](#limitations)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Extensions](#extensions)
- [Ecosystem](#ecosystem)
- [Documentation](#documentation)
- [FAQ](#faq)
- [Community Contributors](#community-contributors)
- [License](#license)
- [Contributing](#contributing)
- [Author](#author)

## Installation

> ℹ️ **Which version are you installing?**
>
> - **Public open-source (default).** The commands below install from [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) — MIT, public releases, no membership required.
> - **AI Marketing Hub Pro member?** Install the community version with early access instead: swap `AgriciDaniel/claude-seo` for `AI-Marketing-Hub/claude-seo` and the plugin slug `claude-seo@agricidaniel-claude-seo` for `claude-seo@ai-marketing-hub-claude-seo`. Requires `gh auth login` (or PAT) with access to the `AI-Marketing-Hub` org. If `/plugin marketplace add` 404s, DM in the [Skool community](https://www.skool.com/ai-marketing-hub-pro) to get added.

### Plugin Install (Claude Code 1.0.33+)

The fastest path. One-time marketplace add, then plugin install:

``\`bash
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
``\`

### Manual Install (Unix / macOS / Linux)

``\`bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
``\`

<details>
<summary>One-liner (curl, review then run)</summary>

``\`bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh > install.sh
cat install.sh        # review before running
bash install.sh
rm install.sh
``\`

</details>

### Windows (PowerShell)

``\`powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
``\`

> **Why `git clone` instead of `irm | iex`?** Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk: downloading and executing remote code without verification. The `git clone` approach lets you inspect `claude-seo\install.ps1` before running it.

## Quick Start

``\`bash
# Start Claude Code
claude

# Full site audit: parallel sub-agents produce a prioritized action plan
/seo audit https://example.com

# Deep single-page analysis: on-page elements, content quality, schema
/seo page https://example.com/about

# Schema markup audit: detect, validate, generate
/seo schema https://example.com

# AI search optimization: passage citability + primary-source-aligned recommendations
/seo geo https://example.com

# Generate a sitemap with industry templates
/seo sitemap generate
``\`

## Commands

![Claude SEO sub-skill ecosystem: 25 modules grouped into 8 categories (audit, content, schema, technical, AI search, local + maps, commerce + intl, extensions) around the central orchestrator](assets/sub-skills.svg)

25 user-invocable `/seo` commands across the orchestrator and its sub-skills. Full reference in [docs/COMMANDS.md](docs/COMMANDS.md).

| Command | Description |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel sub-agent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo technical <url>` | Technical SEO audit across 9 categories |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo content-brief <topic>` | Detailed content brief: target keywords, outline, internal links |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo sitemap <url \| generate>` | Analyze or generate XML sitemaps |
| `/seo images <url>` | Image optimization analysis |
| `/seo plan <type>` | Strategic SEO planning (saas, local, ecommerce, publisher, agency) |
| `/seo programmatic <url>` | Programmatic SEO analysis and planning |
| `/seo competitor-pages <url>` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang <url>` | Hreflang / i18n SEO audit and generation |
| `/seo google [command]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4, PDF reports) |
| `/seo backlinks <url>` | Backlink profile analysis (Moz, Bing, Common Crawl) |
| `/seo cluster <keyword>` | SERP-based semantic clustering |
| `/seo sxo <url>` | Search Experience Optimization (page-type, user stories, personas) |
| `/seo drift baseline \| compare \| history <url>` | SEO drift monitoring with SQLite snapshots |
| `/seo ecommerce <url>` | E-commerce SEO and marketplace intelligence |
| `/seo flow [stage]` | FLOW framework prompts (CC BY 4.0, evidence-led) |
| `/seo firecrawl [command] <url>` | Full-site crawling (extension) |
| `/seo dataforseo [command]` | Live SEO data (extension) |
| `/seo image-gen [use-case]` | AI image generation for SEO assets (extension) |

## Features

### What Core Web Vitals does Claude SEO check?

Claude SEO measures the current three Core Web Vitals: **LCP** (Largest Contentful Paint, target under 2.5s), **INP** (Interaction to Next Paint, target under 200ms), and **CLS** (Cumulative Layout Shift, target under 0.1). [INP replaced FID](https://web.dev/articles/inp) on March 12, 2024; FID was removed from all Chrome tools (CrUX API, PageSpeed Insights, Lighthouse) on September 9, 2024, and Claude SEO never references FID. Field data comes from the Chrome User Experience Report (CrUX) when available; lab data falls back to Lighthouse via PageSpeed Insights. LCP can be decomposed into subparts (TTFB, load delay, load duration, render delay) via the `/seo google` CrUX integration to localize bottlenecks. Mobile and desktop are measured separately. CrUX History (25-week trend) is included in the Tier 0 free credential set.

### How does Claude SEO assess E-E-A-T?

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is evaluated against the Search Quality Rater Guidelines, last updated September 2025 with YMYL expanded to include political and social topics. Experience signals: original research, case studies, first-hand photos. Expertise: author credentials and topical depth. Authoritativeness: external citations and brand mentions. Trustworthiness, the most heavily weighted of the four: contact info, secure HTTPS, transparent corrections, date stamps. Before scoring sub-factors, Claude SEO applies Google's own Who / How / Why heuristic from the [helpful-content guide](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Generative AI content is fine if it meets Search Essentials; it crosses into spam when used to scale low-value pages, which `seo-content humanize` and `seo-content verify` are designed to detect.

### What Schema.org types does Claude SEO support?

JSON-LD is the preferred format (Google's stated preference). Active types Claude SEO detects, validates, and generates: Organization, LocalBusiness, Article, BlogPosting, NewsArticle, Product, ProductGroup, Offer, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting, Reservation, OrderAction, plus video and specialized types (BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode). FAQPage: Google stopped showing FAQ rich results for all sites on May 7, 2026; still useful as a supporting AI/entity signal, not for rich results. Deprecated and never recommended: HowTo (rich results removed September 2023), SpecialAnnouncement (July 2025), ClaimReview, VehicleListing, EstimatedSalary, LearningVideo, CourseInfo carousel (all retired June 2025). Replacement guidance: [skills/seo-schema/references/deprecated-types-2024-2026.md](skills/seo-schema/references/deprecated-types-2024-2026.md).

### How does Claude SEO optimize for AI search?

Aligned with [Google's AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), which states that "AEO" and "GEO" are rebranded labels for SEO. AI Overviews and AI Mode are grounded in the same ranking systems as classic Search; pages must be indexed and eligible for snippet display to appear in any AI feature. Claude SEO scores passage citability (optimal 134-167 word self-contained answer blocks), question-based heading hierarchy, attribution density, structured data coverage, and entity presence across Wikipedia, Reddit, YouTube, and LinkedIn. The `seo-geo` skill includes evidence-based reframes of three popular myths: llms.txt is not currently a citation lever ([primary-source evidence](skills/seo-geo/references/llmstxt-evidence.md)), content chunking is not required, and AI-specific keyword rewriting is unnecessary because synonym understanding is sufficient.

### Which Google SEO APIs does Claude SEO integrate with?

A 4-tier credential system lets you start with zero keys and add data as needed. Every tier delivers real value at its level:

| Tier | Credentials | APIs Unlocked |
|------|------|------|
| 0 | API key | PageSpeed Insights, CrUX, CrUX History (25-week trends) |
| 1 | + OAuth or Service Account | + Search Console (queries, URL Inspection, sitemap status), Indexing API |
| 2 | + GA4 property config | + GA4 organic traffic, top landing pages, device / country breakdown |
| 3 | + Ads developer token | + Keyword Planner search volume and competition data |

PDF reports are generated via [WeasyPrint](https://weasyprint.org/) (A4 layout) with matplotlib charts at 200 DPI. Run `/seo google setup` for the credential wizard. All credentials live under `~/.config/claude-seo/` with `0o600` permissions; nothing is checked into the repo.

### How does Claude SEO handle local SEO?

Three layers. **Google Business Profile signals**: categories, hours, photos, posts, products, attributes. **NAP consistency** across citations: name, address, phone matched against major directories with deviation flagging. **Review intelligence**: rating trends, sentiment, response coverage. For multi-location businesses, Claude SEO enforces a 30-page warning threshold and a 50-page hard stop to prevent doorway-page violations (configurable). The `/seo maps` workflow adds geo-grid rank tracking, GBP profile auditing, and competitor radius mapping. Local schema generation covers `LocalBusiness` with all required and recommended properties (geo coordinates, opening hours, areaServed). Phase F (v2) added a GBP deprecation linter that detects retired chat-field references and `.business.site` URLs.

## Compared to manual / agency / commercial tools

| | Manual audit | Agency engagement | Commercial SEO audit tool | **Claude SEO** |
|---|---|---|---|---|
| **Time per audit** | 4-8 hrs senior SEO time | 1-3 weeks turnaround | 10-45 min crawl + report | **10-15 min** |
| **Cost** | High (billable hours) | $2k-$15k+ project | $99-$999/mo subscription | **Free skill + Claude Code subscription** |
| **Repeatable** | Inconsistent across analysts | Inconsistent across engagements | Yes | **Yes, deterministic + scriptable** |
| **Output format** | Wall-of-findings PDF | Branded slide deck | Web dashboard, CSV exports | **Markdown + PDF + JSON, local files** |
| **Custom benchmarks** | Manual per analyst | Agency-specific frameworks | Vendor-fixed | **Edit local SKILL.md** |
| **Data leaves machine?** | No (your spreadsheet) | Yes (sent to agency) | Yes (uploaded to vendor) | **No, fully local by default** |
| **Lock-in** | None | High | High (data-exit friction) | **None. MIT, your files.** |
| **AI search awareness** | Depends on analyst | Depends on agency seniority | Lagging (typically 6-12 mo behind) | **Google AI Optimization Guide (May 2026), Sept 2025 QRG, INP-not-FID, GEO/AEO=SEO reframe, llms.txt evidence-based posture** |
| **Falsifiability per finding** | No | No | No | **Yes. Every recommendation carries a "how would we know this failed?" check + leading indicator** |

> Cost benchmarks: manual audit assumes a senior SEO consultant at typical agency billable rates; agency engagement based on common discovery/audit deliverable scopes; commercial-tool subscriptions reflect published mid-tier pricing across the SEO audit category (Ahrefs, Semrush, Sitebulb, Screaming Frog). Your numbers may differ.

## Use cases

**SEO agency lead running 10 client sites.** Replaces the quarterly "deep audit" ritual with a weekly Monday-morning `/seo audit` run per site. Time to deliver a client health-score email drops from 4 hours to 12 minutes; coverage goes from quarterly to weekly without billing more hours. The drift baseline catches regressions between audits so the client conversation moves from "look at this snapshot" to "here is what changed this week."

**In-house SEO lead at a 50-person SaaS company.** Runs `/seo audit` 24 hours before each quarterly business review. Catches the items the platform UI buries (broken canonical chains on programmatic pages, schema deprecation after Google's June 2025 retirement wave, AI-citability gaps that erode SERP-to-AI-Overview pickup, expired-domain heritage on acquired blog assets) before the CMO asks why organic traffic is down in front of the board.

**Freelance SEO consultant onboarding a new client.** Runs `/seo audit` on the discovery call. Anchors the engagement scope with a real 0-100 score, 3 prioritized critical findings, and a falsifiability check on each recommendation, instead of a vague "I'll take a look and get back to you." Closes more retainers because the proof of value happens during the call, not after the proposal.

## Sample Output

Claude SEO writes real markdown reports as its primary deliverable. Below is the first ~50 lines of a `/seo schema https://rankenstein.pro/about` audit verbatim. The actual structure, headers, and grading format the plugin produces follows.

<details>
<summary><code>SCHEMA-REPORT.md</code>: first 50 lines of a real audit</summary>

``\`markdown
# Schema Markup Report: rankenstein.pro/about

**URL:** https://rankenstein.pro/about
**Date:** 2026-02-09
**Format Detected:** JSON-LD (3 blocks) | No Microdata | No RDFa

---

## Summary

| Metric | Value |
|--------|-------|
| **JSON-LD Blocks** | 3 |
| **Schema Types** | Organization, WebSite, SoftwareApplication |
| **Critical Issues** | 2 |
| **Warnings** | 5 |
| **Passed Checks** | 18 |
| **Overall Grade** | B+ (solid foundation, actionable gaps) |

---

## Existing Schema Validation

### 1. Organization (`@id: #organization`)

| Property | Value | Status | Notes |
|----------|-------|--------|-------|
| `@context` | https://schema.org | Valid | |
| `@type` | Organization | Valid | Active type |
| `@id` | https://rankenstein.pro#organization | Good | Enables cross-referencing |
| `name` | Rankenstein | Valid | |
| `description` | Present, 200+ chars | Good | Descriptive and keyword-rich |
| `url` | https://rankenstein.pro | Valid | Absolute URL |
| `logo` | ImageObject with @id, url, width, height, caption | Excellent | Well-structured |
| `foundingDate` | "2024" | Imprecise | Year-only accepted but ISO 8601 preferred |
| `areaServed` | "Worldwide" | Text | Works but `GeoShape` is more semantic |
| `contactPoint` | email + contactType | Valid | Consider adding `telephone` |
| `founder` | 1 Person (Daniel Agrici) | Incomplete | Page describes two co-founders; second missing |
| `sameAs` | 5 social profiles | Good | GitHub, X, LinkedIn, YouTube, Reddit |
| `knowsAbout` | 6 topics | Good | Relevant topical signals |

**Critical Issue:** The `founder` property only includes Daniel Agrici. Benjamin Samar (Co-Founder & Technical Director) is displayed on the page but absent from the schema. This creates a content-schema mismatch that can confuse search engines.
``\`

</details>

Other audit outputs follow the same shape: `FULL-AUDIT-REPORT.md` (umbrella audit), `GEO-ANALYSIS.md` (AI-search readiness), `LOCAL-SEO-ANALYSIS.md` (GBP and citations), and a production PDF via WeasyPrint + matplotlib (cover, TOC, executive summary, data sections, recommendations, methodology, roughly 32 A4 pages for a full site audit).

## Architecture

![Claude SEO audit signal flow: /seo audit enters the orchestrator, fans out to 25 sub-skills and 6 parallel audit agents, and converges through the scoring engine into a prioritized report](assets/signal-flow.svg)

The plugin follows the [Agent Skills standard](https://docs.claude.com/en/docs/claude-code/skills) with a 3-layer architecture (directive, orchestration, execution). Skills and agents are auto-discovered from `skills/seo-*/` and `agents/seo-*.md`. The orchestrator (`skills/seo/SKILL.md`) handles industry detection (SaaS, local, ecommerce, publisher, agency), parallel sub-agent dispatch up to 15 simultaneously, and synthesis through the [10-principle framework](#methodology) before emitting the action plan. Full architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Methodology

![Claude SEO 10-principle methodology: PERCEIVE, ANALYZE, VALIDATE, and ACT phases with 10 principles arranged by quadrant](assets/framework.svg)

Every audit walks 10 principles grouped into four phases. Each emitted recommendation carries four fields: the first-principle observation it rests on, its dependency relationship to other recommendations, a "how would we know this failed?" check, and a leading indicator to monitor.

| Phase | Principles | What it does |
|---|---|---|
| **PERCEIVE** | OBSERVE (external) · OBSERVE (internal) · LISTEN | Collect raw signals; audit your own assumptions; read what the SERP, the brand voice, and the community actually say |
| **ANALYZE** | THINK · CONNECT (lateral) · CONNECT (system) | Reduce to first principles; find non-obvious cross-skill links; sequence into a dependency graph |
| **VALIDATE** | FEEL · ACCEPT | Pressure-test against UX, brand voice, operator capacity; surface falsifiability |
| **ACT** | CREATE · GROW | Ship the artifact; set the feedback loop for the next audit |

Full methodology: [skills/seo/references/thinking-framework.md](skills/seo/references/thinking-framework.md).

## What's New in v2

v2.0.0 is the largest release in the plugin's history. Six build phases, all shipped:

- **Phase A: Headless rendering everywhere.** Shared `scripts/render_page.py` with Playwright Chromium plus [trafilatura](https://github.com/adbar/trafilatura) and [htmldate](https://github.com/adbar/htmldate). Every audit subagent gets SPA-aware fetching via `--render auto` (auto-detected on Next.js, React, Vue, Nuxt, Astro islands). Closes the SPA limitation that capped v1.x.
- **Phase B: QRG-aligned content quality gates.** Filler detector and AI-pattern humanizer keyed to QRG §4.6.5 and §4.6.6, claim-verification scanner, expired-domain heritage check via WHOIS, primary-source Google updates changelog.
- **Phase C: Technical and CWV depth.** LCP subparts via CrUX (TTFB, load delay, load duration, render delay), Speculation Rules and bfcache detection, IndexNow submitter for Bing / Yandex / Seznam / Naver, Unlighthouse multi-page Lighthouse wrapper.
- **Phase D: Schema completeness.** Four explicit generators (Reservation, OrderAction, DiscussionForumPosting, ProfilePage), e-commerce schema validator (`hasMerchantReturnPolicy`, `shippingDetails`, `MemberProgram`, EU `energyEfficiencyClass`, ProductGroup variants), dual validator (Rich Results Test plus Schema Markup Validator).
- **Phase E: AI search reframing and 5 new MCP extensions.** Ahrefs, SE Ranking (AI Share-of-Voice), Profound (LLM citation tracker), Bing Webmaster plus IndexNow, Unlighthouse. Plus the parasite-SEO risk scanner per Google's November 2024 [site reputation abuse policy](https://developers.google.com/search/blog/2024/11/site-reputation-abuse-update).
- **Phase F: Local, international, and privacy polish.** Google Business Profile deprecation linter (chat field, `.business.site` URLs, Q&A), DMA consent-mode-v2 click-through diagnostic, machine-translation QA flag per January 2025 QRG.

Test coverage: 248 → 271 (a 5.4× increase over the v1.9.9 baseline). 83 SSRF and DNS-rebinding bypass tests close the full obfuscated-IPv4, FQDN-trailing-dot, and redirect-rebinding bypass classes. Full migration notes and breaking changes: [docs/MIGRATION-v1-to-v2.md](docs/MIGRATION-v1-to-v2.md).

## Limitations

Two real boundaries worth being upfront about.

**Heavy client-side hydration timing.** Phase A's headless renderer handles most SPAs out of the box (`--render auto` detects empty `<div id="root">` shells and switches to Playwright). Edge cases that still produce noisy findings: pages with hydration tied to scroll position past the fold, pages that fetch critical content after user interaction (modal opens, tab clicks), pages with race-condition-prone third-party widget mounts. For these, manually triggering the `seo-visual` subagent and comparing its Playwright snapshot to the raw-HTML subagents' findings is the recommended workflow.

**Local-only without enrichment.** The free tier does not call any external API and produces zero-network output. Adding Google API credentials (Tier 0 through 3) unlocks real field data and live indexation status; without them, Core Web Vitals are lab estimates only and indexation is inferred from page-level signals. Adding MCP extensions (Ahrefs, DataForSEO, SE Ranking, Profound) similarly unlocks competitive and AI-citation data but requires their respective accounts.

## Requirements

- Python 3.10+
- Claude Code CLI
- Optional: Playwright Chromium (auto-installed by `install.sh`) for SPA rendering and screenshots
- Optional: Google API credentials for enriched CWV / GSC / GA4 data (see `/seo google setup`)

## Uninstall

``\`bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/uninstall.sh
``\`

<details>
<summary>One-liner (curl)</summary>

``\`bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash
``\`

</details>

## Extensions

Optional MCP servers add live data to the audit pipeline. Claude SEO ships extensions for 8 servers; the plugin core works without any of them.

### DataForSEO

Live SERP data, keyword research, backlinks, on-page analysis, content analysis, business listings, AI visibility checks, and LLM mention tracking. 22 commands across 9 API modules.

``\`bash
./extensions/dataforseo/install.sh   # requires DataForSEO account
```

## File: AGENTS.md

Excerpt: first 160 of 174 lines.

```markdown
# Claude SEO: Multi-Platform Agent Instructions

> For **Cursor**, **Cursor Cloud Agents**, **Google Antigravity**, **Gemini CLI**,
> **OpenAI Codex CLI**, **Cline**, **Aider**, and any other agent harness that
> reads project-root agent instructions.
>
> Claude Code users: see `CLAUDE.md` instead.

## Cross-platform portability (v2.0.0)

Every skill in `skills/*/SKILL.md` is authored to a portable subset of the
Claude Code skill spec. Validate compatibility with your harness via:

``\`bash
python3 scripts/portability_check.py
``\`

The check confirms each `SKILL.md` has the minimum frontmatter every harness
expects (`name`, `description`, optional `model`, optional `tools`) and warns
on Claude-Code-specific features (`maxTurns`, multi-line tool list with
descriptive comments) that other harnesses may ignore but do not reject.

### Per-harness notes

| Harness | How to load claude-seo |
|---|---|
| **Cursor** | Symlink or copy `skills/` and `agents/` into `.cursor/rules/`. Commands are invoked as text prompts; the harness reads `SKILL.md` body as system context. |
| **Cursor Cloud Agents** | Push the repo; Cloud Agents read `AGENTS.md` automatically at session start. |
| **Google Antigravity** | Point the workspace at this repo root; Antigravity reads `AGENTS.md` first, falls back to `skills/`. |
| **Gemini CLI** | `gemini init` in this repo loads `AGENTS.md`. Skills are activated via `activate_skill <name>` in conversation. |
| **OpenAI Codex CLI** | Reads `AGENTS.md` from project root. Bash tools work as documented; some Claude-specific tool names (Read/Write/Edit) are aliased to Codex equivalents transparently. |
| **Cline** | Loads `AGENTS.md` from project root. Skills appear as system messages; subagent delegation falls back to in-context expansion. |
| **Aider** | Reads `AGENTS.md` if present; otherwise falls back to README. Aider does not support sub-agent dispatch; the seo-* skills run inline. |

### Tool-name compatibility

Where claude-seo skills mention Claude Code tools (`Read`, `Write`, `Edit`,
`Bash`, `Glob`, `Grep`, `WebFetch`), each harness typically has an equivalent:

| Claude Code | Codex | Cline | Aider | Cursor / Antigravity |
|---|---|---|---|---|
| Read       | read_file        | read_file       | (inline)        | read |
| Write      | write_file       | write_file      | /add then edit  | write |
| Edit       | apply_diff       | replace_in_file | /edit           | edit |
| Bash       | bash             | execute_command | /run            | shell |
| Glob       | glob             | search_files    | (inline)        | find |
| Grep       | grep             | search_files    | /grep           | grep |
| WebFetch   | fetch / browse   | (browser tool)  | (n/a)           | fetch |

These mappings are automatic in most harnesses; we list them for transparency
in case a recipe needs a specific call.

## Overview

Claude SEO is a Tier 4 SEO analysis skill with 25 sub-skills (21 core + 1 orchestrator +
1 framework integration + 2 extension mirrors), 18 sub-agents (15 core + 1 framework
integration + 2 extension mirrors), and 50 Python execution scripts.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel subagent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo schema <url>` | Schema.org detection, validation, generation |
| `/seo sitemap <url>` | XML sitemap analysis or generation |
| `/seo images <url>` | Image SEO: on-page audit, SERP analysis, file optimization |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <type>` | Strategic SEO planning |
| `/seo cluster <keyword>` | SERP-based semantic clustering and content architecture |
| `/seo sxo <url>` | Search Experience Optimization: page-type analysis, personas |
| `/seo drift baseline <url>` | Capture SEO baseline for change monitoring |
| `/seo drift compare <url>` | Compare current state to stored baseline |
| `/seo drift history <url>` | Show drift history over time |
| `/seo ecommerce <url>` | E-commerce SEO: product schema, marketplace intelligence |
| `/seo programmatic [url]` | Programmatic SEO at scale |
| `/seo competitor-pages [url]` | Competitor comparison pages |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews) |
| `/seo maps [cmd] [args]` | Maps intelligence (geo-grid, GBP audit, competitors) |
| `/seo hreflang <url>` | Hreflang/i18n SEO audit, cultural profiles, content parity |
| `/seo google [cmd] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |
| `/seo backlinks <url>` | Backlink profile analysis |
| `/seo backlinks setup` | Setup free backlink APIs |
| `/seo backlinks verify <url>` | Verify known backlinks still exist |
| `/seo dataforseo [cmd]` | Live SEO data via DataForSEO (extension) |
| `/seo image-gen [use-case]` | AI image generation for SEO assets (extension) |
| `/seo firecrawl [cmd] <url>` | Full-site crawling and site mapping (extension) |

## Using with Cursor / Cursor Cloud

Cursor reads this file automatically. All SKILL.md files contain the full
analysis logic as natural language instructions. Python scripts in `scripts/`
provide execution capabilities.

**Running scripts directly** (Cursor doesn't have MCP):
``\`bash
# Page fetching with SSRF protection
python3 scripts/fetch_page.py https://example.com

# HTML parsing for SEO elements
python3 scripts/parse_html.py https://example.com

# PageSpeed Insights
python3 scripts/pagespeed_check.py https://example.com --json

# Drift baseline
python3 scripts/drift_baseline.py https://example.com

# DataForSEO (requires credentials)
DATAFORSEO_USERNAME=user DATAFORSEO_PASSWORD=pass python3 scripts/dataforseo_merchant.py search "keyword"
``\`

**Cursor Cloud gotchas:**
- SSL certificates may not resolve for some domains. Investigate the certificate issue rather than disabling verification.
- PATH may not include Python venv. Use full path: `~/.claude/skills/seo/.venv/bin/python`
- Screenshots save to `/tmp/` not CWD. Check absolute paths.

## Using with Google Antigravity

Antigravity discovers this project via `.claude-plugin/plugin.json`.
Place the repo in `~/.gemini/antigravity/plugins/claude-seo/` or install via:

``\`bash
bash install.sh
``\`

## Architecture

``\`
skills/                    # 25 sub-skills (auto-discovered)
  seo/SKILL.md            # Main orchestrator + routing
  seo-cluster/            # Semantic clustering (v1.9.0)
  seo-sxo/                # Search Experience Optimization (v1.9.0)
  seo-drift/              # SEO drift monitoring (v1.9.0)
  seo-ecommerce/          # E-commerce SEO (v1.9.0)
  seo-audit/              # Full site audit
  seo-page/               # Single-page analysis
  seo-technical/          # Technical SEO
  seo-content/            # E-E-A-T quality
  seo-schema/             # Schema.org markup
  seo-sitemap/            # XML sitemaps
  seo-images/             # Image optimization
  seo-geo/                # AI search / GEO
  seo-local/              # Local SEO
  seo-maps/               # Maps intelligence
  seo-plan/               # Strategic planning
  seo-hreflang/           # International SEO
  seo-google/             # Google APIs
  seo-backlinks/          # Backlink analysis
  seo-programmatic/       # Programmatic SEO
  seo-competitor-pages/   # Competitor pages
  seo-dataforseo/         # DataForSEO (extension)
  seo-image-gen/          # AI images (extension)
agents/                    # 18 subagents
scripts/                   # 50 Python scripts
schema/                    # JSON-LD templates
extensions/                # Optional add-ons (DataForSEO, Firecrawl, Banana, ASO)
``\`
```

## File: CLAUDE.md

Excerpt: first 160 of 290 lines.

```markdown
# Claude SEO: Universal SEO Analysis Skill

## Project Overview

This repository contains **Claude SEO**, a Tier 4 Claude Code skill for comprehensive
SEO analysis across all industries. It follows the Agent Skills open standard and the
3-layer architecture (directive, orchestration, execution). 25 sub-skills (21 core +
1 orchestrator + 1 framework integration + 2 extension mirrors), 18 sub-agents (15 core +
1 framework integration + 2 extension mirrors), and an extensible reference
system cover technical SEO, content quality,
schema markup, image optimization, sitemap architecture, AI search optimization,
local SEO (GBP, citations, reviews, map pack), maps intelligence, semantic topic
clustering, search experience optimization (SXO), SEO drift monitoring, e-commerce
SEO, and international SEO with cultural adaptation profiles.

## Architecture

``\`
claude-seo/
  CLAUDE.md                          # Project instructions (this file)
  CONTRIBUTORS.md                    # Community credits (Pro Hub Challenge)
  AGENTS.md                          # Multi-platform agent instructions (Cursor, Antigravity)
  .claude-plugin/
    plugin.json                    # Plugin manifest (v2.2.0)
    marketplace.json               # Marketplace catalog for distribution
  skills/                            # 25 sub-skills (auto-discovered)
    seo/                           # Main orchestrator skill
      SKILL.md                     # Entry point, routing table, core rules
      references/                  # On-demand knowledge files (12 files)
    seo-audit/SKILL.md            # Full site audit with parallel agents
    seo-page/SKILL.md            # Deep single-page analysis
    seo-technical/SKILL.md       # Technical SEO (9 categories)
    seo-content/SKILL.md         # E-E-A-T and content quality
    seo-schema/SKILL.md          # Schema.org markup detection/generation
    seo-sitemap/SKILL.md         # XML sitemap analysis/generation
    seo-images/SKILL.md          # Image optimization analysis
    seo-geo/SKILL.md             # AI search / GEO optimization
    seo-local/SKILL.md           # Local SEO (GBP, citations, reviews, map pack)
    seo-maps/SKILL.md            # Maps intelligence (geo-grid, GBP audit, reviews, competitors)
    seo-plan/SKILL.md            # Strategic SEO planning
    seo-programmatic/SKILL.md    # Programmatic SEO at scale
    seo-competitor-pages/SKILL.md # Competitor comparison pages
    seo-hreflang/SKILL.md       # International SEO / hreflang
    seo-google/                  # Google SEO APIs
      SKILL.md
      references/                # API reference files (10 files)
    seo-backlinks/SKILL.md      # Backlink profile analysis
    seo-cluster/                 # Semantic topic clustering (v1.9.0, by Lutfiya Miller)
      SKILL.md
      references/                # Clustering methodology, architecture, workflow
      templates/                 # cluster-map.html interactive visualization
    seo-sxo/                     # Search Experience Optimization (v1.9.0, by Florian Schmitz)
      SKILL.md
      references/                # Page-type taxonomy, user stories, personas, wireframes
    seo-drift/                   # SEO drift monitoring (v1.9.0, by Dan Colta)
      SKILL.md
      references/                # Comparison rules (17 rules, 3 severity levels)
    seo-ecommerce/               # E-commerce SEO (v1.9.0, by Matej Marjanovic)
      SKILL.md
      references/                # Marketplace API endpoints
    seo-dataforseo/SKILL.md     # Live SEO data via DataForSEO MCP (extension mirror)
    seo-image-gen/              # AI image generation for SEO assets (extension mirror)
      SKILL.md
      references/                # Image gen reference files (7 files)
  agents/                          # 18 subagents (auto-discovered)
    seo-technical.md             # Crawlability, indexability, security
    seo-content.md               # E-E-A-T, readability, thin content
    seo-schema.md                # Structured data validation
    seo-sitemap.md               # Sitemap quality gates
    seo-performance.md           # Core Web Vitals, page speed
    seo-visual.md                # Screenshots, mobile rendering
    seo-geo.md                   # AI crawler access, GEO, citability
    seo-local.md                 # GBP, NAP, citations, reviews, local schema
    seo-maps.md                  # Geo-grid, GBP audit, reviews, competitor radius
    seo-google.md                # Google API analyst (CrUX, GSC, GA4)
    seo-backlinks.md             # Backlink profile analyst (Moz, Bing, CC, verify)
    seo-dataforseo.md            # DataForSEO data analyst
    seo-image-gen.md             # SEO image audit analyst
    seo-cluster.md               # Semantic clustering analysis
    seo-sxo.md                   # Search experience optimization
    seo-drift.md                 # SEO drift monitoring
    seo-ecommerce.md             # E-commerce SEO analysis
  hooks/                           # Quality gate hooks
    hooks.json                   # PostToolUse schema validation
  scripts/                         # Python execution scripts (50 tracked + dev-only helpers)
    google_auth.py               # Credential management (OAuth, SA, API key, 4-tier detection)
    backlinks_auth.py            # Backlink API credential management (Moz, Bing)
    moz_api.py                   # Moz Link Explorer API (DA/PA, spam, domains, anchors)
    bing_webmaster.py            # Bing Webmaster Tools API (links, competitor comparison)
    commoncrawl_graph.py         # Common Crawl web graph parser (PageRank, in-degree)
    verify_backlinks.py          # Backlink existence verification crawler
    pagespeed_check.py           # PSI v5 + CrUX API
    crux_history.py              # CrUX History API (25-week trends)
    gsc_query.py                 # Search Console (queries, pages, sitemaps, sites)
    gsc_inspect.py               # URL Inspection (single + batch)
    indexing_notify.py           # Indexing API v3 (URL_UPDATED/URL_DELETED)
    ga4_report.py                # GA4 organic traffic reports
    google_report.py             # PDF/HTML report generator (WeasyPrint + matplotlib)
    youtube_search.py            # YouTube Data API v3
    nlp_analyze.py               # Cloud Natural Language API
    keyword_planner.py           # Google Ads Keyword Planner
    fetch_page.py                # Page fetcher with UA rotation
    parse_html.py                # HTML parser for SEO elements
    capture_screenshot.py        # Playwright screenshots
    analyze_visual.py            # Visual analysis helper
    drift_baseline.py            # SEO drift baseline capture (SQLite)
    drift_compare.py             # SEO drift comparison engine (17 rules)
    drift_report.py              # SEO drift HTML report generator
    drift_history.py             # SEO drift history query
    dataforseo_costs.py          # DataForSEO cost estimation and budget tracking
    dataforseo_merchant.py       # Google Shopping / Amazon data fetching
    dataforseo_normalize.py      # DataForSEO response normalization utility
    sync_flow.py                 # FLOW prompt library sync (GitHub API, CC BY 4.0 headers, --dry-run, --ref)
    url_safety.py                # Canonical URL/SSRF safety module (validate, DNS-pin, safe fetch)
    render_page.py               # Shared headless renderer (SPA-aware, Playwright)
    lcp_subparts.py              # LCP subparts breakdown via CrUX API
    preload_check.py             # Speculation Rules / bfcache / prerender / preload detector
    agent_ux_check.py            # Agent-friendly page auditor
    content_quality.py           # QRG-aligned content quality detector
    content_humanize.py          # AI-pattern remover (rewrites AI-typical phrasing)
    content_verify.py            # Claim extractor + citation-gap detector
    schema_generate.py           # JSON-LD generators for high-leverage v2 schema types
    schema_ecommerce_validate.py # Product schema validator (merchant-listing requirements)
    iptc_ai_label.py             # IPTC DigitalSourceType audit/injection for AI imagery
    parasite_risk.py             # Parasite-SEO risk scanner
    gbp_deprecation_lint.py      # GBP feature-deprecation linter
    domain_history.py            # Expired-domain heritage check
    seo_updates.py               # Primary-source Google updates query tool
    indexnow_submit.py           # IndexNow submitter
    ucp_check.py                 # UCP (Universal Commerce Protocol) profile auditor
    unlighthouse_run.py          # Unlighthouse CLI wrapper (site-wide Lighthouse)
    validate_backlink_report.py  # Backlink report validation
    portability_check.py         # Cross-platform portability lint for SKILL.md files
    release_sign.py              # SHA-256 manifest generator for release signing
    verify_release.py            # Verify checkout integrity against a release manifest
    mobile_analysis.py           # Mobile rendering analysis (gitignored, dev-only)
  schema/                          # Schema.org JSON-LD templates
  extensions/                      # Optional add-on install helpers
    dataforseo/                  # DataForSEO MCP install scripts
    firecrawl/                   # Firecrawl MCP install scripts
    banana/                      # Banana MCP install scripts
  docs/                            # Extended documentation
``\`

## Commands

| Command | Purpose |
|---------|---------|
| `/seo audit <url>` | Full site audit with up to 15 parallel subagents |
| `/seo page <url>` | Deep single-page analysis |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo content-brief <topic>` | Detailed SEO content brief: keywords, outline, internal links |
| `/seo schema <url>` | Schema.org detection, validation, generation |
| `/seo sitemap <url>` | XML sitemap analysis or generation |
| `/seo images <url or optimize>` | Image SEO: on-page audit, SERP analysis, file optimization |
| `/seo geo <url>` | AI search / Generative Engine Optimization |
| `/seo plan <type>` | Strategic SEO planning by industry |
| `/seo programmatic` | Programmatic SEO analysis and planning |
| `/seo competitor-pages` | Competitor comparison page generation |
```

## File: docs/ARCHITECTURE.md

Excerpt: first 220 of 276 lines.

```markdown
# Architecture

## Overview

Claude SEO follows Anthropic's official Claude Code skill specification with a modular, multi-skill architecture.

## Directory Structure

The plugin ships 25 sub-skills (21 core + 1 orchestrator + 1 framework integration + 2 extension mirrors) and 18 sub-agents (15 core + 1 framework integration + 2 extension mirrors).

``\`
~/.claude/plugins/.../claude-seo/
├── skills/
│   ├── seo/                    # Main orchestrator
│   │   ├── SKILL.md
│   │   └── references/         # On-demand reference files (12 files)
│   │
│   ├── seo-audit/              # Full site audit (parallel subagents)
│   ├── seo-page/               # Single page analysis
│   ├── seo-technical/          # Technical SEO (9 categories)
│   ├── seo-content/            # E-E-A-T and content quality
│   ├── seo-content-brief/      # Competitive content brief generation
│   ├── seo-schema/             # Schema markup detection and generation
│   ├── seo-sitemap/            # XML sitemap analysis and generation
│   ├── seo-images/             # Image optimization analysis
│   ├── seo-geo/                # AI search optimization (GEO)
│   ├── seo-local/              # Local SEO (GBP, citations, reviews)
│   ├── seo-maps/               # Maps intelligence (geo-grid, GBP audit)
│   ├── seo-backlinks/          # Backlink profile analysis
│   ├── seo-cluster/            # Semantic topic clustering (SERP-based)
│   ├── seo-sxo/                # Search Experience Optimization
│   ├── seo-drift/              # SEO drift monitoring (baselines)
│   ├── seo-ecommerce/          # E-commerce SEO (product schema, marketplaces)
│   ├── seo-hreflang/           # International SEO and hreflang
│   ├── seo-plan/               # Strategic SEO planning (industry templates)
│   ├── seo-programmatic/       # Programmatic SEO at scale
│   ├── seo-competitor-pages/   # Competitor comparison page generation
│   ├── seo-google/             # Google SEO APIs (GSC, PSI, CrUX, GA4)
│   ├── seo-flow/               # FLOW framework integration (CC BY 4.0)
│   ├── seo-dataforseo/         # DataForSEO MCP mirror (extension surface)
│   └── seo-image-gen/          # Banana MCP mirror (extension surface)
│
└── agents/
    ├── seo-technical.md        # Crawlability, indexability, security
    ├── seo-content.md          # E-E-A-T, readability, thin content
    ├── seo-schema.md           # Structured data validation
    ├── seo-sitemap.md          # Sitemap quality gates
    ├── seo-performance.md      # Core Web Vitals
    ├── seo-visual.md           # Screenshots, mobile rendering
    ├── seo-geo.md              # AI crawler access, citability
    ├── seo-local.md            # GBP signals, NAP, reviews
    ├── seo-maps.md             # Geo-grid, competitor radius mapping
    ├── seo-backlinks.md        # Moz, Bing Webmaster, Common Crawl
    ├── seo-cluster.md          # Semantic clustering analysis
    ├── seo-sxo.md              # Page-type, user stories, personas
    ├── seo-drift.md            # Baseline comparison, regression detection
    ├── seo-ecommerce.md        # Product schema, marketplace intelligence
    ├── seo-google.md           # GSC, PSI, CrUX, GA4 analyst
    ├── seo-flow.md             # FLOW framework prompt selection
    ├── seo-dataforseo.md       # DataForSEO MCP mirror
    └── seo-image-gen.md        # Banana MCP mirror
``\`

## Component Types

### Skills

Skills are markdown files with YAML frontmatter that define capabilities and instructions.

**SKILL.md Format:**
``\`yaml
---
name: skill-name
description: >
  When to use this skill. Include activation keywords
  and concrete use cases.
---

# Skill Title

Instructions and documentation...
``\`

### Subagents

Subagents are specialized workers that can be delegated tasks. They have their own context and tools.

**Agent Format:**
``\`yaml
---
name: agent-name
description: What this agent does.
tools: Read, Bash, Write, Glob, Grep
---

Instructions for the agent...
``\`

### Reference Files

Reference files contain static data loaded on-demand to avoid bloating the main skill.

## Orchestration Flow

### Full Audit (`/seo audit`)

``\`
User request
    │
    ▼
┌──────────────────┐
│   seo            │  Main orchestrator (skills/seo/SKILL.md)
└────────┬─────────┘
         │  Detects business type and signals
         │  Spawns subagents in parallel
         │
    ┌────┴────┬────────┬────────┬────────┬────────┬────────┐
    ▼         ▼        ▼        ▼        ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│tech   │ │content│ │schema │ │sitemap│ │perf   │ │visual │ │geo    │
└───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘ └───┬───┘
    │         │         │         │         │         │         │
    └─────────┴─────────┴────┬────┴─────────┴─────────┴─────────┘
                             │
                             │  Conditional spawns:
                             │  - seo-google     (Google API creds detected)
                             │  - seo-local      (local business detected)
                             │  - seo-maps       (local + DataForSEO MCP)
                             │  - seo-backlinks  (Moz/Bing/CC available)
                             │  - seo-cluster    (content strategy signals)
                             │  - seo-sxo        (always in full audits)
                             │  - seo-drift      (baseline exists for URL)
                             │  - seo-ecommerce  (e-commerce detected)
                             ▼
                    ┌────────────────┐
                    │  Aggregate     │
                    │  Results       │
                    └────────┬───────┘
                             │
                             ▼
                    ┌────────────────┐
                    │  Generate      │
                    │  Health Score  │
                    │  + Action Plan │
                    └────────────────┘
``\`

### Individual Command

``\`
User Request (e.g., /seo page)
    │
    ▼
┌─────────────────┐
│   seo       │  ← Routes to sub-skill
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   seo-page      │  ← Sub-skill handles directly
│   (SKILL.md)    │
└─────────────────┘
``\`

## Design Principles

### 1. Progressive Disclosure

- Main SKILL.md is concise (<200 lines)
- Reference files loaded on-demand
- Detailed instructions in sub-skills

### 2. Parallel Processing

- Subagents run concurrently during audits
- Independent analyses don't block each other
- Results aggregated after all complete

### 3. Quality Gates

- Built-in thresholds prevent bad recommendations
- Location page limits (30 warning, 50 hard stop)
- Schema deprecation awareness
- FID → INP replacement enforced

### 4. Industry Awareness

- Templates for different business types
- Automatic detection from homepage signals
- Tailored recommendations per industry

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Skill | `seo-{name}/SKILL.md` | `seo-audit/SKILL.md` |
| Agent | `seo-{name}.md` | `seo-technical.md` |
| Reference | `{topic}.md` | `cwv-thresholds.md` |
| Script | `{action}_{target}.py` | `fetch_page.py` |
| Template | `{industry}.md` | `saas.md` |

## Extension Points

### Adding a New Sub-Skill

1. Create `skills/seo-newskill/SKILL.md`
2. Add YAML frontmatter with name and description
3. Write skill instructions
4. Update main `skills/seo/SKILL.md` to route to new skill

### Adding a New Subagent

1. Create `agents/seo-newagent.md`
2. Add YAML frontmatter with name, description, tools
3. Write agent instructions
4. Reference from relevant skills

### Adding a New Reference File

1. Create file in appropriate `references/` directory
```

## File: docs/COMMANDS.md

Excerpt: first 220 of 582 lines.

```markdown
# Commands Reference

## Overview

All Claude SEO commands start with `/seo` followed by a subcommand.

## Command List

### `/seo audit <url>`

Full website SEO audit with parallel analysis.

**Example:**
``\`
/seo audit https://example.com
``\`

**What it does:**
1. Crawls up to 500 pages
2. Detects business type
3. Delegates to 7 specialist subagents in parallel
4. Generates SEO Health Score (0-100)
5. Creates prioritized action plan

**Output:**
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`
- `screenshots/` (if Playwright available)

---

### `/seo page <url>`

Deep single-page analysis.

**Example:**
``\`
/seo page https://example.com/about
``\`

**What it analyzes:**
- On-page SEO (title, meta, headings, URLs)
- Content quality (word count, readability, E-E-A-T)
- Technical elements (canonical, robots, Open Graph)
- Schema markup
- Images (alt text, sizes, formats)
- Core Web Vitals potential issues

---

### `/seo technical <url>`

Technical SEO audit across 9 categories.

**Example:**
``\`
/seo technical https://example.com
``\`

**Categories:**
1. Crawlability
2. Indexability
3. Security
4. URL Structure
5. Mobile Optimization
6. Core Web Vitals (LCP, INP, CLS)
7. Structured Data
8. JavaScript Rendering
9. IndexNow Protocol

---

### `/seo content <url>`

E-E-A-T and content quality analysis.

**Example:**
``\`
/seo content https://example.com/blog/post
``\`

**What it evaluates:**
- Experience signals (first-hand knowledge)
- Expertise (author credentials)
- Authoritativeness (external recognition)
- Trustworthiness (transparency, security)
- AI citation readiness
- Content freshness

---

### `/seo content-brief <topic or url>`

Generate a detailed SEO content brief: target keywords, search intent, heading outline, internal link targets, and competitor angle.

**Example:**
``\`
/seo content-brief "best running shoes for flat feet"
``\`

**What it produces:**
- Primary and secondary target keywords
- Search intent and audience
- Section-by-section heading outline
- Internal link recommendations
- Competitor content angles to beat

---

### `/seo schema <url>`

Schema markup detection, validation, and generation.

**Example:**
``\`
/seo schema https://example.com
``\`

**What it does:**
- Detects existing schema (JSON-LD, Microdata, RDFa)
- Validates against Google's requirements
- Identifies missing opportunities
- Generates ready-to-use JSON-LD

---

### `/seo geo <url>`

AI Overviews / Generative Engine Optimization.

**Example:**
``\`
/seo geo https://example.com/blog/guide
``\`

**What it analyzes:**
- Citability score (quotable facts, statistics)
- Structural readability (headings, lists, tables)
- Entity clarity (definitions, context)
- Authority signals (credentials, sources)
- Structured data support

---

### `/seo images <url>`

Image optimization analysis.

**Example:**
``\`
/seo images https://example.com
``\`

**What it checks:**
- Alt text presence and quality
- File sizes (flag >200KB)
- Formats (WebP/AVIF recommendations)
- Responsive images (srcset, sizes)
- Lazy loading
- CLS prevention (dimensions)

---

### `/seo sitemap <url>`

Analyze existing XML sitemap.

**Example:**
``\`
/seo sitemap https://example.com/sitemap.xml
``\`

**What it validates:**
- XML format
- URL count (<50k per file)
- URL status codes
- lastmod accuracy
- Deprecated tags (priority, changefreq)
- Coverage vs crawled pages

---

### `/seo sitemap generate`

Generate new sitemap with industry templates.

**Example:**
``\`
/seo sitemap generate
``\`

**Process:**
1. Select or auto-detect business type
2. Interactive structure planning
3. Apply quality gates (30/50 location page limits)
4. Generate valid XML
5. Create documentation

---

### `/seo plan <type>`

Strategic SEO planning.

**Types:** `saas`, `local`, `ecommerce`, `publisher`, `agency`

**Example:**
``\`
/seo plan saas
``\`

**What it creates:**
- Complete SEO strategy
- Competitive analysis
- Content calendar
- Implementation roadmap (4 phases)
- Site architecture design

---

```

## File: docs/INSTALLATION.md

Excerpt: first 160 of 177 lines.

```markdown
# Installation Guide

## Prerequisites

- **Python 3.10+** with pip
- **Git** for cloning the repository
- **Claude Code CLI** installed and configured

Optional:
- **Playwright** for screenshot capabilities

## Quick Install

### Plugin Install (Claude Code 1.0.33+)

The recommended path. Inside Claude Code:

``\`
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
``\`

### Manual Install (Unix, macOS, Linux)

``\`bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
``\`

Review-then-run alternative:

``\`bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh > install.sh
cat install.sh        # review
bash install.sh       # run when satisfied
rm install.sh
``\`

### Manual Install (Windows, PowerShell)

``\`powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
``\`

The Windows path uses `git clone` rather than `irm | iex` because Claude Code's own security guardrails flag piped remote-script execution. Inspect `install.ps1` before running.

## Manual Installation

1. **Clone the repository**

``\`bash
git clone https://github.com/AgriciDaniel/claude-seo.git
cd claude-seo
``\`

2. **Run the installer**

``\`bash
./install.sh
``\`

3. **Install Python dependencies** (if not done automatically)

The installer creates a venv at `~/.claude/skills/seo/.venv/`. If that fails, install manually:

``\`bash
# Option A: Use the venv
~/.claude/skills/seo/.venv/bin/pip install -r ~/.claude/skills/seo/requirements.txt

# Option B: User-level install
pip install --user -r ~/.claude/skills/seo/requirements.txt
``\`

4. **Install Playwright browsers** (optional, for visual analysis)

``\`bash
pip install playwright
playwright install chromium
``\`

Playwright is optional. Without it, visual analysis uses WebFetch as a fallback.

## Installation Paths

The installer copies files to:

| Component | Path |
|-----------|------|
| Main skill | `~/.claude/skills/seo/` |
| Sub-skills | `~/.claude/skills/seo-*/` |
| Subagents | `~/.claude/agents/seo-*.md` |

## Verify Installation

1. Start Claude Code:

``\`bash
claude
``\`

2. Check that the skill is loaded:

``\`
/seo
``\`

You should see a help message or prompt for a URL.

## Uninstallation

If installed as a plugin:

``\`
/plugin uninstall claude-seo@agricidaniel-claude-seo
/plugin marketplace remove AgriciDaniel/claude-seo
``\`

If installed manually, run the uninstaller from a fresh clone:

``\`bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/uninstall.sh
``\`

`uninstall.sh` removes all installed sub-skills, sub-agents, and the plugin's MCP entries from `~/.claude/settings.json`. Do not maintain a hand-coded `rm` list. The shipped uninstaller is the canonical source.

## Upgrading

To upgrade to the latest version:

Caution: Prefer downloading, inspecting, then running remote scripts; the pipe-to-shell form below is the less-safe convenience option.

``\`bash
# Uninstall current version
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash

# Install new version
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
``\`

## Troubleshooting

### "Skill not found" error

Ensure the skill is installed in the correct location:

``\`bash
ls ~/.claude/skills/seo/SKILL.md
``\`

If the file doesn't exist, re-run the installer.

### Python dependency errors

Install dependencies manually:

``\`bash
pip install beautifulsoup4 requests lxml playwright Pillow urllib3 validators
``\`
```

## File: docs/MCP-INTEGRATION.md

```markdown
# MCP Integration

## Overview

Claude SEO can integrate with Model Context Protocol (MCP) servers to access external APIs and enhance analysis capabilities.

## Available Integrations

### PageSpeed Insights API

Use Google's PageSpeed Insights API directly for real Core Web Vitals data.

**Configuration:**

1. Get an API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the PageSpeed Insights API
3. Use in your analysis:

``\`bash
curl -H "X-Goog-Api-Key: $GOOGLE_API_KEY" \
  "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL"
``\`

### Google Search Console

For organic search data, use the `mcp-server-gsc` MCP server by [ahonn](https://github.com/ahonn/mcp-server-gsc). Provides search performance data, URL inspection, and sitemap management.

**Configuration:**

``\`json
{
  "mcpServers": {
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "mcp-server-gsc"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json"
      }
    }
  }
}
``\`

### PageSpeed Insights MCP Server

Use `mcp-server-pagespeed` by [enemyrr](https://github.com/enemyrr/mcp-server-pagespeed) for Lighthouse audits, CWV metrics, and performance scoring via MCP.

**Configuration:**

``\`json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "mcp-server-pagespeed"],
      "env": {
        "PAGESPEED_API_KEY": "your-api-key"
      }
    }
  }
}
``\`

### Official SEO MCP Servers (2025-2026)

The MCP ecosystem for SEO has matured significantly. These are production-ready integrations:

| Tool | Package / Endpoint | Type | Notes |
|------|-------------------|------|-------|
| **Ahrefs** | `@ahrefs/mcp` | Official | Launched July 2025. Supports local and remote modes. Backlinks, keywords, site audit data. |
| **Semrush** | `https://mcp.semrush.com/v1/mcp` | Official (remote) | Full API access via remote MCP endpoint. Domain analytics, keyword research, backlink data. |
| **Google Search Console** | `mcp-server-gsc` | Community | By ahonn. Search performance, URL inspection, sitemaps. |
| **PageSpeed Insights** | `mcp-server-pagespeed` | Community | By enemyrr. Lighthouse audits, CWV metrics, performance scoring. |
| **DataForSEO** | `dataforseo-mcp-server` | Official extension | 9 modules, 79 tools, 22 commands. Install: `./extensions/dataforseo/install.sh`. See [extension docs](../extensions/dataforseo/README.md). |
| **kwrds.ai** | kwrds MCP server | Community | Keyword research, search volume, difficulty scoring. |
| **SEO Review Tools** | SEO Review Tools MCP | Community | Site auditing and on-page analysis API. |

## API Usage Examples

### PageSpeed Insights

``\`python
import requests

def get_pagespeed_data(url: str, api_key: str) -> dict:
    """Fetch PageSpeed Insights data for a URL."""
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "strategy": "mobile",  # or "desktop"
        "category": ["performance", "accessibility", "best-practices", "seo"]
    }
    headers = {"X-Goog-Api-Key": api_key}
    response = requests.get(endpoint, params=params, headers=headers)
    return response.json()
``\`

### Core Web Vitals from CrUX

``\`python
def get_crux_data(url: str, api_key: str) -> dict:
    """Fetch Chrome UX Report data for a URL."""
    endpoint = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"
    payload = {
        "url": url,
        "formFactor": "PHONE"  # or "DESKTOP"
    }
    headers = {"Content-Type": "application/json", "X-Goog-Api-Key": api_key}
    response = requests.post(endpoint, json=payload, headers=headers)
    return response.json()
``\`

## Metrics Available

### From PageSpeed Insights

| Metric | Description |
|--------|-------------|
| LCP | Largest Contentful Paint (lab) |
| INP | Interaction to Next Paint (estimated) |
| CLS | Cumulative Layout Shift (lab) |
| FCP | First Contentful Paint |
| TBT | Total Blocking Time |
| Speed Index | Visual progress speed |

### From CrUX (Field Data)

| Metric | Description |
|--------|-------------|
| LCP | 75th percentile, real users |
| INP | 75th percentile, real users |
| CLS | 75th percentile, real users |
| TTFB | Time to First Byte |

## Best Practices

1. **Rate Limiting**: Respect API quotas (typically 25k requests/day for PageSpeed)
2. **Caching**: Cache results to avoid redundant API calls
3. **Field vs Lab**: Prioritize field data (CrUX) for ranking signals
4. **Error Handling**: Handle API errors gracefully

## Without API Keys

If you don't have API keys, Claude SEO can still:

1. Analyze HTML source for potential issues
2. Identify common performance problems
3. Check for render-blocking resources
4. Evaluate image optimization opportunities
5. Detect JavaScript-heavy implementations

The analysis will note that actual Core Web Vitals measurements require field data from real users.

```

## File: .claude-plugin/plugin.json

```markdown
{
  "name": "claude-seo",
  "version": "2.2.0",
  "description": "Comprehensive SEO analysis plugin for Claude Code. 25 sub-skills (21 core + 1 orchestrator + 1 framework + 2 extension mirrors) and 18 sub-agents cover technical SEO, content quality, schema, sitemaps, Core Web Vitals, local SEO, backlinks, AI/GEO, ecommerce, hreflang, SXO, clustering, drift monitoring, and Google APIs. Includes optional MCP extensions, SPA-aware rendering, portability, and hardened SSRF/DNS-rebinding safe fetchers.",
  "author": {
    "name": "AgriciDaniel",
    "email": "agricidaniel@gmail.com",
    "url": "https://github.com/AgriciDaniel"
  },
  "license": "MIT",
  "homepage": "https://claude-seo.md",
  "repository": "https://github.com/AgriciDaniel/claude-seo",
  "keywords": [
    "seo",
    "technical-seo",
    "content-quality",
    "e-e-a-t",
    "schema-markup",
    "core-web-vitals",
    "local-seo",
    "geo",
    "ai-search",
    "sitemap",
    "image-optimization",
    "image-serp",
    "google-images",
    "hreflang",
    "google-search-console",
    "pagespeed",
    "crux",
    "ga4",
    "backlinks",
    "moz",
    "bing-webmaster",
    "common-crawl",
    "backlink-verification",
    "semantic-clustering",
    "topic-clusters",
    "sxo",
    "search-experience",
    "drift-monitoring",
    "ecommerce-seo",
    "google-shopping",
    "cultural-profiles",
    "content-parity",
    "mcp-extensions",
    "headless-rendering",
    "ssrf-safe-fetchers",
    "ai-citation-optimization",
    "synthesis-framework"
  ]
}

```

## File: .claude-plugin/marketplace.json

```markdown
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "agricidaniel-claude-seo",
  "owner": {
    "name": "AgriciDaniel"
  },
  "metadata": {
    "description": "Comprehensive SEO analysis plugin for Claude Code. 25 sub-skills and 18 sub-agents, plus 8 optional MCP extensions (DataForSEO, Firecrawl, Banana, Ahrefs, SE Ranking, Profound, Bing Webmaster, Unlighthouse). v2 adds shared headless rendering, QRG-aligned content quality gates, LCP subparts via CrUX, IndexNow, four Schema.org generators, AI Share-of-Voice tracking, parasite-SEO risk scanning, multi-platform portability, and a hardened SSRF + DNS-rebinding safety layer."
  },
  "plugins": [
    {
      "name": "claude-seo",
      "source": "./",
      "description": "Comprehensive SEO analysis plugin for Claude Code. 25 sub-skills (21 core + 1 orchestrator + 1 framework integration + 2 extension mirrors) and 18 sub-agents (15 core + 1 framework integration + 2 extension mirrors), plus 8 optional MCP extensions. v2 adds shared headless rendering across every fetching agent, QRG-aligned content quality gates, LCP subparts via CrUX, IndexNow submission, four Schema.org generators (Reservation / OrderAction / DiscussionForumPosting / ProfilePage), AI Share-of-Voice tracking, parasite-SEO risk scanning, and multi-platform portability.",
      "author": {
        "name": "AgriciDaniel",
        "email": "agricidaniel@gmail.com",
        "url": "https://github.com/AgriciDaniel"
      },
      "category": "marketing",
      "homepage": "https://claude-seo.md",
      "keywords": [
        "seo",
        "technical-seo",
        "content-quality",
        "e-e-a-t",
        "schema-markup",
        "core-web-vitals",
        "local-seo",
        "geo",
        "ai-search",
        "sitemap",
        "image-optimization",
        "image-serp",
        "google-images",
        "hreflang",
        "google-search-console",
        "pagespeed",
        "crux",
        "ga4",
        "backlinks",
        "moz",
        "bing-webmaster",
        "common-crawl",
        "backlink-verification",
        "semantic-clustering",
        "topic-clusters",
        "sxo",
        "search-experience",
        "drift-monitoring",
        "ecommerce-seo",
        "google-shopping",
        "cultural-profiles",
        "content-parity",
        "mcp-extensions",
        "headless-rendering",
        "ssrf-safe-fetchers",
        "ai-citation-optimization",
        "synthesis-framework"
      ]
    }
  ]
}

```

## File: skills/seo/SKILL.md

Excerpt: first 180 of 272 lines.

```markdown
---
name: seo
description: "Comprehensive SEO analysis for any website or business type. Full site audits, single-page analysis, technical SEO (crawlability, indexability, Core Web Vitals with INP), schema markup, content quality (E-E-A-T), image optimization, sitemap analysis, and GEO for AI Overviews/ChatGPT/Perplexity. Industry detection for SaaS, e-commerce, local, publishers, agencies. Triggers on: SEO, audit, schema, Core Web Vitals, sitemap, E-E-A-T, AI Overviews, GEO, technical SEO, content quality, page speed, structured data."
user-invocable: true
argument-hint: "[command] [url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.2.0"
  category: seo
---

# SEO: Universal SEO Analysis Skill

**Invocation:** `/seo $1 $2` where `$1` is the command and `$2` is the URL or argument.

**Scripts:** Located at the plugin root `scripts/` directory.

Comprehensive SEO analysis across all industries (SaaS, local services,
e-commerce, publishers, agencies). Orchestrates 24 sub-skills (21 core + 1 framework
integration + 2 extension mirrors) and 18 sub-agents. A separate optional Firecrawl
extension is also installable (see "Optional Extensions" below).

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/seo audit <url>` | Full website audit with parallel subagent delegation |
| `/seo page <url>` | Deep single-page analysis |
| `/seo sitemap <url or generate>` | Analyze or generate XML sitemaps |
| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |
| `/seo images <url or optimize>` | Image SEO: on-page audit, SERP analysis, file optimization |
| `/seo technical <url>` | Technical SEO audit (9 categories) |
| `/seo content <url>` | E-E-A-T and content quality analysis |
| `/seo content-brief <topic or url>` | Generate detailed SEO content brief with target keywords, outline, internal links |
| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |
| `/seo plan <business-type>` | Strategic SEO planning |
| `/seo programmatic [url\|plan]` | Programmatic SEO analysis and planning |
| `/seo competitor-pages [url\|generate]` | Competitor comparison page generation |
| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |
| `/seo maps [command] [args]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |
| `/seo hreflang [url]` | Hreflang/i18n SEO audit and generation |
| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |
| `/seo backlinks <url>` | Backlink profile analysis (free: Moz, Bing, CC; premium: DataForSEO) |
| `/seo cluster <seed-keyword>` | SERP-based semantic clustering and content architecture |
| `/seo sxo <url>` | Search Experience Optimization: page-type analysis, user stories, personas |
| `/seo drift baseline <url>` | Capture SEO baseline for change monitoring |
| `/seo drift compare <url>` | Compare current state to stored baseline |
| `/seo drift history <url>` | Show drift history over time |
| `/seo ecommerce <url>` | E-commerce SEO: product schema, marketplace intelligence |
| `/seo firecrawl [command] <url>` | Full-site crawling and site mapping (extension) |
| `/seo dataforseo [command]` | Live SEO data via DataForSEO (extension) |
| `/seo image-gen [use-case] <description>` | AI image generation for SEO assets (extension) |
| `/seo flow [stage] [url\|topic]` | FLOW framework: evidence-led prompts for Find, Leverage, Optimize, Win, or Local stages |

## Orchestration Logic

When the user invokes `/seo audit`, delegate to subagents in parallel:
1. Detect business type (SaaS, local, ecommerce, publisher, agency, other)
2. Spawn subagents: seo-technical, seo-content, seo-schema, seo-sitemap, seo-performance, seo-visual, seo-geo
3. If Google API credentials detected (`python3 scripts/google_auth.py --check`), also spawn seo-google agent
4. If local business detected, also spawn seo-local agent
5. If local business detected AND DataForSEO MCP available, also spawn seo-maps agent
6. If backlink APIs detected (`python3 scripts/backlinks_auth.py --check`), also spawn seo-backlinks agent
7. If Firecrawl MCP available, use `firecrawl_map` to discover all site URLs before analysis
8. If content strategy signals detected (blog, pillar pages, topic clusters), also spawn seo-cluster agent
9. If e-commerce detected, also spawn seo-ecommerce agent
10. If drift baseline exists for this URL (`python3 scripts/drift_history.py <url>`), also spawn seo-drift agent
11. Always include seo-sxo in full audits (search experience applies to all sites)
12. Collect results and generate unified report with SEO Health Score (0-100)
13. **Synthesize via the 10-principle framework** (see "Synthesis Methodology" below) — walk PERCEIVE → ANALYZE → VALIDATE → ACT before bucketing findings into Critical / High / Medium / Low
14. Create prioritized action plan with dependency sequencing + falsifiability per recommendation
15. **Offer PDF report**: "Generate a professional PDF report? Use `/seo google report full`"

For individual commands, load the relevant sub-skill directly.
After any analysis command completes, offer to generate a PDF report via `scripts/google_report.py`.

## Synthesis Methodology

Audits are not just findings — they are findings synthesized into a coherent
strategy. claude-seo uses a 10-principle thinking framework grouped into four
phases: **PERCEIVE** (observe-external · observe-internal · listen),
**ANALYZE** (think · connect-lateral · connect-system), **VALIDATE** (feel ·
accept), **ACT** (create · grow).

Full audits (`/seo audit`, `/seo page`) walk every phase before emitting the
action plan. Narrower commands (`/seo schema`, `/seo images`, etc.) pass at
least THINK + ACCEPT before emitting (sound first principle, surfaced
falsifiability). The Critical / High / Medium / Low priority buckets are the
**output** of validation, not a substitute for it.

Full methodology + per-principle SEO mapping: `references/thinking-framework.md`.

Each emitted recommendation should carry:
- The first-principle observation it rests on (THINK)
- The dependency on / unblock relationship to other recommendations (CONNECT-system)
- An explicit "how would we know this failed?" check (ACCEPT)
- A leading indicator the user can monitor without re-running the audit (GROW)

## Industry Detection

Detect business type from homepage signals:
- **SaaS**: pricing page, /features, /integrations, /docs, "free trial", "sign up"
- **Local Service**: phone number, address, service area, "serving [city]", Google Maps embed --> auto-suggest `/seo local` for deeper analysis
- **E-commerce**: /products, /collections, /cart, "add to cart", product schema
- **Publisher**: /blog, /articles, /topics, article schema, author pages, publication dates
- **Agency**: /case-studies, /portfolio, /industries, "our work", client logos

## Quality Gates

Read `references/quality-gates.md` for thin content thresholds per page type.
Hard rules:
- WARNING at 30+ location pages (enforce 60%+ unique content)
- HARD STOP at 50+ location pages (require user justification)
- Never recommend HowTo schema (deprecated Sept 2023)
- FAQ schema: Google retired FAQ rich results for ALL sites on May 7, 2026 (no SERP feature anymore; supersedes the Aug 2023 gov/health restriction). Flag existing FAQPage at Info (not Critical) for its AI/LLM citation benefit; do not recommend removal; do not recommend new FAQPage for Google SERP benefit; use QAPage for genuine user Q&A
- All Core Web Vitals references use INP, never FID

## Community Footer

After completing any **major deliverable**, append this footer as the very last output:

``\`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Built by agricidaniel — Join the AI Marketing Hub community
🆓 Free  → https://www.skool.com/ai-marketing-hub
⚡ Pro   → https://www.skool.com/ai-marketing-hub-pro
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
``\`

### When to show

Display after these commands complete their full output:
- `/seo audit` (after full site audit report + action plan)
- `/seo page` (after deep single-page analysis)
- `/seo technical` (after technical audit report)
- `/seo content` (after E-E-A-T content assessment)
- `/seo schema` (after schema detection/validation report)
- `/seo sitemap` (after sitemap analysis or generation)
- `/seo geo` (after GEO optimization report)
- `/seo plan` (after strategic SEO plan)
- `/seo local` (after local SEO audit)
- `/seo maps` (after maps intelligence report)
- `/seo google` (after Google API data report)
- `/seo backlinks` (after backlink profile analysis)
- `/seo cluster` (after cluster plan generation)
- `/seo sxo` (after SXO analysis report)
- `/seo drift compare` (after drift comparison report)
- `/seo ecommerce` (after e-commerce analysis)

### When to skip

Do NOT show the footer after:
- `/seo images` (quick image check — too small)
- `/seo hreflang` (quick validation — too small)
- `/seo competitor-pages` (page generation step)
- `/seo programmatic` (quick analysis)
- `/seo dataforseo` (data fetching utility)
- `/seo image-gen` (asset generation)
- Context intake questions (before analysis starts)
- Error messages or "missing data" prompts

## Reference Files

Load these on-demand as needed (do NOT load all at startup):
- `references/cwv-thresholds.md`: Current Core Web Vitals thresholds and measurement details
- `references/schema-types.md`: All supported schema types with deprecation status
- `references/eeat-framework.md`: E-E-A-T evaluation criteria (Sept 2025 QRG update)
- `references/quality-gates.md`: Content length minimums, uniqueness thresholds
- `references/local-seo-signals.md`: Local ranking factors, review benchmarks, citation tiers, GBP status
- `references/local-schema-types.md`: LocalBusiness subtypes, industry-specific schema and citation sources

Maps-specific references (loaded by seo-maps skill, not at startup):
- `references/maps-geo-grid.md`, `references/maps-gbp-checklist.md`, `references/maps-api-endpoints.md`, `references/maps-free-apis.md`

## Scoring Methodology

### SEO Health Score (0-100)
Weighted aggregate of all categories:

```

## File: skills/seo-geo/SKILL.md

Excerpt: first 180 of 287 lines.

```markdown
---
name: seo-geo
description: >
  Optimize content for AI Overviews (formerly SGE), ChatGPT web search,
  Perplexity, and other AI-powered search experiences. Generative Engine
  Optimization (GEO) analysis including brand mention signals, AI crawler
  accessibility, llms.txt compliance, passage-level citability scoring, and
  platform-specific optimization. Use when user says "AI Overviews", "SGE",
  "GEO", "AI search", "LLM optimization", "Perplexity", "AI citations",
  "ChatGPT search", or "AI visibility".
user-invocable: true
argument-hint: "[url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.2.0"
  category: seo
---

# AI Search / GEO Optimization (May 2026)

## Primary Source: Google's AI Optimization Guide

Google's official position, published under Search Central docs:

> "Optimizing for generative AI search is **still SEO** from Google's
> perspective. AEO and GEO are rebranded labels for the same work."

Read `references/google-ai-optimization-guide.md` for the full synthesis,
myth-busting list (`llms.txt`, chunking, AI-rephrasing, mention-farming —
all rejected by Google as ineffective), and the Who/How/Why test for
content quality.

Audits should frame GEO findings as **SEO fundamentals applied to AI-search
surfaces**, not as a separate optimization discipline. When community
recommendations contradict Google's primary source, defer to Google and note
the contradiction in the report.

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| AI Overviews reach | 1.5 billion users/month across 200+ countries | Google |
| AI Overviews query coverage | 50%+ of all queries | Industry data |
| AI Mode monthly users | 1B+ (surpassed May 2026) | Google |
| AI Mode model | Gemini 3.5 Flash (default, global, since I/O 2026) | Google |
| AI-referred sessions growth | 527% (Jan-May 2025) | SparkToro |
| ChatGPT weekly active users | 900 million | OpenAI |
| Perplexity monthly queries | 500+ million | Perplexity |

## Critical Insight: Brand Mentions > Backlinks

**Brand mentions correlate 3x more strongly with AI visibility than backlinks.**
(Ahrefs December 2025 study of 75,000 brands)

| Signal | Correlation with AI Citations |
|--------|------------------------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit mentions | High |
| Wikipedia presence | High |
| LinkedIn presence | Moderate |
| Domain Rating (backlinks) | ~0.266 (weak) |

**Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query, so platform-specific optimization is essential.

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation. And **~44% of AI
citations come from the first 30% of a page** (SE Ranking study) — front-load
your most citable, self-contained answer rather than burying it below the fold.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**92% of AI Overview citations come from top-10 ranking pages**, but 47% come from pages ranking below position 5, demonstrating different selection logic.

**Strong signals:**
- Clean H1->H2->H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- **Recency** — content under 3 months old is ~3x more likely to be cited in AI answers; pages left stale 6+ months lose citation eligibility (SE Ranking, 1.3M-citation study). A scheduled refresh program is one of the highest-leverage GEO plays.
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript.** Server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt` for these AI crawlers:

| Crawler | Owner | Purpose |
|---------|-------|---------|
| GPTBot | OpenAI | ChatGPT web search |
| OAI-SearchBot | OpenAI | OpenAI search features |
| ChatGPT-User | OpenAI | ChatGPT browsing |
| ClaudeBot | Anthropic | Claude web features |
| PerplexityBot | Perplexity | Perplexity AI search |
| CCBot | Common Crawl | Training data (often blocked) |
| anthropic-ai | Anthropic | Claude training |
| Bytespider | ByteDance | TikTok/Douyin AI |
| cohere-ai | Cohere | Cohere models |

**Recommendation:** Allow GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot for AI search visibility. Block CCBot and training crawlers if desired.

---

## llms.txt Standard

Read `references/llmstxt-evidence.md` for the primary-source evidence (Mueller, Illyes, SE Ranking 300k-domain study, OtterlyAI server-log audit) on why `/llms.txt` is not currently a citation lever for major AI search systems. claude-seo reports presence but assigns no citation-ranking weight.

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
``\`
# Title of site
> Brief description
```

## File: skills/seo-content/SKILL.md

Excerpt: first 180 of 199 lines.

```markdown
---
name: seo-content
description: >
  Content quality and E-E-A-T analysis with AI citation readiness assessment.
  Use when user says "content quality", "E-E-A-T", "content analysis",
  "readability check", "thin content", or "content audit".
user-invocable: true
argument-hint: "[url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.2.0"
  category: seo
---

# Content Quality & E-E-A-T Analysis

## Google's "Who / How / Why" Test (canonical heuristic)

Before scoring E-E-A-T sub-factors, every page audit should pass Google's
own three-question heuristic from the helpful-content guide:

| Question | What to look for |
|---|---|
| **Who** created it? | Visible byline, author bio page, professional credentials. Required where readers expect it; non-negotiable for YMYL. |
| **How** was it created? | Process disclosure where readers would reasonably ask — especially for AI-assisted content. Original research / first-hand evidence / lived experience. |
| **Why** does it exist? | "To help people" rather than "to attract search clicks." Watch for niche entry without expertise, content churn for freshness signals, content written to a word-count target. |

Primary source:
https://developers.google.com/search/docs/fundamentals/creating-helpful-content

When all three answers are weak, the page is at risk under the core ranking
system's helpfulness signals (formerly the standalone Helpful Content System,
merged into core during the March 2024 update).

## E-E-A-T Framework (updated Sept 2025 QRG)

Read `skills/seo/references/eeat-framework.md` for full criteria.

### Experience (first-hand signals)
- Original research, case studies, before/after results
- Personal anecdotes, process documentation
- Unique data, proprietary insights
- Photos/videos from direct experience

### Expertise
- Author credentials, certifications, bio
- Professional background relevant to topic
- Technical depth appropriate for audience
- Accurate, well-sourced claims

### Authoritativeness
- External citations, backlinks from authoritative sources
- Brand mentions, industry recognition
- Published in recognized outlets
- Cited by other experts

### Trustworthiness
- Contact information, physical address
- Privacy policy, terms of service
- Customer testimonials, reviews
- Date stamps, transparent corrections
- Secure site (HTTPS)

## Content Metrics

### Word Count Analysis
Compare against page type minimums:
| Page Type | Minimum |
|-----------|---------|
| Homepage | 500 |
| Service page | 800 |
| Blog post | 1,500 |
| Product page | 300+ (400+ for complex products) |
| Location page | 500-600 |

> **Important:** These are **topical coverage floors**, not targets. Google has confirmed word count is NOT a direct ranking factor. The goal is comprehensive topical coverage; a 500-word page that thoroughly answers the query will outrank a 2,000-word page that doesn't. Use these as guidelines for adequate coverage depth, not rigid requirements.

### Readability
- Flesch Reading Ease: target 60-70 for general audience

> **Note:** Flesch Reading Ease is a useful proxy for content accessibility but is NOT a direct Google ranking factor. John Mueller has confirmed Google does not use basic readability scores for ranking. Yoast deprioritized Flesch scores in v19.3. Use readability analysis as a content quality indicator, not as an SEO metric to optimize directly.
- Grade level: match target audience
- Sentence length: average 15-20 words
- Paragraph length: 2-4 sentences

### Keyword Optimization
- Primary keyword in title, H1, first 100 words
- Natural density (1-3%)
- Semantic variations present
- No keyword stuffing

### Content Structure
- Logical heading hierarchy (H1 -> H2 -> H3)
- Scannable sections with descriptive headings
- Bullet/numbered lists where appropriate
- Table of contents for long-form content

### Multimedia
- Relevant images with proper alt text
- Videos where appropriate
- Infographics for complex data
- Charts/graphs for statistics

### Internal Linking
- 3-5 relevant internal links per 1000 words
- Descriptive anchor text
- Links to related content
- No orphan pages

### External Linking
- Cite authoritative sources
- Open in new tab for user experience
- Reasonable count (not excessive)

## AI Content Assessment (Sept 2025 QRG addition)

Google's raters now formally assess whether content appears AI-generated.

### Acceptable AI Content
- Demonstrates genuine E-E-A-T
- Provides unique value
- Has human oversight and editing
- Contains original insights

### Low-Quality AI Content Markers
- Generic phrasing, lack of specificity
- No original insight
- Repetitive structure across pages
- No author attribution
- Factual inaccuracies

> **Helpful Content System (March 2024):** The Helpful Content System was merged into Google's core ranking algorithm during the March 2024 core update. It no longer operates as a standalone classifier. Helpfulness signals are now weighted within every core update. The same principles apply (people-first content, demonstrating E-E-A-T, satisfying user intent), but enforcement is continuous rather than through separate HCU updates.

## AI Citation Readiness (GEO signals)

Optimize for AI search engines (ChatGPT, Perplexity, Google AI Overviews):

- Clear, quotable statements with statistics/facts
- Structured data (especially for data points)
- Strong heading hierarchy (H1->H2->H3 flow)
- Answer-first formatting for key questions
- Tables and lists for comparative data
- Clear attribution and source citations

### AI Search Visibility & GEO (2025-2026)

**Google AI Mode** is Google's conversational AI search surface — powered by **Gemini 3.5 Flash** since I/O 2026 (May 2026) and now past **1 billion monthly users** globally. Unlike AI Overviews (which appear above organic results), AI Mode is a fully conversational experience with **zero organic blue links**, making AI citation the only visibility mechanism. It is a *distinct citation engine* from AI Overviews — the two share only ~14% of cited URLs — so optimize for both surfaces, not one (see the `seo-geo` skill).

**Key optimization strategies for AI citation:**
- **Structured answers:** Clear question-answer formats, definition patterns, and step-by-step instructions that AI systems can extract and cite
- **First-party data:** Original research, statistics, case studies, and unique datasets are highly cited by AI systems
- **Schema markup:** Article, FAQPage (Google retired FAQ *rich results* in May 2026, but the markup still aids AI parsing/entity resolution) or QAPage for genuine user Q&A, and structured content schemas help AI systems parse and attribute content
- **Topical authority:** AI systems preferentially cite sources that demonstrate deep expertise. Build content clusters, not isolated pages
- **Entity clarity:** Ensure brand, authors, and key concepts are clearly defined with structured data (Organization, Person schema)
- **Multi-platform tracking:** Monitor visibility across Google AI Overviews, AI Mode, ChatGPT, Perplexity, and Bing Copilot, not just traditional rankings. Treat AI citation as a standalone KPI alongside organic rankings and traffic.

**Generative Engine Optimization (GEO):**
Per Google's AI optimization guide, "AEO" and "GEO" are rebranded labels for SEO — AI Overviews and AI Mode are grounded in the same ranking and quality systems as classic Search. The optimization signals that matter (quotability, attribution, heading hierarchy, freshness) are SEO fundamentals applied to AI-search surfaces, not a separate discipline. Cross-reference the `seo-geo` skill for detailed workflows; both surfaces share the primary-source synthesis in `skills/seo-geo/references/google-ai-optimization-guide.md`.

## Content Freshness

- Publication date visible
- Last updated date if content has been revised
- Flag content older than 12 months without update for fast-changing topics

## Output

### Content Quality Score: XX/100

### E-E-A-T Breakdown
| Factor | Score | Key Signals |
|--------|-------|-------------|
| Experience | XX/25 | ... |
| Expertise | XX/25 | ... |
| Authoritativeness | XX/25 | ... |
| Trustworthiness | XX/25 | ... |

### AI Citation Readiness: XX/100

```

## File: skills/seo-schema/SKILL.md

```markdown
---
name: seo-schema
description: >
  Detect, validate, and generate Schema.org structured data. JSON-LD format
  preferred. Use when user says "schema", "structured data", "rich results",
  "JSON-LD", or "markup".
user-invocable: true
argument-hint: "[url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.2.0"
  category: seo
---

# Schema Markup Analysis & Generation

## Detection

1. Scan page source for JSON-LD `<script type="application/ld+json">`
2. Check for Microdata (`itemscope`, `itemprop`)
3. Check for RDFa (`typeof`, `property`)
4. Always recommend JSON-LD as primary format (Google's stated preference)

## Validation

- Check required properties per schema type
- Validate against Google's supported rich result types
- Test for common errors:
  - Missing @context
  - Invalid @type
  - Wrong data types
  - Placeholder text
  - Relative URLs (should be absolute)
  - Invalid date formats
- Flag deprecated types (see below)

## Schema Type Status (as of May 2026)

Read `references/schema-types.md` for the full list. Key rules:

### ACTIVE (recommend freely):
Organization, LocalBusiness, SoftwareApplication, WebApplication, Product (with Certification markup as of April 2025), ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

### VIDEO & SPECIALIZED (recommend freely):
BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode

See `schema/templates.json` for ready-to-use JSON-LD templates for these types.

> **JSON-LD and JavaScript rendering:** Per Google's December 2025 JS SEO guidance, structured data injected via JavaScript may face delayed processing. For time-sensitive markup (especially Product, Offer), include JSON-LD in the initial server-rendered HTML.

### NO RICH RESULTS — KEEP FOR AI:
- **FAQPage**: Google retired FAQ rich results for ALL sites on May 7, 2026 (supersedes the Aug 2023 gov/health restriction). No SERP feature anymore — but flag existing FAQPage at Info (not Critical), since the markup still aids AI Mode / AI Overviews entity resolution. For genuine user Q&A pages, use **QAPage**.

### DEPRECATED (never recommend):
- **HowTo**: Rich results removed September 2023
- **SpecialAnnouncement**: Deprecated July 31, 2025
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired June 2025
- **ClaimReview**: Retired from rich results June 2025
- **VehicleListing**: Retired from rich results June 2025
- **Practice Problem**: Retired from rich results late 2025
- **Dataset**: Retired from rich results late 2025
- **Book Actions**: Deprecated then reversed, still functional as of Feb 2026 (historical note)

## Generation

When generating schema for a page:
1. Identify page type from content analysis
2. Select appropriate schema type(s)
3. Generate valid JSON-LD with all required + recommended properties
4. Include only truthful, verifiable data. Use placeholders clearly marked for user to fill
5. Validate output before presenting

## Common Schema Templates

### Organization
``\`json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Company Name]",
  "url": "[Website URL]",
  "logo": "[Logo URL]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Phone]",
    "contactType": "customer service"
  },
  "sameAs": [
    "[Facebook URL]",
    "[LinkedIn URL]",
    "[Twitter URL]"
  ]
}
``\`

### LocalBusiness
``\`json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "telephone": "[Phone]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
``\`

### Article/BlogPosting
``\`json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Title]",
  "author": {
    "@type": "Person",
    "name": "[Author Name]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "image": "[Image URL]",
  "publisher": {
    "@type": "Organization",
    "name": "[Publisher]",
    "logo": {
      "@type": "ImageObject",
      "url": "[Logo URL]"
    }
  }
}
``\`

## Output

- `SCHEMA-REPORT.md`: detection and validation results
- `generated-schema.json`: ready-to-use JSON-LD snippets

### Validation Results
| Schema | Type | Status | Issues |
|--------|------|--------|--------|
| ... | ... | ✅/⚠️/❌ | ... |

### Recommendations
- Missing schema opportunities
- Validation fixes needed
- Generated code for implementation

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report connection error with status code. Suggest verifying URL and checking if the page requires authentication. |
| No schema markup found | Report that no JSON-LD, Microdata, or RDFa was detected. Recommend appropriate schema types based on page content analysis. |
| Invalid JSON-LD syntax | Parse and report specific syntax errors (missing brackets, trailing commas, unquoted keys). Provide corrected JSON-LD output. |
| Deprecated schema type detected | Flag the deprecated type with its retirement date. Recommend the current replacement type or advise removal if no replacement exists. |

```

## File: skills/seo-google/SKILL.md

Excerpt: first 180 of 348 lines.

```markdown
---
name: seo-google
description: >
  Google SEO APIs: Search Console (Search Analytics, URL Inspection, Sitemaps),
  PageSpeed Insights v5, CrUX field data with 25-week history, Indexing API v3,
  and GA4 organic traffic. Provides real Google field data for Core Web Vitals,
  indexation status, search performance, and organic traffic trends. Use when
  user says "search console", "GSC", "PageSpeed", "CrUX", "field data",
  "indexing API", "GA4 organic", "URL inspection", "google api setup",
  "real CWV data", "impressions", "clicks", "CTR", "position data",
  "LCP", "INP", "CLS", "FCP", "TTFB", or "Lighthouse scores".
user-invocable: true
argument-hint: "[command] [url|property]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.2.0"
  category: seo
---

# Google SEO APIs

Direct access to Google's own SEO data. Bridges the gap between crawl-based
analysis (existing claude-seo skills) and Google's real-time field data: actual
Chrome user metrics, real indexation status, search performance, and organic traffic.

All APIs are free. Setup requires a Google Cloud project with API key and/or
service account -- run `/seo google setup` for step-by-step instructions.

## Prerequisites

Before executing any command, check credentials:
``\`bash
python3 scripts/google_auth.py --check --json
``\`

Config file: `~/.config/claude-seo/google-api.json`
``\`json
{
  "service_account_path": "/path/to/service_account.json",
  "api_key": "<GOOGLE_API_KEY>",
  "default_property": "sc-domain:example.com",
  "ga4_property_id": "properties/123456789"
}
``\`

If missing, read `references/auth-setup.md` and walk the user through setup.

### Credential Tiers

| Tier | Detection | Available Commands |
|------|-----------|-------------------|
| **0** (API Key) | `api_key` present | `pagespeed`, `crux`, `crux-history`, `youtube`, `nlp` |
| **1** (OAuth/SA) | + OAuth token or service account | Tier 0 + `gsc`, `inspect`, `sitemaps`, `index` |
| **2** (Full) | + `ga4_property_id` configured | Tier 1 + `ga4`, `ga4-pages` |
| **3** (Ads) | + `ads_developer_token` + `ads_customer_id` | Tier 2 + `keywords`, `volume` |

Always communicate the detected tier before running commands.

## Quick Reference

| Command | What it does | Tier |
|---------|-------------|------|
| `/seo google setup` | Check/configure API credentials | -- |
| `/seo google pagespeed <url>` | PSI Lighthouse + CrUX field data | 0 |
| `/seo google crux <url>` | CrUX field data only (p75 metrics) | 0 |
| `/seo google crux-history <url>` | 25-week CWV trend analysis | 0 |
| `/seo google gsc <property>` | Search Console: clicks, impressions, CTR, position | 1 |
| `/seo google inspect <url>` | URL Inspection: index status, canonical, crawl info | 1 |
| `/seo google inspect-batch <file>` | Batch URL Inspection from file | 1 |
| `/seo google sitemaps <property>` | GSC sitemap status | 1 |
| `/seo google index <url>` | Submit URL to Indexing API | 1 |
| `/seo google index-batch <file>` | Batch submit up to 200 URLs | 1 |
| `/seo google ga4 [property-id]` | GA4 organic traffic report | 2 |
| `/seo google ga4-pages [property-id]` | Top organic landing pages | 2 |
| `/seo google youtube <query>` | YouTube video search (views, likes, duration) | 0 |
| `/seo google youtube-video <id>` | YouTube video details + top comments | 0 |
| `/seo google nlp <url-or-text>` | NLP entity extraction + sentiment + classification | 0 |
| `/seo google entities <url-or-text>` | Entity analysis only (for E-E-A-T) | 0 |
| `/seo google keywords <seed>` | Keyword ideas from Google Ads Keyword Planner | 3 |
| `/seo google volume <keywords>` | Search volume lookup from Keyword Planner | 3 |
| `/seo google entity <query>` | Knowledge Graph entity check | 0 |
| `/seo google safety <url>` | Web Risk URL safety check | 0 |
| `/seo google quotas` | Show rate limits for all APIs | -- |

---

## PageSpeed + CrUX

### `/seo google pagespeed <url>`

Combined Lighthouse lab data + CrUX field data.

**Script:** `python3 scripts/pagespeed_check.py <url> --json`
**Reference:** `references/pagespeed-crux-api.md`
**Default:** Both mobile + desktop strategies, all Lighthouse categories.

Output merges lab scores (point-in-time Lighthouse) with field data (28-day
Chrome user metrics). CrUX tries URL-level first, falls back to origin-level.

### `/seo google crux <url>`

CrUX field data only (no Lighthouse run). Faster.

**Script:** `python3 scripts/pagespeed_check.py <url> --crux-only --json`

### `/seo google crux-history <url>`

25-week CrUX History trends. Shows whether CWV metrics are improving, stable, or degrading.

**Script:** `python3 scripts/crux_history.py <url> --json`
**Reference:** `references/pagespeed-crux-api.md`

Output includes per-metric trend direction, percentage change, and weekly p75 values.

---

## Search Console

### `/seo google gsc <property>`

Search Analytics: clicks, impressions, CTR, position for last 28 days.

**Script:** `python3 scripts/gsc_query.py --property <property> --json`
**Reference:** `references/search-console-api.md`
**Default:** 28 days, dimensions=query,page, type=web, limit=1000.

Includes quick-win detection: queries at position 4-10 with high impressions.

### `/seo google inspect <url>`

URL Inspection: real indexation status from Google.

**Script:** `python3 scripts/gsc_inspect.py <url> --json`

Returns: verdict (PASS/FAIL), coverage state, robots.txt status, indexing state,
page fetch state, canonical selection, mobile usability, rich results.

### `/seo google inspect-batch <file>`

Batch inspection from a file (one URL per line). Rate limited to 2,000/day per site.

**Script:** `python3 scripts/gsc_inspect.py --batch <file> --json`

### `/seo google sitemaps <property>`

List submitted sitemaps with status, errors, warnings. Sitemap contents report
submitted counts only; URL Inspection API is the indexation truth for whether
specific URLs are indexed.

**Script:** `python3 scripts/gsc_query.py sitemaps --property <property> --json`

---

## Indexing API

### `/seo google index <url>`

Notify Google of a URL update.

**Script:** `python3 scripts/indexing_notify.py <url> --json`
**Reference:** `references/indexing-api.md`

The Indexing API is officially for JobPosting and BroadcastEvent/VideoObject pages.
Always inform the user of this restriction. Daily quota: 200 publish requests.

### `/seo google index-batch <file>`

Batch submit URLs from a file. Tracks quota usage.

**Script:** `python3 scripts/indexing_notify.py --batch <file> --json`

---

## GA4 Traffic

### `/seo google ga4 [property-id]`

Organic traffic report: daily sessions, users, pageviews, bounce rate, engagement.

```

## File: skills/seo-drift/SKILL.md

Excerpt: first 180 of 220 lines.

```markdown
---
name: seo-drift
description: >
  SEO drift monitoring: capture baselines of SEO-critical elements, detect changes,
  and track regressions over time. Git for SEO — baseline, diff, and track changes
  to your on-page SEO. Use when user says "SEO drift", "baseline", "track changes",
  "did anything break", "SEO regression", "compare SEO", "before and after",
  "monitor SEO changes", or "deployment check".
user-invocable: true
argument-hint: "baseline|compare|history <url>"
license: MIT
metadata:
  author: AgriciDaniel
  original_author: "Dan Colta (Pro Hub Challenge)"
  version: "2.2.0"
  category: seo
---

# SEO Drift Monitor (April 2026)

Git for your SEO. Capture baselines, detect regressions, track changes over time.

---

## Commands

| Command | Purpose |
|---------|---------|
| `/seo drift baseline <url>` | Capture current SEO state as a "known good" snapshot |
| `/seo drift compare <url>` | Compare current page state to stored baseline |
| `/seo drift history <url>` | Show change history and past comparisons |

---

## What It Captures

Every baseline records these SEO-critical elements:

| Element | Field | Source |
|---------|-------|--------|
| Title tag | `title` | `parse_html.py` |
| Meta description | `meta_description` | `parse_html.py` |
| Canonical URL | `canonical` | `parse_html.py` |
| Robots directives | `meta_robots` | `parse_html.py` |
| H1 headings | `h1` (array) | `parse_html.py` |
| H2 headings | `h2` (array) | `parse_html.py` |
| H3 headings | `h3` (array) | `parse_html.py` |
| JSON-LD schema | `schema` (array) | `parse_html.py` |
| Open Graph tags | `open_graph` (dict) | `parse_html.py` |
| Core Web Vitals | `cwv` (dict) | `pagespeed_check.py` |
| HTTP status code | `status_code` | `fetch_page.py` |
| HTML content hash | `html_hash` (SHA-256) | Computed |
| Schema content hash | `schema_hash` (SHA-256) | Computed |

---

## How Comparison Works

The comparison engine applies **17 rules across 3 severity levels**. Load
`references/comparison-rules.md` for the full rule set with thresholds,
recommended actions, and cross-skill references.

### Severity Levels

| Level | Meaning | Response Time |
|-------|---------|---------------|
| **CRITICAL** | SEO-breaking change, likely traffic loss | Immediate |
| **WARNING** | Potential impact, needs investigation | Within 1 week |
| **INFO** | Awareness only, may be intentional | Review at convenience |

---

## Storage

All data is stored locally in SQLite:

``\`
~/.cache/claude-seo/drift/baselines.db
``\`

### Tables

- **baselines**: Captured snapshots with all SEO elements
- **comparisons**: Diff results with triggered rules and severities

URL normalization ensures consistent matching: lowercase scheme/host, strip
default ports (80/443), sort query parameters, remove UTM parameters, strip
trailing slashes.

---

## Command: `baseline`

Captures the current state of a page and stores it.

**Steps:**
1. Validate URL (SSRF protection via `google_auth.validate_url()`)
2. Fetch page via `scripts/fetch_page.py`
3. Parse HTML via `scripts/parse_html.py`
4. Optionally fetch CWV via `scripts/pagespeed_check.py` (use `--skip-cwv` to skip)
5. Hash HTML body and schema content (SHA-256)
6. Store snapshot in SQLite

**Execution:**
``\`bash
python3 scripts/drift_baseline.py <url>
python3 scripts/drift_baseline.py <url> --skip-cwv
``\`

**Output:** JSON with baseline ID, timestamp, URL, and summary of captured elements.

---

## Command: `compare`

Fetches the current page state and diffs it against the most recent baseline.

**Steps:**
1. Validate URL
2. Load most recent baseline from SQLite (or specific `--baseline-id`)
3. Fetch and parse current page state
4. Run all 17 comparison rules
5. Classify findings by severity
6. Store comparison result
7. Output JSON diff report

**Execution:**
``\`bash
python3 scripts/drift_compare.py <url>
python3 scripts/drift_compare.py <url> --baseline-id 5
python3 scripts/drift_compare.py <url> --skip-cwv
``\`

**Output:** JSON with all triggered rules, old/new values, severity, and actions.

After comparison, offer to generate an HTML report:
``\`bash
python3 scripts/drift_report.py <comparison_json_file> --output drift-report.html
``\`

---

## Command: `history`

Shows all baselines and comparisons for a URL.

**Execution:**
``\`bash
python3 scripts/drift_history.py <url>
python3 scripts/drift_history.py <url> --limit 10
``\`

**Output:** JSON array of baselines (newest first) with timestamps and comparison summaries.

---

## Cross-Skill Integration

When drift is detected, recommend the appropriate specialized skill:

| Finding | Recommendation |
|---------|----------------|
| Schema removed or modified | Run `/seo schema <url>` for full validation |
| CWV regression | Run `/seo technical <url>` for performance audit |
| Title or meta description changed | Run `/seo page <url>` for content analysis |
| Canonical changed or removed | Run `/seo technical <url>` for indexability check |
| Noindex added | Run `/seo technical <url>` for crawlability audit |
| H1/heading structure changed | Run `/seo content <url>` for E-E-A-T review |
| OG tags removed | Run `/seo page <url>` for social sharing analysis |
| Status code changed to error | Run `/seo technical <url>` for full diagnostics |

---

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable | Report error from `fetch_page.py`. Do not guess state. Suggest user verify URL. |
| No baseline exists for URL | Inform user and suggest running `baseline` first. |
| SSRF blocked (private IP) | Report `validate_url()` rejection. Never bypass. |
```

