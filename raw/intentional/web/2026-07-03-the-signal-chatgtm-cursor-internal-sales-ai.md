---
type: raw_capture
source_type: web
title: "The Signal ChatGTM Cursor Internal Sales AI"
url: "https://www.thesignal.club/p/chatgtm"
collected_at: 2026-07-02T18:23:03Z
published_at: 2026-07-02
capture_quality: complete
status: raw
trust_lane: intentional
---

# The Signal ChatGTM Cursor Internal Sales AI

Source: https://www.thesignal.club/p/chatgtm

## Capture Text


The Signal
The Signal


Inside “ChatGTM”: Cursor’s Internal Sales AI Used by their 400+ Sales Org
SDRs are booking 3x qualified meetings and AEs are shaving ramp by 50%+. What Cursor’s Head of Enterprise Growth, George Hou, built. And whether you should build your own version.
Brendan J Short
Jul 02, 2026

If you were forwarded this newsletter, join 9,252 weekly readers—some of the smartest GTM operators & founders—by subscribing here:

Type your email...
Subscribe
Thanks for reading this hand-rolled, 100% organic, farm-to-table (human-written) newsletter.


Presented by:



Bring AI agents, enrichment, and intent data together and turn insights into relevant, timely action. Start building for free.

& Supported by:

Attention → AI Agents for RevOps.

Clarify → The Autonomous CRM. Sell more, admin less.

Clearskies → The Context Layer for Revenue AI.

Nooks → All your outbound. One AI workspace.

Rox → Revenue Agents for the Global 2000.

Sumble → Buying signals from tech stacks, people data, & active projects.

Terret → The answer-to-action engine for revenue teams.


Hey y’all! 👋

George Hou (Head of Enterprise Growth at Cursor) and I caught up recently, and he (sort of sheepishly) mentioned an internal tool he had built for the sales team at Cursor. I (not so sheepishly) asked him to share more. Before I knew it, he was screen-sharing and saying things like “I can’t show you that part,” which, of course, made me all the more curious. :)

I’ve gotten to know George, and a few of the folks at Cursor, over the last year or so, and I see them as some of the most impressive people in go-to-market. Not just by resume, but by how they think from first principles, how they ship, and how little ego they carry. It’s a vortex of talent over there.

George is a legend, and a kind supporter of the work I’ve been doing with The Signal. So, he was down to give me (and y’all!) a peek behind the curtain of exactly what he built (thanks for sharing with us, George 🫡).

ChatGTM is gaining crazy adoption within Cursor’s 400+ person sales org, and it’s helping their SDRs book 3x more qualified meetings and decrease AE ramp time by 50%+.

Here’s what we cover in today’s article:

What ChatGTM actually is

Why they built it

But why not just use Claude Cowork, ChatGPT, or Glean?

The question on every Revenue Leader’s mind: Build vs. Buy

Who owns AI x GTM initiatives inside Cursor

The results across their 400-person sales org

Three lessons from George

Alright, let’s get into it.

What ChatGTM actually is
Reps describe ChatGTM as AI that already knows their accounts and how they sell. The easiest way to understand is to watch it work, so here’s a day in the life.

7:30am, on the subway: their morning digest is waiting in Slack: context on today’s meetings and who’ll be in them, overnight news across their accounts, and key territory trends: usage spikes, fresh signups, new exec hires.

8:00am, at the desk: 25 outbound messages are already drafted, each tied to a signal and paired with a landing page personalized for the contact’s tech stack and role. The rep just reviews, tweaks, sends. The send is native to Gmail or Outreach, so there’s no copy-paste required.

8:45am, prepping for a call: the brief flags that the exec hates a hard pitch from an article she just published, so the rep walks in prepped on how peers approached her problems.

9:00am, on the call: the exec lobs a curveball about migrating off legacy infrastructure the rep has never heard of. A quick question to ChatGTM answers it live. They leave with next steps booked and the exec says she doesn’t need a POC.

Between meetings: every call already has its recap email drafted and waiting, plus custom follow-ups to the threads that went quiet.

3:00pm, prepping tomorrow’s exec meeting: the rep builds the whole business case in one thread: the three why’s, the value drivers, a CFO-ready one-pager and deck. Then he maps the org chart to see who else needs to be in the room and how to reach them.

