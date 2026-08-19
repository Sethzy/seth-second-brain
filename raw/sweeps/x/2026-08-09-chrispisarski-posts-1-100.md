---
type: raw_sweep
source_type: x_profile_timeline
url: https://x.com/chrispisarski
handle: chrispisarski
user_id: 1821911422550335488
captured_at: 2026-08-09T00:13:45+08:00
requested_count: 100
captured_count: 100
timeline_offset: 0
timeline_range: 1-100
fetched_for_offset_count: 100
retrieval_method: UserTweets
capture_quality: generated_profile_timeline_snapshot
status: staged
trust_lane: sweep
---

# X profile timeline snapshot: @chrispisarski posts 1-100

## Source

- Profile: [https://x.com/chrispisarski](https://x.com/chrispisarski)
- Timeline range: posts 1-100 at capture time
- Timeline offset: 0
- Requested posts: 100
- Captured posts: 100
- Capture method: authenticated Bird/X UserTweets timeline via Chrome Profile 3 cookies.

## Capture Notes

This is a sweep snapshot for review and synthesis. It preserves the timeline text returned by X at capture time, but durable wiki claims should cite this file and remain conservative about recency, deleted posts, or ranking differences.

## Posts

### 1. Fri Aug 07 21:51:56 +0000 2026

- URL: [https://x.com/chrispisarski/status/2085846429956763655](https://x.com/chrispisarski/status/2085846429956763655)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 20, reposts 29, likes 765

#### Verbatim Text

this is what we call "midbound" - we have done this since YC and its still one of the most effective ways to book sales demos (we run a more targeted version of it)

1. build a map of all of your competitors / creators that make content targeting your ICP

im sure there are other ways to do this but we use the crustdata MCP connected to claude and just run this skill:

"find the founders of [competitor domains] + every creator posting about [your category] in the last 14 days, and any post in that space that went viral in the last 14 days

go beyond the competitors i listed - find any account posting content niched down to my industry that is performing

give me a connection graph of all of them: how they're connected, what the biggest creator clusters are, and categorize every one of them into a specific niche based on what they post about

include likes/comments per account and make that a filter"

you will get back a map of all the relevant "accounts" within your ICP, what they post about and how much engagement they get (which we reuse for influencer marketing)

2. use this map to create hyper personalized lists:

take every comment under every post from those accounts (competitors + creators) in the last 24h, filter and categorize by relevancy and pain points, enrich all commenters using the crustdata MCP (including their email if they are within the ICP) and classify by ICP

you will end up with super personalized lists with stuff like "i have tried x before but it didn't work that well" - you can use all of that context to create the copy with claude and push it to instantly sequences

what we also did during our YC batch was set up a crustdata watcher that sends a slack notification in real-time every single time someone posts about a specific keyword / topic FILTERED by our ICP, which we then use as an opp to just comment / engage and be visible

#### Quoted Post

- URL: https://x.com/codyschneider/status/2085470980218974266
- Author: Cody Schneider (@codyschneider)

nobody wants you to know this but you can just cold email a 100,000 people in a month who liked posts on linkedin related to your product and they'll buy your solution to their pain or the desired outcome you provide

#### Media

- photo: https://pbs.twimg.com/media/HPJjeOHX0AIFWx-.png

### 2. Sat Aug 08 04:43:54 +0000 2026

- URL: [https://x.com/chrispisarski/status/2085950104406495446](https://x.com/chrispisarski/status/2085950104406495446)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 9

#### Verbatim Text

https://t.co/puirn7u4ty

### 3. Thu Jul 30 23:01:16 +0000 2026

- URL: [https://x.com/chrispisarski/status/2082964775131095480](https://x.com/chrispisarski/status/2082964775131095480)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 146, reposts 337, likes 26958

#### Verbatim Text

I still think about this tweet https://t.co/fHNvrY8OvL

#### Media

- photo: https://pbs.twimg.com/media/HOgrGNbWUAAXt07.jpg

### 4. Wed Jul 29 23:58:50 +0000 2026

- URL: [https://x.com/chrispisarski/status/2082616875280941146](https://x.com/chrispisarski/status/2082616875280941146)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 11, reposts 4, likes 58

#### Verbatim Text

always appreciate it when people enjoy/find value in the sales/GTM content

trying to take time every day and think of something good that helped us grow Crustdata

some other sales/GTM accounts I recommend following:

@jjen_abel
@TechSalesGuy
@thedealdirector 
@KyleAsay_  
@Kazanjy 
@FidelCacheFlow
@ryan_c_walsh  
@RooktoRep 
@salesxsaas 
@antinertia

#### Quoted Post

- URL: https://x.com/BoraMutluoglu/status/2082572229515358378
- Author: Bora (@BoraMutluoglu)

@chrispisarski Bro holy fuck how can you give this much value for free

### 5. Tue Jul 28 22:45:26 +0000 2026

- URL: [https://x.com/chrispisarski/status/2082236016161677644](https://x.com/chrispisarski/status/2082236016161677644)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 39, reposts 19, likes 431

#### Verbatim Text

this is how we built all of these sales/GTM workflows in-house with claude code

step 1) connect claude to all of your tools, these are the ones we use internally:

- Hubspot MCP (CRM)
- Slack MCP (team comms + alerts)
- Google Workspace CLI (docs, sheets, etc.)
- Fathom MCP (call recordings)
- Crustdata MCP (people and company data)
- Instantly MCP (outbound)

step 2) ask claude to build the workflows for you

for example..

a) ICP / TAM mapping:

- export all closed-won deals from hubspot: company, deal size, sales cycle length,...

- if you don't have any closed-won yet: use best open opps + competitors' customers (scraped from their case-study pages / G2)

- enrich all via Crustdata MCP: industry, headcount, headcount by department, geo, funding stage, tech stack, open roles,...

- ask claude to run this prompt:

"you have ./winners/ (one json per closed-won customer) and ./crm_export.csv (deal size + cycle length)

1. flag every attribute shared by 70%+ of winners, weighted by deal size

2. drop attributes any random b2b company would also match

3. write ./icp.md: hard filters (industry, headcount, geo, funding) + soft signals with weights (dept ratios, hiring, tech) + anti-icp (attributes of wins that churned or closed slow)

4. spawn a subagent to blind-score every winner against icp.md. 80% of winners must score 70+. loop until they do."

b) mail infra + warmup:

- never send cold from your main domain, buy 2-5 alternate domains to start (yourbrand-hq com, tryyourbrand com), 20-40 at scale

- 2-3 inboxes per domain. person-first names (john@, not sales@), no numbers

- dns on every domain: spf, dkim, dmarc + custom tracking domain (CNAME)

- disable open tracking, pixel hurts deliverability, track replies only

- warmup 2-4 weeks before sending anything. start 5-10/day per inbox and then start ramping up

- warmup never stops: after ramp, ~20 cold + ~30 warmup per inbox daily, 40-50 total

- capacity: 1,000 cold/day = ~50 inboxes across ~20 domains

- before every campaign: verify the list (bounce rate must stay under 2-3%) + run an inbox placement test (primary vs promotions vs spam)

- check all prospects that are behind secure email gateways (proofpoint, mimecast, barracuda). throttle or just delete those and set up a campaign on linkedin instead

c) signal-based lists:

1. reverse-engineer which signals made your prospects reply

- export your outbound history: every prospect ever contacted (instantly export + hubspot): date contacted, replied y/n, meeting y/n, won y/n + fathom as context

- for each account, reconstruct what was true ON the day you contacted them via crustdata: headcount delta the quarter before, days since last funding, open roles matching your buyer titles at that time, new VP+ hire in the prior 90 days, posts made, etc.

- ask claude to run this prompt:

"you have ./outbound_history.csv (every account ever contacted: date, replied, meeting, won)

1. for each account, reconstruct the signal state at contact date via crustdata: headcount delta prior quarter, days since funding, open roles matching [titles], exec hires prior 90 days, posts, all relevant signals

2. calculate lift per signal: reply rate with signal vs baseline reply rate

3. calculate each signal's window: median days between signal and the replies it produced

4. read the reply threads per signal and extract the angle that worked

5. write ./signals.md: only signals with 1.5x+ lift, each with: lift, window, the proven angle. everything else gets deleted, not monitored

6. verify with a subagent: hold out 20% of history, check the ranking predicts reply rate on the holdout. loop until it does"

- no outbound history yet: run the same analysis on closed-won instead (what signal states existed in the 90 days before each winner entered pipeline)

- THEN set up a watcher via crustdata that watches for these signals in real-time, and add that company to your sequence in instantly

d) lookalike lists off closed-won:

- rank customers first: ACV × speed-to-close × expansion, minus churn (using connectors)

- for each: reconstruct the company as it was when it bought, via crustdata (headcount, dept mix, funding stage, what they were hiring at that date)

- pull the fathom transcripts from that deal: why they bought, in their words, and the proxy for that pain (e.g. "drowning in manual prospecting" → SDR headcount growing with no ops hire)

- ask claude to run this prompt on every new closed-won:

"1. check the customer ranks in the top third (ACV × close speed × expansion, minus churn)

2. reconstruct the company at purchase date via crustdata, not its current state

3. read the fathom transcripts from the deal. extract the buying trigger in their words + the observable proxy (what would this pain look like from the outside)

4. crustdata search: companies matching the at-purchase profile AND the pain proxy. exclude current customers, open pipeline, closed-lost < 6 months old

5. score 1-100 on firmographic match × pain-proxy match. keep 70+, cap at 25

6. verify with a subagent: blind-mix the 25 with 25 random companies that pass basic ICP filters. it must identify the real lookalikes 80%+ of the time. if it can't, the criteria are too generic, tighten and loop"

- you can then push the list into a sheet (google workspace CLI), add it to hubspot, or send it to instantly

e) champion tracking:

- pull every contact on closed-won deals from hubspot: tagged champion/decision-maker + get more context from fathom

- resolve their emails to linkedin profiles via crustdata (batch reverse-email lookup)

- one-time backfill first: enrich all of them, diff current employer vs the deal's account

- create a crustdata watcher on each profile, set up a slack channel to get a notification every time something happens: new funding round, new hire made by that company, web traffic, posts where they mention something specific

- you can then set up claude workflows to react to every signal that is interesting for your industry

ask claude:

"pull fired watchers. for each job change:

1. enrich the new company + the new email of the champion using crustdata

2. score the new company against icp.md. below 70 → log it in hubspot, no alert

3. 70+ → create the company + contact in hubspot, tag champion-landed, assign the AE from the original deal

4. slack the AE: who they are, what they bought, the original deal size, what the new company does + a drafted first touch referencing the history using fathom as context"

these are just some of the workflows you can power by connecting your stack to claude

you can build any dream GTM/sales workflow yourself by just asking claude to go through all of these workflows and build something specific for your industry and company, with all the context it has about you

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2081846875217399998
- Author: Chris Pisarski (@chrispisarski)

4 months later and the majority of YC founders i'm speaking with are still trying to hire the person that can do all of this with AI:

- map out the entire ICP and TAM
- build signal-based lists
- build lookalike lists off closed-won accounts
- track every champion who changes jobs and route them as a new account
- watch for any signal (tech stack changes, funding, layoffs, headcount swings on named accounts) and react in real time
- set up the mail infra
- run outbound and auto route qualified leads to sales reps
- build an automated multi-touch sequence across email and linkedin
- build the inbound system end to end: creating content, filtered for the ICP, building out a creator network and distributing across linkedin
- score every inbound against past closed-won
- de-anonymize website traffic, push it into pipeline and add them to the outbound sequence
- run focused AEO efforts
- re-engage closed-lost 
- watch product usage for expansion signals automatically / add to a sequence
- analyze sales calls and create feedback loops for all reps
- auto-build a pre-call brief for every meeting on the calendar
- generate the one-pager, ROI model and proposal per deal
- build the expansion play per account
- own the CRM architecture and reporting

...and the list goes on

it's really hard to find one person who can own and maintain all of this

for a long time we had two. they built and ran every workflow above and more, and took us from 700k to millions in revenue

the team has since grown to 3

all of them have 3 things in common:

1) they understand the full sales cycle from prospecting to close
2) they're technical, or at least highly technical in how they think
3) they know how to use claude in the most efficient way (spawning /subagents that verify the output and /loop until the outcome is achieved)

and most of these workflows run for a fraction of what the equivalent sales tools cost, as long as your team builds them internally with claude code and a few external APIs

### 6. Wed Jul 29 01:06:41 +0000 2026

- URL: [https://x.com/chrispisarski/status/2082271559671013794](https://x.com/chrispisarski/status/2082271559671013794)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 5

#### Verbatim Text

if you want to set up any of these workflows, happy to do it live!

we'll throw in a bunch of test credits for the Crustdata MCP so you can try it yourself:

https://t.co/RVJTuhck7C

### 7. Mon Jul 27 20:59:08 +0000 2026

- URL: [https://x.com/chrispisarski/status/2081846875217399998](https://x.com/chrispisarski/status/2081846875217399998)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 79, reposts 56, likes 1247

#### Verbatim Text

4 months later and the majority of YC founders i'm speaking with are still trying to hire the person that can do all of this with AI:

- map out the entire ICP and TAM
- build signal-based lists
- build lookalike lists off closed-won accounts
- track every champion who changes jobs and route them as a new account
- watch for any signal (tech stack changes, funding, layoffs, headcount swings on named accounts) and react in real time
- set up the mail infra
- run outbound and auto route qualified leads to sales reps
- build an automated multi-touch sequence across email and linkedin
- build the inbound system end to end: creating content, filtered for the ICP, building out a creator network and distributing across linkedin
- score every inbound against past closed-won
- de-anonymize website traffic, push it into pipeline and add them to the outbound sequence
- run focused AEO efforts
- re-engage closed-lost 
- watch product usage for expansion signals automatically / add to a sequence
- analyze sales calls and create feedback loops for all reps
- auto-build a pre-call brief for every meeting on the calendar
- generate the one-pager, ROI model and proposal per deal
- build the expansion play per account
- own the CRM architecture and reporting

...and the list goes on

it's really hard to find one person who can own and maintain all of this

for a long time we had two. they built and ran every workflow above and more, and took us from 700k to millions in revenue

the team has since grown to 3

all of them have 3 things in common:

1) they understand the full sales cycle from prospecting to close
2) they're technical, or at least highly technical in how they think
3) they know how to use claude in the most efficient way (spawning /subagents that verify the output and /loop until the outcome is achieved)

