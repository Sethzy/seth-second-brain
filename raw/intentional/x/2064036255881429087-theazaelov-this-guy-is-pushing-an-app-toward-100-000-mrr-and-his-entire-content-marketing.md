---
type: raw_capture
source_type: x
url: https://x.com/theazaelov/status/2064036255881429087
original_url: https://x.com/theazaelov/status/2064036255881429087
author: "Azael"
handle: theazaelov
status_id: 2064036255881429087
captured_at: 2026-06-19T23:41:36+08:00
published_at: "Mon Jun 08 17:26:05 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 6
  reposts: 1
  likes: 11
---

# X post by @theazaelov

## Source

- Original: [https://x.com/theazaelov/status/2064036255881429087](https://x.com/theazaelov/status/2064036255881429087)
- Canonical: [https://x.com/theazaelov/status/2064036255881429087](https://x.com/theazaelov/status/2064036255881429087)
- Author: Azael (@theazaelov)

## Verbatim Text

This guy is pushing an app toward $100,000 MRR and his entire content marketing is run by an AI agent that produces the ads itself and scales them itself too.

He doesn't need a creative team, editors or live UGC actors.

He works as the operator of a growth command center, where in the background the system runs the whole growth cycle from generating clips to revenue analysis, puts out 48 short videos a day, keeps a library of 550 unique assets and turns organic and paid traffic into subscriptions.

His pipeline separates the production of the creative from its evaluation.

What he does:

→ First the system generates short-form assets in batches for different formats: POV UGC ads, short dramatic scenes, "day in the life" clips, CTA inserts, studio transitions and vertical cuts

→ Then it sorts them by hypotheses: POV pool, drama CTA, short drama rotation, trends for the US and Germany, follow-up angles, and every branch works as a separate ad line

→ It promotes the winning combos not by intuition but through a virality predictor, which looks at historical retention, view velocity, CTR and audience reaction

→ End-to-end analytics ties the creative to the whole funnel for him, and you can see the numbers right in the clip: 4.1M views, 19,667 sign-ups, $45,600 MRR and paid traffic at 2.1 ROAS on $1,900 of spend

→ When a trend takes off, it doesn't just log a one-off win but sends it to the backlog for reproduction, expands the rotation, finds similar angles and launches new variations across the accounts

→ A separate agent named Scout looks for raw material for the next cycle: which formats took off, which topics to pick up, which CTAs to test and which markets to expand

He doesn't even chase a mega-viral hit, because at 48 clips a day regular average winners are enough for him, and one format that lands brings thousands of sign-ups with no ad spend.

I broke down the economics of this system by its own numbers.

Results:

From view to sign-up the system converts at around 0.48%.

At $45,600 MRR and an average check of $19–29 a month the product adds up to 1,570–2,400 paying users, so the paid conversion holds at 8–12%.

A manual team of this capacity would cost $18,500–40,500 a month, while the whole AI stack runs him $1,500–4,000, so he saves $15,000–35,000 every month.

If you have ever tried to scale a subscription product through content, you know this friction.

Either you hire an agency and a performance team for tens of thousands a month, or you edit 5 or 10 versions yourself and spend weeks looking for a winner, or you put out few clips and never hit the format that converts into sign-ups.

Now he launches one pipeline, and it unfolds into a multi-account grid, where one account runs POV ads, another short dramas, a third UGC reviews, and another one localized content for Germany, France, Spain or Brazil, and the system itself shifts the generation toward the winners.

For everyone who is building a SaaS, a D2C or a subscription app, here is what matters: he can sell this same factory as a service to other projects for $5,000–15,000 a month per client, and ten clients give $50,000–150,000 MRR not inside the app but in the service around growth generation.

The real power here is not in the number of clips but in the closed learning loop: in 2 or 3 weeks the system builds up its own library of winning hooks, formats, CTAs and markets and then tests by data instead of by taste.

In the end a future $100,000 MRR business looks for him not like an office with a team but like one person in front of screens and a fleet of AI agents, and while competitors are still discussing their creative strategy, his pipeline has already put out 48 clips, found three winners and sent them to scaling.

## Quoted Post

- URL: https://x.com/browomo/status/2063945337094451427
- Author: Blaze (@browomo)

Claude AI agents as a service. $15,000/month automating content for experts and agencies.

## The full business model: what to build, who to sell to, how to charge $2,000/month on retainer and how to close your first clients in 30 days.

---

## PART 1 - The Opening

An education brand in Lisbon ran a 4-person content team: topic research, post drafts, cutting clips from webinars, replying in comments, weekly reach reports. All manual. All costing 19,000 EUR per month in salaries.

They replaced 75% of it with four Claude agents.

Tool cost: 180 EUR per month.

Monthly savings: about 14,000 EUR.

The person who built those agents charges 2,000 EUR per month to maintain them.

That is the entire model. Build the agents once. Keep them on retainer. $15,000 per month is 7 to 8 clients.

Here is everything you need to copy it.

---

## PART 2 - How an agent differs from a chatbot

Most people confuse agents with chatbots. They are different things.

A chatbot answers a question. An agent runs the whole process end to end.

A chatbot works like this: a human asks, Claude answers, done. The human asks again, Claude answers, done.

An agent works differently: a trigger fires, Claude reads the input, decides what to do, acts in external systems, checks the result, routes the output to the right place, and the process completes with no humans involved. Then it runs again on the next trigger.

An agent can watch a folder of webinar transcripts, pull 5 post ideas from each one, write drafts in the brand's voice, file them in Notion, create tasks in a planner, and send a digest to Slack. All triggered by one new file, all done in minutes, 24/7, without anyone touching it.

That is what experts and agencies pay 2,000 EUR per month to have permanently.

## PART 3 - Why now

The tools became broadly accessible in 2024 to 2025. Claude API is $20 to $60 per month at typical content volume. n8n connects 400+ apps with no code.

Every content operation already lives in Notion, Google Docs, Slack, YouTube and Telegram, all of which connect in minutes.

The implementation gap is huge. Everyone knows AI exists. Almost no one knows how to wire it into their content pipeline.

That gap is the business.

---

## PART 4 - The tech stack

Two tools do everything. Claude is the brain. n8n is the nervous system.

Claude API (console.anthropic.com) is the brain inside every agent: it reads inputs, makes decisions, writes copy, costs $20 to $60 per month at typical volume, and connects to n8n in 2 clicks via an HTTP Request.

n8n (n8n.io) is workflow automation, more powerful than Zapier: it connects 400+ apps, works visually with drag-and-drop and no code, and is free self-hosted or $20 per month in the cloud.

Client-side tools connected per client: content base in Notion and Google Docs, video and audio from YouTube and transcripts (Whisper or Fireflies), social on Telegram, X, LinkedIn and Instagram via API, analytics in GA4 and native platform stats, notifications in Slack and a Telegram bot.

Your own infrastructure as a one-time setup: billing in Stripe, contracts in PandaDoc, a Notion workspace per client as the portal, and n8n built-in execution logs for monitoring.

Total cost is $80 to $200 per month on your side and $0 to $40 per month extra on the client side.

---

## PART 5 - Agent 1: Idea and Draft Generator

Every expert's biggest pain is "I don't know what to write" and "I have no time for drafts." Topics show up randomly, posts come in bursts, there is no system.

This agent delivers 5 ideas and 3 finished drafts in the brand's voice every morning. Every day.

How it works: the trigger is a new transcript file landing in a folder or a schedule (every weekday at 8:00). Step 1, n8n grabs the source. Step 2, it sends it to the Claude API. Step 3, Claude pulls ideas and writes drafts. Step 4, n8n files the result in Notion with tags. Step 5, review tasks are created in the planner. Step 6, a digest is sent to the author on Telegram.

The Claude prompt:

```
You are a senior content strategist for [Brand Name].
About the brand: [niche, audience, tone of voice, taboos]
Big themes we develop: [3 to 5 points]

Here is today's source material:
[insert transcript or notes]

Do the following:
1. Pull 5 post ideas. For each, give a sharp angle (not a topic, an angle), a format (story / breakdown / list / opinion), and the platform where it would land best.
2. From the best 3 ideas, write finished drafts: a strong opening hook, one core idea with no filler, natural human-sounding language, no corporate cliches, under 220 words each.
3. Output ONLY as valid JSON:
{
"ideas": [{"angle": string, "format": string, "platform": string}],
"drafts": [{"title": string, "body": string, "platform": string}],
"editor_notes": string
}

Time saved: 2 hrs/day x $30/hr x 250 days = $15,000/year
```

## PART 6 - Agent 2: Repurposing (1 asset into 10 pieces)

An expert records a one-hour webinar, and that is it. But there is two weeks of content sitting inside: posts, quotes, carousels, newsletter angles. Nobody has time to cut it up.

This agent turns one long asset into 10+ ready-to-publish pieces tailored to each platform.

How it works: the trigger is a webinar or podcast transcript being uploaded. Step 1, n8n passes the text to Claude. Step 2, Claude slices it by platform formats. Step 3, results are filed in Notion by column. Step 4, visual pieces go to the designer as tasks. Step 5, everything is logged into the content plan.

The Claude prompt:

```
You are a repurposing editor for [Brand Name].
Tone of voice: [description]
Platforms we cut for: [Telegram, X, LinkedIn, newsletter]

Source material:
[insert full transcript]

Do the following:
1. Pull the 3 key points of the material.
2. Generate content pieces: 3 short Telegram posts (under 120 words), 2 X threads (5 to 7 tweets each), 1 LinkedIn post (expert tone), 5 quote cards (one strong line each), 1 email teaser paragraph.
3. For each piece, flag whether it needs an image.
4. Output ONLY as valid JSON:
{
"key_points": [string],
"telegram": [string],
"x_threads": [[string]],
"linkedin": string,
"quote_cards": [string],
"email_teaser": string
}

Time saved: 3 hrs/asset x 8 assets/mo x $35/hr = about $10,000/year
```

## PART 7 - Agent 3: Comment moderation and replies

80% of comments are variations of the same 15 questions. A human reads, looks up the answer, and types it out, for information that has not changed in months. The rest sinks, and the audience feels ignored.

This agent answers the routine instantly, escalates the complex with full context, and never loses a thread.

How it works: the trigger is a new comment or message on a platform. Step 1, n8n captures the text and metadata. Step 2, it pulls this person's history. Step 3, it sends everything to Claude. Step 4, if it is an auto-reply, it posts or sends it. Step 5, if it is an escalation, it goes to the author in Slack with context. Step 6, everything is logged and a weekly topic summary is sent.

The Claude prompt:

```
You are a community manager for [Brand Name].
Tone: [warm / expert / friendly]
Knowledge base: [insert FAQ and key facts]

Incoming message:
From: [name]
Text: [full text]
History: [past touchpoints, subscriber status]

Do the following:
1. Classify: question / objection / praise / negativity / spam / partnership request.
2. Decide the reaction type. AUTO-REPLY if the answer exists in the base and no personal action is required. ESCALATE if there is an emotional complaint, a partnership request, a question outside the base, or a potential client.
3. If AUTO-REPLY, write the reply: by name, to the point, warm, under 80 words, no template feel.
4. If ESCALATE, give a short summary for the author plus a suggested reply.
5. Output ONLY as valid JSON:
{
"category": string,
"response_type": "auto_reply|escalate",
"response": string,
"escalation_notes": string or null,
"sentiment": "positive|neutral|negative"
}

Time saved: 2.5 hrs/day x $25/hr x 250 days = $15,625/year
```

## PART 8 - Agent 4: Weekly content report

Most experts check their stats randomly: they remember, they open it; they forget, they skip it. What worked and why stays unclear. Decisions get made on gut feel.

Every Friday at 3pm this agent sends a living report: what worked, why, and what to do next week.

How it works: the trigger is every Friday at 2pm. Step 1, n8n collects the week's platform metrics. Step 2, it pulls the list of published posts. Step 3, Claude analyzes the format-to-result link. Step 4, the report goes to the author by 3pm. Step 5, on an anomaly (a viral hit or a flop) it fires an instant alert.

The Claude prompt:

```
You are a content analyst for [Brand Name] in the [niche] space.
Our goals this quarter: [description]
Formats we are testing: [list]

This week's data:
[insert metrics per post: format, reach, engagement, clicks]

Produce a report:
1. WHAT WORKED BEST. Specific posts and the reason: format, angle, topic.
2. WHAT DID NOT LAND. No excuses. A hypothesis why.
3. PATTERNS OF THE WEEK. Which format or angle consistently drives engagement?
4. PLAN FOR NEXT WEEK. 3 to 4 concrete actions, not abstractions. Not "post more" but "3 story posts Tue to Thu".
5. ALERT LEVEL. Green / Yellow / Red, and why.
Rule: every observation leads to an action. No observations without an implication.

Time saved: 4 hrs/week x $40/hr x 50 weeks = $8,000/year
```

---

## PART 9 - The discovery call that closes clients

The call has one goal: make the math undeniable. The product sells itself once the numbers are on the table. Here is the full 30-minute script.

Minutes 0 to 2, open with: "Thanks for taking the time. Before I show you anything, I want to understand how your content runs today. Is that okay?" Never pitch first, diagnose first.

Minutes 2 to 12, find the repetitive work: "Walk me through a typical week for your content team. What gets done the same way every time?" Listen for topic research, drafts, clipping, replies and reports, since all of it is automatable. Then ask "How many hours a week does that take across the team?" and "And at their rate, what does that cost per month?" Calculate live (hours x rate x 4.33 = monthly cost) and write the number where they can see it.

Minutes 12 to 20, show the solution: "Can I show you what that looks like automated?" Then show a recording of a real agent on a live example, one minute, transcript loaded, 90 seconds later 5 drafts in Notion.

Minutes 20 to 25, run the ROI math: "Right now you spend $[X] per month on this work. The agent handles 75%. That is $[X x 0.75] per month saved. The retainer is $[Y] per month. You are ahead by $[difference] every month. Setup pays back in [weeks] weeks." Show the numbers and let silence work.

Minutes 25 to 30, close: "Here is how it works: a one-time setup of $[X], I build and configure everything for your systems, then $[Y] per month and I monitor, maintain and improve it. When would you like to start?" Not "are you interested", but "when". Move forward.

---

## PART 10 - Pricing that closes

Beginners underprice out of nerves. These are real market rates. A lower price signals inexperience, not value.

For a single agent, when the client insists, charge a setup of $1,200 to $2,000 for simple (1 to 2 integrations), $2,000 to $3,500 for medium (3 to 5 integrations), $3,500 to $5,500 for complex (6+ integrations), with a retainer of $400 to $1,200 per month.

Always lead with packages instead.

Starter is 2 agents: $4,000 setup, $1,200 per month retainer, client saving of $4,000 to $6,000 per month, payback in 4 to 6 weeks.

Growth is 3 agents: $7,500 setup, $2,000 per month retainer, saving of $8,000 to $12,000 per month, payback in 3 to 5 weeks.

Full Pipeline is 4 agents: $14,000 setup, $3,000 per month retainer, saving of $14,000 to $20,000 per month, payback in 3 to 4 weeks.

When the objection is "That seems expensive," respond with "Let's look at your current cost for this process together," pull out the ROI math, and the conversation changes immediately.

---

## PART 11 - How to build and test your first agent

Here is the step-by-step for the idea-generation agent, the best starting point.

Day 1 is setup, about 2 hours. Create the accounts: n8n.io (free cloud trial), console.anthropic.com (create account), then get the Claude API key and copy it. In n8n go to Settings, Credentials, Add new, HTTP Request Auth, Bearer token, paste the key and name it "Claude API". Then create a new workflow.

Day 2 is the build, about 4 hours. Node 1 is the trigger (Webhook or Schedule). Node 2 is an HTTP Request to Claude: POST to https://api.anthropic.com/v1/messages with a JSON body of {"model":"claude-sonnet-4-20250514","max_tokens":1500,"messages":[{"role":"user","content":"[prompt with data]"}]}. Node 3 is JSON Parse to extract ideas and drafts. Node 4 is Notion to create draft pages. Node 5 is Telegram to send a digest to the author. Node 6 is an IF node: if a draft is strong, create a separate task.

Day 3 is testing, about 2 hours. Run a normal transcript, a very short input, an input in another language, off-topic material, an empty file, and a very long text (5,000+ words). For each, check idea quality, JSON format, the Notion entry, and the digest.

---

## PART 12 - How to land your first 3 clients in 30 days

Week 1 is building the demo. The first client does not come from a website or cold outreach; they come from one conversation with someone who watched a 2-minute demo. Days 1 to 2, build the idea agent and run 20 tests, all passing. Day 3, record the demo in Loom: transcript loaded, 90 seconds later 5 drafts in Notion, narrate as it runs, keep it under 2 minutes.

Week 2 is publishing and distributing. Post 1 is the demo video with the caption "Built this in 2 days. One webinar into 10 ready posts automatically. Here is how it works." Post 2 is the numbers: "An expert spends 8 hours a week clipping content. This agent does the same in minutes." Post 3 is the offer: "Taking on 3 projects this month. DM me and let's see if it fits your content process."

Weeks 3 to 4 are discovery calls. Run every call with the 30-minute script above, send the proposal within 24 hours, and follow up at 48 and 72 hours.

---

## PART 13 - The roadmap to $15,000 per month

Month 1: the goal is 1 client at $2,000 per month, reached through demo, call and first contract, with 40 to 60 hours to build, and the constraint is getting that first client.

Months 2 to 3: the goal is 3 clients at $6,000 per month, driven by content bringing inbound plus a referral from client number one, with about 30 hours per month of maintenance, and the constraint is delivery speed.

Months 4 to 6: the goal is 5 clients at $10,000 per month through productized packages and templated delivery, with the constraint being systematizing the work.

Months 7 to 9: the goal is 7 to 8 clients at $15,000 per month through a referral flywheel plus upsells, with margin above 85%, and the constraint is deciding whether to stay solo or hire.

---

## PART 14 - Mistakes that kill the business early

Mistake 1, building before selling: 40 hours on a perfect agent before anyone agreed to pay. Build a demo in 2 days, sell it, and finish the real version after the contract.

Mistake 2, hourly pricing: the better you get, the less you earn, so package everything as setup plus a monthly retainer.

Mistake 3, taking every client: the worst clients have a vague problem, a low budget and high expectations, so qualify hard, because one bad client costs more than two good ones earn.

Mistake 4, no written scope: "we'll figure out the details later" always costs money, so document what the agent does, what triggers it, what it connects, and what is out of scope.

Mistake 5, no retainer: take the setup fee and walk away and you have one-off projects, not a business, because agents need monitoring and improvements, and with no retainer there is no business.

Mistake 6, skipping the test phase: run 20+ test inputs before launch, including edge cases, because the weird inputs always show up in production.

Mistake 7, building in public too early: posting "I'm starting an AI agency" with no client attracts other beginners, not clients, so build and deliver first, then post the results.

---

## PART 15 - The first 48 hours plus final call to action

Everything above is useless without action.

In hour 1, create an n8n account (n8n.io, free), create an Anthropic account (console.anthropic.com), and get the Claude API key.

In hours 2 to 8, build the idea agent using the steps above and test on 20 samples with all edge cases passing.

In hours 9 to 12, record a 2-minute demo and publish the article and the demo video.

In hours 13 to 24, reply to every comment and DM and schedule 3 discovery calls.

In hours 25 to 48, run the calls with the script, send 3 proposals within 24 hours, and follow up at 48 hours.

Every expert, course, agency and media brand has processes running on human time that should run on AI. The math works. The demand exists. The tools are ready.

The only question is whether you start this week.

Follow for AI automation breakdowns every week.

Save this, every prompt is copy-paste ready.

Like if you'd automate one of these right now.

## Media

- video: https://pbs.twimg.com/amplify_video_thumb/2064020063271665664/img/0nl4gh51Rq-B7f5d.jpg
- video: https://video.twimg.com/amplify_video/2064020063271665664/vid/avc1/720x1280/U41iBUhFhSxhAp-d.mp4?tag=27

## Capture Note

TweetDetail returned complete normal-post text.
