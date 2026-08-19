---
type: wiki_article
title: GTM Prospecting Tool Index
updated_at: 2026-07-06
status: active
source_count: 3
tags:
  - gtm
  - prospecting
  - sales-tools
  - enrichment
  - tool-index
---

# GTM Prospecting Tool Index

> Sources: ProspectingStack / The Signal, captured 2026-06-24; Origami homepage, captured 2026-06-26; Deepline homepage, captured 2026-06-10
> Raw: [ProspectingStack GTM tool index embedded catalog](../../raw/intentional/web/2026-06-24-prospectingstack-gtm-tool-index-embedded-catalog.md); [Origami website homepage](../../raw/intentional/web/2026-06-26-origami-website-homepage.md); [Deepline homepage](../../raw/intentional/web/2026-06-10-deepline-gtm-api-designed-for-agents.md)

## Overview

ProspectingStack is now the main wiki reference for GTM prospecting tools: a selective market map of prospecting vendors plus an embedded adoption dataset for GTM stacks at fast-growing private B2B companies. Use this page when Seth asks for tools by job-to-be-done, wants alternatives to a known vendor, or needs to sanity-check which GTM tools appear in modern B2B stacks.

The captured site bundle contains 20 market-map categories, 81 deduped market-map/comparison vendors, 60 tracked tools in the top-tech-stack dataset, and 63 company stack rows. ProspectingStack says the top-stack analysis sources data from Sumble and Clay, plus Claude-assisted customer-logo extraction from websites and review sites.

Important caveat: treat this as a directional market/reference index, not as verified buying advice. The raw capture preserves the extracted JSON; individual vendor claims, pricing, and current capabilities should be refreshed from vendor sources before purchase or implementation decisions.

Origami is now a direct-captured product lead adjacent to this index. Its positioning is "find your perfect customers in one prompt": prompt an ICP, search live sources, generate a verified lead table, enrich contact data through waterfalls, and optionally run multi-channel outreach through Send. Treat it as a productized alternative to the hand-rolled Claude Code + Prospeo/Smartlead/Zapmail outbound stack.

Deepline is also a direct-captured agent-native GTM infrastructure lead. Its homepage positions it as a GTM API for agents that connects Claude Code, Codex, Hermes, and custom apps to 96+ GTM integrations, with workflows in code, results saved in the user's own database, and provider access managed through one Deepline account.

## Retrieval Shortcuts

- Looking for contact/enrichment tools: start with Data, Signal-Based Selling, Intent Data, Job Changers, and Website Visitor De-Anonymization.
- Looking for outbound execution tools: start with Sales Engagement, Dialer, Email Warming, LinkedIn Tools, Calendaring, and Lead Routing.
- Looking for agentic/AI-native GTM tools: start with AI SDR, AI Email Writing, Research Agents, AI-Native CRM, All-In-One AI Sales Platforms, and Data Orchestration.
- Looking for prompt-to-lead-list products: check Origami before stitching together a manual stack from Clay/Prospeo/Smartlead-style components.
- Looking for agent-native GTM APIs or waterfall enrichment layers: check Deepline and the [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md) page.
- Looking for incumbent stack norms: use the Top Tech Stack Adoption table; Salesforce, HubSpot, dbt, Gong, Clay, Snowflake, ZoomInfo, Outreach, Apollo, and Sales Navigator are the highest-adoption tools in the captured dataset.

## Direct Capture Notes

| Vendor | Source | Notes |
|---|---|---|
| Deepline | [homepage](../../raw/intentional/web/2026-06-10-deepline-gtm-api-designed-for-agents.md) | Agent-native GTM API for Claude Code, Codex, Hermes, and custom apps. Captured homepage claims 96+ GTM integrations, workflows in code, results saved in the user's own database, and provider access through one Deepline account. The example prompt covers competitor research, LinkedIn engager scraping, waterfall email enrichment, and persona-specific outbound campaign creation. |
| Origami | [homepage](../../raw/intentional/web/2026-06-26-origami-website-homepage.md) | Prompt-driven prospecting for hard-to-reach buyers. Homepage claims 50+ live sources, including Google Maps, LinkedIn, job boards, company sites, and the open web; 100M+ companies and 350M+ profiles; email waterfall across Findymail, LeadMagic, Wiza, People Data Labs, and Prospeo; phone waterfall across Bytemine, People Data Labs, LeadMagic, Wiza, Findymail, Forager, Prospeo, ContactOut, and Zeliq; and Send multi-channel outreach on paid plans. Pricing on capture date: free one-time 1,000 credits; Starter $29/month; Enterprise custom. |

## Reference Pages

The captured ProspectingStack dataset is split into focused reference pages so this hub stays usable for retrieval and synthesis:

- [GTM Prospecting Category Market Map](gtm-prospecting-category-market-map.md) - category taxonomy and market-map vendor groups.
- [GTM Prospecting Stack Adoption](gtm-prospecting-stack-adoption.md) - top-stack adoption counts by tool.
- [GTM Prospecting Vendor Directory](gtm-prospecting-vendor-directory.md) - vendor-by-category directory.
- [GTM Prospecting Company Stack Lookup](gtm-prospecting-company-stack-lookup.md) - company stack rows from the captured dataset.

## Implications For Seth

- Treat Clay as the orchestration center of gravity: it appears in many ProspectingStack categories and is high-adoption in the top-stack dataset.
- Treat Salesforce and HubSpot as unavoidable integration surfaces for serious B2B GTM work, even when the workflow layer is AI-native.
- Separate signal ingestion from outbound execution. Signal tools include Clay, Common Room, Sumble, UserGems, Warmly, 6sense, Demandbase, and ZoomInfo; execution tools include Outreach, Salesloft, Apollo, Instantly, Smartlead, Lemlist, Nooks, and Orum.
- When building an agentic GTM workflow, favor tools with APIs, orchestration hooks, clear provenance, or database-like outputs before tools that only offer an opaque UI.
- Keep Deepline on the short list for code-first GTM systems: it is closer to an API/integration layer than a UI-first prospecting database, so compare it against Gooseworks, Clay MCP, Browserbase company-research, and hand-rolled Claude Code workflows on the same target-account task.
- Use the company-stack table as a benchmark list for what mature B2B stacks often contain: CRM, data warehouse/reverse ETL, enrichment, conversation intelligence, sequencer, and automation.

## See Also

- [GTM Prospecting Category Market Map](gtm-prospecting-category-market-map.md)
- [GTM Prospecting Stack Adoption](gtm-prospecting-stack-adoption.md)
- [GTM Prospecting Vendor Directory](gtm-prospecting-vendor-directory.md)
- [GTM Prospecting Company Stack Lookup](gtm-prospecting-company-stack-lookup.md)
- [Agentic GTM Campaign Workflows](agentic-gtm-campaign-workflows.md)
- [AI-Native Account Intelligence](ai-native-account-intelligence.md)
- [GTM Waterfall Enrichment APIs](../scraping-revops/gtm-waterfall-enrichment-apis.md)
