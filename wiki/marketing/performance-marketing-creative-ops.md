---
type: wiki_article
title: Performance Marketing Creative Ops
updated_at: 2026-06-18
status: active
source_count: 8
tags:
  - marketing
  - performance-marketing
  - ads
  - creative-ops
  - google-ads
  - meta-ads
---

# Performance Marketing Creative Ops

> Sources: Anthropic growth-marketing article, Hesamation X capture, performance marketing Last30Days sweep, Eric Siu AI Marketing Skills README, Agency Agents README, Ivan Falco ads-skills repository snapshot, paid-ads Claude Code transcript.
> Raw: [Anthropic growth marketing article](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md); [Hesamation X capture on Anthropic growth marketing](../../raw/intentional/x/2031497289617883451-hesamation-anthropic-s-entire-growth-marketing-team-has-been-one-person-for-10-months-the.md); [Performance marketing Last30Days raw](../../raw/sweeps/last30days/performance-marketing-ai-ad-generation-google-ads-meta-ads-creative-variants-raw.md); [Performance marketing Last30Days digest](../../staging/last30days/2026-06-17-performance-marketing-ai-ad-generation-google-ads-meta-ads-creative-variants-digest.md); [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md); [Agency Agents README](../../raw/intentional/web/2026-06-11-agency-agents-readme.md); [Ivan Falco ads-skills repository snapshot](../../raw/intentional/web/2026-06-18-ivangfalco-ads-skills-repository-snapshot.md); [How To Get Unlimited Leads Using Claude Code For Paid Ads transcript](../../raw/intentional/youtube/2026-06-18-how-to-get-unlimited-leads-using-claude-code-for-paid-ads-tr.md)

## Overview

Performance marketing is the strongest evidence that AI marketing should be a production workflow, not a copy prompt. The job is to turn campaign data, platform constraints, brand/product rules, and prior performance into reviewable creative variants and measurable experiments.

Anthropic's official growth-marketing article gives the clean example: a marketer used Claude Code for Figma ad production and Google Ads responsive search ad workflows. The workflow compressed ad creation, but its structure matters more than the time claim: campaign data and existing copy go in, Claude applies brand/product accuracy and Google Ads constraints, the marketer reviews, and the output is exported for upload.

The Hesamation X capture is useful as third-party social evidence around an expanded version of the same pattern: export ads/performance data, use Claude to flag weak ads, generate headline/description variations with subagents, and connect creative iteration to Meta Ads tooling. Treat it as a lead/corroboration source, not official Anthropic evidence.

Ivan Falco's ads-skills repo and paid-ads transcript make the pattern more concrete: a local Claude Code setup can package paid-media strategy files, platform API scripts, credential onboarding, and approval rules into a system that researches an ICP, builds LinkedIn/Meta audiences, generates ad concepts, renders creative variants, and stages campaigns through ad-platform APIs. The transcript's durable loop is two-agent: an audience/list builder creates ICP matrices, company/contact lists, and enrichment-ready audiences, while an ad generator mines landing pages, ad-library screenshots, reviews, Reddit/G2/Trustpilot language, sales collateral, brand assets, and winning templates to produce upload-ready concepts. The repo's operational caution is important: live campaigns should start paused and remain human-reviewed before spend.

## Workflow Pattern

1. **Ingest:** campaign objective, audience, offer, landing page, prior copy, product claims, performance export, platform constraints, and brand rules.
2. **Diagnose:** find weak ads, fatigued creative, missing angles, unclear offers, mismatched landing pages, or platform-policy risks.
3. **Build audience:** turn ICP/account criteria into company/contact lists, enrichment jobs, and platform-specific audience uploads where credentials and consent permit.
4. **Generate:** create platform-specific variants for RSA, static/social ads, UGC scripts, hooks, descriptions, thumbnails, Figma templates, or generated-image concepts.
5. **Validate:** check claims, voice, product accuracy, legal/compliance, character limits, forbidden terms, naming conventions, and campaign settings.
6. **Review and export:** produce CSV, design files, or upload-ready paused campaigns for human approval.
7. **Measure:** compare performance by angle, channel, format, audience, and landing page, then feed results back into the next generation pass.

## Why This Is Marketing-Centric

The agent is not replacing taste or performance judgment. It is compressing the low-level production and analysis loop so the marketer can test more hypotheses while staying inside product truth and platform constraints.

The durable artifact for a Stripe-style FDA interview is a working creative-ops loop: one input folder, one brand/product rule file, one ads export, one generation command, one validation report, and one reviewable export.

## Sources

Exact company claims should come from the Anthropic raw article. Sweep items are used for market trend shape and tool leads. The Hesamation X post is captured raw but remains third-party social evidence. The Ivan Falco repo/transcript are strongest as implementation shape: repo-native skills plus ad-platform APIs, paused-campaign defaults, audience building, enrichment, creative templates, and human approval gates.

## Raw Links

- [Anthropic growth marketing article](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md)
- [Hesamation X capture on Anthropic growth marketing](../../raw/intentional/x/2031497289617883451-hesamation-anthropic-s-entire-growth-marketing-team-has-been-one-person-for-10-months-the.md)
- [Performance marketing Last30Days raw](../../raw/sweeps/last30days/performance-marketing-ai-ad-generation-google-ads-meta-ads-creative-variants-raw.md)
- [Performance marketing Last30Days digest](../../staging/last30days/2026-06-17-performance-marketing-ai-ad-generation-google-ads-meta-ads-creative-variants-digest.md)
- [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md)
- [Agency Agents README](../../raw/intentional/web/2026-06-11-agency-agents-readme.md)
- [Ivan Falco ads-skills repository snapshot](../../raw/intentional/web/2026-06-18-ivangfalco-ads-skills-repository-snapshot.md)
- [How To Get Unlimited Leads Using Claude Code For Paid Ads transcript](../../raw/intentional/youtube/2026-06-18-how-to-get-unlimited-leads-using-claude-code-for-paid-ads-tr.md)

## Open Questions

- What minimum dataset should Seth use to demo the loop without exposing private ad account data?
- Should the first artifact target Google Ads RSA, Meta static variants, Figma creatives, or landing-page variants?
- What approval gate is sufficient before upload: human review checklist, diff report, platform preview, or all three?
- Which performance fields should be normalized for feedback: impressions, CTR, CPC, CPA, CVR, pipeline, revenue, fatigue, or qualitative reviewer score?
- What no-credentials demo should mirror Ivan's workflow: audience intelligence brief, paused-campaign JSON, creative pack, or all three?

## See Also

- [Agentic Marketing Workflows](agentic-marketing-workflows.md)
- [Marketing Analytics And FDA Enablement](marketing-analytics-and-fda-enablement.md)
- [UGC And Creator Systems](ugc-and-creator-systems.md)
- [Autonomous Websites And Landing Pages](autonomous-websites-and-landing-pages.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
