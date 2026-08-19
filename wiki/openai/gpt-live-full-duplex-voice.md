---
type: wiki_article
title: GPT-Live And Full-Duplex Voice
updated_at: 2026-07-23
status: active
source_count: 9
tags:
  - openai
  - gpt-live
  - voice
  - full-duplex
  - realtime-api
  - customer-experience
---

# GPT-Live And Full-Duplex Voice

> Sources: OpenAI GPT-Live announcement, system card, ChatGPT release notes and Voice help, GPT-Realtime-2.1 documentation, and OpenAI voice-infrastructure material, checked 2026-07-23.
> Raw: [OpenAI GPT-Live announcement](../../raw/intentional/web/2026-07-08-openai-introducing-gpt-live.md)

## Correction To The Earlier Watchlist

The official release is **GPT-Live**, not the previously reported "GPT-Bidi-1." OpenAI announced **GPT-Live-1** and **GPT-Live-1 mini** on July 8, 2026. The prior Bidi item in this Second Brain was a third-party app-code signal and should now be treated as superseded by the official launch.

GPT-Live is also distinct from the developer-facing **GPT-Realtime** family. As of July 23, GPT-Live is a ChatGPT consumer voice model/experience; OpenAI says API access is coming "soon." Production developers currently use GPT-Realtime-2.1 and the Realtime API.

## What Full Duplex Means

OpenAI says GPT-Live continuously processes input while generating output. It can listen and speak at the same time and decide many times per second whether to speak, keep listening, pause, interrupt, or invoke a tool.

| Architecture | Mechanics | Main trade-off |
|---|---|---|
| Cascaded voice | Speech-to-text → language model → text-to-speech. | Modular, but slower and can lose tone, timing, and other audio information between stages. |
| Turn-based speech-to-speech | One model consumes and emits audio but waits for an end-of-turn signal. | Smoother than a cascade, but pauses/noise can trigger awkward interruptions. |
| GPT-Live full duplex | Continuous input processing during output generation. | Supports overlapping speech, active listening, better timing, and natural interruption behavior. |

OpenAI has disclosed the behavioral architecture, not enough low-level detail to assert a particular neural topology, codec, training objective, or fully end-to-end implementation.

## Two-Plane Architecture

GPT-Live separates:

1. **The conversational plane**, which maintains timing, rapport, listening, acknowledgements, interruptions, and status.
2. **The intelligence/action plane**, which can delegate search, reasoning, or agentic work to a frontier model while the conversation continues.

At launch, the delegated model is GPT-5.5. Instant and mini use GPT-5.5 Instant; Medium and High use GPT-5.5 Thinking at corresponding effort. This decoupling is strategically important: fast conversation does not need to wait silently for slower reasoning.

## Capabilities

- Natural interruption, overlap, thought pauses, backchannels, and "stay quiet and listen" behavior.
- Better handling of background noise and fewer premature end-of-turn decisions.
- Search, memory, text/image context, streamed text, and supported visual widgets.
- Live translation as an architectural capability, without a published GPT-Live language count or translation benchmark.
- Strong OpenAI-reported preference over Advanced Voice Mode for conversational flow, turn-taking, interruptions, naturalness, GPQA, BrowseComp, and an internal telecom voice task; numeric results were not published for the launch comparisons.

Full duplex removes the need to wait for a clean turn boundary. It does not remove inference, tool, transport, or audio-playback latency, and OpenAI published no GPT-Live response-time benchmark.

## Availability And Limits

As of 2026-07-23:

- GPT-Live-1 is rolling out to paid consumer users; GPT-Live-1 mini to Free.
- It is available on chatgpt.com, iOS, and Android in supported regions.
- It was **not available in ChatGPT Business, Enterprise, or Edu workspaces at launch**.
- It was **not yet available through the API**.
- Video and screen sharing were not supported at launch.
- Connected apps/plugins were initially unsupported in Live.
- Some languages may have non-native accents or fluency gaps.
- Plan-dependent limits apply; individual Live sessions can run for up to two hours according to the Voice help page.

The narrower Help Center availability should override the temptation to interpret "global rollout" as enterprise or API availability.

## Safety

GPT-Live adds voice-native evaluations and live checks over inputs and generated outputs. The system can steer or interrupt a response, play a spoken safety message, show written resources, or end a high-risk conversation. OpenAI also describes teen protections, parental controls, emotional-reliance monitoring, self-harm support flows, predefined voices, and anti-impersonation safeguards.

OpenAI reported safety performance equal to or better than Advanced Voice Mode across most evaluated areas, with small non-statistically-significant regressions disclosed for emotional reliance and sexual content in specific comparisons.

## Enterprise And CX Significance

GPT-Live is an enabling interaction model, not a complete enterprise CX platform. Production deployments still need telephony, identity, CRM/policy integration, permissions, audit, evaluation, monitoring, escalation, and human handoff.

That creates a clean product relationship:

- **GPT-Live** demonstrates the future human interaction primitive.
- **Realtime API / GPT-Realtime** is the current builder layer.
- **OpenAI Presence** packages the production-agent operating system and deployment motion.

Sierra, Wonderful, Intercom, and Parloa compete more directly with Presence at the application/deployment layer. GPT-Live can still be strategically important because better continuous interaction can improve whichever platform gains access to it.

## Interview Talk Track

> GPT-Live changes the interaction model from turn-taking to continuous conversation. The deeper architectural point is that OpenAI decoupled the low-latency conversational loop from slower reasoning and agent work, so the assistant can keep listening and talking while another model searches or reasons in the background. That is highly relevant to customer service, but the enterprise product is Presence; GPT-Live itself was a consumer launch and was not yet in the API or business workspaces at launch.

## See Also

- [OpenAI Presence](openai-presence.md)
- [Enterprise Agent Competitive Landscape](enterprise-agent-competitive-landscape.md)
- [Voice As The Next Frontier](../voice-agents/voice-as-next-frontier.md)
- [Voice Agent Stack Landscape](../voice-agents/voice-agent-stack-landscape.md)

