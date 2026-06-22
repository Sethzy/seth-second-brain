---
type: raw_capture
source_type: pasted
title: "Sunder sync: pipeline-stages.md"
url: "https://google.serper.dev/search"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-4-outreach/references/pipeline-stages.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-4-outreach/references/pipeline-stages.md"
sha256: "281d2d328f9b012dfc613137b19dda4ba8b47b3db5666c98720e27b802db8b18"
duplicate_of: ""
---

# Sunder sync: pipeline-stages.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-4-outreach/references/pipeline-stages.md`

Primary URL: https://google.serper.dev/search

Duplicate of existing source-map entry: `none`

## Capture Text

# Pipeline Stages Reference

Detailed specifications for each stage of the outreach pipeline.

---

## Stage Overview

| Stage | Name | Batch Size | API | Rate Limit | Input | Output |
|-------|------|------------|-----|------------|-------|--------|
| 1 | Website Leadership Scrape | 1 | Gemini + Search | 0.15s | Company domain | Contacts JSON |
| 2 | Leadership Search | 1 | Serper + Gemini | 0.15s | All companies | Contacts JSON |
| — | Dedupe | — | Local | instant | Stage 1+2 results | Deduped contacts |
| 4 | Decision Maker Validation | 10 | Gemini (no search) | 0.15s | All contacts | CURRENT/USEFUL flags |
| — | **CLAY BREAKPOINT** | — | Manual | — | Validated contacts | Work Email + research columns |
| 6 | Email Generation | 5 | Gemini (no search) | 0.15s | Clay CSV + Template | 3 emails JSON |

**Deprecated/Removed Stages:**
- ~~Stage 3 (LinkedIn URL Search)~~ - LinkedIn URLs now found in Stage 1/2
- ~~Stage 5 (Hook Research)~~ - Clay now handles all company research via Claygent prompts
- ~~Stage 7 (Subject Line)~~ - Subject lines now generated inline in Stage 6

---

## Phase 1: Find People

### Stage 1: Website Leadership Scraping

**Purpose:** Find decision makers from company websites.

**Input:**
- Each company with a valid `domain`
- Process one at a time (not batched)

**Process:**
```
1. Build search query: site:{domain} leadership team executives
2. Call Gemini with search grounding
3. Parse leadership_found array
4. For each person found:
   a. Check if already in TAM-People.csv (by name + domain)
   b. If new, append row to People CSV
5. Update company progress in session state
```

**Output:**
- New rows in TAM-People.csv
- Session state updated with contacts found

**People CSV columns for new rows:**
| Column | Source |
|--------|--------|
| `Full Name` | Gemini response |
| `Company Domain` | Company domain |
| `Company Name` | Company name |
| `Job Title` | Gemini response |
| `LinkedIn Profile` | Gemini (if found) |
| `role_category` | founder/ceo/cfo/coo/director/manager |
| `source` | "website_scrape" |
| `found_date` | Today's date |

**Data flow:**
```
TAM-Companies.csv (each company)
    ↓ (Gemini website search)
Parse leadership
    ↓ (dedupe against existing)
Append to TAM-People.csv
```

---

### Stage 2: Leadership Search (Serper + Gemini)

**Purpose:** Find additional decision makers via Google search. **Always runs** to supplement website scraping.

**Input:**
- All companies in batch
- Process one at a time

**Process:**
```
1. Build Serper search query:
   "{company_name}" {location} founder OR CEO OR CFO OR director OR manager
2. Call Serper API → get search results
3. Pass results to Gemini for analysis:
   - Extract people with decision maker titles
   - Parse: name, title, role_category, source_url
4. For each person found:
   a. Check if already in TAM-People.csv (dedupe by name + company)
   b. Skip if matches excluded_titles from industry_config
   c. Append to People CSV if new
```

**Serper API call:**
```bash
curl -X POST 'https://google.serper.dev/search' \
  -H 'X-API-KEY: $SERPER_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "q": "\"AFIC Logistics\" Singapore founder OR CEO OR CFO OR director",
    "num": 10
  }'
```