4:00pm: a Slack digest pulls everything worth catching up on: product releases, account updates, DMs. Where a release is relevant to an account, it drafts tailored outreach for them to review.

Thursday, before the forecast: ChatGTM scans every deal, its notes, stage changes, and next steps, then assembles the forecast and drafts the weekly update for their manager and account team.

Start of a new quarter, strategizing a new book: the rep kicks off ChatGTM on a research job that would’ve taken weeks: every intent signal, usage trend, past Gong call, and Salesforce record, plus each account’s key initiatives and tech stack. It comes back with a stack-ranked plan for how to spend the quarter.


The morning digest reps work from: pre-drafted messages, each with a landing page tailored to the contact’s stack, role, and seniority.

The feed (UI) is the visible part. Underneath it, ChatGTM goes directly to the sources (eg: Salesforce, Gong, data warehouse, LinkedIn, third-party data vendors, and the open web) and pulls context on demand. This is a very unique approach (more on this later).

Roughly 70% of usage is outbound and account research. The other 30% is more varied (and interesting). One rep describes ChatGTM as her “fleet of agents.” She described it as a manager who coaches her before an external sales call or even an internal forecast meeting (“What are things that my manager will stress test me on?”).




The home screen reps start from: one chat box to launch an outbound plan, an org chart, or deep account research. Automations land in their inbox.
It also has memory: individual preferences (”I like shorter emails,” “I care about these signals, not those”), and team-level context (like an org chart one rep corrects on a call that then propagates to everyone else).

Why they built it
George runs enterprise growth at Cursor. The team’s mandate is to convert intent signals into pipeline, at scale, across a GTM team of almost 500. So George did the unglamorous thing and sat next to the SDR team to watch their actual workflows.

He noticed that before a rep could pick a single account to work, they were opening seven tabs. A Hex dashboard, Salesforce, Gong, LinkedIn, and a couple of others. 45 minutes of aggregating data, and then they’d sit there staring at a blank canvas, trying to figure out how to reach out.

He told me his initial thought was that if he could make SDRs 20% more productive, that would be a win.

He started small. First, custom SQL queries to pull everything into one table. Then a scoring formula to prioritize who to hit. Then drafting the copy. Then, long-running agents to do deep account research. The agents were robust and comprehensive, but slow, expensive, and not dynamic. When George showed that long-running agent output to the SDRs, they found it very valuable, but wanted it to refresh every single day.

Around the same time, customer success and a few AEs saw it and started asking ad hoc questions (”give me the talk track that resonated with FinServ customers last quarter”). That’s when the chat interface was introduced. Chat, plugged into powerful tools and context, enabled anyone to ask anything. This design gave space for flexibility in how reps used it. In other words, he made the users of the product (reps)—who are subject matter experts—the builders of the product. (We’ll come back to this important point.)


Account research in action: a point of view, org chart build, the signals worth acting on, and a first pass at the three why’s.

But why not just use Claude Cowork, ChatGPT, or Glean?
I get this question often. And Cursor actually had every possible tool on the shelf. So I asked George: why build your own?

Going from no AI to one of these tools is a huge leap. Of course it feels like magic. But it stalls fast.

These tools are genuinely good at small, simple pieces of the job: call notes, recap emails, call prep.

But to help do a rep’s job end to end, the AI has to know your business cold: your product, your pricing, who you sell to, how you sell, your whole GTM motion. Then it has to carry the work the whole way: build the org chart, pull the one line that matters from hours of Gong calls, shape a point of view and the three whys, draft the CFO one-pager and deck, tee up the outreach. That’s the hard part, and where these tools crack.

As one rep put it, using Claude meant repeatedly uploading data and re-explaining context.

Cursor isn’t alone here. The same questions come up with most sales leaders George talks to.

Can you point to an efficiency gain? Not whether reps like it and are using it. What number actually moved? One VP’s honest reflection after a few months: no real efficiency gain beyond better-written emails. If it didn’t inflect pipeline, ramp, or win rate, it’s an expensive assistant.

When’s the last time it was wrong? A RevOps leader admitted she still catches inaccurate outputs regularly. For every one you catch, how many does a rep miss and send to a customer anyway? Turning on an MCP isn’t the same as pulling the right data, and one wrong number can cost a deal.

