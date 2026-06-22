---
type: raw_capture
source_type: x
title: "Sunder sync: i-automated-all-our-content-creation-using-openclaw-reddit-semrush-aws-g-twitter-shnai0-2021163270040846400-FULL.md"
url: "https://x.com/shnai0/status/2021163270040846400?s=46"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/i-automated-all-our-content-creation-using-openclaw-reddit-semrush-aws-g-twitter-shnai0-2021163270040846400-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/i-automated-all-our-content-creation-using-openclaw-reddit-semrush-aws-g-twitter-shnai0-2021163270040846400-FULL.md"
sha256: "a63ba5ce43f3e0699a956d646e38928bd4918df905a9ee82469a701e1e673642"
duplicate_of: ""
---

# Sunder sync: i-automated-all-our-content-creation-using-openclaw-reddit-semrush-aws-g-twitter-shnai0-2021163270040846400-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/i-automated-all-our-content-creation-using-openclaw-reddit-semrush-aws-g-twitter-shnai0-2021163270040846400-FULL.md`

Primary URL: https://x.com/shnai0/status/2021163270040846400?s=46

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @shnai0: I automated all our content creation using OpenClaw: Reddit + Semrush + AWS + GitHub + GSC

**URL:** https://x.com/shnai0/status/2021163270040846400?s=46
**Author:** iuliia shnai (@shnai0)
**Posted:** Feb 10, 2026, 10:04 AM UTC
**Engagement:** 21 replies, 42 reposts, 608 likes, 58.4K views

## Summary
Near-verbatim extraction of the original X/Twitter post plus embedded X Article content when available.

## Full Article

### Original Post (Near-Verbatim)

https://t.co/W8kJufoX3F

### Embedded X Article (Near-Verbatim): I automated all our content creation using OpenClaw: Reddit + Semrush + AWS + GitHub + GSC

**Before: **2M impressions per month 
1800+ articles & page**s 
**3 people writing content
**After:** 1 bot named "Ink"
**Cost:** ~$1-5 per piece (still hard to count)

**Tools connected and account given:  **

- Reddit, HN - content ideas daily

- GitHub - access to our repo for existing content and to push new one

- AWS - upload images 

- Semrush - check keywords volume difficulty

- GSC- indexing 

**Papermark website has:**

- 1270 articles (on different languages)

- 400 help and customer stories 

- 140 pages

## What I wanted to achieve 

**1. I do not need to open computer anymore/all from mobile**
We have a 6 months old at home, every time you need to open computer this is the whole event. Babies looooove screens. So, I wanted for long time to have possibility to manage everything through phone.  

**2. Content created based on existing formats and instructions are followed and automatically updated**
When I give feedback, Ink updates its own instructions. Next article is better. It was always a problem, to repeat multiple time for content creation before,

**3. Real stories/case studies found in Reddit or Hacker News, Twitter ** always come up with some ideas for content, but I want smth on more permanent bases, that bot bring ideas based on news. Particularly because news is one of the best performing and mentioned content types.

## Set up 

There are multiple detailed articles how to set up your clawdbot, so I am not gonna write much about it but will share a bit more on how the workflow with content bot works.  

## Ink's (My bot) Workflow

Here's what happens when I send a keyword:

1. I send a keyword/or Ink send it to me via Telegram

1. Check keyword difficulty and volume in Semrush

1. Ink decides the format of article or content type: page, blog, help

1. Ink decided on subtype of blog/page

1. It creates the content following detailed guidelines

1. Takes screenshots of every tool mentioned or product

1. Uploads images to our separate repository

1. Commits to GitHub, opens a PR

1. Waits for Vercel preview to build

1. Sends me **only** the preview link

1. I review on my phone, reply with feedback

1. We iterate until approved

1. Index it in GSC when it pushed

## Step 1-2: Keywords

For now I set it two ways either I send keyword, or it send based on the recent news in Reddit, Hacker News and related to our product. The second is done via browser. 
Further it checks in Semrush keywords difficulty and volume 

[Media omitted]

After there is decision we update existing or make new content. 

**Problem**: It is not yet ideal, as it often miss smth in the repo and not find all articles for the topic.

## Step 3-5: Ink decides on format and create content

There are two level, first format of content like page or article. Second is type of the articlr/page. 

I provide instructions and GitHub access to all our repo with all article.  That way the bot can decide which article format how.

[Media omitted]

All content instructions are in here Content Instructions (WORKFLOW.md)

## Step 6. Select or take screenshots

Either it select among existing images from existing articles via GitHub or create new. 
Nee screenshots are kind of hardest part. I mainly use screenshots in articles of real tools or our tool, so the goal to make full setup of images. Currently I have a lot of troubles here. 
1. Low quality
2. Wrong formats and sizes
3. Cookie banner avoiding
So we evolved from screenshots like that: 

[Media omitted]

To screenshots like that 

[Media omitted]

To finally get me listened Iswitched from Sonnet to Opus. 

[Media omitted]

**Problem**: It is not deterministic it still make a lot of mistakes on screenshots

## Step 7. Upload images to our AWS

We have a separate website connected to our AWS bucket to add screenshots for website, now it is accessible via browser by bot. Very comfortable.

[Media omitted]

## Step 8-10 Commits, Vercel builds and Preview

So next step is commit it, I am not getting text send to me before. As I want to see full article in mdx format live, because it also can be broken if smth with mdx formatting happens 

[Media omitted]

I still did not deligate it to other bot, mainly because for now I want the process be more solid and see the result myself improving the instructions. 

## **Step 11. Iteration loop**

This currently takes most of time, Ink sending me preview link, I comment and it improves it, and building again preview, and than again and again. And of course updating instructions. But it really takes most of time now. 

Telegram easily became my most used app on the phone

[Media omitted]

## Step 12. Indexing

Last step is index what was already pushed and live. This is essential as I dont even need to think. If the new content indexed or not 

[Media omitted]

## Results

- Content done by Ink, instead of person 

- We did not loose on quality 

- I can do 90% from phone from Telegram

- Ink gets better, but not full automation

## What still can be improved?

1. **Screenshots **

This is still a huge pain, mistakes in formats in selecting existing images, so I need to do I think separate skill just for images. 

**2.  Setting up schedule**

I am not sure, but it can not remind me to do anything, so probably I need to set cron job or smth like that. I did not do anything here yet. Like for example every day it send me the news and related topic from reddit. Now it is done from my request.

**3. Better connect product and marketing project.** 

Despite Papermark repo is open , it still not navigating via it good enough. Images not taken properly. So I feel like I am missing smth here in connecting two repos. 

**4. Decrease my review time**

I still invest a lot of time, I dont know if it is set up or what, and maybe I need to set other bot for review as many of people recommend it here. 

**5. Workflow errors**

[Media omitted]


## Metadata
- Tweet ID: 2021163270040846400
- Canonical URL: https://twitter.com/shnai0/status/2021163270040846400
- Source tier used: tier2
- Embedded X article extracted: yes

