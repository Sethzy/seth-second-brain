---
type: wiki_article
title: Agent Framework Landscape
updated_at: 2026-07-03
status: draft
source_count: 19
tags:
  - agent-frameworks
  - agent-runtimes
  - harness-engineering
  - ai-sdk
  - eve
  - deep-agents
---

# Agent Framework Landscape

> Sources: LangChain framework/runtime/harness taxonomy, 2026-06-13 capture; LangChain Deep Agents overview, 2026-06-12 capture; LangChain Two Sandbox Patterns article, 2026-02-10; Anthropic Claude Agent SDK article, 2026-06-13 capture; OpenAI developer docs and captured OpenAI developer roundup, 2026 captures; Vercel Eve Concepts docs, 2026-06-28 capture; Vercel Introducing Eve announcement, 2026-06-17; Vercel Filesystems And Bash article, 2026-01-09; Omar/DAIR AI Eve X Article, 2026-06-27 capture; current official docs research for Google ADK, Microsoft Agent Framework, CrewAI, Pydantic AI, Mastra, LlamaIndex, Cloudflare Agents, Inngest AgentKit, Strands, AutoGen, Agno, Haystack, and VoltAgent.
> Raw: [Agent Frameworks, Runtimes, and Harnesses](../../raw/intentional/web/2026-06-13-agent-frameworks-runtimes-and-harnesses-oh-my.md); [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md); [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md); [Building agents with the Claude Agent SDK](../../raw/intentional/web/2026-06-13-building-agents-with-the-claude-agent-sdk.md); [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md); [OpenAI skills for Agents SDK maintenance](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md); [AgentOps framework integrations](../../raw/intentional/web/2026-06-13-agentops.md); [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md); [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md); [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md); [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md)
> Source addendum: Sreejith Sreejayan / Towards AI Claude-Code-like Deep Agents walkthrough, 2026-06-10.
> Raw addendum: [Build Your Own Claude Code Using Langchin](../../raw/intentional/web/2026-07-03-build-your-own-claude-code-using-langchin-a-deepdive-into-la.md)

## Overview

Agent frameworks are now splitting into three overlapping layers:

- **Frameworks** give developers model/tool abstractions, structured outputs, provider wrappers, memory, and reusable agent definitions.
- **Runtimes** make agent execution durable: checkpointing, retries, persistence, schedules, event logs, human approval, and resumable long-running work.
- **Harnesses** package opinionated behavior around the model loop: filesystem/workspace, planning, subagents, shell or sandbox execution, compaction, skills, approvals, evals, and debugging.

LangChain's taxonomy is the best local router: LangChain is a framework, LangGraph is a runtime, and Deep Agents is a harness. Vercel eve is important because it collapses several layers into a filesystem-first TypeScript framework with production plumbing built in: durable execution, sandboxed compute, approvals, subagents, evals, channels, schedules, connections, tools, and skills. Treat eve as a high-priority TypeScript production-agent watch item, especially if the target surface is Vercel, Slack/Discord/GitHub channels, or web-native product agents.

Sreejith Sreejayan's Claude Code reconstruction article adds a practical Deep Agents implementation example: start from the simple model/tool loop, then layer in purpose-built file/search/edit/test tools, `write_todos` planning, virtual-filesystem context offloading, task subagents, shell backend plus interrupts, and LangGraph checkpointing. It reinforces that Deep Agents is best read as a harness starter kit rather than a whole product platform: it supplies the general loop and batteries, while safe execution boundaries, domain-specific tools, and behavior prompts remain application work.

Omar/DAIR's Eve article strengthens the local mental model rather than changing it: eve makes the agent definition inspectable as a directory, but it does not mean all product state belongs in files. For an AI CRM, the database/CRM remains the source of truth for accounts, contacts, deals, messages, permissions, and audit events; the eve filesystem owns the agent's instructions, tools, skills, channels, schedules, evals, connections, and sandbox config.

