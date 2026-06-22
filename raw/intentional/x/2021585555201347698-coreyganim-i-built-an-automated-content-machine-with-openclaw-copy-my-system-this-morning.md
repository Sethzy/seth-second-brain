---
type: raw_capture
source_type: x
url: https://x.com/coreyganim/status/2021585555201347698
original_url: https://x.com/GanimCorey/status/2021585555201347698
author: "Corey Ganim"
handle: coreyganim
status_id: 2021585555201347698
captured_at: 2026-06-19T20:17:53+08:00
published_at: "Wed Feb 11 14:02:10 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 6
  reposts: 18
  likes: 251
---

# X post by @coreyganim

## Source

- Original: [https://x.com/GanimCorey/status/2021585555201347698](https://x.com/GanimCorey/status/2021585555201347698)
- Canonical: [https://x.com/coreyganim/status/2021585555201347698](https://x.com/coreyganim/status/2021585555201347698)
- Author: Corey Ganim (@coreyganim)

## Verbatim Text

I Built An Automated Content Machine With OpenClaw (copy my system)

This morning I woke up to a finished X article in my Google Drive. Research done. Headlines written. Thumbnails designed.

I didn't write a word.

I spent yesterday building an AI "ghostwriting" employee (using @openclaw) that does this job every morning at 7 AM.

Here's exactly what I built and how you can build the same thing.

PS: I made a custom GPT that interviews you (takes 3 minutes) then delivers a custom AI Agent Blueprint.

The blueprint contains the skills/data you need in order to launch an effective custom AI agent.

Grab it (free) here: [http://return-my-time.kit.com/4b0927a64c](https://t.co/CJwQXs0PCm)

-----------------------------------

# The Problem: Content Production is a Time Trap

Most people use AI like this:

1. Open ChatGPT

2. Write prompt: "Write an article about X"

3. Get output

4. Edit for 30 minutes

5. Format it

6. Create thumbnails (20 minutes)

7. Upload to your platform

8. Write headlines

9. Finally publish

Total time: 2-3 hours per article.

You're still doing most of the work. AI just made step 3 slightly faster.

But everything changed when I stopped using AI as a tool and started treating it as an employee.

# What an AI Employee Actually Means

An employee doesn't wait for you to assign tasks. They have a job description and a schedule.

My AI employee's job description:

- Research trending topics in AI/marketing every morning

- Write an 800-1000 word article in my voice

- Generate 5-7 headline options

- Create 3 thumbnail designs (5:2 ratio for X)

- Upload everything to Google Drive

- Send me a summary in Discord

Schedule: Every day at 7:00 AM EST (via cron job)

My involvement: 5 minutes to review and approve. That's it.

# The Tech Stack (All No-Code/Low-Code)

You don't need to be a developer. Here's what I used:

Core: OpenClaw (AI agent platform)

Skills:

- x-article-creation (custom skill I built)

- last30days (trending topic research)

- brand-voice (writes in my style)

- browser (renders thumbnail HTML)

Integrations:

- Google Drive (via gog CLI)

- Discord (for notifications)

- Cron (for scheduling)

Cost: ~$0.50 per article in API calls (Claude Sonnet 4)

# How I Built It (The Full Workflow)

Step 1: Research Trending Topics

The AI employee starts by running the last30days skill:

```
python3 last30days.py "AI marketing automation" --days=7
```

This scrapes:

- Reddit discussions (last 7 days)

- X posts (high engagement)

- Web articles

It picks the topic with the most engagement and a unique angle I can own.

Alternative: If I built something interesting yesterday, it writes about that instead (build-first approach).

Step 2: Write the Article

The AI uses my brand voice profile to write 800-1000 words.

How it knows my voice:

- I created a brand voice profile document with:

- Words I use vs. avoid

- Sentence structure patterns

- Example writing samples

- Tone guidelines

The AI references this every time it writes.

Result: First drafts that actually sound like me.

Where most people fail: They don't document their voice, so AI output is generic.

Step 3: Generate Headlines

After writing the article, it creates 5-7 headline options using proven patterns:

- Number + Curiosity: "5 AI Workflows That Made Me Say 'Wait, It Can Do That?'"

- Bold Claim + Proof: "I Automated 23 Hours/Month. Here's the Exact System."

- Before/After: "From 2.5 Hours to 5 Minutes Per Article"

- Accessibility: "AI Agents for Non-Technical Business Owners"

I pick the one that fits the angle best.

Step 4: Create Thumbnails

The AI generates 3 HTML files with different thumbnail designs:

Thumbnail A: Dark theme with stat boxes
Thumbnail B: Clean text focus with big numbers
Thumbnail C: Grid layout with key points

It renders each HTML file in a browser, takes a screenshot at 1200×480px, and saves as PNG.

Why HTML instead of image generation APIs: Full control over layout, typography, and brand consistency. Plus it's free.

Step 5: Upload Everything

All files go to Google Drive:

- Article as markdown file

- 3 thumbnail PNGs

The AI uses gog drive upload to handle this automatically.

Why Google Drive: Easy to access from any device, built-in version history, shareable links.

Step 6: Notify Me

Finally, it sends me a Discord message:

📊 X Article Complete: [Topic]

✅ Google Doc: [link]

✅ Word count: 987

📰 7 Headline Options: [listed]

🎨 3 Thumbnails: [attached]

Ready to publish!

I click the link, review for 5 minutes, pick a headline and thumbnail, and publish.

Total time from waking up to published article: 7 minutes.

# The Cron Job (How It Runs on Schedule)

This is the key difference between a tool and an employee: employees have a schedule.

I created a cron job that triggers the workflow every morning:

```
0 12 * * * # Runs at 7 AM EST (12 UTC)
```

The cron job sends a system event that says: "Run the x-article-creation skill with today's date."

The AI wakes up, does the work, and goes back to sleep.

I don't trigger it. I don't think about it. It just runs.

# What This Actually Saves Me

Before (manual process):

- Research: 30 min

- Writing: 60-90 min

- Headline variations: 15 min

- Thumbnails: 20-30 min

- Formatting/upload: 10 min Total: 2.5-3 hours per article

After (AI employee):

- Review article: 3 min

- Pick headline: 1 min

- Pick thumbnail: 1 min Total: 5 minutes per article

Time saved per article: 2.5 hours
Articles per week: 5-7
Time saved per week: 12.5-17.5 hours
Time saved per month: 50-70 hours

That's more than a full-time hire. For $15-20/month in API costs.

# The Mental Shift That Makes This Work

Most people think: "How can AI help me write faster?"

I started thinking: "What if AI had this job and I was the manager?"

When you're the writer: You prompt, edit, format, upload, manage every step.

When you're the manager: You review output and approve/reject.

The work happens without you. You're just the quality gate.

# Common Mistakes (What Doesn't Work)

Mistake 1: Trying to automate everything at once

I didn't start with a 7-step workflow. I started with:

- Step 1: AI writes article

- That's it.

Then I added:

- Step 2: AI generates headlines

Then:

- Step 3: AI creates thumbnails

One piece at a time. Each piece worked before I added the next.

Mistake 2: Not documenting your voice

If you don't give the AI a voice profile, it will write in "AI voice" (generic, bland, and obviously not you).

Spend 30 minutes creating a voice document:

- Words you use

- Words you never use

- Sentence structure

- Example paragraphs

The AI will reference this forever.

Mistake 3: Manual triggers

If you have to remember to run the workflow, you'll forget. Or you'll skip it when busy.

Schedule it. Make it automatic. That's what makes it an employee.

# How to Build Your Own (Starting Today)

You don't need my exact stack. Here's the framework:

Step 1: Pick one content type

Don't automate everything. Pick one:

- X articles

- LinkedIn posts

- Email newsletters

- Podcast show notes

- YouTube video scripts

Start with whichever takes you the most time.

Step 2: Map your current process

Write down every step you do manually:

1. Research topic

2. Outline

3. Write first draft

4. Edit

5. Format

6. Create graphics

7. Upload/publish

Step 3: Automate steps 1-6, keep step 7

AI can handle research, writing, formatting, and graphics. You should still approve and publish.

Step 4: Build It Iteratively

Week 1: AI writes first draft
Week 2: AI also does research
Week 3: AI creates graphics too
Week 4: Full workflow automated

Step 5: Schedule it

Once it works manually, set up a cron job or scheduled task. Make it run daily or weekly without you.

# The ROI Math

Your time is worth: $X per hour (fill in your rate)

Hours saved per month: 50-70

Value returned: $ X × 50-70

Cost: $15-20/month in API calls

ROI: Depends on your hourly rate, but for most business owners: 10-50x minimum.

# What I'd Build Next (If I Were You)

If this article resonated, here are the next AI employees to build:

1. Email responder - Drafts replies to common emails in your voice, you just review and send

2. Meeting prep agent - Researches everyone on your calendar, creates brief before each call

3. Social media repurposer - Takes one piece of content (article, video, podcast) and creates 5-10 social posts

4. Weekly newsletter - Compiles what you built/learned this week, drafts newsletter

5. Client onboarding - Sends welcome emails, schedules kickoff, creates project folders

Each one follows the same pattern:

1. Define the job

2. Document your voice/preferences

3. Build the workflow

4. Schedule it

-------------------------

Want to build something similar?

My Agent Blueprint Builder custom GPT (free) can help.

It'll give you a blueprint of the exact data/skills you need to create an effective custom AI agent.

Get it here: [http://return-my-time.kit.com/4b0927a64c](https://t.co/CJwQXs0PCm)

## X Article Metadata

- Title: I Built An Automated Content Machine With OpenClaw (copy my system)
- Preview: This morning I woke up to a finished X article in my Google Drive. Research done. Headlines written. Thumbnails designed. 
I didn't write a word.
I spent yesterday building an AI "ghostwriting"

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
