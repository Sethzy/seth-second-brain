---
type: raw_capture
source_type: x
url: https://x.com/dkundel/status/2046297434205430130
original_url: https://x.com/dkundel/status/2046297434205430130
author: "dominik kundel"
handle: dkundel
status_id: 2046297434205430130
captured_at: 2026-06-19T22:03:22+08:00
published_at: "Mon Apr 20 18:38:21 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 11
  reposts: 27
  likes: 511
---

# X post by @dkundel

## Source

- Original: [https://x.com/dkundel/status/2046297434205430130](https://x.com/dkundel/status/2046297434205430130)
- Canonical: [https://x.com/dkundel/status/2046297434205430130](https://x.com/dkundel/status/2046297434205430130)
- Author: dominik kundel (@dkundel)

## Verbatim Text

How I Stopped Needing to Explain Things to Codex

Last week we launched a series of new features in Codex including computer use, 90+ new plugins and experimental support for memories.

[Embedded Tweet: https://x.com/i/status/2044827705406062670]

Today we launched a research preview of Chronicle. Chronicle augments your memories with context from your screen to learn the tools you use beyond Codex and how you work.

[Embedded Tweet: https://x.com/i/status/2046288243768082699]

This combination has drastically changed how I work with Codex. I don’t have to package every bit of context before I ask for help. With Chronicle and memories, Codex can pick up more of the related context and sometimes catch details I would have missed

## My setup

Beyond the Codex app features above I also have a vault similar to @karpathy 's [LLM knowledge base](https://x.com/karpathy/status/2039805659525644595). I have several automations running in this vault.

- I have an automation that runs several times a day to ingest the latest context from my Gmail, Calendar, Slack and Google Drive to stay up-to-date with what I’m working on and connect context.

- I have a thread automation that runs on my “Chief of Staff” thread that posts todos twice a day. I also use this thread to communicate with my vault in most cases. It’s an infinite thread that gets auto compacted

I use this on top of memories to have a place for me to explicitly bring together topics and have a place for Codex to make sense of more long running projects.

Codex has learned through memories that it can rely on this vault as a way to learn more but then still treats sources like plugins as more definitive sources.

## Codex can figure it out

One thing Codex has been long good at is navigating large codebases to understand implied context about the project. It tends to do its “homework” before diving into making changes in an unknown codebase.

Codex treats other context in the same way. If it realizes it’s missing some context and has the right tools it will go and get that context before diving in. That’s where memories, Chronicle and plugins come in.

Over time, just like a colleague, it learned that “message Romain” means to DM my colleague @romainhuet on Slack or that the “docs draft” refers to the Google Doc that I’ve been editing recently on my screen. 

So a quick “sync with the latest docs draft changes and message Romain when you are done” thread in our developer website repo results in Codex:

- Finding the right document based on memory

- Using the Google Drive plugin to read the draft

- Making the right updates to the markdown

- Ensuring the build passes

- Using GitHub to send a PR

- Sending the right Romain a DM on Slack with the PR link

No need for me to agonize over painstakingly explaining Codex what to do.

## No more mental overhead

Once Codex starts having more context of what you are working on, jumping into new tasks is significantly easier as it drops all mental overhead.

If I ask Codex to create a new project it uses vite because that’s how I normally start projects. If I ask Codex to start a new doc to coordinate on a launch, it knows to create a Google Doc and not a markdown file. When I ask it to check the feedback channel for bugs and fix them, Codex knows which Slack channel I’m referring to. And when it runs into a common issue during a project, it knows how I previously debugged it and tries the same.

Over time Codex learns alongside you and starts to use the same tools and workflows as you, so I can talk to Codex the way I would with a colleague and it just figures it out.

> Chronicle is still in a research preview limited to Pro users outside of the EU, UK and Switzerland and comes with some risks. [Check out the developer docs to learn more](https://developers.openai.com/codex/memories/chronicle).

## X Article Metadata

- Title: How I Stopped Needing to Explain Things to Codex
- Preview: Last week we launched a series of new features in Codex including computer use, 90+ new plugins and experimental support for memories.
 
Today we launched a research preview of Chronicle. Chronicle

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
