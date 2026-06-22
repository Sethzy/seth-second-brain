---
type: raw_capture
source_type: x
title: "Sunder sync: 66-twitter-jumperz-discord-swarm-FULL.md"
url: "https://x.com/jumperz/status/2020305891430428767"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/66-twitter-jumperz-discord-swarm-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/66-twitter-jumperz-discord-swarm-FULL.md"
sha256: "e8eb74ca5c7e2ef4c4a7bea69ee8a2f2d52e38fb8dfd3098f9235be08d1c4dc3"
duplicate_of: ""
---

# Sunder sync: 66-twitter-jumperz-discord-swarm-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/66-twitter-jumperz-discord-swarm-FULL.md`

Primary URL: https://x.com/jumperz/status/2020305891430428767

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @jumperz: I Built an AI Agent Swarm in Discord - Full Guide

**URL:** https://x.com/jumperz/status/2020305891430428767
**Author:** JUMPERZ (@jumperz) - Verified
**Posted:** Feb 8, 2026 (inferred from tweet ID)
**Engagement:** 39 replies, 57 reposts, 675 likes, 1.8K bookmarks, 77K views

## Summary
Comprehensive guide to building a Discord-based AI agent swarm. "It Works Better Than Anything I've Tried." 5 named agents (Find, Build, Track, Watch, Create) coordinate via Discord channels, spawn temporary "interns" for scale, use model tiering for cost optimization. Discord channels serve as the database - no Postgres, no vector stores. Always-on system with heartbeats, memory, and self-improvement loop.

## Full Article

### I Built an AI Agent Swarm in Discord. It Works Better Than Anything I've Tried (Full Guide)

So I built this agent coordination system that lives in my Discord server. They talk to each other, split work, and deliver results. I was surprised how easily this actually worked out. It's honestly kinda wild. Let me walk you through everything.

---

## The Entry Point (YOU)

You type plain English in #orders channel. No special commands. It's a Discord channel where everything starts.

Examples:
- "Research the top 10 AI coding tools and write a comparison thread"
- "Build a landing page for my new SaaS idea"
- "Track engagement on my last 5 tweets and suggest improvements"

That's it. Just natural language. Just drop your task like you're texting a friend.

---

## The Brain (Coordinator)

One smart model reads your task, thinks about what needs to happen, breaks it into pieces, spawns the right agents. **It never does the work itself. It only thinks and delegates.**

Like a manager who actually manages.

The coordinator sees "research AI coding tools" and thinks:
- 'Find agent': scrape websites, read docs, collect data
- 'Create agent': write the comparison thread
- 'Track agent': measure which tools get mentioned most

Then it spawns them all at once.

---

## The Team (5 Agents)

1. **Find (Research):** Web scraping, data collection, trend analysis
2. **Build (Implement):** Code, websites, automations, integrations
3. **Track (Measure):** Analytics, monitoring, performance data
4. **Watch (Observe):** Social listening, competitor tracking, alerts
5. **Create (Write):** Content, copy, documentation, threads

**All run as real independent sessions in parallel. Not one agent pretending to be many. Real separate sessions working at the same time.**

**PS.** You have to give them names so you can easily remember them later. Mine are called Scout, Max, John, Maya, etc. So when you need one you call them by name easily and your coordinator (which also needs a name) would remember and recognize them way easier.

---

## The Model Tier Trick

Only the coordinator and builder use the expensive smart model (Claude Opus). Everything else runs on the fast cheap one (Claude Haiku, Sonnet) whatever you want.

**Same quality and 80% less cost.**

If the output gets reviewed before shipping, the cheap model is fine because you're not publishing raw AI output anyway.

- Find agent scraping data? Haiku can do that.
- Create agent writing a thread? Sonnet + human review = good enough.
- Build agent writing complex code? That needs Opus.

And so on. **Smart routing = budget control.**

---

## Three Channels Per Agent

1. **Output (what they found):** The actual work results
2. **Logs (how they did it):** Debug info, thought process, errors
3. **Memory (what they learned):** Knowledge that persists between runs

**Discord channels ARE the database.** No Postgres, no vector stores. Already searchable, threaded, and persistent.

> Want to see what Find agent discovered about AI tools last month? Search #find-output.
> Need to debug why Build agent failed? Check #build-logs.

Everything is already organized and you didn't build a single database schema.

---

## Interns (You need channels for this)

Any agent can spawn temporary workers. One job, then gone.

Need to analyze 10 articles? Spawn 10 interns, all work at the same time, results in 3 minutes instead of 30.

That's how it scales without permanent cost. The 5 main agents are always available but the interns come and go based on workload.

> Big research project = 20 interns for 10 minutes.
> Slow day = zero interns.

You basically pay for what you use and scale when you need it.

---

## Coordination (#agent-chat)

Agents report "done", "stuck", or hand off to the next agent. Find hands to Build. Build hands to Track. Like a relay race.

The coordinator watches everything but the agents talk to each other directly... faster than going through the middle man every time.

Example conversation:
> Find: "Found 15 AI tools, data in #find-output, handing to Create"
> Create: "Got it, writing comparison thread now"
> Build: "Need the thread content before I can make the landing page"
> Create: "Thread done, check #create-output"

**It's real coordination, not scripted handoffs.**

---

## The Synthesis

Coordinator reads all outputs, combines into one clean result.

You asked one question, 5 agents worked on it, you get back one answer - not 5 separate messages.

**The magic happens in the synthesis.** Raw agent outputs are messy. The coordinator cleans it up, connects the dots, presents it like a human analyst would.

You see the polished result. The chaos stays in the background channels.

---

## Dashboard + Live Feed (You need channels for this)