and most of these workflows run for a fraction of what the equivalent sales tools cost, as long as your team builds them internally with claude code and a few external APIs

#### Quoted Post

- URL: https://x.com/antinertia/status/2028750956230271156
- Author: Jeddi (@antinertia)

i advise 10+ companies doing 7 to 9-fig arr

they all ask me the same question:

“who’s the best gtm/growth person we should hire?”

and i have 0 names to give

there’s a massive shortage of elite gtm/growth talent

you can see it in the market

salaries have doubled in 3 years

if you’re a GREAT gtm/growth operator, dm me

i probably have a job for you

### 8. Tue Jul 28 04:56:46 +0000 2026

- URL: [https://x.com/chrispisarski/status/2081967074184736886](https://x.com/chrispisarski/status/2081967074184736886)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 1, likes 19

#### Verbatim Text

our team built all of these workflows in-house with Claude + the Crustdata MCP + Instantly and integrated them with the rest of our entire stack (google workspace cli, hubspot, slack, etc.)

if you are this person / trying to build something similar, would love to give you access to the Crustdata API and see what you can build on top of it!

https://t.co/YVDXjePtmg

### 9. Fri Jul 24 23:37:01 +0000 2026

- URL: [https://x.com/chrispisarski/status/2080799444635697279](https://x.com/chrispisarski/status/2080799444635697279)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 1, likes 37

#### Verbatim Text

"AI services" gets thrown around a lot these days

here's how we built our AI services arm at @crustdata & generated enough revenue to know it's the future:

a few months ago we saw a rapid shift toward companies wanting to build products in-house

but despite all the hype around replacing SaaS, there are usually some blockers

prospects:

- don't know where to start, or what "it" should look like
- don't know how to go about building it
- lack the resources to build and maintain it

taking all of that into account, we adapted the "palantir model" for sales and ran an experiment: what if we still sell our data/APIs, but also help deploy these workflows for our customers?

we started in recruiting, sat down with talent teams and codified their entire sourcing workflow into a claude skill, powered by our MCP for candidate search + contact info

we've now done this enough times that AI labs, big-tech recruiters, and hundreds of recruiting agencies are using our skill + MCP to power their entire sourcing inside claude

there are probably hundreds of similar workflows you can find in the usage data

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2080390720012054713
- Author: Chris Pisarski (@chrispisarski)

so anthropic open-sourced their claude usage data?

if i had to start a new company today, i'd spend the next 24h going through all of it

find the fastest growing use-cases getting adoption inside companies

then start an AI services agency that deploys those workflows

for example:

> 20% of US claude usage is content creation and copywriting

1) start a claude-first content agency, help companies build an in-house content machine on top of claude 

2) reach out to content leads and CMOs at funded b2b companies:

"hey x, 20% of US claude usage now goes into content creation according to anthropic's new usage report from this month...

we  help companies build and deploy a claude-powered in-house content machine across the org. we've done this with a few others already. curious if you'd be down to see how that looks?"

you'll get revenue faster than most "startups" out there

there are probably 100s of workflows like this in the usage data

### 10. Thu Jul 23 20:32:54 +0000 2026

- URL: [https://x.com/chrispisarski/status/2080390720012054713](https://x.com/chrispisarski/status/2080390720012054713)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 15, reposts 12, likes 209

#### Verbatim Text

so anthropic open-sourced their claude usage data?

if i had to start a new company today, i'd spend the next 24h going through all of it

find the fastest growing use-cases getting adoption inside companies

then start an AI services agency that deploys those workflows

for example:

> 20% of US claude usage is content creation and copywriting

1) start a claude-first content agency, help companies build an in-house content machine on top of claude 

2) reach out to content leads and CMOs at funded b2b companies:

"hey x, 20% of US claude usage now goes into content creation according to anthropic's new usage report from this month...

we  help companies build and deploy a claude-powered in-house content machine across the org. we've done this with a few others already. curious if you'd be down to see how that looks?"

you'll get revenue faster than most "startups" out there

there are probably 100s of workflows like this in the usage data

#### Quoted Post

- URL: https://x.com/claudeai/status/2079979809606664564
- Author: Claude (@claudeai)

You can now ask Claude about the Anthropic Economic Index, our public dataset measuring how AI is used across the economy.

Ask which occupations use AI the most, or what kinds of tasks people are automating, and the answers draw directly from the Index data. https://t.co/21DKJTJmrz

#### Media

- photo: https://pbs.twimg.com/media/HN8GqhMWsAA1lWE.jpg

### 11. Wed Jul 22 20:10:11 +0000 2026

- URL: [https://x.com/chrispisarski/status/2080022615578517676](https://x.com/chrispisarski/status/2080022615578517676)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 5, reposts 3, likes 41

#### Verbatim Text

every sales rep at Crustdata has an unlimited dinner budget for "high-potential" accounts

personal relationships are the single biggest lever in sales

every expansion, closed deal, renewal is easier once a personal connection has been built

it doesn't matter how good your product is , if the person behind the screen can't trust you at all

and personal connections can only be built when you meet people in-person

this is why we encourage our GTM team to get in front of customers/prospects as often as possible

after one dinner, the goal is the second dinner, a cascading waterfall of meet-ups at their favorite spots

people don't say no to this

and it doesn't have to be a dinner, it can be an in-person office visit, a coffee, a courtside seat at a game, a drink after a conference... whatever it takes to meet in person

the focus is "in-person"

realizing that the more upmarket we move, the more important these relationships are

### 12. Thu Jul 16 22:18:44 +0000 2026

- URL: [https://x.com/chrispisarski/status/2077880639055941693](https://x.com/chrispisarski/status/2077880639055941693)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 12, reposts 8, likes 156

#### Verbatim Text

even Anthropic is hiring BDRs to do outbound sales

one of the best-performing cold email copy formats we use to run our own cold outreach is the "creative idea'" email

instead of pitching your own product, you email a prospect 2-3 hyper-specific campaign/growth ideas for their business, then tie it back to how you'd help them pull it off:

"Hey [name], I had some ideas about how we could target [their customer type] together, here's what I'm thinking," then the idea(s), value prop, CTA

it can be very short:

"Hey Olipop,

Quick idea. We could reach out to gyms and boutique fitness studios that don't stock Olipop yet and get it into their fridges as the "healthy soda" for post-workout

Worth testing?"

or longer:

"Hey Olipop,

Had a few ideas for getting in front of new buyers:

1) Email gyms/studios that don't stock it yet for their fridges
2) Target corporate offices for kitchens + vending
3) Reach out to college campus stores for the Gen Z crowd

We'd run the whole outbound for you. Of course we can do other things too, let me know if any of these are interesting!"

And you can automate the entire workflow using Claude (to come up with the ideas), Crustdata MCP (to feed Claude everything about the company + person, their focus, what they sell, contact info) and the Instantly MCP to send out the emails

#### Media

- photo: https://pbs.twimg.com/media/HNYUSxTWYAApA84.jpg

### 13. Wed Jul 15 21:24:04 +0000 2026

- URL: [https://x.com/chrispisarski/status/2077504495991558179](https://x.com/chrispisarski/status/2077504495991558179)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 9, reposts 0, likes 44

#### Verbatim Text

some people just love doing sales 

we're currently hiring for an AE to join our team at @crustdata so I reached out to someone who did an incredible job trying to sell us his product a while ago

this was his reply

he just keeps going no matter what

as a salesperson, you're either

1) motivated by money (getting that commission, fighting hard for that deal..)

2) motivated by meeting/ talking with people (our former YC founder turned AE is one of them, he just loves helping other people, he's teaching a class about entrepreneurship at Columbia every Saturday)

3) in love with sales and going through the entire process, following up, asking the right questions, figuring it out (a very tiny % would count for this)

you need to be in one of these 3 categories if you're trying to make it in tech sales

#### Media

- photo: https://pbs.twimg.com/media/HNTD1ORW0AA2p7v.jpg

### 14. Tue Jul 14 21:00:36 +0000 2026

- URL: [https://x.com/chrispisarski/status/2077136203770429650](https://x.com/chrispisarski/status/2077136203770429650)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 7, likes 111

#### Verbatim Text

"we could have executed more big bets if we had had a single person owning & iterating on them. Former successful founder profile with drive and speed"

+1

seems obvious but hiring former founders for early sales/GTM is very underrated

not only because of the speed (which is needed in an earlier stage, just taking more calls & closing deals faster)

but also because they are incredible at making bets and iterating very quickly

we had our first $1M month because of a bet started by an ex-YC founder turned AE (using the @crustdata  MCP to power internal recruiting use cases)

he recorded personalized looms for hundreds of our customers, explained the use case and managed to expand accounts

also hired someone to build out the Claude skills for us and (with the help of our growth team) got us enough traction to justify us spending more time and resources on this new ICP

you need to hire quicker but also look out especially for entrepreneurial/ex-founder talent, they can change the trajectory of your company

#### Quoted Post

- URL: https://x.com/Carles_Reina/status/2077075493946597749
- Author: Carles Reina (@Carles_Reina)

If I had to restart @ElevenLabs GTM from scratch, these are the things that I would change 🖊️ 

- Hire quicker. I was alone selling for the first 9 months because I believed we didn't have PMF. Main reasons: the AI tourist external mantra of 2023, and the uphill battle convincing everyone to hire more GTM (Sales development, Sales, Customer Success) because we were still mostly PLG / self-service. The hiring constraint lasted until earlier this year when we boosted our team to meet demand.

- Build an enablement team earlier. Sales enablement has such an important role in an org, and we mostly think about it when we hire a lot of people. The reality is that we need Enablement earlier due to the speed of product iteration.

- Open more markets. The results from Uber v Lyft operating models played a key role in deciding to open markets early, but I would triple down on it if we were to start over. 

- Have more big bets. Similar to VCs, you only need 1 big bet to work in order to generate Alpha. We could have executed more big bets if we had had a single person owning & iterating on them. Former successful founder profile with drive and speed.

- Be more vocal about product ROI & our success. People buy from people, and companies buy based on success & ROI. In AI, we've all been slow showing ROI. This should be the key number when you start a conversation. 

- Hire senior sellers. In startups, we've been told that culture is everything and someone with +25y experience may struggle to fit in. This is bullshit. The experience, connections and drive +25y sellers bring is crazy. We have a bunch today, but I would hire many more earlier.

- Reduce cash commissions and replace them with more equity. Cash is king, but Equity is queen. Queens also rule countries, so why not make Equity the dominant one in GTM? 

- Open more offices. We are a remote-first company, but our customers are everywhere, and employees want to meet each other. I would open more offices to be embedded in markets quicker. 

- Fun brand. Brand perception is 33% of the work. Building a fun brand adds quickly. 

- Outbounds outbounds outbounds. We waited too long to migrate to an Outbound organisation. I would do it from day 1 now.

- Pipeline construction with more whales. The ideal pipeline needs to have a combo of segments to reduce risk, improve results and provide liquidity. We waited too long to pitch & bring whales. 

- Not all deals are good deals. We, sellers, want to close a lot of ARR, but it is important to split early on between good vs bad deals.

Thank you to Tomasz Gmur for asking how I would do GTM again!

### 15. Mon Jul 13 20:27:34 +0000 2026

- URL: [https://x.com/chrispisarski/status/2076765500890337614](https://x.com/chrispisarski/status/2076765500890337614)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 0, likes 79

#### Verbatim Text

simple sales hack: disqualify prospects before taking demo calls and help them with what they're trying to solve

someone books a demo, you read their notes and it's v clear they're not a fit

don't take the call

just email them and let them know what the better fit for their use-case would be 

we've seen so many prospects come back months later with a qualified use-case for @crustdata or refer us in their network, which is worth far more

it's something that you just don't expect from companies nowadays

potential copy to bookmark:

"Hey [name],

Thanks for signing up for a [company] demo!

From what you shared, I'd actually point you toward [better-fit solution] - that's a better fit for what you're trying to achieve.

[explaining what your company does & how that is different]

Nevertheless, thanks for taking the time to sign up.

Also, just had a look at your page and wanted to say that I love [...] :)

If there's ever anything I can help with now or in the future, please let me know!"

#### Media

- photo: https://pbs.twimg.com/media/HNId9gSXAAAyJCx.jpg

### 16. Thu Jul 09 20:50:23 +0000 2026

- URL: [https://x.com/chrispisarski/status/2075321693233410382](https://x.com/chrispisarski/status/2075321693233410382)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 15, reposts 7, likes 274

#### Verbatim Text

our entire GTM/sales operation that got us our first $1M month is run by just 3 people

1) one person focused on inbound (most of our demos come inbound: socials, google, content, referrals)

- creating and distributing content across every channel and constantly tweaking it based on impact/results, this person built our own in-house platform that generates content from our data and distributes it to hundreds of accounts and sites daily

- building and maintaining a creator and partnerships network

- everything SEO and AEO, there's a lot to unpack here (we're also working with an agency on the AEO side)

