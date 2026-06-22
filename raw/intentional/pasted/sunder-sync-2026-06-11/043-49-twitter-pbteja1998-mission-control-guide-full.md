---
type: raw_capture
source_type: x
title: "Sunder sync: 49-twitter-pbteja1998-mission-control-guide-FULL.md"
url: "https://x.com/pbteja1998/status/2017662163540971756"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/49-twitter-pbteja1998-mission-control-guide-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/49-twitter-pbteja1998-mission-control-guide-FULL.md"
sha256: "67a9479f00098ff6b2a52e8f3e690d320e309d19450b40f9520457b5d5c25974"
duplicate_of: ""
---

# Sunder sync: 49-twitter-pbteja1998-mission-control-guide-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/49-twitter-pbteja1998-mission-control-guide-FULL.md`

Primary URL: https://x.com/pbteja1998/status/2017662163540971756

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @pbteja1998: Complete Guide to Building Mission Control (10 AI Agent Squad)

**URL:** https://x.com/pbteja1998/status/2017662163540971756
**Author:** Bhanu Teja P (@pbteja1998) - Verified
**Platform:** Twitter/X Article
**Posted:** (Date from URL: Jan 31, 2026)
**Engagement:** 431 replies, 1.1K reposts, 8.2K likes, 31.6K bookmarks, 3.7M views

## Article Summary

Bhanu Teja's comprehensive technical guide on building "Mission Control" - a system where 10 AI agents work together like a real team using Clawdbot/OpenClaw. Covers architecture, sessions, cron jobs, shared database (Convex), agent personalities (SOUL files), memory persistence, heartbeat system, notifications, and daily standups. Each agent is an independent Clawdbot session with specialized configuration. Agents communicate via shared Mission Control database and @mentions. Extremely high engagement (31.6K bookmarks, 3.7M views) indicates this is a definitive technical resource.

## Article Title

"The Complete Guide to Building Mission Control: How We Built an AI Agent Squad"

## Opening

"This is the full story of how I built Mission Control. A system where 10 AI agents work together like a real team.

If you want to replicate this setup, this guide covers everything.

If you're already familiar with Clawdbot (now OpenClaw), you might be thinking 'wait, can't I just run multiple Clawdbots?'

Yes. That's exactly what this is. This guide shows you how."

## Part 1: Why I Built This

### The Problem With AI Assistants

"I run @SiteGPT, an AI chatbot for customer support. I use AI constantly. But every AI tool I tried had the same problem.

**No continuity.** Every conversation started fresh. Context from yesterday? Gone. That research I asked for last week? Lost in some chat thread I'd never find again.

I wanted something different:
- Agents that remember what they're working on
- Multiple agents with different skills working together
- A shared workspace where all context lives
- The ability to assign tasks and track progress

Basically, I wanted AI to work like a team, not like a search box."

### The Starting Point: Clawdbot

"I was already using Clawdbot. It's an open-source AI agent framework that runs as a persistent daemon.

It connects to Claude (or other models) and gives the AI access to tools like:
- File system
- Shell commands
- Web browsing
- And more

One Clawdbot instance gave me one AI assistant (Jarvis) connected to Telegram. Useful, but limited.

Then I had a thought. What if I ran multiple Clawdbot sessions, each with its own personality and context?

That's when I realized the architecture was already there. I just needed to orchestrate it."

## Part 2: Understanding Clawdbot Architecture

### What Is Clawdbot?

"Clawdbot (now called OpenClaw) is an AI agent framework with three main jobs:

1. **Connects AI models to the real world**
   - File access
   - Shell commands
   - Web browsing
   - APIs

2. **Maintains persistent sessions**
   - Conversation history that survives restarts

3. **Routes messages**
   - Connect the AI to Telegram, Discord, Slack, or any channel

It runs as a daemon (background service) on a server, listening for messages and responding."

### The Gateway

"The Gateway is the core process:
- Runs 24/7 on your server
- Manages all active sessions
- Handles cron jobs (scheduled tasks)
- Routes messages between channels and sessions
- Provides a WebSocket API for control

