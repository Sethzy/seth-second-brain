---
type: raw_capture
source_type: web
title: "Sunder sync: 28-outboundphd-list-building-types-FULL.md"
url: "https://www.linkedin.com/posts/outboundphd_here-are-the-5-types-of-list-building-that-share-7423941361348915200-nHVN"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/28-outboundphd-list-building-types-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/28-outboundphd-list-building-types-FULL.md"
sha256: "2b5a05bbe5dc39962fd4e8917a75f413cb7d26ac38d71cee91d4721f98bd6a93"
duplicate_of: ""
---

# Sunder sync: 28-outboundphd-list-building-types-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/28-outboundphd-list-building-types-FULL.md`

Primary URL: https://www.linkedin.com/posts/outboundphd_here-are-the-5-types-of-list-building-that-share-7423941361348915200-nHVN

Duplicate of existing source-map entry: `none`

## Capture Text

# LinkedIn - Eric Nowoslawski: 5 Types of List Building

**URL:** https://www.linkedin.com/posts/outboundphd_here-are-the-5-types-of-list-building-that-share-7423941361348915200-nHVN
**Author:** 🦾Eric Nowoslawski (@outboundphd)
**Platform:** LinkedIn
**Posted:** 3 days ago
**Engagement:** 74 reactions, 24 comments
**Followers:** 49,662

## Post Summary

Comprehensive framework of **5 list building types** used by Eric's agency, with specific tools for each. Claims 80% of lists can be built with Type 1, but provides specialized approaches for niche/complex needs.

## Full Post Content

"Here are the 5 types of list building that come up in our agency and the tools we use to build them so hopefully you can get some ideas for your own niche lists.

We get a lot of different list requests and even though they all sound different and have mini requests, I believe they can all be built in these 5 buckets.

**1) Standard Industry and Contact Filtering**

Great when your target market has a great presence on LinkedIn or Google Maps and they self report their industries well. Still requires some keyword clean up and AI Fit scoring but **80% of people's lists can be accomplished this way.**

**Prospeo.io** recently released their database and is our daily driver for this because of their API. I now have a prospeo skill that I use that just queries whatever I want and helps me improve my searches. We can get the whole search and store it in supabase for usage later.

**2) Lookalikes**

When standard filtering isn't going to be quite good enough and your customers are all within a niche. For instance, finding a list of fintech companies is a great use case to use a lookalike tool.

**Ocean.io** and **DiscoLike** are the go-tos here. Discolike's recent case study on how Anthropic uses their tool was very compelling.

**3) Google Maps Scraping**

Great for local businesses or other companies that don't have a huge LinkedIn presence.

We built our own internally with a rapid api endpoint and what **Nico Marino** is doing with **gtme.business** looks very interesting.

**4) Custom Scraping**

Great for when an event, niche directory, facebook group, government database holds all of the gold you need.

**Instant Data Scraper** is the gateway drug of scraping chrome extensions for this. Browser automation and tools like **Browser Use** are making this even easier.

**5) Exa / Parallel Web Systems Custom Agent Searching**

I made a post on this earlier this week of how you can start with your seed list of current good fit customers and use these tools to create agents that go find another 10 that look like your current customers, run another AI to make sure they actually fit, save them, find another 10 lookalikes, and so on.

