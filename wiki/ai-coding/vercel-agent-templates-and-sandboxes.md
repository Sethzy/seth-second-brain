---
type: wiki_article
title: Vercel Agent Templates And Sandboxes
updated_at: 2026-06-11
status: draft
source_count: 8
tags:
  - vercel
  - ai-sdk
  - sandbox
  - slack-agents
  - workflow-devkit
  - gtm-agents
---

# Vercel Agent Templates And Sandboxes

> Sources: Seth pasted Vercel AI SDK sandbox templates batch, 2026-06-11; Vercel Slack Agent Template README, 2026-06-11 capture; Vercel Slack Agent Template page, 2026-06-11 capture; Vercel Call Summary Agent with Sandbox README, 2026-06-11 capture; Vercel Call Summary Agent template page, 2026-06-11 capture; Vercel Lead Agent README, 2026-06-11 capture; Vercel Lead Processing Agent template page, 2026-06-11 capture; av1dlive X link staged partial, 2026-06-11
> Raw: [Vercel AI SDK sandbox agent templates batch](../../raw/intentional/pasted/2026-06-11-vercel-ai-sdk-sandbox-agent-templates-batch.md); [Vercel Slack Agent Template README](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-readme.md); [Vercel Slack Agent Template page](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-page.md); [Vercel Call Summary Agent with Sandbox README](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-with-sandbox-readme.md); [Vercel Call Summary Agent template page](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-template-page.md); [Vercel Lead Agent README](../../raw/intentional/web/2026-06-11-vercel-lead-agent-readme.md); [Vercel Lead Processing Agent template page](../../raw/intentional/web/2026-06-11-vercel-lead-processing-agent-template-page.md); partial lead: [av1dlive Vercel sandbox agent X link](../../staging/incomplete-captures/x/2026-06-11-av1dlive-vercel-sandbox-agent-lead.md)

## Overview

This batch points to Vercel's emerging agent reference-architecture lane: AI SDK agents, Workflow DevKit durable execution, Slack as a human-in-the-loop surface, Vercel AI Gateway for model access, and Vercel Sandbox for secure file/code exploration.

The Slack Agent Template is the base work surface. It uses Workflow DevKit's `DurableAgent`, AI SDK tools, Slack Bolt, Nitro, streaming Slack Assistant responses, and approval hooks for sensitive actions such as joining channels. Its reusable pattern is: receive a Slack event, collect thread context, start a durable workflow, run an agent with typed tools, stream output back to Slack, and pause for approval when a tool needs human authorization.

The Call Summary Agent applies the same architecture to sales-call analysis. Gong is the starting integration, but the README explicitly frames the pattern as adaptable to Zoom, Google Meet, CRM context, Slack posting, and other services. The agent loads transcript and context files into a Vercel Sandbox, explores them with a bash tool, and returns structured call summaries, objections, tasks, and insights.

The Lead Agent applies the pattern to inbound GTM. A contact-sales form starts a Workflow DevKit background workflow, a deep-research AI SDK agent researches the lead, `generateObject` qualifies the lead, `generateText` drafts the reply, and Slack approval gates outbound email.

## Reusable Architecture

- Slack can be the operating surface for agents, not just a notification sink: thread context, assistant events, Block Kit approvals, and webhook callbacks all become part of the workflow.
- Workflow DevKit gives agents durable control flow: `use workflow` for the long-running orchestration, `use step` for retryable side effects, and hooks for waiting on human approval without burning compute.
- AI SDK is the model/tool layer: typed tools, agent loops, `generateObject` for structured qualification, and `generateText` for drafts.
- Vercel Sandbox is useful when the agent needs to inspect files, transcripts, research notes, or generated context with shell-like tools instead of squeezing everything into the prompt.
- AI Gateway is the provider abstraction layer: one model endpoint, centralized keys, failover, and easier provider swaps.
- Human-in-the-loop should be a first-class primitive. Joining a Slack channel, sending an email, updating CRM, or posting a summary should pause for approval when risk is meaningful.

## Candidate Uses

- Second-brain Slackbot: adapt the Slack Agent Template so Slack threads can query this repo, save capture candidates, and ask for confirmation before writing raw/staging/wiki updates.
- Sales-call intelligence: adapt the Call Summary Agent to process Gong, Zoom, Google Meet, or Granola transcripts into objections, tasks, pain points, next steps, and CRM/wiki updates.
- Inbound lead triage: adapt the Lead Agent to research new leads, classify fit, draft response emails, and ask for Slack approval before any outbound message.
- Acme/eGiro GTM OS: use the call-summary and lead-processing templates as concrete starting points for low-touch onboarding, account research, and sales learning loops.
- Sandbox research worker: use Vercel Sandbox as a safer place for agents to explore downloaded account files, transcripts, CSV exports, and generated reports.

## Open Questions

- Is Vercel Workflow DevKit mature enough to own Seth's first production-ish Slackbot, or should this stay as a reference architecture while local scripts/Codex handle writes?
- Does Vercel Sandbox add enough value over plain server-side file access for transcript/account research, or only when code execution and isolation matter?
- Should the first prototype be a Slack capture bot, call-summary worker, or inbound lead triage flow?
- How should source provenance be written back from a Vercel-hosted agent into this Karpathy-style wiki without breaking the raw/compiled separation?
- Which approval actions belong in Slack buttons versus Codex review: send email, update CRM, create wiki page, add raw capture, or post to a channel?

## Sources

- [Vercel AI SDK sandbox agent templates batch](../../raw/intentional/pasted/2026-06-11-vercel-ai-sdk-sandbox-agent-templates-batch.md)
- [Vercel Slack Agent Template README](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-readme.md)
- [Vercel Slack Agent Template page](../../raw/intentional/web/2026-06-11-vercel-slack-agent-template-page.md)
- [Vercel Call Summary Agent with Sandbox README](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-with-sandbox-readme.md)
- [Vercel Call Summary Agent template page](../../raw/intentional/web/2026-06-11-vercel-call-summary-agent-template-page.md)
- [Vercel Lead Agent README](../../raw/intentional/web/2026-06-11-vercel-lead-agent-readme.md)
- [Vercel Lead Processing Agent template page](../../raw/intentional/web/2026-06-11-vercel-lead-processing-agent-template-page.md)
- [av1dlive Vercel sandbox agent X link, partial](../../staging/incomplete-captures/x/2026-06-11-av1dlive-vercel-sandbox-agent-lead.md)

## See Also

- [Agent Platforms And Work Surfaces](../personal-systems/agent-platforms-and-work-surfaces.md)
- [Agentic GTM Campaign Workflows](../gtm-sales/agentic-gtm-campaign-workflows.md)
- [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md)