Start it with:
```bash
clawdbot gateway start
```

Configuration lives in a JSON file. You define:
- Which AI provider and model to use (Anthropic, OpenAI, etc.)
- Which channels to connect (Telegram, Discord, etc.)
- What tools agents can access
- Default system prompts and workspace paths"

### Sessions: The Key Concept

"A session is a persistent conversation with context.

Every session has:
- **Session key** (unique identifier, like `agent:main:main`)
- **Conversation history** (stored as JSONL files on disk)
- **Model** (which AI to use)
- **Tools** (what the AI can access)

Here's the important part:

**Sessions are independent.** Each session has its own history, its own context, its own 'memory' of past conversations.

When you run multiple agents, you're really running multiple sessions. Each with their own identity."

### How Sessions Work

```plaintext
User sends message to Telegram
↓
Gateway receives it
↓
Gateway routes to correct session (based on config)
↓
Session loads conversation history
↓
AI generates response (with full context)
↓
Response sent back through Telegram
↓
History updated and saved to disk
```

**Session types:**
- **Main sessions** (long-running, interactive, like chatting with Jarvis)
- **Isolated sessions** (one-shot, for cron jobs, wake up, do task, done)

### Cron Jobs: Scheduled Agent Wakeups

"Clawdbot has a built-in cron system. You can schedule tasks:

```bash
clawdbot cron add \\
  --name 'morning-check' \\
  --cron '30 7 * * *' \\
  --message 'Check today's calendar and send me a summary'
```

When a cron fires:
1. Gateway creates or wakes a session
2. Sends the message to the AI
3. AI responds (can use tools, send messages, etc.)
4. Session can persist or terminate

This is how agents 'wake up' periodically without being always-on."

### The Workspace

"Every Clawdbot instance has a workspace. That's a directory on disk where:
- Configuration files live
- Memory files are stored
- Scripts and tools are accessible
- The AI can read and write files

The workspace is how agents persist information between sessions. They write to files. Those files survive restarts.

```plaintext
/home/usr/clawd/ ← Workspace root
├── AGENTS.md ← Instructions for agents
├── SOUL.md ← Agent personality
├── memory/
│   ├── WORKING.md ← Current task state
│   ├── 2026-01-31.md ← Daily notes
│   └── ...
├── scripts/ ← Utilities agents can run
└── config/ ← Credentials, settings
```"

## Part 3: From One Clawdbot to Ten Agents

### The Insight

"Clawdbot sessions are independent. Each can have:
- Its own personality (via SOUL.md)
- Its own memory files
- Its own cron schedule
- Its own tools and access

So each agent is just a Clawdbot session with a specialized configuration.

**Jarvis** isn't special. He's a session with:
- Session key `agent:main:main`
- A SOUL.md that says 'You are Jarvis, the squad lead...'
- Access to all tools
- A connection to my Telegram

**Shuri** is another session with:
- Session key `agent:product-analyst:main`
- A SOUL.md that says 'You are Shuri, the product analyst...'
- The same tools (file access, shell, browser)
- Her own heartbeat cron

**Ten agents = ten sessions.** Each waking up on their own schedule. Each with their own context."

### Session Keys: Agent Identity

```plaintext
agent:main:main → Jarvis (Squad Lead)
agent:product-analyst:main → Shuri
agent:customer-researcher:main → Fury
agent:seo-analyst:main → Vision
agent:content-writer:main → Loki
agent:social-media-manager:main → Quill
agent:designer:main → Wanda
agent:email-marketing:main → Pepper
agent:developer:main → Friday
agent:notion-agent:main → Wong
```

When I send a message to a specific session, only that agent receives it. Their histories are separate."

### Cron Jobs: The Heartbeat

"Each agent has a cron job that wakes them every 15 minutes:

```bash
# Pepper wakes at :00, :15, :30, :45
clawdbot cron add \\
  --name 'pepper-mission-control-check' \\
  --cron '0,15,30,45 * * * *' \\
  --session 'isolated' \\
  --message 'You are Pepper, the Email Marketing Specialist. Check Mission Control for new tasks...'
```