The official Vercel concepts page turns this from a partial watch item into a concrete framework entry: eve discovers the `agent/` directory, validates files, compiles a manifest, serves the runtime as a deployable app, runs sessions on Vercel Workflows, resolves models through AI Gateway, exposes channels, supports Vercel Connect-backed connections, gives every agent one sandbox, and records Agent Runs in Observability.

The new sandbox architecture split is now an explicit comparison dimension. LangChain's pattern is "agent in sandbox" versus "sandbox as tool." Agent-in-sandbox is closer to local dev and tightly couples the harness to the execution environment. Sandbox-as-tool keeps the agent runtime, secrets, conversation state, and business tools outside the sandbox, then calls the sandbox only for isolated execution. Vercel/eve, OpenAI Agents SDK sandbox workspaces, and many hosted product agents should be evaluated through this lens before deciding where files, credentials, and durable state live.

## Shortlist

| Framework | Layer | Best Fit | Watch Notes |
|---|---|---|---|
| Vercel eve | Harness + runtime + framework | TypeScript agents where production deployment, channels, schedules, approvals, subagents, connections, sandbox, observability, and evals should be first-class from day one | Official docs and announcement now captured. Still needs a tiny prototype and beta/API-volatility check. |
| LangChain / LangGraph / Deep Agents | Framework + runtime + harness | Python/JS agents that need mature orchestration, tracing/evals through LangSmith, and a clear path from primitives to batteries-included harness | Deep Agents is the canonical harness reference already in the wiki; the Towards AI walkthrough is a practical Claude Code-shaped build example. |
| OpenAI Agents SDK | Code-first framework + sandbox-capable harness | Apps that need tools, handoffs, guardrails, tracing, and optional sandbox execution in Python or TypeScript | Strong when the app is already OpenAI/Responses-centric or needs sandbox workspaces. |
| Claude Agent SDK | Harness around Claude Code | Agents that should read files, run commands, edit code, search/fetch web, use MCP, spawn subagents, and resume sessions | This is likely what Seth meant by "Claude ADK"; Google owns the ADK name. |
| Google ADK | Multi-language agent development kit | Gemini/Google Cloud/Vertex-oriented agents, multi-agent orchestration, graph workflows, evals, deployment, and A2A | Best default if the target stack is Google Cloud or Gemini-native. |
| Microsoft Agent Framework | Enterprise framework + workflows | Python/.NET teams needing AutoGen-style agents plus Semantic Kernel enterprise features, telemetry, type safety, and graph workflows | Direct successor path for AutoGen/Semantic Kernel users. |
| CrewAI | Python multi-agent framework | Role-based agent teams plus production flows where a Flow controls state and delegates hard work to Crews | Useful mental model: Flow is process; Crew is autonomous work unit. |
| Pydantic AI | Typed Python framework | Production Python apps where typed dependencies, validated tools, structured output, evals, Logfire/OTel, and model portability matter | Strong for "FastAPI feeling" in agent apps. |
| Mastra | TypeScript app framework | TS agents with memory, workflows, RAG, MCP, evals, observability, and web-app integration | A practical TypeScript alternative to LangChain.js when the app layer matters. |
| LlamaIndex | Context/data agent framework | Document-heavy, RAG-heavy, workflow-heavy agents where data ingestion, parsing, indexing, and context-aware reasoning are core | Strongest in knowledge/document automation. |
| Cloudflare Agents | Edge/stateful runtime | Stateful agents with WebSockets, Durable Objects, scheduling, fibers/durable execution, and Workers-native deployment | More runtime/platform than general agent framework. |
| Inngest AgentKit | TypeScript orchestration | Multi-agent networks with deterministic routing, typed state, MCP tools, live UI streaming, and durable Inngest steps | Strong when workflow durability and event-driven app integration are central. |
| Strands Agents | Python/TypeScript SDK | Model-first AWS-friendly agents with MCP, multi-agent patterns, evals, OTel, and Bedrock/OpenAI/Anthropic/Google support | Worth tracking for AWS/Bedrock ecosystems. |

## Broader Watchlist

