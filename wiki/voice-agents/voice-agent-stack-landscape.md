---
type: wiki_article
title: Voice Agent Stack Landscape
updated_at: 2026-07-23
status: active
source_count: 12
tags:
  - voice-agents
  - speech-to-speech
  - vapi
  - elevenlabs
  - telephony
---

# Voice Agent Stack Landscape

> Sources: Seth's 2026-06-30 Last30Days sweep on open-source voice-agent repositories; Seth's personal-agent ops stack notes on voice providers and interactive voice surfaces; 2026-06-25 AI agent workflow link bundle routing note for voice AI; Vapi/n8n MCP receptionist YouTube transcript; Vapi agent-builder update YouTube transcript; Seth's Avoca-inspired Singapore voice AI CSR planning chat; Avoca inbound AI CSR page; OpenAI GPT-Live announcement; Voice AI Newsletter interview with Zach Koh of Fixie AI; Voice AI Newsletter AI live interpretation article; Voice As The Next Frontier compilation.
> Raw/Staging: [OpenAI GPT-Live announcement](../../raw/intentional/web/2026-07-08-openai-introducing-gpt-live.md); [Open-source voice agent repositories Last30Days digest](../../staging/last30days/2026-06-30-open-source-voice-agent-repositories-digest.md); [Open-source voice agent repositories raw sweep](../../raw/sweeps/last30days/open-source-voice-agent-repositories-raw.md); [Personal Agent Ops Stack](../personal-systems/personal-agent-ops-stack.md); [AI Agent Workflow Link Bundle](../archive/2026-06-25-ai-agent-workflow-link-bundle.md); [Vapi n8n MCP receptionist transcript](../../raw/intentional/youtube/2026-06-30-i-built-an-ai-voice-receptionist-with-vapi-and-n8n-mcp.md); [Vapi agent-builder update transcript](../../raw/intentional/youtube/2026-06-30-vapi-just-got-a-massive-update-complete-walkthrough.md); [Avoca-inspired Singapore voice AI CSR planning chat](../../raw/intentional/pasted/2026-06-30-avoca-inspired-singapore-voice-ai-csr-thesis-chat.md); [Avoca inbound AI CSR page](../../raw/intentional/web/2026-06-30-avoca-inbound-ai-csr-page.md); [superseded CryptoBriefing GPT-Bidi-1 watchlist report](../../raw/intentional/web/2026-07-03-openai-prepares-chatgpt-voice-upgrade-with-bidi-1-model.md); [Voice AI Newsletter Zach Koh transcript](../../raw/intentional/web/2026-07-03-speech-to-speech-ai-models-with-zach-koh-voice-ai-newsletter.md); [Voice AI Newsletter AI live interpretation article](../../raw/intentional/web/2026-07-03-ai-voice-translation-breaking-language-barriers-in-call-cent.md); [Voice As The Next Frontier](voice-as-next-frontier.md)

## Purpose

This is the router for voice-agent work: speech-to-speech demos, phone agents, telephony providers, STT/TTS/model choices, open-source frameworks, hosted developer platforms, and CX workflows that talk to business tools.

Keep voice agents separate from generic agent frameworks because the hard problems are different: turn-taking, barge-in, latency, telephony, audio quality, provider cost stacking, call state, recordings, transfers, and tool execution while a human is waiting on the line.

## Current Working Decision

For Seth's interview demo, the current default path is:

```text
Vapi-hosted phone agent
  + configurable LLM provider
  + configurable transcriber
  + ElevenLabs or Cartesia-style voice
  + one tiny tool endpoint for CRM/order lookup
```

This keeps voice and telephony infrastructure out of scope while preserving CLI/API configurability and model-provider optionality. The custom tool endpoint is still needed for business actions: order lookup, ticket creation, refund status, callback scheduling, or human transfer context.

The captured Vapi/n8n MCP receptionist demo validates the same pattern: Vapi owns the live voice call and reasoning, while the backend exposes narrow deterministic tools for CRM lookup, appointment booking, appointment changes, transfer, FAQ lookup, and call logging. See [Vapi n8n MCP Receptionist Demo](vapi-n8n-mcp-receptionist-demo.md).

The Vapi agent-builder update walkthrough adds the operational layer: choose STT/model/TTS deliberately, configure fallbacks, attach reusable tools, set structured outputs/scorecards/monitors, tune turn-taking, and send end-of-call reports to a webhook. See [Vapi Agent Builder Update Walkthrough](vapi-agent-builder-update-walkthrough.md).

The current product-thesis layer is [Singapore Voice AI CSR Thesis](singapore-voice-ai-csr-thesis.md): an Avoca-inspired, Singapore-adapted idea for a voice-first AI overflow receptionist where Vapi owns the live call, WhatsApp continues the conversation, and the custom product owns booking, escalation, CRM/calendar write-back, inbox state, and recovered-call analytics.

The broader market-thesis layer is [Voice As The Next Frontier](voice-as-next-frontier.md): voice is compelling where high-intent calls, existing phone workflows, frontier-model reasoning, and simulation/observability infrastructure meet. Use that page for argument curation, enterprise proof points, and reliability/eval framing.

A second stack path is emerging around speech-understanding models and real-time transport, not just hosted telephony orchestration. The Zach Koh/Fixie transcript argues for direct speech embeddings, audio as the source of truth, WebRTC transport, call-to-GPU affinity, cache reuse, and removing latency-adding proxies. That is not a replacement for Vapi-style hosted phone agents in the near term; it is the model/runtime layer to watch when the product needs open-source optionality, on-prem deployment, or voice experiences beyond phone support.

