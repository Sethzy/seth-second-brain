---
type: wiki_article
title: GTM Waterfall Enrichment APIs
updated_at: 2026-06-16
status: active
source_count: 16
tags:
  - gtm
  - enrichment
  - waterfall
  - agents
  - revops
  - company-research
  - mcp
---

# GTM Waterfall Enrichment APIs

> Sources: Deepline homepage, 2026-06-10 capture; Seth pasted Deepline note, 2026-06-10; Seth pasted Codex maxxing/GTM bundle, 2026-06-10; Shiv Sakhuja X post, 2026-04-24; Jay Sahnan X post, 2026-04-24; Browserbase company-research skill, 2026-06-11 capture; Seth pasted harness/company-research bundle, 2026-06-11; Browserbase GTM page, 2026-06-11 capture; Seth pasted Acme bundle, 2026-06-11
> Raw: [Deepline homepage](../../raw/intentional/web/2026-06-10-deepline-gtm-api-designed-for-agents.md); [GTM API waterfall enrichment links](../../raw/intentional/pasted/2026-06-10-gtm-api-waterfall-enrichment-links.md); [Codex maxxing and GTM agent opportunity bundle](../../raw/intentional/pasted/2026-06-10-codex-maxxing-and-gtm-agent-opportunity-bundle.md); [Shiv Sakhuja Gooseworks CLI X post](../../raw/intentional/x/2047780107339903214-shivsakhuja-launching-gooseworks-cli-a-unified-api-for-your-ai-agents-to-access-dozens-of.md); [Jay Sahnan company-research X post](../../raw/intentional/x/2047730585313980499-jaysahnan-i-just-open-sourced-one-of-our-internal-gtm-skills-introducing-the-company-resea.md); [Browserbase company-research skill](../../raw/intentional/web/2026-06-11-browserbase-company-research-skill.md); [harness/company-research/video workflow bundle](../../raw/intentional/pasted/2026-06-11-harness-codex-company-research-video-workflow-and-clay-mcp-bundle.md); [Browserbase GTM industry page](../../raw/intentional/web/2026-06-11-browserbase-gtm-industry-page.md); [Acme GTM OS pasted bundle](../../raw/intentional/pasted/2026-06-11-acme-gtm-os-agentic-sales-marketing-and-design-bundle.md)
> 2026-06-16 additions: [Acme/eGiro first-10-day goals](../../raw/intentional/pasted/2026-06-16-acme-egiro-first-10-day-goals-and-side-projects.md); [enterprise sales X profile digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-digest.md); [GTM workspace agentic outbound and Acme OS docs](../../raw/intentional/pasted/2026-06-16-gtm-workspace-agentic-outbound-and-acme-os-docs.md); [sales plugin account-research and outreach skills](../../raw/intentional/pasted/2026-06-16-sales-plugin-account-research-and-outreach-skills.md); [enterprise sales X profile backdated digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-backdated-digest.md); [Fivos Aresti posts 101-190](../../raw/sweeps/x/2026-06-16-fivosaresti-posts-101-190.md)

## Overview

Deepline is a concrete lead for an agent-native GTM API layer: one interface that connects Codex, Claude Code, Hermes, or custom apps to many GTM integrations. Seth's note summarizes the core appeal as "one api to do waterfall enrichment."

The homepage positions Deepline around production GTM systems, workflows in code, provider access through one account, and saving results into the user's own database. The example prompt is directly in the target use case: find competitors, scrape LinkedIn engagers, waterfall enrich emails, and create outbound campaigns per persona.

The newer captures add two adjacent patterns. Gooseworks CLI presents a unified data-access layer for agents doing GTM/growth work across Apollo, Fiber, Crustdata, People Data Labs, Nyne, Aviato, Apify, Serper, Exa, and other sources. Browserbase's `/company-research` skill gives a concrete agent-skill structure: discover target companies with Browserbase Search API, run Plan -> Research -> Synthesize for each company, score ICP fit, and output both a research report and CSV. Seth also noted that Clay has an MCP, which should be verified with a full source capture before treating it as more than a lead.