Does it scale past your best rep? Your power user will thrive with anything. But “just build a skill” isn’t a plan. Will the other 90% find it, remember it, and use it? In an open chat box, most never get past the basics.

Where are the guardrails? A blank chat box has none. Nothing guarantees it pulls from the right data every time, or runs the way you actually sell: MEDDICC, command of the message, the three why’s. So the playbook you drill at SKO stays a slide deck. Whether it shows up in the work is left to each rep to remember.

And what does it cost once it’s actually used? It runs away from you. Ask for something like LinkedIn research and it uses your browser for 30 minutes, torching a chunk of the month’s budget in a single task.

None of this is a knock on these tools. They’re genuinely great, and Cursor’s reps still reach for them for a few use cases. But answering a question and doing a seller’s job end to end are different problems. George was trying to tackle the latter.

The question on every Revenue Leader’s mind: Build vs. Buy
Cursor isn’t the first company to build a full-blown sales platform. Ramp built a similar system in-house (which I covered in my piece: 11 growth-stage companies that built GTM agents in-house). But, George explicitly told me:

I don’t think most GTM teams should build this.

And I totally agree with his reasoning. Like Ramp, Cursor’s team is very AI-pilled; they have the internal resources (people and money), they have a ton of first-party data to use, the technical infrastructure (data warehouse and connectors) and data team in place, and have a ‘build over buy’ culture.

Plus, there’s a lot of context-engineering work underneath, which Cursor happens to be unusually good at (because building Cursor required exactly that). George shared with me that the core of ChatGTM took about two months. But that sat on top of a pile of earlier failures, compounded learnings, and hard-won knowledge about agents and data providers. None of that is just sitting on a shelf for an eager CRO or GTM Engineer at a Series D company.




Should small teams build a one-off agent in-house (lead qualification, call prep, an ICP rebuilt over a weekend)? Absolutely.

But what George built sits at the far end of the spectrum. It’s a full go-to-market product that reps work out of throughout their day.

They also, notably, didn’t rip out the systems of record. They kept Gong. They kept Salesforce. They kept Slack. They kept Nooks for the SDRs’ parallel dialing. ChatGTM sits on top of those and pulls from them on demand.

The “you need a GitHub repo full of sales context” idea you see all over LinkedIn? They didn’t do that either. In other words, all that context is not sitting in a data warehouse or in a GitHub repo. Instead, ChatGTM queries Salesforce, Gong, etc., in real time, going to the data warehouse or wherever the data already lives. It’s fetched on demand (via live API/MCP tool calls), not pre-loaded into a repo someone has to maintain.

Who owns AI x GTM initiatives inside Cursor
One of my biggest questions about this project is who actually built it, who owns it, and who maintains it?

It didn’t come from RevOps. It wasn’t handed to a recent GTM Engineer hire. It came from growth.

George started it solo. Wilson, a product research engineer who’s done ambitious harness engineering work (incl. building a search engine and browser!), built the infrastructure that finds and feeds the AI the right information at the right time. And Emily, a growth engineer, helped build key integrations. That’s the whole build team.

But the more interesting answer to “who owns it” is: the reps.

Cursor built ChatGTM in a way that enables a non-technical seller to create their own skills (repeatable workflows) and automations (a scheduled skill) in natural language, inside ChatGTM. They are the subject-matter experts. They shape how the product is used and evolves, and have created 500+ skills and 1,000+ automations

Sales reps are just piling in skills and automations, and every time I chat with them, they light up. They’re so excited to screen-share what they’ve built. Our sales team describes this as their ‘Cursor moment.’ The first time they got real superpowers from AI, because the thing actually knew their context and how they liked to work.

The results across their 400-person sales org
They started with a tiger team of 8 SDRs. That cohort is the most mature set of data/users (they have been using ChatGTM for ~1.5 months at the time I spoke with George).

Results (what we’re all here for):

The SDR team is booking triple the qualified meetings. The top 2 reps are at 4x.

Remember, the initial goal George was aiming for was to improve their outputs by 20%.

Separately, sales leaders are saying AE ramp time has decreased by more than 50%.

They’re tracking success against four core metrics:

Pipeline generated

Rep ramp time decreased

Sales cycles shortened

Time saved.

Anecdotes:

