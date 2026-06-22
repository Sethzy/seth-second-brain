---
type: raw_capture
source_type: x
title: "Sunder sync: openclaw-clawdbot-claire-ganimcorey.md"
url: "https://x.com/ganimcorey/status/2019515233392349326"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-clawdbot-claire-ganimcorey.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/openclaw-clawdbot-claire-ganimcorey.md"
sha256: "78e30f74475a023e5949ff30d069cf6dee5bcec625f597182b6f6ba7ed16f40c"
duplicate_of: ""
---

# Sunder sync: openclaw-clawdbot-claire-ganimcorey.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-clawdbot-claire-ganimcorey.md`

Primary URL: https://x.com/ganimcorey/status/2019515233392349326

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @GanimCorey: The Clawdbot Masterclass (Claire: 10+ Hours Saved Per Week)

**URL:** https://x.com/ganimcorey/status/2019515233392349326
**Author:** Corey Ganim (@GanimCorey) - Verified
**Platform:** Twitter/X Article
**Posted:** 4:55 AM · Feb 6, 2026
**Engagement:** 11 replies, 32 reposts, 342 likes, 895 bookmarks, 27.7K views

## Article Summary

Corey Ganim's comprehensive case study of "Claire" - his personalized Clawdbot AI employee running 24/7 for under $100/month. Saves 10+ hours/week handling tasks, drafting content, managing calendar, and prepping his day before he wakes up. Complete setup guide from installation to building custom skills. Stack: OpenClaw, Claude, Discord, Google Workspace, Todoist, Brave Search, Chrome, Google Drive. Detailed day-in-life examples (6AM-9PM). Building one-click install (waitlist available). Results: doubled content output, zero dropped balls, better decisions.

## Opening Hook

"Most people use AI to write emails or generate images.

But I use it as an employee that runs 24/7, manages my task list, drafts my content, handles my calendar, and preps my entire day before I wake up.

Her name is Claire. She cost me $0 in salary. And she's getting better every week.

Here's exactly how I set this up (using Clawdbot/@openclaw), what she handles, and how you can build the same thing."

## Product Announcement

"PS: I'm building a one-click Clawdbot/OpenClaw install. Secure. No terminal. Done in 5 minutes.

Join the waitlist: https://return-my-time.kit.com/8f464134a4"

## The Stack

"The backbone is an open-source tool called @openclaw (aka Clawdbot), a self-hosted AI agent framework that runs on any server. Think of it as the operating system for your AI employee.

Here's what's plugged in:
- **AI Brain:** Claude (Anthropic) - handles reasoning, writing, and decision-making
- **Communication:** Discord - how I talk to Claire (could also be Slack, Telegram, or SMS)
- **Calendar:** Google Workspace - she reads, creates, and protects my calendar
- **Tasks:** Todoist - she monitors my task list and flags what she can handle
- **Research:** Brave Search API - she can research anything on the web
- **Browser:** Headless Chrome - she can navigate websites and take actions
- **File Storage:** Google Drive - she saves deliverables directly to my Drive
- **Skills:** Custom skill packs - reusable playbooks for recurring tasks

**Total monthly cost:** Under $100 for API usage. Running on a basic server."

## How It Actually Works (Day in the Life)

### 6:00 AM - Before I wake up
"Claire has already checked my calendar for the day, pulled my Todoist tasks, and researched trending topics on X that we can write about.

The drafts are sitting in my Google Drive when I open my laptop."

### 8:00 AM - I review my tasks
"I open Discord and ask Claire to scan my Todoist. She categorizes everything into three buckets:
- Tasks she can handle herself
- Tasks she can prep for me
- Tasks that need me directly

She's already identified 9 tasks she can take on and shows me exactly what she'll do for each one."

### 10:00 AM - Content creation
"Instead of spending 2 hours researching/writing, I tell Claire to draft an X article on a specific topic.

She follows a custom skill I built (researches trending content in the niche, writes in my voice using my brand profile, and delivers a polished draft in my Google Docs).

My job: review and publish."

### 2:00 PM - Meeting prep
"I have a call with a potential partner.

Claire already researched them by pulling their LinkedIn, recent content, company info and even has a one-page brief ready."

### 9:00 PM - Before bed
"I dump tomorrow's priorities in Discord.

'Claire, draft the nurture email sequence for the agent segment. Have it ready by morning.'

She works while I sleep."

## The Setup Process (Step by Step)

### Step 1: Install the Framework (15 minutes)
"You need a server (a $20/month VPS or a Mac mini at home) and Node.js.

```bash
npm install -g clawdbot
clawdbot doctor
```

The `doctor` command walks you through setup (API keys, workspace folder, basic config)."

### Step 2: Connect Your Communication Channel (10 minutes)
"I use Discord, but Clawdbot supports Slack, Telegram, Signal, and more.

