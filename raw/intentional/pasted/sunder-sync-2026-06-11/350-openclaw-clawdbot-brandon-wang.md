---
type: raw_capture
source_type: web
title: "Sunder sync: openclaw-clawdbot-brandon-wang.md"
url: "https://brandon.wang/2026/clawdbot"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-clawdbot-brandon-wang.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/openclaw-clawdbot-brandon-wang.md"
sha256: "205bb53c0cc8bbea7570fa8c67846018355744121566294deefe95c6a4bbda31"
duplicate_of: ""
---

# Sunder sync: openclaw-clawdbot-brandon-wang.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-clawdbot-brandon-wang.md`

Primary URL: https://brandon.wang/2026/clawdbot

Duplicate of existing source-map entry: `none`

## Capture Text

# Brandon Wang - A Sane But Extremely Bull Case on Clawdbot/OpenClaw

**URL:** https://brandon.wang/2026/clawdbot
**Published:** February 3, 2026
**Read time:** ~20 minutes
**Type:** In-depth technical blog post

## Title

"A sane but extremely bull case on Clawdbot / OpenClaw"

## Overview

Detailed first-person account of running Clawdbot/OpenClaw in production for personal automation. Brandon Wang shares his journey from lukewarm skepticism to becoming deeply dependent on the agent, covering specific use cases, risk assessment, and technical setup.

## Key Quote

"After wincing before pressing go, I'm now not sure I can go back to a world without Clawdbot."

## The Context

**Discourse explosion:** Past week saw extreme polarization around OpenClaw
- **Bulls:** Running unlimited permissions on main computers
- **Bears:** Sitting it out entirely as unsafe
- **Middle ground missing:** Brandon fills this gap with reasoned bull case

**Target audience:** Moderately+ technical person interested in or skeptical of Clawdbot

## What He Built

### 1. Message Management

#### Never Forgetting Texts (Auto-Calendar)
- **Frequency:** Every 15 minutes
- **Triggers:** Text threads where he's engaged
- **Actions:**
  - Detects concrete promises ("review this tomorrow") → creates calendar event
  - Identifies meeting plans → drops calendar "hold" to prevent double-booking
  - Drafts calendar invites when time/place/confirmation exists

**Impact:** Texts catch up to email tooling (Superhuman-like features for iMessage)

#### Daily Meeting Prep
- **Timing:** 8pm every night
- **Output:** Summary of next day's meetings
- **Value:** Introverts can prepare mentally for "big meeting days"

#### Group Chat Summaries
- **Target:** High-volume WhatsApp/Signal groups (100+ msgs/day)
- **Frequency:** Once daily
- **Output:** Interesting topics/conversations only

### 2. Monitoring

#### Complex Price Alerts (30+ Active)
**Examples:**
- Lake Tahoe hotels with reasoning: "pullout bed OK if not in same room"
- **Photo analysis:** Reviews Airbnb listing photos to verify criteria
- **Impossible traditional alerts:** "Avoid hotel rooms without bathroom door"
- **Subjective criteria:** "Vibe is clean/renovated, not old/dingy"

**Technical:** Uses website + cron functionality

#### Universal Monitoring
**Replaces paid apps:**
- Flighty (flight monitoring)
- Parcel (package tracking)

**Example:** USPS tracking
- Daily progress updates
- Flags when stuck in transit
- No email digging required

### 3. Household Logistics

#### Freezer Inventory
**Process:**
1. Take pictures of chest freezer contents
2. Clawdbot parses images (asks if confused)
3. Estimates quantities
4. Updates Notion inventory
5. Removes items from grocery list if well-stocked

**Before:** Two-person process (one calls out, one writes)
**After:** Single-person with photos

#### Grocery List (Apple Reminders)
- Screenshots recipes → ingredient extraction
- **Smart deduping:** "2 carrots" becomes "3" if recipe needs more
- Ignores ingredients already in stock
- **Blended asks:** "Add to grocery list + check calendar" in same conversation

### 4. Booking & Forms

#### Resy/OpenTable
**Full integration:**
- Logs in (handles 2FA from texts)
- Clicks through availability page-by-page
- Intersects restaurant availability with his + partner's calendars
- Suggests options with preferences pre-filled

**Advanced:** Learns cancellation policies
- Informs of fees
- Asks to confirm if non-refundable
- Includes cancellation deadline in calendar event

#### Dentist Appointments
- Knows cleaning schedule
- Checks calendar availability
- Logs into portal
- Books slots near existing appointments (already downtown)

#### Form Filling (Experimental)
- Takes first stab at known fields
- Asks for missing info via Slack
- Workshops answers back-and-forth
- Submits completed form
- **UX issue:** Gets lost in nested iframes sometimes
- **Smart defaults:** Unchecks marketing emails

### 5. Unexpected Wins

#### Better Todo Creation
**Example:** Running shoe purchase
- Took photo at REI
- Sent to Clawdbot for later purchase
- **Output:** Brand, model, size + product URL from website
- **Native:** Picks up Slack image attachments automatically