OpenAI's July 8 GPT-Live launch confirms the full-duplex model/runtime bucket. GPT-Live continuously listens and speaks while delegating deeper work to another frontier model, but it launched as a consumer ChatGPT Voice experience rather than an enterprise API. The stack question therefore splits: GPT-Live is the interaction roadmap, GPT-Realtime is the current developer layer, and OpenAI Presence is the managed production-agent product.

Live interpretation is a separate stack question from autonomous phone agents. The Krisp article frames AI Live Interpreter as a real-time, bi-directional translation layer for call centers that works with softphones and gives agents live transcription plus translated context. The stack risk is quality assurance: translation scores, ASR quality, accents, domain jargon, cultural nuance, privacy, and human escalation all need explicit evals before this can be sold as reliable multilingual support.

## Stack Buckets

| Bucket | Examples | Use When | Main Risk |
|---|---|---|---|
| Hosted developer orchestration | Vapi, Retell | You want CLI/API configuration, phone calls, tools, and zero voice infra | Platform markup and hosted-platform constraints |
| Voice-native agent platform | ElevenLabs Agents | Voice quality, multilingual voice, and polished agent monitoring matter most | Easier to drift into platform-specific workflow/UI patterns |
| Speech-understanding model/runtime | GPT-Live, GPT-Realtime, UltraVox/Fixie | You need direct audio understanding, WebRTC, low latency, full-duplex interaction, open-source/on-prem optionality, or non-phone voice collaboration | Availability boundaries, model maturity, devX, and infra ownership |
| Live interpretation layer | Krisp AI Live Interpreter, translation/ASR overlays | You need multilingual support across existing agents and softphones before fully autonomous multilingual agents | Translation quality, ASR input quality, accents, domain jargon, cultural nuance, and privacy |
| Own-the-stack SDK | Patter | You want open-source phone-agent ergonomics with Twilio/Telnyx/Plivo and Python/TypeScript | You run the server/tunnel/deploy path |
| Production OSS framework | LiveKit Agents | You need WebRTC/telephony production control and can operate infra | More setup and ops burden |
| Pipeline experimentation | Pipecat | You want modular STT/LLM/TTS experiments and transport flexibility | You own more integration and deployment glue |

## Open-Source Repo Signal

The 2026-06-30 Last30Days GitHub-only sweep suggests:

- Pipecat is the most starred targeted voice-agent framework in the checked set.
- LiveKit Agents is close behind and looks stronger as a production realtime voice/video/telephony foundation.
- Patter is much smaller and newer, but best shaped for the "give my AI agent a phone number" demo path.
- TEN Framework is popular and active, but broader than the immediate phone-CX demo need.
- HuggingFace `speech-to-speech` is relevant for local/open-model voice agents, not necessarily phone-agent orchestration.

Because that sweep only had GitHub coverage, treat it as repo-popularity signal rather than a complete market read.

## Demo Questions To Answer

- What is the cheapest acceptable model/transcriber/voice stack for a believable support call?
- Where does Vapi charge separately from LLM, transcriber, TTS, and phone minutes?
- Can Codex manage the full assistant definition from files and CLI commands, with minimal dashboard use?
- What tool interface should the demo expose first: order lookup, ticket creation, refund status, callback booking, or transfer summary?
- What exact demo scenario should show that the agent solved a CX problem rather than merely chatted?

## Compiled Demo Sources

- [Vapi n8n MCP Receptionist Demo](vapi-n8n-mcp-receptionist-demo.md) captures the reusable build structure from the YouTube transcript: Vapi as the hosted voice/reasoning layer, n8n MCP as deterministic backend tools, and a CX workflow that proves account lookup, appointment creation, rescheduling, FAQ answering, handoff, and call logging.
- [Vapi Agent Builder Update Walkthrough](vapi-agent-builder-update-walkthrough.md) captures the updated Vapi dashboard structure and the production controls that matter for a demo: transcriber/model/voice selection, fallbacks, logs, reusable tools, structured outputs, monitors, webhook reports, turn-taking, voicemail detection, timeouts, recordings, and idle/end-call behavior.
- [Singapore Voice AI CSR Thesis](singapore-voice-ai-csr-thesis.md) captures the founder-memo version of the Avoca-inspired Singapore product idea: voice-first missed-call recovery, WhatsApp follow-up, unified inbox, narrow booking workflows, deterministic tools, and ICP questions deferred until validation.
- [Voice As The Next Frontier](voice-as-next-frontier.md) captures the argument map for why voice is becoming a major AI interface: high-intent calls, stalled scripted phone systems, enterprise adoption proof, Vapi/Claude positioning, Coval-style simulation and observability, GPT-Live full duplex, speech-understanding model/runtime arguments, and voice-native testing/eval requirements.
- [GPT-Live And Full-Duplex Voice](../openai/gpt-live-full-duplex-voice.md) is the canonical current OpenAI page; the earlier GPT-Bidi-1 report is retained only as a superseded watchlist artifact.
- [OpenAI Presence](../openai/openai-presence.md) tracks OpenAI's managed production product for voice/chat customer and internal workflows.
- [Voice AI Newsletter Zach Koh transcript](../../raw/intentional/web/2026-07-03-speech-to-speech-ai-models-with-zach-koh-voice-ai-newsletter.md) is the strongest technical stack augment: direct speech embeddings, no transcript as source of truth, WebRTC, GPU/cache routing, open-source enterprise optionality, and future multi-person AI collaboration.
- [Voice AI Newsletter AI live interpretation article](../../raw/intentional/web/2026-07-03-ai-voice-translation-breaking-language-barriers-in-call-cent.md) adds the multilingual-support layer: real-time bi-directional translation, softphone compatibility, live transcript plus translation context for agents, BLEU-style translation metrics, and explicit limitations around accents, jargon, cultural nuance, and integration.
