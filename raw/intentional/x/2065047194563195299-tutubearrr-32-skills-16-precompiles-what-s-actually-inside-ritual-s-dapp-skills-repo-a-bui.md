---
type: raw_capture
source_type: x
url: https://x.com/tutubearrr/status/2065047194563195299
original_url: https://x.com/tutubearrr/status/2065047194563195299
author: "tutubear (\u2756,\u2756)"
handle: tutubearrr
status_id: 2065047194563195299
captured_at: 2026-06-19T23:58:19+08:00
published_at: "Thu Jun 11 12:23:12 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 46
  reposts: 3
  likes: 94
---

# X post by @tutubearrr

## Source

- Original: [https://x.com/tutubearrr/status/2065047194563195299](https://x.com/tutubearrr/status/2065047194563195299)
- Canonical: [https://x.com/tutubearrr/status/2065047194563195299](https://x.com/tutubearrr/status/2065047194563195299)
- Author: tutubear (❖,❖) (@tutubearrr)

## Verbatim Text

32 Skills, 16 Precompiles: What's Actually Inside Ritual's dApp Skills Repo

> A builder's guide to everything Ritual gives you for free

I spent an afternoon reading through every skill in Ritual's dApp skills repository. 32 skills. 16 precompile ABIs. 2 agents. 10 behavioral protocols. And I realized something: most builders on Ritual are using maybe 10% of what's available. Not because the other 90% is useless, because nobody told them it existed. This is my attempt to fix that. If you've been building on Ritual, or thinking about building on Ritual, here's what's actually inside the toolbox.

---

## The Meta Layer: How The System Thinks

Before you write a single line of code, Ritual loads something most people don't even know exists: 10 behavioral rules that run as invisible middleware during every build session. These aren't suggestions. They're enforced protocols. Track cost, your turn budget governs every decision. Distrust priors, Ritual violates Ethereum assumptions. Don't assume Infernet exists. Don't assume standard patterns work. Search before asking, exhaust a 5-step resolution hierarchy before you ask a human. Circuit breaker, detect trajectory divergence and stop before wasting budget. The meta layer isn't documentation. It's how the system prevents you from building the wrong thing. Most frameworks give you tools and wish you luck. Ritual gives you guardrails.

---

## The Build Skills: What You Can Actually Build

This is the meat. Every precompile has a corresponding skill with complete encoding examples, Solidity patterns, and viem integration. HTTP Call (0x0801) makes external API requests on-chain. Not through an oracle. Not through a relay. The precompile itself handles HTTP, including headers, methods, and response parsing. The skill teaches you the 13-field encoding format, executor, encrypted secrets, TTL, URL, method, headers, body, and shows you exactly how to decode the response. LLM Inference (0x0802) is what powers Ritual Oracle. But the skill goes way beyond what I implemented. It covers conversation history encoding, model selection via the ModelPricingRegistry, temperature tuning, and streaming responses. If you're building anything that needs on-chain AI inference, the LLM skill is 20 pages of battle-tested patterns. ONNX ML Inference (0x0800) is synchronous, unlike the async precompiles, this one returns results in the same transaction. The skill shows you how to encode model inputs, handle tensor shapes, and decode outputs. If you want to run a fraud detection model on-chain, this is how. Long HTTP (0x0805) handles requests that take longer than a single block. Poll/deliver pattern. The skill covers job submission, status polling, and result delivery, including error recovery when executors timeout.

---

## Agent Precompiles: The Autonomous Layer

Sovereign Agent (0x080C) and Persistent Agent (0x0820) are where things get interesting. I wrote about these in Day 2, but the skills repo goes deeper. Sovereign Agent creates ephemeral agents, deploy, execute task, terminate. The factory contract at 0x9dC4 handles deployment. The skill shows you the complete lifecycle: deploy, fund, call, receive callback, settle. Persistent Agent creates agents that live forever. They have identity, memory, and state that persists across transactions. The factory at 0xD4AA deploys them. The skill covers how to encode initial prompts, how callbacks work, how to query an agent's memory. What surprised me is how practical these are. Sovereign Agent isn't a concept. It's a precompile you can call from a Solidity contract. Persistent Agent isn't a whitepaper idea. It's deployed on testnet and ready to use.

---

## The Auth Layer: Identity Without EOA

Ed25519 Verification (0x0009) verifies cryptographic signatures on-chain. Not Ethereum's secp256k1, Ed25519, the curve used by modern systems. The skill covers verification patterns, signature encoding, and how to integrate with off-chain identity systems. SECP256R1 (0x0100) enables passkey authentication. WebAuthn, FIDO2, biometric auth, all verifiable on-chain. If you want your dApp to support "sign in with fingerprint" instead of "sign in with MetaMask," this precompile makes it possible. TxPasskey (0x77) is a custom transaction type that combines authentication with execution. One transaction, one signature, identity verified and action executed atomically. The auth skills aren't just reference documentation. They show you how to build authentication flows that don't rely on private keys stored in browser extensions.

---

## The Operations Layer: Production Infrastructure

Secrets Management uses ECIES encryption to protect sensitive data on-chain. The skill covers key generation, encryption patterns, and PII redaction, making sure your agent doesn't accidentally leak personal information in transaction data. The Scheduler precompile enables time-based execution. No more cron jobs on a VPS. No more "trust me, this server will stay running." Your agent's scheduled tasks live on-chain, executed by the network. The skill shows you how to define predicates, set intervals, and handle execution failures.

---

## The Debug Layer: When Things Break

Ritual's debugger agent runs a sequential pipeline when things go wrong. Triage first, what's the symptom? Then smoke tests, does basic functionality work? Then quick-match against 10 known root causes, executor not found, insufficient balance, TTL expired, callback not firing. If none of those match, systematic diagnosis kicks in. The debug skills cover every error code in the system. "No services found for capability", check TEEServiceRegistry. "Precompile call failed", input encoding mismatch. "Job expired", increase TTL. "Unauthorized delivery", callback address wrong. I've hit half of these building Oracle. Having a reference that maps error → cause → fix saves hours.

---

## What Most Builders Miss

The skill system isn't just documentation. It's executable knowledge. Each skill has trigger conditions, when should you load this? Numbered steps with exact commands, not "figure it out yourself." A pitfalls section, what goes wrong and how to avoid it. Verification steps, how to confirm you did it right. When you load a skill with skill_view, you're not reading a blog post. You're following a procedure that's been validated against the actual precompile behavior on Ritual Chain. That's the difference between "I read the docs" and "I know this works."

---

## The Missing Piece: Multimodal

Image (0x0818), Audio (0x0819), and Video (0x0817) precompiles exist. The skills are written. But the executor availability on testnet is limited. This is the frontier, the part of the toolbox that's ready but waiting for the network to catch up. When multimodal executors go live, builders who already understand the patterns from the skills will be months ahead.

---

## Why This Matters

Most chains ship infrastructure and say "figure it out." Ritual ships infrastructure AND the knowledge to use it. 32 skills covering every aspect of building, from first deployment to production debugging. 16 precompile ABIs with encoding examples you can copy-paste. A testing pyramid that covers Foundry fuzz tests, Vitest unit tests, and Playwright E2E. A debugging pipeline that matches errors to solutions. If you're evaluating which chain to build on, the skills repo isn't just a nice-to-have. It's the difference between spending weeks figuring out undocumented behavior and spending hours following validated procedures.

---

## The Bigger Picture

[Embedded Tweet: https://x.com/i/status/2047781690752332148]

Read the skills repo end-to-end and you'll understand something about Ritual's vision that isn't obvious from the marketing. This isn't a chain that happens to support AI. This is a chain designed for autonomous economic agents. Every precompile, every skill, every behavioral protocol is oriented toward one goal: making agents work. Payments work. Identity works. Privacy works. Compute works. And the research pipeline keeps making it better. For builders, that means the tools you need are being actively developed. You're not building on a chain that might support your use case. You're building on a chain that was designed for exactly what you're building.

Building in public on @ritualnet

## X Article Metadata

- Title: 32 Skills, 16 Precompiles: What's Actually Inside Ritual's dApp Skills Repo
- Preview: A builder's guide to everything Ritual gives you for free
I spent an afternoon reading through every skill in Ritual's dApp skills repository. 32 skills. 16 precompile ABIs. 2 agents. 10 behavioral

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