- building out tools and making them go viral

2) one person focused on outbound

- we are focused on targeted value-based outbound powered by claude, only a few companies are doing that the way he is doing it (e.g. building  out custom platforms and tools for prospects just to reach out to them,...) this person set a completely new bar

- he runs everything solo and in-house (domain health, sequencing, ICP targeting, list building, signals, building out the tools, etc.) using claude, the Crustdata MCP, and a sequencing tool

3) one person focused on experiments

- how can you grow exponentially without making bets that can lead to exponential results? we created a role focused on finding and launching these bets

- some of our most creative campaigns came out of this, including one that closed a big 4 customer. another one was betting that building custom claude skills for recruiting teams (using our MCP) would open up larger opportunities, which is now one of the biggest use-cases for the crustdata MCP

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2074962469907304498
- Author: Chris Pisarski (@chrispisarski)

we just had our first ever $1M month at @crustdata

the potentially defining factor: 30 days ago, I told all of our sales reps to cancel as many calls as they could

after spending hours going through every Fathom recording from the past few months, I asked our team to disqualify prospects faster and more aggressively, even before taking a call

we were wasting hours a day on calls that were never going to close, this includes the ime debt of context switching

there is a lot that you can do wrong here, this is what helped us get there:

1) build tools to qualify your prospects

we built an internal tool off all our closed-won deals, grouped by ICP. It tells us the probability a new prospect closes and pulls the closest lookalikes to customers we already won.

talking to a brand new ICP is very exciting, but at volume it comes down to focus. we chose to focus on the ICPs we know we will win

2) disqualify as fast as possible

we try to DQ a prospect in the first 2 minutes, ask them to rate the pain 1 to 10, ask when they'd sign if it worked out, bring up pricing

the harder we try to DQ someone, the harder they pitch us on why they think they need our solution, it saves everyone time, there is no downside to that. we DQ before the call many times, even if it's uncomfortable

3) offer them the right solution

we either point them to self-serve or send them the service or tool we think is the likely fit for what they are trying to solve, the reactions/relationships we get from doing that are amazing

### 17. Fri Jul 10 01:19:57 +0000 2026

- URL: [https://x.com/chrispisarski/status/2075389529255538888](https://x.com/chrispisarski/status/2075389529255538888)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 6

#### Verbatim Text

hosting a live session with our 3-person growth team to break down how they do it &amp; chat about how to run growth/GTM nowadays

join us:
https://t.co/oNXVUeWTeU

### 18. Wed Jul 08 21:02:58 +0000 2026

- URL: [https://x.com/chrispisarski/status/2074962469907304498](https://x.com/chrispisarski/status/2074962469907304498)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 17, reposts 4, likes 179

#### Verbatim Text

we just had our first ever $1M month at @crustdata

the potentially defining factor: 30 days ago, I told all of our sales reps to cancel as many calls as they could

after spending hours going through every Fathom recording from the past few months, I asked our team to disqualify prospects faster and more aggressively, even before taking a call

we were wasting hours a day on calls that were never going to close, this includes the ime debt of context switching

there is a lot that you can do wrong here, this is what helped us get there:

1) build tools to qualify your prospects

we built an internal tool off all our closed-won deals, grouped by ICP. It tells us the probability a new prospect closes and pulls the closest lookalikes to customers we already won.

talking to a brand new ICP is very exciting, but at volume it comes down to focus. we chose to focus on the ICPs we know we will win

2) disqualify as fast as possible

we try to DQ a prospect in the first 2 minutes, ask them to rate the pain 1 to 10, ask when they'd sign if it worked out, bring up pricing

the harder we try to DQ someone, the harder they pitch us on why they think they need our solution, it saves everyone time, there is no downside to that. we DQ before the call many times, even if it's uncomfortable

3) offer them the right solution

we either point them to self-serve or send them the service or tool we think is the likely fit for what they are trying to solve, the reactions/relationships we get from doing that are amazing

### 19. Wed Jul 01 19:23:05 +0000 2026

- URL: [https://x.com/chrispisarski/status/2072400619756028210](https://x.com/chrispisarski/status/2072400619756028210)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 103, reposts 27, likes 918

#### Verbatim Text

this is now what companies expect from salespeople

our entire sales/GTM team has access to unlimited claude tokens

they all have pre-made claude skills that they can run:

=> org chart maker: internal claude skill that builds a full org chart for you (who reports to who, who owns the budget, who the champion is vs the blocker,etc..)

=> pre-call research briefs connected to your calendar: every morning claude reads your calendar and sends you a daily report of everyone you have a demo with today, including the company (funding, hiring, tech stack, job openings, web traffic, recent news...) and the person you're talking to (their career history, what they've posted about, mutual connections...)

=> meeting follow-up: after calls, you get the recap email drafted in your voice, and the CRM notes filled in with the next steps logged

=> inbound lead triage: scoring inbound leads against your ICP with company + funding + headcount + everything else and giving you a percentage of how likely they are to close based on all the closed-won deals you've had before

=> trigger-based outreach: claude watches your accounts for job changes, new funding rounds, exec hires etc. and the minute it happens it can draft a relevant email. you can also add the sequencing part (with instantly for example) via claude

=> list building / prospecting: our reps build their lists and signals using claude and the crustdata MCP

and so many more workflows (proposal + one-pager generator, competitive research, multithreading maps, discovery call prep, lost deal analysis, etc.)

we have an internal library of claude skills that everyone is using, happy to share via DM if you're curious to try it out!

#### Quoted Post

- URL: https://x.com/NotionHQ/status/2071723944441466986
- Author: Notion (@NotionHQ)

Skip the resume. Seriously.

We're hiring SDRs and BDRs. To apply, just build an agent a sales team would actually use.

Apply by July 15 (tag your friends):  https://t.co/WYyaJSp3D0 https://t.co/JNmazdWMZH

### 20. Wed Jul 01 23:04:04 +0000 2026

- URL: [https://x.com/chrispisarski/status/2072456230790897984](https://x.com/chrispisarski/status/2072456230790897984)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 18

#### Verbatim Text

i'm going through the DMs right now and sharing the skills, apologies if it takes some time!!

if you're interested in seeing a live demo of how these skills work combined with the Crustdata MCP, let's chat!

https://t.co/puirn7u4ty

### 21. Mon Jun 29 17:44:55 +0000 2026

- URL: [https://x.com/chrispisarski/status/2071651138336620705](https://x.com/chrispisarski/status/2071651138336620705)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 1, likes 60

#### Verbatim Text

we hit all our 2-week revenue goals during YC using these sales tactics

here's what you should do during a demo:

1) know their process inside out - what are they trying to build? be able to explain it very clearly after the call

2) know what's broken with their current process or provider

e.g. "what made you start looking for something new? what does your current workflow look like? what have you tried so far to fix it?"

3) know what they want to see in the trial and what they expect from it

4) get a call on the calendar for the end of the trial and create urgency

5) if they push back on anything, understand the underlying why. there's always a solution, but it's worth going deeper into discovery here

e.g. "we don't want to commit to annual." why? product not ready? need funding first? once you know, you can tailor a solution

do all of this consistently and you'll close

### 22. Fri Jun 26 16:57:21 +0000 2026

- URL: [https://x.com/chrispisarski/status/2070552005022556532](https://x.com/chrispisarski/status/2070552005022556532)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 8, reposts 2, likes 84

#### Verbatim Text

one of the best sales advice we picked up during YC is the "time-to-first-value" method

every prospect cares about solving 2-3 workflows

long discoveries are helpful for bigger deals, but we've found that showing value as fast as possible works best

what we usually do is always ask this:

"what would this platform need to show you to prove it can solve your problem?"

they tell you exactly the value they expect and your job is to show it to them as fast as possible

it's also much easier to do now with claude, many of our prospects want to see the full depth of our data, so we started running queries that they give us live on calls with Claude connected to our MCP

for recruiters that might be a live search on a JD they share on the call, or finding a warm intro to a prospect live..

for every demo, they will get at least the value that they expected from booking a call with us

it's also a good follow-up method: if you run a query live with a prospect, you can share the results in the call but also after the call as a follow-up to get the deal moving

### 23. Thu Jun 25 20:13:49 +0000 2026

- URL: [https://x.com/chrispisarski/status/2070239057733665051](https://x.com/chrispisarski/status/2070239057733665051)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 0, likes 56

#### Verbatim Text

i don't think people understand how much value Anthropic/Claude has yet to capture

after coding, the largest area of value increase is in sourcing, for both recruiting and sales.

we're now working with internal recruiting teams at Fortune 500s and they all want to use us for one reason: 

automating sourcing via Claude using the Crustdata MCP

it's an AI service, you work together with their recruiting teams to build out their own Claude skills based on the way they source, create their workflows and add custom integrations into their ATS or CRM, all powered by Claude

with every new search they make, the results get better.

the global recruiting/staffing industry is valued at $640–860 billion.

what happens when Claude can source better, more accurately, and exactly the way a recruiter wants to that entire industry?

#### Quoted Post

- URL: https://x.com/BenyaminHolley/status/2022821111067533369
- Author: 🏍benyamin (@BenyaminHolley)

i'm about to put our recruiting team out of a job.

we have 31 open roles at AirOps right now. instead of paying a recruiter $30K per placement, i built a system that mines my own LinkedIn network (10K connections) against every open JD.

exported my full LinkedIn data dump into SQLite. scraped all 31 job descriptions from our Ashby board into structured JSON. built a two-tier matching engine — tier 1 does keyword matching on titles, companies, and skills (fast, free). tier 2 uses exa for cheap linkedin enrichment, then claude code scores enriched profiles against each role: work history, tenure, location, tech stack overlap.

top-tier candidates get deeper enrichment through leadmagic, and the system drafts personalized LinkedIn DMs based on why that specific person is actually a fit.

i'm already connected to these people. they already know who i am. a warm DM from me converts at a completely different rate than a cold InMail from a recruiter.

the system scores candidates so i'm not guessing — it tells me "Maya is a 47/50 match for Senior AI Engineer because she built RAG pipelines at Notion and has 7 years in ML." i review the context and hit send.

recruiter fee for 31 roles: ~$500K 
my system: ~$40 in API calls

time to break my comp plan

btw Airops is trying to 3x headcount this year if you want to join a rocketship 👀

### 24. Wed Jun 24 21:22:02 +0000 2026

- URL: [https://x.com/chrispisarski/status/2069893837368311958](https://x.com/chrispisarski/status/2069893837368311958)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 39

#### Verbatim Text

this is how to sell to YC startups

when you join YC, you get a flood of deals and offers from companies handing you free credits for months, sometimes years

they compete for YC startups because they know a few will eventually grow big enough to make it worth it - imagine powering Airbnb just when they were getting started (and making them build their product on top of your offering)

when a deal comes to an end, the startup has to make a decision: sign a new contract with the vendor they had, or switch to another one

most vendor lock-ins don't really matter nowadays (with good enough planning), it's something you can negotiate with competing vendors (they'll dedicate time and give you a better deal to help you migrate off your current provider)

but to even be considered in this evaluation phase (multi million figure contracts) where the decision gets made, all you have to do is reach out

if you reach out to the right person at the right time, it doesn't matter how good your copy is or how many customers you have, you will get a reply

no one wants to make a bad decision, so you'll get added to the shortlist of vendors

there's a company that figured out exactly when our deal would expire, and they've been reaching out to us ever since, constantly, through every possible channel

we're now looking to move forward with them

one cold email to the right person at the right time, can close millions in revenue

this is also why our Watcher API has become one of our most successful products, you can watch any company in real time and get notified the moment something changes (someone drops their company name from their headline = likely just laid off, a new VP of engineering starts = new budget and a fresh vendor decision), just seconds after making that change to their profile

the sooner you reach out, the better

#### Media

- photo: https://pbs.twimg.com/media/HLm80x0WsAAc5Hd.jpg

### 25. Tue Jun 23 21:02:35 +0000 2026

- URL: [https://x.com/chrispisarski/status/2069526554502459689](https://x.com/chrispisarski/status/2069526554502459689)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 5, likes 86

#### Verbatim Text

this is how to get your first 10 customers according to the new YC sales video:

1) decide which channels are worth the effort by answering these questions about your buyer:

what does their average day look like?

how often do they check their email?

do they go to conferences?

where can you find them organically?

where do they source recommendations?

be very strategic about it => linkedin/email are only great for some buyers, one YC founder closed more at a 3-day trade show than in 3 months of cold email

2) before doing any outreach, find your warm paths aka customer origins. these are people like:

friends in the industry
former colleagues
classmates from school
people one intro away

the first 3 customers usually always come from here since they don't trust the product yet, they trust you

small note: you can also do this at scale:

a) export your linkedin connections → settings → data privacy → get a copy of your data → "connections only"

b) drop the csv file into claude as context and connect the crustdata mcp

c) ask claude to enrich every single connection through crustdata → it pulls their full work history, education, current role, recent posts, everything

you now have an internal database of your entire team's extended network, fully enriched + fully searchable in claude

3) customers 4–10 = doing things that don't scale. e.g.:

flying out in person to meet a prospect or just showing up at their office

founder dinners / happy hours for 6–10 ICP people (converts way better than big conferences dinner)

booking 15-min back-to-back meetings at a small industry conference

4) go where your ICP complains: reddit, fb groups, discord, niche forums, wherever the people you defined in step 1 are talking about their problems. 

post in these threads and DM the commenters.

5) be strategic about framing an early product

ask for advice / a review / mentorship instead of just pitching

one YC founder paid lawyers $100–200/hr for "feedback" and some of them converted to customers