Re: Pipeline generated — SDRs describe not being able to live without ChatGTM at this point. Some half-joke that if ChatGTM has an outage, they might as well go home because they can’t effectively outbound at the same pace. And to be clear: this team was AI-pilled before ChatGTM, with full-built skills that took months to build.

Re: Ramp time — a strat rep used to need more than a week to get up to speed on a single account (Slack archaeology, Salesforce, Gong, piles of context tracked nowhere). Now they’re ramped on an account in 30-45 minutes. It’s day and night. Sales leaders are seeing the same thing. One watched a rep in their third week sound like a year-long veteran on a call.

Re: Sales cycle — one rep described ChatGTM as her “fleet of agents” that collapsed multiple people into one chat: a manager who stress-tests her before a call, an SE who builds a usage graph, an SDR who sources contacts, an analyst who pulls closed-lost reasons. A sales leader had a similar moment on a call with a head of global AI, who fired off tough questions. Normally that’s a “let me get back to you.” Instead he answered live with ChatGTM five weeks in and booked the next step right then.

Re: Time saved — one leader pulled out his phone at his son’s lacrosse practice, fired off a few requests to ChatGTM between plays, and had detailed research briefs and drafted email replies waiting by the time the game wrapped. He calls it having unlimited agents in his pocket.




In the past month, top reps have booked more than 60 qualified meetings (4x increase) and saved 100+ hours.
The rate of adoption proves ChatGTM is valuable in the stack. The vast majority of the GTM org are DAUs.

When the SDR manager rebuilt the new-hire outbound curriculum, he told his team they were only allowed to use three tools: ChatGTM, Nooks (for parallel dialing), and LinkedIn. They should not be logging in to anything else.

Three lessons from George
I asked George what he’d tell someone who was at the beginning of this journey. He gave three concrete tips.

1. Work backwards from the metric you’re accountable for.

Find the fastest path to inflecting this number, whether that means buying or building on top. Shiny demos are cool until leaders ask for the impact. It’s hard to debate the cold metrics.

2. Nail one burning problem first.

Their approach early on was to throw agents at the problem and hope. That doesn’t work. An agent without the right context won’t magically solve anything. Most of the work is figuring out what context it actually needs, one workflow at a time.

3. Your team is the context.

Agents don’t come knowing how you sell. Your reps and leaders do. The real unlock is making it dead simple for those subject-matter experts to pour in their judgment, then getting out of their way.

Most teams won’t build their own version of ChatGTM, and George would be the first to tell you they shouldn’t. But, I hope this helps you think through “the art of what’s possible,” the ever-evolving (and nuanced) Build vs. Buy decision for revenue leaders right now, and how AI x GTM is shifting.

Oh, and if any Revenue Leaders are thinking through this now, George is happy to chat and share learnings. So reach out to him on LinkedIn.

Thanks again to George for giving us a peek behind one of the wildest in-house builds I’ve seen. We’ll have to revisit ChatGTM again in 6 months to get an update!

That’s it for today. Hope you enjoyed this insider peek into how one of the big 3 labs is building its GTM engine. Absolutely wild to see.

As always, thank you for your attention and trust. I do not take it for granted.

See you next time,
Brendan 🫡

Subscribe to The Signal
By Brendan J Short · Launched 3 years ago
The GTM playbook has changed. We break down what the best AI-native teams are doing.
Type your email...
Subscribe
By subscribing, you agree Substack's Terms of Use, and acknowledge its Information Collection Notice and Privacy Policy.
20 Likes
∙
2 Restacks
Discussion about this post
Write a comment...

The Rise of the GTM Engineer
The Signal
Nov 15, 2024 • Brendan J Short and Jason Saltzman

49

4

3


How to Become a GTM Engineer (8 Resources)
The Signal
Apr 19, 2025 • Brendan J Short

32

2

1


9 Lessons From 11 Growth-Stage Companies That Built GTM Agents In-House
Vercel, Ramp, LangChain, ClickUp, Deel, Vanta & others: what they built, their tech stacks, and what we can learn from them
Mar 20 • Brendan J Short

33

2

3


Ready for more?
Type your email...
Subscribe
© 2026 Brendan Short · Privacy ∙ Terms ∙ Collection notice
Start your Substack
Get the app
Substack is the home for great culture
Hyper Icon
