---
type: raw_capture
source_type: x
url: https://x.com/mikenevermiss/status/2080532258960597249
original_url: https://x.com/mikenevermiss/status/2080532258960597249
author: "MIKE"
handle: mikenevermiss
status_id: 2080532258960597249
captured_at: 2026-07-26T15:15:25+08:00
published_at: "Fri Jul 24 05:55:19 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 21
  reposts: 15
  likes: 106
---

# X post by @mikenevermiss

## Source

- Original: [https://x.com/mikenevermiss/status/2080532258960597249](https://x.com/mikenevermiss/status/2080532258960597249)
- Canonical: [https://x.com/mikenevermiss/status/2080532258960597249](https://x.com/mikenevermiss/status/2080532258960597249)
- Author: MIKE (@mikenevermiss)

## Verbatim Text

How to Build and Automate Anything with Claude, Kimi K3, and Beyond

1/8: What You'll Walk Away Knowing

1. The simple loop behind every AI build, and which two steps people usually skip

2. Which AI model to use for which job, Claude, Kimi K3, GPT-5.6, and one free-to-download option, with real prices

3. A full walkthrough that takes a one-paragraph idea to a live website, with the exact words to type

4. How to connect a model to n8n so a real task runs on a schedule without you touching it

5. How to use two models on one project so each one does the part it's actually good at

6. Five specific mistakes that waste hours, and the quick fix for each

## 2/8: How AI Building Actually Works

Every build follows the same five-step loop, no matter which tool you use: you describe what you want (prompt), the AI breaks it into steps (plan), it actually does the work (execute), it checks whether the work is right (check), and if something's off, it fixes it and tries again (fix).

You describe the outcome in plain language. The AI breaks that into steps, sometimes it shows you the steps first, sometimes it just gets moving. Then it takes real action: writing an actual file, calling an actual website, clicking through an actual browser, not just telling you how you could do it yourself. After that, it checks its own work, running a test, loading the page, reading back what it just wrote. If something's broken, it fixes it and loops through again, sometimes without you asking, sometimes because you pointed out what's wrong.

This is the real difference between chatting with an AI and building with one. If a model just explains how to set up a contact form, it hasn't built anything yet. The loop only kicks in once the model can actually touch something, a terminal window, your files, a browser, a direct connection to another app, and actually uses it. That's what separates a tool like Claude Code, Kimi Code, or Codex (all called "agents") from a regular chatbot.

Your job in this loop isn't to write the code yourself. It's to handle two things: the plan and the check. Say clearly what you want before anything runs, glance at the plan if the AI shows you one, and always look at the real result yourself, the actual live page, the actual test output, the actual email that got sent, instead of just trusting what the AI tells you it did. Almost every mistake in section 7 comes down to someone skipping that last check.

## 3/8: Which Model for Which Job

Four models cover almost everything a solo builder needs. Claude, for anything where getting it right matters more than getting it fast. Kimi K3, Moonshot AI's new model released July 16, 2026, for cheap, high-quality output with a huge memory for detail. GPT-5.6 Sol, OpenAI's current top model, for tasks that need to work across several apps at once. DeepSeek V4 Pro, for doing the same simple task over and over as cheaply as possible. Google's Gemini 3.1 Pro is a solid fifth pick if your work already lives inside Google Workspace (Docs, Sheets, Gmail), but it doesn't change anything below.

A quick note on the money: prices below are per million "tokens." Tokens are just small chunks of text, roughly three-quarters of a word each. "Input" is what you feed the model, "output" is what it writes back.

Model

Claude (Sonnet 5 / Opus 4.8)

Real strength

Stays on track through long, multi-step jobs without losing the thread

Real weakness

Most expensive at the top tier ($5 / $25 per million tokens), only works through Anthropic

One task you'd actually hand it

A build inside Claude Code that spans many files and many days

Kimi K3

Real strength

Excellent at building web pages and interfaces, cheap for how good it is, remembers a huge amount at once

Real weakness

Makes up more wrong answers as it gets more confident, and the free downloadable version isn't out until July 27

One task you'd actually hand it

Generating a polished landing page or app screen fast, without paying top dollar

GPT-5.6 Sol

Real strength

Best at handling tasks that span multiple apps on its own, browser, docs, spreadsheets

Real weakness

Just as pricey as Claude ($5 / $30 per million), only works through OpenAI

One task you'd actually hand it

Automating a task that needs to open a browser, fill in a doc, and update a spreadsheet, all unattended

DeepSeek V4 Pro

Real strength

Extremely cheap ($0.44 / $0.87 per million), you can download it and run it yourself for free

Real weakness

Falls behind on the hardest reasoning and multi-step tasks

One task you'd actually hand it

Doing the same small job thousands of times, first drafts, sorting, labeling, anything where price per use matters most

Simple rule of thumb: use Claude when a mistake would actually cost you something and the job takes a while. Use Kimi K3 when you want near-top-tier output without the near-top-tier price, and can live with occasional confident wrong answers. Use GPT-5.6 Sol when the task needs to control multiple apps by itself. Use DeepSeek V4 Pro, or run it yourself, when you're repeating the same cheap task thousands of times.

## 4/8: Build a Website End to End

The idea: a one-page website for a pottery studio. A hero section, a class schedule, a short bio for the instructor, a contact form, and a booking button.

Step 1: Describe it in Claude Design.

Go to claude.ai/design (a newer, test-stage feature, available if you're on a paid Claude plan: Pro, Max, Team, or Enterprise). Type your idea as one paragraph:

Code

Claude Design builds a working first draft you can see and click through right away. Fix it up by leaving comments, editing directly, or using the sliders it gives you for things like spacing and color, just say things like "make the hero image full-width" or "swap the accent color for terracotta." Here's a full walkthrough of the tool in action: Claude Design: First Look + Full Walkthrough.

Step 2: Turn it into a real, live web address.

From inside Claude Design, publish straight to Vercel (a hosting service) for a working web address instantly, no extra software needed. If you'd rather not connect an account, download the project as a .zip file and drag it onto Vercel's upload page instead.

Step 3: Add real functionality with Claude Code.

A simple page is fine until you need the contact form to actually send you an email, or a blog that pulls in real posts. Claude Design can package everything up and hand it straight to Claude Code, Anthropic's tool for developers that lives in a terminal (a plain, text-based command window) instead of a chat window. Open a terminal in your project folder, type claude to start it, and give it your next request in plain English:

Code

Claude Code reads through your files, writes the new code, installs anything it needs, and checks its own work. Link the project to GitHub (a place to store your code online) and Vercel will automatically update your live site every time you save a change, so future edits become as simple as "make this change, save it." Here's a beginner's walkthrough of Claude Code itself: The Ultimate Beginner Guide to Claude Code.

Step 4: Add your own domain name.

In Vercel or Cloudflare's settings, add the domain you own and update a couple of settings they give you, called DNS records, they just tell the internet where your website actually lives. It usually takes a few minutes to a few hours to fully work, and the secure padlock icon (HTTPS) gets added automatically.

That's the Claude-based path from start to finish. Three other tools are worth knowing about for when this specific path isn't the right fit:

- Lovable is the closest all-in-one alternative outside Anthropic's tools, and the option most reviewers recommend for non-technical founders. One click to a live site, and it also connects directly to other AI tools through something called MCP, a way for AI models to plug into outside apps. Watch it in action here: Lovable Beginner Tutorial.

- Bolt.new is the fastest way to get a clickable prototype, no sign-up, works entirely in your browser, but you're stuck with one specific type of backend (the behind-the-scenes part that stores your data) and can't add certain extra code add-ons.

- Replit Agent (its current version is Agent 4) gives you the most complete package if you want a real backend, a real database, and an actual terminal alongside the AI, a good pick if you eventually want to understand the code yourself.

- v0 only makes sense if you're already committed to Next.js and Vercel specifically, a particular web framework and hosting combo. It's narrower on purpose, and its full-app features are newer and less proven than Lovable's or Replit's.

- Cursor isn't a one-shot website builder at all. It's a code editor with AI built in, useful once you already have a codebase and want to edit it file by file, not for going from a blank page to a live site in one go.

## 5/8: Automate a Real Workflow

The goal: automatically draft a weekly roundup post from a few sources, with a real person approving it before it goes live.

Here's how to build this in n8n, a visual automation tool you can run yourself or use through n8n.cloud, step by step. Here's a beginner-friendly demo of connecting Claude to n8n: Claude Code + n8n: Complete Beginners Guide.

Step 1: Set the trigger.

Add a Schedule Trigger, a block that starts the workflow automatically, set to run every Monday at 6:00 AM.

Step 2: Gather your sources.

Add one RSS Feed Read block for each source you follow, RSS just means "get me new posts from this site automatically," then a Merge block to combine them all into one.

Step 3: Write the draft.

Add an AI Agent block, this is n8n's box for "send this to an AI model and get something back." Connect it to your Anthropic account, and give it these instructions:

Code

Step 4: Send it for approval.

Add a Slack block that posts the draft to a private channel: "Weekly roundup ready, reply approve to publish." Follow it with a Wait block that pauses everything until you reply.

Step 5: Publish it.

Once you approve, an HTTP Request block, which just means "send this data to another website automatically," posts the draft to your website's backend as a draft first, so you still get one last look before it's public.

Step 6: Get confirmation.

A final Slack or email message sends you the live link once it's posted.

Two things worth knowing before you build this. First, n8n needs its own separate Anthropic API key (a password-like code from Anthropic that lets other apps use your account) and its own separate bill, your existing Claude subscription doesn't cover it. Second, running n8n yourself on cloud servers costs roughly $300 to $500 a month, unless you use their hosted plan instead.

If building a workflow from scratch sounds like too much, Zapier has its own version of MCP that lets Claude act directly on any of your 9,000-plus connected apps without you setting up the steps ahead of time, better for one-off requests than for something that needs to run the exact same way every week without you. Make.com sits in the middle: easier to learn than n8n, with more visual control over branching decisions, like "if this is urgent, do X, otherwise do Y," than Zapier gives you.

## 6/8: Chain Models Together

The scenario: you've inherited an old codebase, 40,000 lines of it, and you need it rewritten in a modern setup. First, you actually need to understand what the old code does.

Step 1.

Point Kimi K3 at the entire codebase in one go, using its huge memory window, it can read roughly 1 million tokens, about 750,000 words, at once:

Code

Step 2.

Take that summary, now just a few thousand words instead of hundreds of thousands, and hand it to Claude Code along with your actual instruction:

Code

Claude Code works from that short, clear summary and the real files it can see directly, then writes the code, tests it, and fixes anything that breaks. Here's a real example of Kimi K3 and Claude Code being used together: Kimi K3 + Claude Code Demo.

Why bother splitting the job across two models instead of just giving Claude everything at once. It's not that Claude can't handle a huge amount of text, current Claude models can read about a million tokens too now. The real issue is that every AI model, Claude included, gets fuzzier on details the longer and messier the input gets, well before it hits its actual limit. Independent testing has found that most models drop to less than half their usual accuracy by around 32,000 tokens, a little over 20,000 words, into a long, cluttered input. Claude holds up better than most, but it's not immune. Handing your main coding model an entire messy codebase and asking it to both understand everything and carefully rewrite a piece of it stacks two hard jobs on top of each other. Splitting them means the wide, messy first read happens somewhere else, and the actual writing happens from a short, clean summary where nothing important gets buried.

It also protects what you're actually paying for. If you're on a Claude plan with usage limits, or a metered Claude Code budget, spending that budget reading a million words of old code you'll mostly throw away is a worse trade than paying Kimi's separate, cheaper rate for that first read, and saving Claude's attention for the part where getting it right actually matters.

## 7/8: Failure Patterns That Waste Time

1. Running out of free credits mid-build.

Several "describe it and it builds it" tools, sometimes called vibe-coding tools, burn through an entire free plan in a single request once you go past a toy example, one documented test used up a whole free plan in one go.

Fix: check the tool's free-plan limits before you start, and expect to pay for the first tier if it's more than a quick test.

1. Assuming your subscription covers everything.

Paying for Claude Pro or Max, or ChatGPT Plus, does not cover the separate API key an automation tool like n8n needs, that's a different bill, charged by usage.

Fix: get the API key and check the current price per use before you build the automation, not after it's already running.

1. Letting an AI act with zero human check.

A well-known incident involved an AI coding tool changing real, live data on a hosted platform after being told directly not to touch it, the platform's own CEO publicly called it unacceptable. You can't fully stop an autonomous AI from doing something just by asking it nicely in the instructions.

Fix: always add a human approval step before any AI-driven action touches live data or a live site, exactly like the pause-for-approval step in section 5.

1. Trusting a company's own performance claims at face value.

Companies often compare their model to others using a different test setup for each one, and at least one independent test creator has publicly called out a company for using a scoring method that makes results look better than they really are.

Fix: before a comparison number changes which model you pick, check what test setup actually produced it.

1. Picking the tool before you know what you actually need.

Bolt.new and v0 lock you into a specific type of backend and hosting from the start, and that becomes a real wall the moment your project needs something different, like a different backend language or your own hosting. By the time you notice, you've usually already sunk real time in.

Fix: figure out what the finished thing actually needs first, a database, a specific backend, a mobile app, before picking a one-shot builder, not three weeks into using the wrong one.

## 8/8: Do This Today

1. Pick one real task you've been putting off, a website, a weekly report, an inbox you keep meaning to sort, not a hypothetical one.

2. Match it against the table in section 3, and pick the model actually built for that job, not whichever one's trending this week.

3. If it's a website, open claude.ai/design or lovable.dev and use the same approach from section 4: describe the whole page in one paragraph, fix it up, then publish it.

4. If it's something you'll do again and again, sign up for n8n.cloud or install it yourself, and build the same five-step workflow from section 5 with your own trigger and your own sources.

5. If it involves a huge document or codebase, split the job the way section 6 does: one model reads everything and summarizes, a second model does the actual work.

6. Before you call anything finished, run it past the five mistakes in section 7, especially the human-approval check.

7. Write down which model you used, for what, and what it cost. That's the note that makes your next build faster than this one.

if you find this useful,  follow @mikenevermiss for more

## X Article Metadata

- Title: How to Build and Automate Anything with Claude, Kimi K3, and Beyond
- Preview: 1/8: What You'll Walk Away Knowing
The simple loop behind every AI build, and which two steps people usually skip
Which AI model to use for which job, Claude, Kimi K3, GPT-5.6, and one

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