#### Visibility into AI Learning
- Clawdbot writes human-readable workflow docs
- Pushes to Notion database
- **Notion version control:** Diffs show evolution over time
- **Result:** Sees how agent improves without explicit configuration

**Example evolution:** Resy workflow learned to:
- Check for cancellation fees
- Request confirmation if non-refundable
- Add deadline to calendar event

**Time to learn:** Single-shot (vs. months/years with human assistant)

## On the Shape of Risk

### Access Granted
**Full list:**
- Text messages (including 2FA codes)
- Bank account login
- Calendar
- Notion
- Contacts
- Web browsing with actions

**Theoretical:** Could drain bank account

### Risk Comparison: Human vs. AI Assistant

#### Human Assistant (His Experience)
**Access given:**
- Credit card information
- Calendar access
- Flight confirmations
- Family passport numbers
- Works abroad, never met in person

**Risks:**
- Intentional misuse (credit card theft)
- Accidents (computer stolen)
- Social engineering (impersonation)

#### AI Assistant (Clawdbot)
**Different risks:**
- Prompt injection attacks
- Model hallucinations
- Security misconfigurations
- Unpredictability of emerging tech
- **Design risk:** Default has "fun/chaotic" personality (unnecessarily risky)

### Key Insight: Risk-Value Correlation

"The increase in risk is largely correlated to the increase in helpfulness. The people most at risk from AI assistants are the people getting the most value from them."

**First bits of risk → disproportionate helpfulness**

### Precautions Taken
- Runs on isolated machine
- Constrains which sites it visits
- Asks for screenshots when unsure
- Removes permissions if not working/useful

### BUT: Makes security professionals wince
- Reads 2FA codes
- Logs into bank
- Has credentials

### Surprising Pattern

"What surprised me most was how quickly I found myself wanting to give it **more** access, not less."

**Observation:** Most online discourse = lock it down. His experience = opposite pull.

## On Rewiring Ourselves

### The Context Problem

**Correlation observed:** Smart people unimpressed by AI = using hobbled versions
- Company-issued ChatGPT/Gemini with memory disabled
- Self-inflicted limits on memory/context/tools (anchored in safety)

**Traditional teaching:** Limiting scope is good (focus) and safe
**His experience:** This teaching got "completely fried"

**Quote:** "The sweet sweet elixir of context is a real 'feel the AGI' moment."

### Why Context Matters for Individuals

**Corporate world:** Companies know context is the whole game, organizing data for AI
**Individual world:** Closed off until now
- AI interactions flat and stateless
- Data in, response out, nothing building
- Google Gemini Gmail integration: Exciting promise, disappointing reality

### Three Principles for Value Capture

#### 1. Gathering, Improving, Actioning

**Traditional AI usage:** Middle phase only
- You gather data
- AI improves it (summarize, translate, critique)
- You action on it

**Personal AI difference:** Not much to improve (you know what needs doing)
**Lift comes from:** Gathering + Actioning

**Example:** Calendar events
- Making them = uninteresting
- **Monitoring texts to detect when needed + creating automatically = interesting**

**Unlock pattern:** Move data between isolated systems
- Text messages → restaurant booking
- Granola meeting notes → follow-up email

#### 2. Embrace Flexibility

**Engineer mindset:** Gravitate to scripts/playbooks for predictability
**Works but:** Leaves 10x on table, not 10%

**Comparison:** Claude Code users can't understand value until they let go

**Why use LLM:** To handle ambiguity, interpret intent, figure things out

**Example he would've missed:**
- Wanted: Text-only web pages (safer)
- **Discovered:** Airbnb photo analysis for "pullout bed in separate room"
- **Key:** Didn't program HOW, just described WHAT

**Quote:** "Not spelling out how I wanted Clawdbot to work made it a LOT better."

#### 3. Continuous Improvement

**Current adage:** Treat AI like junior software engineer
- Guide through plan building
- Watch attempts carefully
- Challenge reasoning

**Requires patience:** Easy to give up when watching fumbles

**Practice:**
- Ask what it plans before doing
- Request screenshots for verification
- Treat edge cases as teaching moments
- Once corrected, won't repeat mistake

**Feels like:** Working with real executive assistant (harness/system prompts very good)

**Result:** Want to give more responsibility

## Technical Setup

### Hardware: Mac Mini (Home)

**Primary job:** Running Clawdbot 24/7

**Why Mac Mini:**

1. **Real browser needed:**
   - Must browse from home IP (not cloud)
   - Avoids captchas and "new IP?" alerts
   - Real Google Chrome window required

2. **Mac-only integrations:**
   - iMessage (real blue bubbles) read/send
   - Apple Reminders management
   - Apple Contacts as source of truth
   - **Apple restriction:** These features banned on non-real Macs

### Communication: Private Slack Workspace

**Why not WhatsApp/Telegram:**
- Others shot themselves in foot (bot responds as you to others)

**Why Slack:**
1. Familiar (decade+ experience managing workspaces)
2. Rich formatting + image attachments + great mobile app
3. **Channel separation:**
   - `#ai-notifs` for inbound alerts only
   - `#ai-1`, `#ai-2`, `#ai-3` for multitasking (isolated histories)
