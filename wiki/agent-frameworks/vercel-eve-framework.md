---
type: wiki_article
title: Vercel Eve Framework
updated_at: 2026-06-28
status: active
source_count: 3
tags:
  - vercel
  - eve
  - ai-sdk
  - durable-agents
  - sandbox
  - agent-frameworks
---

# Vercel Eve Framework

> Sources: Vercel Eve Concepts docs, 2026-06-28 capture; Vercel Introducing Eve announcement, 2026-06-17; Omar/DAIR AI Eve X Article, 2026-06-27 capture.
> Raw: [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md); [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md); [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md)

## Overview

Vercel eve is a filesystem-first framework for durable backend AI agents. Its thesis is that an agent should be readable as a directory: the files under `agent/` define what the agent is, what tools it has, what skills it can load, where it can receive work, when it can run on its own, which integrations it can reach, and what sandbox it can use.

The official docs frame eve as a compiler/runtime: you author an `agent/` project, eve discovers named files and directories, validates them, compiles a manifest, and serves the result as a deployable app. The announcement frames the same idea as "production already built in": durable execution, sandboxed compute, human approvals, subagents, evals, channels, and connections.

Use this page as the canonical local explanation of eve. Use [Agent Framework Landscape](agent-framework-landscape.md) for comparisons with Mastra, Cloudflare Agents, Claude Agent SDK, OpenAI Agents SDK, Deep Agents, and similar options. Use [Sandbox Filesystem Agent Architecture](sandbox-filesystem-agent-architecture.md) for the filesystem, durable storage, shell, and sandbox mental model.

## Agent Directory

The core shape is:

```text
agent/
  agent.ts              runtime config, especially model
  instructions.md       always-on system prompt
  tools/                typed actions, one tool per file
  skills/               on-demand procedures or domain knowledge
  subagents/            child agents with separate history/state
  channels/             Slack, HTTP, Discord, Teams, etc.
  connections/          typed external integrations
  sandbox/              isolated compute environment
  instrumentation.ts    optional OpenTelemetry setup
```

The directory is not "where all business data goes." It is the agent definition surface. For an AI CRM, the CRM/database still owns accounts, contacts, deals, messages, permissions, approvals, and audit trails. The `agent/` directory owns behavior: prompts, tools, playbooks, channels, schedules, evals, and sandbox rules.

## Turn Flow

End to end, an eve agent works like this:

1. A channel or HTTP request starts a session. A channel can be Slack, HTTP, Discord, Teams, Telegram, Twilio, GitHub, Linear, or a custom adapter.
2. Each user message or external event creates a turn inside that session.
3. Eve loads the agent definition from the `agent/` directory: instructions, model config, available tools, relevant skills, channels, connections, and sandbox configuration.
4. The model loop runs through AI SDK and model strings resolve through Vercel AI Gateway on deploy, so provider keys and routing live outside the agent prompt.
5. The agent can call typed tools, load skills, delegate to subagents, read/write sandbox files, or stream lifecycle events back to the client.
6. If an action is risky, an approval gate can pause the session without consuming compute and resume from the same place once a human approves.
7. Vercel Workflows persist the session as an event log and replay it to reconstruct state, so sessions can survive cold starts, deploys, crashes, and long waits.
8. Observability records sessions, turns, tool calls, reasoning, timing, token usage, and optional OpenTelemetry spans. Evals can run the real agent locally or in CI.

## Components

- **Runtime config**: `agent/agent.ts` uses `defineAgent` to set model and options.
- **Instructions**: `agent/instructions.md` is the always-on system prompt before every model call.
- **Tools**: `agent/tools/*.ts` defines typed actions. The filename becomes the tool name the model sees.
- **Skills**: `agent/skills/*` holds larger procedures or reference material loaded only when relevant.
- **Subagents**: child agents run focused subtasks with separate conversation history and state; they are different from skills, which add context to the current agent.
- **Connections**: `agent/connections/*` points at MCP servers or APIs and keeps provider configuration and credentials out of the model prompt. Delegated credentials can use Vercel Connect.
- **Channels**: platform entry points into the same runtime. The same agent can live behind HTTP and inside Slack or other channels.
- **Sandbox**: every eve agent has one isolated bash-style environment with its own filesystem. Framework tools such as `bash`, `read_file`, and `write_file` target it. On Vercel, this can run on Vercel Sandbox using ephemeral microVMs for untrusted or model-generated commands.
- **Observability and evals**: Agent Runs show session and turn detail in Vercel; OpenTelemetry can export spans elsewhere; evals turn expected behavior into test suites.

## AI CRM Interpretation

For a NewBot-style AI CRM, eve's shape maps cleanly:

- `agent/instructions.md`: the CRM agent's job, tone, safety rules, and "do not send/update without approval" policy.
- `agent/tools/`: typed CRM actions such as `search_accounts`, `summarize_account`, `draft_followup`, `update_deal_stage`, and `create_task`.
- `agent/skills/`: sales playbooks, qualification rules, objection handling, CRM hygiene rules, account-research procedure, and follow-up style guide.
- `agent/channels/`: Slack/web entry points for reps and founders.
- `agent/schedules/`: recurring checks such as stale deals, no-reply follow-ups, upcoming meetings, or weekly pipeline summary.
- `agent/connections/`: Salesforce/HubSpot/Attio, Gmail, Calendar, Gong/Granola, Notion, Snowflake, Linear, and internal APIs.
- `agent/sandbox/`: isolated work for PDFs, spreadsheets, CSV exports, generated reports, browser/code tasks, or anything user-uploaded or model-generated.
- CRM/database: the source of truth for customers, deals, permissions, messages, approvals, and audit history.

The simplest rule: files define the agent; databases define the business.

## Relation To OpenClaw

OpenClaw's local model starts from a gateway, persistent sessions, tool policy, shared files, and multi-agent routing. Eve starts from a committed `agent/` directory and a Vercel deployment path. They agree on the important product ideas: durable sessions, tool gates, approvals, sandboxing, channel surfaces, and readable agent behavior.

The implementation choice is different. Use OpenClaw as the self-hosted operating-layer reference. Use eve when the desired shape is a TypeScript/Vercel agent app with production concerns bundled into the framework.

## Open Questions

- Is eve mature enough for Seth's first production-ish Slackbot or AI CRM prototype, or should it stay in prototype/evaluation mode while it is beta?
- What is the smallest useful prototype: Second Brain Slackbot, AI CRM account brief worker, lead triage agent, or call-summary agent?
- How should a Vercel-hosted eve agent write back to this Karpathy-style wiki without violating the raw/compiled separation?
- Which actions need approval: sending email, updating CRM, creating tasks, publishing summaries, writing wiki pages, or running sandbox code?

## Sources

- [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md)
- [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md)
- [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md)

## See Also

- [Agent Framework Landscape](agent-framework-landscape.md)
- [Sandbox Filesystem Agent Architecture](sandbox-filesystem-agent-architecture.md)
- [Vercel Agent Templates And Sandboxes](../ai-coding/vercel-agent-templates-and-sandboxes.md)
- [OpenClaw Architecture And Operating Model](../openclaw/openclaw-architecture-and-operating-model.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