The schedule is staggered so agents don't all wake at once:
- :00 Pepper
- :02 Shuri
- :04 Friday
- :06 Loki
- :07 Wanda
- :08 Vision
- :10 Fury
- :12 Quill

Each cron creates an **isolated session**. It runs, does its job, and terminates. This keeps costs down."

### Agents Talking to Each Other

"How do agents communicate?

**Option 1: Direct session messaging**
```bash
clawdbot sessions send --session 'agent:seo-analyst:main' --message 'Vision, can you review this?'
```
Jarvis can send messages directly to Vision's session.

**Option 2: Shared database (Mission Control)**
All agents read and write to the same Convex database. When Fury posts a comment, everyone can see it.

We use **Option 2 primarily.** It creates a shared record of all communication."

## Part 4: The Shared Brain (Mission Control)

### What Mission Control Does

"Mission Control is the shared infrastructure that turns independent agents into a team.

It provides:
- **Shared task database** where everyone sees the same tasks
- **Comment threads** where agents discuss work in one place
- **Activity feed** for real-time visibility into what's happening
- **Notification system** where @mentions alert specific agents
- **Document storage** where deliverables live in a shared repo

Think of it as the 'office' where all agents work. Each agent is still a separate Clawdbot session, but they're all looking at the same whiteboard."

### Why Convex?

"I chose Convex for the database because:
- **Real-time** (changes propagate instantly, when Loki posts a comment, the UI updates live)
- **Serverless** (no database to manage)
- **TypeScript-native** (type safety throughout)
- **Generous free tier** (more than enough for this scale)"

### The Schema

"Six tables power everything:

```javascript
agents: {
  name: string,        // 'Shuri'
  role: string,        // 'Product Analyst'
  status: 'idle' | 'active' | 'blocked',
  currentTaskId: Id<'tasks'>,
  sessionKey: string,  // 'agent:product-analyst:main'
}

tasks: {
  title: string,
  description: string,
  status: 'inbox' | 'assigned' | 'in_progress' | 'review' | 'done',
  assigneeIds: Id<'agents'>[],
}

messages: {
  taskId: Id<'tasks'>,
  fromAgentId: Id<'agents'>,
  content: string,     // The comment text
  attachments: Id<'documents'>[],
}

activities: {
  type: 'task_created' | 'message_sent' | 'document_created' | ...,
  agentId: Id<'agents'>,
  message: string,
}

documents: {
  title: string,
  content: string,     // Markdown
  type: 'deliverable' | 'research' | 'protocol' | ...,
  taskId: Id<'tasks'>, // If attached to a task
}

notifications: {
  mentionedAgentId: Id<'agents'>,
  content: string,
  delivered: boolean,
}
```

Agents interact with this via Convex CLI commands:

```bash
# Post a comment
npx convex run messages:create '{\"taskId\": \"...\", \"content\": \"Here's my research...\"}'

# Create a document
npx convex run documents:create '{\"title\": \"...\", \"content\": \"...\", \"type\": \"deliverable\"}'

# Update task status
npx convex run tasks:update '{\"id\": \"...\", \"status\": \"review\"}'
```"

### The Mission Control UI

"I built a React frontend that displays all this data:
- **Activity Feed** showing a real-time stream of everything happening
- **Task Board** with Kanban columns (Inbox → Assigned → In Progress → Review → Done)
- **Agent Cards** showing the status of each agent and what they're working on
- **Document Panel** to read and create deliverables
- **Detail View** where you can expand any task to see full context and comments

The aesthetic is intentionally warm and editorial. Like a newspaper dashboard. I spend hours looking at this, so it should feel good."

## Part 5: The SOUL System (Agent Personalities)

### What's in a SOUL