Great for really niche lists under 10k (probably even better when it's so niche your list is under 5k companies too).

**Any other list building types I might be missing?**"

## The 5 Types (Detailed Breakdown)

### Type 1: Standard Industry & Contact Filtering
**Use when:** Target market has strong LinkedIn/Google Maps presence and self-reports industries accurately

**Coverage:** 80% of people's lists

**Primary tool:** **Prospeo.io**
- Recently released database
- API-first (critical for automation)
- "Daily driver" for Eric's agency
- Custom Prospeo skill for Claude Code queries
- Stores results in Supabase

**Process:**
1. Query by industry/location/company size
2. Keyword cleanup
3. AI Fit scoring
4. Store in Supabase

**Limitations:** Requires good self-reporting, LinkedIn presence

---

### Type 2: Lookalikes
**Use when:** Standard filtering insufficient, customers all in same niche

**Example use case:** Finding fintech companies

**Primary tools:**
- **Ocean.io**
- **DiscoLike**
  - Anthropic case study was compelling
  - (DiscoLike commented: Has tech stack targeting, 2x BuiltWith coverage)
  - Better local business coverage than Google Maps
  - Good for businesses without map pins or negative reviews (dentists)

**Process:**
1. Provide seed list of good customers
2. Tool finds lookalikes based on multiple signals
3. Returns similar companies

**Value:** Goes beyond industry codes to behavioral/pattern matching

---

### Type 3: Google Maps Scraping
**Use when:** Local businesses or companies without LinkedIn presence

**Tools mentioned:**
- **RapidAPI endpoint** (Eric's team built internal tool)
- **gtme.business** (Nico Marino's tool - looks "very interesting")

**Use cases:**
- Local service businesses
- Restaurants, retailers, service providers
- Companies that prioritize local SEO over LinkedIn

**Alternative mentioned in comments:** DiscoLike claims better local coverage than Google Maps for certain categories

---

### Type 4: Custom Scraping
**Use when:** Data exists in:
- Event attendee lists
- Niche directories
- Facebook groups
- Government databases
- Industry-specific sources

**Tools:**
- **Instant Data Scraper** (Chrome extension)
  - Described as "gateway drug" of scraping
  - Easy entry point
- **Browser Use** (automation tool)
  - Making custom scraping even easier
  - Next-gen browser automation

**Process:**
1. Identify data source (event, directory, etc.)
2. Use scraping tool to extract
3. Clean and structure data
4. Match/enrich with additional data

---

### Type 5: Exa / Parallel Custom Agent Searching
**Use when:** Really niche lists under 10k companies (even better under 5k)

**Tools:**
- **Exa** (AI-powered search)
- **Parallel Web Systems** (scraping)
- **Claude Code** (orchestration - from previous post)

**Process:**
1. Start with seed list of current good-fit customers
2. Agent finds 10 companies that look like seed list
3. AI validates actual fit
4. Saves validated companies
5. Finds another 10 lookalikes from expanded list
6. Repeats iteratively

**Value:**
- Autonomous execution
- Budget-controlled
- Iterative refinement
- Good for "unsearchable" or "unlabeled" segments

**Limitations:** Not recommended for lists >10k companies

---

## Comments (24 total, 10 shown)

### Nico Marino (3d ago)
**Context:** Eric mentioned gtme.business

"of course you do this when i take it down for 48 hours lololololol. ladies and gentlemen the site will be back up in less than 24 hours."

**Reactions:** 4

---

### Joshua Solomon 🌲 (3d ago)
"Awesome! In what scenarios, do you prefer RapidAPI over Apify?"

**Question:** API choice for scraping

---

### Jeremy Schaller (3d ago - SIGNIFICANT)
"The three I'd add to the list are:

1. **Signal-based lists** (which i suppose could be considered a subset of the agent scraped lists but to me it's a very different toolkit)
   - e.g news aggregation of bankruptcy announcements

2. **Job function based lists**
   - e.g we don't care what the company is we only care that the guy manages their IT assets

3. **Tech-stack lists**
   - e.g we use **HGinsights** for what kind of products or software a company gives their employees and how much budget is spent on each category"

**Insight:** 3 additional list types not covered by Eric's 5

---

### DiscoLike (3d ago)
"Appreciate the mention! Please don't miss our **Tech Stack targeting**, it's often 2x that of BuiltWith.

And for more local businesses we will have **better coverage than Google Maps**, especially those that drive to location and don't have a pin or those that are sensitive to bad comments, like dentist offices, as they would rather not list vs have negative coverage"

**Insight:** DiscoLike positions as alternative to Google Maps for certain local biz

---

### Tom B. (3d ago)
"Love seeing you break down list building like this. My experience is that the best lists come from getting super clear on who actually has the problem you solve. Once you nail that, any tool or 'type' ends up working a lot better."

**Philosophy:** ICP clarity > tool choice

---

### Nikita Yefimov (2d ago - SIGNIFICANT)
"I'd probably sneak in a 6th bucket called **'ICP chaos mode'**: throw your existing list, product usage data and a few weird signals like changelogs or pricing updates into an LLM and let it spit out segments you'd never manually think to filter for.

Have you played with that kind of thing yet?"

**Insight:** LLM-powered segment discovery from mixed signals

---

### Amir Nurmagomedov (3d ago)
"try **CompanyEnrich** for lookalikes - that's our sweet spot."

**Reactions:** 2
**Tool mention:** CompanyEnrich as lookalike alternative

---

### Goran Zdravkovic (3d ago)
"DiscoLike is pretty fun, https://www.surfe.com/, too"

**Tool mention:** Surfe as additional option

---

### Jose Miguel Sarenas (3d ago)
"When it comes to custom scraping, where do you find these directories, facebook groups, or databases?"

**Question:** Data source discovery

---

### Richard Mechaly (3d ago)
"I promise you, the greatest obstacle in not succeeding is simply not following your advice, we are drowning in information overload."

**Pain point:** Too much information, not enough execution

---

## Extended Framework: 8 Types (Eric's 5 + Comments)

### Jeremy's 3 Additions:

**6. Signal-Based Lists**
- **Triggers:** Bankruptcy announcements, funding rounds, layoffs, expansions
- **Tools:** HGinsights (implied), news aggregation
- **Use case:** Time-sensitive targeting based on business events

**7. Job Function Lists**
- **Target:** Role-based, company-agnostic
- **Example:** "IT asset managers" regardless of company
- **Use case:** Persona targeting across industries

**8. Tech Stack Lists**
- **Tool:** HGinsights
- **Data:** What software company uses + budget per category
- **Use case:** Replacement sales, complementary products
- **DiscoLike alternative:** 2x better coverage than BuiltWith

### Nikita's Addition:

**9. ICP Chaos Mode**
- **Inputs:** Existing list + product usage data + "weird signals" (changelogs, pricing updates)
- **Process:** Feed to LLM, discover unexpected segments
- **Use case:** Finding patterns humans wouldn't think to look for
- **Status:** Proposed, not yet validated

## Tool Landscape

### By Category

| Type | Tool(s) | Notes |
|------|---------|-------|
| **Standard filtering** | Prospeo.io | API-first, Eric's daily driver |
| **Lookalikes** | Ocean.io, DiscoLike, CompanyEnrich | DiscoLike used by Anthropic |
| **Google Maps** | RapidAPI, gtme.business | Eric built internal solution |
| **Custom scraping** | Instant Data Scraper, Browser Use | Chrome extensions → automation |
| **Agent search** | Exa, Parallel Web Systems, Claude Code | For <10k company lists |
| **Signals** | HGinsights, news aggregators | Event-triggered |
| **Job function** | (Not specified) | Role-centric databases |
| **Tech stack** | HGinsights, DiscoLike, BuiltWith | Software/budget intelligence |
| **Other** | Surfe | Mentioned in comments |

### Tool Comparisons from Comments

**Tech stack:**
- DiscoLike: "2x that of BuiltWith"
- HGinsights: Budget + software categories

**Local business:**
- DiscoLike: Better than Google Maps for sensitive businesses (dentists), drive-to locations

**Lookalikes:**
- Ocean.io: Established
- DiscoLike: Used by Anthropic
- CompanyEnrich: "Our sweet spot"

## Key Insights

### 1. The 80/20 Rule
**Quote:** "80% of people's lists can be accomplished this way [Type 1]"

**Implication:** Most businesses should start with standard filtering, only move to advanced methods when needed.

### 2. Tool Proliferation is Real
**Evidence:**
- 9+ tools mentioned in post + comments
- Multiple tools per category
- New tools constantly emerging (gtme.business, Browser Use)

**Challenge:** Tool selection paralysis

### 3. API-First is Critical
**Eric's priority:** Prospeo.io chosen partly "because of their API"

**Why:** Enables:
- Automation
- Custom Claude Code skills
- Supabase storage
- Programmatic workflows

### 4. Agent-Based is Emerging
**Type 5** (Exa/Parallel/Claude Code) is newest, most cutting-edge approach

**Characteristics:**
- Autonomous execution
- Iterative refinement
- Budget-aware
- Best for niche (<10k)

### 5. Case Studies Matter
**Quote:** "Discolike's recent case study on how Anthropic uses their tool was very compelling."

**Impact:** Social proof from reputable AI company drives tool adoption.

### 6. Local Business is Underserved
**DiscoLike insight:** Many local businesses avoid Google Maps due to:
- Negative review concerns (dentists)
- Drive-to locations (no fixed pin)
- Review management challenges

**Opportunity:** Alternative data sources for local biz lists

## Use Cases by List Type

### Type 1: Standard Filtering
- **Industry targeting:** Tech companies in SF Bay Area
- **Company size filtering:** Series B-C SaaS companies
- **Location targeting:** Remote-first companies in US

### Type 2: Lookalikes
- **Example given:** Fintech companies
- **Other:** AI infrastructure companies, vertical SaaS in specific niche
- **Anthropic use case:** (Case study exists but not detailed here)

### Type 3: Google Maps
- **Local services:** Restaurants, retail, home services
- **Professional services:** Medical, legal, accounting (local)
- **Physical locations:** Gyms, salons, car washes

### Type 4: Custom Scraping
- **Events:** Conference attendees, webinar registrants
- **Directories:** Industry-specific member lists
- **Gov databases:** Licensed contractors, certified professionals
- **Facebook groups:** Niche community members

### Type 5: Exa/Parallel Agent
- **Niche B2B:** Non-QM loan funders (from previous post)
- **Unlabeled:** Luxury commercial security
- **Media-first:** Newsletter companies
- **Any:** <10k total addressable market

### Type 6: Signal-Based
- **Growth signals:** Recent funding, hiring sprees
- **Distress signals:** Layoffs, bankruptcy
- **Change signals:** New CEO, office moves

### Type 7: Job Function
- **Cross-industry:** IT asset managers everywhere
- **Role-first:** CTOs at companies 50-500 employees
- **Function-specific:** RevOps leaders regardless of vertical

### Type 8: Tech Stack
- **Replacement:** Companies using competitor software
- **Complementary:** Salesforce users without Outreach
- **Budget intelligence:** Companies spending $X on category

## Eric's Agency Approach

### Infrastructure
- **Storage:** Supabase (mentioned for Prospeo data)
- **Automation:** Claude Code skills
- **API integration:** Prospeo.io, RapidAPI
- **Custom tooling:** Internal Google Maps scraper

### Workflow
1. Classify list request into one of 5 types
2. Select appropriate tool(s)
3. Execute search/scraping
4. Store in Supabase
5. AI Fit scoring
6. Keyword cleanup
7. Deliver to client

### Philosophy
**Quote from Tom B.'s comment (Eric's agreement implied):**
"The best lists come from getting super clear on who actually has the problem you solve."

**ICP first, tools second.**

## Category

List Building, B2B Sales, Prospecting, Sales Intelligence, Tools, Frameworks, AI Agents

## Related

- **Author:** Eric Nowoslawski (outboundphd)
- **Tools:** Prospeo.io, Ocean.io, DiscoLike, Exa, Parallel Web Systems, gtme.business, Instant Data Scraper, Browser Use, HGinsights, CompanyEnrich, Surfe
- **Related post:** Item #27 (Exa/Parallel/Claude Code niche lists)
- **Framework:** 5 types (Eric) + 3 additions (Jeremy) + 1 experimental (Nikita) = 9 total
- **Coverage:** 80% of lists via Type 1 (Standard filtering)
- **API-first:** Prospeo.io chosen for API access
- **Storage:** Supabase
- **Automation:** Claude Code skills

