---
type: raw_capture
source_type: web
title: "Sunder sync: 27-outboundphd-niche-lists-FULL.md"
url: "https://www.linkedin.com/posts/outboundphd_3-times-in-the-last-month-we-had-a-niche-share-7423928893520269312-O1L-"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/27-outboundphd-niche-lists-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/27-outboundphd-niche-lists-FULL.md"
sha256: "423b3d3b4f80c52030acb713e3febe16dfdf0db8c226cf48b101cc49b27e9ddc"
duplicate_of: ""
---

# Sunder sync: 27-outboundphd-niche-lists-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/27-outboundphd-niche-lists-FULL.md`

Primary URL: https://www.linkedin.com/posts/outboundphd_3-times-in-the-last-month-we-had-a-niche-share-7423928893520269312-O1L-

Duplicate of existing source-map entry: `none`

## Capture Text

# LinkedIn - Eric Nowoslawski: Building Niche Lists with Exa + Parallel + Claude Code

**URL:** https://www.linkedin.com/posts/outboundphd_3-times-in-the-last-month-we-had-a-niche-share-7423928893520269312-O1L-
**Author:** 🦾Eric Nowoslawski (@outboundphd)
**Platform:** LinkedIn
**Posted:** 4 days ago
**Engagement:** 50 reactions, 8 comments

## Author

**Eric Nowoslawski**
- LinkedIn: linkedin.com/in/outboundphd
- Known for: Sales/outbound strategies
- Emoji brand: 🦾 (mechanical arm - representing automation/power)

## Post Summary

Used **Exa + Parallel Web Systems + Claude Code** to build niche B2B lists that traditional tools couldn't handle. Cost $20 for test, scaled up after validation. Good for lists under 10,000 companies.

## Full Post Content

"3 times in the last month, we had a niche list we needed to build and a combination of **Exa** and **Parallel Web Systems** really came in handy.

Lists that I was struggling to build with normal tools because the qualification they were looking for was high and they aren't on LinkedIn very much and don't have a google maps category.

Here were some examples:
- Funders of non-QM loans
- Luxury commercial security companies
- Newsletter companies (not just companies with a newsletter, they are media companies as a newsletter)

The funders might be on LinkedIn but you have to process a sea of Banking and Financial Services companies. There's no such thing as a luxury security company industry or Google maps listing and they don't have a LinkedIn presence anyway. Newsletter companies report themselves as being in whatever industry their newsletter is about and you can't just search for \"newsletter\" in their descriptions because so many regular companies have that as a CTA in their linkedin descriptions.

So I fired up **Claude code** to run Exa and Parallel with some goals. I said, \"here's a list of their customers that we know are good fits, find companies that look like them and create searches programmatically to find more. Dedupe along the way. Check in every 10 searches or so on budget. For this test, I'm willing to spend $20.\"

And then it got to work.

- Writing the prompt for what makes a company a good fit so I can approve.
- Creating the programmatic searches like \"non QM lender NYC\" vs. \"Los Angeles\"
- Everything.
- Hit the budget so I could approve it.
- Made some tweaks, gave it a bigger budget and let it rock.

I wouldn't suggest when you need to target a list you think is going to end being bigger than 10,000 but really good for helping build out really niche lists below that."

## Problem: Hard-to-Target Lists

### Difficulty Factors

1. **Not on LinkedIn** (or minimal presence)
2. **No standard industry classification**
3. **No Google Maps category**
4. **High qualification needed**
5. **Hidden in noise** (e.g., funders buried in "Banking & Financial Services")
6. **Ambiguous signals** (e.g., "newsletter" appears in CTAs, not just actual newsletter companies)

### Example Segments

#### 1. Funders of Non-QM Loans
**Challenge:** Buried in sea of Banking/Financial Services companies
**Why hard:** No industry code for "non-QM lender"
**LinkedIn presence:** Some, but undifferentiated

#### 2. Luxury Commercial Security Companies
**Challenge:** No "luxury security" industry or category
**Why hard:** Regular security companies don't self-identify as "luxury"
**LinkedIn presence:** Minimal

#### 3. Newsletter Companies (Media-First)
**Challenge:** Self-report industry of newsletter topic (tech, finance, etc.)
**Why hard:** "Newsletter" keyword polluted by regular companies with newsletter CTAs
**Example:** Tech newsletter company lists itself as "Software" not "Media"
**Qualification:** Must be media company as newsletter, not company with newsletter

## Solution Stack

### 1. Exa
**Type:** AI-powered search tool
**Use:** Find companies matching semantic criteria
**Advantage:** Goes beyond keyword/industry filters

### 2. Parallel Web Systems
**Type:** Web scraping/data extraction
**Use:** Extract data from discovered companies
**Advantage:** Scalable data collection

### 3. Claude Code
**Type:** AI coding assistant
**Use:** Orchestrate Exa + Parallel, manage workflow
**Advantage:** Autonomous execution with budget control

## Workflow

### Phase 1: Setup
1. **Gather seed list** - Known good-fit customers
2. **Define prompt** - What makes company a good fit
3. **Set budget** - Start with $20 test
4. **Launch Claude Code** - Autonomous execution begins

### Phase 2: Execution (Automated)
**Claude Code handles:**
1. **Prompt writing** - Translates criteria to search prompts
2. **Programmatic search generation**
   - Example: "non QM lender NYC"
   - Example: "non QM lender Los Angeles"
   - Varies by geography, modifiers, etc.
3. **Search execution** - Runs Exa/Parallel queries
4. **Deduplication** - Removes duplicates along the way
5. **Budget tracking** - Checks in every ~10 searches
6. **Approval checkpoints** - Presents results for human review