6) outbound: don't let AI write your outreach (or use tools that don't make it sound like AI), keep it short with a very clear cta, offer value first, always follow uP

### 26. Mon Jun 22 20:12:19 +0000 2026

- URL: [https://x.com/chrispisarski/status/2069151516427006324](https://x.com/chrispisarski/status/2069151516427006324)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 0, likes 19

#### Verbatim Text

we're currently hiring for an Account Executive to join our sales team

the entire search is now powered by a Claude skill

if you've ever hired salespeople, you know how much noise there is. everyone hits and exceeds their quota, and if they didn't, well, then no one on their team did either. that goes for President's Club too, it's a good indicator for sure, but not always

it's hard to know if someone actually crushed it so far, and most hires (at least from my experience) end up being referrals

so we built a skill in Claude called /find-reps, it uses the Crustdata MCP for the data and it can 

- pull every rep at a company

- read the quota numbers off their profiles (which a lot of AEs add)

- benchmark each person against the rest of the reps at their company

for example: how many reps hit 140% of quota last quarter? how big is the sales team? how fast did it grow?

we then combine that with company-level search, finding teams/companies that scaled a product extremely fast, even without a great brand/logo behind them

it's been really good so far at surfacing great candidates, which is not easy with this much noise for a role like this

#### Media

- photo: https://pbs.twimg.com/media/HLcaVWCWQAAOlsB.jpg

### 27. Fri Jun 19 20:38:53 +0000 2026

- URL: [https://x.com/chrispisarski/status/2068071040299794566](https://x.com/chrispisarski/status/2068071040299794566)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 1, likes 40

#### Verbatim Text

we also built our entire sales inbound qualification and enrichment flow this way

you don't need to spend thousands on an inbound qualification system. you can build your own with Claude Code and one external API:

1) create a Slack app. Go to api-slack-com/apps, "Create New App“, choose "From scratch", name it something like "Inbound Enricher" and pick your workspace. under "OAuth & Permissions" add the bot scopes chat:write, channels:read, and channels:history, then install the app to your workspace. copy the Bot User OAuth Token from the top of that page (it starts with xoxb-) and copy your signing secret from "Basic Information"

2) create a Slack channel called inbound-leads and invite the bot into it. wire your website demo form so each submission sends a notification into that channel, either through a webhook or whatever your form provider gives you (you can also ask Claude Code to help set this up)

3) add the Crustdata API and ask Claude to write a script for your bot to reverse-enrich every signup with it, the call looks like this:

Business email:

curl -X GET "api-crustdata-com/screener/person/enrich?business_email=&enrich_realtime=true" -H "Authorization: Token auth_token" -H "Accept: application/json, text/plain, */*" -H "Content-Type: application/json"

Personal email:

curl -X GET "api-crustdata-com/screener/person/enrich?personal_email=test@email" -H "Authorization: Token auth_token" -H "Accept: application/json, text/plain, */*" -H "Content-Type: application/json"

Paste this prompt:

"Build me a Slack bot that watches inbound-leads for new demo signups. For each one, pull the email and run it through the Crustdata person enrich endpoint above. If it's a business email, use the business_email parameter, otherwise fall back to personal_email. From the response, pull the person's name, role, how long they've been at the company, what they did before, and what they've been posting about lately. Then enrich the company around them: web traffic and whether it's climbing or falling, the last funding round and who's behind it, headcount and hiring pace, the roles they're filling right now, and recent news. Grab the confidence score on the match too. Post all of it back to inbound-leads as a clean card, person up top, company snapshot below, recent news at the bottom. If the email doesn't map to a real person, flag the lead as unqualified"

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2067727763415658725
- Author: Chris Pisarski (@chrispisarski)

all of our sales reps now run this Claude Code routine before every demo call

here's how to build it yourself:

1) Download the Claude desktop app, it doesn't work in the browser version

2) Open Claude Code, go to Routines, then New routine, and name it something like "Daily sales call brief"

3) Create a Slack channel for the briefs to land in (sales-briefs for example). You can also have it write a Google Doc that gets emailed to you each morning if you don't use Slack

4) Copy paste this in as the instructions:

"Each morning, look at every meeting on my calendar for today and build a pre-call brief for each one

For the company, use Crustdata to pull: web traffic and whether it's trending up or down, the last funding round and who's backing them, headcount and how fast they're hiring, the roles they're hiring for right now, and any recent news or social posts that hint at what they care about.

For each attendee, pull their role, how long they've been there, what they did before, and what they've been posting about lately.

Then write me a brief covering who these people are, what they probably care about, where we fit, and any recent trigger worth bringing up live.

Add 5 to 7 discovery questions written for this exact account and stage, not generic ones.

Post each brief to sales-briefs. If I've got nothing booked today, just tell me"

5) Set it to run every morning

6) Connect the MCPs it needs: Google Calendar, Slack, and Crustdata for the company and people data

7) Run it with Opus 4.8, then let it run

we also added a feedback loop, you can just build a second routine that runs after calls and paste this in as its instructions:

"After each of my sales calls today, pull the Fathom (or any other AI notetaker) transcript for it and compare it against that morning's pre-call brief. Check which of the discovery questions  got asked and which I skipped. Note any objections that came up, anything the prospect cared about that we didn't predict, and the next steps we agreed on. Then write a short follow-up email I can send, log the next steps and a quick deal summary into HubSpot, and post a recap in sales-briefs. Keep a running list of what the briefs keep missing, and use it to make tomorrow's briefs better"

#### Media

- photo: https://pbs.twimg.com/media/HLNDpbrWwAAHVcP.jpg

### 28. Thu Jun 18 21:54:49 +0000 2026

- URL: [https://x.com/chrispisarski/status/2067727763415658725](https://x.com/chrispisarski/status/2067727763415658725)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 10, reposts 1, likes 108

#### Verbatim Text

all of our sales reps now run this Claude Code routine before every demo call

here's how to build it yourself:

1) Download the Claude desktop app, it doesn't work in the browser version

2) Open Claude Code, go to Routines, then New routine, and name it something like "Daily sales call brief"

3) Create a Slack channel for the briefs to land in (sales-briefs for example). You can also have it write a Google Doc that gets emailed to you each morning if you don't use Slack

4) Copy paste this in as the instructions:

"Each morning, look at every meeting on my calendar for today and build a pre-call brief for each one

For the company, use Crustdata to pull: web traffic and whether it's trending up or down, the last funding round and who's backing them, headcount and how fast they're hiring, the roles they're hiring for right now, and any recent news or social posts that hint at what they care about.

For each attendee, pull their role, how long they've been there, what they did before, and what they've been posting about lately.

Then write me a brief covering who these people are, what they probably care about, where we fit, and any recent trigger worth bringing up live.

Add 5 to 7 discovery questions written for this exact account and stage, not generic ones.

Post each brief to sales-briefs. If I've got nothing booked today, just tell me"

5) Set it to run every morning

6) Connect the MCPs it needs: Google Calendar, Slack, and Crustdata for the company and people data

7) Run it with Opus 4.8, then let it run

we also added a feedback loop, you can just build a second routine that runs after calls and paste this in as its instructions:

"After each of my sales calls today, pull the Fathom (or any other AI notetaker) transcript for it and compare it against that morning's pre-call brief. Check which of the discovery questions  got asked and which I skipped. Note any objections that came up, anything the prospect cared about that we didn't predict, and the next steps we agreed on. Then write a short follow-up email I can send, log the next steps and a quick deal summary into HubSpot, and post a recap in sales-briefs. Keep a running list of what the briefs keep missing, and use it to make tomorrow's briefs better"

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2065138536400015727
- Author: Chris Pisarski (@chrispisarski)

ok we just set up a new sales workflow to test it out

it's all powered by claude. every day it analyzes every meeting our reps have, enriches the company and the attendees (web traffic, funding, social posts,….), and writes a pre-call brief the reps can use for the demo

it also writes the specific questions to ask and flags where they need to do more discovery

all running on claude with slack, crustdata and hubspot MCP integrations

### 29. Fri Jun 19 12:37:13 +0000 2026

- URL: [https://x.com/chrispisarski/status/2067949825388126683](https://x.com/chrispisarski/status/2067949825388126683)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 6

#### Verbatim Text

Crustdata MCP for Claude:

https://t.co/WUv5OV1PMQ

### 30. Mon Jun 15 19:31:20 +0000 2026

- URL: [https://x.com/chrispisarski/status/2066604487372857477](https://x.com/chrispisarski/status/2066604487372857477)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 10, reposts 3, likes 148

#### Verbatim Text

some very simple GTM/sales advice for early startups:

1) get every customer AND prospect into a shared Slack channel

it's worth it. the moment someone's in a channel with you, you're part of their org. there's a reason Salesforce paid what they did for Slack. they know exactly how much power a Slack channel has

2) ask for a number on your demo form

we did this too late. since adding it + enriching the phone numbers using our own API, our conversion rates have been increasing by a considerable %, especially for larger deals with many stakeholders. at some point you have to move the convo into this channel

3) build three things at once: content, outbound, SEO

you need a real plan for all three, and they all feed each other:

- content: post daily on LinkedIn, and mostly only LinkedIn. connect with the ICP you're targeting so they actually see your posts, if you start from 0, post lists

- outbound: invest time in creating a good list with signals+ authentic copy. don't let AI write it. go for volume early on

- SEO/GEO: invest in GEO. a large % of our signups now come from AI search engines. the earlier you figure that out, the better. I have seen smaller startups get extremely good at this and pull in a lot of signups because of it

### 31. Sat Jun 13 01:07:37 +0000 2026

