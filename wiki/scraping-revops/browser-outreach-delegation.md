---
type: wiki_article
title: Browser Outreach Delegation
updated_at: 2026-06-10
status: draft
source_count: 2
tags:
  - browser-agents
  - outreach
  - gtm
  - audit-trails
  - delegation
---

# Browser Outreach Delegation

> Sources: Seth pasted Manus outreach note, 2026-06-10; Anthropic Claude blog, 2026-05-13
> Raw: [agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md); [Claude browser-use best practices](../../raw/intentional/web/2026-06-10-claude-best-practices-for-computer-and-browser-use-with-clau.md)

## Overview

Browser outreach delegation treats an agent as a constrained ops teammate for repetitive distribution work. Seth's Manus note is the clearest example: humans set the target list, positioning, and tone, while Manus operated LinkedIn and Twitter/X slowly, followed target lists, attempted DMs or connection requests where available, and returned an audit trail with successes and dead ends.

This belongs partly in GTM and partly in scraping/revops. The work is not just internal tooling. It is distribution: finding accounts, identifying relevant people, pacing actions, respecting platform limits, and recording what happened.

## Key Ideas

- The durable pattern is constrained delegation, not spam automation.
- Humans should own target selection, offer, positioning, and tone; the browser agent should own repetitive research and execution inside clear bounds.
- A good run records dead ends as first-class output: no active handle, DMs restricted, no good contact, poor fit, or insufficient confidence.
- For partnership or sponsor outreach, the contact-finding heuristic should bias toward people likely to care: developer relations, growth, product marketing, partnerships, founders, GTM leads, and relevant operators.
- Browser-use reliability depends on the harness: screenshots need usable resolution, coordinates must match the displayed UI, ambiguous states should be checked, and the agent needs an audit trail rather than only a final claim.

## Operating Loop

1. Define the target list, offer, tone, exclusion criteria, and per-company action cap.
2. Ask the browser agent to research company accounts and affiliated people.
3. Rank contacts by likely relevance to the offer.
4. Execute only allowed actions, slowly and with platform-aware pacing.
5. Log every outcome, including dead ends and reasons for skipping.
6. Review the audit trail before the next batch changes targeting or copy.

## My Take

This is a practical bridge between AI GTM research and actual distribution. The most reusable artifact is not the sent DM; it is the structured run report: company, candidate contacts, action attempted, result, blocker, and next recommendation.

## Open Questions

- What is Seth's default outreach run schema for company, contact, platform, action, result, blocker, and next step?
- Which outreach workflows are acceptable for browser delegation, and which should remain manual?
- Should this page connect to a future "AI event sponsor/partner outreach" playbook?

## Sources

- [Agent workflow links batch](../../raw/intentional/pasted/2026-06-10-agent-workflow-links-goals-classifier-manus-outreach-scratch.md)
- [Claude browser-use best practices](../../raw/intentional/web/2026-06-10-claude-best-practices-for-computer-and-browser-use-with-clau.md)

## See Also

- [AI GTM Opportunity Leads](../gtm-sales/ai-gtm-opportunity-leads.md)
- [Warm Intro Pathfinding With AI](../gtm-sales/warm-intro-pathfinding-with-ai.md)
- [GTM Waterfall Enrichment APIs](gtm-waterfall-enrichment-apis.md)