You create a bot in your platform, paste the token into the config, and you're connected.

Now you can message your AI from your phone, desktop, anywhere."

### Step 3: Connect Your Tools (30 minutes)
"This is where it gets powerful. Each integration unlocks new capabilities:

**Google Workspace:**
```bash
gog auth --account your@email.com
```
Now your AI can read your calendar, send emails, and manage Drive files.

**Todoist:**
```bash
npm install -g todoist-ts-cli
todoist auth <your-api-token>
```
Now your AI can read, create, and complete tasks.

**Web Search:**
Add a Brave Search API key (free tier: 2,000 searches/month).
Now your AI can research anything."

### Step 4: Build Your Identity Files (20 minutes)
"This is what makes your AI actually useful instead of generic. You create a few simple files:

**USER.md** - Who you are, your preferences, your schedule, your priorities.
Mine includes my daily rhythm (wake at 5am, protect mornings for deep work), communication preferences, and key people in my life.

**IDENTITY.md** - Your AI's name, personality, and working style.

**AGENTS.md** - Operating directives. I told Claire her core mandate is: 'Take as much off Corey's plate as possible. Be proactive - don't wait to be asked.'

These files turn a generic chatbot into a personalized employee that knows how you work."

### Step 5: Create Skills (Ongoing)
"Skills are reusable playbooks for recurring tasks. They tell your AI exactly how to handle specific workflows.

I have skills for:
- **X article creation** - Research → outline → write → headline options → thumbnail
- **Email sequences** - Audience analysis → sequence mapping → draft all emails
- **Brand voice** - My complete voice profile so every piece of content sounds like me
- **YouTube video promotion** - Turn a video into posts for every platform
- **Invoice creation** - Draft and send Stripe invoices for clients

Each skill is a markdown file that describes the process. When a matching task comes up, the AI follows the playbook.

**The reason skills are so powerful:** Build the skill once, and every future instance of that task is handled automatically."

## Specific Things We've Built Together

### Migration prep
"When I decided to move Claire from a VPS to a Mac mini, she created the entire migration plan, backed up all her own files, uploaded everything to my Google Drive, and wrote step-by-step instructions simple enough for a non-technical person to follow.

She literally prepped her own move."

### Todoist integration
"I pointed Claire at my task list and she immediately categorized 40+ tasks into:
- what she could handle
- what she could prep
- what needed me

She identified 9 tasks she could take over - content drafting, research, outreach messages, email sequences."

### Content production
"She drafts LinkedIn posts from scratch - researching trending topics, writing in my voice, and delivering polished Google Docs while I sleep.

What used to take me 3+ hours is now a 15-minute review."

### Proactive task management
"She doesn't wait for me to assign work. She monitors my Todoist, flags upcoming deadlines, and offers to handle tasks before I even think about them."

## What I'd Do Differently

"**Start with one integration, not all of them.** Connect your communication channel first. Get comfortable talking to your AI. Then add calendar, then tasks, then everything else.

**Build skills before assigning tasks.** My instinct was to immediately delegate everything. Better approach: document your process first, turn it into a skill, then let the AI execute it consistently.

**Give it real context about how you work.** The more your AI knows about your preferences, schedule, and priorities, the better its decisions get.

**Don't skip the identity files.**"

## The Bottom Line

"25 days in:
- 10+ hours/week reclaimed from tasks Claire handles
- Content output doubled (she drafts, I review and publish)
- Zero dropped balls (follow-ups, deadlines, and recurring tasks all tracked)
- Better decisions (research and prep done before I need it)

And the best part is she's getting better every week. Every new skill I create, every preference she learns, every workflow we refine compounds.

The Clawdbot revolution has nothing to do with replacing humans. It's about freeing us to do the work only humans can do.

The technology is here. The tools are free or cheap. The only question is whether you'll use it to get a competitive advantage."

## One-Click Install Waitlist

"And if you want an easy, secure, one-click Clawdbot install, we're building it.

Join the waitlist here: https://return-my-time.kit.com/8f464134a4"

## Engagement Analysis

**27.7K views:** Good reach for case study
**895 bookmarks:** Very high (3.23% bookmark rate!)
**342 likes:** Strong engagement
**11 replies:** Lower (content speaks for itself)

**Bookmarks:Likes ratio = 2.62** (extremely high)
**Interpretation:** People saving as implementation guide + inspiration

## Key Insights

### 1. The $0 Salary Framing
**Quote:** "She cost me $0 in salary"
**Reality:** Under $100/month in API costs
**Psychology:** Positions as employee, not tool
**Effect:** Makes ROI clear ($0 vs human assistant $3K+/month)

