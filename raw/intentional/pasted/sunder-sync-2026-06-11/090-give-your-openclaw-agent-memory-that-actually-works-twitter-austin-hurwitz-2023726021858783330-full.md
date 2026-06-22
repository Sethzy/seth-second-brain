---
type: raw_capture
source_type: x
title: "Sunder sync: give-your-openclaw-agent-memory-that-actually-works-twitter-austin-hurwitz-2023726021858783330-FULL.md"
url: "https://x.com/austin_hurwitz/status/2023726021858783330"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/give-your-openclaw-agent-memory-that-actually-works-twitter-austin-hurwitz-2023726021858783330-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/give-your-openclaw-agent-memory-that-actually-works-twitter-austin-hurwitz-2023726021858783330-FULL.md"
sha256: "b20fd47132a556f73452e62c5e5434e3cea53493167cf5c36885294c8663878c"
duplicate_of: ""
---

# Sunder sync: give-your-openclaw-agent-memory-that-actually-works-twitter-austin-hurwitz-2023726021858783330-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/give-your-openclaw-agent-memory-that-actually-works-twitter-austin-hurwitz-2023726021858783330-FULL.md`

Primary URL: https://x.com/austin_hurwitz/status/2023726021858783330

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @austin_hurwitz: Give Your OpenClaw Agent Memory that Actually Works

**URL:** https://x.com/austin_hurwitz/status/2023726021858783330
**Author:** austin (@austin_hurwitz)
**Posted:** Feb 17, 2026, 11:47 AM UTC
**Engagement:** 30 replies, 47 reposts, 438 likes, 36.5K views

## Summary
Near-verbatim extraction of the original X/Twitter post plus embedded X Article content when available.

## Full Article

### Original Post (Near-Verbatim)

https://t.co/2i3n2HWYGX

### Embedded X Article (Near-Verbatim): Give Your OpenClaw Agent Memory that Actually Works

Everyone's experience with OpenClaw starts the same. It feels like this great unlock - an agent who has context on everything you do and can take actions on your behalf.

Then inevitably it hits a wall.

 "I'm sorry, I don't remember what we were doing"

Memory is the biggest problem to solve and while my setup isn't fool proof it will get you in a much better place than your out of the box solution. 

## Step 1: Install QMD and make it the default (link:https://github.com/tobi/qmd)

Think of QMD as an on device search engine which indexes your various markdown files for more reliable, consistent, queries. 

Tell your agent to always default to QMD for search and save it in it's Tools.md file. 

## Step 2: Split up memory into four files: long term memory,  daily notes, active tasks, and lessons. 

The default memory system crams everything into a single markdown file. Over time this can become increasingly difficult for your agent to parse. Breaking the system into four files across the lifecycle of an agent's memory gives it more targeted searches depending on the context. When the agent makes a mistake be sure it always logs it in it's lessons file. 

## Step 3: Maintenance

Setup periodic crons as hygiene for your files. 

1. Review memory for anything that's actually a tool and move it to tools.md

1. Move key lessons from daily notes and memory to lessons.md 

1. Remove outdated context 

## Memory System Skill File (Point Your Agent Here)

```
# Memory System

You have persistent memory. Use it.

## Files
- MEMORY.md — Long-term context. Read every session.
- TOOLS.md — Technical configs and how-to.
- memory/YYYY-MM-DD.md — Daily notes. Write immediately.
- memory/active-tasks.md — In-progress work. Check on startup.
- memory/lessons.md — Mistakes worth remembering.

## Session Start
1. Read MEMORY.md
2. Check active-tasks.md — resume any interrupted work
3. Read today's daily notes if they exist

## During Session
Write to daily notes immediately when:
- You complete something
- You learn a preference
- A decision gets made
- Something important happens

## Finding Things
Use `qmd query "search terms"` to search across all memory files.
Use `qmd get <file>:<line> -l N` to pull specific sections.

## Maintenance
Periodically move important stuff from daily notes to MEMORY.md.
Move technical learnings to TOOLS.md.
Remove outdated content.

## Principle
Text beats brain. If you want to remember it, write it down.
```


## Metadata
- Tweet ID: 2023726021858783330
- Canonical URL: https://twitter.com/austin_hurwitz/status/2023726021858783330
- Source tier used: tier2
- Embedded X article extracted: yes

