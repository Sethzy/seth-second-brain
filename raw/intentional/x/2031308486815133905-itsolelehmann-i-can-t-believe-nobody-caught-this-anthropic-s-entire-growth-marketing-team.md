---
type: raw_capture
source_type: x
url: https://x.com/itsolelehmann/status/2031308486815133905
original_url: https://x.com/itsolelehmann/status/2031308486815133905
author: "Ole Lehmann"
handle: itsolelehmann
status_id: 2031308486815133905
captured_at: 2026-06-19T21:43:19+08:00
published_at: "Tue Mar 10 09:57:37 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 307
  reposts: 811
  likes: 9112
---

# X post by @itsolelehmann

## Source

- Original: [https://x.com/itsolelehmann/status/2031308486815133905](https://x.com/itsolelehmann/status/2031308486815133905)
- Canonical: [https://x.com/itsolelehmann/status/2031308486815133905](https://x.com/itsolelehmann/status/2031308486815133905)
- Author: Ole Lehmann (@itsolelehmann)

## Verbatim Text

i can't believe nobody caught this.

Anthropic's entire growth marketing team was just ONE PERSON

(for 10 months, confirmed)

a single non-technical person ran paid search, paid social, app stores, email marketing, and SEO for the $380B company behind claude

here's exactly how one human is doing the job of a full marketing team:

it starts with a CSV.

1. he exports all his existing ads from his ad platforms along with their performance metrics (click-through rates, conversions, spend, etc)

2. feeds the whole file into claude code

3. and tells it to find what's underperforming.

claude analyzes the data, flags the weak ads, and generates new copy variations on the spot

this is where he gets clever:

he then splits the work into 2 specialized sub-agents:

1. one that only writes headlines (capped at 30 characters)

2. and one that only writes descriptions (capped at 90 characters).

each agent is tuned to its specific constraint so the quality is way higher than cramming both into a single prompt

so now he's got hundreds of fresh headlines and descriptions.

but that's just the text.

he still needs the actual visual ad creative, the images and banners that go on facebook, google, etc.

so he built a figma plugin that:

1. takes all those new headlines and descriptions
2. finds the ad templates in his figma files
3. and automatically swaps the copy into each one.

up to 100 ready-to-publish ad variations generated at half a second per batch.

what used to take hours of duplicating frames and copy-pasting text by hand

so now the ads are live.

the next question is which ones are actually working.

for that he built an MCP server (basically a custom integration that lets claude talk directly to external tools) connected to the meta ads API.

so he can ask claude things like:

• "which ads had the best conversion rate this week"
• or "where am i wasting spend"

and get real answers from live campaign data without ever opening the meta ads dashboard

and the part that ties it all together and closes the loop:

he set up a memory system that logs every hypothesis and experiment result across ad iterations.

so when he goes back to step one and generates the next batch of variations...

claude automatically pulls in what worked and what didn't from all previous rounds.

the system literally gets smarter every cycle.

that kind of systematic experimentation across hundreds of ads would normally need a dedicated analytics person just to track

the numbers from the doc:

ad creation went from 2 hours to 15 minutes. 10x more creative output.

and he's now testing more variations across more channels than most full marketing teams

a $380 billion company.

and their entire growth marketing operation (not GTM) = just one person and claude code lol

truly unbelievable

## Media

- photo: https://pbs.twimg.com/media/HDCoTeCaMAEG0Z1.png

## Capture Note

TweetDetail returned complete normal-post text.
