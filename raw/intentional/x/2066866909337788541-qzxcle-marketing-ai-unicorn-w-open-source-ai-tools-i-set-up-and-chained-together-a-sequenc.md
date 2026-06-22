---
type: raw_capture
source_type: x
url: https://x.com/qzxcle/status/2066866909337788541
original_url: https://x.com/qzxcle/status/2066866909337788541
author: "MW"
handle: qzxcle
status_id: 2066866909337788541
captured_at: 2026-06-20T01:00:00+08:00
published_at: "Tue Jun 16 12:54:06 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 0
  reposts: 0
  likes: 5
---

# X post by @qzxcle

## Source

- Original: [https://x.com/qzxcle/status/2066866909337788541](https://x.com/qzxcle/status/2066866909337788541)
- Canonical: [https://x.com/qzxcle/status/2066866909337788541](https://x.com/qzxcle/status/2066866909337788541)
- Author: MW (@qzxcle)

## Verbatim Text

Marketing AI Unicorn w/ Open-Source AI Tools

I set up and chained together a sequence of skills and agentic workflows that freed up at least 10 hours of manual/menial labor a week. This is a diary of my experience with the open source AI tools that helped our team cut the time it takes to go from 0 to 1 on each edition of OS Field Notes by 98% (which is HUGE).

---

# /last30days

Any newsletter needs news. Sourcing it is one of the most time consuming parts of the workload.

So I tried the /last30days ([https://github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)) repo to research everything new that has happened over the past X days. So instead of manually switching between tabs and platforms, juggling multiple AI tools, monitoring the timeline, and keeping a record of all that I set up an agent in Claude Code that does it for me.

Claude/GPT deep research isn't nearly as good as /last30days. When I try to use Claude's deep research to source and organize the latest news in open-source AI, for example, new policies, new weight releases, new tools, and frameworks, it usually a) takes a good half an hour to complete, and b) responds with a report that has too much irrelevant or outdated information. Then I end up running multiple deep research sessions to get the info I need, which wastes too many tokens. Or, I go online and monitor the timeline, which consumes an exorbitant amount of time and focus.

/last30days is a research engine that fans out across 12 platforms: Reddit, Hacker News, YouTube, GitHub, TikTok, Instagram, Threads, Bluesky, Polymarket, Digg AI-1000, Brave Search, and X.

Then Claude Code takes all that random mass as input and organizes it into a coherent first draft based on user-defined criteria (which in my case is the structure our newsletter follows).

To my surprise, it actually surfaced recent, corroborated events, then put everything together into a decent first draft, which I can instantly pick up and start editing.

So what I did was I asked the engine to research the last 10 days across 10 topic areas: open-weight model releases, multimodal models, reasoning models, agent frameworks, local LLM inference, developer tools, world models, the open weights vs. open source debate, policy and government deals, and enterprise partnerships. Then filter to items that are new and specifically open-source. Bucket into three sections. Write each item in house format. Flag everything that couldn't be verified.

Claude + /last30days went on and mapped the 10 down to 4 broader queries that share subreddits and repos, scoped each one tightly with handle, subreddit, and repo flags, and aligned them to the three output sections. One query for models, one for inference and dev tools, one for agent frameworks, one for policy and partnerships.

In total, it took ~4 minutes for the agents to gallivant in parallel, source the news, and produce a first draft with the core stories and a rough outline.

Now it's time to make it into something more useful...

# /agent-reach

A lot of times the output is too vague. So I need to dive deeper into one piece of news by clicking a bunch of links and going through a whole bunch of sources, often searching for even more links, just to get a more comprehensive understanding of that particular topic.

That's where /agent-reach ([https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)) can pick up the draft and malleate it into something more insightful. For example, make it easier to better understand the quirks of a new open-source model release, or to simply cross-reference facts and claims.

/agent-reach is an open-source tool that lets AI agents read and search web content across platforms without paying API fees. It's installed as an agent skill, so there's no need to memorize commands. So Claude takes as input any specific question like 'Research the KIMI K2.7-CODE benchmark results,' or a looser one like 'Why is Microsoft Scout built on open-source OpenClaw?,' and digs through the web for answers.

For example, it took KIMI's announcement about its new K2.7 model release and enriched it with a bunch of n information.

It does that for every piece of news sourced and drafted by /last30days.

---

# /avoid-ai-writing & /writing-prose-like-a-human-for-agents

After (i) proper research and sourcing all the latest news with /last30days, (ii) drafting the first newsletter with Claude, (iii) deepening each paragraph/piece of news with more info and verifying with /agent-reach, the last step before the draft reaches a human is to de-slop the writing. No one really wants to read the entire thing and trigger every other sentence because the language is too 'AI, not human'.

So I needed something to somewhat decently audit and rewrite the draft to remove AI writing patterns before it reaches our team workspace. I found /avoid-ai-writing and /writing-prose-like-a-human-for-agents and integrated them both into this automation workflow. Here's what it can do:

Writing is very hard to nail with AI. Neither of these adds literary depth to the write-up. /avoid-ai-writing and /writing-prose-like-a-human-for-agents just make it sound less AI, which makes the draft a more pleasant read. And it's good enough, since the goal is to get a good first draft that we can edit properly. This step is the difference between the following two paragraphs describing the same thing:

"UK GOVERNMENT: The European Commission published its updated Open Source Strategy, explicitly addressing open-source AI, the £500K worth of compute for builders, and foundation models as policy-relevant categories. The move comes amid a wider European push on open-source AI, echoing the UK's recent launch of its Open-Source AI Builder Fund and Open-Source AI Developer Board. [ref] [10 JUN 2026]"

vs

"UK GOVERNMENT: The UK government launched a new Open-Source AI Builder Fund, offering over £500K worth of compute to help innovators turn prototypes into AI tools that can improve public services. It also launched an Open-Source AI Developer Board, giving 10 UK-based developers under 30 direct access to government and a stronger role in shaping the country’s AI strategy. [[ref](https://www.gov.uk/government/news/new-backing-for-open-source-ai-builders-data-centre-design-challenge-and-robotics-partnership)] [10 JUN 2026]"

---

# What comes next? AI VidGen.

One of the ways to scale the newsletter is firing the AI slop cannon on X (especially considering its new video-friendly algo), TikTok, Instagram,  and YouTube. I tried to get to know this growth hack better a few months ago and it went well, but it's still far too dependent on human-in-the-loop to fully or even partially automate it in any meaningful way. If you'd like to know more about my experiment, you can read the article below:

[Embedded Tweet: https://x.com/i/status/2035120708154462693]

In short, the farthest I came to automating the pipeline that takes one piece of news out of the final report and makes it into an AI generated video that doesn't feel like a cringy slop is this one:

---

Don't miss this week's OS Field Notes. Sign up at sentient.xyz.

## X Article Metadata

- Title: Marketing AI Unicorn w/ Open-Source AI Tools
- Preview: I set up and chained together a sequence of skills and agentic workflows that freed up at least 10 hours of manual/menial labor a week. This is a diary of my experience with the open source AI tools

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
