---
type: raw_capture
source_type: x
url: https://x.com/mstockton/status/2047885644605608154
original_url: https://x.com/mstockton/status/2047885644605608154
author: "Matt Stockton"
handle: mstockton
status_id: 2047885644605608154
captured_at: 2026-06-11T00:17:42+08:00
published_at: "Sat Apr 25 03:49:20 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 9
  reposts: 6
  likes: 221
---

# X post by @mstockton

## Source

- Original: [https://x.com/mstockton/status/2047885644605608154](https://x.com/mstockton/status/2047885644605608154)
- Canonical: [https://x.com/mstockton/status/2047885644605608154](https://x.com/mstockton/status/2047885644605608154)
- Author: Matt Stockton (@mstockton)

## Verbatim Text

I am fully aligned with companies using Codex or Cowork as their harness and then hooking their data sources to that, with a skills library. If you do this right, your team can get a lot of work done with just slash commands.

It takes a bit of work to dial in the skills, but you can get there. Definitely worth having someone who knows how to design the skills.

But what if you have some proprietary data source you need to hook up? Maybe an internal database or an external service that has an API but no MCP or maybe just a bunch of files you want to expose.

There’s definitely an emerging recipe for this. My flavor is:

- FastMCP python wrappers around API invocations (important to get the context right in tool definitions)
- Deployment on Modal - modal is such a nice service to use. I used it for tons of stuff now
- Auth0 for authentication - def don’t want to build this yourself. 

And you can def get your good friend Claude Code to help you build this all out.

There are emerging building blocks for sure, but you can do these things, and if you have someone who knows what they are doing, it’s very achievable .

## Capture Note

TweetDetail returned complete normal-post text.
