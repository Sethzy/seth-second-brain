---
type: raw_capture
source_type: x
url: https://x.com/nityeshaga/status/2017128005714530780
original_url: https://x.com/nityeshaga/status/2017128005714530780
author: "Nityesh"
handle: nityeshaga
status_id: 2017128005714530780
captured_at: 2026-06-19T19:59:06+08:00
published_at: "Fri Jan 30 06:49:27 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 48
  reposts: 47
  likes: 635
---

# X post by @nityeshaga

## Source

- Original: [https://x.com/nityeshaga/status/2017128005714530780](https://x.com/nityeshaga/status/2017128005714530780)
- Canonical: [https://x.com/nityeshaga/status/2017128005714530780](https://x.com/nityeshaga/status/2017128005714530780)
- Author: Nityesh (@nityeshaga)

## Verbatim Text

How We Built an AI Project Manager Using Claude Code

Claude Code for non-technical work is going to sweep the world by storm in 2026. This is how we built Claudie, our internal project manager for the consulting business. This process provides a great peek into my role as an applied AI engineer.

My Role

I'm an applied AI engineer at @every. My job is to take everything we learn about AI — from client work, from the industry, from internal experiments — and turn it into systems that scale. Curriculum, automations, frameworks. I turn the insights clients give us on discovery calls to curriculum that designers can polish into final client-ready materials. When there's a repetitive task across sales, planning, or delivery, I build the automation, document it, and train the internal team to use.

The highest-value internal automation I've built so far is the one I'm about to tell you about.

What We Needed to Automate

Every Consulting runs on Google Sheets. Every client gets a detailed dashboard — up to 12 tables per sheet — tracking people, teams, sessions, deliverables, feedback, and open items. Keeping these sheets accurate and up-to-date is genuinely a full person's job.

@NataliaZarina, our consulting lead, was doing that job on top of 20 other things. She's managing client relationships, running sales, making final decisions on scope and delivery — and also manually updating dashboards, cross-referencing emails and calendar events, and keeping everything current. It was the work of two people, and she was doing both.

So I automated the second person.

Step 1: Write a Job Description

The first thing I did was ask Natalia to write a job description. Not for an AI agent — for a human. I asked her to imagine she's hiring a project manager: what would she want this person to do, what qualities would they have, what would be an indicator of them succeeding in their role, and everything else you'd put in a real job description.

See screenshot 1.

Once I had this job description, I started thinking about how to turn it into an agent flow. That framing — treating it like hiring a real person — ended up guiding every architectural decision we made. More on that later.

Step 0: Build the Tools

Before any of the agent work could happen, we needed Claude Code to be able to access our Google Workspace. That's where the consulting business lives — Gmail, Calendar, Drive, Sheets.

Google does not have an official MCP server for their Workspace tools. But here's something most people don't know: MCP is simply a wrapper on top of an API. If you have an API for something, you basically have an MCP for it. I used Claude Code's MCP Builder skill — I gave it the Google Workspace API and asked it to build me an MCP server, and it did.

Once it was confirmed that Claude Code could work with Google Sheets, that was the biggest unknown resolved, and we knew it would be able to do the work we needed.

Version 1: Slash Commands

Now it was time for context engineering. The first thing we tried was to create a bunch of slash commands — simple instructions that tell Claude what to do for each piece of work.

This treated slash commands as text expanders, which is what they are, but it didn't work. It failed for one critical reason: using MCP tools to read our data sources and populate our sheets was very expensive in terms of context. By the time the agent was able to read our data sources and understand what was needed, it would be out of context window. We all know what that does to quality — it just drops drastically.

So that didn't work.

Version 2: Orchestrator and Sub-Agents

This is also exactly when Anthropic released the new Tasks feature. We decided the new architecture would work by having our main Claude be the orchestrator of sub-agents, creating tasks that each get worked on by one sub-agent.

But this ran into another unexpected problem. The main Claude would have its context window overwhelmed when it started 10 or more sub-agents in parallel. Each sub-agent would return a detailed report of what they did, and having so many reports sent to the orchestrator at the same time would overwhelm its context window.

For example, our very first tasks launch data investigation agents which look at our raw data sources and create a detailed report about what has happened with a client over a specific period of time, based on a particular source like Gmail or Calendar. The output of these sub-agents needs to be read by all the sub-agents down the line — up to 35 of them. There would definitely be a loss in signal if it was the job of the main orchestrator to pass all required information between sub-agents.

The Fix: A Shared Folder

So we made one little change. We made every sub-agent output their final report into a temp folder and tell the orchestrator where to find it. Now the main Claude reads reports as it sees fit, and every downstream sub-agent can read the reports from earlier phases directly.

This totally solved the problem. And it also improved communication between sub-agents, because they could read each other's full output without the orchestrator having to summarize or relay anything.

See screenshot 2.

Version 3: From Skills to a Handbook

With the orchestration working, I initially created separate skills for each specific piece of work — gather-gmail, gather-calendar, check-accuracy, check-formatting, and so on. Eleven skills in total. Each sub-agent would read the skill it needed and get all the context for its task.

This worked, but it was ugly. These were very specific, narrow skills, and it created all sorts of fragility in the system. Not to mention that it was difficult for even the humans to read and maintain.

That's when the job description framing came back around. We started by treating this like hiring a real person. We wrote them a job description. So what do you do once you've actually hired someone? You give them an onboarding handbook — a document that covers how you approach things on your team and tells them to use it to get the job done, all aspects of their job.

So that's what we built. One single project management skill that contains our entire handbook, organized into chapters:

• Foundation — who we are, the team, our tools and data sources, when to escalate, data accuracy standards
• Daily Operations — how to gather data from all our sources
• Client Dashboards — how the dashboards are structured, what the master dashboard tracks, how to run quality checks
• New Clients — how to onboard a new client and set up their dashboard from scratch

Now when a sub-agent spins up, it reads the foundation chapters first (just like a new hire would), then reads the chapters relevant to its specific task. The handbook replaced eleven fragmented skills with one coherent source of truth.

Here's what the final architecture looks like: See screenshot 4.

What This Felt Like

This was the most exhilarating work I've done in two weeks, and it was all of the things at once.

Working with @NataliaZarina was the most important part. We were on calls for hours, running Claude Code sessions on each of our computers and trading inputs. She has the taste — she knows what the dashboards should look like, what the data should contain, what quality means for our clients. I have the AI engineering. Working together on this was genuinely exciting.

Then there's the speed. We went through three major architectural generations in a span of two weeks. Everything was changing so fast. And what was actually the most exciting was how hard we were driving Claude Code. I've been using Claude Code for programming for months, but I was not driving it this hard before. This last couple weeks, I was consistently running out of my usage limits. In fact, both Natalia and I were running out of our combined usage limits on the ultimate max plans on multiple days. When you're consuming that much AI inference, you can imagine how fast things are moving. And that was just exciting as fuck.

This was also a completely novel problem. Applied AI engineering as a discipline is still new, and this was the first real big shift in how I think about it.

Why Now, and Why 2026

Here's why I opened with the claim that Claude Code for non-technical work will sweep the world in 2026.

We realized that if you give Claude Code access to the tools you use as a non-technical person and do the work to build a workflow that covers how you actually use those tools, that is all you need. That's how non-technical work works.

The reason this hasn't been done until now is that we were running Claude Code at its limits. This would not have been possible with a previous version of the AI or a previous version of Claude Code. We're literally using the latest features and the latest model. It requires reasoning through and understanding of the underlying tools and how to operate them, along with planning capabilities and context management capabilities that did not exist even six months ago.

But now they do. And we're only in January.

Every piece of the stack that made this possible is brand new:

• MCP Builder skill — I built our own Google Workspace MCP server by asking Claude Code to use the Google Workspace API. That was not possible before Anthropic released MCP Builder on Oct 16, 2025

• Opus 4.5 — Its reasoning and planning capabilities made the entire orchestration possible. The agent needs to understand complex sheet structures, figure out what data goes where, and coordinate across dozens of sub-agents. Released Nov 24, 2025.

• The Tasks feature — Sub-agent orchestration through Tasks made Version 2 and 3 possible at all. This was released Jan 23, 2026.

That's why I'm saying Claude Code for non-technical work will sweep 2026. The building blocks just arrived.

## Quoted Post

- URL: https://x.com/NataliaZarina/status/2017012404907892751
- Author: Natalia (@NataliaZarina)

We just brought on a new project manager for @every, an agent called Claudie.

The job description is a https://t.co/HdKYJTtSdj file. It pulls from Gmail, Drive, Calendar & meeting notes into a real-time client dashboard. Custom skills & tasks enforce quality.

@nityeshaga  & I built it over the past 2 weeks because managing clients with hundreds of employees across multiple teams was drowning us in manual work.

Setup for our latest client took Claudie 30 min & would've taken us 5 hrs.

Welcome to the team!

## Media

- photo: https://pbs.twimg.com/media/G_5F8IhbUAE-6i2.png
- photo: https://pbs.twimg.com/media/G_5GOgVboAA_RAP.jpg
- photo: https://pbs.twimg.com/media/G_5GZysaIAAFj9B.png

## Capture Note

TweetDetail returned complete normal-post text.
