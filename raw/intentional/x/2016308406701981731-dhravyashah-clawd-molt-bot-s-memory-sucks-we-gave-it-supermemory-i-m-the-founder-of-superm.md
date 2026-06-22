---
type: raw_capture
source_type: x
url: https://x.com/DhravyaShah/status/2016308406701981731
original_url: https://x.com/DhravyaShah/status/2016308406701981731
author: "Dhravya Shah"
handle: DhravyaShah
status_id: 2016308406701981731
captured_at: 2026-06-19T20:15:49+08:00
published_at: "Wed Jan 28 00:32:40 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 59
  reposts: 72
  likes: 1049
---

# X post by @DhravyaShah

## Source

- Original: [https://x.com/DhravyaShah/status/2016308406701981731](https://x.com/DhravyaShah/status/2016308406701981731)
- Canonical: [https://x.com/DhravyaShah/status/2016308406701981731](https://x.com/DhravyaShah/status/2016308406701981731)
- Author: Dhravya Shah (@DhravyaShah)

## Verbatim Text

Clawd / Molt bot's memory SUCKS. We gave it supermemory.

I'm the founder of supermemory. Clawd/Molt bot is blowing up right now, with many, many use cases. I set it up, too, and have been using it through telegram.

> TLDR: just go to https://supermemory.ai/docs/integrations/clawdbot to set up supermemory for your clawd bot.

However, me and some other friends of mine noticed that it's memory is really bad. It almost feels like... it never wants to utilize it's memory to answer questions.

For such a big and successful project, this sucks. but why? We instantly got to work...

@manthanguptaa did an awesome job breaking down their architecture - https://x.com/manthanguptaa/status/2015780646770323543?s=42 and from that, we know that it heavily relies on tools to reference memory.

The problem with tools - The models aren't trained to use them all the time.

Memory needs to be something that the model can access any time, it should just be fed into the model on every run. However, the current architecture of Molt won't work at all because of this poor memory.

## The fix.

We integrated clawd bot with supermemory - with:

- Automatic recall at all time

- Tools to manually search, forget, get profile, etc.

- /remember and /recall commands

So now, you _always_ know that your clawd bot will have perfect memory.

Now, i can have extremely long conversations with Molt, switch from telegram to whatsapp to slack, and it has all the context about me, synced with supermemory.

This feels magical. You should try it.

If you want to learn more about supermemory, just read this - https://x.com/DhravyaShah/status/2015132693835714909?s=20 


To install supermemory for your clawd bot, go here https://supermemory.ai/docs/integrations/clawdbot

## X Article Metadata

- Title: Clawd / Molt bot's memory SUCKS. We gave it supermemory.
- Preview: I'm the founder of supermemory. Clawd/Molt bot is blowing up right now, with many, many use cases. I set it up, too, and have been using it through telegram. 


TLDR: just go to

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