**Rate limit:** 2s between Serper calls, 3s between Gemini calls
**Monthly limit:** 2500 Serper searches

**Output:**
- New rows in TAM-People.csv
- `source` = "serper_search"
- Deduped against existing contacts from Stage 1

---

### Dedupe Step (between Stage 2 and Stage 3)

**Purpose:** Deduplicate all found contacts before enriching with LinkedIn URLs.

**Input:**
- All contacts found in Stage 1 (website scrape)
- All contacts found in Stage 2 (Serper search)
- Existing TAM-People.csv

**Dedupe Key:**
```python
def dedupe_key(contact):
    name = contact['Full Name'].lower().strip()
    company = contact['Company Name'].lower().strip()
    return f"{name}|{company}"
```

**Process:**
```
1. Load existing TAM-People.csv
2. Build set of existing keys
3. Collect all Stage 1 + Stage 2 contacts
4. For each contact:
   a. Generate dedupe key
   b. Skip if key exists in TAM-People.csv
   c. Skip if key already seen in this batch
   d. Otherwise, add to deduped list
5. Append deduped contacts to TAM-People.csv
6. Report stats
```

**Implementation:**
```python
def dedupe_and_append(new_contacts, people_csv_path):
    # Load existing
    existing = load_csv(people_csv_path)
    existing_keys = {dedupe_key(c) for c in existing}

    # Dedupe new contacts
    seen_keys = set()
    deduped = []
    duplicates_across_stages = 0
    duplicates_existing = 0

    for contact in new_contacts:
        key = dedupe_key(contact)

        if key in existing_keys:
            duplicates_existing += 1
        elif key in seen_keys:
            duplicates_across_stages += 1
        else:
            deduped.append(contact)
            seen_keys.add(key)

    # Append to CSV
    append_to_csv(people_csv_path, deduped)

    return {
        'total_found': len(new_contacts),
        'duplicates_across_stages': duplicates_across_stages,
        'duplicates_existing': duplicates_existing,
        'new_added': len(deduped)
    }
```

**Output:**
- New contacts appended to TAM-People.csv
- Stats for reporting

---

### Stage 3: LinkedIn URL Search (DEPRECATED)

> **DEPRECATED:** LinkedIn URLs are now found in Stage 1/2 via Gemini search grounding. This stage no longer runs.

**Purpose:** Find LinkedIn profiles for contacts without them.

**Input:**
- All contacts in TAM-People.csv (existing + newly added) where `LinkedIn Profile` is empty
- Batch into groups of 10

**Process:**
```
1. Select contacts without LinkedIn URLs
2. Batch 10 contacts
3. Call Gemini with search: "{name}" "{company}" site:linkedin.com/in
4. Parse results with confidence scores
5. Only update if confidence = high or medium
```

**Output:**
- TAM-People.csv `LinkedIn Profile` column updated

**Confidence handling:**
| Confidence | Action |
|------------|--------|
| high | Update LinkedIn Profile |
| medium | Update LinkedIn Profile, flag for review |
| low | Do not update |
| not_found | Leave blank |

---

### Stage 4: Decision Maker Validation

**Purpose:** Validate contacts BEFORE Clay to avoid paying for bad leads.

**Input:**
- All contacts found in Stages 1-3
- Batch into groups of 10

**Process:**
```
1. For each batch, build validation prompt
2. Inject industry_config:
   - decision_maker_titles
   - excluded_titles
3. Call Gemini (no search needed)
4. Parse CURRENT and USEFUL for each contact
5. Update People CSV
```

**Validation logic:**
```
CURRENT = YES by default
CURRENT = NO only if explicit evidence they left

USEFUL = YES if job_title matches any decision_maker_titles
USEFUL = NO if job_title matches any excluded_titles
USEFUL = MAYBE if title unclear
```

**Output columns:**
| Column | Values |
|--------|--------|
| `dm_current` | YES, NO |
| `dm_current_reason` | Text explanation |
| `dm_useful` | YES, NO, MAYBE |
| `dm_useful_reason` | Text explanation |
| `dm_validated_date` | Today's date |