- URL: [https://x.com/chrispisarski/status/2065601954756128941](https://x.com/chrispisarski/status/2065601954756128941)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 19

#### Verbatim Text

no more warm intros

"we must abruptly disable Fable 5 and Mythos 5 for all our customers" https://t.co/OqFuzC2XUM

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2064448900057235743
- Author: Chris Pisarski (@chrispisarski)

ok so Claude Fable 5 is really really good at finding warm intro paths for sales/GTM

we have an internal benchmark/skill that uses our MCP for the data but gives claude freedom on picking the right filters and being creative

i asked it to find me a warm connection at McKinsey. it found people who studied at the same school, same year, worked at the same jobs,  engaged with my content before & built a full map

by far the best warm intro paths a claude model has found so far

#### Media

- photo: https://pbs.twimg.com/media/HKp9k7_WwAEMlYo.jpg

### 32. Thu Jun 11 18:26:10 +0000 2026

- URL: [https://x.com/chrispisarski/status/2065138536400015727](https://x.com/chrispisarski/status/2065138536400015727)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 1, likes 33

#### Verbatim Text

ok we just set up a new sales workflow to test it out

it's all powered by claude. every day it analyzes every meeting our reps have, enriches the company and the attendees (web traffic, funding, social posts,….), and writes a pre-call brief the reps can use for the demo

it also writes the specific questions to ask and flags where they need to do more discovery

all running on claude with slack, crustdata and hubspot MCP integrations

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2064448900057235743
- Author: Chris Pisarski (@chrispisarski)

ok so Claude Fable 5 is really really good at finding warm intro paths for sales/GTM

we have an internal benchmark/skill that uses our MCP for the data but gives claude freedom on picking the right filters and being creative

i asked it to find me a warm connection at McKinsey. it found people who studied at the same school, same year, worked at the same jobs,  engaged with my content before & built a full map

by far the best warm intro paths a claude model has found so far

#### Media

- photo: https://pbs.twimg.com/media/HKjW-2jW4AARbmF.jpg

### 33. Tue Jun 09 20:45:48 +0000 2026

- URL: [https://x.com/chrispisarski/status/2064448900057235743](https://x.com/chrispisarski/status/2064448900057235743)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 24, reposts 20, likes 667

#### Verbatim Text

ok so Claude Fable 5 is really really good at finding warm intro paths for sales/GTM

we have an internal benchmark/skill that uses our MCP for the data but gives claude freedom on picking the right filters and being creative

i asked it to find me a warm connection at McKinsey. it found people who studied at the same school, same year, worked at the same jobs,  engaged with my content before & built a full map

by far the best warm intro paths a claude model has found so far

#### Quoted Post

- URL: https://x.com/claudeai/status/2064394146916229443
- Author: Claude (@claudeai)

Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use.

Its capabilities exceed those of any model we’ve ever made generally available. https://t.co/2AvmEjHIX8

#### Media

- photo: https://pbs.twimg.com/media/HKZlVG1WMAEf3_i.jpg

### 34. Mon Jun 08 19:35:53 +0000 2026

- URL: [https://x.com/chrispisarski/status/2064068917715193931](https://x.com/chrispisarski/status/2064068917715193931)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 34

#### Verbatim Text

the best way to break into tech sales is being insanely fast at replying to anything

the best account executives i know all have this in common:

email convos should feel like texting a friend. one reply, then another, then another...

when you're that fast, the buyer feels it too. they reply faster, the deal keeps moving and you keep the momentum

i've seen it firsthand how companies lose deals just by replying too slow...

and it's not easy to do. being that fast means you need both confidence and emotional intelligence

instead of "thanks for asking, let's circle back...", you take the initiative to just figure it out somehow and keep the deal moving

it takes a lot of work, intelligence, and confidence to get this right. 

but all the best salespeople i've hired / interacted with have this in commo

### 35. Wed Jun 03 21:01:16 +0000 2026

- URL: [https://x.com/chrispisarski/status/2062278468264739162](https://x.com/chrispisarski/status/2062278468264739162)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 17

#### Verbatim Text

if you hear "we don't have the budget" in a sales call...

it just means you haven't done enough discovery yet!

every company has "budget"

your job is to find where it's already being spent and figure out how your service fits into that project

we had a company trialing us for their internal recruiting usecase. 

they pivoted, killed the recruiting effort, and suddenly there was no budget for the deal anymore

but a pivot like that usually means they're going twice as hard somewhere else

so we asked!

turns out they were pouring everything into sales and GTM

we just closed them to power that GTM motion with our data through the Crustdata MCP inside Claude

always ask what they're focused on, what the main project is, where the money's going

then make the connection

### 36. Mon Jun 01 20:52:02 +0000 2026

- URL: [https://x.com/chrispisarski/status/2061551368612073473](https://x.com/chrispisarski/status/2061551368612073473)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 0, likes 9

#### Verbatim Text

Some really good advice here

#### Quoted Post

- URL: https://x.com/KyleAsay_/status/2060001254386872322
- Author: Kyle Asay (@KyleAsay_)

Ten SaaS sales realities I’ve learned the hard way:

1) If you only hear good news, you are losing the deal. All deals have risk. Champions share risk. No risk shared means no champion. No champion means you lose.

### 37. Thu May 28 20:10:09 +0000 2026

- URL: [https://x.com/chrispisarski/status/2060091277111116023](https://x.com/chrispisarski/status/2060091277111116023)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 5, reposts 6, likes 237

#### Verbatim Text

this is how we run our daily war room:

1) get everyone in one room. it should be in-person,  "remote war rooms" never hit the same intensity/energy imo

2) for every open deal, find a backchannel

this is the single most useful thing we invested time into. half of the "stuck deal" wins came from a warm intro/backchannel

here's how to set this up at your own company:

1. ask your entire growth and sales team to export their linkedin connections. 

linkedin → settings → data privacy → get a copy of your data → "connections only"

2) everyone gets a csv

3) add all of the files to claude code as context and connect the Crustdata MCP to it

4) ask claude to enrich every single connection through Crustdata, it will pull their full work history, education, current role, recent posts, everything

you now have an internal database of your entire team's extended network, fully enriched and fully searchable through claude

in war room, for any open deal you just ask: "find me the warmest connection to the cfo of [target company]"

claude will then enrich the target account, identify the champion and decision-makers, then cross-reference against your internal database and surface the warmest intro path

the person with the best connection sends the intro request that same afternoon

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2059723409605734778
- Author: Chris Pisarski (@chrispisarski)

one of the best sales advice we got back in YC was the "daily war room":

every day for 15 minutes, the CEO + the entire sales + growth team come together in one room

they go through every open deal and ask one question:
"what was the last touch, and what do we do next?"

there are no stupid questions or status updates, just going through the top deals on that day and answering these 2 questions / figuring out what the next move is

even if you are a solo founder, you should probably have a daily war room

a lot of deals closed because someone in the room said "wait, have you tried looping in their CFO? I know x that can intro us here to push the deal forward"

and you did it that afternoon

### 38. Wed May 27 19:48:23 +0000 2026

- URL: [https://x.com/chrispisarski/status/2059723409605734778](https://x.com/chrispisarski/status/2059723409605734778)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 19, reposts 17, likes 649

#### Verbatim Text

one of the best sales advice we got back in YC was the "daily war room":

every day for 15 minutes, the CEO + the entire sales + growth team come together in one room

they go through every open deal and ask one question:
"what was the last touch, and what do we do next?"

there are no stupid questions or status updates, just going through the top deals on that day and answering these 2 questions / figuring out what the next move is

even if you are a solo founder, you should probably have a daily war room

a lot of deals closed because someone in the room said "wait, have you tried looping in their CFO? I know x that can intro us here to push the deal forward"

and you did it that afternoon

### 39. Tue May 26 17:58:13 +0000 2026

- URL: [https://x.com/chrispisarski/status/2059333298367684684](https://x.com/chrispisarski/status/2059333298367684684)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 0, likes 12

#### Verbatim Text

5 founders are now working on this idea and building a new sales outreach tool

we are powering all of them with free credits until they go live

my bet is that this product, if done really well, will not just go insanely viral

every company will end up trialing it and seeing how it goes

It won't last forever (especially if everyone starts doing it / it becomes too easy)

I think this window of opportunity exists only for the next 4-6 months, until either everyone can generate videos like this or someone has already done it really well and made a brand out of it

We want to power this brand

reach out and I will personally set you up until you go live

there aren't many moments where the only thing limiting you is CODE

if you genuinely build a great product, there's no question people will buy / atleast try it out 

and that's usually not the case

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2058968674430533658
- Author: Chris Pisarski (@chrispisarski)

i can't believe nobody built this product yet, I know at least 40 YC companies that would start using this immediately: 

sending outreach with personalized, high-quality AI sales videos about the company

1) get all of the profile pictures + context (social posts etc.) of a company (can get both using the crustdata API)

2) feed it into an AI model and tell it to create a funny internal storyline

3) send the video automatically

4) video gets shared internally in the company Slack just because it's unique + hilarious, and you get into any account you want 

I'm pretty sure that this tweet/video was shared in the anthropic slack channel

Imagine doing this for any account but with a custom message for your product

why has no one built this yet?

#### Media

- photo: https://pbs.twimg.com/media/HJQ1pEtXIAEvDES.png

### 40. Tue May 26 17:58:55 +0000 2026

- URL: [https://x.com/chrispisarski/status/2059333475983868333](https://x.com/chrispisarski/status/2059333475983868333)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 2

#### Verbatim Text

https://t.co/RVJTuhck7C

### 41. Mon May 25 17:49:20 +0000 2026

- URL: [https://x.com/chrispisarski/status/2058968674430533658](https://x.com/chrispisarski/status/2058968674430533658)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 15, reposts 3, likes 164

#### Verbatim Text

i can't believe nobody built this product yet, I know at least 40 YC companies that would start using this immediately: 

sending outreach with personalized, high-quality AI sales videos about the company

1) get all of the profile pictures + context (social posts etc.) of a company (can get both using the crustdata API)

2) feed it into an AI model and tell it to create a funny internal storyline

3) send the video automatically

4) video gets shared internally in the company Slack just because it's unique + hilarious, and you get into any account you want 

I'm pretty sure that this tweet/video was shared in the anthropic slack channel

Imagine doing this for any account but with a custom message for your product

why has no one built this yet?

#### Quoted Post

- URL: https://x.com/siddsax/status/2058556345566241092
- Author: Siddhartha Saxena (@siddsax)

Anthropic onboarding day: Michael Scott introducing Karpathy like he just signed Wemby in free agency. https://t.co/oAVLfxAZSP

### 42. Mon May 25 17:54:10 +0000 2026

- URL: [https://x.com/chrispisarski/status/2058969891734974880](https://x.com/chrispisarski/status/2058969891734974880)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 4

#### Verbatim Text

this is the future of account-based marketing

we want to power this use case

if you are a sales platform/founder looking to build something like this or similar - will give out free credits just for you to test it and go live

fastest 0 → $1M product idea, if you get this right, you can use your own product to get customers:

https://t.co/qQj8oB2skH

### 43. Fri May 22 17:55:35 +0000 2026

- URL: [https://x.com/chrispisarski/status/2057883082590405117](https://x.com/chrispisarski/status/2057883082590405117)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 1, likes 22

#### Verbatim Text

If I had to start from 0 sales and get to $1M ARR again without YC, this is what I would do:

1. Content
2. Outreach
3. SEO/GEO

you need to nail down all 3 parts, and they're all connected:

1) Content:

It's all about LinkedIn.

1) unless you already have a really good presence on X, it's not worth it, you should spend your time on LinkedIn

2) post daily. If you don't have any network yet, create lists and tag people. We run a daily analysis of the most liked posts across our industry and WHO is liking the posts, and we then reuse many hooks/formats. It's all done within Claude + Crustdata MCP for the post search

3) make sure to max out the weekly connection requests so your prospects see the content. also plug in your notetaker, you can generate content based on that which resonates with your ICP

4) don't spend time experimenting with other platforms (IG/X) if you don't know how they work yet. You don't have time for this. LI works, so make sure it works for you too

2) Outreach

A combination of LI Sales Nav + emails

1) first of all, you need to build a really good list. Use Apollo or Crustdata for that, with Crustdata you can get all of their social posts programmatically via API, so you have more than enough context and more signals

2) don't use AI to write the copy. one good copy can change everything. you need to have a very authentic, non-sloppy way to make someone curious and explain why it's worth it to talk with you

3) make sure to figure out deliverability and email warm-up. There is no excuse not to spend 3–4 hours sitting down, watching videos, experimenting, talking with people, and figuring this out yourself

volume is king here, at the early stage, you want to move fast and break things and talk to as many people as possible and click send, just do it

3) SEO/GEO

you might not need this for the start, but the earlier you figure out how this works, the better

I can go very deep into this, but if you want, just have a look at our site and try to copy what you think is worth it. we work with selected agencies here that help us out, it's worth it

### 44. Thu May 21 20:40:43 +0000 2026

