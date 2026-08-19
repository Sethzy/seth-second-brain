# Last30Days Digest: open-source-voice-agent-repositories-raw

> Raw: ../../raw/sweeps/last30days/open-source-voice-agent-repositories-raw.md
> Window: 2026-05-31 to 2026-06-30
> Generated: 2026-06-30
> Status: staged
> Compile Recommendation: Keep staged unless a broader voice-agent landscape page is created.

## Strong Signals

- Pipecat is the most starred targeted voice-agent framework in the checked set: 13,097 stars, BSD-2-Clause, latest release v1.4.0 on 2026-06-17.
- LiveKit Agents is close behind on popularity: 11,178 stars, Apache-2.0, latest release livekit-agents@1.6.4 on 2026-06-24, and strongest positioning for production realtime voice/video/telephony agents.
- TEN Framework has comparable stars at 10,810 and recent release activity, but is broader/more framework-heavy and less clearly the default choice for a phone CX demo.
- Patter is much smaller at 902 stars but highly relevant to Seth's demo because it is phone-agent-specific, MIT, Python/TypeScript, and supports Twilio/Telnyx/Plivo directly.

## Repeated Themes

- Popularity and build-fit diverge: Pipecat wins raw GitHub stars, while LiveKit Agents looks stronger as a production foundation.
- Phone-agent demos need telephony, interruption handling, tool calls, and observability, not only speech-to-speech models.
- Newer purpose-built SDKs like Patter trade ecosystem size for demo velocity and direct phone-number ergonomics.

## Candidate Wiki Updates

- Potential new page: `wiki/ai-coding/voice-agent-stack-landscape.md` or `wiki/ai-knowledge-work/voice-agent-stack-landscape.md`.
- If compiled, cite this Last30Days sweep alongside direct GitHub API snapshots and Patter local repo index.

## Sources Worth Manual Capture

- GitHub repo pages for `pipecat-ai/pipecat`, `livekit/agents`, `TEN-framework/ten-framework`, `PatterAI/Patter`, and `huggingface/speech-to-speech`.
- Official docs for LiveKit Agents and Pipecat if implementation begins.

## Cautions

- The sweep only had GitHub coverage; X/Twitter and web sources were unavailable in this run.
- Last30Days ranked TEN highest due to local fallback scoring and issue/comment counts. For the user-facing recommendation, prefer transparent metrics: stars, recent commit/release activity, telephony fit, and demo velocity.
