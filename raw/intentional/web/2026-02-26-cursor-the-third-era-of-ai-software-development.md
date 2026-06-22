---
type: raw_capture
source_type: web
title: "The third era of AI software development"
url: "https://cursor.com/blog/third-era/"
canonical_url: "https://cursor.com/blog/third-era/"
vendor_blog: cursor
published_at: 2026-02-26
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# The third era of AI software development
Original URL: https://cursor.com/blog/third-era/
Published: 2026-02-26
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [ideas](/blog/topic/ideas)

Feb 26, 2026·[ideas](/blog/topic/ideas)

# The third era of AI software development

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fmichael-truell-avatar.jpg&w=48&q=70)

Michael Truell · 4 min read

[![](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/og/blog-third-era-5a-20260304-072622-1200.gif)](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/og/blog-third-era-5a-20260304-072622-1200.mp4)

### Table of Contents

↑

* [From Tab to agents](#from-tab-to-agents)
* [Cloud agents and artifacts](#cloud-agents-and-artifacts)
* [The shift is underway inside Cursor](#the-shift-is-underway-inside-cursor)

When we started building Cursor a few years ago, most code was written one keystroke at a time. Tab autocomplete changed that and opened the first era of AI-assisted coding.

Then agents arrived, and developers shifted to directing agents through synchronous prompt-and-response loops. That was the second era. Now a third era is arriving. It is defined by agents that can tackle larger tasks independently, over longer timescales, with less human direction.

As a result, Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software. This factory is made up of fleets of agents that they interact with as teammates: providing initial direction, equipping them with the tools to work independently, and reviewing their work.

Many of us at Cursor are already working this way. More than one-third of the PRs we merge are now created by agents that run on their own computers in the cloud. A year from now, we think the vast majority of development work will be done by these kinds of agents.

### [#](#from-tab-to-agents)From Tab to agents

Tab excelled at identifying where low-entropy, repetitive work could be automated. For nearly two years, it produced significant leverage.

Then the models improved. Agents could hold more context, use more tools, and execute longer sequences of actions. Developer habits began to shift, slowly through the summer, then rapidly over the last few months with the releases of Opus 4.6, Codex 5.3, and Composer 1.5.

The transformation has been so complete that today, most Cursor users never touch the tab key. In March 2025, we had roughly 2.5x as many Tab users as agent users. Now, that is flipped: we now have 2x as many agent users as Tab users.

![Agents become mainstream and then the default](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fthird-era-chart-r5.png&w=3840&q=70)![Agents become mainstream and then the default](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fthird-era-chart-dark-r5.png&w=3840&q=70)

Agent usage in Cursor has grown over 15x in the last year.

But already this shift is giving way to something bigger. The Tab era lasted nearly two years. The second era, in which most work is done with synchronous agents, may not last one.

### [#](#cloud-agents-and-artifacts)Cloud agents and artifacts

Compared to Tab, synchronous agents work further up the stack. They handle tasks that require context and judgment, but still keep the developer in the loop at every step. But this form of real-time interaction, combined with the fact that synchronous agents compete for resources on the local machine, means it is only practical to work with a few at a time.

Cloud agents remove both constraints. Each runs on its own virtual machine, allowing a developer to hand off a task and move on to something else. The agent works through it over hours, iterating and testing until it is confident in the output, and returns with something quickly reviewable: logs, video recordings, and live previews rather than diffs.

This makes running agents in parallel practical, because artifacts and previews give you enough context to evaluate output without reconstructing each session from scratch. The human role shifts from guiding each line of code to defining the problem and setting review criteria.

### [#](#the-shift-is-underway-inside-cursor)The shift is underway inside Cursor

Thirty-five percent of the PRs we merge internally at Cursor are now created by agents operating autonomously in cloud VMs. We see the developers adopting this new way of working as characterized by three traits:

1. Agents write almost 100% of their code.
2. They spend their time breaking down problems, reviewing artifacts, and giving feedback.
3. They spin up multiple agents simultaneously instead of handholding one to completion.

There is a lot of work left before this approach becomes standard in software development. At industrial scale, a flaky test or broken environment that a single developer can work around turns into a failure that interrupts every agent run. More broadly, we still need to make sure agents can operate as effectively as possible, with full access to tools and context they need.

We think [yesterday's launch](https://cursor.com/blog/agent-computer-use) of Cursor cloud agents is an initial but important step in that direction.

Filed under: [ideas](/blog/topic/ideas)

Author: Michael Truell