The Acme bundle turns this into an account-data pipe: scrape the licensed-company TAM, map stakeholders, refresh job changes every two weeks, run trigger monitors, and use provider-specific tools only when they fit the data type.

The Sunder sync turns older local scrape work into retrievable raw evidence: TAM CSVs, SG insurance/property datasets, food/agri, manufacturing, freight, distributor-pricing, email-output, Clay/export, and other market-list files. These files are preserved as raw snapshots and should be inspected directly before using them for enrichment schemas, account universes, or campaign inputs.

## Key Ideas

- Waterfall enrichment is a natural fit for agents because the workflow has multiple provider calls, fallbacks, confidence checks, and structured outputs.
- A single GTM API can hide vendor-specific integration complexity while letting the agent work in code rather than fragile browser flows.
- The durable system should save enriched records into Seth-controlled storage, not just return transient agent chat output.
- Provider access, enrichment costs, and campaign actions need auditability before any outbound workflow becomes trusted.
- Deepline belongs on the opportunity radar as both a tool to try and a market signal: agent-native GTM infrastructure is becoming a product category.
- The pasted GTM bundle adds comparable market evidence: Claude Code-ready GTM tools are increasingly exposing APIs, MCP servers, lookalike search, free search endpoints, buying-window signals, and agent-friendly enrichment.
- Gooseworks is another example of the same product shape: one command installs a unified API layer so agents can call many GTM data providers without individual subscriptions/API-key handling in the prompt.
- Company-research skills should produce both human-readable research files and structured CSV outputs, so the result can feed campaign systems instead of dying in chat.
- Browserbase's depth modes suggest a useful knob for GTM agents: quick/deep/deeper modes trade scale against research quality.
- Clay MCP is a high-priority source to verify because Clay already sits close to Seth's GTM workflow surface.
- Trigger.dev-style scheduled scrapers are a good fit for regulated/event data: scrape, validate, store, and only then sync to outreach tools.
- A provider map should choose tools by job: Clay orchestration, Prospeo/BlitzAPI contact finding, OpenWeb Ninja search scraping, Parallel deep research, Apify/RapidAPI structured scrapers, and Browserbase/browser-use for click-through workflows.

## Enterprise Account Data Pipe Implications

The 2026-06-16 enterprise-sales captures add a data-pipe constraint: account intelligence should support patient, high-context selling, not just bulk enrichment. The useful object is a sourced account graph with freshness dates, confidence levels, and "why now" triggers.

Immediate implications:

- Crustdata and similar APIs belong in the stakeholder and company-change layer: people, companies, job changes, hiring signals, funding, and LinkedIn-adjacent enrichment.
- Clay MCP or Clay workflows are useful orchestration surfaces, but raw provider outputs should still be copied into Seth-controlled storage before agent summaries become CRM facts.
- Apify/LinkedIn scraping is useful for account lists, social proof, job movements, and profile context, but it should remain separated from manual high-trust captures and labeled by source-confidence.
- WhatsApp sync should enter as conversation evidence, not free-form CRM truth. The system should preserve the original conversation excerpt, account/contact mapping, capture timestamp, and which claims were promoted.
- Job-change checks should run on a two-week cadence for named stakeholders and champions, with separate fields for "role changed," "left account," "joined target account," and "needs human review."
- Source-confidence handling should be explicit: raw source URL, provider, capture time, normalized field, confidence, staleness date, and whether the field is safe for outbound personalization.
- Signal systems need a routing table, not just a warehouse. Each signal should resolve to one of: Slack alert, CRM task, outbound trigger, nurture flow, retargeting audience, research queue, or no action. Closed-won and closed-lost outcomes should feed back into signal weights.

## Possible Seth Workflow

1. Start with a target account list.
2. Find likely companies, competitors, or relevant social/LinkedIn activity.
3. Waterfall enrich people and company records through a single API.
4. Store raw provider responses, normalized fields, source confidence, and costs.
5. Generate persona-specific campaign drafts.
6. Require human approval before sending or syncing to outbound tools.
7. Refresh stakeholders and trigger fields on a schedule, but treat high-impact changes as review tasks rather than automatic outreach.

