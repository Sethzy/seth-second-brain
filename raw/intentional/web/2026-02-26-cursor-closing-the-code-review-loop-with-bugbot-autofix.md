---
type: raw_capture
source_type: web
title: "Closing the code review loop with Bugbot Autofix"
url: "https://cursor.com/blog/bugbot-autofix/"
canonical_url: "https://cursor.com/blog/bugbot-autofix/"
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

# Closing the code review loop with Bugbot Autofix
Original URL: https://cursor.com/blog/bugbot-autofix/
Published: 2026-02-26
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [product](/blog/topic/product)

Feb 26, 2026·[product](/blog/topic/product)

# Closing the code review loop with Bugbot Autofix

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjon-kaplan.png&w=48&q=70)

Jon Kaplan · 3 min read

Agents are now tackling more ambitious tasks, generating thousands of lines of code, and [controlling their own computers](/blog/agent-computer-use) to demo their work. Today, we're extending these capabilities to Bugbot, our code review agent.

Bugbot can now find and automatically fix issues in PRs. Bugbot Autofix spawns cloud agents that work independently in their own virtual machines to test your software. Over 35% of Bugbot Autofix changes are merged into the base PR.

Autofix is now out of beta and available to all Bugbot users. Once enabled, the PRs Bugbot reviews will include proposed fixes to give you a jumpstart on code review.

## [#](#resolving-more-bugs-per-pr)Resolving more bugs per PR

We’ve [continued to](/blog/building-bugbot) [invest](https://cursor.com/blog/building-bugbot) in Bugbot’s effectiveness at identifying issues while optimizing for bugs that get fixed.

The average number of issues identified per run has nearly doubled in the last six months, while the resolution rate (i.e., percentage of bugs resolved by users before the PR is merged) has increased from 52% to 76%. This means Bugbot is catching more bugs and flagging fewer false positives.

![Bugbot's resolution rate has increased from 52% to 76% while the average number of issues identified per run has nearly doubled.](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fchart-bugbot-autofix-r4.png&w=1920&q=70)![Bugbot's resolution rate has increased from 52% to 76% while the average number of issues identified per run has nearly doubled.](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fchart-bugbot-autofix-dark-r4.png&w=1920&q=70)

## [#](#whats-next)What's next

Bugbot Autofix is an early example of agents running automatically based on an event like PR creation. Next, we are working on giving teams the ability to configure custom automations for workflows beyond code review.

We’re also focused on enabling Bugbot to verify its own findings, conduct deep research on complex issues, and continuously scan your codebase to catch and resolve bugs.

Get started by enabling Bugbot Autofix in your [Bugbot dashboard](https://cursor.com/dashboard/bugbot). Or learn more in our [docs](https://cursor.com/docs/bugbot#autofix).

Filed under: [product](/blog/topic/product)

Author: Jon Kaplan
