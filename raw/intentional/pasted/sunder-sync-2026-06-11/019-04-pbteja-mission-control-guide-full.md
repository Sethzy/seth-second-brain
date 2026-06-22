---
type: raw_capture
source_type: x
title: "Sunder sync: 04-pbteja-mission-control-guide-FULL.md"
url: "https://x.com/pbteja1998/status/2017662163540971756"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/04-pbteja-mission-control-guide-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/04-pbteja-mission-control-guide-FULL.md"
sha256: "e356da989e1d5637503baaec3849c94f6e9459daca00747cdb82dd0d22abfefa"
duplicate_of: ""
---

# Sunder sync: 04-pbteja-mission-control-guide-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/04-pbteja-mission-control-guide-FULL.md`

Primary URL: https://x.com/pbteja1998/status/2017662163540971756

Duplicate of existing source-map entry: `none`

## Capture Text

# The Complete Guide to Building Mission Control - Bhanu Teja P

**Author:** Bhanu Teja P (@pbteja1998)
**Posted:** Feb 1, 2026
**URL:** https://x.com/pbteja1998/status/2017662163540971756

## Overview

Complete guide to building Mission Control - a system where 10 AI agents work together like a real team using Clawdbot (now OpenClaw). This is essentially running multiple Clawdbot sessions with specialized configurations.

## Part 1: Why I Built This

### The Problem With AI Assistants

Running @SiteGPT (AI chatbot for customer support), author encountered recurring issues with AI tools:
- **No continuity** - Every conversation started fresh
- **Lost context** - Research and previous work disappeared
- **No memory** - Context from yesterday was gone

### What Was Needed

- Agents that remember ongoing work
- Multiple agents with different skills working together
- Shared workspace for all context
- Ability to assign tasks and track progress
- **AI to work like a team, not like a search box**

### The Starting Point: Clawdbot

Clawdbot = open-source AI agent framework running as persistent daemon
- Connects to Claude (or other models)
- Provides tool access: file system, shell commands, web browsing
- One instance = one AI assistant (Jarvis) connected to Telegram

**Key insight:** Run multiple Clawdbot sessions, each with its own personality and context. The architecture was already there - just needed orchestration.

## Part 2: Understanding Clawdbot Architecture

### What Is Clawdbot?

AI agent framework with three main jobs:
1. **Connects AI models to real world** - File access, shell, web browsing, APIs
2. **Maintains persistent sessions** - Conversation history survives restarts
3. **Routes messages** - Connect to Telegram, Discord, Slack, etc.

Runs as daemon (background service) on server, listening and responding 24/7.

### The Gateway

Core process running 24/7:
- Manages all active sessions
- Handles cron jobs (scheduled tasks)
- Routes messages between channels and sessions
- Provides WebSocket API for control

Start with: `clawdbot gateway start`

Configuration in JSON file defines:
- AI provider and model (Anthropic, OpenAI, etc.)
- Channels to connect (Telegram, Discord, etc.)
- Tools agents can access
- Default system prompts and workspace paths

### Sessions: The Key Concept

**Session** = persistent conversation with context

Every session has:
- **Session key** - Unique identifier (e.g., `agent:main:main`)
- **Conversation history** - Stored as JSONL files on disk
- **Model** - Which AI to use
- **Tools** - What the AI can access

**IMPORTANT:** Sessions are independent. Each session has its own history, context, and "memory" of past conversations.

Multiple agents = multiple sessions, each with their own identity.

### How Sessions Work

```
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
- **Main sessions** - Long-running, interactive (like chatting with Jarvis)
- **Isolated sessions** - One-shot, for cron jobs (wake up, do task, done)

### Cron Jobs: Scheduled Agent Wakeups

Built-in cron system for scheduling tasks:

```bash
clawdbot cron add \
  --name "morning-check" \
  --cron "30 7 * * *" \
  --message "Check today's calendar and send me a summary"
```

When cron fires:
1. Gateway creates or wakes a session
2. Sends message to AI
3. AI responds (can use tools, send messages, etc.)
4. Session persists or terminates

This is how agents "wake up" periodically without being always-on.

### The Workspace

Every Clawdbot instance has a workspace = directory on disk:

```
/home/usr/clawd/ ← Workspace root
├── AGENTS.md ← Instructions for agents
├── SOUL.md ← Agent personality
├── memory/
│   ├── WORKING.md ← Current task state
│   ├── 2026-01-31.md ← Daily notes
│   └── ...
├── scripts/ ← Utilities agents can run
└── config/ ← Credentials, settings
```

Workspace enables information persistence between sessions:
- Agents write to files
- Files survive restarts
- Shared context across all agents

## Part 3: From One Clawdbot to Ten Agents

### The Insight

Clawdbot sessions are independent. Each can have:
- Its own personality (via SOUL.md)
- Its own memory files
- Its own cron schedule
- Its own tools and access

**Therefore:** Each agent = Clawdbot session with specialized configuration

**Example:**
- **Jarvis** = session `agent:main:main`, SOUL.md says "You are Jarvis, the squad lead...", access to all tools, connected to Telegram
- **Shuri** = session `agent:product-analyst:main`, SOUL.md says "You are Shuri, the product analyst...", same tools, own heartbeat cron

**Ten agents = ten sessions**
- Each waking up on own schedule
- Each with own context

## Engagement Stats

- **Replies:** 81
- **Reposts:** 104
- **Likes:** 1,004
- **Bookmarks:** 3,376
- **Views:** 169K

## Key Takeaways

1. **Multi-agent orchestration** is achievable by running multiple Clawdbot sessions
2. **Persistent context** via workspace files enables true memory across restarts
3. **Cron-based scheduling** allows agents to wake up and work autonomously
4. **Independent sessions** = independent personalities, contexts, and capabilities
5. **Shared workspace** enables team-like collaboration between agents

## Tools & Concepts

- **Clawdbot/OpenClaw** - Open-source AI agent framework
- **Gateway** - Core daemon managing sessions and routing
- **Sessions** - Persistent conversations with independent context
- **Cron jobs** - Scheduled task execution for autonomous agent behavior
- **Workspace** - Shared file system for persistent memory
- **SOUL.md** - Agent personality definition file

## Related

- Company: @SiteGPT (AI chatbot for customer support)
- Framework: Clawdbot (now OpenClaw)
- Category: Agent Infrastructure, Multi-Agent Systems, Agent Orchestration