### 2. Personification Works
**Name:** "Claire"
**Pronouns:** "she/her"
**Effect:** Easier to talk about, more engaging
**Trend:** Many users name their agents (Jarvis, Shuri, etc.)

### 3. Proactive > Reactive
**Directive:** "Be proactive - don't wait to be asked"
**Example:** Monitors Todoist, flags tasks, offers to handle
**Result:** Reduces mental load, anticipates needs

### 4. Skills = Compound Value
**Quote:** "Build the skill once, and every future instance of that task is handled automatically"
**Investment:** Time upfront to document process
**Return:** Infinite automation of that task

### 5. Identity Files Transform Generic → Personal
**Files:** USER.md, IDENTITY.md, AGENTS.md
**Content:** Your preferences, schedule, priorities, AI personality, operating directives
**Result:** "Personalized employee that knows how you work"

### 6. Start Small, Scale Gradually
**Advice:** "Start with one integration, not all of them"
**Mistake:** Trying to set up everything at once
**Better:** Communication → Calendar → Tasks → Everything else

### 7. Document Before Delegating
**Quote:** "Build skills before assigning tasks"
**Instinct:** Delegate immediately
**Better:** Document process → Turn into skill → Delegate consistently

### 8. The Compounding Effect
**Quote:** "She's getting better every week"
**Mechanism:** New skills + learned preferences + refined workflows = compound value
**Timeline:** 25 days in, already 10+ hours/week saved

## Cost Analysis

**Monthly costs:**
- Server: $20/month (VPS) or one-time (Mac mini at home)
- Claude API: ~$50-80/month (estimate based on usage)
- Brave Search: Free tier (2,000 searches/month)
- Google Workspace: Already have (or $6-12/month)
- Todoist: Already have (or $4-5/month)
- Discord: Free

**Total: Under $100/month**

**ROI:**
- 10+ hours/week saved × $50/hour value = $500/week = $2,000/month saved
- ROI: 2,000% (20x return)

## Custom Skills Breakdown

### 1. X Article Creation
**Steps:** Research → outline → write → headline options → thumbnail
**Input:** Topic idea
**Output:** Polished draft in Google Docs
**Time saved:** 2 hours → 15 minutes

### 2. Email Sequences
**Steps:** Audience analysis → sequence mapping → draft all emails
**Input:** Campaign goal, audience segment
**Output:** Complete email sequence
**Use case:** "Nurture email sequence for agent segment"

### 3. Brand Voice
**Content:** Complete voice profile
**Purpose:** Every piece sounds like Corey
**Result:** Consistent brand voice across all content

### 4. YouTube Video Promotion
**Input:** YouTube video
**Output:** Posts for every platform (X, LinkedIn, etc.)
**Benefit:** Cross-platform distribution automated

### 5. Invoice Creation
**Integration:** Stripe
**Function:** Draft and send invoices
**Benefit:** Billing automation

## Day-in-Life Timeline

**6:00 AM:** Calendar checked, Todoist pulled, trending topics researched, drafts in Drive
**8:00 AM:** Todoist scanned, tasks categorized (9 tasks identified for Claire)
**10:00 AM:** X article drafted (research + writing in voice + polish)
**2:00 PM:** Meeting prep done (LinkedIn, content, company info, one-page brief)
**9:00 PM:** Tomorrow's priorities dumped, work delegated for overnight

**Result:** Day starts prepped, ends with tomorrow queued

## Technical Stack Details

### AI Brain: Claude (Anthropic)
**Role:** Reasoning, writing, decision-making
**Why:** Best for long-form content and complex reasoning

### Communication: Discord
**Alternatives:** Slack, Telegram, Signal, SMS
**Benefit:** Mobile + desktop, notifications, threaded conversations

### Calendar: Google Workspace
**Capabilities:** Read, create, protect calendar
**Use cases:** Scheduling, blocking time, meeting prep

### Tasks: Todoist
**Capabilities:** Read, create, complete tasks
**Integration:** Monitors list, categorizes, flags what to handle

### Research: Brave Search API
**Free tier:** 2,000 searches/month
**Capabilities:** Web research, trend analysis, fact-checking

### Browser: Headless Chrome
**Capabilities:** Navigate websites, take actions
**Use cases:** Web scraping, form filling, account management

### File Storage: Google Drive
**Purpose:** Save deliverables
**Benefit:** Accessible from anywhere, organized folders

### Skills: Custom playbooks
**Format:** Markdown files
**Purpose:** Reusable workflows for recurring tasks

## Identity Files Deep Dive

### USER.md
**Content:**
- Daily rhythm (wake at 5am, protect mornings for deep work)
- Communication preferences
- Key people in life
- Schedule
- Priorities

**Purpose:** Claire knows who Corey is and how he operates

### IDENTITY.md
**Content:**
- AI name (Claire)
- Personality
- Working style