- URL: [https://x.com/chrispisarski/status/2057562251343856121](https://x.com/chrispisarski/status/2057562251343856121)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 18

#### Verbatim Text

i'm still doing founder-led sales with millions in ARR

that means so many other responsibilities, so I find myself trying to disqualify prospects asap

and the faster and harder I DQ, the more the customer starts to pitch why they actually need our product

exclusivity, as in all walks of life, holds true for B2B Sales

you never want to be in a position where your prospects have the feeling that you need to close this deal

### 45. Wed May 20 19:35:03 +0000 2026

- URL: [https://x.com/chrispisarski/status/2057183340273230228](https://x.com/chrispisarski/status/2057183340273230228)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 1, likes 79

#### Verbatim Text

every frontier lab is hiring sales/GTM talent right now

this is the summary of all the roles posted by openai, anthropic and the rest of the frontier labs in the last 7 days 

if you're in tech sales and you're really good at what you are doing, be aware that the demand for really great sales talent is exploding right now

everyone is now building a product - and they all need to sell it

#### Media

- photo: https://pbs.twimg.com/media/HIyUPdTXQAAcQzU.png

### 46. Wed May 20 19:36:09 +0000 2026

- URL: [https://x.com/chrispisarski/status/2057183617789366450](https://x.com/chrispisarski/status/2057183617789366450)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 0, likes 12

#### Verbatim Text

we built a free tool with crustdata that tracks every new role at the frontier labs in real-time:

https://t.co/79zJHixXBO

 refreshed every 30 min

### 47. Tue May 19 19:42:05 +0000 2026

- URL: [https://x.com/chrispisarski/status/2056822722328686878](https://x.com/chrispisarski/status/2056822722328686878)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 14

#### Verbatim Text

every startup should learn about the "Sales Trade Theory" 

a buyer asks for a price match, a top-off, a discount and the sales rep just says "sure, here you go"

every yes you give for free is a yes you'll never get back

so every ask has to be a trade.

nothing leaves your side of the table without something coming back the other way

want a price match? sure. let's move you from monthly to annual

want a top-off this month? happy to. let's lock the rate for 12 months

want a discount on renewal? cool. let me get a logo on the homepage and a 6-month case study commitment

give and get. give and get. give and get.

the difference between a $25M ARR year and a $40M ARR year is whether every single deal got 10% better on the way out because someone fought for it

### 48. Mon May 18 18:34:57 +0000 2026

- URL: [https://x.com/chrispisarski/status/2056443437893792015](https://x.com/chrispisarski/status/2056443437893792015)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 0, likes 26

#### Verbatim Text

we just won a deal because of one of the best pieces of sales advice we picked up during YC:

"Audit the Audit"

a lot of deals at early-stage startups die for the same reason:

your prospect benchmarks you, you lose, they go quiet and you move on

but most of the time the buyer isn't running the test right

they hit the wrong endpoint, pass the wrong params, compare against a stale doc page, score you on a field your product wasn't built for

and they don't know they're doing it wrong, because they're not the expert on your product, YOU are

so when you lose a benchmark, never accept the result

always audit the audit

ask for the actual call they made, which competitors they tested you against, which fields they scored on, what their real use case is

then audit everything

a prospect just benchmarked us against 3 competitors, we "lost"

instead of moving on, we asked to see the curl. one param was off, the response was returning the wrong data

we sent the corrected version and he re-ran the benchmark

we are now at the top of his entire enrichment waterfall and his primary data provider for both person and company

always make sure to audit the audit, because most of the time, they just tested you wrong

#### Media

- photo: https://pbs.twimg.com/media/HIn0E4fXoAARxXc.jpg

### 49. Thu May 14 19:46:30 +0000 2026

- URL: [https://x.com/chrispisarski/status/2055011896122581277](https://x.com/chrispisarski/status/2055011896122581277)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 7, likes 209

#### Verbatim Text

when a prospect asks "how are you different from [biggest competitor]" in a sales call, what do you answer?

one of the best sales leaders we met during YC  told us to say this:

"it depends on what you are optimizing for. if your goal is [competitor's strength], you should honestly go with them. but if your goal is [your unique strength], then we are the better fit. which of those two is a higher priority for your team right now?"

this is called polarity selling, you are forcing the prospect to choose. if they choose yours, they disqualify your competitor

### 50. Wed May 13 19:10:05 +0000 2026

- URL: [https://x.com/chrispisarski/status/2054640343170372045](https://x.com/chrispisarski/status/2054640343170372045)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 2, likes 63

#### Verbatim Text

want to meet someone who would never reply to a cold sales email and you have no warm path?

use the giftcard method:

map out their network + find every person publicly connected to them (the first boss they talk about, college roommate in old interviews, the old mentor they shouted out on a podcast 4 years ago)

those people are 10x easier to reach because nobody is pitching them.

we once needed to meet a founder who was completely unreachable. found a podcast where he named his old mentor. dug up the mentor, who happened to mention his favorite sushi spot in a separate interview. sent him a gift card to that exact restaurant with a 3-sentence note about something specific he'd taught publicly

he replied in 90 minutes. took our call. by minute 20 he said "you should really meet [actual target]" and made the intro himself

cost: $50+ 2 hours of research (which can be replaced and automated with the Crustdata API now)  

outcome: a meeting we'd been chasing for months

### 51. Mon May 11 17:33:44 +0000 2026

- URL: [https://x.com/chrispisarski/status/2053891317038543014](https://x.com/chrispisarski/status/2053891317038543014)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 5, reposts 6, likes 334

#### Verbatim Text

the "email your boss" sales hack for early stage founders

one of our investors shared this with us and it works incredibly well for breaking into massive accounts

instead of emailing the vp of marketing, email the cmo (their boss) with a highly customized insight about their business. end the email with: "i assume you are too busy to look at this, but is there someone on your team i should direct this to?"

the cmo will often forward your email down to the vp of marketing and say: "please look into this"

the VP will take the meeting every time since it's initiated directly by their boss

### 52. Fri May 08 19:34:12 +0000 2026

- URL: [https://x.com/chrispisarski/status/2052834473272573970](https://x.com/chrispisarski/status/2052834473272573970)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 35, reposts 17, likes 495

#### Verbatim Text

stop asking prospects for a "quick 15 minute call"

if your prospect is a c-level or vp, 15 minutes of their time is incredibly expensive. they literally won't give it to you just because you asked nicely

during YC, we stopped asking for time and started asking for permission to send information:

"hey mark, i analyzed how your sales team is doing outbound and noticed you have a huge bottleneck in step 2. i recorded a 2-minute video showing exactly how to fix it. opposed to me sending it over?"

people will happily say "sure, send it". once they watch the video and realize you actually know what you are talking about, they will ask you for a meeting

### 53. Thu May 07 18:20:48 +0000 2026

- URL: [https://x.com/chrispisarski/status/2052453611930562953](https://x.com/chrispisarski/status/2052453611930562953)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 36

#### Verbatim Text

stop building custom features for free just to close a sales deal

if a prospect says "we will absolutely sign if you build this specific dashboard," they are sometimes bluffing

if you spend three weeks building the dashboard, they will ghost you when it's done

we learned to turn feature requests into binding commitments:

"we can absolutely build that dashboard for you. it will take our engineering team two weeks. i'll send over the annual contract today with a clause that says the contract is only legally binding upon delivery of that specific dashboard. does that work?"

if they say no, they were never going to buy anyway. you just saved three weeks of engineering time

### 54. Wed May 06 18:06:18 +0000 2026

- URL: [https://x.com/chrispisarski/status/2052087576090051064](https://x.com/chrispisarski/status/2052087576090051064)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 3, likes 111

#### Verbatim Text

when a prospect stalls, send them an "anti-case study"

Every company sends out case studies showing a happy customer whose revenue went up 500%. prospects are numb to them.

instead, find a time someone made the exact mistake your prospect is about to make

"hey david, knowing you guys are weighing doing this manually vs using our platform, i wanted to send over this post-mortem from a company that tried to scale this manually last year

they ran into a massive data issue in month 4 that broke their CRM. happy to walk you through exactly how to avoid it, even if you don't end up using us"

### 55. Tue May 05 17:52:55 +0000 2026

- URL: [https://x.com/chrispisarski/status/2051721819514655039](https://x.com/chrispisarski/status/2051721819514655039)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 7, reposts 2, likes 108

#### Verbatim Text

the biggest mistake technical founders make in sales is answering "yes" too quickly

prospect: "does your platform integrate with hubspot?"

founder: "yes, we have a native integration!"

this is terrible sales. they asked a technical question and you gave a technical answer. but you learned nothing about why they asked it

try this instead:

"yes, we do. but i am curious - what specific data are you trying to push back and forth from hubspot?"

never answer a technical question without extracting the business pain behind it

### 56. Fri May 01 18:46:14 +0000 2026

- URL: [https://x.com/chrispisarski/status/2050285685270106449](https://x.com/chrispisarski/status/2050285685270106449)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 19, reposts 15, likes 612

#### Verbatim Text

one of the best pieces of advice we got during YC:

be annoying

every sizeable deal has a procurement process. nobody wants to be the person who made the wrong buying decision, so they benchmark 3-5 options

the entire game at early stage is: are you in that shortlist the moment they start looking?

which means one thing: be everywhere

ping everyone. email everyone. tag everyone. be "annoying"

the reason big companies can afford to not do this is because they've already spent millions putting their name in your head. ads, funnels, referral machines, brand. they don't need to fight for the mention

you do

if you're a new company trying to optimize for "brand" before you've earned it, you will get crushed by these companies

get your name out first to become an option

### 57. Sat May 02 00:33:20 +0000 2026

- URL: [https://x.com/chrispisarski/status/2050373034863653240](https://x.com/chrispisarski/status/2050373034863653240)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 24

#### Verbatim Text

- no spam

obviously don’t piss people off, you will be in that industry for a long time (people will remember you and your product)

the goal is to get your name out there. talk to as many people as possible, share your product, be everywhere every day

### 58. Thu Apr 30 19:17:58 +0000 2026

- URL: [https://x.com/chrispisarski/status/2049931282952393021](https://x.com/chrispisarski/status/2049931282952393021)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 0, likes 19

#### Verbatim Text

openAI can increase Codex subscriptions/sales by just adding more FOMO

I don’t understand how OpenAI hasn’t figured this out yet, but the reason why everyone is using Claude is because everyone is POSTING about Claude

every creator knows that if you post anything mentioning Claude, it will get impressions

people don’t want to miss out on something, even if codex is better (which I find the case for some workflows) 

what OpenAI needs is a network of creators/influencers/YouTubers building codex workflows and posting about it everywhere every day

#### Quoted Post

- URL: https://x.com/sama/status/2049493609028923826
- Author: Sam Altman (@sama)

feels like codex is having a chatgpt moment

### 59. Wed Apr 29 19:05:59 +0000 2026

- URL: [https://x.com/chrispisarski/status/2049565877759025523](https://x.com/chrispisarski/status/2049565877759025523)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 0, likes 95

#### Verbatim Text

I really believe anyone can book at least 20–30 sales demos from LinkedIn every single month just by posting

and if you don’t have the time for that, this is what I would do instead:

1) have an AI notetaker every time you go into meetings

2) connect the AI notetaker via API with Claude Code

3) ask Claude to find the most interesting pain points and insights that were brought up in the calls

4) feed it the most viral hooks that were trending this week in your niche (you can use Crustdata for that)

5) ask it to generate posts that directly target your ICP in a very authentic way

6) after you get the drafts, make sure to block 30–50 minutes every week to go through them and pick the best ones or rewrite them, you can generate the entire content for the week in this timeframe

7) Images: try to find an image that works for each post, it can be a lead magnet, a personal insight, anything

8) If you are starting from 0, you should tag people and get them to engage with your post

the key here is 1) consistency and 2) always adjusting based on what’s working

if you have a format that performed well, just double triple down on that

### 60. Tue Apr 28 18:14:21 +0000 2026

- URL: [https://x.com/chrispisarski/status/2049190499236647169](https://x.com/chrispisarski/status/2049190499236647169)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 0, likes 36

#### Verbatim Text

Daniel used Nutella jars to book sales demos

Daniel is one of our first hires at @Crustdata, but before that, he was a former YC founder himself

it was 2015, he was competing with Lyft, Andreessen and Google for the same eyeballs at the Columbia fair

he couldn't afford to spend what these companies were spending

so he bought a bunch of Nutella jars instead and made an event out of his booth: 

snap a pic in front of them and share it, and you get a free Nutella jar at the end of the night

his booth was always crowded, people were laughing, and they were having great conversations with everyone because of it

one of the best hires he ever made came from that event, alongside with countless demos and leads

if you are a startup, you have a responsibility to think creatively

find new ways to get discovered and get your name out there, you can't compete with big companies using the same methods

you need to find your own way that costs 10x less but has the same impact

and if that means using the Nutella jar method, so be it

#### Media

- photo: https://pbs.twimg.com/media/HHAvhfpaYAAvSsY.jpg
- photo: https://pbs.twimg.com/media/HHAviIQbYAAvBhA.jpg

### 61. Mon Apr 27 18:14:49 +0000 2026

- URL: [https://x.com/chrispisarski/status/2048828225527197746](https://x.com/chrispisarski/status/2048828225527197746)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 0, likes 31

#### Verbatim Text

sales advice on how to close more customers we picked up during YC:

the "does this make sense?" method

make a lot of assumptions and ask if they resonate. it's the fastest way to surface the pain your product solves:

"based on what i'm hearing, most teams at your stage are dealing with X and Y - and the impact is usually Z. does any of that sound familiar or am i completely off?"

"i'm going to guess your biggest problem right now is actually Y - right?"

"most people i talk to in your role have already tried X, it didn't work, and now they need Y - is that where you're at?"

if you're right, they feel understood

if you're wrong, they correct you and hand you the real answer

### 62. Fri Apr 24 16:57:05 +0000 2026

- URL: [https://x.com/chrispisarski/status/2047721499784540623](https://x.com/chrispisarski/status/2047721499784540623)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 1, likes 27

#### Verbatim Text

this how you can help your champion sell your product internally:

we were on a call with a prospect who loved the Crustdata API, used it every day during the trial

but when it came time to sign, he said "i need to figure out how to get this approved"

so we asked: "which tool in your stack are you using the least right now?"

he thought about it for a second and named one

we said: "most of our customers redirect that budget to us in month one. net zero impact on your spend"

your buyer already knows they want to buy. what they don't have is the story to tell their boss

so give them one:

1) ask what tool they'd cut
2) frame it as a swap vs an addition
3) now the convo with their boss is "i'm replacing X" instead of "i need new budget"

### 63. Thu Apr 23 18:47:42 +0000 2026

- URL: [https://x.com/chrispisarski/status/2047386950592512351](https://x.com/chrispisarski/status/2047386950592512351)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 0, likes 20

#### Verbatim Text

how to optimize your website to get more sales demos using Claude:

there's nothing worse than landing on a website and then seeing “you need to talk to sales"

a friend of mine who is a CIO at a public company said this on a call about every B2B product he evaluates:

the person evaluating your product has already decided how much friction they'll tolerate BEFORE they ever talk to you

and the bar is getting lower every quarter

if you're losing deals and can't figure out why, run what we call the "CIO test":

1. go to your own website as if you've never seen it
2. try to get value - any value - without talking to a human
3. time how long it takes before you hit a "book a demo" wall

And ask claude to do exactly the same using the chrome extension (just copy paste this tweet)

if you can't get ANY value in under 5 minutes without talking to sales, you're losing the buyers
who would've been your best customers

the best buyers hate talking to sales. make sure they don't have to

a good example of that is the @Crustdata website

### 64. Wed Apr 22 18:19:15 +0000 2026

- URL: [https://x.com/chrispisarski/status/2047017402903265730](https://x.com/chrispisarski/status/2047017402903265730)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 5, likes 112

#### Verbatim Text

one of the biggest deal-killers we've seen selling a usage-based product is the "shadow spreadsheet"

your prospect is sold on the product. but before they can buy, they need to justify the cost internally

so they build a financial model in google sheets. they estimate usage, guess at pricing tiers, and calculate annual cost

the problem is they always get at least one assumption wrong. and that one wrong assumption can double the projected cost overnight

you will never see this spreadsheet. you will never get to correct it. the deal just dies and you don't know why

the fix is what we call the "pre-built business case":

1) after every demo, send them YOUR version of the cost model, pre-populated with realistic assumptions based on discovery (this is why it’s so important to get discovery right)

2) include a tab that shows cost-per-outcome and not just cost-per-credit

3) add a comparison tab vs. their current solution or vs doing it manually

if someone else is building the spreadsheet that decides your deal, you've lost control of it

### 65. Tue Apr 21 17:32:10 +0000 2026

- URL: [https://x.com/chrispisarski/status/2046643168804774200](https://x.com/chrispisarski/status/2046643168804774200)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 8, reposts 9, likes 232

#### Verbatim Text

one of the best pieces of sales advice we got during YC is what we call the "one workflow pitch"

most AI startups walk into sales meetings and say "we're here to solve all your problems"

then they ask: "so... what are your problems?"

was speaking with a customer last week who is getting pitched a lot by AI startups, and this is what he told me about how this lands on the buyer side:

"i'm not giving you all my use cases so that you know what to build and then i'm going to pay you for it"

you're asking them to be your free design partner, which is a red flag if you don’t have a good relationship with them already

how to fix this:

1) before the call, pick ONE workflow you know you can solve (not four, not "whatever you need")

2) open with: "we've been working with teams like yours on [specific workflow]. here's exactly what we do and what we don't do"

3) let THEM expand the scope,  never start wide and ask them to narrow it

the more open-ended your pitch is, the more it sounds like you don't have a product yet

buyers want to hear "we solve this one thing really well" and not "tell us your problems and we'll figure it out"

### 66. Mon Apr 20 17:31:29 +0000 2026

- URL: [https://x.com/chrispisarski/status/2046280605831397689](https://x.com/chrispisarski/status/2046280605831397689)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 13, reposts 8, likes 244

#### Verbatim Text

one of our investors during YC shared this sales advice on how startups can sell to and close big enterprise companies:

it’s the same method we used at @Crustdata to close a 6-figure deal:

help your champion run an internal hackathon

1) we used to say this: "what if we ran a half-day workshop with your team where they build agents? we would love to sponsor it with our data"

2) let THEM discover the use cases

3) the agents they build become your business case

your champion, just like everyone else, wants to have internal wins to show their boss

imagine running a hackathon with marketers, sales ops, finance people…

and after the hackathon, everyone has built agents using the Crustdata API that help them with their day-to-day work

our champion estimated that the agents built during that hackathon would save them at least 6 figures in vendor costs.

you can now use this number and the success of the hackathon as a case to progress the deal you are working on

### 67. Mon Apr 20 20:18:10 +0000 2026

- URL: [https://x.com/chrispisarski/status/2046322553036406864](https://x.com/chrispisarski/status/2046322553036406864)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 3

#### Verbatim Text

@crustdata if you are looking for real-time people and company data via API, bulk datasets, or webhooks AND want to search and fetch the entire web, you should check out Crustdata!

https://t.co/puirn7uCj6

### 68. Fri Apr 17 18:01:31 +0000 2026

- URL: [https://x.com/chrispisarski/status/2045201003965034876](https://x.com/chrispisarski/status/2045201003965034876)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 2, likes 23

#### Verbatim Text

there’s a well-known piece of sales advice we picked up during YC called “default to action"

especially at the early stage, closing a deal is better than getting it perfect

and not every AE is optimized to do that

I spoke with @jerseejess a while ago about what your first AE hire should look like:

#### Quoted Post

- URL: https://x.com/Saul_Lieberman/status/2009346638855459114
- Author: Saul Lieberman (@Saul_Lieberman)

@chrispisarski Say a bit more about how the new AE  brought a level up in your tenacity to close quickly.

#### Media

- video: https://pbs.twimg.com/amplify_video_thumb/2045197765399977984/img/FNKUDIh1Qxhd7H5a.jpg
- video: https://video.twimg.com/amplify_video/2045197765399977984/vid/avc1/1280x720/jRInqbl-VRMv_KMu.mp4?tag=21

### 69. Thu Apr 16 18:24:19 +0000 2026

- URL: [https://x.com/chrispisarski/status/2044844352090873907](https://x.com/chrispisarski/status/2044844352090873907)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 10, reposts 5, likes 53

#### Verbatim Text

Anthropic is now hiring more Sales people than AI researchers and engineers combined

They just can't sell Claude fast enough

Very interesting shift from the old Anthropic playbook around AGI/Safety

Now they seem to be going full go-to-market and getting into every vertical & launching consumer products

#### Media

- photo: https://pbs.twimg.com/media/HGC-9_mWEAAF5qa.jpg

### 70. Wed Apr 15 19:31:21 +0000 2026

- URL: [https://x.com/chrispisarski/status/2044498832801566871](https://x.com/chrispisarski/status/2044498832801566871)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 18, reposts 31, likes 404

#### Verbatim Text

you can automate the entire McKinsey model with Claude

every sales team can now build their own GTM engine that:

1) researches every account before the call, scores them, and generates a custom report that gets better with every call

2) surfaces conversation starting points, what to mention, what to avoid, and what the company is actively trying to achieve right now based on the data signals

3) creates the perfect follow-up doc after the call 

4) auto-enriches every person and stakeholder mentioned during the call so your one-pager is already personalized

5) maps the full buying process so you know exactly who else needs to be addressed and what matters to them

