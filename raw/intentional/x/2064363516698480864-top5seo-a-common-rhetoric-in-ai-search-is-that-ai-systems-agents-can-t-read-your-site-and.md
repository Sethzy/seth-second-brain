---
type: raw_capture
source_type: x
url: https://x.com/top5seo/status/2064363516698480864
original_url: https://x.com/top5seo/status/2064363516698480864
author: "David McSweeney"
handle: top5seo
status_id: 2064363516698480864
captured_at: 2026-06-19T23:41:58+08:00
published_at: "Tue Jun 09 15:06:31 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 9
  reposts: 2
  likes: 30
---

# X post by @top5seo

## Source

- Original: [https://x.com/top5seo/status/2064363516698480864](https://x.com/top5seo/status/2064363516698480864)
- Canonical: [https://x.com/top5seo/status/2064363516698480864](https://x.com/top5seo/status/2064363516698480864)
- Author: David McSweeney (@top5seo)

## Verbatim Text

A common rhetoric in AI search is that AI systems/agents "can't read your site" and that you need to serve an "optimized" version.

In fact there was a (very) large acquisition last week for a platform that offers to do this for you.

So does serving an optimized version of your content increase citations? Or is it a load of GEO nonsense? Could it in fact harm your site?

Well, I have my opinions.

But opinions are like... (you know what), so I spent the last week or so building an "agent friendly" API and am currently serving faithful compressed summaries, with optional additional retrieval to selected user agents on a few test domains.

The "agent" gets instructions on how to use the API to request more content (full document, a specific section, search within the page). It can also search across the full site (semantic or keyword). All agent "journeys" are tracked via sessions.

Soon I'll report if:

a) there was any increase/decrease in citations/AI bot activity
b) whether the "agents" interacted with the API after getting the initial summary (so far, none of them have, but it's been live for less than 24 hours)
c) whether any of them requested the full API instructions
d) lots more... (already have some myths debunked)

On that note, if you have a site you don't mind testing things on (this to my mind isn't without risk) then let me know.

If you're a QueryBurst subscriber you actually have access to it already. But it's heavily caveated with "this is experimental - we recommend running on a test domain".  I wouldn't go gung-ho and add it to your main site at the moment...

...although with that being said, for full dogfooding, one of the test domains is QueryBurst's marketing site itself.

Note: while in testing I may experiment A/B test various content formats for the initial served summary (currently it's a highly compressed 200-300 tokens). Although at all times it will be a faithful compression of what's actually on the page with nothing new injected, other than the API instructions.

Technical notes:

1. Requests are intercepted at the edge via a Cloudflare Worker. Known AI user-agents (ChatGPT-User, Claude-User, Perplexity-User etc.) are routed to a backend API that serves a compressed markdown summary (~200-300 tokens) built from the page's existing QueryBurst Site intelligence (key claims, document structure, metadata).

2. The response includes instructions and links for deeper retrieval. Full page content, specific sections by heading, page-scoped search, or site-wide semantic search. Each interaction carries a session ID so we can trace the full agent journey (did it stop at the summary? drill into a section? search for related content?).

3. Static assets are excluded at the Worker level. All responses are served sub-200ms. Human visitors see the normal site, nothing changes for them.

4. The compression is deterministic (no LLM in the serving path). It's pre-computed from our existing Site Intelligence pipeline. Nothing is invented or injected beyond factual assertions already present on the page.

## Media

- photo: https://pbs.twimg.com/media/HKYUCqMXIAAkD3k.jpg
- photo: https://pbs.twimg.com/media/HKYUpV1WQAAnYQF.jpg

## Capture Note

TweetDetail returned complete normal-post text.