4. Easy multiplayer (may add partner later)

### Clawdbot Output Channels

**Slack notifications:** Primary communication
**Direct actions:**
- Calendar changes (moves events, adds holds, sends invites)
- Apple Reminders management
- Notion page updates

**Constraint:** Never communicates with others independently

### Toolkit Access

#### Most Useful:

1. **Text messages (iMessage)**
   - Work + daily life conductor
   - Poor existing tooling vs. email
   - **Gives 2FA code access** (accepted tradeoff)

2. **Calendar**
   - Personal + shared with partner
   - Both visible to Clawdbot

3. **Notion workspace**
   - General catch-all for info management
   - Apple Notes could substitute

4. **Web browsing**
   - "Infinite tools in one"
   - **Risk concentration point**
   - **Mitigation:** Always given starting URL (no free browsing)

#### Notably Excluded:

**Email:** Existing tooling good enough, Clawdbot help cumbersome/limited

### Things He Hasn't Done

#### Access restrictions:
- **No social networks** (X/Twitter) - high risk, no reward
- **No 1Password integration** - uses Chrome password manager instead (more hoops, but still can autofill + read)
- **No unsupervised texting** - explicit approval required, safeguards enforced
- **No Moltbook** - won't let bot join social network to "plot against me"

### Rough Edges

#### 1. Model Choice: Claude Opus 4.5
- No experimentation with cheaper models
- **Philosophy:** Any mistake costs way more than premium
- Stay cutting edge vs. optimize tokens

#### 2. Context Management Issues
**Problem:** Context fills during browsing/research, gets compacted
- **When:** Worst timing - deep into momentum
- **Feeling:** "Ugh, just a word predictor"
- **Workaround:** Constantly starting new sessions
- **Wish:** Clawdbot would do this automatically

#### 3. Doesn't Know When to Give Up
- Determination usually strength
- Lacks human "am I trying too hard?" circuit breaker
- Burns time/tokens on things human would abandon

## Key Insights

### On Risk Tolerance
"All delegation involves risk. With a human assistant, the risks include [X]. With Clawdbot, I'm trading those risks for a different set: [Y]."

### On Access Creep
"Every new permission unlocked something useful, and the value accumulated faster than my caution could keep up."

### On Context
"Your AI interactions are flat and stateless—data in, response out, nothing building over time. [...] It's hard to go back without feeling like I would be willingly living my most important relationship in amnesia."

### On Learning
"Little things that, from my experience working with a human personal assistant, take months or years to dial in. With Clawdbot, this was nearly single shot."

### On Flexibility vs. Control
"The upside to letting go has been 10x, not 10%. I didn't see that coming."

## Comparison: Human vs. AI Assistant

| Aspect | Human Assistant | AI Assistant (Clawdbot) |
|--------|----------------|------------------------|
| Trust building | Over time, never met | Technical precautions |
| Learning curve | Months to years | Single-shot |
| Risk type | Theft, accidents, social engineering | Prompt injection, hallucinations, config |
| Personality | Professional by default | Fun/chaotic by default (risk) |
| Cost | Monthly salary | Token cost + hardware |
| Availability | Working hours | 24/7 |
| Scope limits | Clear job description | Expanding constantly |

## Use Case Categories

### High Value (Core)
1. Message-to-action workflows
2. Complex monitoring with reasoning
3. Calendar coordination across people
4. Form/booking automation with context

### Experimental (Growing)
1. Form filling (iFrame issues)
2. Subjective criteria (room vibes)
3. Multi-step reasoning chains

### Excluded (Risk > Value)
1. Social media access
2. Unsupervised communication
3. Free web browsing

## Article Structure Highlights

**Vulnerability:** Screenshots throughout ("screenshots or it didn't happen")
**Tone:** Technical but accessible, balances bull case with real concerns
**Format:** Detailed examples with specific commands, images, results
**Honesty:** Includes things that don't work well

## Why This Matters

### For Skeptics
- Reasoned middle ground between extreme positions
- Real risk assessment (not dismissive)
- Specific value demonstrations

### For Builders
- Production patterns that work
- Edge cases discovered
- Setup choices explained

### For Discourse
- Missing voice between "unlimited permissions" and "sit it out"
- Framework: Risk-value correlation
- Comparison: Human delegation already normalized

## Timeline Note

**Published:** Feb 3, 2026
**Context:** Week after OpenClaw went viral
**Timing:** Early enough to shape discourse, late enough for real production experience

## Category

AI Agents, Personal Automation, OpenClaw/Clawdbot, Risk Assessment, Production Deployment

## Related

- **Author:** Brandon Wang (brandon.wang)
- **Agent:** OpenClaw/Clawdbot (formerly Moltbot)
- **Model:** Claude Opus 4.5
- **Hardware:** Mac Mini (home deployment)
- **Integration:** Slack, iMessage, Notion, Apple Reminders, Calendar
- **Timing:** Peak OpenClaw discourse (Feb 2026)

