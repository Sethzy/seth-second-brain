---
type: wiki_article
title: Vercel Agent Templates And Sandboxes
updated_at: 2026-06-28
status: draft
source_count: 14
tags:
  - vercel
  - ai-sdk
  - sandbox
  - slack-agents
  - workflow-devkit
  - gtm-agents
  - website-cloning
---

# Vercel Agent Templates And Sandboxes

> Sources: Seth pasted Vercel AI SDK sandbox templates batch, 2026-06-11; Vercel Slack Agent Template README, 2026-06-11 capture; Vercel Slack Agent Template page, 2026-06-11 capture; Vercel Call Summary Agent with Sandbox README, 2026-06-11 capture; Vercel Call Summary Agent template page, 2026-06-11 capture; Vercel Lead Agent README, 2026-06-11 capture; Vercel Lead Processing Agent template page, 2026-06-11 capture; av1dlive X link staged partial, 2026-06-11; Omar/DAIR AI Eve X Article, 2026-06-27 capture; Vercel Eve Concepts docs, 2026-06-28 capture; Vercel Introducing Eve announcement, 2026-06-17
> Raw: [Vercel AI SDK sandbox agent templates batch](../../raw/intentional/pasted/2026-06-11-vercel-ai-sdk-sandbox-agent-templates-batch.md); [Vercel Slack Agent Template README](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-readme.md); [Vercel Slack Agent Template page](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-page.md); [Vercel Call Summary Agent with Sandbox README](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-with-sandbox-readme.md); [Vercel Call Summary Agent template page](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-template-page.md); [Vercel Lead Agent README](../../raw/intentional/web/2026-06-11-vercel-lead-agent-readme.md); [Vercel Lead Processing Agent template page](../../raw/intentional/web/2026-06-11-vercel-lead-processing-agent-template-page.md); partial lead: [av1dlive Vercel sandbox agent X link](../../staging/incomplete-captures/x/2026-06-11-av1dlive-vercel-sandbox-agent-lead.md)
> Source addendum: JCodesMore ai-website-cloner-template repository snapshot, 2026-06-28 capture; Omar/DAIR AI Eve X Article, 2026-06-27 capture; Vercel Eve Concepts docs, 2026-06-28 capture; Vercel Introducing Eve announcement, 2026-06-17; Vercel Filesystems And Bash article, 2026-01-09; LangChain Two Sandbox Patterns article, 2026-02-10.
> Raw addendum: [JCodesMore ai-website-cloner-template repository snapshot](../../raw/intentional/web/2026-06-28-jcodesmore-ai-website-cloner-template-repository-snapshot-complete.md); [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md); [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md); [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md); [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md); [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md)

## Overview

This batch points to Vercel's emerging agent reference-architecture lane: AI SDK agents, eve filesystem-first agent projects, Workflow DevKit durable execution, Slack as a human-in-the-loop surface, Vercel AI Gateway for model access, and Vercel Sandbox for secure file/code exploration.

The Slack Agent Template is the base work surface. It uses Workflow DevKit's `DurableAgent`, AI SDK tools, Slack Bolt, Nitro, streaming Slack Assistant responses, and approval hooks for sensitive actions such as joining channels. Its reusable pattern is: receive a Slack event, collect thread context, start a durable workflow, run an agent with typed tools, stream output back to Slack, and pause for approval when a tool needs human authorization.

The Call Summary Agent applies the same architecture to sales-call analysis. Gong is the starting integration, but the README explicitly frames the pattern as adaptable to Zoom, Google Meet, CRM context, Slack posting, and other services. The agent loads transcript and context files into a Vercel Sandbox, explores them with a bash tool, and returns structured call summaries, objections, tasks, and insights.

The Lead Agent applies the pattern to inbound GTM. A contact-sales form starts a Workflow DevKit background workflow, a deep-research AI SDK agent researches the lead, `generateObject` qualifies the lead, `generateText` drafts the reply, and Slack approval gates outbound email.