```markdown
# SOUL.md — Who You Are

**Name:** Shuri
**Role:** Product Analyst

## Personality
Skeptical tester. Thorough bug hunter. Finds edge cases.
Think like a first-time user. Question everything. Be specific.
Don't just say 'nice work.'

## What You're Good At
- Testing features from a user perspective
- Finding UX issues and edge cases
- Competitive analysis (how do others do this?)
- Screenshots and documentation

## What You Care About
- User experience over technical elegance
- Catching problems before users do
- Evidence over assumptions
```"

### Why Personalities Matter

"An agent who's 'good at everything' is mediocre at everything.

But an agent who's specifically 'the skeptical tester who finds edge cases' will actually find edge cases. The constraint focuses them.

Each of our agents has a distinct voice:
- **Loki** is opinionated about word choice (pro-Oxford comma, anti-passive voice)
- **Fury** provides receipts for every claim (sources, confidence levels)
- **Shuri** questions assumptions and looks for what could break
- **Quill** thinks in hooks and engagement"

### The AGENTS.md File

"SOUL says who you are. AGENTS.md says how to operate.

Every agent reads AGENTS.md on startup. It covers:
- Where files are stored
- How memory works
- What tools are available
- When to speak vs. stay quiet
- How to use Mission Control

This is the operating manual. Without it, agents make inconsistent decisions about basic things."

## Part 6: Memory and Persistence

### The Memory Stack

"AI sessions start fresh by default. No memory of yesterday. This is a feature (prevents context bloat) but also a problem (agents forget what they're doing).

**1. Session Memory (Clawdbot built-in)**
Clawdbot stores conversation history in JSONL files. Agents can search their own past conversations.

**2. Working Memory (/memory/WORKING.md)**
Current task state. Updated constantly.

```markdown
# WORKING.md

## Current Task
Researching competitor pricing for comparison page

## Status
Gathered G2 reviews, need to verify credit calculations

## Next Steps
1. Test competitor free tier myself
2. Document the findings
3. Post findings to task thread
```

This is the most important file. When an agent wakes up, they read WORKING.md first to remember what they were doing.

**3. Daily Notes (/memory/YYYY-MM-DD.md)**
Raw logs of what happened each day.

```markdown
# 2026-01-31

## 09:15 UTC
- Posted research findings to comparison task
- Fury added competitive pricing data
- Moving to draft stage

## 14:30 UTC
- Reviewed Loki's first draft
- Suggested changes to credit trap section
```

**4. Long-term Memory (MEMORY.md)**
Curated important stuff. Lessons learned, key decisions, stable facts."

### The Golden Rule

"If you want to remember something, write it to a file.

'Mental notes' don't survive session restarts. Only files persist.

When I tell an agent 'remember that we decided X,' they should update a file. Not just acknowledge and forget."

## Part 7: The Heartbeat System

### The Problem

"Always-on agents burn API credits doing nothing. But always-off agents can't respond to work."

### The Solution: Scheduled Heartbeats

"Each agent wakes up every 15 minutes via cron job:

```plaintext
:00 Pepper wakes up
    → Checks for @mentions
    → Checks assigned tasks
    → Scans activity feed
    → Does work or reports HEARTBEAT_OK
    → Goes back to sleep

:02 Shuri wakes up → Same process
:04 Friday wakes up → Same process
...and so on
```"

### What Happens During a Heartbeat

"1. **Load context**
   - Read WORKING.md
   - Read recent daily notes
   - Check session memory if needed

2. **Check for urgent items**
   - Am I @mentioned anywhere?
   - Are there tasks assigned to me?

3. **Scan activity feed**
   - Any discussions I should contribute to?
   - Any decisions that affect my work?

4. **Take action or stand down**
   - If there's work to do, do it
   - If nothing, report HEARTBEAT_OK"

### The HEARTBEAT.md File

```markdown
# HEARTBEAT.md

## On Wake
- [ ] Check memory/WORKING.md for ongoing tasks
- [ ] If task in progress, resume it
- [ ] Search session memory if context unclear

## Periodic Checks
- [ ] Mission Control for @mentions
- [ ] Assigned tasks
- [ ] Activity feed for relevant discussions
```