All you need is Claude + the Crustdata MCP + an AI notetaker API

everytime someone books a Crustdata demo, our AEs get this report:

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2044129874244448655
- Author: Chris Pisarski (@chrispisarski)

one of the best sales advice we picked up during YC is the "McKinsey Model"

a lot of deals at early-stage startups die for the same reason:

your champion is afraid to advocate for your product

if they push for it internally and it doesn't work out, their job is on the line

so they never come back to you and hit you with the "we need to align internally first"

that's why you need to be their McKinsey consultant: instead of them pitching, you personally take the blame

after every demo, send them:
- a one-pager
- a security doc 
- an ROI calculator with their numbers
- useful context/overview of your industry that can help with what they're struggling with right now
- a pre-written slack message they can forward

make it as easy as possible for your champion to forward your material without them feeling responsible for integrating your solution or "fighting" for it

#### Media

- photo: https://pbs.twimg.com/media/HF-EZGVbEAET3hR.png

### 71. Thu Apr 16 13:59:54 +0000 2026

- URL: [https://x.com/chrispisarski/status/2044777807985655832](https://x.com/chrispisarski/status/2044777807985655832)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 1, likes 4

#### Verbatim Text

https://t.co/WUv5OV1PMQ

### 72. Tue Apr 14 19:05:14 +0000 2026

- URL: [https://x.com/chrispisarski/status/2044129874244448655](https://x.com/chrispisarski/status/2044129874244448655)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 50, reposts 105, likes 2344

#### Verbatim Text

one of the best sales advice we picked up during YC is the "McKinsey Model"

a lot of deals at early-stage startups die for the same reason:

your champion is afraid to advocate for your product

if they push for it internally and it doesn't work out, their job is on the line

so they never come back to you and hit you with the "we need to align internally first"

that's why you need to be their McKinsey consultant: instead of them pitching, you personally take the blame

after every demo, send them:
- a one-pager
- a security doc 
- an ROI calculator with their numbers
- useful context/overview of your industry that can help with what they're struggling with right now
- a pre-written slack message they can forward

make it as easy as possible for your champion to forward your material without them feeling responsible for integrating your solution or "fighting" for it

### 73. Mon Apr 13 19:11:12 +0000 2026

- URL: [https://x.com/chrispisarski/status/2043768987188621404](https://x.com/chrispisarski/status/2043768987188621404)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 4, likes 89

#### Verbatim Text

how to get a warm intro to any sales account you want using Claude:

everyone is connected to everyone. most of the time, it is just a matter of not knowing who knows who

this is how our sales team solved this problem to book more demos:

1) go to your LinkedIn => Settings => Export your connections (CSV)

2) ask 2 to 3 colleagues to do the same

3) connect Claude with the Crustdata MCP to enrich every contact: titles, companies, seniority, buying signals, emails, phone numbers, etc.

4) ask one question: "Give me ONE path to break into [Account Name]"

that's it

Claude will use the data to map your entire team's network and surface the exact warm intro path you did not know you had

### 74. Fri Apr 10 18:00:53 +0000 2026

- URL: [https://x.com/chrispisarski/status/2042664127957504393](https://x.com/chrispisarski/status/2042664127957504393)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 23, reposts 2, likes 223

#### Verbatim Text

we just renegotiated our Slack Enterprise upgrade with Salesforce

instantly understood how Salesforce is valued at $150B after that call

their AE used the exact same tactics every enterprise sales org uses:

1) "our quarter ends Friday, so I can get you a bigger discount if you sign by then"  and kept pushing: "if I send over the proposal today, would you be able to sign by Friday?"

2) gave us two pricing options where the bulk purchase was designed to look like the obvious choice

3) used our own growth number against us, "you're adding X users/month, so you'll need these seats anyway. why not lock in a better price now?"

### 75. Fri Apr 10 20:58:50 +0000 2026

- URL: [https://x.com/chrispisarski/status/2042708911132696772](https://x.com/chrispisarski/status/2042708911132696772)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 14

#### Verbatim Text

obviously will sign, happy slack customer

### 76. Thu Apr 09 19:09:35 +0000 2026

- URL: [https://x.com/chrispisarski/status/2042319028186988880](https://x.com/chrispisarski/status/2042319028186988880)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 13, reposts 13, likes 388

#### Verbatim Text

our entire sales team is now claude pilled, they all use a claude skill we made called “pre-call research”

everyone of them connected their Claude to Google Calendar, the Crustdata MCP and Slack

before every call it automatically:

- looks at who's attending
- pulls the company's page + domain data
- checks the inbound booking context
- fetches enriched real-time profiles of each attendee via Crustdata
- creates a full brief: company snapshot, talking points, prospect assessment

you can also schedule it:

"every morning at 8am, run pre-call research on all my calls for the day and DM me the briefs"

its pretty insane that this workflow alone could have been the main feature of a sales saas not even 1 year ago and now its just something anyone can run on claude

### 77. Wed Apr 08 18:44:37 +0000 2026

- URL: [https://x.com/chrispisarski/status/2041950356306051346](https://x.com/chrispisarski/status/2041950356306051346)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 8, reposts 4, likes 309

#### Verbatim Text

something I noticed during YC that both the top sellers (and the top job applicants) are doing:

the "oops, forgot to mention" follow-up

it’s a very simple way to break through the noise

1) they send an email with the main info

2) if they don’t get a response, they send a second one with a "forgot to add this" subject line

very underrated way to get your open rate higher if you struggle with this metric. works every time someone does it on me

### 78. Tue Apr 07 20:02:25 +0000 2026

- URL: [https://x.com/chrispisarski/status/2041607550425051235](https://x.com/chrispisarski/status/2041607550425051235)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 2, likes 62

#### Verbatim Text

if there is one thing we learned during YC about taking sales calls, it’s this:

proactively mention a "downside" of your product early

compare it to other solutions on the market and make it clear where you stand:

'i’m sure you are aware that there are a lot of data providers in this space. I wanted to give you some insight into where we stand, which has been a key driver of our growth over the last few months

we are primarily used for [X] by [Target Group A], whereas others focus more on [Y] for [Target Group B]"

providing industry insights and numbers that your lead can then take and share internally has been incredibly huge for demo-to-customer conversions

### 79. Thu Apr 02 18:15:47 +0000 2026

- URL: [https://x.com/chrispisarski/status/2039768775525036181](https://x.com/chrispisarski/status/2039768775525036181)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 26

#### Verbatim Text

this is how I handle the typical "we need to think about it" in a sales call:

=> "of course, totally understood. mind if I ask what specifically would make this a clear yes for you?"

they'll usually do one of two things:

1) they give you a real blocker
"we need sign-off from our CFO"
"not sure about the implementation effort"
"still evaluating two other vendors"

you then work through the blockers one by one:
"what would it take to get your CFO on the next call?"

2) they stay vague
"we just need some time to discuss internally"

you answer with "totally understand. let's do this:
I'll send you a one-pager you can share internally, and let's block 20 minutes next week so I can answer any questions that come up. how does that sound?"

the goal is always to convert #2 into #1

you need to be part of their evaluation process

### 80. Tue Mar 31 18:43:19 +0000 2026

- URL: [https://x.com/chrispisarski/status/2039050926384648623](https://x.com/chrispisarski/status/2039050926384648623)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 1, likes 14

#### Verbatim Text

fun fact: SpaceX has over 294 salespeople

"AI is going to replace Sales" is so funny to me

because it's the last job AI will ever replace

every company, even a rocket company, needs salespeople

here are some of the roles they hired:

- Sr. Manager, Commercial Launch Sales
- Sr. Government Satellite Sales Manager
- Starlink Sales Manager - State, Local & Education
- Consumer Sales Manager, Europe
- Senior Manager, Global Starlink Enterprise Sales Ops

#### Media

- photo: https://pbs.twimg.com/media/HEwp9V0bkAAnvSF.png

### 81. Fri Mar 27 20:46:10 +0000 2026

- URL: [https://x.com/chrispisarski/status/2037632293502943627](https://x.com/chrispisarski/status/2037632293502943627)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 5, reposts 1, likes 17

#### Verbatim Text

one of my biggest sales enterprise deals involved over 40 different stakeholders

we started building stakeholder maps for every major deal

the goal was to visualize every relationship

after every call, we would update the map with "the script" to identify blind spots:

"typically, for a project like this, we see [Role A] and [Role B] getting involved to evaluate the technical fit. who is that person on your team, and what is the best way to keep them in the loop early?"

this maps out the 5 key players you need to identify:

- the champion: who is selling this internally for you?
- the economic buyer: who signs the check?
- the technical buyer: who is vetting your stack?
- the user: who is actually using the tool every day?
- the enemy: who loses power or budget if you win?

that was a long time ago, now you can automate this entire process with AI

#### Media

- photo: https://pbs.twimg.com/media/HEcfgaeWcAAmiKz.jpg

### 82. Thu Mar 26 18:49:40 +0000 2026

- URL: [https://x.com/chrispisarski/status/2037240584428282302](https://x.com/chrispisarski/status/2037240584428282302)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 18

#### Verbatim Text

one of the most simple, but effective questions to ask in a sales call:

“would our x (feature) remove the customer complaints you mentioned earlier?”

always make sure to remind your prospects about the problems they face, and how you can solve them

pretty surprising how many of them will forget what triggered the conversation in the first place and how effective this is

### 83. Wed Mar 25 19:22:49 +0000 2026

- URL: [https://x.com/chrispisarski/status/2036886539934847058](https://x.com/chrispisarski/status/2036886539934847058)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 13, reposts 6, likes 151

#### Verbatim Text

this is exactly why we decided to adopt a "Palantir" model for sales

seeing more and more YC companies doing the same:

there is a massive shift right now toward wanting to build products in-house

but despite all the hype around replacing SaaS, there are still some blockers companies have:

they:
1) don't know where to start or what "it" should look like
2) don't know how they should go about building
3) lack the resources to build / maintain it

taking all that into account, we've decided to adopt a Palantir model for sales and will be testing: what if we still sell our data/APIs, but also take care of the building end-to-end?

the results so far of some of the products that came out of it:

- fully automated TAM building and email sequence platform for a Big 4 company

- automated "warmest path" for intros to founders for a private equity fund

and others that are basically a manifestation of the question: "what's your dream state for X?"
(X being sales, marketing, investing, etc.)

It's a lot to promise, but we're excited about the early potential. if you are interested in building your dream state for sales, recruiting, or investing - drop a note and we'll reach out!

#### Quoted Post

- URL: https://x.com/rauchg/status/2036447879985037495
- Author: Guillermo Rauch (@rauchg)

Almost every SaaS app inside Vercel has now been replaced with a generated app or agent interface, deployed on Vercel.

Support, sales, marketing, PM, HR, dataviz, even design and video workflows. It’s shocking.

The SaaSpocalypse is both understated and overstated. Over because the key systems of record and storage are still there (Salesforce, Snowflake, etc.)

Understated because the software we are generating is more beautiful, personalized, and crucially, fits our business problems better. 

We struggled for years to represent the health of a Vercel customer properly inside Salesforce. Too much data (trillions of consumption data points), the ontology of Vercel was a mismatch to the built-in assumptions, and the resulting UI was bizarre. We generated what we needed instead. When you don’t need a UI, you just ask an agent with natural language.

We’ve also been moving off legacy systems with poor, slow, outdated, and inconsistent APIs, as well as just dropping abstraction down to more traditional databases. UI is a function 𝑓 of data (always has been), and that 𝑓 is increasingly becoming the LLM.

### 84. Tue Mar 24 19:02:27 +0000 2026

- URL: [https://x.com/chrispisarski/status/2036519029255340526](https://x.com/chrispisarski/status/2036519029255340526)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 5, likes 41

#### Verbatim Text

I can’t remember how many sales deals we saved during YC just by summarizing the blockers

“just to summarize, it sounds like problem x and problem y are currently the blockers. is that fair to say?”

and if they agree, you work on both

many prospects don’t have a clear overall picture, so your goal is always to summarize the conversation for them and give direction on where the call should go next

### 85. Mon Mar 23 19:24:48 +0000 2026

- URL: [https://x.com/chrispisarski/status/2036162262256296278](https://x.com/chrispisarski/status/2036162262256296278)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 9, reposts 3, likes 166

#### Verbatim Text

one of the best pieces of sales advice I got during YC is the "decision-making" framework

If a prospect tells you:

“i’m thinking of switching to you, but we have to evaluate if the engineering cost is worth it”

you should avoid arguing why it is worth it and instead ask about their decision process:

“sounds great, if you don’t mind me asking, can you help me understand what that process usually looks like?”

they will explain the steps, and your goal should be to address every part of that decision-making process

### 86. Fri Mar 20 17:54:48 +0000 2026

- URL: [https://x.com/chrispisarski/status/2035052450097316239](https://x.com/chrispisarski/status/2035052450097316239)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 8, likes 0

#### Verbatim Text

RT @TechSalesGuy: Don't even ask the question.

Yes, you should follow-up. 

Think you sent that email and they'll get back to you? Maybe,…

### 87. Thu Mar 19 18:34:41 +0000 2026

- URL: [https://x.com/chrispisarski/status/2034700099905786274](https://x.com/chrispisarski/status/2034700099905786274)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 10, reposts 14, likes 268

#### Verbatim Text

anyone can become great in sales if they follow some basic advice:

1) get a general overview of their business
2) ask if anyone else should be on the call
3) ask what they’ve tried in the past and why it didn’t work
4) understand what they’re currently doing
5) clarify what their desired outcome is
6) ask: 6 / 12 months down the line, what would the ideal outcome look like?
7) keep digging deeper: if they say “we used tool X and it wasn’t great,” your goal is to understand why it wasn’t great (missing features, bad data, no onboarding, etc.)

