---
type: wiki_article
title: Enterprise Agent Competitive Landscape
updated_at: 2026-07-23
status: active
source_count: 18
tags:
  - openai
  - presence
  - sierra
  - wonderful
  - enterprise-agents
  - customer-experience
---

# Enterprise Agent Competitive Landscape

> Sources: OpenAI Presence; Sierra product, Agent Studio/SDK, Channels, Horizon, SoftBank, trust, customer, and pricing pages; Wonderful platform, Agent Studio, deployment, open-architecture, Singapore, and customer-story pages, checked 2026-07-23.
> Raw: [OpenAI Presence](../../raw/intentional/web/2026-07-22-openai-introducing-presence.md); [Sierra SoftBank partnership](../../raw/intentional/web/2026-07-14-sierra-softbank-partnership.md); [Sierra Horizon](../../raw/intentional/web/2026-07-16-sierra-horizon.md); [Wonderful Singapore](../../raw/intentional/web/2026-05-04-wonderful-singapore.md); [Wonderful open architecture](../../raw/intentional/web/2026-06-10-wonderful-open-architecture.md); [Wonderful ELTA case study](../../raw/intentional/web/2026-07-14-wonderful-elta-customer-story.md)

## Bottom Line

OpenAI Presence now competes directly with Sierra and Wonderful for enterprise voice/chat agents that connect to systems, take actions, enforce policies, use simulations/evals, escalate to people, and improve after launch.

The competition is not simply model versus model. It is **production agent platform + deployment organization + evidence + commercial model**.

## Direct Comparison

| Dimension | OpenAI Presence | Sierra | Wonderful |
|---|---|---|---|
| Core scope | Managed real-time voice/chat agents for customer and high-risk internal workflows. | Mature customer-agent operating system across service, revenue, and long-horizon engagement. | Broad enterprise agent platform across customer, employee, and back-office work. |
| Channels | Voice and chat at launch. | Voice, chat, SMS, WhatsApp, Apple Business Chat, email, ChatGPT, and Live Assist. | Voice, chat, email, documents, WhatsApp, embedded interfaces, apps, and computer use. |
| Build surface | FDE/SI-led; not self-serve. | Agent Studio plus code-first Agent SDK and embedded Agent Strategists. | Plain-language Studio plus CLI/code control and local deployment teams. |
| Improvement loop | Production signals → Codex investigation → proposed changes → eval comparison → human-approved rollout. | Monitoring/Insights/Explorer → Ghostwriter fixes → simulations/regression → controlled experiments. | Agent Builder converts failures into evals and iterates prompts, code, tools, and interfaces with human review. |
| Model strategy | OpenAI frontier models/research integration. | Model constellation spanning frontier, open-weight, proprietary, and specialist models. | Model-agnostic; publicly uses Gemini/Vertex AI among other infrastructure. |
| Deployment | Limited GA via OpenAI FDEs and select global SIs. | Enterprise partnership with Agent Strategists; customer Studio/SDK ownership. | Multi-tenant, single-tenant, customer cloud, and claimed air-gapped options; transfer-to-client emphasis. |
| Public proof | Strong quantified OpenAI support deployment; external partners are exploring/testing. | Broad named enterprise production evidence and mature customer-agent footprint. | Multiple multilingual production stories across Europe/LATAM and a fast local-market expansion model. |
| Commercial posture | Pricing undisclosed. | Outcome-based or negotiated hybrid pricing; no public card. | High-touch enterprise pricing; public marketplace references should not be treated as universal list price. |
| Distinctive wedge | Vertical integration with OpenAI Research, models, Codex, Frontier, and FDEs. | Dedicated CX maturity, channels, memory, long-horizon Horizon agents, compliance, and outcome economics. | Hyperlocal language/culture, deployment flexibility, open/exportable architecture, and local FDE teams. |

## The SoftBank Collision

SoftBank is the clearest evidence that the overlap is account-level rather than theoretical:

- Sierra announced SoftBank Corp as its exclusive Japan sales partner on July 14 and reported production results for the LINEMO brand.
- OpenAI named SoftBank as a Presence design partner/testing customer on July 22.

Sierra reported 97% inquiry resolution and 93% customer satisfaction for LINEMO. These are vendor/customer-reported metrics, not standardized benchmarks. The significance is that both companies are pursuing the same enterprise, language, customer-experience, and deployment territory within days of each other.

