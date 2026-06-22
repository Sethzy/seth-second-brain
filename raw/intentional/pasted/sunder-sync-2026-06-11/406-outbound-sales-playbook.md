---
type: raw_capture
source_type: x
title: "Sunder sync: Outbound Sales Playbook.md"
url: "https://www.clay.com/blog/b2b-cold-email-deliverability"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/03_Resources/Playbooks/Sales/Outbound Sales Playbook.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "03_Resources/Playbooks/Sales/Outbound Sales Playbook.md"
sha256: "6b77fea23f53c01a269054dbc052eaa224273fecce64c36995a84aa865637f54"
duplicate_of: ""
---

# Sunder sync: Outbound Sales Playbook.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/03_Resources/Playbooks/Sales/Outbound Sales Playbook.md`

Primary URL: https://www.clay.com/blog/b2b-cold-email-deliverability

Duplicate of existing source-map entry: `none`

## Capture Text

# Outbound Sales Playbook

> Condensed from SalesCraft methodology. Original: `temp_resources/2025 Overview of SalesCraft.md`

---

## Core Philosophy

**AI tools are multipliers.** They take what works manually and scale it 100x. But 0 x 100 = 0. If your offer doesn't resonate, no amount of AI personalization will fix it.

**Cold email is like a private ads network:**
- You can guarantee impressions (open rates)
- You cannot guarantee conversions (meetings)
- Success depends on how much prospects need your product

---

## The Process Overview

```
1. Define ICP (Baseline + Best Case Signals)
        ↓
2. Build List (Apollo + Job Boards + Custom Scraping)
        ↓
3. Dedup & Enrich (Clay)
        ↓
4. AI Qualify & Score
        ↓
5. Segment into 6-10 Campaigns
        ↓
6. Write Personalized Copy (AI-assisted)
        ↓
7. Send via Warmed Inboxes
        ↓
8. Track & Iterate
```

---

## 1. Define Your ICP

### Layer 1: Baseline ICP (Minimum Criteria)

The fallback when no other signals are available.

**Example (SalesCraft):**
- B2B Company
- Inferred LTV of $5,000+ or enterprise pricing
- Less than 100 employees
- Target: CEOs, Sales/Marketing heads
- Exclude: staffing, fintech, IT outsourcing, cybersecurity

### Layer 2: Best Case Signals (Buyer Intent)

> "If we had 10 minutes to research and qualify your dream prospect, what data points are we looking for?"

**Example signals:**
- Hiring for sales/ops roles (job boards)
- First-time founder
- Technical founder without sales head
- Recently fundraised
- DMARC/email config issues
- Specific tech stack (e.g., uses HubSpot)
- Recent LinkedIn posts about relevant pain

**Split into 6-10 campaigns** based on signal combinations.

---

## 2. Build Your List

### Primary Sources

| Source | Best For | Notes |
|--------|----------|-------|
| **Apollo** | General B2B, US/EU | Best price-to-quality ratio. Start here 90% of time |
| **LinkedIn Sales Nav** | Any B2B | Source of truth for contact data |
| **Job Boards** | High-intent signals | Companies actively hiring = active pain |
| **Crunchbase** | VC-backed, funding data | No contact details - enrich via Apollo |
| **Storeleads** | Ecommerce | Market leader for ecommerce data |
| **Google Maps** | Local SMBs | Use Outscraper or D7 Lead Finder |

### Apollo Best Practices

**Building company lists:**
- Use NAIC codes or Industry filters if ICP fits
- Use "Company keyword search" for SaaS, Ecommerce, etc.
- Exclude: Coach, Consulting, Agency
- Check top 5 results to validate keyword effectiveness

**Building contact lists:**
- Use job title filter: "chief marketing" or "head marketing"
- Only export verified emails (6% bounce vs 20% unverified)
- Double-validate with Debounce in Clay

**Columns to export:**
- First Name, Last Name, Title
- Company Name, Email, Employees
- Industry, Website
- Person LinkedIn URL, Company LinkedIn URL
- City, State, Country

### Email Waterfall (Clay)

Use max 3 providers in sequence:
1. **Prospeo** → 2. **Findymail** → 3. **Datagma**

Findymail and Datagma only charge for valid emails found.

### Validation

- **Debounce** ($0.0015/email) - best price-to-quality
- Keep bounce rate below 2-3% or domain gets burnt

---

## 3. Dedup & Enrich

Use **Clay** to:
- Normalize company names
- Merge duplicates from multiple sources
- Enrich with missing emails (waterfall)
- Add signal data (tech stack, hiring, funding)
- Score and qualify

---

## 4. Create Your Offer

### Alex Hormozi Value Equation

**Increase:**
- Dream Outcome
- Perceived Likelihood of Achievement

**Decrease:**
- Perceived Time Delay
- Perceived Effort & Sacrifice

### Offer Enhancers

