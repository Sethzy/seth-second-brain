---
type: wiki_article
title: OpenAI Presence
updated_at: 2026-07-23
status: active
source_count: 10
tags:
  - openai
  - presence
  - enterprise-agents
  - voice
  - customer-experience
  - codex
  - fde
---

# OpenAI Presence

> Sources: OpenAI Presence announcement, OpenAI AI phone-support guide, OpenAI support-system retrospective, Frontier, Realtime API, Deployment Company, API platform, and enterprise-privacy pages, checked 2026-07-23.
> Raw: [OpenAI Presence announcement](../../raw/intentional/web/2026-07-22-openai-introducing-presence.md)

## Definition

OpenAI Presence is a managed enterprise product for building and operating trusted real-time voice and chat agents across customer and internal workflows. It combines model reasoning, system integration, policy controls, testing, observability, continuous improvement, and deployment services.

This is OpenAI moving from supplying agent intelligence to selling the operating product.

## Scope And Availability

| Dimension | Current state |
|---|---|
| Customers | Eligible enterprise customers through the OpenAI account team. |
| Availability | Limited general availability; not self-serve. |
| Delivery | Led by OpenAI Forward Deployed Engineers and select global systems integrators. |
| Channels | Real-time voice and chat. |
| Workflows | Customer support, outbound sales, billing, claims, employee IT, and other high-risk internal work. |
| Commercial details | No public pricing, minimum commitment, SLA, concurrency, or implementation timeline. |

Each deployment begins with one specific job. The agent receives only the knowledge and system access required for that job, while the company defines which actions are allowed, which require approval, and when a person must take over.

## Production Lifecycle

1. **Scope the job:** identify the high-value workflow and success criteria.
2. **Connect context and systems:** supply job-specific knowledge and least-required access.
3. **Encode behavior:** policies, SOPs, guardrails, approved actions, approvals, and escalation rules.
4. **Simulate before launch:** test common requests, edge cases, and high-risk scenarios.
5. **Grade behavior:** outcome, policy adherence, tool use, and correct escalation.
6. **Observe production:** sessions, escalations, quality signals, production health, and customer intent expose gaps.
7. **Improve with Codex:** Codex using a Presence plugin investigates signals and proposes updates.
8. **Test and approve:** teams compare proposed changes against production and approve controlled rollout.

The product's most differentiated public thesis is not only agent building; it is supervised post-launch adaptation.

## Proof

OpenAI says Presence powers its English-language phone-support line at 1-888-GPT-0090. It reportedly:

- handles open-ended requests;
- verifies callers and uses account context;
- takes approved actions;
- resolves 75% of inbound issues without human assistance; and
- reduced human handoffs by 15 percentage points in ten days through the Codex improvement loop.

These are first-party metrics without a published denominator, issue mix, methodology, cost, or independent audit.

The Help Center narrows the claim: the phone agent handles routine product, account-support, and troubleshooting questions, but cannot perform several sensitive operations, guarantee follow-up, or connect directly to a live person. "Take action" and "escalate" are workflow-specific capabilities, not universal promises.

External launch references are earlier:

- **BBVA Mexico:** design partner exploring banking voice support.
- **SoftBank:** testing Japanese-language customer conversations.
- **IAG:** exploring insurance support during severe weather and claims events.

OpenAI describes these as exploring or testing, not as quantified production deployments.

## Strategic Meaning

### OpenAI now sells the resolved workflow

The success metrics are resolution, approved actions, policy compliance, handoff reduction, and continuous quality—not tokens or model calls.

### Presence spans the CX production stack

It brings together voice/chat interaction, reasoning, tools, enterprise systems, permissions, policies, evals, simulation, observability, controlled change, and deployment labor.

### The Codex loop targets maintenance cost

Specialized agent vendors often differentiate on production analytics and tuning. Presence puts Codex into that maintenance loop: investigate failures, propose changes, regression-test them, and retain human approval.

### Narrow jobs enable expansion

Policies, evaluations, and escalation rules can be reused across workflows and channels. One successful billing, claims, support, or IT workflow can become the entry point for adjacent deployments.

### Services capacity is both moat and bottleneck

FDE-led delivery can unlock mission-critical use cases that fail as self-serve software. Limited GA and bespoke deployment also constrain near-term scale and create a services-heavy motion.

## Relationship To Other OpenAI Products

| Product | Relationship to Presence |
|---|---|
| GPT-Live | Consumer full-duplex interaction breakthrough; not the enterprise deployment platform. |
| Realtime API | Developer primitive for custom production voice systems. |
| ChatGPT Work | Individual knowledge-work execution, not a real-time service agent. |
| Workspace Agents | Governed repeatable team workflows inside ChatGPT/Slack/schedules/API triggers. |
| Frontier | Complementary enterprise context, identity, permissions, execution, and evaluation layer; an explicit dependency is not publicly confirmed. |
| Deployment Company / partners | Delivery capacity for workflow redesign, integration, and rollout. |

## Open Questions

- What models and telephony/orchestration stack underlie Presence?
- Which CRM, ticketing, contact-center, identity, payment, and human-handoff integrations are supported?
- What are the hosting, residency, retention, audit, and certification terms specific to Presence?
- Which languages and regions are supported at production quality?
- How are pricing and outcomes structured?
- Can customers export agents, policies, evals, traces, and improvement history?
- How much work can internal teams own after launch?

## Interview Talk Track

> Presence is OpenAI's move from model supplier to managed enterprise-agent operator. It starts with a narrowly scoped job, connects only the necessary knowledge and systems, encodes approvals and escalation, tests the agent through simulations and graders, and then uses production signals plus Codex to propose controlled improvements. That puts OpenAI directly into Sierra and Wonderful's category, while the limited-GA, FDE-led model shows that deployment expertise is part of the product.

Best question to ask:

> How will OpenAI decide what belongs in self-serve Workspace Agents, what belongs in Presence, and what requires a broader Frontier/FDE transformation—and how will customers retain operational ownership as those layers converge?

## See Also

- [Enterprise Agent Competitive Landscape](enterprise-agent-competitive-landscape.md)
- [GPT-Live And Full-Duplex Voice](gpt-live-full-duplex-voice.md)
- [OpenAI Enterprise Product Framing](openai-enterprise-product-framing.md)
- [OpenAI Release Radar](release-radar.md)

