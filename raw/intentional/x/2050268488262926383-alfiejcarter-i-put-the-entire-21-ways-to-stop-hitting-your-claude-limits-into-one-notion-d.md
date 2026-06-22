---
type: raw_capture
source_type: x
url: https://x.com/AlfieJCarter/status/2050268488262926383
original_url: https://x.com/AlfieJCarter/status/2050268488262926383
author: "Alfie Carter"
handle: AlfieJCarter
status_id: 2050268488262926383
captured_at: 2026-06-19T22:19:44+08:00
published_at: "Fri May 01 17:37:54 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 30
  reposts: 3
  likes: 35
---

# X post by @AlfieJCarter

## Source

- Original: [https://x.com/AlfieJCarter/status/2050268488262926383](https://x.com/AlfieJCarter/status/2050268488262926383)
- Canonical: [https://x.com/AlfieJCarter/status/2050268488262926383](https://x.com/AlfieJCarter/status/2050268488262926383)
- Author: Alfie Carter (@AlfieJCarter)

## Verbatim Text

I put the entire 21 Ways to Stop Hitting Your Claude Limits into ONE Notion doc.

3 sections. No fluff.

- Why you are hitting your limit in the first place: every message forces Claude to reread the entire conversation from the beginning - your 30th message costs more than your first 15 combined. One developer tracked a 100-message session and found 98.5% of tokens went to rereading history and only 1.5% went to generating the response. It is a context hygiene problem not a Claude problem
- 9 general tips that apply everywhere: edit instead of following up so bad responses get replaced not stacked, batch all requests into one prompt so three tasks cost one context reload not three, fresh chat every 15-20 messages with a pasted summary, right model per task with Haiku for quick and Opus only for deep reasoning, extended thinking off by default since output tokens cost 5x more than input, files converted to markdown before uploading to reduce token weight by 60-90%, projects for repeated documents so they are cached not retokenised, session reset timing to start your 5-hour window early, and off-peak working since same prompts cost less when fewer people are on the platform
- 8 Claude Code tips and 4 Cowork tips covering the segments most people never address: run /context before typing anything since most people are already 40-70k tokens deep before their first message, disconnect MCP servers not in use since one server can be 18k tokens of dead weight per turn, replace MCPs with CLIs for 40% token savings, use /clear between unrelated tasks as the single habit separating people who hit limits in 2 hours from people who never hit them, run /compact at 50% not 95%, use sub-agents with Haiku for grunt work and Opus for thinking only, keep CLAUDE.md under 200 lines, point Cowork at a clean dedicated folder only containing files relevant to the current task, and build a local memory system with instructions.md and memory.md that is portable across any tool

This is the setup I would have KILLED for before burning Opus tokens on tasks Haiku handles identically, hitting my limit two hours into a session with no idea why, and paying for irrelevant session history on every new prompt across a full working day.

Like + comment "LIMITS" and I'll send it over

(must be connected for priority access)

## Media

- photo: https://pbs.twimg.com/media/HHQEUHUW8AA4YBn.png

## Capture Note

TweetDetail returned complete normal-post text.