| Lever | Example |
|-------|---------|
| **Scarcity** | "We only service 25 customers total. We have a waitlist." |
| **Urgency** | "X% discount if you sign by Y date" |
| **Bonuses** | Stack additional deliverables with named value |
| **Guarantees** | "3 month commitment, then month-to-month" |

### 3 Reasons B2B Buyers Buy

1. **Save Money** - cheaper than competitor
2. **Make Money** - improves conversion/revenue
3. **Save Time** - automation, efficiency

Write value props for each and A/B test.

### Lead Magnets

**Tangible (best):** Free deliverable they'd normally pay for
- Free list of 100 qualified prospects
- Free audit of their current setup
- Free template they can use immediately

**Intangible:** Insights they can't get elsewhere
- Founding story / expertise
- Data across your customer base
- Competitor analysis
- Industry benchmarks

**Template:**
```
I saw {{something relevant}}

We help companies achieve {{results}}

But I'd never expect you to believe me without giving you something first.

I made you a {{resource}} - would you let me know if it's useful?
```

---

## 5. Email Infrastructure

### Domain Setup

- Buy secondary domains (trysunder.com, getsunder.co)
- Use .com or .co only
- Max 3 email seats per domain
- Max 40 emails/day per inbox
- Use Google Workspace or Microsoft 365

### DNS Configuration

1. MX Records (mail routing)
2. DKIM (email authentication)
3. SPF (sender verification)
4. DMARC (authentication protocol)
5. Domain redirect to primary

### Warm-up Rules

- Start: 5 warm-up emails day 1
- Ramp: +5 emails/day
- Cap: 50 emails/day warm-up
- Duration: 3 weeks minimum
- During campaign: Keep 10/day warm-up at 100% reply rate

### Deliverability Rules

**Copywriting:**
- Plain text only (no HTML)
- No links in first email
- No images
- No spammy words (FREE, 50%, etc.)
- Personalize beyond just {{first_name}}

**Technical:**
- Verify all emails before sending
- Send consistently (no sudden volume spikes)
- Have spare warmed domains ready
- Maintain DNC list
- Turn off bad campaigns immediately

### Benchmarks

- **Open rate:** 50-80% (below 35% = problem)
- **Positive response:** ~1 per 300 leads

---

## 6. Campaign Segmentation

Create 6-10 campaigns based on signal combinations:

| Segment | Message Angle |
|---------|---------------|
| First-time founder + technical | "Founder-to-founder, I know you're focused on product..." |
| Recently raised + hiring sales | "Congrats on the raise. Scaling sales is next..." |
| VP Sales + hiring SDRs | "Saw you're hiring SDRs. What if you could..." |
| Uses competitor tool | "Noticed you're using X. Customers switch because..." |

**Each segment gets different:**
- Opening line (personalized to their situation)
- Value prop emphasis
- Social proof / case study
- CTA

---

## 7. Email Sequence Structure

**Email 1: Initial Outreach**
- Personalized opening (signal-based)
- Value prop
- Soft CTA

**Email 2: Follow-up (Day 3)**
- Different angle or additional value
- Reference email 1

**Email 3: Break-up (Day 7)**
- Final attempt
- "If this isn't relevant, just let me know"

---

## 8. Tools Stack

### Email Maxis Stack
- **Prospecting:** Apollo.io
- **Scraping:** Apify
- **Enrichment:** LeadMagic
- **Workflow:** Clay
- **Sending:** Instantly.ai or Smartlead

### LinkedIn Social Sellers Stack
- **Audience:** Sales Nav
- **Signals:** Common Room
- **Content:** Taplio
- **CRM:** Breakcold
- **Outreach:** lemlist

---

## Key Metrics

| Metric | Target |
|--------|--------|
| Open rate | 50-80% |
| Reply rate | 1-5% |
| Positive reply rate | 0.3-1% |
| Meetings per 1000 leads | 3-10 |
| Bounce rate | <2% |

---

## Anti-Patterns (Don't Do)

- Spray and pray (unpersonalized mass email)
- Sending to unverified emails
- Links in first email
- HTML formatting / images
- Volume spikes (3x overnight)
- Ignoring complaints / spam reports
- Using shared SMTP (Mailchimp, HubSpot for cold)

---

## References

- [Clay B2B Cold Email Deliverability Guide](https://www.clay.com/blog/b2b-cold-email-deliverability)
- [Instantly Cold Email Strategy](https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy)
- [MXToolbox](https://mxtoolbox.com/) - DNS verification
- [Spamhaus TLD Stats](https://www.spamhaus.org/reputation-statistics/cctlds/domains/)

---

## Quick Reference: Prospecting Flow for Sunder

```
Job Boards (hiring signals)  +  Apollo (ICP match)
                    ↓
              Dedup in Clay
                    ↓
         AI Qualify (website, signals)
                    ↓
              Score & Segment
                    ↓
         6-10 Personalized Campaigns
                    ↓
              Send via Instantly
                    ↓
           Track in Obsidian CRM
```