## Sierra

Sierra is the more mature dedicated CX platform. Its Agent OS answers questions, accesses systems, takes actions, hands work to people, and preserves goals/guardrails. Agent Studio and the Agent SDK support no-code and code-first building; Ghostwriter builds or repairs workflows, integrations, guardrails, tone, and tests from SOPs, transcripts, and simulation failures.

Recent expansion matters:

- **Horizon** (July 16) extends agents across days or months, reacting to signals, preserving memory, coordinating inbound/outbound contact, and planning next actions.
- Sierra advertises voice and digital channels well beyond Presence's launch scope.
- Its public compliance posture includes SOC 2, HIPAA, GDPR, PCI, FedRAMP High, ISO 27001, and ISO 42001.
- It prices many deployments by agreed outcomes such as resolution, retention, purchase, or cross-sell.

Sierra's immediate advantage is application-layer maturity and proof. Its risk is that outcome pricing and high-touch deployment are operationally complex, while voice-agent reliability remains an industry-wide constraint.

## Wonderful

Wonderful's original wedge is production AI agents for non-English and culturally specific markets. It localizes dialect, accent, cadence, register, tone, cultural norms, and regulatory behavior through local deployment teams.

Its Singapore positioning is directly relevant to Seth:

- English, Mandarin, Malay, Tamil, and Singlish create a high bar for generic voice systems.
- The company is hiring local Deployment Strategists, Forward Deployed Engineers, and GTM operators.
- It targets customer care, collections, back-office operations, and sales.

Wonderful also differentiates on enterprise control:

- agents, skills, tools, governance configuration, and apps are claimed to be exportable;
- the platform supports headless use and bidirectional external-agent interoperability;
- it markets multi-tenant, single-tenant, customer-cloud, and air-gapped deployment choices;
- it is model-agnostic and claims portability across major cloud providers.

The ELTA case study illustrates the localization thesis: Wonderful reports a Greek-language tracking agent live in five weeks, 86% production resolution, four times daily call capacity, and peak waits falling from ten minutes to zero. Treat these as vendor/customer-reported figures.

## Competitive Interpretation

### Presence's advantage

Vertical integration may let OpenAI combine frontier-model progress, voice research, Codex maintenance, Frontier context/governance, and FDE delivery faster than an independent application vendor.

### Sierra's advantage

Sierra already exposes a broad customer-agent operating system: more channels, detailed compliance, persistent data/memory, long-horizon work, Studio/SDK ownership, outcome pricing, and a deep case-study base.

### Wonderful's advantage

Wonderful has the clearest documented localization and deployment-flexibility story. It can attack language quality, sovereignty, on-prem requirements, model lock-in, and capability-transfer concerns.

### The likely battleground

Deals will turn on:

- production task success rather than conversational demos;
- language and noise performance;
- integration depth and time to launch;
- policy, approval, escalation, and audit fidelity;
- post-launch improvement cost;
- customer ownership and portability;
- outcome economics;
- credible local delivery capacity.

## Diligence Questions

1. What percentage of eligible interactions resolve end to end, and what is the eligibility filter?
2. Which actions are deterministic, approval-gated, reversible, and auditable?
3. How does the platform regress-test changes across languages, channels, and customer segments?
4. What happens during model/provider failure?
5. Which data, prompts, policies, evals, tools, and traces can the customer export?
6. What is the full services burden through launch and steady state?
7. How are human handoffs measured, routed, and priced?
8. Which metrics are independently audited versus vendor-defined?

## Interview Talk Track

> Presence makes OpenAI a direct competitor to Sierra and Wonderful because all three now sell production agents that act in company systems under policies, evals, and human escalation. Sierra has the stronger dedicated-CX product maturity and public production base. Wonderful has the sharper localization, open architecture, and deployment-flexibility story. OpenAI's differentiated bet is vertical integration: frontier models, Research, Codex-driven improvement, Frontier, and FDEs in one stack. I would not claim a winner without the customer's language, channels, systems, risk, ownership, and pricing requirements.

## See Also

- [OpenAI Presence](openai-presence.md)
- [GPT-Live And Full-Duplex Voice](gpt-live-full-duplex-voice.md)
- [OpenAI Enterprise Product Framing](openai-enterprise-product-framing.md)
- [Voice Agent Stack Landscape](../voice-agents/voice-agent-stack-landscape.md)