JCodesMore's `ai-website-cloner-template` belongs in this page as the repo-template counterpart to Vercel's runtime templates. It does not use Workflow DevKit; instead, it packages a Vercel-ready Next.js scaffold plus a cross-agent `/clone-website` skill that turns browser inspection, design references, `docs/research/` artifacts, downloaded assets, and build/visual checks into the workbench for reconstructing a site.

The Omar/DAIR Eve article is the clearest plain-language capture for the new Vercel stack. It says an eve agent is a directory: `agent/instructions.md` and optional `agent/agent.ts` define identity and runtime config, while `agent/tools/`, `agent/skills/`, `agent/subagents/`, `agent/connections/`, `agent/channels/`, `agent/schedules/`, evals, and sandbox config are auto-discovered files. The practical implementation model is "drop a file, behavior changes, commit the diff."

The official concepts and launch pages confirm the same shape and add the production mapping: sessions and turns run on Vercel Workflows, deployed model strings resolve through AI Gateway, Vercel Connect brokers delegated credentials, every agent has one sandbox, Agent Runs shows sessions/turns/tool calls/reasoning/tokens, and Vercel Functions plus Fluid Compute host long-running streaming agent turns.

Vercel's filesystem/bash article explains why the Call Summary and AI CRM patterns are attractive: transcripts, CRM records, account notes, support tickets, and document extractions can be projected into directories, then the agent can use `ls`, `find`, `grep`, `cat`, and scripts to retrieve only the relevant context. LangChain's sandbox-pattern article clarifies the boundary: the sandbox can either contain the agent or be called as a tool. For Vercel/eve-style product agents, the safer default is to keep CRM truth and agent state outside the sandbox while using the sandbox for isolated file/code execution.

## Reusable Architecture

- Slack can be the operating surface for agents, not just a notification sink: thread context, assistant events, Block Kit approvals, and webhook callbacks all become part of the workflow.
- Workflow DevKit gives agents durable control flow: `use workflow` for the long-running orchestration, `use step` for retryable side effects, and hooks for waiting on human approval without burning compute.
- AI SDK is the model/tool layer: typed tools, agent loops, `generateObject` for structured qualification, and `generateText` for drafts.
- eve is the project/framework layer: it turns the agent's filesystem into deployable production software with durable sessions, channels, schedules, approvals, subagents, evals, connections, observability, model routing, and sandbox support.
- Vercel Sandbox is useful when the agent needs to inspect files, transcripts, research notes, or generated context with shell-like tools instead of squeezing everything into the prompt.
- Tools and sandbox have different jobs. A tool executes trusted application logic in the app runtime; the sandbox is for isolated shell/file/code work, especially agent-generated or user-provided artifacts that should not touch the main runtime directly.
- Filesystem context is an interface, not automatically the durable source of truth. For an AI CRM, project account/call/customer data into files for inspection, but keep canonical records in the CRM/database and keep artifacts in durable storage.
- Skills are progressive disclosure for playbooks and procedures: keep long support, CRM, sales, or filing instructions as markdown skills and load them only when the request matches.
- AI Gateway is the provider abstraction layer: one model endpoint, centralized keys, failover, and easier provider swaps.
- Human-in-the-loop should be a first-class primitive. Joining a Slack channel, sending an email, updating CRM, or posting a summary should pause for approval when risk is meaningful.
- Evals should drive the real agent through sessions and assert on behavior such as tool calls, completions, and approval gates, giving prompt/tool changes a CI-like safety net.
- Repo templates can be agent workbenches even without a hosted runtime: pre-scaffold the app, preserve `docs/research/` and `docs/design-references/` as durable extraction artifacts, and distribute the same skill across coding-agent surfaces.

## Candidate Uses