**Only contacts with CURRENT=YES and USEFUL=YES/MAYBE proceed to Clay export.**

---

## Clay Breakpoint

**Purpose:** Email discovery via Clay waterfall (Prospeo, Hunter, etc.)

**This is a manual step AFTER validation, BEFORE email domain validation.**

### Export Process

After Stage 4 completes:

```
1. Query TAM-People.csv for validated contacts (dm_current=YES, dm_useful=YES/MAYBE)
2. Join with TAM-Companies.csv for company data
3. Export to: {vertical}/clay-export.csv
```

**Export columns (exact match to Clay table):**
| Column | Source |
|--------|--------|
| `Full Name` | TAM-People.csv |
| `Company Domain` | TAM-Companies.csv |
| `Company Name` | TAM-Companies.csv |
| `Person Profile URL` | TAM-People.csv `LinkedIn Profile` |
| `Company Linkedin Profile URL` | TAM-Companies.csv |

**Note:** `Personal Email` and `Work Email` are Clay outputs, not inputs.

### User Actions

1. Import `clay-export.csv` into Clay table
2. Run email waterfall enrichment (Prospeo → Hunter → Apollo)
3. Export with `Work Email` column
4. Update TAM-People.csv with the `Work Email` column

### Import Verification

When user says "continue":

```
1. Read TAM-People.csv
2. Check for Work Email column populated
3. Count contacts with emails found
4. Report stats and continue to Phase 2
```

**Post-import stats:**
```
CLAY IMPORT VERIFIED
════════════════════

Contacts validated: 18
Contacts with email found: 16/18 (89%)

Continuing to Phase 2: Email Validation
```

---

## Phase 2: Copy Generation

### Stage 5: Hook Research (DEPRECATED)

> **DEPRECATED:** Clay now handles all company research via Claygent prompts. See `references/clay-company-research-prompts.md` for the 6 modular prompts that run in Clay.

**Purpose:** Find personalization signals for each company.

**Input:**
- Companies with at least 1 validated contact (dm_current=YES, dm_useful=YES)
- Batch into groups of 5

**Process:**
```
1. Build research prompt with industry_config.search_terms
2. Call Gemini with search grounding
3. Parse signals for each company:
   - hiring (roles, dates)
   - news (headlines, dates)
   - clients (types, named)
   - technology (TMS, carriers)
   - contact_research (posts, education)
4. Store signals in session state
```

**Signal priority for hooks:**
| Priority | Signal Type | Strength |
|----------|-------------|----------|
| 1 | Alumni match | +++++ |
| 2 | Referral/mutual | +++++ |
| 3 | Event spoke at | ++++ |
| 4 | Awards | ++++ |
| 5 | Hiring | +++ |
| 6 | News/expansion | +++ |
| 7 | Fallback | + |

**Output:**
- Session state updated with signals per company
- `best_signal_for_hook` determined

---

### Stage 6: Email Generation

**Purpose:** Generate email body using template and signals.

**Input:**
- Companies with signals from Stage 5
- Loaded template
- Batch into groups of 5

**Process:**
```
1. Load template
2. Build generation prompt with:
   - Template content
   - Signals JSON
   - Best signal recommendation
3. Call Gemini (no search)
4. Parse generated variables:
   - PERSONALIZATION_HOOK
   - AI_SPECIFICITY_LINE
   - CUSTOM_PS
   - full_email_body
```

**Template variables:**
| Variable | Source |
|----------|--------|
| `{{first_name}}` | People CSV |
| `{{job_title}}` | People CSV |
| `{{company_name}}` | Companies CSV |
| `{{PERSONALIZATION_HOOK}}` | Stage 6 generation |
| `{{AI_SPECIFICITY_LINE}}` | Stage 6 generation |
| `{{CUSTOM_PS}}` | Stage 6 generation |

**Output:**
- Generated emails stored in session state
- Ready for subject line + review

---

### Stage 7: Subject Line Selection (DEPRECATED)

