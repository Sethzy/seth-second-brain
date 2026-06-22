---
type: raw_capture
source_type: x
title: "Sunder sync: 11-jesseprovo-FULL.md"
url: "https://x.com/jesseprovo/status/2016280574684758507"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/11-jesseprovo-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/11-jesseprovo-FULL.md"
sha256: "a8be81e21e0774be83335da36c5fb66c591f453f9d5902d5718999f02d3df9b0"
duplicate_of: ""
---

# Sunder sync: 11-jesseprovo-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/11-jesseprovo-FULL.md`

Primary URL: https://x.com/jesseprovo/status/2016280574684758507

Duplicate of existing source-map entry: `none`

## Capture Text

# Jesse Provost - Background Agents: From Reactive Alerts to Proactive Discovery

**Author:** Jesse Provost (@JesseProvo)
**Posted:** 6:42 AM · Jan 28, 2026
**URL:** https://x.com/jesseprovo/status/2016280574684758507

## Main Thesis

**"Background Agents: From Reactive Alerts to Proactive Discovery"**

Alerting systems are one of the most natural applications for AI agents, but traditional alerts are brittle. Agents change this fundamentally.

## The Problem with Traditional Alerts

Traditional alerting systems are **brittle:**
- Match **keywords without understanding meaning**
- Fire on **schedules without considering context**
- Require **manual configuration for every trigger**

## What Agents Enable

Agents can:
- **Understand what you actually care about**
- **Discover where that information appears**
- **Interpret whether a match is genuinely relevant**
- **Maintain state across runs**
- **Update their own configuration**
- **Learn from your behavior**

## Context: Fintool's Alerting System

### Domain

**Financial research:** SEC filings, earnings calls, press releases, market data

### User Problem

Investment analyst covering 50 companies needs to monitor:
- All SEC filings
- All earnings calls
- All press releases
- Market data across entire portfolio

### Inadequate Options

1. **Subscribe to everything** → notification fatigue
2. **Miss critical information** → business risk

**Goal:** Build something better using AI agents.

## The Fundamental Challenge

**Relevance varies by profession and context.**

Different roles need different signals:
- Portfolio manager ≠ Credit analyst
- Merger arbitrageur ≠ Dividend investor

"Material" information depends entirely on the user's **investment thesis**.

## Example: "Alert me when a company announces layoffs"

Seems straightforward, but:

### Where layoffs might be disclosed:
- 8-K filing
- Earnings call mention
- Press release
- 10-Q footnote (buried)

### Language variation:
- "layoffs" might not appear
- Companies say: "workforce reduction," "restructuring," "right-sizing," "headcount optimization"

### Announcement vs. reference:
- Not all mentions are announcements
- CEO might say "we have no plans for layoffs"
- Might reference layoffs from years ago

### Materiality varies:
- 100 layoffs at 500-person company = **significant**
- 100 layoffs at 50,000-person company = **noise**

**Result:** Traditional keyword alerts fail spectacularly - either miss relevant documents (false negatives) or flood users with irrelevant matches (false positives).

## Fintool's Solution

### Insight: Separate Triggering from Analysis

1. **Cast a wide net** with triggers (err heavily on inclusion)
2. **Let AI handle semantic interpretation:**
   - Is this actually a layoff announcement?
   - Is it material?
   - What are the details?

## Agent Skills Architecture

### Natural Language Alert Creation

Users create alerts through natural conversation (not forms or config syntax).

Built on **Agent Skills** (from both Anthropic and OpenAI):
- Organized folders of instructions, scripts, and resources
- Agents discover and load dynamically
- Perform specific tasks

**A skill encodes:**
- Mechanical steps to accomplish something
- **Domain knowledge** that makes those steps effective

### Fintool's Alerts Skill

Teaches the LLM how to configure monitoring that actually works for financial professionals.

### Example Workflow

User says: "set up an alert for when any biotech in my portfolio mentions Phase 3 trial results"

**Agent follows structured workflow** (details in third step below)

## The Critical Third Step: Asking Questions

Real user requests are often **underspecified**.

The agent must clarify:
- Which specific companies?
- What triggers relevance?
- What actions to take?
- Delivery preferences?

## Engagement Stats

- **Replies:** 3
- **Reposts:** 7
- **Likes:** 87
- **Bookmarks:** 235
- **Views:** 32.8K

## Key Takeaways

1. **Traditional alerts are brittle** - keyword matching fails for complex domains
2. **Agent alerts are semantic** - understand meaning, not just keywords
3. **Separation of concerns** - wide triggering + AI interpretation
4. **Agent Skills pattern** - encodes both mechanics and domain knowledge
5. **Natural language config** - conversation beats forms
6. **Context matters** - relevance varies by role and investment thesis
7. **Underspecification** - agents must ask clarifying questions

## Technical Architecture

### Components

- **Trigger layer:** Wide net, high recall
- **AI interpretation layer:** Semantic analysis, relevance filtering
- **Agent Skills:** Domain knowledge + procedures
- **Natural language interface:** Conversational alert creation
- **State management:** Agents maintain context across runs
- **Self-updating:** Agents update their own configuration
- **Behavioral learning:** Learn from user actions

### Domain: Financial Research

- SEC filings (8-K, 10-Q, 10-K)
- Earnings calls (transcripts)
- Press releases
- Market data
- Company-specific monitoring across portfolios

## Use Cases

- **Investment analysts:** Monitor 50+ companies
- **Portfolio managers:** Material events affecting holdings
- **Credit analysts:** Risk indicators and financial health
- **Merger arbitrageurs:** Deal-related developments
- **Dividend investors:** Dividend policy changes

## Category

AI Agents, Financial Technology, Alerting Systems, Agent Skills

## Related

- **Company:** Fintool (financial research alerting)
- **Domain:** Financial research and analysis
- **Pattern:** Agent Skills (Anthropic/OpenAI)
- **Architecture:** Trigger layer + AI interpretation