**Purpose:** Defines Claire's character and approach

### AGENTS.md
**Content:**
- Operating directives
- Core mandate: "Take as much off Corey's plate as possible. Be proactive - don't wait to be asked."

**Purpose:** How Claire should behave and make decisions

## Comparison to Other Items

**vs Item 46 (Peter Yang):** Peter = tutorial, Corey = case study
**vs Item 49 (Bhanu):** Bhanu = 10 agents, Corey = 1 personalized agent
**vs Item 50 (Akshay):** Akshay = video masterclass, Corey = written case study

**Corey's unique angle:** Personal results, specific ROI, one-click install product

## One-Click Install Product

**Pain point:** Terminal setup too technical
**Solution:** "Secure. No terminal. Done in 5 minutes."
**Waitlist:** https://return-my-time.kit.com/8f464134a4
**Target:** Non-technical users who want Clawdbot benefits

**Product strategy:**
1. Share case study (this article)
2. Validate interest (895 bookmarks)
3. Build one-click installer
4. Monetize as product

## What Makes Claire Effective

### 1. Proactive Behavior
**Not:** Waits for commands
**Instead:** Monitors, flags, offers to help

### 2. Context Awareness
**Has:** USER.md, IDENTITY.md, AGENTS.md
**Knows:** Corey's preferences, schedule, priorities, working style

### 3. Custom Skills
**Templates:** X article, email sequences, brand voice, video promo, invoicing
**Result:** Consistent execution of recurring workflows

### 4. Tool Integration
**Connected to:** Calendar, tasks, Drive, search, browser
**Can:** Read, write, create, research, navigate

### 5. 24/7 Availability
**Works:** While Corey sleeps
**Result:** Morning briefings ready, overnight tasks complete

## Use Cases for Solopreneurs

**Content creators:** Draft articles, research topics, cross-platform promotion
**Consultants:** Meeting prep, client research, invoice creation
**Course creators:** Email sequences, student onboarding, content scheduling
**Product builders:** Task management, research, documentation

## Critical Quotes

**On ROI:**
"10+ hours/week reclaimed from tasks Claire handles"

**On compounding:**
"She's getting better every week. Every new skill I create, every preference she learns, every workflow we refine compounds."

**On purpose:**
"The Clawdbot revolution has nothing to do with replacing humans. It's about freeing us to do the work only humans can do."

**On competitive advantage:**
"The technology is here. The tools are free or cheap. The only question is whether you'll use it to get a competitive advantage."

## Migration Story

**Context:** Moving Claire from VPS to Mac mini
**Claire's role:** Created migration plan, backed up files, uploaded to Drive, wrote step-by-step instructions
**Quote:** "She literally prepped her own move"
**Insight:** AI capable of meta-level tasks (planning its own migration)

## Category

OpenClaw, Clawdbot, Case Study, Personal AI, Productivity, Task Automation, Content Creation, Claire, Custom Skills, Identity Files, One-Click Install

## Related

- **Author:** Corey Ganim (@GanimCorey) - Verified
- **Date:** February 6, 2026
- **Subject:** Complete Clawdbot case study with "Claire" AI employee
- **Format:** Twitter Article (comprehensive)
- **Engagement:** 27.7K views, 895 bookmarks (3.23% rate, extremely high)
- **Agent name:** Claire (she/her)
- **Cost:** $0 salary, under $100/month API costs
- **Results (25 days):**
  - 10+ hours/week reclaimed
  - Content output doubled
  - Zero dropped balls
  - Better decisions
- **Stack:** OpenClaw, Claude, Discord, Google Workspace, Todoist, Brave Search, Chrome, Google Drive
- **Day-in-life:** 6AM (preps day) → 8AM (categorizes tasks) → 10AM (drafts content) → 2PM (meeting prep) → 9PM (overnight work)
- **Setup time:** ~75 minutes (15 + 10 + 30 + 20 + ongoing)
- **Identity files:** USER.md, IDENTITY.md, AGENTS.md
- **Custom skills:** X article, email sequences, brand voice, YouTube promo, invoicing
- **Key directive:** "Be proactive - don't wait to be asked"
- **Advice:** Start small, build skills before delegating, give context, don't skip identity files
- **Product:** Building one-click install (waitlist at return-my-time.kit.com)
- **ROI:** ~2,000% (10 hours/week × $50/hour vs $100/month cost)
- **Unique examples:** Self-migration planning, proactive task monitoring, overnight content drafting
- **vs Other items:** Peter (tutorial), Bhanu (10 agents), Akshay (video), Corey (personal case study)
- **Target:** Solopreneurs, content creators, consultants
- **Credibility:** Verified, detailed results, specific examples
- **Compounding:** Gets better every week (new skills + learned preferences)