- **AutoGen** remains a major multi-agent research/prototyping framework, but Microsoft is steering production work toward Microsoft Agent Framework.
- **Semantic Kernel** remains relevant as enterprise middleware and plugin infrastructure; greenfield agent orchestration should compare it against Microsoft Agent Framework first.
- **Agno** is an SDK/runtime/control-plane path for owning agent platforms, sessions, memory, tracing, scheduling, RBAC, and audit logs in your own cloud.
- **Haystack** is strongest when agents sit on top of retrieval pipelines and tool catalogs, especially with searchable toolsets and MCP exposure.
- **VoltAgent** is another TypeScript agent engineering platform with agents, workflows, memory, RAG, guardrails, MCP, voice, evals, and an ops console.
- **DBOS, Temporal, and Inngest** are not always "agent frameworks," but they are crucial runtime choices when the hardest problem is durable execution rather than model orchestration.

## Decision Rules

- Start with **eve** when the desired product shape is an agent directory that deploys like a Vercel app and includes tools, skills, subagents, channels, schedules, approvals, connections, sandboxes, and evals without building all plumbing. Keep customer/product truth in databases and business systems; use the directory as the agent definition and operating surface.
- Treat **sandbox architecture** as a first-order decision. Choose agent-in-sandbox when local/prod mirroring and direct environment access matter most. Choose sandbox-as-tool when credentials, agent state, observability, and product mutations should stay outside the execution boundary.
- Start with **Deep Agents** when the task needs a general-purpose harness with planning, filesystem context, subagents, compaction, skills, and memory, especially for research/coding-style tasks.
- Start with **OpenAI Agents SDK** when you want code-first orchestration with handoffs, guardrails, tracing, and sandbox workspaces while staying close to the OpenAI API surface.
- Start with **Claude Agent SDK** when you want Claude Code's file/command/edit/search/fetch loop as a programmable library.
- Start with **Pydantic AI** when type safety, dependency injection, structured outputs, and Python application ergonomics are the main priority.
- Start with **Mastra** when a TypeScript product needs a unified app framework for agents, workflows, memory, RAG, MCP, observability, and deployment adapters.
- Start with **LlamaIndex** when the agent's value depends on document parsing, indexing, retrieval, and context-aware reasoning over private data.
- Start with **Cloudflare Agents, DBOS, Temporal, or Inngest** when the agent will wait, resume, retry, schedule, or survive failures for hours or days.

## Open Questions

- Can eve replace the current Vercel AI SDK + custom workflow glue for Seth's web-native agent experiments, or is it still beta-grade for anything beyond prototypes?
- What is the smallest apples-to-apples benchmark across eve, Deep Agents, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, and Mastra?
- Should this repo maintain a `framework-comparison.md` matrix with language, runtime, memory, sandbox, MCP, approval, eval, observability, deployment, and maturity columns?
- Which framework should power the first Second Brain maintenance agent: Deep Agents, OpenAI Agents SDK sandbox agents, or just Codex plus repo scripts?
- Does "Claude ADK" in Seth's notes mean Claude Agent SDK, Claude Code SDK, or Google ADK? Use "Claude Agent SDK" for Anthropic and "Google ADK" for Google unless Seth says otherwise.

## Sources

- [Agent Frameworks, Runtimes, and Harnesses](../../raw/intentional/web/2026-06-13-agent-frameworks-runtimes-and-harnesses-oh-my.md)
- [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md)
- [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md)
- [Building agents with the Claude Agent SDK](../../raw/intentional/web/2026-06-13-building-agents-with-the-claude-agent-sdk.md)
- [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md)
- [OpenAI skills for Agents SDK maintenance](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md)
- [AgentOps framework integrations](../../raw/intentional/web/2026-06-13-agentops.md)
- [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md)
- [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md)
- [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md)
- [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md)

## See Also

- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Agent Skill Libraries And Requirements](../ai-coding/agent-skill-libraries-and-requirements.md)
- [Sandbox Filesystem Agent Architecture](sandbox-filesystem-agent-architecture.md)
- [Vercel Eve Framework](vercel-eve-framework.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
