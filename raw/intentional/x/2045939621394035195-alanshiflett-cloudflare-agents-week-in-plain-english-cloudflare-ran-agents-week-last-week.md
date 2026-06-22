---
type: raw_capture
source_type: x
url: https://x.com/AlanShiflett/status/2045939621394035195
original_url: https://x.com/AlanShiflett/status/2045939621394035195
author: "Alan Shiflett"
handle: AlanShiflett
status_id: 2045939621394035195
captured_at: 2026-06-19T22:03:15+08:00
published_at: "Sun Apr 19 18:56:32 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 14
  likes: 188
---

# X post by @AlanShiflett

## Source

- Original: [https://x.com/AlanShiflett/status/2045939621394035195](https://x.com/AlanShiflett/status/2045939621394035195)
- Canonical: [https://x.com/AlanShiflett/status/2045939621394035195](https://x.com/AlanShiflett/status/2045939621394035195)
- Author: Alan Shiflett (@AlanShiflett)

## Verbatim Text

Cloudflare Agents Week in Plain English

Cloudflare ran "Agents Week" last week and it was quite impressive, both in the number of announcements and the depth of what they shipped. Great job @eastdakota ,@Cloudflare, @ritakozlov, [@minglu](https://x.com/@minglu)!

As someone who's tinkered with Cloudflare for some personal projects, I was excited to see them make such huge strides toward rebuilding their developer platform to be written and run by AI.

Yesterday I sat down to play around with the announcements and see what impact they actually make. As part of that I built a prototype I called Keystone: a property management system that stitched six of the new features together end-to-end, including voice agent, browser automation, multi-agent coordination, durable workflows, persistent storage, and inbound email. If Cloudflare said building on top of this would be simple and lightweight, I wanted to see whether that was actually true.

The TLDR for those who don't care about the details: I really like the direction Cloudflare is going, and I plan to build more on top of it after these releases.

For everyone else, here is a breakdown of what I learned in my best attempt at plain English.

## The stuff that actually matters

1. Dynamic Workers — "give the AI a safe place to run its own code"

How it used to be: When an AI agent writes code (and increasingly they do, not just tool calls but actual code), that code has to run somewhere. The safe option was spinning up a container: basically a little virtual computer, locked off from everything else. Secure, but slow to start and expensive to leave running. The fast option was just... running the AI's code directly inside your own app. Faster, yes, but also the software equivalent of letting a stranger borrow your house keys. One bad line of code and your whole app is compromised. So developers picked: pay a lot and wait, or move fast and take on real risk.

What changed: Dynamic Workers give you a third option: a tiny, walled-off environment that starts up in milliseconds. Think of it less like spinning up a virtual computer and more like a sealed glass box. The AI drops its code inside, the code runs, the box gets thrown away. Cheap enough to do a thousand times a minute, safe enough that the code can't escape the box.

Why it matters: This is what makes "agents that write code" work at any real scale. Any time an AI agent needs to actually run code it wrote (not just describe it, but execute it), someone has to solve this problem. Every provider building coding agents is wrestling with it in their own way. Dynamic Workers is Cloudflare's answer, and it's a good one: fast enough to run constantly, cheap enough to not burn money on idle time, safe enough that you don't need to worry about the AI doing something bad with your app.

My take: This is the single most important announcement of the week, even though it's the least exciting to look at. It's the foundation that makes everything else in Agents Week actually affordable to run.

2. Sandboxes (GA) — "give the agent a real computer"

How it used to be: If your agent needed a full computer to work with (not just to run a quick snippet of code, but to install software, download files, and juggle multiple tasks), you were renting a virtual machine or wrestling with Docker. And if the agent paused, everything reset by default. You were re-setting up the same workspace every time.

What changed: Sandboxes are now generally available. Each one is a real computer your agent can use. It can install whatever it needs, work on a task across multiple steps, and pick up exactly where it left off between turns. Think of it as a laptop your agent borrows, except it never has to shut down and you don't have to ship it anywhere.

Why it matters: There's a real distinction between "run this snippet" (Dynamic Workers) and "do development work that takes hours and spans multiple steps" (Sandboxes). Coding agents need both. Before, you had to build both yourself. Now Cloudflare gives you both, with one bill and one dashboard.

My take: Sandboxes have been in beta since mid-2025, so this isn't brand-new. Hitting GA is the signal that you can build real things on it in production. If you wanted that before, you were reaching for a third-party service like E2B or Modal. Now there's a first-party option on Cloudflare. One fewer vendor to bring in.

3. The Agents SDK — "Project Think" and Fibers

How it used to be: Let's say you're building an agent that has to do a five-step workflow: acknowledge the request, find a contractor, dispatch them, notify the landlord, confirm with the tenant. If your server crashes halfway through step three, what happens? In the old world, you pulled in a workflow engine (Temporal, Airflow, AWS Step Functions), wrote a bunch of glue, and hoped for the best. Or you used a queue and prayed.

What changed: Cloudflare added something called Fibers, a way for the agent to pause mid-task, save its place, and pick up later. Each step gets saved automatically. If the server dies at step three, a different server resumes at step three. No external workflow tools. The agent itself handles it.

There's also a new "Think" base class that bundles all of this together. The agent can split off smaller sub-agents for specific tasks, it remembers conversations across sessions, it has durable workflows baked in. You get all the hard stuff as a starting point.

Why it matters: This is the one that hit hardest when I was building Keystone. In the old world, my emergency-dispatch flow would have needed a bunch of extra plumbing (queues, state tracking, retry logic, a separate database) just to survive a crash halfway through. With Fibers, it's one function that just... survives crashes. I killed the server mid-flow and it resumed on its own. Durable execution isn't a new idea. Temporal, DBOS, and others have been packaging it well for a while. What's different here is that Cloudflare bakes it directly into the agent itself, so you don't stand up a separate system to get it.

My take: Underhyped. This deserves more attention than the flashier voice and browser stuff. If you're building anything multi-step, this is where you should look first.

4. Voice Agents — talking to your agent, in just a few lines of code

How it used to be: Want your agent to have a voice? You were stitching together separate vendors: one for the phone line (like Twilio), one for speech-to-text (like Deepgram or Whisper), one for text-to-speech (like ElevenLabs), and your own orchestration layer to move audio back and forth between all of them. Multiple vendors, multiple bills, and a lot of latency to manage at every hop

What changed: Cloudflare shipped a @cloudflare/voice package that wraps the speech-to-text, agent logic, and text-to-speech into one pipeline running on their network. The built-in providers use Workers AI so you can start without any external accounts. Same agent, same conversation history, just a new way for users to talk to it.

Why it matters: Voice used to be a separate product. Now it's just another way to interact with your agent. A user can start by typing, switch to voice mid-conversation, and switch back. The agent doesn't know or care. For anyone building consumer-facing agents (customer service, scheduling, smart-home), this reduces the complexity significantly. It took me less than five minutes to get a voice agent running in Keystone.

My take: Adding voice used to feel like a whole separate project. Now it's a feature you bolt onto an existing agent in an afternoon. It's still early. Latency could be better, and the non-default speech providers take some extra work to plug in. But for the first time it's actually practical for a solo builder to ship a voice-enabled agent without it being the whole app.

5. Browser Run — "let the agent actually browse the web"

How it used to be: Browser Rendering (the old name) was useful but limited. Your agent could load web pages and take screenshots, but you were capped on how many could run at once, and if it got stuck on a login screen or a CAPTCHA, there was no good way to step in and help.

What changed: It's now called Browser Run, with 4× the concurrency, a "Live View" feature so you can watch the agent click around in real time, session recordings for debugging, and Human-in-the-Loop support. That last one is the big unlock. When your agent gets stuck, you can jump into the Live View for that session and click, type, or log in for it yourself, then let the agent pick back up where it left off.

Why it matters: Agents that can browse the real web unlock a huge category of use cases: research, form-filling, competitive intelligence, verifying things on third-party sites. The Human-in-the-Loop bit is the quiet killer feature. It's the difference between "cool demo" and "thing I'd actually trust in production."

My take: In Keystone I had the contractor agent search Google for local plumbers, visit their websites, and check the Texas licensing portal. It worked. Screenshots came back, data got extracted, nothing fell over. The rebrand from "Browser Rendering" to "Browser Run" is mostly marketing, but the capability upgrades are real.

6. Agent Memory — "stop stuffing everything into the context window"

How it used to be: Your agent "remembers" things by jamming the whole conversation history into every prompt. Works fine for five turns, starts to degrade at fifty, falls apart at five hundred. Even with 1M-token context windows, quality drops as you stuff more in (the industry calls this "context rot"). The alternative was building your own memory system from scratch, which is a multi-week engineering project most teams got wrong.

What changed: Cloudflare's new Agent Memory service (still in private beta) gives your agent a set of simple commands to work with: save something, recall something, forget something. Behind it is a managed system that does the retrieval for you. The agent asks "what did we decide about X?" and gets back just the relevant bits, without jamming the full history into every prompt.

Why it matters: Every serious agent eventually hits this wall. Having memory as a built-in primitive will save a lot of teams from reinventing the wheel badly.

My take: I didn't get to test this in Keystone because it's not public yet. But conceptually it's the right shape. I'll come back to this one once I can actually play with it.

## The quieter wins — nice if you're already building here

- AI Gateway unified inference layer. Call 70+ models from 14+ providers through one API. If you're already on Cloudflare, this saves you from wiring up OpenRouter or Fireworks.ai separately. You get the same multi-provider access, cost visibility, and failover, with one fewer account to manage. Matters more than it sounds.

- Kimi K2.5 on Workers AI. Technically a March launch rather than an Agents Week one, but Cloudflare leaned into it during the week as part of their inference story. I've been running Kimi K2.5 in my own agent stack (OpenClaw) for a while and I'm a fan. Having it available natively on Workers AI, without bringing in yet another inference provider, is a nice add-on if you're already on the platform.

- Email Service (public beta). Send and receive email natively from your agent. I played around with this and I'm glad it's in the same place as everything else. In the past I'd reach for SendGrid or Resend, yet another account, another API key, another bill. One less thing to juggle.

- Cloudflare Mesh. Zero-trust private networking so agents can safely reach your internal APIs and databases without exposing them publicly. Meaningful for enterprises, overkill for solo builders, but nice to know it's there when you need it.

- Unified CLI (cf). A single command-line tool that replaces the dozen scattered ones Cloudflare had accumulated. Not flashy, but if you've ever had to remember which CLI manages which product, you'll appreciate it immediately.

## The "interesting but niche" pile

- Artifacts. A Git-compatible versioned storage system for agent-generated code. Clever idea. Whether the world needs a new place to store millions of ephemeral agent-generated repos... we'll see.

- Flagship. A native feature flag service optimized for agents. The pitch is that agents write code behind a flag, deploy with flag off, and ramp themselves up. That's a reasonable future, but right now it's a feature flag service competing with LaunchDarkly and OpenFeature.

- Unweight. A lossless LLM weight compression technique that saves 15-22% memory. If you're Cloudflare operating thousands of GPUs, this matters enormously. If you're building an app, it's invisible.

## The "I'm not sure this matters" pile

- Agent Readiness Score / isitagentready.com. A scoring system that rates whether your website is "agent-friendly." Good idea in principle, but the score is based on Cloudflare's specific take on which standards matter, and those haven't been adopted outside Cloudflare yet. The industry could easily go a different direction. Revisit in a year when we know whose standards stuck.

- Redirects for AI Training. Turns <link rel="canonical"> tags into 301 redirects for AI crawlers. A sensible quality-of-life feature for publishers. Not much more to it than that.

- Shared Dictionaries. A smarter way to compress website files so browsers download less every time a site updates. Genuinely clever engineering. The business case (that agent-driven development will change code so often that current methods break) feels a bit aspirational right now.

## What I'd actually do with all this

If you've been thinking about dabbling with agents, it's hard to find a platform that's as out-of-the-box ready as this. Where to start:

- If your agent needs to think and act across multiple steps, start with the Agents SDK and the new Think base class. Durable execution is hard to build yourself.

- If your agent needs to run code it writes itself, reach for Dynamic Workers before containers.

- If it needs to browse the web, Browser Run is the path of least resistance. Turn on Human-in-the-Loop for anything with logins or CAPTCHAs.

- If it needs to talk, the voice pipeline is about as painless as it gets today.

- If it needs to remember things across sessions, plan for Agent Memory, even in beta.

Overall, I'm excited for the direction Cloudflare is heading and how it's making it simpler to ship with agents. Looking forward to what they and other platforms do next.

Originally published on ByteTalk.ai

## X Article Metadata

- Title: Cloudflare Agents Week in Plain English
- Preview: Cloudflare ran "Agents Week" last week and it was quite impressive, both in the number of announcements and the depth of what they shipped. Great job @eastdakota ,@Cloudflare, @ritakozlov, @minglu!
As

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