## Company Research Skill Shape

1. Define the product, ICP, exclusions, and desired company count.
2. Discover candidates with a search/data provider.
3. For each company, plan the research, gather evidence, synthesize fit, and cite sources.
4. Score ICP fit and confidence.
5. Write one markdown file per company plus a final CSV.
6. Pass approved accounts into enrichment/campaign workflows.

## Open Questions

- Which enrichment providers does Deepline actually call behind the 96+ integrations?
- Can Deepline return provider-level provenance and confidence per field?
- Does it support Seth's desired storage pattern: local CSV/DB first, outbound system second?
- What would a small test look like: 10 companies, 3 personas, enrichment cost cap, no sending?
- Should Seth compare Deepline, Gooseworks, Clay MCP, Browserbase company-research, and Crustdata/LangChain-style closers on the same target-account task?
- What minimum schema should the company-research CSV use so it can plug into Clay/Deepline/outbound without rework?
- Which licensed-company source should define Acme's TAM, and what cadence keeps it current without polluting the CRM?
- Should job-change monitoring live in Supabase cron, Trigger.dev, Clay, or Attio automation?

## Sources

- [Deepline homepage](../../raw/intentional/web/2026-06-10-deepline-gtm-api-designed-for-agents.md)
- [GTM API waterfall enrichment links](../../raw/intentional/pasted/2026-06-10-gtm-api-waterfall-enrichment-links.md)
- [Codex maxxing and GTM agent opportunity bundle](../../raw/intentional/pasted/2026-06-10-codex-maxxing-and-gtm-agent-opportunity-bundle.md)
- [Shiv Sakhuja Gooseworks CLI X post](../../raw/intentional/x/2047780107339903214-shivsakhuja-launching-gooseworks-cli-a-unified-api-for-your-ai-agents-to-access-dozens-of.md)
- [Jay Sahnan company-research X post](../../raw/intentional/x/2047730585313980499-jaysahnan-i-just-open-sourced-one-of-our-internal-gtm-skills-introducing-the-company-resea.md)
- [Browserbase company-research skill](../../raw/intentional/web/2026-06-11-browserbase-company-research-skill.md)
- [Harness/company-research/video workflow bundle](../../raw/intentional/pasted/2026-06-11-harness-codex-company-research-video-workflow-and-clay-mcp-bundle.md)
- [Browserbase GTM industry page](../../raw/intentional/web/2026-06-11-browserbase-gtm-industry-page.md)
- [Acme GTM OS pasted bundle](../../raw/intentional/pasted/2026-06-11-acme-gtm-os-agentic-sales-marketing-and-design-bundle.md)
- [Sunder Sync Source Captures](../archive/2026-06-11-sunder-sync-source-captures.md)
- [Acme/eGiro first-10-day goals](../../raw/intentional/pasted/2026-06-16-acme-egiro-first-10-day-goals-and-side-projects.md)
- [Enterprise sales X profile digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-digest.md)
- [GTM workspace agentic outbound and Acme OS docs](../../raw/intentional/pasted/2026-06-16-gtm-workspace-agentic-outbound-and-acme-os-docs.md)
- [Sales plugin account-research and outreach skills](../../raw/intentional/pasted/2026-06-16-sales-plugin-account-research-and-outreach-skills.md)
- [Enterprise sales X profile backdated digest](../../staging/x-profile-digests/2026-06-16-enterprise-sales-x-profiles-backdated-digest.md)
- [Fivos Aresti posts 101-190](../../raw/sweeps/x/2026-06-16-fivosaresti-posts-101-190.md)

## See Also

- [Browser Outreach Delegation](browser-outreach-delegation.md)
- [AI GTM Opportunity Leads](../gtm-sales/ai-gtm-opportunity-leads.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [AI-Native Account Intelligence](../gtm-sales/ai-native-account-intelligence.md)
