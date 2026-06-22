---
type: raw_capture
source_type: x
url: https://x.com/largedatabank/status/2057927487036723218
original_url: https://x.com/largedatabank/status/2057927487036723218
author: "Jordan Lewis"
handle: largedatabank
status_id: 2057927487036723218
captured_at: 2026-06-19T23:03:53+08:00
published_at: "Fri May 22 20:52:02 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 2
  reposts: 1
  likes: 16
---

# X post by @largedatabank

## Source

- Original: [https://x.com/largedatabank/status/2057927487036723218](https://x.com/largedatabank/status/2057927487036723218)
- Canonical: [https://x.com/largedatabank/status/2057927487036723218](https://x.com/largedatabank/status/2057927487036723218)
- Author: Jordan Lewis (@largedatabank)

## Verbatim Text

Mica: AI Transformation at Cockroach Labs

In the past 3 months, work life in every division at Cockroach Labs has transformed thanks to Mica, our homegrown agentic AI work platform. Mica is an agentic surface, built on @CockroachDB, that lets anyone at the company build agents and apps that work with all of their corporate tools.

Last month I posted about becoming 1% better every day with AI, a copy of a post I'd sent to my engineering managers back in February. The post resonated internally, but it also exposed a problem I hadn't fully articulated yet.

The most common response I got was "great idea, but do you really want all of us to make our own MCP servers for Google Docs"? People wanted the AI-native workflow, but they just didn't want to spend the time to configure MCPs, wire up OAuth connections, or manage their own local tool servers. The few who pushed through had wildly different setups, with no way to share what they'd learned.

We'd created urgency without providing infrastructure.

So in February, we started building Mica — Cockroach Labs' central agentic AI surface. One place where every employee could get a fully configured, context-aware AI assistant platform connected to all of our company's tools, without touching a config file.

3 months later:

- ~300 daily active users across every department

- 1,600 apps built by employees in plain English

- 50,000+ sessions, 1.8 million app tool calls

- This quote:

Here's what we built, and why it worked.

Everything connects on day one.

Mica connects Claude to 31 workplace services — Gmail, Slack, Jira, Snowflake, Salesforce, GitHub, Confluence, Gong, Zendesk, Figma, and more — through a federated identity system.

No configuration. Sign in once, connect your tools with OAuth, and Mica already knows your calendar, your tickets, your customers, your pipeline. Every session starts with context instead of catching up.

The key design decision: Mica acts as you. Not a service account. Your credentials, your permissions, your access — never more. Every write action shows you exactly what it's about to do before it does it.

This matters for trust. Dipping your feet into the agentic waters for the first times requires understanding how agents act, and this federated identity model is something that people understand intuitively.

Skills: one person's breakthrough becomes everyone's baseline.

Users save repeatable workflows as skills — instructions that teach Mica exactly how a specific task should be done, forever. Through a company-wide marketplace, those workflows are shared and remixed across teams.

My weekly engineering communique is drafted every Monday morning before I've opened my laptop. Our sales team has a skill that pulls live pipeline data from Snowflake and formats it for exec review. One engineer built a skill that reads a failing test, traces the bug through the codebase, and files a clean fix PR — without touching a terminal.

People are using AI, and also teaching it how their work works. Then sharing those lessons with the whole company.

Triggers: agents that run without user intervention

Mica runs scheduled, headless agents on a schedule. No chat required.

Every Monday, the weekly changelog posts to Slack automatically. Every Tuesday night, it reads exec meeting notes and cascades the right context to my engineering staff before Wednesday's meeting. Finance gets overnight anomaly reports. Support gets morning escalation digests.

Apps: vibe coded connected applications with builtin RBAC and instant shareability

Anyone at Cockroach Labs can describe a dashboard, tool, or stateful application they need — in plain English — and Mica builds it. A fully functional web app, running inside the product, with live access to all 31 connected services, LLMs, and the same approval flows that govern every other Mica action. Apps have built-in role based access control, shareability, and durability in their own isolated CockroachDB instance.

The barrier from "I wish I had an app for this" to "I have an app for this, and my coworkers can immediately use it" is now one conversation, with a predictable reaction:

In 12 weeks, our employees have built over 1600 apps. Here are some examples that are running in production.

- Support Command Center — 853,749 AI tool calls. A live intelligence layer over Zendesk, Jira, and customer accounts, built by our support team without an engineering sprint.

- Event Campaign Activity Intelligence — 138,813 calls. Marketing's real-time campaign tracker, same story.

- DealPulse — a pipeline intelligence app,

Our FP&A partner Allen uses Mica to build margin analyzers and advanced financial dashboards. His verdict on the money we've spent on AI in 90 days:

When building this out, I did not expect that one of the most enthusiastic power users at the company is in Finance.

How CockroachDB powers Mica

I mentioned at the top of the article that Mica is powered by CockroachDB. While this was clearly a golden opportunity to dogfood the database, there are 3 reasons why CockroachDB was an amazing fit for an internal corporate AI tool like Mica.

Agentic State Management Agents write data - a lot of it. Conversation logs, tool calls, user preferences, task progress, audits, and more. CockroachDB is a great fit for agent data - its horizontal scalability, resilience and consistency makes sure that agents can run interrupted 24/7 without running into scalability limits. And online schema changes make sure that the agentic backplane can be changed and upgraded without interrupting agentic work that people at the company are conducting even over the weekends.

Vector + Relational in 1 database. CockroachDB's native vector search enables Mica to provide semantic search to users across all their conversations, no separate search database required. Conversations are embedded and stored in a vector index that is used for fast retrieval based on a vague memory of what a conversation was about.

Multi-tenant data at scale. Every app in Mica can use its own, freshly provisioned isolated CockroachDB Cloud Basic instance. This takes apps from "pretty dashboard" to "source of truth" - enabling shareable internal apps that store data like customer health scores, personal performance reflections, pastebins, or even financial planning data. This capability is made easy with CockroachDB Cloud's API, which allows users to spin up fresh CockroachDB Basic clusters in just a few seconds programmatically.

How we use Mica to build Mica

Mica is also exposed on Slack, and people love to give Mica feedback via Mica. This directly informs Mica's backlog, and allows our entire company to build Mica themselves. This feedback loop (informed by @bcherny's process of building Claude Code) makes giving feedback feel safe for internal customers - and turning around feature requests quickly makes sure that Mica continues to satisfy internal need for agents and agentic systems at Cockroach Labs.

What we learned

So at the end of the day, the lesson isn't about pure, fiery AI-pilled tokenmaxxing. It's actually about providing shared infrastructure that everyone can use in a way that's legible and shareable.

When I told our engineering managers to get 1% better every day, I was right about the direction but wrong about the mechanism. Individual ambition doesn't scale. Infrastructure does. Mica didn't succeed because we hired AI enthusiasts or mandated adoption — it succeeded because we removed every friction point between "I have an idea" and "it's running in production."

People across every division at @CockroachDB are now building tools, automating workflows, and teaching AI how their work actually works. And not via a top-down tokenmaxxing mandate! Really this is happening because it's finally easier to build the thing yourself than to keep doing it manually.

That's 1% better every day, for real this time.

## X Article Metadata

- Title: Mica: AI Transformation at Cockroach Labs
- Preview: In the past 3 months, work life in every division at Cockroach Labs has transformed thanks to Mica, our homegrown agentic AI work platform. Mica is an agentic surface, built on @CockroachDB, that lets

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
