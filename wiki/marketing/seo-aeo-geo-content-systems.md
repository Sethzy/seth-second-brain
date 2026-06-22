---
type: wiki_article
title: SEO AEO GEO Content Systems
updated_at: 2026-06-19
status: active
source_count: 9
tags:
  - marketing
  - seo
  - aeo
  - geo
  - content-ops
  - search
---

# SEO AEO GEO Content Systems

> Sources: jet-seo local project snapshot, TheCraigHewitt SEO Machine repository snapshot, AgriciDaniel Claude SEO README and refreshed repository snapshot, Corey Haines marketingskills repository snapshot, Eric Siu AI Marketing Skills README, SEO/AEO/GEO Last30Days sweep, and related GTM campaign workflows.
> Raw: [jet-seo local project snapshot](../../raw/intentional/pasted/2026-06-17-jet-seo-atlas-seo-content-pipeline-local-project.md); [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md); [AgriciDaniel Claude SEO README](../../raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md); [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md); [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md); [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md); [SEO/AEO/GEO Last30Days raw](../../raw/sweeps/last30days/seo-aeo-geo-llm-search-ai-search-visibility-marketing-workflows-raw.md); [SEO/AEO/GEO Last30Days digest](../../staging/last30days/2026-06-17-seo-aeo-geo-llm-search-ai-search-visibility-marketing-workflows-digest.md)

## Overview

SEO/AEO/GEO is the clearest current subdomain where marketing-centric AI becomes a machine-executable workflow. The goal is not just to write articles faster. It is to run a pipeline that discovers demand, validates opportunities, creates briefs, generates drafts, checks answer/citation readiness, publishes, links, and re-measures.

The local `jet-seo` project is the strongest implementation example. It defines an Ahrefs-driven Atlas SEO content pipeline with four phases: research, prioritization, briefs, and production. Its state lives in `WORKFLOW.md`, `MEMORY_STATE.md`, and CSV trackers. The execution model is batch-then-advance: all eligible keywords move through a step before the next step starts. It has one explicit human handoff for Ahrefs export, then agent-executable work through SERP analysis, scoring, briefs, MDX generation, internal linking, and validation.

Claude SEO / Codex SEO is the specialist-audit example. It packages technical SEO, content quality, Schema.org, AI search/GEO, local, e-commerce, and international SEO into commands and specialist agents. Its useful contribution is the insistence on falsifiable recommendations, primary-source guidance, and measurable failure checks. The refreshed June 2026 repository snapshot shows the system evolving beyond a README into a plugin surface: marketplace metadata, command docs, architecture docs, extensions, hooks, tests, and per-domain `SKILL.md` files.

TheCraigHewitt's SEO Machine is the complementary content-production workspace. Where Claude SEO emphasizes audit and falsifiable recommendations, SEO Machine emphasizes turning context into output: brand voice, style guides, target keywords, competitor analysis, internal-link maps, CRO best practices, AI-citation targets, Claude Code commands, specialist agents, Python data-source modules, and WordPress/Yoast publishing. For Seth's purposes, it is a strong reference for a repo-shaped SEO/content machine rather than a one-off prompt.

Corey Haines' `marketingskills` repo supplies the portable, cross-agent version of the SEO/content lane. It is less deep than Claude SEO as an audit plugin, but broader as a marketing system: `seo-audit`, `ai-seo`, `programmatic-seo`, `schema`, `site-architecture`, `content-strategy`, `analytics`, and `product-marketing` are separate skills that all expect shared positioning context first. This makes it useful as a menu of reusable workflow contracts for a Codex or Claude workspace where Seth wants SEO/AEO/GEO work to stay tied to ICP, offer, conversion goal, and measurement.

## AEO/GEO Framing

AEO and GEO should be treated as answer/citation visibility layers on top of SEO fundamentals, not as magic new hacks. The Last30Days sweep showed repeated market vocabulary around ChatGPT, Perplexity, AI Overviews, direct answers, AI-ready schema, and visibility gap analysis. The more durable workflow is:

1. Identify real questions, jobs-to-be-done, comparison needs, and commercial/informational intent.
2. Build pages with clear entities, definitions, steps, examples, evidence, FAQs, comparison tables, and source-backed claims.
3. Validate technical crawlability, schema, internal links, content quality, and citation-friendly passages.
4. Track visibility across search and AI-answer surfaces without assuming one metric explains everything.

## Workflow Pattern

- **Research:** seed discovery, Ahrefs/keyword exports, SERP analysis, competitor/page review, and question mining.
- **Prioritization:** score by relevance, difficulty, value, funnel stage, and ability to provide original evidence.
- **Briefs:** define query cluster, search intent, audience, outline, required evidence, internal links, CTA, and AEO/GEO checks.
- **Production:** generate MDX/content, sync frontmatter, add links, validate voice and originality, then publish or stage.
- **Validation:** ensure commercial pages include comparisons/FAQs/stats where appropriate and informational pages include definitions, steps, and evidence.
- **Measurement:** monitor rankings, traffic, AI-answer mentions, citations, conversions, and refresh triggers.

Two implementation shapes are now worth separating:

- **Pipeline workspace:** `jet-seo` and SEO Machine use state files, context folders, commands, trackers, output folders, and publishing hooks to move content from research to draft to publishable artifact.
- **Specialist audit plugin:** Claude SEO uses a command surface, sub-skills, specialist agents, data extensions, tests, and reports to diagnose a site and produce prioritized recommendations.
- **Portable skill pack:** `marketingskills` splits SEO/AEO/GEO into focused, installable skills that route through product-marketing context and adjacent analytics/CRO/content skills.

## Sources

The exact workflow details come from `jet-seo`, SEO Machine, Claude SEO, and `marketingskills`. The sweep is used only to establish that AEO/GEO/AI-search visibility is a live marketing topic in the last 30 days.

## Raw Links

- [jet-seo local project snapshot](../../raw/intentional/pasted/2026-06-17-jet-seo-atlas-seo-content-pipeline-local-project.md)
- [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md)
- [AgriciDaniel Claude SEO README](../../raw/intentional/web/2026-06-11-agricidaniel-claude-seo-readme.md)
- [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md)
- [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md)
- [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md)
- [SEO/AEO/GEO Last30Days raw](../../raw/sweeps/last30days/seo-aeo-geo-llm-search-ai-search-visibility-marketing-workflows-raw.md)
- [SEO/AEO/GEO Last30Days digest](../../staging/last30days/2026-06-17-seo-aeo-geo-llm-search-ai-search-visibility-marketing-workflows-digest.md)

## Open Questions

- Which primary AEO/GEO guidance should be captured next: Google AI optimization, Microsoft AEO/GEO, Perplexity/ChatGPT visibility docs, or tool-specific docs?
- What is Seth's minimum AEO/GEO validation rubric for a portfolio project?
- Should `jet-seo` become a public proof-of-work artifact, a case-study screenshot, or a private reference implementation?
- Should Seth's Stripe proof artifact borrow more from SEO Machine's content-production workspace or Claude SEO's audit-plugin architecture?
- Which AI-search visibility tools deserve exact capture and testing?
- Which `marketingskills` SEO subset should be converted into a local proof workflow: `ai-seo`, `seo-audit`, `programmatic-seo`, or the product-marketing to content-strategy to analytics chain?

## See Also

- [Agentic Marketing Workflows](agentic-marketing-workflows.md)
- [Content Ops And Editorial Systems](content-ops-and-editorial-systems.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [Agent Skill Libraries And Requirements](../ai-coding/agent-skill-libraries-and-requirements.md)
