---
type: raw_capture
source_type: x
url: https://x.com/prukalpa/status/2011117250762207347
original_url: https://x.com/prukalpa/status/2011117250762207347
author: "Prukalpa \u2728"
handle: prukalpa
status_id: 2011117250762207347
captured_at: 2026-06-19T19:58:17+08:00
published_at: "Tue Jan 13 16:44:51 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 41
  reposts: 77
  likes: 610
---

# X post by @prukalpa

## Source

- Original: [https://x.com/prukalpa/status/2011117250762207347](https://x.com/prukalpa/status/2011117250762207347)
- Canonical: [https://x.com/prukalpa/status/2011117250762207347](https://x.com/prukalpa/status/2011117250762207347)
- Author: Prukalpa ✨ (@prukalpa)

## Verbatim Text

Context Graphs Are a Trillion-Dollar Opportunity. But Who Actually Captures It?

Jaya Gupta's thesis is right about context graphs, and wrong about who wins. In a world of heterogeneity, the integrator always wins, not the application.

If you’re in the data world, you probably saw systems of record and context graphs go viral in recent weeks.

Jamin Ball’s (@jaminball) [“Long Live Systems of Record”](https://cloudedjudgement.substack.com/p/clouded-judgement-121225-long-live) argued that, despite the discourse, AI agents won’t kill systems of record like data warehouses, CRMs, ERPs, HRISes, etc. Instead, “truth” will live in systems of record with a semantic layer on top that tells agents how to use that truth.

Jaya Gupta ([@JayaGup10](https://x.com/JayaGup10)) and Ashu Garg (@ashugarg) responded in the now-viral [“AI’s trillion-dollar opportunity: Context graphs”](https://foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/), arguing that adding AI to systems of record with some semantic layer isn’t enough. Instead the next trillion-dollar opportunity is in what this misses: decision traces, or the “why” behind past decisions. All of these will form a context graph, which they called the next trillion-dollar opportunity.

Who gets to own this? Jaya and Ashu think it’s not the systems of records but instead the agents that work in the “execution path” and can see the full context when a decision is made. In other words, vertical agent startups will own the context graph for their domain. The sales agent company will capture context around renewals, the support agent company will capture context around escalations, and so on.

This prompted a lot of debate and discussion: [how to](https://www.graphlit.com/blog/building-the-event-clock) [actually](https://x.com/akoratana/status/2005303231660867619) [build](https://trustgraph.ai/news/context-graph-manifesto/) a context graph, the [two-layer context architecture](https://www.linkedin.com/posts/anthony-alcaraz-b80763155_foundation-capital-just-published-context-activity-7410253380641734656-RuYD), the importance of [operational context](https://www.graphlit.com/blog/context-layer-ai-agents-need) and [execution intelligence](https://x.com/edsim/status/2004935604706914745), and what this means for [agent reliability](https://www.reddit.com/r/AI_Agents/comments/1q25fqr/why_enterprise_ai_agents_fail_in_production/), [governance](https://subramanya.ai/2025/12/26/context-graphs-my-thoughts-on-the-trillion-dollar-evolution-of-agentic-memory/), [observability](https://www.linkedin.com/posts/jain-arvind_theres-been-a-lot-of-excitement-about-context-activity-7414733088691458048-g3L-), [AppSec](https://www.pixee.ai/blog/appsec-systems-of-decision-context-graphs), [financial recovery](https://www.linkedin.com/pulse/decoding-decision-my-exploration-incorporating-context-seshadri-ntc4c), and more.

No wonder this article went viral, it's an elegant thesis. And I think they're right about the importance and opportunity of context graphs. But they're wrong about who gets to capture that trillion dollars.

That’s because this idea of the context graph runs headfirst into a messy reality in enterprises: heterogeneity.

I've been wrestling with the context problem for the past 18–24 months — in conversations with customers, in our product strategy at Atlan, and in essays I've written about the [enterprise context layer](https://atlan.com/know/closing-the-context-gap/) and the [AI context gap](https://atlan.com/know/ai-value-chasm/). This post is my attempt to pull those threads together, connect them with the "systems of intelligence" stack, and share where I think the world is really going.

## The end of one heterogeneity, and the start of another

For the last decade, "heterogeneity" in data meant a mess of point tools orbiting a few closed warehouses, followed by a wave of consolidation as platforms tried to pull everything into their gravity well. Iceberg and open table formats are ending that era, with storage becoming open, compute becoming fungible, and lock-in moving downhill.

But fragmentation isn't going away. Heterogeneity is just moving up the stack.

Instead of five warehouses, we’re moving toward hundreds of agents, copilots, and AI applications. Each with its own partial view of the world, its own embedded definitions, its own "private" context window. Instead of arguing about where data lives, we'll be arguing about whose semantics are right, whose AI we can trust, and how to keep dozens of autonomous systems aligned with a single version of reality.

Unfortunately, this isn’t a guess for the future. We're already seeing this happen.

One customer told us: "We have 1,000+ Databricks Genie rooms and no way to govern them all. It's like BI sprawl all over again."

Another said: "We have all kinds of agentic tools (Sierra, Writer, Google Agentspace, Snowflake Cortex) and none of them talk to each other. I want a common layer of context so I don't need to context-engineer every single one of them."

## Why vertical agents can't solve this

Execution paths are local, context is global

Let's go back to Jaya and Ashu’s core argument for agents owning the context graph: "Systems of agents startups have a structural advantage. They sit in the execution path."

This is true for capturing decision traces within a single workflow. But for most decisions, context comes from everywhere.

When a renewal agent proposes a 20% discount, it doesn't just pull from the CRM. It pulls from:

- PagerDuty for incident history

- Zendesk for escalation threads

- Slack for the VP approval from last quarter

- Salesforce for the deal record

- Snowflake for usage data

- The semantic layer for the definition of "healthy customer"

And here's the kicker: every enterprise has a different combination of these systems. One customer runs Salesforce + Zendesk + Snowflake. Another runs HubSpot + Intercom + Databricks. A third runs a homegrown CRM + ServiceNow + BigQuery.

I think this is the heterogeneity problem that Jaya and Ashu’s thesis doesn't address. The vertical agent startup sees the execution path and captures context within their workflow. But enterprises have dozens of agents, across dozens of vendors, each building their own context silo. The vertical agent can’t see this full context web.

To truly capture the context graph, a vertical agent would need to integrate with 50-100+ systems just to cover the common cases. Now multiply that across every vertical agent company — the sales agent, the support agent, the finance agent, the HR agent — each building the same integrations.

The two halves of context

System heterogeneity is just the start of the problem. Though we think of “context” as a single concept, context itself is heterogeneous.

[Tomasz Tunguz ](https://tomtunguz.com/operational-analytical-context-databases/)gave a great explanation of the two emerging types of context databases:

- Operational context databases store standard operating procedures and institutional knowledge: when a customer calls about resetting a password, when legal reviews an NDA, when HR answers questions about options vesting. These processes represent trade secrets and intellectual property.

- Analytical context databases are the evolution of semantic layers: definitions and calculations for metrics like revenue or customer acquisition cost. Semantic layers told AI what data meant, while analytical context databases teach AI how to reason about it.

These two forms of context are deeply intertwined and yet distinct, both in what they look like and where they live, a fact that the context graph discourse has yet to account for.

A renewal decision doesn't just pull from operational context ("here's our exception policy for discounts"). It also pulls from analytical context ("here's how we calculate customer health score, here's what 'at-risk' means"). And that analytical context is defined in your semantic layer, which sits on top of your data warehouse, which contains data from your CRM, support system, product analytics, and billing platform.

The vertical agent sees the workflow, not the analytical context that feeds it. The data warehouse sees the metrics, not the operational decisions that use them. The context graph needs to bridge both of these perspectives.

## From execution paths to compounding systems

In practice, context turns out to be cross-system and multi-layered. And that changes the question. It’s no longer just who captures a decision trace at the moment it’s made, but what kind of system can capture, refine, and deliver context across dozens of agents over time.

In a world with hundreds of agents operating simultaneously, the hard problem isn’t initial context capture. It’s coordination and improvement. How does context get better? How does it stay consistent? How do we ensure that what one agent learns can benefit another?

That’s where two ideas become foundational: feedback loops and context platforms.

Context compounds through feedback loops

[Tomasz](https://tomtunguz.com/operational-analytical-context-databases/) made another point that’s relevant here: "The key to both operational & analytical context databases isn't the databases themselves. It's the feedback loops within them."

The system that wins isn't the one that captures the most context on day one. It's the one that gets better at capturing and delivering context over time.

This creates a flywheel:

- Accuracy creates trust: When the context is right, agents make better decisions.

- Trust creates adoption: Teams use the system more.

- Adoption creates feedback: More usage generates more corrections and refinements.

- Feedback creates accuracy: The context gets better.

The vertical agent can run this flywheel within their domain, but they can only improve context for their workflow. They can't improve the shared building blocks for all workflows: the underlying definitions of key terms, entity resolution across systems, semantic understanding of metrics, and precedents from one domain that affect others.

The universal context layer runs this flywheel once, at the platform level, and every agent benefits. Every interaction — across sales, support, finance, and operations — improves the shared context. The semantic definition of "customer health" gets refined. The entity resolution between Salesforce contacts and Zendesk users gets better. The understanding of which exceptions create precedents gets sharper.

That’s where compounding lives: at the platform layer, not the application layer.

## From context engineering to context platforms

Today, making AI work in enterprises requires enormous amounts of manual context engineering.

They rely on armies of forward-deployed AI engineers and agent product managers, who gather context from customers and manually update system prompts and evals. This approach works, but it's slow and labor-intensive. And crucially, it means every vertical agent vendor is doing the same context engineering, over and over, for each customer.

Instead, there’s been a shift from "ad-hoc context engineering" to [productized context platforms](https://theoryvc.com/blog-posts/from-context-engineering-to-context-platforms).

[Tomasz](https://tomtunguz.com/operational-analytical-context-databases/) made this point recently: "Enterprises learned a lesson from cloud data warehouses. They handed over both data & compute, then watched as the most strategic asset in their business, how they operate, became someone else’s leverage…” This is why Iceberg exists and [open table formats are winning](https://metadataweekly.substack.com/i/183699428/apache-iceberg-will-go-mainstream-and-drive-the-data-stack-to-fundamental-interoperability). Enterprises realized that ceding control of their data to a single vendor created lock-in that hurt them strategically, and the data itself became leverage against them.

Now imagine doing that with something even more valuable than data: the accumulated institutional knowledge of how your company makes decisions. The tribal knowledge. The exception logic. The "we always do X because of Y" reasoning that lives in people's heads. That’s what context graphs capture.

Enterprises are not going to hand that over to a dozen vertical agent startups, each owning a slice of their operational DNA. Their strategic asset is context, not agents. Enterprises will want to own their own context with open, federated context platforms that any agent can read from, humans can govern, and the organization can improve over time.

## Who will capture the trillion-dollar opportunity?

Context is a trillion-dollar opportunity, but I think the winner won't be the company that sees one workflow deeply. It will be the company that stitches context across workflows, across systems, across the heterogeneous mess of enterprise technology.

Here’s what that actually requires:

1. Cross-system connectivity: Integrations with hundreds of data sources, from warehouses to CRMs to BI tools to communication platforms

2. Operational context synthesis: Extracting SOPs and institutional knowledge from logs, tickets, chats, and human behavior

3. Analytical context management: Governing metric definitions, business entities, and semantic relationships

4. Context delivery at inference time: Serving the right context to any agent, at the moment of decision

5. Feedback loops at scale: Improving context continuously across every interaction

6. Governance and trust: Ensuring all agents operate on a shared version of reality

This is a platform problem, not an application problem.

The companies that have already built #1 and #3 — the ones that connect to Snowflake and Databricks and BigQuery and Salesforce and dbt and Looker — have a structural advantage here. They've already solved the heterogeneity problem, understand how data flows through an organization, and have the relationship graph that ties systems together.

This is the real trillion-dollar opportunity: creating a universal context layer that helps all of the enterprise data and AI systems work together.

In a world of heterogeneity, the integrator always wins. And in a world where enterprises learned the Iceberg lesson, the platform that lets customers own their context will beat the platforms that try to own it for them.

We’re exploring this at [The Great Data Debate](https://atlan.com/great-data-debate-2026/?utm_source=Substack&utm_medium=email&utm_campaign=MDWS_GDD) with thought leaders who are shaping the space from some of the world’s leading organizations. Join [Tristan Handy](https://www.linkedin.com/in/tristanhandy/) (dbt Labs), [Karthik Ravindran](https://www.linkedin.com/in/ravindrankarthik/) (Microsoft), [Bob Muglia](https://www.linkedin.com/in/bob-muglia/) (Snowflake), and [Jaya Gupta](https://www.linkedin.com/in/jayagupta10/) (Foundation Capital) as they unpack where we are today and debate who’s best positioned to win the trillion-dollar opportunity ahead.

I’d love to hear what you think. Share your thoughts in the comments!

## X Article Metadata

- Title: Context Graphs Are a Trillion-Dollar Opportunity. But Who Actually Captures It?
- Preview: Jaya Gupta's thesis is right about context graphs, and wrong about who wins. In a world of heterogeneity, the integrator always wins, not the application.
If you’re in the data world, you probably saw

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
