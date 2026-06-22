---
type: raw_capture
source_type: x
url: https://x.com/0xzak/status/2021736621264019839
original_url: https://x.com/0xzak/status/2021736621264019839
author: "zak.eth"
handle: 0xzak
status_id: 2021736621264019839
captured_at: 2026-06-19T20:18:20+08:00
published_at: "Thu Feb 12 00:02:27 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 105
  reposts: 98
  likes: 1563
---

# X post by @0xzak

## Source

- Original: [https://x.com/0xzak/status/2021736621264019839](https://x.com/0xzak/status/2021736621264019839)
- Canonical: [https://x.com/0xzak/status/2021736621264019839](https://x.com/0xzak/status/2021736621264019839)
- Author: zak.eth (@0xzak)

## Verbatim Text

My Anthropic bill for the past 2 weeks has been insane and I've been desperately trying to figure out how to cut costs. I think I finally figured out how to cut it by 10x, so I hope this works. 

Most agent tasks are janitorial. Reading files, checking status, formatting output, answering "what time is it in Tokyo?" or "why is ETH price down so bad?" This stuff doesn't require a $15/M model.

The fix is hierarchical routing based on task complexity:

- Routine (80%) > DeepSeek at $0.14/M
File ops, status checks, simple Q&A, formatting

- Moderate (15%) > Sonnet at $3/M
Code, summaries, drafts, light analysis

- Hard (5%) > Opus at $15/M
Debugging, architecture, multi-step reasoning

$225/month on pure Opus vs $19/month with hierarchy.

Packaged this into an agent skill that teaches your AI to classify tasks and route them to the cheapest model that can handle them. 28 tests, works with OpenClaw, Claude Code, or any agent system. Boom. Check it out and lmk if it saves you money without degrading your output.

https://t.co/3aP4MTPKhv

## Capture Note

TweetDetail returned complete normal-post text.
