---
type: raw_capture
source_type: web
title: "Better AI models enable more ambitious work"
url: "https://cursor.com/blog/better-models-ambitious-work/"
canonical_url: "https://cursor.com/blog/better-models-ambitious-work/"
vendor_blog: cursor
published_at: 2026-04-15
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Better AI models enable more ambitious work
Original URL: https://cursor.com/blog/better-models-ambitious-work/
Published: 2026-04-15
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [research](/blog/topic/research)

Apr 15, 2026·[research](/blog/topic/research)

# Better AI models enable more ambitious work

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fluke-melas-kyriazi.jpg&w=48&q=70)

Luke Melas-Kyriazi · 4 min read

[![](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/economics-research-blog-og.png)](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/suproteem-cover-image.mp4)

### Table of Contents

↑

* [Media, software, and finance lead the way](#media-software-and-finance-lead-the-way)
* [A shift right in complexity](#a-shift-right-in-complexity)
* [A changing task distribution](#a-changing-task-distribution)
* [Expanding economic activity](#expanding-economic-activity)

We are interested in understanding how improvements in AI models change how developers work. In particular, to what extent do developers perform more of the tasks they were already doing, and to what extent do better models enable work that was out of reach before?

To answer that question, we partnered with Professor Suproteem Sarkar from the University of Chicago Booth School of Business to study the work habits of developers at 500 companies using Cursor, from July 2025 through March 2026. This eight-month window included the releases of Opus 4.5 and GPT-5.2, two models that delivered step-change advances in AI coding capability.

[Our paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6578939) finds that better AI leads to greater AI demand. This is consistent with a Jevons-like effect, where gains in efficiency increase total consumption rather than reducing it. AI usage, defined as average weekly messages per user, increased 44% during the study period.

![Average weekly messages per user over the study period, showing a 44% increase](/marketing-static/_next/image?url=%2Fmarketing-static%2Fblog%2Fbetter-ai-models-ambitious-work%2Fusage-increased-light.png&w=1920&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)![Average weekly messages per user over the study period, showing a 44% increase](/marketing-static/_next/image?url=%2Fmarketing-static%2Fblog%2Fbetter-ai-models-ambitious-work%2Fusage-increased-dark.png&w=1920&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)

The increase wasn’t immediate or uniform. We observed that developers first used better models to do more work of similar complexity, and only later began taking on more complex tasks. Moreover, the shift was especially concentrated in industries like finance, media, and advertising, where competitive forces and greenfield opportunities may have spurred adoption.

## [#](#media-software-and-finance-lead-the-way)Media, software, and finance lead the way

Usage increased in every sector we studied, but the gains were larger in some industries than others. In particular, media and advertising saw the biggest jump, with a 54% increase in messages per user, followed by software and developer tools (+47%) and finance and fintech (+45%).

We hypothesize that in finance, better AI can create an arms-race dynamic, where once one firm uses AI to gain a trading edge, others face competitive pressure to follow. In media and advertising, the mechanism may be different, with more capable models expanding greenfield opportunities that firms take advantage of.

![Messages per user by sector, with media and advertising, software and developer tools, and finance and fintech highlighted](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fuploads%2Fchicago-in-media-software-finance-light.jpg&w=1920&q=70)![Messages per user by sector, with media and advertising, software and developer tools, and finance and fintech highlighted](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fuploads%2Fchicago-in-media-software-finance-dark.jpg&w=1920&q=70)

## [#](#a-shift-right-in-complexity)A shift right in complexity

Initially, developers did more of the same with the improved AI models, but after a lag of 4–6 weeks, we observed that they began using models for more complex tasks. Overall, the number of “low complexity” messages increased 22% over the study period, while the number of “high complexity” messages grew 68%, with most of that growth occurring during the last six weeks.

In the paper, we hypothesize that the delay reflects both the time it takes developers to discover what a better model can do, and the need for firms to reorient their workflows around new capabilities.

![Low- and high-complexity message volume over time, showing stronger growth in high complexity after a lag](/marketing-static/_next/image?url=%2Fmarketing-static%2Fblog%2Fbetter-ai-models-ambitious-work%2Fusage-shifted-light.png&w=1920&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)![Low- and high-complexity message volume over time, showing stronger growth in high complexity after a lag](/marketing-static/_next/image?url=%2Fmarketing-static%2Fblog%2Fbetter-ai-models-ambitious-work%2Fusage-shifted-dark.png&w=1920&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)

## [#](#a-changing-task-distribution)A changing task distribution

As AI improves at code generation, the developer’s job shifts to managing that output. This change shows up clearly in our data, where we can measure how usage evolves across task categories. The largest increases were in documentation (+62%), architecture (+52%), code review (+51%), and learning (+50%), while more self-contained tasks like UI/styling grew far less (+15%).

This indicates that as AI-generated code expands codebase size, the need to document, understand, and review that code grows in proportion. Larger and faster-moving codebases also increase the complexity of managing how it all fits together, which may explain the sharp growth in cross-system tasks like architecture and deployment. More capable models may also make developers more willing to use agents for these cross-system tasks.

![Task categories showing larger growth in documentation, architecture, code review, and learning than in UI and styling](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fuploads%2Fchicago-tasks-with-dependencies-light.jpg&w=1920&q=70)![Task categories showing larger growth in documentation, architecture, code review, and learning than in UI and styling](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fuploads%2Fchicago-tasks-with-dependencies-dark.jpg&w=1920&q=70)

## [#](#expanding-economic-activity)Expanding economic activity

A central question around AI adoption is whether it merely facilitates existing work, or also opens up new productive opportunities. Our study indicates that it does both, but that expansion may eventually be the bigger story.

[Read the full paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6578939).

Filed under: [research](/blog/topic/research)

Author: Luke Melas-Kyriazi
