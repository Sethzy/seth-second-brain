---
type: raw_capture
source_type: x
title: "Sunder sync: Context Graphs Platform.md"
url: "https://x.com/prukalpa/status/2011117250762207347"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Ideas/Context Graphs Platform.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "02_Areas/Product/Ideas/Context Graphs Platform.md"
sha256: "11e5e9bc97dd7e4a40af73a521e4aa7b901ad639d68ccb96cb2742c0cfd9a8ab"
duplicate_of: ""
---

# Sunder sync: Context Graphs Platform.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/02_Areas/Product/Ideas/Context Graphs Platform.md`

Primary URL: https://x.com/prukalpa/status/2011117250762207347

Duplicate of existing source-map entry: `none`

## Capture Text

---
created: 2026-01-15
tags: [product-idea]
type: feature
priority: none
linear_url:
---

# Context Graphs Platform

## Problem
AI agents need more than data - they need decision traces (the "why" behind past decisions). Current systems of record capture what happened, not why. The reasoning connecting data to action was never treated as data.

## Solution
Build a context graph platform that captures decision traces and makes context executable by agents.

## The Debate

### Three Perspectives
1. **Jamin Ball:** AI won't kill systems of record; truth lives in SoRs with semantic layer on top
2. **Jaya Gupta/Ashu Garg:** Next trillion-dollar opportunity is "context graphs" - decision traces, the "why" behind past decisions. Vertical agents will own context for their domain
3. **Prukalpa (Atlan):** Vertical agents can't win because context is global, not local. The integrator/platform wins.

### Seth's Synthesis - The Missing Layer
Both Prukalpa and Jaya are right but miss a packaging problem:
- Context flows in from multiple systems (Prukalpa's heterogeneity)
- Context is created during execution (Jaya's decision traces)

**The gap:** How does context become *executable* by agents?

Raw context graphs capture the "what." Missing layer is the "how" - structured protocols agents can actually execute.

> "Skills capture how to decide. Decision traces capture what was decided and why. You need both. That's the difference between an agent that executes and an agent that learns."

### Jet's Take
Same conclusion but industry-wide, not single enterprise. Prukalpa's thesis = "Palantir wins."

## Key Concepts

### What Systems of Record Don't Capture
- **Exception logic in people's heads:** "We always give healthcare companies an extra 10% because their procurement cycles are brutal"
- **Precedent from past decisions:** "We structured a similar deal for Company X last quarter"
- **Cross-system synthesis:** Support lead checks ARR in Salesforce, escalations in Zendesk, Slack thread flagging churn risk
- **Approval chains in Slack/Zoom:** Discount approved in DM, but opportunity record only shows final price

### Two Types of Context
1. **Operational context** - SOPs, institutional knowledge, trade secrets
2. **Analytical context** - metric definitions, calculations (evolved semantic layers)

### The Context Graph
A living record of decision traces stitched across entities and time so precedent becomes searchable. Not "the model's chain-of-thought" but:
- What inputs were gathered from which systems
- What policies applied
- What exceptions were granted
- Who approved
- Why

### Why Incumbents Can't Build This
- **Salesforce/ServiceNow/Workday:** Built on current state storage. Can't replay state at decision time.
- **Snowflake/Databricks:** In read path, not write path. Receive data via ETL after decisions are made.
- **Systems of agents startups:** Structural advantage - they're in the orchestration path at commit time.

## What Winners Need
1. Cross-system connectivity (100s of integrations)
2. Operational context synthesis (from logs, tickets, chats)
3. Analytical context management (metric definitions, entities)
4. Context delivery at inference time
5. Feedback loops at scale
6. Governance and trust

## Three Startup Paths
1. **Replace SoRs:** AI-native CRM/ERP with event-sourced state and policy capture (e.g., Regie.ai)
2. **Replace modules:** Target specific sub-workflows where exceptions concentrate (e.g., Maximor for finance)
3. **Create new SoRs:** Start as orchestration, persist decision traces, become authoritative artifact (e.g., PlayerZero)

## Key Signals for Where to Build
- High headcount doing workflow manually (50+ people routing tickets, triaging requests)
- Exception-heavy decisions where precedent matters
- Organizations at intersection of systems (RevOps, DevOps, Security Ops)

## Implications for Sunder
- Document processing agents should capture decision traces
- Integration breadth matters more than vertical depth
- Customer-owned context = competitive moat
- Every improvement to knowledge packaging compounds across all agents

**Key quote:** "The system that wins isn't the one that captures the most context on day one. It's the one that gets better at capturing and delivering context over time."

## Notes
This is a platform problem, not an application problem. In a world of heterogeneity, the integrator always wins.

## Sources
- Prukalpa (Atlan): https://x.com/prukalpa/status/2011117250762207347
- Jaya Gupta: https://x.com/JayaGup10/status/2003525933534179480
- Original article: "AI's trillion-dollar opportunity: Context graphs" by Jaya Gupta and Ashu Garg (12.22.2025)

## Updates
