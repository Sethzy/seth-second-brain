---
type: raw_capture
source_type: x
url: https://x.com/hasantoxr/status/2065757441963462964
original_url: https://x.com/hasantoxr/status/2065757441963462964
author: "Hasan Toor"
handle: hasantoxr
status_id: 2065757441963462964
captured_at: 2026-06-19T23:59:02+08:00
published_at: "Sat Jun 13 11:25:28 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 2
  reposts: 18
  likes: 74
---

# X post by @hasantoxr

## Source

- Original: [https://x.com/hasantoxr/status/2065757441963462964](https://x.com/hasantoxr/status/2065757441963462964)
- Canonical: [https://x.com/hasantoxr/status/2065757441963462964](https://x.com/hasantoxr/status/2065757441963462964)
- Author: Hasan Toor (@hasantoxr)

## Verbatim Text

Kimi Agent Swarm Explained: How to Run 300 AI Agents in a Single Prompt

(The feature that made ChatGPT Agent and Claude Cowork look like they were running on dial up and most people still haven't tried it.)

On April 20, 2026, Moonshot AI quietly shipped something that nobody in the West was talking about for a week.

Then a screenshot started circulating.

One prompt. 104-page literature review. 10,000 words. Fully cited. Generated in a single run.

Exported straight to Word, PDF, and PowerPoint.

No follow-up prompts. No human in the loop. One person typed a request, walked away to grab coffee, and came back to a finished academic document that would have taken a PhD student two weeks.

The tool that did it is called Kimi Agent Swarm. It can now run up to 300 AI agents in parallel, coordinate 4,000 steps across them, and deliver finished files not chat replies. And right now, almost nobody outside China is using it.

I've spent the last few weeks pushing it on real work research, content batches, dataset generation, competitive analysis. This is the complete guide I wish someone had handed me before I figured it out by trial and error. Every feature. Every first prompt. The honest limits. And the moment you should reach for it instead of Claude or ChatGPT.

1. Save this guide and try one swarm task this weekend on something boring you've been putting off.

2. Send it to anyone still doing research one Google tab at a time.

## Agent Swarm is not a chatbot. It is not even one agent. It is a company.

Here is the simplest way to understand the shift.

ChatGPT is one smart person at a desk. You ask a question. They think. They type. They send.

Claude Cowork is one smart person at a desk who can open your folders, read your files, and run errands for you. Better, but still one person.

Kimi Agent Swarm is a temporary company. You hire it for one task. The main agent acts as a CEO. It reads your request, figures out what kind of work needs to happen, and then hires up to 300 specialist sub-agents on the spot researchers, analysts, fact-checkers, writers, coders, designers. Each one gets a piece of the job. They work in parallel. They report back. The CEO synthesizes everything into a finished deliverable.

Nobody designs that organization in advance. The swarm designs itself, based on what your task needs.

I describe what I want. The swarm decides whether the job needs 12 agents or 247. It splits the work. I come back to a finished document. That loop changes what "a single prompt" actually means.

## The numbers everyone is missing

Moonshot AI shipped the first version of Agent Swarm in January 2026 with Kimi K2.5. It maxed out at 100 sub-agents and 1,500 coordinated steps per run. That was already a leap past anything else on the market.

Three months later, in April 2026, they shipped K2.6. The new ceiling:

• 300 parallel sub-agents per run (3x the old cap)
• 4,000 coordinated steps per run (2.7x the old cap)
• 86.3% on the BrowseComp Swarm benchmark, beating GPT-5.4 at 78.4%
• 92.5 f1-score on DeepSearchQA, where GPT-5.4 sits at 78.6
• 4.5x faster than running the same task sequentially with a single agent

Moonshot's own internal test: K2.6 Agent Swarm autonomously overhauled an 8-year-old open-source financial matching engine in 13 hours of continuous work. Result: 185% through put improvement. 4,000+ coordinated steps. No human supervising the loop.

That is the headline. The deeper story is what "horizontal scaling" of intelligence actually unlocks. For three years the AI industry has been chasing bigger models with more parameters. That race has a ceiling. Agent Swarm is the first serious bet that the next 10x of capability does not come from making one model smarter. It comes from coordinating many of them.

Vertical scaling has a ceiling physical, economic, and intellectual. Horizontal scaling does not. A single model is one expert. A self-organizing swarm is a company.

## The 5 jobs Agent Swarm is built for

After enough real-world testing, every great use case for the swarm falls into one of five buckets. If your task does not fit one of these, you do not need the swarm. Use regular Kimi or Claude. Save your credits.

1. Discovery at scale

When you need to find a mountain of things that are hard to find.Example: "Find the top 3 creators in 100 niche YouTube domains." The swarm spawns 100 sub-agents, each one researching a different niche in parallel. Twenty minutes later you have a structured spreadsheet.

Another real run: collect every Paul Graham essay ever published, scattered across his personal site, old blogs, transcribed talks, and archived pages. The swarm assigned specialist agents to search, download, categorize, summarize, and compile. The output: 200+ essays, sorted into 6 topic-based folders, with a full summary report. One prompt.

2. Output at scale

When you need a massive document not a paragraph, not a page, but a real book-length deliverable.

This is where the 104-page literature review comes from. Upload 40 social psychology PDFs. Ask for a literature review. The swarm decomposes the task across the documents, assigns writing-focused sub-agents to specific sections, and synthesizes everything into a 100-page, two-column academic document with formatted citations and references.

You can also point it at 200 product reviews and ask for a 50-page competitive teardown. Or 1,000 customer interviews and ask for a strategic research report. The point is: the output is too big for one agent to write coherently. The swarm splits the writing.

3. Perspective at scale

When you need disagreement on purpose when the value is in seeing one problem from many angles at once.

Example: launching a new product. Spawn a fake C-suite. A skeptical VC who questions your unit economics. A veteran PM who flags technical debt. An ethicist probing for dark patterns. A customer success lead championing edge cases. The swarm runs all four in parallel, each one armed with a different mental model. The synthesis is a much sharper plan than any single review.

Or use it for creative work. Take a chapter of a novel and ask 20 writers from different literarytraditions to continue it Virginia Woolf's interior monologue, Kafkaesque absurdity, García Márquez magical realism. Twenty completed alternate endings in parallel. Pick the one that works.

4. Processing at scale

Run hundreds of similar tasks at the same time.

Classify 10,000 customer reviews by sentiment and theme. Extract pricing data from 500 competitor websites. Generate personalized outreach for 200 leads with research baked into each one. Build a 20,000-row dataset by visiting and parsing 20,000 sources.Anywhere you would have written a Python script with a for-loop, the swarm now does it in one prompt and handles the edge cases your script would crash on.

5. Long-horizon execution

Tasks that take hours of continuous work, not minutes.

This is where the 13-hour financial engine overhaul lives. The swarm coordinates a long sequence of steps, recovers when sub-agents fail, reassigns work, and keeps going. Most single-agent tools collapse past 30 minutes of autonomous execution. The swarm is designed for the multi-hour run.

## Your first 60 minutes with Agent Swarm

Block an hour. Here is exactly what to do with it.

1. Minutes 0–5: Get access

Go to kimi.com. Free tier exists, but it gives you Instant mode and limited Agent credits not the full swarm. To unlock Agent Swarm with 300 parallel sub-agents, you need a paid plan.

The tiers, as of April 2026:

• Moderato $19/month. K2.6 chat, agent credits, Deep Research, Kimi Code. No full swarm.
• Allegretto $39/month. Agent Swarm unlocked. Best entry tier for most users.
• Allegro $99/month. More swarm credits, more Code credits, Claw cloud deployment.
• Vivace $199/month. Pro tier with the largest quotas.

If you want to try it before paying, the free tier still lets you experience Agent mode. The full 300 agent swarm starts at Allegretto.

2. Minutes 5–15: Pick the right mode

Kimi K2.6 ships with four modes. Knowing which one to pick is half the skill.

• Instant: fast Q&A. Use for quick answers and conversational tasks.
• Thinking: deep reasoning. Use for hard problems where you want the model to slow down.
• Agent: one agent, can use tools and search. Use for medium tasks like research summaries.
• Agent Swarm: the full multi-agent system. Use only when the job actually splits into parallel pieces.

The mistake everyone makes: defaulting to Swarm. Swarm is expensive in credits and slow to start. For anything a single agent can handle in 5 minutes, the swarm is overkill. Save it for jobs where you genuinely need 50+ sub-agents.

3. Minutes 15–30: Run your first real swarm task

Pick something boring you've been putting off. Real work, not a test. The swarm rewards specific prompts with concrete deliverables.

Bad first prompt: "Research AI tools for marketing."

Good first prompt: "Research the 50 most popular AI tools for B2B marketing in 2026. For each one, find: pricing tier, target customer size, top 3 features, top 3 limitations from reviews, and a one-line positioning summary. Output as a sortable spreadsheet with one row per tool. Include a final summary section ranking the top 10 by value-for-price."

The good prompt does three things the bad one does not. It defines a finite list. It names the fields. And it specifies the output format. The swarm reads this, decomposes it into ~50 parallel research jobs, and assembles a finished sheet.

4. Minutes 30–45: Watch the swarm work

Once you fire the prompt, the interface shows you the live decomposition. You see the main agent's plan. You see sub-agents spawn, run, and report back. You can step in at any point if it heads in the wrong direction.

Resist the urge to interrupt. The first time most people use the swarm, they cancel after 4 minutes because they don't see a final answer yet. The swarm is not a chatbot. It is a workflow. The output appears at the end, not along the way.

5. Minutes 45–60: Export and review

When the swarm finishes, it offers exports in Word, PDF, PowerPoint, or Excel whatever fits the deliverable. Download. Open. Review.

This is the moment that broke ChatGPT for me. ChatGPT gives you a chat thread you have to copy-paste out. The swarm gives you a finished file.

## The 5 swarm prompt patterns that actually work

Every prompt I've tested that produced a great swarm output followed one of these five patterns. Copy them. Adapt them.

Pattern 1: The list research swarm"

Research [N specific things]. For each one, find [field 1], [field 2], [field 3]. Output as a [format] with one row per item. Include a final summary ranking the top [N] by [criterion]."

Use this when you have a finite list of things to research. It triggers the discovery-at-scale workflow with one sub-agent per item.

Pattern 2: The document synthesis swarm

"Read the [N] documents I uploaded. Produce a [length]-page [type of report] covering [topic 1], [topic 2], [topic 3]. Include full citations. Format as a two-column academic document. Export as Word."

Use this when you have a stack of source material and need a long-form synthesis. The swarm assigns one writing agent per section.

Pattern 3: The expert panel swarm

"Review my [plan / pitch / draft] from the perspective of [role 1], [role 2], [role 3], and [role 4]. Each reviewer should focus on the concerns specific to their role. Provide their individual reviews, then a synthesis with my top 5 action items."

Use this for any plan that needs stress-testing. The swarm runs the perspectives in parallel, so they don't anchor on each other's opinions.

Pattern 4: The batch processing swarm

"For each of these [N inputs], do [task]. Output as a single [file type] with results indexed by input. Flag any items that need human review."

Use this for repetitive work. Classification. Tagging. Extraction. Personalization. The swarm runs the loop in parallel and returns a structured deliverable.

Pattern 5: The deep build swarm

"Build [a deliverable] that requires [research phase], [analysis phase], [drafting phase], and [polish phase]. Use the right specialist agents for each phase. Synthesize into a single [output type]."

Use this for big creative or strategic outputs. The swarm picks the right sub-agents for each phase and hands off cleanly between them.

What Agent Swarm is honestly bad at

Every guide on the internet right now is selling you the highlight reel. Here are the limits you will hit after week one. Knowing them in advance saves you hours of debugging. 

It is not always faster than just doing it yourself.

For tasks that take a human 15 minutes, the swarm often takes 10 minutes. Worth it?

Sometimes. But the swarm shines when the alternative is 6 hours of manual work, not 15 minutes.

Orchestration overhead is real.

Practitioners have noted that pushing past 100 parallel agents on complex tasks can produce inconsistent coordination. The 300-agent ceiling is a capacity number, not a guarantee. For most real workflows, the sweet spot is 20–80 sub-agents.

It cannot run truly sequential work in parallel.

If each step depends on the previous one like a multi-stage data pipeline where stage 2 needs stage 1's output the swarm cannot parallelize it. The swarm wins on wide tasks, not deep ones.

Some tasks lose nuance when split.

A 100-page literature review written by 30 sub-agents will feel slightly less unified than the same review written by one expert. The swarm trades coherence for speed. For 90% of work, that trade is fine. For your dissertation, maybe not.

Region and tier restrictions apply.

Agent Swarm is still labeled beta. Some features are gated by region. International users see USD pricing and the Allegretto+ tiers. Mainland China users see different pricing in RMB.

Always check the active tier on kimi.com before assuming swarm access.

It is not free.

Each swarm run consumes a lot of credits. A 200-row research task can eat 20–40% of a monthly quota on the Allegretto tier. Plan your runs. Don't fire the swarm at trivial work.

When to use the Swarm vs Claude Cowork vs ChatGPT Agent

These three tools all sound similar from the outside. They are not. After heavy testing, this is my honest decision tree.

Use ChatGPT Agent when:

You need a single autonomous task done end-to-end with web browsing, basic file work, and a clean UI. Best for booking, simple research, and short-horizon "do this for me" jobs. Limited to one agent, modest steps.

Use Claude Cowork when:

The work lives in your local files. You need a tool that reads and writes your folders, asks clarifying questions, runs scheduled tasks, and integrates with your real workflow. Best for personal knowledge work, documents, spreadsheets, and recurring automations. One agent, deep integration with your machine.

Use Kimi Agent Swarm when:

The task is wide. Many items, many sources, many sections, many perspectives. You need a finished long-form file, not a chat thread. You're okay with cloud-only execution. Best for research at scale, document synthesis, batch processing, and book-length outputs.

These are not competitors. They are complements. The right setup in 2026 is: ChatGPT for quick answers, Cowork for your daily knowledge work, and the Kimi swarm for the heavy research and batch jobs you used to outsource.

## Why this is the real beginning of agentic AI

Single-agent AI hits a wall. Every researcher knows it. The context window fills up. The model has to compress its history. Reasoning quality decays. Long tasks fall apart.

That wall is not solved by making the agent smarter. It is solved by giving the agent the ability to hire help.

Agent Swarm is the first mainstream product where the model itself decides in real time how many agents to spawn, what each one should do, and how to pull their work back together. The orchestration is not a separate framework you install. It is baked into the model.

For three years, anyone who wanted multi-agent workflows had to learn LangGraph, CrewAI, or AutoGen. They had to wire up the agents themselves. They had to debug the coordination.

They had to maintain the infrastructure. That entire layer just got absorbed into Kimi.

The implication is not that one product wins. It is that horizontal scaling many coordinated agents instead of one bigger one is the path forward for everyone. Anthropic will ship something similar. OpenAI will ship something similar. Google already has hints in Gemini Deep Think.

But Kimi shipped first, at scale, and made it usable for non-developers. That matters.

In the AI age, literacy may be measured by how many tokens we use.

## Your Agent Swarm roadmap

Pick where you are and start there. 

Today (30 minutes)

Sign up at kimi.com. Try the free tier in Agent mode. Run one research task to see how it feels. Decide whether to upgrade to Allegretto for full swarm access.

This week (a few hours)

Pick one real piece of work from your job research, a competitive teardown, a literature review, a batch of customer analysis and run it through the swarm. Compare the output against what you would have produced manually. Notice the gap, in both directions.

This month (a few sessions)

Build a small library of swarm prompts that work for your role. Save the ones that produce great output. Refine the ones that don't. The swarm rewards prompt craftsmanship like nothing else on the market.

Ongoing

Audit every task in your week. Anything that involves looking up many items, processing many documents, or synthesizing many sources is a swarm task. Stop doing them manually.

The people getting the most out of AI in 2026 are not the ones with the cleverest single prompts.

They are the ones who learned to delegate to swarms of agents and trusted the swarm to do the work.

Six months from now, this will be the default way people work. The gap between swarm users and everyone else will look like the gap between people who used spreadsheets in 1985 and people who still used calculators.

The question is not whether to learn this. The question is whether you learn it now while the gap is still something you can close.

If this guide helped you, send it to the one person in your network who still does research one

Google tab at a time. They'll thank you in a month.

Try Kimi Agent Swarm: kimi.com/agent-swarm | 

Official blog: kimi.com/blog/agent-swarm

RESOURCE LINKS

• Official Agent Swarm blog: kimi.com/blog/agent-swarm

• Try Agent Swarm: kimi.com/agent-swarm

• Official tweet: x.com/Kimi_Moonshot

• Kimi K2.6 model page: kimi.com/ai-models/kimi-k2-6

• Pricing: kimi.com/membership/pricing

• Brand assets: moonshotai.github.io/Branding-G

## X Article Metadata

- Title: Kimi Agent Swarm Explained: How to Run 300 AI Agents in a Single Prompt
- Preview: (The feature that made ChatGPT Agent and Claude Cowork look like they were running on dial up and most people still haven't tried it.)

On April 20, 2026, Moonshot AI quietly shipped something that

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
