---
type: wiki_article
title: Vapi Agent Builder Update Walkthrough
updated_at: 2026-06-30
status: draft
source_count: 1
tags:
  - voice-agents
  - vapi
  - dashboard
  - observability
  - production-settings
---

# Vapi Agent Builder Update Walkthrough

> Source: [VAPI just got a massive update (Complete Walkthrough) - YouTube](../../raw/intentional/youtube/2026-06-30-vapi-just-got-a-massive-update-complete-walkthrough.md)

## What Changed

This video walks through Vapi's redesigned agent builder. The creator frames the redesign as a sign that Vapi is becoming more enterprise-facing after, in the video's account, a $50M Series B and high call volume. The important product shift is that agent setup is now organized into clearer pages rather than one long cluttered configuration surface.

The main pages are:

- Assistant: core model, transcriber, voice, first message, system prompt, and attached files.
- Logs: per-agent call logs directly inside the agent page.
- Tools: account-level tools assigned to individual assistants.
- Analysis: structured outputs, scorecards, and monitors for post-call extraction and quality tracking.
- Advanced: fallbacks, compliance, webhook server, turn-taking, voicemail detection, timeouts, recording, messaging, idle messages, and deprecated settings.

## Core Stack Controls

The assistant page puts the three cost/quality/latency drivers near the top:

| Layer | What It Controls | Notes From The Video |
|---|---|---|
| Transcriber | Speech-to-text quality, language, endpointing, denoising, profanity/numeral handling | The creator likes Deepgram and recommends background denoising; production agents should have a fallback transcriber from a different provider. |
| Model | Reasoning, instruction following, tool choice, response generation | GPT-4o is presented as strong for voice AI but with more latency. |
| Voice | Text-to-speech realism, speed, volume, background sounds | Cartesia Sonic 3 is highlighted for human-like speech and non-verbal expression; custom voice IDs can be pasted from provider playgrounds. |

The video reinforces the earlier stack decision: Vapi can orchestrate separate providers for STT, LLM, and TTS. This is useful for cost control and provider optionality, but it also means the demo cost is a stack of Vapi platform cost plus provider usage rather than one single model bill.

## Prompt And First Message

The first-message setting matters because inbound and outbound calls behave differently:

- Inbound: the assistant often speaks first, such as "Hi, this is Tim from Eximus. I'm your digital assistant. What can I help you with?"
- Outbound: the human usually answers first, so the assistant may wait for the user or generate a first message based on the prompt.

The system prompt remains the main behavior contract: identity, company context, task, tone, what to say, what not to say, and how to use tools. The video presents prompt work as permanently iterative, not a one-time setup step.

Files are attached as knowledge sources. For a CX demo, this means the FAQ/policy document should be a real source of truth rather than invented prompt text.

## Tools And Reuse

Tools are global account resources that can be assigned to one or more assistants. This matters for a multi-agent or multi-department demo:

- Create a tool once, such as appointment booking or account lookup.
- Assign it to the receptionist, support assistant, sales assistant, or other agents as needed.
- Remove access from assistants that should not be allowed to perform the action.

This matches the n8n MCP receptionist pattern: tool definitions should be reusable, narrow, and attached only where the assistant needs them.

## Analysis, Extraction, And Monitoring

The video says the older summary, success evaluation, and structured-data settings are deprecated, with new work moving toward:

- Structured outputs: post-call extraction from transcripts.
- Scorecards: quality/success evaluation.
- Monitors: operational alerting for failures and quality issues.

Structured outputs can use AI extraction or regex extraction. Regex is better for stable patterns such as order IDs, phone numbers, and confirmation codes. AI extraction is easier for fuzzy fields such as appointment intent or customer outcome, but it is not deterministic and needs testing.

For the demo, useful structured outputs are:

- `customer_intent`
- `resolution_status`
- `order_or_ticket_id`
- `appointment_time`
- `handoff_required`
- `call_outcome`
- `follow_up_action`

Monitors can watch for production issues such as transcriber request failures, attach severity, and notify through email, Slack, or webhook after thresholds are crossed.

## Advanced Production Controls

The advanced page contains the controls that make a voice agent feel production-grade:

- Fallbacks: backup transcriber and voice providers, preferably from different companies.
- Compliance: HIPAA and zero-data-retention settings, treated in the video as premium/special-case settings.
- Webhook server: the endpoint that receives call events and end-of-call reports; production can include API-key authentication.
- Start speaking plan: when the assistant begins talking after the user finishes.
- Stop speaking plan: when the assistant stops talking after the user interrupts.
- Voicemail detection: recommended as always-on for outbound or phone workflows.
- Call timeouts: silence timeout and maximum call duration to avoid wasting credits.
- Recording/artifacts: audio recording, call logs, transcripts, and storage format.
- Messaging: server messages, especially end-of-call report delivery.
- Idle messages: prompts sent when the user goes silent before the call ends.
- End call tool: the newer way to allow the assistant to hang up intentionally.

The start/stop speaking settings are especially important for perceived quality. More aggressive settings can make the agent snappier, but increase the risk of interrupting the caller. More conservative settings reduce interruption but make the agent feel slower.

## Implications For Seth's Demo

This video makes Vapi look stronger for a CLI/Codex-built demo where Vapi handles the hard voice infrastructure and the custom code handles business logic. The practical checklist is:

1. Pick transcriber, model, and voice deliberately because they drive latency, quality, and cost.
2. Add fallbacks before presenting anything as production-ready.
3. Keep tool logic narrow and reusable across assistants.
4. Use structured outputs and end-of-call reports to prove the agent solved a CX problem.
5. Configure turn-taking, silence timeout, max duration, idle messages, voicemail detection, and recording so the call feels like a real product rather than a toy demo.
6. Treat the dashboard as a map of required settings, but prefer managing the repeatable assistant definition from files/API when possible.

## Open Questions

- Which Vapi settings are fully manageable through API today, and which still require dashboard clicks?
- Can the demo export the assistant configuration into a repo so Codex can diff, revise, and redeploy it?
- What is the cheapest acceptable combination of transcriber, model, voice, and fallbacks for a believable customer-support call?
- Should the demo include monitors/scorecards, or is structured output plus call logging enough for the interview?
