---
type: raw_capture
source_type: x
url: https://x.com/0xzak/status/2018871985254617295
original_url: https://x.com/0xzak/status/2018871985254617295
author: "zak.eth"
handle: 0xzak
status_id: 2018871985254617295
captured_at: 2026-06-19T19:59:57+08:00
published_at: "Wed Feb 04 02:19:24 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 42
  reposts: 27
  likes: 549
---

# X post by @0xzak

## Source

- Original: [https://x.com/0xzak/status/2018871985254617295](https://x.com/0xzak/status/2018871985254617295)
- Canonical: [https://x.com/0xzak/status/2018871985254617295](https://x.com/0xzak/status/2018871985254617295)
- Author: zak.eth (@0xzak)

## Verbatim Text

openclaw performance optimization playbook:

- add deepseek ($0.14/$1.10) for routine ops vs sonnet ($3/$15) for complex work
- set contextTokens to 120k not 150k, prevents the dreaded freeze when context overflows 200k limit
- build auto-healing watchdog scripts that restart services when they hang
- enable cross-context messaging so your telegram agent can post to slack channels
- backup your config daily, restarts wipe everything without it
- model hierarchy opus for reasoning, sonnet for moderate tasks, deepseek for everything else

or (if i could shill my own project) you can just wait on the next version of gru which automates all of this for you 👀

## Capture Note

TweetDetail returned complete normal-post text.