Agents follow this checklist strictly."

### Why 15 Minutes?

"- **Every 5 minutes** is too expensive. Agents wake too often with nothing to do.
- **Every 30 minutes** is too slow. Work sits waiting too long.
- **Every 15 minutes** is a good balance. Most work gets attention quickly without excessive costs."

## Part 8: The Notification System

### @Mentions

"Type @Vision in a comment → Vision gets notified on his next heartbeat
Type @all → Everyone gets notified"

### How Delivery Works

"A daemon process (running via pm2) polls Convex every 2 seconds:

```javascript
// Simplified
while (true) {
  const undelivered = await getUndeliveredNotifications();

  for (const notification of undelivered) {
    const sessionKey = AGENT_SESSIONS[notification.mentionedAgentId];

    try {
      await clawdbot.sessions.send(sessionKey, notification.content);
      await markDelivered(notification.id);
    } catch (e) {
      // Agent might be asleep, notification stays queued
    }
  }

  await sleep(2000);
}
```

If an agent is asleep (no active session), delivery fails. The notification stays queued.

Next time that agent's heartbeat fires and their session activates, the daemon successfully delivers."

### Thread Subscriptions

"**The problem:** 5 agents discussing a task. Do you @mention all 5 every comment?

**The solution:** Subscribe to threads.

When you interact with a task, you're subscribed:
- Comment on a task → subscribed
- Get @mentioned → subscribed
- Get assigned to the task → subscribed

Once subscribed, you get notified of ALL future comments. No @mention needed.

This makes conversations flow naturally. Just like Slack or email threads."

## Part 9: The Daily Standup

### What It Is

"Every day at 11:30 PM IST, a cron fires that:
1. Checks all agent sessions
2. Gathers recent activity
3. Compiles a summary
4. Sends it to my Telegram"

### The Format
(Content was cut off in snapshot)

## Engagement Analysis

**3.7M views:** Massive reach for technical content
**31.6K bookmarks:** Extremely high (0.85% bookmark rate)
**8.2K likes:** Strong engagement
**431 replies:** Very active discussion (likely implementation questions)

**Bookmarks:Likes ratio = 3.85** (exceptionally high)
**Interpretation:** Developers saving as definitive technical reference

## Author Context: Bhanu Teja P

**Known for:** SiteGPT (AI chatbot for customer support)
**Credibility:** Verified, hands-on builder, detailed technical knowledge
**Content style:** Comprehensive, practical, step-by-step

## The 10 Agents

1. **Jarvis** (Squad Lead) - `agent:main:main`
2. **Shuri** (Product Analyst) - `agent:product-analyst:main`
3. **Fury** (Customer Researcher) - `agent:customer-researcher:main`
4. **Vision** (SEO Analyst) - `agent:seo-analyst:main`
5. **Loki** (Content Writer) - `agent:content-writer:main`
6. **Quill** (Social Media Manager) - `agent:social-media-manager:main`
7. **Wanda** (Designer) - `agent:designer:main`
8. **Pepper** (Email Marketing) - `agent:email-marketing:main`
9. **Friday** (Developer) - `agent:developer:main`
10. **Wong** (Notion Agent) - `agent:notion-agent:main`

## Key Insights

### 1. Sessions = Agents
**Core insight:** Each agent is just a Clawdbot session with specialized config
**Not:** 10 different codebases
**Instead:** 10 configurations of same framework

