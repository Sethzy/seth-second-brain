---
type: wiki_article
title: Agentic Marketing Workflows
updated_at: 2026-06-19
status: active
source_count: 25
tags:
  - marketing
  - agentic-workflows
  - stripe
  - anthropic
  - skills
  - enablement
---

# Agentic Marketing Workflows

> Sources: Stripe FDA Marketing job posting, Rish Gupta AI operator essay, Andrew Yeung Stripe FDA X post, Anthropic growth-marketing article, Eric Siu AI Marketing Skills README, jet-seo local project, TheCraigHewitt SEO Machine repository snapshot, AgriciDaniel Claude SEO repository snapshot, Ivan Falco ads-skills repository snapshot, Corey Haines marketingskills repository snapshot, paid-ads Claude Code transcript, Bryant Chou Ploy launch X post, JAZII X content research agent article, Last30Days marketing workflow sweep, plus related GTM/skill/wiki pages.
> Raw: [Stripe FDA Marketing job posting](../../raw/intentional/pasted/2026-06-17-stripe-forward-deployed-ai-accelerator-marketing-job-posting.md); [Rish Gupta AI operator essay](../../raw/intentional/web/2026-06-19-the-ai-operator-biggest-role-in-silicon-valley.md); [Andrew Yeung Stripe FDA X post](../../raw/intentional/x/2051444322927526248-andruyeung-stripe-just-created-a-role-that-didn-t-exist-12-months-ago-and-they-re-paying-m.md); [Anthropic growth marketing article](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md); [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md); [jet-seo local project snapshot](../../raw/intentional/pasted/2026-06-17-jet-seo-atlas-seo-content-pipeline-local-project.md); [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md); [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md); [Ivan Falco ads-skills repository snapshot](../../raw/intentional/web/2026-06-18-ivangfalco-ads-skills-repository-snapshot.md); [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md); [How To Get Unlimited Leads Using Claude Code For Paid Ads transcript](../../raw/intentional/youtube/2026-06-18-how-to-get-unlimited-leads-using-claude-code-for-paid-ads-tr.md); [Bryant Chou Ploy launch X post](../../raw/intentional/x/2026-06-18-bryant-chou-ploy-launch-x-post.md); [JAZII X content research agent article](../../raw/intentional/pasted/2026-06-19-jazii-x-content-research-agent-article.md); [Marketing workflow Last30Days raw](../../raw/sweeps/last30days/ai-marketing-workflow-transformation-stripe-anthropic-claude-code-marketers-agents-skills-raw.md); [Marketing workflow Last30Days digest](../../staging/last30days/2026-06-17-ai-marketing-workflow-transformation-stripe-anthropic-claude-code-marketers-agents-skills-digest.md)

## Overview

Marketing-centric AI work is not simply autonomous content generation. The stronger pattern is workflow transformation: marketers start with recurring work, encode the context and standards that make the work good, run tools or agents against real inputs, review the output, then feed performance and adoption data back into the next run.

Stripe's Forward Deployed AI Accelerator role is the clearest local frame. The role is embedded with roughly 20 marketers, identifies high-leverage workflow transformations, builds tools, agents, automations, and skills, coaches marketers from first win to self-sufficiency, scales reusable patterns across cohorts, documents playbooks, tracks maturity, and prepares marketers for autonomous multi-agent workflows. Success is measured by permanently transformed workflows and whether marketers start tasks with AI by default.

The Rish Gupta/Andrew Yeung material sharpens the role category: this is an AI-operator function, not a normal marketing role with AI tools attached. The operator sits between the work and the technology, learns the repetitive and labor-intensive parts of a function, ranks them by impact, builds or buys narrow tools in short cycles, educates the ICs doing the work, and hands off reusable patterns. That maps directly to Stripe FDA marketing: adoption, coaching, and redesigning the workflow matter as much as the technical build.

Anthropic's marketing article is the strongest exact operating proof. Its growth-marketing example does not stop at ad copy generation; it packages brand/product rules, Figma production, Google Ads RSA constraints, manual review, and CSV export into a repeatable workflow. The same article describes marketing uses across influencer scripts, customer case studies, web workflows, product launch briefs, and partner enablement.

The practical definition for this wiki: agentic marketing is a system of reusable loops across research, creative, content, websites, lifecycle, and analytics. Each loop has sources, brand constraints, tool access, quality gates, human approval, and measurement. Autonomous content is only one output surface.