### Phase 3: Refinement
1. **Review initial results** - $20 test batch
2. **Make tweaks** - Adjust criteria/prompts
3. **Increase budget** - Scale up after validation
4. **Let it rock** - Autonomous execution continues

## Key Innovation: Budget-Aware Agent

**Pattern:** Autonomous execution with spending limits

**How it works:**
- Claude Code tracks API costs
- Checks in every 10 searches
- Waits for approval before continuing
- Prevents runaway spending

**Why this matters:**
- Most agent failures = uncontrolled costs
- Budget checkpoints = safety + control
- Iterative refinement = better results
- Human-in-loop only when needed

## Economics

### Test Phase
**Budget:** $20
**Purpose:** Validate approach
**Output:** Sample list for review

### Scale Phase
**Budget:** Increased (amount not specified)
**Purpose:** Build full list
**Output:** Complete niche list

### ROI Calculation
**Alternative:** Manual research
- Hours per company: 5-15 minutes
- 100 companies: 8-25 hours
- At $50/hour: $400-$1,250
- At $100/hour: $800-$2,500

**This approach:** $20-$100
**Savings:** 80-95%

## Limitations

**Not good for:**
- Lists expected to exceed 10,000 companies
- Reason: Cost/efficiency tradeoff changes at scale

**Good for:**
- Niche lists under 10,000
- High-qualification segments
- Hard-to-find companies

## Comments (8)

### Nikita Yefimov (3d ago)
"The budget check every 10 searches is a nice pattern, it turns list building into a controlled experiment instead of a blind scrape. That kind of feedback loop is what most people skip when they bolt LLMs onto data vendors. Have you tried keeping the \"what makes a good fit\" prompt as a reusable asset across projects, almost like a living ICP spec you refine with each new niche?"

**Insight:** Budget pattern = controlled experiment, not blind scrape

### Garrett Wolfe (4d ago)
Links to: https://garrettawolfe.substack.com/p/maybe-we-arent-thinking-big-enough
"Wrote ab how cool these platforms are here"

**Related content:** Substack article about Exa/Parallel

### Arvin Zatulovsky (4d ago)
"Seems there is a trend movimg away from Clay to CC. Same trend happend 1 year ago when n8n took over make.com"

**Insight:** Clay → Claude Code migration (similar to make.com → n8n)

### David Walker-Dobson (3d ago)
"$20 for a niche list that converts is a bargain. building that manually would take days."

**Validation:** Economics work, time savings massive

### Can Timağur (3d ago)
"Totally get this Eric, Exa and Parallel is the move for anything unsearchable or unlabeled"

**Pattern:** Exa + Parallel = go-to for unlabeled segments

### Others (3-4d ago)
- "Huge fan of exa!"
- "Exa is great"
- "building lists based on lookalikes is way smarter than generic industry filters"

## Key Insights

### 1. Lookalike > Industry Filters
**Old way:** Filter by industry/company size/location
**New way:** "Find companies like these good customers"
**Why better:** Captures patterns humans can't articulate

### 2. Trend: Clay → Claude Code
**What's happening:** Migration from no-code tools to AI agents
**Why:** More flexible, cheaper, autonomous
**Similar to:** make.com → n8n migration (2024)

### 3. Budget Pattern Innovation
**What:** Check-ins every N searches
**Why important:** Prevents blind scraping, enables refinement
**Contrast:** Most LLM+data vendor integrations lack this

### 4. ICP-as-Prompt Asset
**Nikita's suggestion:** Reuse "good fit" prompts across projects
**Benefit:** Living ICP specification that improves over time
**Implementation:** Not confirmed if Eric does this yet

## Technical Stack Deep Dive

### Exa
**What it does:** AI-powered semantic search
**How it works:** Understands "companies like X" not just keywords
**Use case:** Find unlabeled/unsearchable segments
**Alternative:** Traditional scraping (misses semantic matches)

### Parallel Web Systems
**What it does:** Web data extraction at scale
**How it works:** Scrapes company data from multiple sources
**Use case:** Enrich discovered companies with details
**Alternative:** Manual research

### Claude Code
**What it does:** Autonomous coding agent
**How it works:** Writes prompts, executes searches, dedupes, tracks budget
**Use case:** Orchestration layer for Exa + Parallel
**Alternative:** Manual execution (slow, error-prone)

## Use Cases

### For Sales Teams
- **Niche vertical targeting**
- **Account-based marketing lists**
- **Lookalike customer expansion**
- **Competitive intelligence**

### For Investors
- **Deal sourcing in specific niches**
- **Market mapping**
- **Portfolio company lookalikes**
- **Vertical landscaping**

### For Recruiters
- **Companies in emerging categories**
- **Startup cohort identification**
- **Executive search lists**

## Comparison to Alternatives

| Tool | Method | Cost | Speed | Accuracy |
|------|--------|------|-------|----------|
| **Exa+Parallel+Claude** | AI semantic | $20-100 | Hours | High |
| **Clay** | No-code automation | $$$ | Hours | Medium |
| **ZoomInfo/Apollo** | Database filters | $$$$ | Minutes | Low (for niche) |
| **Manual LinkedIn** | Human research | $$$$ | Days | High |

**Sweet spot:** Niche segments too hard for databases, too expensive to do manually.

## Category

Sales Intelligence, List Building, AI Agents, B2B Prospecting, Niche Targeting, Claude Code, Exa, Parallel Web Systems

## Related

- **Author:** Eric Nowoslawski (outboundphd)
- **Tools:** Exa, Parallel Web Systems, Claude Code
- **Trend:** Clay → Claude Code migration
- **Pattern:** Budget-aware autonomous agents
- **Use case:** Niche list building (<10k companies)
- **Cost:** $20 test → scale up
- **Alternative:** Manual research (8-25 hours)
- **Related:** Garrett Wolfe substack article