### 2. Heartbeat Cost Optimization
**15-minute intervals:** Balance between responsiveness and API costs
**Isolated sessions:** Wake, work, sleep (don't stay active)
**Staggered schedule:** Agents don't all wake simultaneously

### 3. Shared Database as Coordination Layer
**Convex:** Real-time, serverless, TypeScript-native
**Pattern:** Independent agents, shared state
**Benefit:** No complex inter-process communication

### 4. Memory = Files, Not Context
**Rule:** "Mental notes don't survive restarts"
**Solution:** Write everything to WORKING.md, daily notes, MEMORY.md
**Persistence:** Only files survive session termination

### 5. Personalities Enable Specialization
**Generic agent:** Mediocre at everything
**Specialized agent:** Excellent at specific role
**Constraint:** Focuses behavior and output quality

### 6. Thread Subscriptions > Manual @mentions
**Problem:** 5-agent discussion requires constant @mentioning
**Solution:** Auto-subscribe when you interact
**Result:** Natural conversation flow like Slack

## Technical Stack

**AI Framework:** Clawdbot/OpenClaw
**Database:** Convex (real-time, serverless)
**Frontend:** React
**Process Manager:** pm2 (for notification daemon)
**Chat Platforms:** Telegram, Discord, Slack (supported)
**File Format:** JSONL (session history), Markdown (memory files)

## Use Cases

### For Solo Founders
**Problem:** No team for specialized work
**Solution:** 10 AI agents with distinct roles
**Benefit:** Product analyst + SEO + content writer + developer all working

### For Content Teams
**Agents:** Content writer, SEO analyst, social media manager
**Coordination:** Shared task board, comment threads
**Output:** SEO-optimized content with social promotion

### For Product Development
**Agents:** Product analyst, developer, designer
**Workflow:** Shuri tests → Friday builds → Wanda designs
**Mission Control:** Track features from idea to launch

## Comparison to Other Items

**vs Item 46 (Peter Yang):** Single user + Google Workspace
**vs Item 48 (Composio):** 1000+ app integrations
**Item 49 (Bhanu):** Multi-agent team orchestration

**Bhanu's unique angle:** Team dynamics, agent personalities, coordination at scale

## Missing Information

**Daily Standup format:** (Content cut off)
**Full implementation code:** Not included (architectural guide only)
**Cost analysis:** Not provided (API costs for 10 agents)
**Mission Control UI screenshots:** Not accessible
**Complete article:** May have more content beyond snapshot

## Implementation Complexity

**Beginner-friendly:** No (requires deep Clawdbot knowledge)
**Target audience:** Experienced developers
**Prerequisites:**
- Understanding of Clawdbot/OpenClaw
- Server administration
- Database knowledge (Convex)
- React (for UI)

## Category

OpenClaw, Clawdbot, Multi-Agent Systems, AI Orchestration, Agent Coordination, Convex, Mission Control, Team Dynamics, Agent Personalities, Technical Architecture

## Related

- **Author:** Bhanu Teja P (@pbteja1998) - Verified, SiteGPT founder
- **Date:** January 31, 2026 (inferred from URL)
- **Subject:** Complete guide to building 10-agent Mission Control system
- **Format:** Twitter Article (long-form technical guide)
- **Engagement:** 3.7M views, 31.6K bookmarks (0.85% rate, extremely high)
- **Architecture:** 10 Clawdbot sessions + shared Convex database
- **10 agents:** Jarvis (lead), Shuri (product), Fury (research), Vision (SEO), Loki (content), Quill (social), Wanda (design), Pepper (email), Friday (dev), Wong (Notion)
- **Key files:** SOUL.md (personality), AGENTS.md (operating manual), WORKING.md (current state), HEARTBEAT.md (checklist)
- **Heartbeat:** 15-minute intervals, staggered schedule, isolated sessions
- **Database:** Convex (6 tables: agents, tasks, messages, activities, documents, notifications)
- **Coordination:** @mentions, thread subscriptions, activity feed, task board
- **Memory:** Files only (session memory, WORKING.md, daily notes, MEMORY.md)
- **UI:** React dashboard (Kanban, activity feed, agent cards, documents)
- **Technical:** Clawdbot Gateway, cron jobs, pm2 daemon, WebSocket API
- **Specialization:** Each agent has distinct personality and role
- **Cost optimization:** Wake only every 15 minutes, terminate after work
- **Related:** Item 46 (single-user setup), Item 48 (Composio integrations)
- **Target:** Experienced developers building multi-agent systems
- **Complexity:** High (server, database, orchestration, UI)
- **Credibility:** Very high (hands-on implementation, detailed architecture)

