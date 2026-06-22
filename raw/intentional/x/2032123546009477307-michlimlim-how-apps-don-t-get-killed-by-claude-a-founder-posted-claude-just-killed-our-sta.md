---
type: raw_capture
source_type: x
url: https://x.com/michlimlim/status/2032123546009477307
original_url: https://x.com/michlimlim/status/2032123546009477307
author: "Michelle Lim"
handle: michlimlim
status_id: 2032123546009477307
captured_at: 2026-06-19T21:43:45+08:00
published_at: "Thu Mar 12 15:56:23 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 5
  reposts: 6
  likes: 87
---

# X post by @michlimlim

## Source

- Original: [https://x.com/michlimlim/status/2032123546009477307](https://x.com/michlimlim/status/2032123546009477307)
- Canonical: [https://x.com/michlimlim/status/2032123546009477307](https://x.com/michlimlim/status/2032123546009477307)
- Author: Michelle Lim (@michlimlim)

## Verbatim Text

How apps don’t get killed by Claude

A founder posted "Claude just killed our startup" last month. 8.4k likes. I build an application (@tryflint). Here’s what I’m doing about it.

My assumption: Claude becomes the desktop. And your job is to be indispensable to it.

(Disclaimer: "Claude" here is interchangeable with Claude Code, Claude Cowork, ChatGPT, Codex, or whatever wins. The principle holds.)

What I’m doing:

1. Convert your app into CLIs, APIs, and MCP.

Make it trivial for Claude (and every AI app really) to connect to your product. For Flint (autonomous websites), we started with a create_page API. Already seeing early signs of aggressive agentic usage. One user created a Slackbot for their reps to create account-based pages. Another is hooking it up with their Reddit commenting Clawdbot. You want Claude reaching for your product like a tool, not replacing it like a feature.

2. Build a human control surface for Claude’s intermediate work.

Claude will produce work that needs human judgment. Give people a tool to intervene, then send the corrected output back to Claude. @paper is winning because it lets designers tweak Claude-generated UI using a visual editor. Verbal feedback on frontend code is lossy. Close that loop and you become load-bearing infrastructure in the workflow.

3. Let Claude sign up for your product.

Make the onboarding instant. Claude and Claude users are trigger-happy. Friction kills. @Remotion got me quick because I told Claude to make 12 product demo videos and it finished in minutes. If Remotion needed a sales call, I would've moved on. So would my agent.

4. Build proprietary data with autonomous improvement loop.

This is a real moat. LinkedIn owns professional identity. Pave owns compensation data.  To top it off, the products incentivize users to keep feeding them.

For Flint, we're building the best dataset on how landing pages actually perform for your customer. Every page is an experiment. We run continuous A/B tests across thousands of them, and that flywheel tells us exactly what converts, and it also improves the pages automatically. Claude can generate a landing page. It cannot tell you whether it will convert.

What I’m bearish on:

1. Building your own workflow/automation layer

Everyone is shipping "Workflows" or "Automations": basically Zapier inside their product. With Claude Code now offering Scheduled Tasks, the case for configuring a custom agent inside your walled garden keeps collapsing.

2. Worrying about your coding agents

We have agents inside Flint that run campaigns and build landing pages. I stopped worrying about them. Claude and Codex keep getting better automatically. I built ours in OpenCode (which uses both interchangeably) and moved on. This is a treadmill you don't need to run.

3. Seat based pricing

I’m not optimizing hard on seat-based pricing. The world is moving toward usage-based pricing. One "seat" runs 10,000 agent actions a month. Design for that now.

Make your app irresistible

Amazon killed merchants selling commodity products. Left alone the ones with brands, proprietary inventory, relationships it couldn't replicate. Apple killed thin wrappers. Left alone the apps with proprietary data, network effects, and workflows too complex to absorb.

Claude will do the same. The graveyard won't be full of Claude-integrated companies. It'll be full of ones that thought being a standalone app was enough.

Every app that survives will survive for the same reason: Claude can use it, but can't replace it.

You're not building software. You're building a Claude skill. Make it load-bearing.

(This advice has a 6-month shelf life. Maybe less.)

## X Article Metadata

- Title: How apps don’t get killed by Claude
- Preview: A founder posted "Claude just killed our startup" last month. 8.4k likes. I build an application (@tryflint). Here’s what I’m doing about it. 
My assumption: Claude becomes the desktop. And your job

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