> **DEPRECATED:** Subject lines are now generated inline in Stage 6 as part of the 3-email sequence. Each email gets its subject from the Campaign Template.

**Purpose:** Select appropriate subject line (rule-based, not AI).

**Input:**
- Signals from Stage 6
- Template type

**Process:**
```python
def select_subject_line(signals, template_type):
    # Priority 1: Personal connection
    if signals.get('referral'):
        return f"{signals['referral_name']} suggested I reach out"

    if signals.get('alumni'):
        return f"Fellow {signals['school']} alum - quick question"

    # Priority 2: Template-specific
    if template_type == 'expert_interview':
        return "Re: Could you sanity-check our startup's thesis?"

    # Priority 3: Signal-based
    if signals.get('hiring'):
        return f"Quick question about your {signals['hiring_role']} search"

    if signals.get('news'):
        return f"Congrats on {signals['news_short']} - quick question"

    # Fallback
    return "Quick question about your process"
```

See `references/subject-line-formulas.md` for complete rules.

**Output:**
- Subject line attached to each email

---

## Data Flow Summary

```
TAM-Companies.csv ──────────────────────────────────────────────┐
       │                                                        │
       ├─ Stage 1 (Website) ─→ contacts (in memory)             │
       │                              │                         │
       ├─ Stage 2 (Serper) ──→ contacts (in memory)             │
       │                              │                         │
       │                              ▼                         │
       │                    ┌─────────────────────┐             │
       │                    │      DEDUPE         │             │
       │                    │ • vs each other     │             │
       │                    │ • vs TAM-People.csv │             │
       │                    └──────────┬──────────┘             │
       │                               │                        │
       │                               ▼                        │
       │                    Append new → TAM-People.csv         │
       │                               │                        │
       │                               ▼                        │
       │                    Stage 3 (LinkedIn URLs) ────────────┤
       │                               │                        │
       │                               ▼                        │
       │                    Stage 4 (Validation) ───────────────┤
       │                               │                        │
       │                               │ (CURRENT=YES, USEFUL=YES/MAYBE)
       │                               ▼                        │
       │                    ┌─────────────────────┐             │
       │                    │   CLAY BREAKPOINT   │             │
       │                    │   (validated only)  │             │
       │                    └──────────┬──────────┘             │
       │                               │                        │
       │                               ▼                        │
       │                    TAM-People.csv + Work Email         │
       │                               │                        │
       └───────────────────────────────┼────────────────────────┘
                                       │
Session State (signals, emails) ◄──────┘
       │
       ├─ Stage 5 ─→ signals JSON
       │
       ├─ Stage 6 ─→ generated emails
       │
       └─ Stage 7 ─→ subject lines
                        │
       ┌────────────────┘
       │
Phase 3 (Review) ──→ Approve ──→ Update TAM-Companies.csv
                               (outreach_status, outreach_history)
```

---

## Batch Processing Implementation

