---
type: raw_capture
source_type: x
url: https://x.com/TheMattBerman/status/2032579413204746666
original_url: https://x.com/TheMattBerman/status/2032579413204746666
author: "Matthew Berman"
handle: TheMattBerman
status_id: 2032579413204746666
captured_at: 2026-06-19T21:44:00+08:00
published_at: "Fri Mar 13 22:07:50 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 6
  reposts: 13
  likes: 158
---

# X post by @TheMattBerman

## Source

- Original: [https://x.com/TheMattBerman/status/2032579413204746666](https://x.com/TheMattBerman/status/2032579413204746666)
- Canonical: [https://x.com/TheMattBerman/status/2032579413204746666](https://x.com/TheMattBerman/status/2032579413204746666)
- Author: Matthew Berman (@TheMattBerman)

## Verbatim Text

How To Rank on Google With Openclaw

## This is automated SEO running on @openclaw.

[Embedded Tweet: https://x.com/i/status/2029751967527096554]

Two weeks ago one of my agency clients hit page 1 for a keyword we'd been stuck at position 12 on for weeks and weeks. Finally.

2,400 searches a month. Competitive term.

And I didn't write the article that pushed it over. I didn't build the internal links.

An @openclaw agent did all of it. Without being asked.

Here's exactly how it works.

THE WHOLE THING IS OPEN SOURCE GET IT HERE 👇

[https://github.com/TheMattBerman/seo-kit](https://github.com/TheMattBerman/seo-kit)

---

# Part 1: The Problem

---

I've been doing SEO for 15 years. Content, links, rankings, compounding traffic.

How we 'name' things and the some of our tooling might shift, but the general process hasn't changed in two decades.

Find keywords. Create content. Build links. Make sure the site is fast and crawlable. Monitor rankings. Repeat.

What changed is everything around it.

Right before COVID (late 2019/early 2020) we were doing A LOT of work in legal and medical. And as we saw the onslaught of bogus content bombarding the space.

We started interviewing our clients so that the content we were making was based in their lived experience, and that we could stand out from the article spam COVID initiated. Two years later Google announced EEAT (from EAT).

But that was nothing compared to what would happen next.

In 2024, Google's AI Overview started eating generic content alive. Millions of articles that ranked fine for years? Gone. Disappeared behind a blue box at the top of search results. The AI could summarize them, so Google did. No click needed.

The content that survived had one thing in common: it contained something the AI couldn't synthesize. Real experience. Specific numbers from real campaigns. Opinions backed by actual results. Contrarian takes that required judgment.

---

# Part 2: The Stack

---

Six skills. Two data sources. One feedback loop.

@openclaw: The brain. Open-source framework for running AI agents. Not chatbots. Persistent agents that read files, call APIs, run on schedules, and actually do work. Each "skill" is a module with one job. The agent knows how to use them together.

Google Search Console: Your actual ranking data. Not estimates. Not projections. Your real positions, real clicks, real impressions. Free.

@dataforseo : The API behind most SEO tools. Keyword research, search volumes, competitor analysis, SERP data. Direct access costs $50/month instead of the $200+ that Ahrefs or Semrush charges for the same data with a nice UI on top. If you want backlink access from DataforSEO it's $100. There's a web fallback otherwise.

PageSpeed Insights API: Google's own speed testing tool. Core Web Vitals, load times, performance scores. Free.

Total monthly cost: $50 for DataForSEO. Everything else is free. Skip DataForSEO entirely and use web search fallback. Total: $0.

---

# Part 3: SEO Agent (Discovery + Monitoring)

---

This is the intelligence layer. Three scripts that tell you where to focus.

## seo-discover: Find Your Next Target

```
bash
./seo-discover.sh --site sc-domain:example.com --limit 20

```

Pulls your GSC top queries from the last 28 days. Filters for the strike zone: keywords where you're ranking positions 5-20.

Why 5-20? That's where SEO leverage lives.

Position 12 to position 5 is a 4x increase in clicks. One well-targeted supporting article with good internal links can do that. The discover script finds those opportunities and scores them by search volume, competition, and current position.

Then it hits DataForSEO for related keywords you're missing. Clusters them. Prioritizes by opportunity score. Output: a ranked hit list of exactly what to write next.

## seo-monitor: Track What's Moving

```

bash
./seo-compete.sh --site example.com --competitor competitor.com

```

Snapshots your rankings every week. Diffs against the previous snapshot. Flags what's climbing, what's dropping, and what just entered the strike zone.

This is your radar. Without it, you're publishing content and hoping. With it, you know exactly which articles are gaining momentum and which ones need help.

The monitor saves snapshots to workspace/seo-agent/snapshots/.

Week over week, you build a history. Patterns emerge.

You start seeing which types of content climb fastest, which keywords respond to supporting articles, which ones need backlinks to move.

## seo-compete: Take Their Keywords

```
./seo-compete.sh --site example.com --competitor competitor.com

```

Competitor gap analysis. Every keyword they rank for that you don't. Scored by their position and search volume. Easiest wins first.

Feed the output back into discover as seed keywords. The loop tightens.

---

# Part 4: SEO Forge (Content Engine)

---

Most AI content is DOA. It ranks for 60 days, gets gobbled by an AI Overview, and leaves you with nothing.

SEO Forge is different because it starts by learning who you are. SEO Forge works with interviews, and you can extend this by giving your openclaw internal data and references.

## The Interview

First time you run it, the agent asks 8 questions:

From your answers, it builds a voice profile, audience file, and positioning doc. Every article after this carries your DNA.

## The "Only I Can Write This" Test

Every article gets tested: is there a sentence in here that could only come from someone with real experience? If not, the agent flags it. That's the moat.

AI Overview can summarize any generic article. But what itt can't summarize is my story about scaling a spirits brand from one state to 50. It can't replicate the specific numbers from your last campaign. It can't fake the opinion you formed after 20 years grinding, talking to customers, being in the trenches of doing the work.

That's what survives. That's what SEO Forge produces.

## Weekly Refinement

Every 7 days, the agent checks in. 2 minutes:

- What content performed well?

- Any new products or services?

- Questions customers keep asking?

The context compounds. Week 12 is sharper than week 1 because it knows more about you.

## Topical Authority Built In

Every article fits into a hub-and-spoke structure. The agent maps your topic clusters automatically.

Hub pages target broad, high-volume keywords. Spoke pages target specific long-tail variations and link back to the hub. The hub links to every spoke. Spokes link to related spokes. The whole cluster reinforces itself.

When you publish a new spoke, the agent automatically identifies where to add internal links from existing content. The cluster grows tighter with every article.

## Anti-AI-Overview by Design

At every major section, the agent checks: could Google's AI Overview answer this from public sources? If yes, it goes deeper or goes personal. Sections that AIO could fully answer get flagged for revision.

Three psychology frameworks are baked in:

Puppet Strings — every article targets one human drive (wealth, status, escape, health, romance). The hook, framing, examples, and CTA all serve that drive.

Scroll Traps — the first 300 words use pattern interrupts, term branding, specificity, and tribal signaling to keep people reading.

Care To Click — every article follows an emotional arc: make them care, make them believe, make them see, make them want, make them stay, make them click.

The content reads like a person wrote it. Because a person informed it.

## SEO Images: Visuals That Work Work Work Work Work

Articles with custom images rank better and convert more. The seo-images skill handles it automatically.

Six generation styles. Twenty-one presets. Vertical routing. It picks the right format for the content type: blog hero, infographic, comparison chart, process diagram, social share image. Give it the article brief and the voice profile, it generates images matched to the content.

The images are built around the target keyword and topic cluster so they pull image search traffic alongside the article. Everything the agent produces ties back to your rank.

## The Actual Workflow

Here's what happens when I tell the agent to write an article for "ai marketing automation":

1. Pulls top 10 SERP results from @DataForSEO. Analyzes titles, word counts, angles, gaps.

2. Captures every People Also Ask question (these become mandatory sections).

3. Checks for AI Overview presence. Notes what it covers so we can go beyond it.

4. Builds a content brief: target keyword, secondary keywords, intent, angle, word count, experience anchors needed.

5. Drafts the article with the your (or clients) voice profile loaded. Short paragraphs. Specific numbers. Real opinions.

6. Runs the humanize pass: kills AI-isms, removes hedge words, injects contractions and rhythm variation.

7. Generates matching images via seo-images  (hero, supporting visuals, social share).

8. Generates JSON-LD schema markup: Article + FAQ at minimum.

9. Saves to disk with full frontmatter.

It takes about 15 minutes to draft the article with images.

We usually do a human polish pass and review. Then publish.

---

# Part 5: SEO Links (Backlink Engine)

---

Content without backlinks doesn't rank. Everybody knows this. But most founders don't do anything about it because link building is tedious.

Five scripts that find link opportunities. You handle the outreach (or just go add instantly.ai and make a backlink outbound skill around that, that's what I do).

## link-mine: Competitor Backlinks

```
bash
./link-mine.sh --domain competitor.com --limit 50

```

Every site linking to your competitor is a potential link for you. Resource pages, roundups, directories, guest posts. Prioritized by domain authority.

## link-mentions: Unlinked Brand Mentions

Finds pages that mention your brand but don't link to you. These convert at 15-25%. They already know who you are. A quick email is all it takes.

## link-broken: Dead Link Opportunities

Crawls resource pages in your niche. Finds 404s. You email the site owner: "This link on your page is broken. Here's my content that covers the same topic."

You're doing them a favor!

## link-internal: Your Own Site Audit

Finds orphan pages with no internal links. Suggests cross-links between related content. Run this every time you publish.

## link-prospect: Resource Page Discovery

Finds "best tools," "top resources," and "ultimate guide" pages where you should be listed but aren't.

---

# Part 6: SEO Health (Technical Monitoring)

---

A page with perfect content and strong backlinks will still rank poorly if it takes 6 seconds to load.

Three scripts:

health-speed — hits Google's PageSpeed Insights API and checks Core Web Vitals. LCP, INP, CLS, FCP, TTFB. Tracks scores over time. "Your LCP got 400ms worse this week." You'd want to know that before your rankings drop.

health-crawl — audits your site for broken internal links, redirect chains, missing meta tags, duplicate titles, mixed content.

health-images — checks every image on your top pages. Missing alt text, oversized files, wrong formats, missing dimensions. Tells you what to fix.

Run all three every Monday morning. 5 minutes.

---

# Part 7: A Real Week

---

Here's what actually happens when the system runs.

Monday morning. The agent runs discovery, monitoring, and health checks automatically. My Telegram at 7am:

Tuesday. I tell the agent to write the supporting article for topical authority. It pulls the keyword data, checks what's ranking, identifies the gaps, and drafts a 2,500-word article using the voice profile from my client's interview. seo-images generates a blog hero and two supporting visuals matched to the content. Draft and images in my inbox by lunch. I (honestly my team) spend 15 minutes reviewing. One edit: add a specific client result to section 3. Publish.

Wednesday. Internal link audit runs. 8 cross-links added between the new article and existing content. The agent also finds 4 sites mentioning the brand without linking. Outreach emails drafted.

Thursday. Competitor backlink mining. 15 targets found. 3 broken link opportunities on resource pages. I have another agent (not in this repo) sending mass emails via instantly. My team sends 8 manual outreach emails to bigger targets. Takes 20 minutes.

Friday. Competitor gap analysis. 8 keywords they rank for that we don't. These feed into next Monday's discovery as seeds. The loop closes.

---

# Part 8: The Loop

---

Each skill is useful alone. Together they compound.

No in-house team does this manually. Most agencies don't either. Not consistently. Not across content, links, and technical health simultaneously. But this agent never gets distracted. It runs every week whether you're on vacation or buried in work.

Week 4 is smarter than week 1 because it has monitoring data from weeks 1-3. Week 12 is running a machine that learns what works for your specific site.

The topical authority effect kicks in around week 6-8. Google starts treating your site as an authority on the topic cluster. New articles in the same cluster index faster and rank higher on entry. The agent measures this. It tracks how long new articles take to enter the strike zone compared to earlier ones. That number drops over time. That's the compounding.

---

# Part 9: The Cost

---

That's not a typo. And the output is better because the agent is more consistent than any human at the repetitive work. It never forgets to check site health. It never skips the internal link audit because it's Friday at 4pm. It runs every week whether you're on vacation or buried in client work.

But the real value here is you're freeing up your human time to focus on the things that matter more. That's creating better multimedia content, video, creating brand and personality, creating relationships with your clients or customers, and overseeing the general SEO agentic orchestration.

Manage the agent. Manage the agentic teams. Check the evals. Improve the system. You focus on that 100x more than you do on the pixel pushing and repetitive execution.

Skip DataForSEO entirely and use the web search fallback. Less data, still works. Total: $0. But I'd go for the $50-$100 for the real deal data (if finances permit).

P.S. I'm not counting LLM costs or electricity or any of that. I'm considering that core infra.

---

# Part 10: Lessons Learned

---

I'm going to be honest about what I got wrong.

V1 of this flow over-indexed on content and under-indexed on links. The first version had the discovery and content skills but no link building. I tested by publishing 12 articles in three weeks (v1 was on claude code btw). Great content. None of it ranked because the testing domain had weak backlink authority. Added SEO Links in week four. Rankings started moving in week six. Content without links is a hail mary for most.

The interview is the whole game. I almost shipped SEO Forge without the brand interview. I figured people would skip it anyway. Tested it both ways. And honestly my crew and I do the interviews here. It's better. So do it. Articles written with interview context ranked 3x faster than generic ones. Google's AI Overview couldn't touch them. The interview takes 15 minutes and it's the single highest-leverage thing in the entire system. If you steal anything steal the concept that AI needs your personal experience/data.

Weekly monitoring changes your behavior. Before the agent, I'd check rankings every week or two (for my own project sites). Maybe once a month for side projects. By then it's too late to act on trends. Weekly snapshots let you catch a climber at position 12 and push it to position 5 with a supporting article. That window is 2-3 weeks. Miss it and the competitor who published similar content takes the spot.

The strike zone concept saved me from wasting time. It's tempting to target whatever keywords have the highest volume. Position 87 for a 50,000 volume keyword can feel exciting. It's not. It's a year or two of work. Position 14 for a 1,800 volume keyword is one article away from real traffic if you have some authority or backlink juice. The agent's strike zone filter forces you to focus on what's actually movable.

Site health is boring until it costs you. Most brands skip the health checks at first. We had a client come onboard whose LCP jumped from 1.8s to 4.2s because someone had uploaded uncompressed images. Rankings dropped for 3 weeks before they noticed and hit us up. The health skill would have caught it ASAP. Now it runs every week without exception.

DataForSEO is the best-kept secret in SEO. People deep in the SEO game know it. But most people don't. DataForSEO gives you direct API access for a fraction of the cost. $50/month gets you more data than a $200/month Semrush subscription. AND THAT DOESN'T GET YOU THE API! The catch is there's no pretty dashboard. The agent is the dashboard.

The hub-and-spoke model is not optional. The moment you switch to clusters with a hub page and supporting spokes, rankings accelerate across the whole group. One strong spoke lifts the hub. A strong hub lifts all spokes. The agent maps these clusters automatically now.

---

# Part 11: Get the Kit

---

Everything is open source. Everything is free.

Six skills. The full loop from discovery to content to images to links to monitoring and back again.

[https://github.com/TheMattBerman/seo-kit](https://github.com/TheMattBerman/seo-kit)

What's in the repo:

- seo-agent/ — discover, monitor, compete. Keyword intelligence from GSC + DataForSEO.

- seo-forge/ — brand interview, content engine, weekly refinement, anti-AI-Overview checks, psychology frameworks.

- seo-links/ — competitor backlink mining, unlinked mentions, broken link finder, internal link audit, resource page prospecting.

- seo-health/ — PageSpeed audits, crawl health, image optimization.

- seo-checklist/ — meta tags, schema markup, llms.txt, topical authority reference.

- seo-images/ — AI image generation for SEO content. 6 styles, 21 presets, vertical routing. Blog heroes, infographics, comparison charts, social share images — matched to your content brief and voice profile.

- SOUL.md, AGENTS.md, setup guide, everything configured.

Clone it. Run seo-check.sh to verify your connections. Let the agent interview you. Run your first discovery. Check your site health.

Set it on a weekly schedule and forget about it. Check back in a month.

The agent does your SEO. You just review what it finds.

Stop paying $5,500/month. Start compounding.

## X Article Metadata

- Title: How To Rank on Google With Openclaw
- Preview: This is automated SEO running on @openclaw.
 
Two weeks ago one of my agency clients hit page 1 for a keyword we'd been stuck at position 12 on for weeks and weeks. Finally.
2,400 searches a month.

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
