---
type: wiki_article
title: Agent Framework Landscape
updated_at: 2026-06-18
status: draft
source_count: 13
tags:
  - agent-frameworks
  - agent-runtimes
  - harness-engineering
  - ai-sdk
  - eve
  - deep-agents
---

# Agent Framework Landscape

> Sources: LangChain framework/runtime/harness taxonomy, 2026-06-13 capture; LangChain Deep Agents overview, 2026-06-12 capture; Anthropic Claude Agent SDK article, 2026-06-13 capture; OpenAI developer docs and captured OpenAI developer roundup, 2026 captures; Vercel eve announcement partial, 2026-06-18 staged; current official docs research for Google ADK, Microsoft Agent Framework, CrewAI, Pydantic AI, Mastra, LlamaIndex, Cloudflare Agents, Inngest AgentKit, Strands, AutoGen, Agno, Haystack, and VoltAgent.
> Raw: [Agent Frameworks, Runtimes, and Harnesses](../../raw/intentional/web/2026-06-13-agent-frameworks-runtimes-and-harnesses-oh-my.md); [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md); [Building agents with the Claude Agent SDK](../../raw/intentional/web/2026-06-13-building-agents-with-the-claude-agent-sdk.md); [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md); [OpenAI skills for Agents SDK maintenance](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md); [AgentOps framework integrations](../../raw/intentional/web/2026-06-13-agentops.md); [Vercel eve announcement partial](../../staging/incomplete-captures/web/2026-06-18-vercel-eve-announcement-partial.md)

## Overview

Agent frameworks are now splitting into three overlapping layers:

- **Frameworks** give developers model/tool abstractions, structured outputs, provider wrappers, memory, and reusable agent definitions.
- **Runtimes** make agent execution durable: checkpointing, retries, persistence, schedules, event logs, human approval, and resumable long-running work.
- **Harnesses** package opinionated behavior around the model loop: filesystem/workspace, planning, subagents, shell or sandbox execution, compaction, skills, approvals, evals, and debugging.

LangChain's taxonomy is the best local router: LangChain is a framework, LangGraph is a runtime, and Deep Agents is a harness. Vercel eve is important because it collapses several layers into a filesystem-first TypeScript framework with production plumbing built in: durable execution, sandboxed compute, approvals, subagents, evals, channels, schedules, tools, and skills. Treat eve as a new high-priority watch item for TypeScript production agents, especially if the target surface is Vercel, Slack/Discord/GitHub channels, or web-native product agents.

## Shortlist

| Framework | Layer | Best Fit | Watch Notes |
|---|---|---|---|
| Vercel eve | Harness + runtime + framework | TypeScript agents where production deployment, channels, schedules, approvals, subagents, and evals should be first-class from day one | New public-preview entrant. Needs full source capture and a tiny prototype. |
| LangChain / LangGraph / Deep Agents | Framework + runtime + harness | Python/JS agents that need mature orchestration, tracing/evals through LangSmith, and a clear path from primitives to batteries-included harness | Deep Agents is the canonical harness reference already in the wiki. |
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

- Start with **eve** when the desired product shape is an agent directory that deploys like a Vercel app and includes tools, skills, subagents, channels, schedules, approvals, and evals without building all plumbing.
- Start with **Deep Agents** when the task needs a general-purpose harness with planning, filesystem context, subagents, compaction, skills, and memory, especially for research/coding-style tasks.
- Start with **OpenAI Agents SDK** when you want code-first orchestration with handoffs, guardrails, tracing, and sandbox workspaces while staying close to the OpenAI API surface.
- Start with **Claude Agent SDK** when you want Claude Code's file/command/edit/search/fetch loop as a programmable library.
- Start with **Pydantic AI** when type safety, dependency injection, structured outputs, and Python application ergonomics are the main priority.
- Start with **Mastra** when a TypeScript product needs a unified app framework for agents, workflows, memory, RAG, MCP, observability, and deployment adapters.
- Start with **LlamaIndex** when the agent's value depends on document parsing, indexing, retrieval, and context-aware reasoning over private data.
- Start with **Cloudflare Agents, DBOS, Temporal, or Inngest** when the agent will wait, resume, retry, schedule, or survive failures for hours or days.

## Open Questions

- Can eve replace the current Vercel AI SDK + custom workflow glue for Seth's web-native agent experiments, or is it too new for anything beyond prototypes?
- What is the smallest apples-to-apples benchmark across eve, Deep Agents, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, and Mastra?
- Should this repo maintain a `framework-comparison.md` matrix with language, runtime, memory, sandbox, MCP, approval, eval, observability, deployment, and maturity columns?
- Which framework should power the first Second Brain maintenance agent: Deep Agents, OpenAI Agents SDK sandbox agents, or just Codex plus repo scripts?
- Does "Claude ADK" in Seth's notes mean Claude Agent SDK, Claude Code SDK, or Google ADK? Use "Claude Agent SDK" for Anthropic and "Google ADK" for Google unless Seth says otherwise.

## Sources

- [Agent Frameworks, Runtimes, and Harnesses](../../raw/intentional/web/2026-06-13-agent-frameworks-runtimes-and-harnesses-oh-my.md)
- [LangChain Deep Agents overview](../../raw/intentional/web/2026-06-12-langchain-deep-agents-overview.md)
- [Building agents with the Claude Agent SDK](../../raw/intentional/web/2026-06-13-building-agents-with-the-claude-agent-sdk.md)
- [OpenAI for Developers in 2025](../../raw/intentional/web/2025-12-30-openai-openai-for-developers-in-2025.md)
- [OpenAI skills for Agents SDK maintenance](../../raw/intentional/web/2026-03-09-openai-using-skills-to-accelerate-oss-maintenance-openai-developers.md)
- [AgentOps framework integrations](../../raw/intentional/web/2026-06-13-agentops.md)
- [Vercel eve announcement partial](../../staging/incomplete-captures/web/2026-06-18-vercel-eve-announcement-partial.md)

## See Also

- [Agentic Engineering Practices](../ai-coding/agentic-engineering-practices.md)
- [Agent Skill Libraries And Requirements](../ai-coding/agent-skill-libraries-and-requirements.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