- Second-brain Slackbot: adapt the Slack Agent Template so Slack threads can query this repo, save capture candidates, and ask for confirmation before writing raw/staging/wiki updates.
- AI CRM bot: use eve files for the agent definition, playbooks, tools, approvals, channels, schedules, and evals, but keep CRM truth in a database or CRM system. Use files for account briefs, call notes, proposal drafts, and agent skills; use Vercel Sandbox only when the agent must run code, inspect uploaded files, process spreadsheets/PDFs, or generate artifacts in isolation.
- Sales-call intelligence: adapt the Call Summary Agent to process Gong, Zoom, Google Meet, or Granola transcripts into objections, tasks, pain points, next steps, and CRM/wiki updates.
- Inbound lead triage: adapt the Lead Agent to research new leads, classify fit, draft response emails, and ask for Slack approval before any outbound message.
- Acme/eGiro GTM OS: use the call-summary and lead-processing templates as concrete starting points for low-touch onboarding, account research, and sales learning loops.
- Sandbox research worker: use Vercel Sandbox as a safer place for agents to explore downloaded account files, transcripts, CSV exports, and generated reports.
- Website migration/recovery: adapt the website-cloner template into a Codex skill for rebuilding owned or explicitly permitted sites into a modern Next.js/Vercel codebase with screenshot and visual-diff QA.

## Open Questions

- Is Vercel Workflow DevKit mature enough to own Seth's first production-ish Slackbot, or should this stay as a reference architecture while local scripts/Codex handle writes?
- Is eve mature enough to own Seth's first production-ish Slackbot/AI CRM prototype, or should it stay as a reference architecture while local scripts/Codex handle writes?
- Does Vercel Sandbox add enough value over plain server-side file access for transcript/account research, or only when code execution and isolation matter?
- Should the first prototype be a Slack capture bot, call-summary worker, or inbound lead triage flow?
- How should source provenance be written back from a Vercel-hosted agent into this Karpathy-style wiki without breaking the raw/compiled separation?
- Which approval actions belong in Slack buttons versus Codex review: send email, update CRM, create wiki page, add raw capture, or post to a channel?
- Should a local `clone-website` skill live as a Codex skill, a full repo template, or both: a small reusable skill plus a pre-scaffolded Next.js workbench?

## Sources

- [Vercel AI SDK sandbox agent templates batch](../../raw/intentional/pasted/2026-06-11-vercel-ai-sdk-sandbox-agent-templates-batch.md)
- [Vercel Slack Agent Template README](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-readme.md)
- [Vercel Slack Agent Template page](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-page.md)
- [Vercel Call Summary Agent with Sandbox README](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-with-sandbox-readme.md)
- [Vercel Call Summary Agent template page](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-template-page.md)
- [Vercel Lead Agent README](../../raw/intentional/web/2026-06-11-vercel-lead-agent-readme.md)
- [Vercel Lead Processing Agent template page](../../raw/intentional/web/2026-06-11-vercel-lead-processing-agent-template-page.md)
- [av1dlive Vercel sandbox agent X link, partial](../../staging/incomplete-captures/x/2026-06-11-av1dlive-vercel-sandbox-agent-lead.md)
- [JCodesMore ai-website-cloner-template repository snapshot](../../raw/intentional/web/2026-06-28-jcodesmore-ai-website-cloner-template-repository-snapshot-complete.md)
- [Omar/DAIR AI Eve X Article](../../raw/intentional/x/2070884837372703196-omarsar0-building-agents-with-vercel-s-eve-framework-vercel-recently-shipped-eve-an-open-s.md)
- [Vercel Eve Concepts](../../raw/intentional/web/2026-06-28-vercel-eve-concepts.md)
- [Vercel Introducing Eve](../../raw/intentional/web/2026-06-28-vercel-introducing-eve.md)
- [Vercel Filesystems And Bash](../../raw/intentional/web/2026-06-28-how-to-build-agents-with-filesystems-and-bash.md)
- [LangChain Two Sandbox Patterns](../../raw/intentional/web/2026-06-28-the-two-patterns-by-which-agents-connect-sandboxes.md)

## See Also

- [Vercel Eve Framework](../agent-frameworks/vercel-eve-framework.md)
- [Sandbox Filesystem Agent Architecture](../agent-frameworks/sandbox-filesystem-agent-architecture.md)
- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
- [Agent Skill Libraries And Requirements](agent-skill-libraries-and-requirements.md)
