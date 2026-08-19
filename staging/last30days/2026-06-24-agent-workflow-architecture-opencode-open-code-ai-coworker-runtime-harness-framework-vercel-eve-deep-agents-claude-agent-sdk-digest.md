# Last30Days Digest: agent-workflow-architecture-opencode-open-code-ai-coworker-runtime-harness-framework-vercel-eve-deep-agents-claude-agent-sdk-raw

> Raw: ../../raw/sweeps/last30days/agent-workflow-architecture-opencode-open-code-ai-coworker-runtime-harness-framework-vercel-eve-deep-agents-claude-agent-sdk-raw.md
> Window: 2026-05-25 to 2026-06-24
> Generated: 2026-06-24
> Status: staged
> Compile Recommendation: Do not compile yet. Use as recent-signal evidence for agent-runtime architecture questions; manually capture high-signal X posts or official sources before promoting claims into wiki.

## Strong Signals

- Recent X discussion keeps separating model, prompt, context, harness, tools/MCP, and evals. The practical warning is that weak agent outcomes are often harness/context/eval failures, not just model failures.
- A 2026-06-24 Open Mercato post claims its Agent Orchestrator can run agents via OpenCode in Docker, in-process on Vercel AI SDK, or connected through A2A providers. Treat this as a lead until the product docs or repo are captured.
- A multi-agent workflow post argues that adding more Claude/Codex sessions only adds concurrency; the real leverage is whether owner babysitting time drops through task packages, checkpoints, routing, and acceptance gates.
- A Conduit/Product Hunt reference frames MCP/tool access as a gateway problem: agents should discover the right tools on demand instead of loading a huge tool surface into every context.
- A Deep Agents/OpenRouter post points to model routing by throughput, latency, price, provider policy, and fallback as a production concern for harness design.

## Repeated Themes

- Harnesses are the product surface: context loading, tool permissions, memory, evals, and workflow boundaries matter more than a clever prompt.
- Multi-agent systems need explicit roles and handoffs, but role names alone are weak; the stronger pattern is chief-of-staff routing, producer execution, scout/research, reviewer/verifier, and optimizer loops.
- Tool gateways and MCP routers are emerging as a way to reduce context bloat, enforce auth boundaries, and select tools just-in-time.
- OpenCode is being discussed less as a generic coding app and more as an open harness/worker that other systems can orchestrate.
- Recent chatter remains noisy and X-heavy; primary docs and repo/job-post captures are needed before durable wiki claims.

## Candidate Wiki Updates

- `wiki/agent-frameworks/agent-framework-landscape.md`: add OpenCode as an open CLI harness/watch item after a full source capture.
- `wiki/ai-coding/agentic-engineering-practices.md`: add a note that "more agents" is not the same as lower owner supervision; useful multi-agent systems reduce routing/checkpoint/acceptance burden.
- `wiki/personal-systems/agent-platforms-and-work-surfaces.md`: add tool-gateway/MCP-router as an architecture pattern if corroborated by primary docs.

## Sources Worth Manual Capture

- https://x.com/tomik99/status/2069683762443505677 - Open Mercato Agent Orchestrator lead mentioning OpenCode in Docker, Vercel AI SDK, and A2A.
- https://x.com/vibeeeng/status/2069491772577738780 - harness/context/tool/eval distinction.
- https://x.com/runes_leo/status/2069642223193350170 - multi-agent workflow and owner-babysitting critique.
- https://x.com/vivilinsv/status/2069581337028350123 - Conduit/MCP gateway lead.
- https://x.com/masondrxy/status/2069620506181992565 - Deep Agents plus OpenRouter model-routing lead.

## Cautions

- The sweep used X only; no web evidence was available from the local Last30Days run.
- The strongest OpenCode/Open Mercato item is a single post, not a complete source capture.
- The Flint/OpenCode connection remains unverified in this sweep. Local Flint notes cover "agency via API" and autonomous page agents, but not OpenCode specifically.
- Do not treat likes/reposts as truth. Use this digest as a lead list and architectural mood board, not as durable evidence.
