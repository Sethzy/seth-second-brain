---
type: raw_capture
source_type: web
title: "Meet the new Cursor"
url: "https://cursor.com/blog/cursor-3/"
canonical_url: "https://cursor.com/blog/cursor-3/"
vendor_blog: cursor
published_at: 2026-04-02
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Meet the new Cursor
Original URL: https://cursor.com/blog/cursor-3/
Published: 2026-04-02
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [product](/blog/topic/product)

Apr 2, 2026·[product](/blog/topic/product)

# Meet the new Cursor

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fmichael-truell-avatar.jpg&w=48&q=70)

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fsualeh-asif-avatar.jpg&w=48&q=70)

Michael Truell & Sualeh Asif · 10 min read

### Table of Contents

↑

* [What's new in Cursor 3](#whats-new-in-cursor-3)
* [All your agents in one place](#all-your-agents-in-one-place)
* [Run many agents in parallel](#run-many-agents-in-parallel)
* [New UX for handoff between local and cloud](#new-ux-for-handoff-between-local-and-cloud)
* [Go from commit to merged PR](#go-from-commit-to-merged-pr)
* [Building on the best features of Cursor](#building-on-the-best-features-of-cursor)
* [Files for understanding code](#files-for-understanding-code)
* [Integrated browser](#integrated-browser)
* [Plugins on the Cursor Marketplace](#plugins-on-the-cursor-marketplace)
* [The best way to code with AI](#the-best-way-to-code-with-ai)

Software development is changing, and so is Cursor.

In the last year, we moved from manually editing files to working with agents that write most of our code. How we create software will continue to evolve as we enter the [third era of software development](https://cursor.com/blog/third-era), where fleets of agents work autonomously to ship improvements.

We're building toward this future, but there is a lot of work left to make it happen. Engineers are still micromanaging individual agents, trying to keep track of different conversations, and jumping between multiple terminals, tools, and windows.

**We're introducing Cursor 3, a unified workspace for building software with agents.** The new Cursor interface brings clarity to the work agents produce, pulling you up to a higher level of abstraction, with the ability to dig deeper when you want. It's faster, cleaner, and more powerful, with a multi-repo layout, seamless handoff between local and cloud agents, and the option to switch back to the Cursor IDE at any time.

## [#](#whats-new-in-cursor-3)What's new in Cursor 3

When we started building Cursor, we forked VS Code instead of building an extension so we could shape our own surface. With Cursor 3, we took that a step further by building this new interface from scratch, centered around agents.

### [#](#all-your-agents-in-one-place)All your agents in one place

The new interface is inherently multi-workspace, allowing humans and agents to work across different repos.

### [#](#run-many-agents-in-parallel)Run many agents in parallel

Working with agents is now much easier. All local and cloud agents appear in the sidebar, including the ones you kick off from mobile, web, desktop, Slack, GitHub, and Linear.

Cloud agents produce demos and screenshots of their work for you to verify. This is the same experience you get at [cursor.com/agents](https://cursor.com/agents), now integrated into the desktop app.

### [#](#new-ux-for-handoff-between-local-and-cloud)New UX for handoff between local and cloud

We made moving agents between environments really fast.

Move an agent session from cloud to local when you want to make edits and test it on your own desktop. [Composer 2](https://cursor.com/blog/composer-2), our own frontier coding model with high usage limits, is great for iterating quickly.

In the reverse direction, you can move an agent session from local to cloud to keep it running while you're offline, or so that you can move on to the next task. This is especially useful for longer-running tasks that would otherwise get interrupted when you close your laptop.

### [#](#go-from-commit-to-merged-pr)Go from commit to merged PR

The new diffs view allows you to edit and review changes faster with a simpler UI. When you're ready, you can stage, commit, and manage PRs.

## [#](#building-on-the-best-features-of-cursor)Building on the best features of Cursor

Alpha users told us that a lot of what they like about Cursor 3 is the way it combines the best parts of the IDE with more recent capabilities we've shipped in an agent-first interface.

### [#](#files-for-understanding-code)Files for understanding code

Dive deeper anytime by viewing files, and go to definition in the editor with full LSPs.

### [#](#integrated-browser)Integrated browser

Cursor can use the built-in [browser](https://cursor.com/docs/agent/tools/browser) to open, navigate, and prompt against local websites.

### [#](#plugins-on-the-cursor-marketplace)Plugins on the Cursor Marketplace

Browse hundreds of [plugins](https://cursor.com/docs/plugins) that extend agents with MCPs, skills, subagents, and more. Install with one click, or set up your own [team marketplace](https://cursor.com/docs/plugins#team-marketplaces) of private plugins.

## [#](#the-best-way-to-code-with-ai)The best way to code with AI

With Cursor 3, we have the foundational pieces in place—model, product, and runtime—to build more autonomous agents and better collaboration across teams. We will also continue to invest in the IDE until codebases are self-driving.

This won't be the last time the interface for building software changes. More powerful coding models will unlock new interaction patterns. We are excited to continue to build, simplify, and transform Cursor to be the best way to code with AI.

Upgrade Cursor, and type `Cmd+Shift+P -> Agents Window` to try the new interface. Or learn more in our [docs](https://cursor.com/docs/agent/agents-window).

Filed under: [product](/blog/topic/product)

Authors: Michael Truell & Sualeh Asif
