---
type: raw_capture
source_type: x
title: "Sunder sync: flint-custom-pages-per-prospect-validation.md"
url: "https://x.com/michlimlim/status/2034306846283182552"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/services/flint-custom-pages-per-prospect-validation.md"
source_root: "/Users/sethlim/Documents/sunder-next-migration-20260225"
source_relpath: "roadmap docs/Sunder - Source of Truth/services/flint-custom-pages-per-prospect-validation.md"
sha256: "1832d311c95ee665b54c9a2f0842d287221514f16bd13c9571a954d137bb7788"
duplicate_of: ""
---

# Sunder sync: flint-custom-pages-per-prospect-validation.md

Source file: `/Users/sethlim/Documents/sunder-next-migration-20260225/roadmap docs/Sunder - Source of Truth/services/flint-custom-pages-per-prospect-validation.md`

Primary URL: https://x.com/michlimlim/status/2034306846283182552

Duplicate of existing source-map entry: `none`

## Capture Text

# Flint: Custom Pages Per Prospect — Market Validation for Artifact Publishing

**Source:** https://x.com/michlimlim/status/2034306846283182552
**Product:** Flint (tryflint.com) — autonomous landing page builder for growth teams
**Date captured:** 2026-03-19

## Key Quote

> And it's not just Claude. Our beta users have connected Flint to their Clay, OpenClaw, Relay, and Zapier. Live use cases:
>
> - Flint makes an account-based page for every enriched prospect in a Clay table
> - Claude pulls top Google Ads keywords weekly, Flint generates landing pages for each one
> - A company created Clawdbots to respond to social posts with a custom landing page for every relevant comment

## Why This Matters for Sunder

This validates the **Artifact Publishing (Mini Lovable)** service already specced in `01-Built-In Services`. The core pattern — "generate a unique, personalized page per prospect/property/context" — is seeing real traction in adjacent markets.

### The Pattern

| Flint (growth teams) | Sunder (RE agents) |
|---|---|
| Clay enrichment → custom landing page per prospect | CRM contact data + memory → personalized pitch page per prospect |
| Google Ads keywords → landing page per keyword | Property listings → showcase page per listing |
| Social comment → custom page per commenter | Inbound lead → personalized "why work with me" page |

### What Sunder Does Better

1. **Richer context** — Sunder has compounding memory (SOUL.md, USER.md, MEMORY.md) plus full CRM data feeding each page. Flint relies on whatever Clay/Zapier passes in.
2. **Domain-specific tool chaining** — Property showcase pages chain browser scraping, map embeds, image generation, and CRM data. Not just text-in → page-out.
3. **Agent-native** — The page generation is one capability within a full agent that also handles follow-ups, CRM updates, and briefings. Flint is a standalone page builder.

### Integration Ecosystem Parallel

Flint's integration story (Clay, Zapier, OpenClaw, Relay) maps to Sunder's Composio-powered connections. The same "trigger from external tool → agent generates deliverable" pattern applies:

- Composio webhook (new lead) → Sunder generates pitch page
- Autopilot trigger (listing status change) → Sunder generates updated showcase page
- User request in chat → Sunder generates any artifact on demand

## See Also

- [01-Built-In Services — Artifact Publishing (Mini Lovable)](./01-Built-In%20Services%20(Imported%20from%20RE-AI-CRM).md) — full architecture and use cases
- [flint-apis-mcps-not-coding-agents.md](../references/sandboxes/flint-apis-mcps-not-coding-agents.md) — Flint's API/MCP integration strategy