Ivan Falco's ads-skills repo and paid-ads Claude Code transcript are the current concrete public example for the paid-media segment. The repo turns marketing strategy into local skills and API scripts for LinkedIn, Meta, and Google Ads, while the transcript shows the operating loop: gather company/product evidence, build an ICP and audience intelligence brief, split audience/list building from ad generation, use customer/review/social language for copy, render creative from templates and brand assets, then stage platform uploads behind human approval. This is useful for Seth because it looks like marketing FDA work in miniature: encode the workflow, connect the tools, keep credentials scoped, and turn a multi-day marketer workflow into a repeatable reviewed run.

Bryant Chou's Ploy launch is a useful commercial expression of the same thesis: the website becomes the operating surface for growth rather than a static asset. The post positions Ploy as coordinating site, brand, CMS, CRM, campaigns, analytics, SEO, AEO, and customer data, with daily reports and approval before shipping. Named examples include ABM pages for Hex, Clay-data-powered programmatic SEO, and landing pages per ad for TNT Growth. The strategic hook is that "AI marketing" shifts from asset generation toward a website-centered growth agent with connected data and review gates.

The new SEO/content captures sharpen the implementation shape. SEO Machine shows a Claude Code workspace where context files, commands, agents, data modules, and publishing integrations are organized around repeatable content and landing-page work. The refreshed Claude SEO snapshot shows the audit/plugin version of the same idea: commands, sub-skills, specialist agents, extensions, tests, and local reports. JAZII's X article supplies the social/content research loop: use the agent to watch the market, extract patterns, and propose angles before asking AI to draft.

Corey Haines' `marketingskills` repo is the broad operating-system version of this pattern. It packages 45 cross-agent marketing skills around a shared `product-marketing` context file, then fans out into SEO audit, AI SEO, programmatic SEO, content strategy, copywriting, CRO, analytics, RevOps, lifecycle, social, video, offers, launch, pricing, and related tasks. The repo also includes eval files, a Claude plugin marketplace, Agent Skills installation paths, zero-dependency CLI tools, and a marketing tool registry. For Seth, the durable idea is not to install every skill globally; it is to borrow the routing pattern: create product/audience/positioning context first, then load the narrow marketing skill and tool guide needed for the current workflow.

## Marketing-Centric Means

- **Workflow-first:** start from work marketers repeat weekly, not from an AI feature list.
- **Research-before-generation:** collect market, customer, search, social, and performance signals before asking the system to draft.
- **Brand-and-product grounded:** durable context includes voice, positioning, product truth, offer constraints, customer proof, legal/compliance limits, and channel-specific rules.
- **Tool-connected:** the workflow reads and writes actual files, design tools, CMSs, ad exports, analytics, CRM, or marketing automation systems where appropriate.
- **Review-gated:** generation, analysis, and publishing are separate stages; humans approve public artifacts and side effects.
- **Measured:** loops track campaign performance, artifact quality, workflow adoption, time saved, and whether the marketer became more self-sufficient.
- **Reusable:** a workflow that works for one marketer should become a skill, template, or playbook for peers.

## Segment Map

- [SEO/AEO/GEO Content Systems](seo-aeo-geo-content-systems.md): keyword, SERP, answer-engine, and publication workflows with validation gates.
- [Performance Marketing Creative Ops](performance-marketing-creative-ops.md): ad variants, Figma/creative production, RSA/Meta constraints, and feedback loops.
- [Autonomous Websites And Landing Pages](autonomous-websites-and-landing-pages.md): account, keyword, social, and campaign pages generated from enrichment and measured downstream.
- [UGC And Creator Systems](ugc-and-creator-systems.md): synthetic creator/product-video workflows, paid-social variants, and governance risks.
- [Content Ops And Editorial Systems](content-ops-and-editorial-systems.md): brand voice, product marketing, launch briefs, case studies, scripts, editorial gates, and repurposing.
- [Lifecycle CRM And Marketing Ops](lifecycle-crm-and-marketing-ops.md): scoring, routing, nurture, CRM/Marketo/Salesforce integrations, and consent/audit constraints.
- [Marketing Analytics And FDA Enablement](marketing-analytics-and-fda-enablement.md): attribution, experiment loops, dashboards, and the internal enablement metrics for transforming marketers.

## Operating Model

A useful agentic marketing loop has five layers:

1. **Context:** campaign brief, audience, product truth, brand rules, prior examples, source evidence, and channel constraints.
2. **Execution:** skills, scripts, agents, MCPs, or automations that run against files, APIs, creative tools, CMSs, ads exports, analytics, and CRM.
3. **Validation:** editorial rubric, SEO/AEO checks, product/legal review, platform constraints, hallucination checks, and source provenance.
4. **Distribution:** CMS publish, ad upload, social schedule, landing-page routing, lifecycle sequence, outbound asset, or sales enablement surface.
5. **Feedback:** performance, attribution, qualitative review, cohort adoption, and workflow maturity update.

## Sources

This page synthesizes exact captures and staged sweeps. The sweep evidence supports trend vocabulary, while exact company/tool claims should be traced to the raw captures listed below.

## Raw Links

- [Stripe FDA Marketing job posting](../../raw/intentional/pasted/2026-06-17-stripe-forward-deployed-ai-accelerator-marketing-job-posting.md)
- [Rish Gupta AI operator essay](../../raw/intentional/web/2026-06-19-the-ai-operator-biggest-role-in-silicon-valley.md)
- [Andrew Yeung Stripe FDA X post](../../raw/intentional/x/2051444322927526248-andruyeung-stripe-just-created-a-role-that-didn-t-exist-12-months-ago-and-they-re-paying-m.md)
- [Anthropic growth marketing article](../../raw/intentional/web/2026-06-11-anthropic-growth-marketing-article.md)
- [Eric Siu AI Marketing Skills README](../../raw/intentional/web/2026-06-11-eric-siu-ai-marketing-skills-readme.md)
- [jet-seo local project snapshot](../../raw/intentional/pasted/2026-06-17-jet-seo-atlas-seo-content-pipeline-local-project.md)
- [TheCraigHewitt SEO Machine repository snapshot](../../raw/intentional/web/2026-06-19-thecraighewitt-seomachine-repository-snapshot.md)
- [AgricIDaniel Claude SEO repository snapshot, June 2026](../../raw/intentional/web/2026-06-19-agricidaniel-claude-seo-repository-snapshot-june-2026.md)
- [Ivan Falco ads-skills repository snapshot](../../raw/intentional/web/2026-06-18-ivangfalco-ads-skills-repository-snapshot.md)
- [Corey Haines marketingskills repository snapshot](../../raw/intentional/web/2026-06-19-corey-haines-marketingskills-repository-snapshot-june-2026.md)
- [How To Get Unlimited Leads Using Claude Code For Paid Ads transcript](../../raw/intentional/youtube/2026-06-18-how-to-get-unlimited-leads-using-claude-code-for-paid-ads-tr.md)
- [Bryant Chou Ploy launch X post](../../raw/intentional/x/2026-06-18-bryant-chou-ploy-launch-x-post.md)
- [JAZII X content research agent article](../../raw/intentional/pasted/2026-06-19-jazii-x-content-research-agent-article.md)
- [Marketing workflow Last30Days raw](../../raw/sweeps/last30days/ai-marketing-workflow-transformation-stripe-anthropic-claude-code-marketers-agents-skills-raw.md)
- [Marketing workflow Last30Days digest](../../staging/last30days/2026-06-17-ai-marketing-workflow-transformation-stripe-anthropic-claude-code-marketers-agents-skills-digest.md)
- [LinkedIn post lead on Anthropic marketing guide, incomplete](../../staging/incomplete-captures/web/2026-06-17-linkedin-post-lead-anthropic-guide-on-using-claude-for-marke.md)

## Open Questions

- Which Stripe-relevant proof artifact should Seth build first: an ad-variant loop, an SEO/AEO content loop, a lifecycle/CRM workflow, or a marketing enablement dashboard?
- What maturity rubric would show that a marketer has moved from first AI win to self-sufficient workflow designer?
- Which workflows need full human approval, and which can safely run to draft/staging only?
- What should count as a reusable marketing skill in Seth's portfolio: `SKILL.md`, repo runbook, working demo, video walkthrough, or case study?
- Which `marketingskills` subset should Seth trial first for Stripe-style proof: product-marketing plus AI SEO/content/analytics, or product-marketing plus CRO/copywriting/experimentation?

## See Also

- [SEO/AEO/GEO Content Systems](seo-aeo-geo-content-systems.md)
- [Performance Marketing Creative Ops](performance-marketing-creative-ops.md)
- [Marketing Analytics And FDA Enablement](marketing-analytics-and-fda-enablement.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [Agent Skill Libraries And Requirements](../ai-coding/agent-skill-libraries-and-requirements.md)
- [Agentic Artifact Surfaces](../ai-knowledge-work/agentic-artifact-surfaces.md)