make the prospect feel understood
if you do this right, you transition into the demo:

8) pick the biggest pain point they have
9) focus your entire demo on that pain point
10) tie everything back to their goals:

“in order to get you to that X goal we talked about, we would…”
“in order to get you to that Z goal we talked about, we would…”

11) after the demo, ask how they feel about it:
 “with everything we discussed, how do you feel about X?”

### 88. Wed Mar 18 17:46:21 +0000 2026

- URL: [https://x.com/chrispisarski/status/2034325547917115475](https://x.com/chrispisarski/status/2034325547917115475)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 0, likes 17

#### Verbatim Text

ChatGPT went from 43% of our AI-sourced qualified leads in September to 3% in March. Claude went from 4% to 43%. Nearly all of that change happened in the last 8 weeks (!!)

Even though @crustdata gets 2.5× more sales demos per month from AI than 6 months ago, the share coming from ChatGPT has collapsed

Probably one of the biggest shifts so far: buyers with intent are now using Claude for discovery more than ChatGPT

#### Media

- photo: https://pbs.twimg.com/media/HDtP0j0XMAwC66J.jpg

### 89. Tue Mar 17 18:40:33 +0000 2026

- URL: [https://x.com/chrispisarski/status/2033976802922709490](https://x.com/chrispisarski/status/2033976802922709490)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 25, reposts 25, likes 1263

#### Verbatim Text

7 months ago, someone on Reddit passed on a sales role at Anthropic because Claude was still in the "experimentation phase" and he didn't want to bet on equity

this was when Anthropic was valued at $41B

today they are at $380B https://t.co/ecMIe62kCm

#### Media

- photo: https://pbs.twimg.com/media/HDojHIdXkAABh89.png

### 90. Tue Mar 17 23:54:25 +0000 2026

- URL: [https://x.com/chrispisarski/status/2034055786658468226](https://x.com/chrispisarski/status/2034055786658468226)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 0, reposts 0, likes 12

#### Verbatim Text

speaking of Claude, we just launched our MCP server

connect Claude with real-time data:

"find every Head of Sales at a Series B SaaS company in Europe, hired in the last 2 months, who studied at the same university as me"

"find senior backend engineers in Berlin who worked at X or Y and have Python as a skill on their profile with x public repos"

"find everyone who engaged with my competitor's posts in the last 7 days, enrich them, and filter for HR tech buyers at companies with 50-500 employees"

and get the data in seconds

Giving out free test trials, just mention "Crustdata MCP" in the form and we will share an API key:

https://t.co/E4g8upi7Zc

#### Media

- video: https://pbs.twimg.com/amplify_video_thumb/2034055538963877888/img/facOOrFh-OGF3Oc1.jpg
- video: https://video.twimg.com/amplify_video/2034055538963877888/vid/avc1/1920x1080/KlW3C3rXi-jPRGxQ.mp4?tag=21

### 91. Mon Mar 16 18:59:59 +0000 2026

- URL: [https://x.com/chrispisarski/status/2033619304676216962](https://x.com/chrispisarski/status/2033619304676216962)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 19

#### Verbatim Text

this is why mentioning that a big logo is using your product in a sales call is no longer enough:

most early-stage startups are piloting with big companies for very small deal amounts and list the entire company as a customer

experienced buyers are 1) aware of this 2) expect to learn more about the extent of the partnership

every company should have published case studies that you can reference during a sales call

#### Quoted Post

- URL: https://x.com/owenoktay/status/2024195968816537961
- Author: Owen (@owenoktay)

hack to get top companies on your site as customer logos:

find products you want to use anyway

then convince those companies to pilot your product as a requirement for you to close with them

you'd be shocked at how well this works and how widespread it is

ramp is notorious for doing it

they'll run pilots with hundreds of startups a year simply to get those startups to sign up for ramp

and then those startups get to put ramp as a logo on their site

win win

a great way to build credibility early on before you have many customers

### 92. Thu Mar 12 18:29:44 +0000 2026

- URL: [https://x.com/chrispisarski/status/2032162140396593287](https://x.com/chrispisarski/status/2032162140396593287)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 4, reposts 4, likes 99

#### Verbatim Text

if you’re sending cold emails to get more sales:

gong analyzed millions of cold emails to find the best CTA to end your mail with:

"is this something you're open to exploring?" (interest-based)

this outperformed every other CTA:

specific: "can we chat friday at 2pm?"
open-ended: "do you have time later this week?"

#### Media

- photo: https://pbs.twimg.com/media/HDOwmn5bQAEv75n.jpg

### 93. Wed Mar 11 17:56:22 +0000 2026

- URL: [https://x.com/chrispisarski/status/2031791354162880900](https://x.com/chrispisarski/status/2031791354162880900)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 3, reposts 0, likes 23

#### Verbatim Text

i’ve scaled 2 companies to millions in ARR 10+ years apart, both in the data space. this is what changed over the years:

last time: back then news articles were king, getting cited in the WSJ changed your month

this time: getting into mass media doesn’t matter. Going viral on linkedIn can make your quarter

last time: back then, it was a given that contracts were annual

this time: way more people expect monthly contracts as a default. you have to make the strong case for annual. and, you have to constantly fight to keep the customer, you can’t take them for granted

last time: a good idea with mediocre talent was enough, you could build a moat and sustain it for a while

this time: today, it’s too easy to build products and people will catch up unless you have good people constantly seeking the edge

### 94. Tue Mar 10 17:43:14 +0000 2026

- URL: [https://x.com/chrispisarski/status/2031425661584257357](https://x.com/chrispisarski/status/2031425661584257357)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 6, reposts 0, likes 24

#### Verbatim Text

prediction: every company will push employees to become an “x engineer” in their field

we already saw it with the “gtm engineer” on the sales side

now we’ll get the “recruiting engineer”/ "technical recruiter”, the “content engineer”, and so on

teams will expect more employees to build AI automations/tools around the work they do

### 95. Fri Mar 06 18:23:54 +0000 2026

- URL: [https://x.com/chrispisarski/status/2029986344437477436](https://x.com/chrispisarski/status/2029986344437477436)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 5, likes 178

#### Verbatim Text

great sales questions template I saved a while ago for discovery calls:

1) what about what we do made you interested?

2) why is this a problem? can you walk me through how you're currently doing it today?

3) why now? can you give me an example of how this causes problems?

4) have you tried solving this before? what would success look like for you? what metrics would you want to see?

5) who feels the pain internally? what could you be doing today if this wasn’t an issue?

6) if you didn’t solve it, could you live with it?

### 96. Thu Mar 05 19:24:07 +0000 2026

- URL: [https://x.com/chrispisarski/status/2029639108876980555](https://x.com/chrispisarski/status/2029639108876980555)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 14, reposts 27, likes 690

#### Verbatim Text

learned this during YC - double your growth with minimal effort:

how: when you are going to bat for a potential customer in a sales call (getting them lower pricing, better terms, etc), just say:

"I'm going to take care of you and make sure that you are successful with our product. "

and I have one ask: "I’m going to put a call on your calendar for 30 days from now. If I’ve done my job and the product is making your life easier, I’m going to ask for a recommendation to 2 people that you think would benefit from our product, is that okay?"

most people will say yes because

1) people like helping others and 
2) you are promising to take care of them

each closed deal gets 2 referrals and if anywhere near 50% close rate, you are effectively doubling your growth

### 97. Wed Mar 04 18:43:47 +0000 2026

- URL: [https://x.com/chrispisarski/status/2029266570640244962](https://x.com/chrispisarski/status/2029266570640244962)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 10, reposts 4, likes 174

#### Verbatim Text

never seen something like this before, the demand for building custom GTM/Sales agents is massive

18 months ago, we made the decision to go all in being an API-only company with no other "UI". 

it wasn't obvious back then, but now we are powering the sourcing for YC, tier 1 VCs, and are the data API that powers most of the well-known AI recruiters / sales platforms out there

our biggest growth channel are customers who increase their usage with us because of how much demand they have. We have seen customers go from MVP to $M ARR in just months

the market is big and the only thing that is holding people off is their agency

#### Quoted Post

- URL: https://x.com/chrispisarski/status/2028922432904413463
- Author: Chris Pisarski (@chrispisarski)

Vercel already replaced their 10-person inbound SDR team with 1 GTM Engineer

if you still don't know what GTM Engineering is and how it will change your sales org:

1) install Claude Code

2) get a free Crustdata test API key

3) describe every workflow you're currently doing that isn't directly adding revenue (researching, building lists, enriching...)

4) ask Claude Code how to automate everything you just described using the API + any other tools in your stack

#### Media

- photo: https://pbs.twimg.com/media/HClganuWsAErcN8.jpg

### 98. Tue Mar 03 19:56:18 +0000 2026

- URL: [https://x.com/chrispisarski/status/2028922432904413463](https://x.com/chrispisarski/status/2028922432904413463)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 22, reposts 26, likes 565

#### Verbatim Text

Vercel already replaced their 10-person inbound SDR team with 1 GTM Engineer

if you still don't know what GTM Engineering is and how it will change your sales org:

1) install Claude Code

2) get a free Crustdata test API key

3) describe every workflow you're currently doing that isn't directly adding revenue (researching, building lists, enriching...)

4) ask Claude Code how to automate everything you just described using the API + any other tools in your stack

#### Quoted Post

- URL: https://x.com/irabukht/status/2028610511152230506
- Author: Ira Bodnar (@irabukht)

hiring GTM folks right now feels nearly impossible — harder to find than great engs
you need insane taste, a sense for virality, and be technical
that combo barely exists

### 99. Tue Mar 03 20:07:39 +0000 2026

- URL: [https://x.com/chrispisarski/status/2028925291104514511](https://x.com/chrispisarski/status/2028925291104514511)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 2, reposts 0, likes 9

#### Verbatim Text

@lennysan's podcast with Vercel's COO where they talked about how they did this is a must-hear for everyone in this space - great insights

### 100. Tue Mar 03 19:59:12 +0000 2026

- URL: [https://x.com/chrispisarski/status/2028923162583245281](https://x.com/chrispisarski/status/2028923162583245281)
- Author: Chris Pisarski (@chrispisarski)
- Metrics: replies 1, reposts 0, likes 20

#### Verbatim Text

Get one here:

https://t.co/WUv5OV1PMQ
