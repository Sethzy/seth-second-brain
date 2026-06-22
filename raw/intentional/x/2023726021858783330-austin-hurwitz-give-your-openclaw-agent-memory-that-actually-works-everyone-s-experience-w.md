---
type: raw_capture
source_type: x
url: https://x.com/austin_hurwitz/status/2023726021858783330
original_url: https://x.com/austin_hurwitz/status/2023726021858783330
author: "a12z"
handle: austin_hurwitz
status_id: 2023726021858783330
captured_at: 2026-06-19T21:22:07+08:00
published_at: "Tue Feb 17 11:47:37 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 30
  reposts: 44
  likes: 432
---

# X post by @austin_hurwitz

## Source

- Original: [https://x.com/austin_hurwitz/status/2023726021858783330](https://x.com/austin_hurwitz/status/2023726021858783330)
- Canonical: [https://x.com/austin_hurwitz/status/2023726021858783330](https://x.com/austin_hurwitz/status/2023726021858783330)
- Author: a12z (@austin_hurwitz)

## Verbatim Text

Give Your OpenClaw Agent Memory that Actually Works

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

2. Move key lessons from daily notes and memory to lessons.md

3. Remove outdated context

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

## X Article Metadata

- Title: Give Your OpenClaw Agent Memory that Actually Works
- Preview: Everyone's experience with OpenClaw starts the same. It feels like this great unlock - an agent who has context on everything you do and can take actions on your behalf.
Then inevitably it hits a

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
