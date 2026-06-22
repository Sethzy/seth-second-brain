---
type: raw_capture
source_type: x
url: https://x.com/nickscamara_/status/2024226351369376211
original_url: https://x.com/nickscamara_/status/2024226351369376211
author: "Nicolas Camara"
handle: nickscamara_
status_id: 2024226351369376211
captured_at: 2026-06-19T21:22:39+08:00
published_at: "Wed Feb 18 20:55:45 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 9
  reposts: 7
  likes: 91
---

# X post by @nickscamara_

## Source

- Original: [https://x.com/nickscamara_/status/2024226351369376211](https://x.com/nickscamara_/status/2024226351369376211)
- Canonical: [https://x.com/nickscamara_/status/2024226351369376211](https://x.com/nickscamara_/status/2024226351369376211)
- Author: Nicolas Camara (@nickscamara_)

## Verbatim Text

Your browser is the bottleneck for OpenClaw

Everyone in the valley has either tried OpenClaw or has a coworker shipping something with it. And one of the first problems people run into is browser automation.

The default setup is to let OpenClaw drive your local browser. It works for a few workflows, but the costs show up quickly: you’re putting an agent in the same environment as your real browsing state, enabling a massive security flaw and the moment you try to run a few sessions in parallel your machine becomes the bottleneck; RAM spikes, the agent slows down, runs get flaky.

We built Browser Sandbox in Firecrawl because we kept hitting that same ceiling: local browsers behave like dev tooling, not infrastructure.

Browser Sandbox moves that work into a secure, remote, disposable browser environment. No local Chromium installs. No driver setup. agent-browser and Playwright are already there. Your agent can spin up a browser on demand, one session or dozens, without tying the workload to the machine it’s running on.  Your OpenClaw agent can run on a free-tier EC2 instance, a Raspberry Pi, or whatever you’ve got, while the browsing happens elsewhere.

I encourage you to try it out.

# Setting up Firecrawl

Tell your agent to install Firecrawl with 1 command:

> npx -y firecrawl-cli init --browser

This installs the [Firecrawl CLI](https://github.com/firecrawl/cli), pops a browser so you can authenticate in Firecrawl and then installs the skill.

Your agent is now ready to browse the web. Once installed have your OpenClaw agent try it.

Tell your agent:

> “Use Firecrawl Browser Sandbox to open Hacker News and get me the top 5 news of the day and the first 10 comments on each”

Under the hood, the firecrawl browser ... commands use agent-browser interface to execute commands in a secure sandbox. That matters because your agent can issu intent-level commands (“open”, “click”, “fill”, “snapshot”, “scrape”) instead of generating and debugging Playwright code. Playwright is still there if you need it.

What your agent will end up doing looks like this:

firecrawl browser "open https://news.ycombinator.com"
firecrawl browser "snapshot"
firecrawl browser "scrape"
firecrawl browser close

A few mechanics worth calling out:

- Shorthand auto-session: the shorthand form (firecrawl browser "...") will auto-launch a sandbox session if there isn’t one active, so the agent doesn’t need to manage session lifecycle up front.

- agent-browser by default: those quoted commands are sent to agent-browser automatically inside the sandbox.

- Context offloading + Token efficiency: the agent gets back artifacts (snapshot/extracted content) instead of hauling raw DOM/driver logs into the prompt. It also uses the file system to saved fetched pages and interactions, only querying it when needed.

And the best part is you get a reliable full web toolkit. Scrape, search, and browser automation all through a single CLI that your agent already knows how to use.

## X Article Metadata

- Title: Your browser is the bottleneck for OpenClaw
- Preview: Everyone in the valley has either tried OpenClaw or has a coworker shipping something with it. And one of the first problems people run into is browser automation.
The default setup is to let OpenClaw

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