```python
class PipelineProcessor:
    def __init__(self, session_config):
        self.config = session_config
        self.industry_config = session_config['industry_config']
        self.serper_calls_this_month = 0
        self.serper_monthly_limit = 2500
        self.people_csv_path = session_config['people_csv_path']

    def dedupe_key(self, contact):
        """Generate dedupe key from contact."""
        name = contact['Full Name'].lower().strip()
        company = contact['Company Name'].lower().strip()
        return f"{name}|{company}"

    def run_phase_1(self, companies):
        """Find & Validate People phase."""
        new_contacts = []

        # Stage 1: Website scraping (per company)
        for company in companies:
            found = self.run_stage_1_website_scrape(company)
            for c in found:
                c['source'] = 'website'
            new_contacts.extend(found)
            time.sleep(3)

        # Stage 2: Leadership Search via Serper + Gemini (per company)
        for company in companies:
            if self.serper_calls_this_month >= self.serper_monthly_limit:
                print("Serper monthly limit reached, skipping Stage 2")
                break
            found = self.run_stage_2_serper_search(company)
            for c in found:
                c['source'] = 'serper'
            new_contacts.extend(found)
            self.serper_calls_this_month += 1
            time.sleep(5)  # 2s Serper + 3s Gemini

        # DEDUPE: against each other + existing CSV
        dedupe_stats = self.dedupe_and_append(new_contacts)
        print(f"Dedupe: {dedupe_stats}")

        # Stage 3: LinkedIn URL search (batch 10)
        contacts = self.get_contacts_without_linkedin()
        self.run_stage_3_linkedin_urls(contacts)

        # Stage 4: Decision Maker Validation (batch 10)
        all_contacts = self.get_all_contacts()
        self.run_stage_4_dm_validation(all_contacts)

        # Export only validated contacts for Clay
        validated = self.get_validated_contacts()
        self.export_for_clay(validated)
        return "CLAY_BREAKPOINT"

    def dedupe_and_append(self, new_contacts):
        """Dedupe new contacts against each other and existing CSV."""
        existing = load_csv(self.people_csv_path)
        existing_keys = {self.dedupe_key(c) for c in existing}

        seen_keys = set()
        deduped = []
        stats = {
            'stage_1_found': len([c for c in new_contacts if c.get('source') == 'website']),
            'stage_2_found': len([c for c in new_contacts if c.get('source') == 'serper']),
            'duplicates_across_stages': 0,
            'duplicates_existing': 0,
            'new_added': 0
        }

        for contact in new_contacts:
            key = self.dedupe_key(contact)
            if key in existing_keys:
                stats['duplicates_existing'] += 1
            elif key in seen_keys:
                stats['duplicates_across_stages'] += 1
            else:
                deduped.append(contact)
                seen_keys.add(key)

        append_to_csv(self.people_csv_path, deduped)
        stats['new_added'] = len(deduped)
        return stats

    def run_phase_2(self, companies):
        """Copy generation phase - after Clay import."""
        # Stage 5: Hook research (batch 5)
        self.run_stage_5(companies)

        # Stage 6: Email generation (batch 5)
        self.run_stage_6(companies)

        # Stage 7: Subject lines (rule-based, instant)
        self.run_stage_7(companies)
```

---

## Progress Tracking

Update session state after each stage:

```yaml
progress:
  phase: 1
  stage: 4

  phase_1:
    stage_1_website:
      status: complete
      processed: 10
      contacts_found: 18
    stage_2_serper:
      status: complete
      processed: 10
      contacts_found: 12
      serper_calls_used: 10
    dedupe:
      status: complete
      total_found: 30
      duplicates_across_stages: 5
      duplicates_existing: 3
      new_added: 22
    stage_3_linkedin_urls:
      status: complete
      processed: 22
      linkedin_found: 18
    stage_4_validation:
      status: complete
      processed: 30
      dm_current_yes: 28
      dm_useful_yes: 22
      dm_useful_maybe: 2
      dm_skipped: 6
    clay:
      exported: true
      export_path: "FreightForwarders/clay-export.csv"
      exported_count: 24  # only validated contacts
      imported: false

  phase_2:
    stage_5:
      status: pending
    stage_6:
      status: pending
    stage_7:
      status: pending
```

---

## Timing Estimates

### Stage Timing

| Stage | Items | Batch Size | Delay | Est. Time |
|-------|-------|------------|-------|-----------|
| Stage 1 (Website) | 10 companies | 1 | 3s | 30s |
| Stage 2 (Serper) | 10 companies | 1 | 5s (2+3) | 50s |
| Stage 3 (LinkedIn URLs) | 30 contacts | 10 | 3s | 9s |
| Stage 4 (Validation) | 30 contacts | 10 | 3s | 9s |
| — | Clay | — | manual | 5-10 min |
| Stage 5 (Hook Research) | 10 companies | 5 | 3s | 6s |
| Stage 6 (Email Gen) | 10 companies | 5 | 3s | 6s |
| Stage 7 (Subject) | 10 companies | N/A | instant | 0s |

**Phase 1 (before Clay): ~98 seconds** for 10 companies
**Phase 2 (after Clay): ~12 seconds**
**Total (excluding Clay): ~110 seconds**
