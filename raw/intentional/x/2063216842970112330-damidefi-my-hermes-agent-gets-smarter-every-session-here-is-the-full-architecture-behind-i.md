---
type: raw_capture
source_type: x
url: https://x.com/DamiDefi/status/2063216842970112330
original_url: https://x.com/DamiDefi/status/2063216842970112330
author: "Dami-Defi"
handle: DamiDefi
status_id: 2063216842970112330
captured_at: 2026-06-19T23:40:56+08:00
published_at: "Sat Jun 06 11:10:02 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 17
  reposts: 36
  likes: 292
---

# X post by @DamiDefi

## Source

- Original: [https://x.com/DamiDefi/status/2063216842970112330](https://x.com/DamiDefi/status/2063216842970112330)
- Canonical: [https://x.com/DamiDefi/status/2063216842970112330](https://x.com/DamiDefi/status/2063216842970112330)
- Author: Dami-Defi (@DamiDefi)

## Verbatim Text

My Hermes Agent Gets Smarter Every Session. Here Is the Full Architecture Behind It.

Three weeks after setting up my Hermes programmer agent, it solved a problem in 22 seconds that had taken me 20 minutes the first time I encountered it.

Not because the model got better. Because the agent had written a skill file the first time it solved the problem, stored the working approach in plain markdown, and retrieved it automatically when the same pattern appeared again. The fix was already there. The agent did not rediscover it. It remembered.

That is the compounding Hermes is built around. And it is architecturally different from anything else running in the open-source agent space right now.

Most AI agents are smart. None of the others are learning. Hermes is the only open-source agent that combines runtime skill creation, persistent multi-layer memory, and an offline skill optimization pipeline in a single framework. Not even OpenClaw does all three. That combination is why the agent you are running in month three is genuinely more capable than the one you installed on day one, without you changing a single line of configuration.

This article is the full architecture. What each layer does, why it matters, and how to build a three-agent setup that runs 24/7.

## The Problem Every Other Agent Has

Every AI agent session has the same failure mode at the end of it.

You close the chat. Everything the agent figured out disappears. The fix it spent ten minutes working through. The project convention you corrected it on twice. The exact sequence of steps that finally worked. Gone. Next session, you re-explain everything from scratch.

This is not a model intelligence problem. It is an architecture problem. The agent has no mechanism for writing down what it learned and reading it back later.

Hermes solves this with three distinct compounding mechanisms that work at different speeds.

## The Three Layers That Make Hermes Compound

Layer 1: Runtime skill creation. When the agent solves a complex problem, it writes a skill file documenting the successful approach. Next time it encounters a similar problem, it loads the skill and follows the proven path instead of rediscovering it. The longer you run the agent, the richer the skill library becomes.

Layer 2: Persistent multi-tier memory. Three memory tiers operating at different speeds: a fast in-context layer for critical facts, a searchable SQLite database for full session history, and optional external providers for deeper persistence. Each tier has a specific job. None of them reset when you close the session.

Layer 3: GEPA. An offline skill optimization pipeline that reads your agent's execution traces, identifies where skills are failing, and proposes improvements through evolutionary search. No GPU required. No fine-tuning. Around $2 to $10 per optimization run. This is the layer most people skip and the one that produces the biggest quality jump.

The first layer is active every session. The second builds over weeks. The third is something you run when you want to push the capability ceiling without touching model weights.

No other open-source agent ships all three. That is the architectural claim worth understanding before you install anything.

Two more architectural details worth knowing before you build.

Every task has a hard cap of 90 turns. Subagents share the same budget. This exists because a stuck agent retrying a failing API call would otherwise silently drain API credits without limit. If you hit this limit mid-task, the fix is to break the task into smaller scoped units rather than fighting the cap. It is not a bug. It is the guardrail that makes autonomous agents safe to run overnight.

The agent also runs in six different execution environments: local terminal, Docker, SSH, Modal, Daytona, or Singularity. The code is identical across all six. The only change is a single config value. If you want to move execution from your laptop to a remote server or a cloud GPU, you change one line in config.yaml and nothing else breaks.

## Before Memory: Who Is the Agent?

The memory and skills layer handles what the agent knows and how it does things. But neither tells you who it is.

Without an identity layer, every agent feels generic. The same analytical tone, the same hedging patterns, the same tendency to over-explain simple things. SOUL.md is what changes this.

The file lives at ~/.hermes/SOUL.md and loads as slot one in the system prompt, before memory, before skills, before anything else. It defines personality, communication style, hard limits, and the lens through which everything the agent knows gets filtered.

It is hand-authored and static. You write it once and it stays consistent across every project and every session.

SOUL.md Template

> # SoulYou are [role]. [One sentence on core operating principle].[How you communicate: terse or detailed, direct or exploratory, opinion-heavy or neutral].[What you always do before acting].[What you never do under any circumstances].[Your relationship to being wrong: do you flag uncertainty, push back, or just deliver?]

The specificity of this file determines the gap between an agent that feels like a generic assistant and one that feels like a specialist with a point of view. Vague SOUL.md files produce vague agents. Specific ones produce agents with consistent character across every session.

## The Three-Tier Memory System

Hermes does not have a single memory. It has three layers designed for different jobs.

Tier 1: Two markdown files on disk.

MEMORY.md (2,200 character cap) holds what the agent needs to know about your environment: project conventions, tool quirks, lessons from past sessions, things to avoid. USER.md (1,375 character cap) holds your profile: name, communication preferences, skill level, how you like information delivered.

Both inject into the system prompt as a frozen snapshot at session start. When memory approaches 80% capacity, the agent consolidates automatically, merging related entries into denser versions so only genuinely useful information survives. Low-value captures get pruned. High-signal information stays.

Tier 2: Full-text session search.

Every conversation is stored in SQLite with FTS5 full-text search. The agent can search across weeks of past sessions on demand. When you ask what it was working on last Thursday, it is searching real session data, not fabricating a plausible answer.

The tradeoff is deliberate: Tier 1 is always in context but tiny. Tier 2 has effectively unlimited depth but requires an active search and a summarisation step. Critical facts live in Tier 1. Everything else is searchable when it becomes relevant.

Tier 3: External memory providers.

Eight pluggable providers that extend persistence beyond the built-in system. Only one can be active at a time. When an external provider is active, Hermes prefetches relevant memories before each turn, syncs conversation turns after each response, and extracts memories on session end. All of this happens automatically without you configuring individual retrieval calls.

## Self-Evolving Skills: The Agent Writes Its Own Playbooks

Memory handles facts. Skills handle procedures.

A skill is a markdown file that packages a proven approach to a specific class of problem. When the agent successfully navigates something non-trivial, it creates a skill file documenting what worked. The next time the same pattern appears, it loads the skill and follows the proven path instead of working it out from first principles again.

The file structure is minimal on purpose:

SKILL.md Format

> --- name: [skill-name] description: [one to two sentences describing when to activate this skill] version: 1.0.0 author: agent ---## Procedure [numbered steps of the successful approach]## Pitfalls [what goes wrong if you skip steps or make specific mistakes]## Verification [how to confirm the approach worked]

Skill creation triggers automatically when the agent completes a task requiring five or more tool calls, when it hits errors and finds the working path through them, when you correct its approach, or when it discovers a workflow that is non-obvious enough to be worth capturing.

This is the mechanism behind the 22-second solve I described at the start. The first time the agent encountered that problem, it worked through it using trial and error. It saved the successful path as a skill. The second time, it loaded the skill and followed the path directly.

Progressive disclosure keeps token costs from spiralling.

The agent sees only skill names and descriptions by default, roughly 3,000 tokens for the full catalog. It loads a skill's full content only when it actually needs one. It can drill into specific reference files within a skill when it needs deeper context. The catalog stays searchable without loading everything into context on every turn.

## The Curator: Garbage Collection for Skills

Without maintenance, skills pile up. Narrow, overlapping playbooks accumulate until the catalog becomes noise rather than signal. The Curator handles this automatically.

It does not run on a fixed schedule. It triggers on an inactivity check: if seven days have passed since its last run and the agent has been idle for two or more hours, a background fork of the agent spins up and runs the review without touching your active session.

The Curator operates in two phases. First, automatic transitions that require no model calls: skills unused for 30 days become stale, skills unused for 90 days get archived. Second, an LLM review across all agent-authored skills where the forked agent decides per-skill whether to keep, patch, consolidate, or archive. Up to eight review iterations per run.

Two constraints that matter: the Curator never touches bundled or hub-installed skills, only the ones your agent created. And it never auto-deletes. The worst outcome is archival to ~/.hermes/skills/.archive/ which is recoverable with one command.

Before every Curator pass, Hermes snapshots the entire skills directory to a tar.gz archive. Rollback is one command. Rollbacks are themselves reversible.

If there are skills you need to protect from archival, pin them:

Setup

> hermes curator pin [skill-name]

Pinned skills can still be patched and improved. The pin only prevents archival and deletion.

## The Skills Hub: 687 Skills You Can Install Today

One of the most immediately useful things most new Hermes users miss is that they do not have to wait for the agent to build its own skills from experience.

Hermes maintains an official Skills Hub with 687 pre-built skills across 18 categories. 87 ship bundled with the agent on install. 79 optional skills are available on demand. 16 come directly from Anthropic, including frontend-design, pdf, pptx, docx, and mcp-builder. 505 come from LobeHub, the broader community contribution layer.

On day one, before the agent has solved a single problem for you, you can install production-grade skill libraries that encode workflows it would otherwise take weeks of usage to develop.

Setup

> hermes skills list — browse the full catalog hermes skills install [skill-name] — install a specific skill hermes skills tap add yourname/your-skills-repo — add any GitHub repo as a custom source hermes skills install yourname/your-skills-repo/[skill-name] — install from your custom tap

The tap system is how you share skills across a team or maintain a private collection that is not in the public hub. Build a skill once. Install it across every agent profile in one command.

## GEPA: The Layer Most People Skip

GEPA stands for Genetic-Pareto Prompt Evolution. It is not part of the Hermes runtime. It lives in a companion repository and operates as an offline optimization pipeline. Published as an ICLR 2026 Oral paper. MIT licensed.

The problem it solves: the runtime learning loop has a known weakness. The agent is a biased evaluator of its own performance. It tends toward self-congratulation, rating its outputs as successful even when they are not. Community usage has confirmed this. The same system that creates skills can overwrite good manual customisations with worse versions of them.

GEPA bypasses the self-evaluation problem by reading execution traces rather than asking the agent how it thinks it performed. It identifies where approaches actually failed, generates candidate improvements through evolutionary search, and evaluates those candidates using LLM-as-judge scoring with rubrics rather than binary pass/fail.

The process:

1. Read the current skill from the Hermes repository

2. Generate an evaluation dataset from synthetic test cases, real session history from SQLite, or hand-curated golden examples

3. Run the optimizer: read execution traces, identify failure points, generate candidate skill variants

4. Score candidates against rubrics

5. Apply constraint gates: full test suite must pass at 100%, skill files must stay under 15KB, semantic purpose must not drift

6. The best variant goes out as a pull request against the Hermes repository. Never a direct commit.

Cost: $2 to $10 per optimization run. No GPU required. Everything runs through API calls.

This is where to go before fine-tuning. Most teams reach a performance ceiling with their agent skills and immediately think about RL or GRPO. GEPA is the step that should come first. It improves skill quality through prompt-space search rather than weight-space search. For the cases where the bottleneck is skill design rather than model capability, it produces significant gains at a fraction of the cost.

## The Three-Agent Setup

One agent is useful. Three specialised agents with isolated memory and SOUL.md files is where the architecture gets genuinely interesting.

Hermes calls these profiles. Each profile is a fully isolated instance with its own config, memory, skills, sessions, and identity. They share nothing by default.

Creating the three profiles:

Setup

> hermes profile create programmer --clone hermes profile create researcher --clone hermes profile create designer --clone

The --clone flag copies your default profile's config and environment as a starting point.

Give each profile its own Telegram bot. Telegram only allows one connection per token. Run /newbot in BotFather three times, save the three tokens, then run the gateway setup once per profile:

Setup

> hermes -p programmer gateway setup hermes -p researcher gateway setup hermes -p designer gateway setup

The Programmer Agent

This agent is most useful when it delegates code execution to Claude Code rather than writing code directly in the Hermes terminal. Hermes orchestrates: it reads the problem, plans the approach, calls Claude Code for file edits and command execution, reads the result, and decides what happens next. Claude Code does the actual work inside your real codebase.

If you run a Claude Max subscription, this costs nothing extra. Claude Code uses Max credentials automatically.

SOUL.md for the Programmer

> # SoulYou are my staff engineer. Terse, direct, and pragmatic.You read the existing code before you write new code. You write the smallest change that solves the problem. You prefer standard library over dependencies, boring tech over shiny tech, explicit over clever.Before declaring done: check whether the solution already existed in the codebase. Check whether tests exist. Check what breaks if this fails. Run the tests.

Activate Claude Code delegation in a session with one prompt:

Prompt

> I have a Claude Max subscription. You are my staff engineer for day-to-day coding tasks. Under the hood, use Claude Code for all executions: file reads, writes, tests, git, commands. Set yourself up accordingly and confirm when ready.

The programmer installs the claude-code delegation skill automatically, verifies claude is on PATH, and begins routing all code execution through it from the next message.

The Researcher Agent

This agent runs a daily digest on a schedule. No manual triggering. Every morning it delivers a structured brief to Telegram.

SOUL.md for the Researcher

> # SoulYou are my deep researcher for AI, machine learning, and crypto markets. Your primary job is a daily Telegram digest of what changed since yesterday.Cover four streams: trending GitHub repositories, lab and big tech announcements, fresh research papers worth reading, and the social pulse on X and Hacker News.Lead with what is new, not what is generally true. Cite every claim with a URL. Flag when signal is thin. Use delegate_task aggressively to parallelise across streams. Never state a contested claim as settled. Never fabricate a citation.

Set up the daily cron job inside a researcher session:

Cron Instruction

> Every weekday at 7am, prepare a deep digest of what is new in AI and crypto from the last 24 hours.Cover in order: 1. Trending GitHub repositories with meaningful AI or crypto applications 2. Lab and big tech announcements from Anthropic, OpenAI, Google, Meta, Nous, and others 3. Research papers published or newly discussed in the last 24 hours 4. Social signals from X and Hacker News: what builders are reacting toLead with what changed. Cite every claim. Stay under 600 words. Deliver to Telegram. Set this up as a recurring cron job starting tomorrow.

Chaining cron jobs for multi-stage pipelines

Cron jobs can feed each other using the context_from flag. One job's output becomes the next job's input. This turns cron from a scheduling tool into an automated pipeline.

A practical example: a research collection job runs at 6am, gathering raw material across four data streams. A synthesis job runs at 6:30am, taking the raw collection as input and producing the polished digest. The collection job does the breadth work. The synthesis job does the depth work. Neither has to do both.

Setup

> In the researcher profile, after setting up the collection cron: /cron add "6:30am weekdays" "Synthesise the research collection from the 6am run into a 600-word digest. Deliver to Telegram." --context_from [collection_job_id]

The synthesis job receives everything the collection job produced. The pipeline runs autonomously from collection through delivery every weekday morning without any manual steps.

The Designer Agent

The designer becomes genuinely useful when it can generate visuals in your specific style rather than generic AI output. The mechanism: feed it reference designs, ask it to study them, and have it write a skill file that encodes the style pattern. The agent builds its own style fingerprint and embeds it into every future generation.

SOUL.md for the Designer

> # SoulYou are my visual designer. You create diagrams and illustrations that explain technical concepts clearly. Think clear line work and labelled structure, not polished marketing graphics.Every visual should make a complex idea click in one glance. You lead with the concept, choose the visual metaphor that serves it, then commit. Be direct about when a visual would hurt more than help.

To teach it your visual style, paste reference images and send this prompt:

Prompt

> Study these reference illustrations carefully. Note the colour palette, line weight, level of detail, composition structure, and recurring visual motifs.Create a skill called "my-design-style" that: 1. Documents the style fingerprint in plain language 2. Includes a Python script that takes a text description and generates a new image in this exact style using the Gemini image generation API via OpenRouter 3. Reads OPENROUTER_API_KEY from the environmentUse skill_manage to create it. Test the script on a sample prompt before confirming it is done.

The designer writes the skill, generates the Python script, saves it to the designer profile's skills directory, and verifies it runs. From that point, every image generation request loads the style skill automatically.

## The Slash Commands That Change Daily Operation

Most documentation covers what Hermes can do. Few sources cover how to operate it effectively once it is running. Three slash commands make the biggest practical difference.

/background runs a task in an isolated background session without interrupting your current conversation. You are mid-conversation with the programmer agent and you want the researcher agent to pull a paper while you keep talking. Send the background command to the researcher profile, your current session continues uninterrupted, and the result comes back when it is ready. Multiple threads run simultaneously without colliding.

Setup

> /background [task description] — runs the task in isolation, never interrupts the active conversation

/goal sets a persistent north star for the session. Every response the agent gives is evaluated against it. Every tool call is checked against it before execution. Without /goal, a long session can drift. With it, the agent returns to the stated objective after every response and flags when something is pulling it off track.

Setup

> /goal [what you want to accomplish in this session] — agent measures every action against this

/steer redirects the agent mid-task without stopping its current execution. If the programmer is in the middle of a refactor and you want to add a constraint without interrupting the flow, /steer injects the new direction without forcing a restart. The agent incorporates it on the next loop.

Setup

> /steer [new direction or constraint] — redirects without interrupting current execution

## The Full File System

After install, everything lives in ~/.hermes/. The layout is worth understanding because every interaction touches one of these paths.

Setup

> ~/.hermes/ ├── config.yaml — model, tools, MCP servers, all non-secret config ├── .env — API keys and secrets ├── SOUL.md — identity layer, slot 1 in system prompt ├── memories/ │ ├── MEMORY.md — persistent agent facts (2,200 char cap) │ └── USER.md — your profile (1,375 char cap) ├── skills/ — all skills: bundled, hub-installed, agent-created ├── sessions/ — per-platform session metadata ├── state.db — SQLite with FTS5, full session history ├── cron/ │ ├── jobs.json — scheduled jobs │ └── output/ — cron run outputs └── logs/ — agent.log, gateway.log, errors.log

The three files that matter most: SOUL.md because it governs every output regardless of what the agent knows. state.db because it is what makes past session search actually work. skills/ because it is where the entire compounding mechanism lives.

## How to Install

Linux, macOS, or WSL2. Python 3.11 or higher. 8GB RAM is sufficient for API-based usage.

Setup

> curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash source ~/.bashrc

Run the setup wizard. It walks through provider, API key, model, and tool configuration:

Setup

> hermes setup

Start in terminal:

Setup

> hermes

Connect Telegram: get a bot token from @BotFather with /newbot, get your user ID from @userinfobot, then add both to config.yaml. The agent is immediately available from your phone.

Model switching and cost management

Hermes routes any model provider through a single translation layer. Switching from Claude to GPT to Gemini to a local Ollama model is one command and nothing else changes.

Setup

> hermes model — lists all available models and current active model hermes -p researcher model set gemini-flash — switches the researcher profile to Gemini Flash hermes -p programmer model set claude-opus-4-7 — keeps the programmer on Opus

For three agents running 24/7, this matters for cost. The researcher running a daily digest on Gemini Flash costs a fraction of running it on Opus. The programmer handling complex multi-file refactors earns the Opus cost. The designer making image generation calls routes through OpenRouter for the multimodal models. Route each agent to the cheapest model that produces acceptable output for its specific job. The translation layer means you never have to rewrite prompts when you switch.

## What Compounds and When

The first week the skill library is thin. The agent creates its first files but there is not enough history for the patterns to feel significant.

By week three, something shifts. The skills the agent created in week one are already informing week three sessions. The researcher's digest is drawing on three weeks of saved session context. The programmer is hitting cached solutions rather than rediscovering approaches.

By month two, the capability gap between this agent and a fresh Claude session is visible and measurable. Not because the model changed. Because the memory is real, the skills are earned, and the curator has already pruned the playbooks that did not hold up.

That is what compounding in an AI agent actually looks like. Not a capability that appears on launch. A capability that builds quietly over the first sixty days and then does not stop building.

Most people close their agent sessions and lose everything they just built. This architecture is designed so that every session adds to the next one.

The agents that are worth running are the ones that get smarter when you do.

Follow @damidefi on X for daily Claude AI tools, crypto analysis, and the full journey to 100K. Bookmark this. Share it with one person still running AI agents that forget everything the moment the session closes.

## X Article Metadata

- Title: My Hermes Agent Gets Smarter Every Session. Here Is the Full Architecture Behind It.
- Preview: Three weeks after setting up my Hermes programmer agent, it solved a problem in 22 seconds that had taken me 20 minutes the first time I encountered it.
Not because the model got better. Because the

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
