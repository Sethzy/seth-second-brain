---
type: raw_capture
source_type: x
url: https://x.com/himanshustwts/status/2038924027411222533
original_url: https://x.com/i/status/2038924027411222533
author: "himanshu"
handle: himanshustwts
status_id: 2038924027411222533
captured_at: 2026-06-19T23:40:23+08:00
published_at: "Tue Mar 31 10:19:04 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 152
  reposts: 692
  likes: 6348
---

# X post by @himanshustwts

## Source

- Original: [https://x.com/i/status/2038924027411222533](https://x.com/i/status/2038924027411222533)
- Canonical: [https://x.com/himanshustwts/status/2038924027411222533](https://x.com/himanshustwts/status/2038924027411222533)
- Author: himanshu (@himanshustwts)

## Verbatim Text

Based on everything explored in the source code, here's the full technical recipe behind Claude Code's memory architecture:

[shared by claude code]

Claude Code’s memory system is actually insanely well-designed. It isn't like  “store everything” but constrained, structured and self-healing memory.

The architecture is doing a few very non-obvious things:

> Memory = index, not storage
+ MEMORY.md is always loaded, but it’s just pointers (~150 chars/line)
+ actual knowledge lives outside, fetched only when needed

> 3-layer design (bandwidth aware)
 + index (always)
 + topic files (on-demand)
+ transcripts (never read, only grep’d)

> Strict write discipline
 +  write to file → then update index
 + never dump content into the index
 +  prevents entropy / context pollution

> Background “memory rewriting” (autoDream)
 +  merges, dedupes, removes contradictions
 +  converts vague → absolute
 +  aggressively prunes
 +  memory is continuously edited, not appended

> Staleness is first-class
 + if memory ≠ reality → memory is wrong
 +  code-derived facts are never stored
 +  index is forcibly truncated

> Isolation matters
 + consolidation runs in a forked subagent
 + limited tools → prevents corruption of main context

> Retrieval is skeptical, not blind
 +  memory is a hint, not truth
 +  model must verify before using

> What they don’t store is the real insight
 +  no debugging logs, no code structure, no PR history
 +  if it’s derivable, don’t persist it

## Media

- photo: https://pbs.twimg.com/media/HEu2icGbEAAvoFI.jpg

## Capture Note

TweetDetail returned complete normal-post text.