Dashboard shows what happened today at a glance. Live feed lets you watch agents work in real time.

Most days you don't need to look. But when you're curious, it's there.

High level overview or deep dive - your choice.

---

## Memory System

Agents read their memory channels when they spawn. They know what they knew last time. **They get smarter every run.**

Two layers:
- **Discord channels** (shared team memory)
- **Local .md files** (private agent memory)

> Find agent remembers which websites have good data.
> Create agent remembers your writing style.
> Build agent remembers your preferred tech stack.

Knowledge compounds automatically.

---

## Local Config (Agent DNA)

- **SOUL.md** defines personality
- **AGENTS.md** has the rules
- **MEMORY.md** stores knowledge

**This lives on YOUR machine, not in some cloud. The agent DNA is yours.**

---

## Always On

Heartbeats pulse every 30 minutes. Cron jobs handle scheduled tasks. Event triggers react to the world.

You wake up to a morning brief of what happened overnight:
- "Found 5 new competitors while you slept"
- "Your thread got 50 replies, top feedback themes analyzed"
- "Server metrics look good, no issues detected"

**Work continues when you're not there.**

---

## Research (Self Improvement)

Drop a link in #drop-links. System auto summarizes, extracts takeaways, archives it.

**Research on autopilot.**

Every article you save gets processed:
- Summary in your words
- Key takeaways extracted
- Whatever we can apply in our system to improve
- Filed in searchable archive

Basically, the more articles and insights you find on X or other platforms and the more you drop in, the more your agents get smarter, because you're feeding them real knowledge they remember next time.

**Your input becomes their intelligence. The system learns what you learn.**

---

## Analysis

### Architecture Brilliance

**Discord as Infrastructure:** Using Discord channels as the database is genius. No schema design, built-in search, threading, persistence, mobile access, and notification system all come free.

**Model Tiering:** 80% cost reduction by routing tasks to appropriate model tiers. Opus for complex reasoning (coordinator, builder), Haiku/Sonnet for execution (scraping, writing with review).

**Intern Pattern:** Elastic scaling through ephemeral workers. 20 parallel interns for 10 minutes = same cost as 1 worker for 200 minutes, but 20x faster results.

**Named Agents:** Human-friendly naming (Scout, Max, John, Maya) makes the system approachable and memorable. The coordinator understands context better with names than IDs.

**Three-Channel Pattern:** Separating output/logs/memory prevents information overload while preserving full observability and historical knowledge.

### Coordination Philosophy

**Peer-to-Peer Delegation:** Agents coordinate directly rather than always routing through the coordinator. Faster handoffs, more natural workflow.

**Synthesis Layer:** The coordinator's primary value is synthesis, not execution. Turns multi-agent chaos into clean human-consumable output.

**Relay Race Metaphor:** Sequential handoffs (Find → Create → Build → Track) model real workflows better than parallel fan-out.

### Memory & Learning

**Dual Memory:** Discord (shared, searchable) + local .md files (private, portable). Best of both worlds.

**Knowledge Compounding:** "The system learns what you learn" - continuous improvement through research ingestion (#drop-links).

**Agent DNA:** SOUL.md, AGENTS.md, MEMORY.md live locally. Full control and portability.

### Operational Excellence

**Always-On:** 30-minute heartbeats + cron jobs + event triggers = autonomous operation. Morning briefs summarize overnight activity.

**Observability:** Dashboard (high-level), live feed (real-time), individual channel logs (deep dive). Choose your depth.

**Natural Language Interface:** No special commands, just type to #orders. The lowest-friction interface possible.

## Strategic Implications

**Framework-Free:** No mention of LangChain, AutoGen, or other orchestration frameworks. Pure agent coordination through Discord API + Claude.

**Cost-Conscious:** The model tiering strategy addresses the #1 objection to agentic systems - cost. 80% reduction makes this economically viable.

**Operational Autonomy:** Always-on operation with morning briefs suggests this replaces a virtual assistant or analyst, not just a coding tool.

**Self-Improvement Loop:** The #drop-links research ingestion creates a flywheel - the more you use it, the smarter it gets.

**Template Replicability:** "It Works Better Than Anything I've Tried" suggests this architecture is battle-tested and generalizable.

## Comparison to Other Systems

**vs. Yam Peleg's WhatsApp Swarm (Item 64):**
- Yam: WhatsApp groups, voice-controlled, "dangerously bypass permissions"
- JUMPERZ: Discord channels, text-based, structured architecture

**vs. Chi Wang's Orion (Item 65):**
- Orion: Multi-device coordination, GUI integration
- JUMPERZ: Single Discord server, pure coordination layer

**Common Patterns:**
- All three use named agents for human-friendly coordination
- All three emphasize autonomous operation ("while you slept")
- All three avoid traditional orchestration frameworks

## Technical Questions (Unanswered)

- **Agent Runtime:** What runs the independent sessions? Claude Code CLI? Custom implementation?
- **Discord Bot:** Is there a Discord bot handling the webhook integration?
- **State Management:** How does the coordinator track active agents and their status?
- **Conflict Resolution:** What happens when two agents try to spawn interns simultaneously?
- **Cost Tracking:** How is usage monitored across 5 agents + N interns?

## Categories
#discord #agent-swarm #multi-agent #coordination #model-tiering #cost-optimization #always-on #memory-system #synthesis #architecture #guide

## Related Items
- Item 64: Yam Peleg's WhatsApp agent swarm
- Item 65: Chi Wang's Orion multi-device system
- Item 62: Nicolas Bustamante on aggregation theory (infrastructure → API pattern)
- Pattern: Discord/messaging as agent infrastructure
- Pattern: Model tiering for cost optimization
- Pattern: Intern/ephemeral worker scaling

