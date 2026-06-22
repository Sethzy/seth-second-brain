---
type: raw_capture
source_type: pasted
title: "Sunder sync: gemini-prompts.md"
url: "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-4-outreach/references/gemini-prompts.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-4-outreach/references/gemini-prompts.md"
sha256: "b20fc42507edd3de05e96c78cf543d470c1c2e4f63b841b36215180d15d8fa0b"
duplicate_of: ""
---

# Sunder sync: gemini-prompts.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-4-outreach/references/gemini-prompts.md`

Primary URL: https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent

Duplicate of existing source-map entry: `none`

## Capture Text

# Gemini Prompts Reference

All prompt templates for the 7-stage pipeline. Uses `{{industry_config}}` variables for industry-agnostic operation.

> **⚠️ NEVER use Claude WebFetch. Always use Gemini API or Serper API.**

---

## API Configuration

**First, load API keys:**
```bash
source "/Users/sethlim/Documents/Sunder Workspace/.env"
```

**Required keys:**
- `GEMINI_API_KEY` - for all Gemini calls
- `SERPER_API_KEY` - for Stage 2 leadership search

```bash
source "/Users/sethlim/Documents/Sunder Workspace/.env"

# Gemini with search grounding (Stages 1, 3, 5)
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{"parts": [{"text": "[PROMPT]"}]}],
    "tools": [{"google_search": {}}]
  }'

# Gemini without search (Stages 2 analysis, 4, 6)
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{"parts": [{"text": "[PROMPT]"}]}]
  }'

# Serper API (Stage 2 search)
curl -X POST 'https://google.serper.dev/search' \
  -H "X-API-KEY: $SERPER_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"q": "[SEARCH_QUERY]", "num": 10}'
```

---

## Stage 1: Website Leadership Scraping

**Batch size:** 1 (per company)
**Search grounding:** YES

### Prompt

```
Find leadership/executive team members for {{company_name}} ({{domain}}).

Search: site:{{domain}} OR "{{company_name}}" leadership team executives about us management

TITLES WE'RE LOOKING FOR:
{{#each industry_config.search_titles}}
- {{this}}
{{/each}}

For each person found, extract:
- Full name
- Job title (exact as shown)
- Role category (founder/ceo/cfo/coo/director/manager)
- Email address (if visible on page)
- LinkedIn URL (if mentioned)
- Source URL where found

OUTPUT FORMAT (JSON):
{
  "company": "{{company_name}}",
  "domain": "{{domain}}",
  "leadership_found": [
    {
      "full_name": "John Smith",
      "job_title": "Chief Financial Officer",
      "role_category": "cfo",
      "email": "john@company.com",
      "linkedin_url": "https://linkedin.com/in/johnsmith",
      "source_url": "https://company.com/about"
    }
  ],
  "general_contact_email": "info@company.com",
  "search_successful": true,
  "notes": "Found 3 executives on About page"
}

If no decision makers found, set search_successful to false and explain in notes.
```

### JSON Schema

```json
{
  "type": "object",
  "properties": {
    "company": {"type": "string"},
    "domain": {"type": "string"},
    "leadership_found": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "full_name": {"type": "string"},
          "job_title": {"type": "string"},
          "role_category": {"enum": ["founder", "ceo", "cfo", "coo", "director", "manager", "other"]},
          "email": {"type": ["string", "null"]},
          "linkedin_url": {"type": ["string", "null"]},
          "source_url": {"type": "string"}
        },
        "required": ["full_name", "job_title", "role_category"]
      }
    },
    "general_contact_email": {"type": ["string", "null"]},
    "search_successful": {"type": "boolean"},
    "notes": {"type": "string"}
  }
}
```

---

## Stage 2: Leadership Search (Serper + Gemini)

**Batch size:** 1 (per company)
**APIs:** Serper (search) → Gemini (analysis)

### Step 1: Serper Search

Build query from `search_titles` in session config:

```bash
# search_titles = ["founder", "CEO", "CFO", "director", "manager"]
# → "founder OR CEO OR CFO OR director OR manager"

curl -X POST 'https://google.serper.dev/search' \
  -H "X-API-KEY: $SERPER_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "q": "\"{{company_name}}\" {{location}} {{search_titles_as_or_boolean}}",
    "num": 10
  }'
```

Example: `"AFIC Logistics" Singapore founder OR CEO OR CFO OR director OR manager`

### Step 2: Gemini Analysis Prompt

```
Analyze these search results to find decision makers for {{company_name}}.

SEARCH RESULTS:
{{serper_results_json}}

TITLES WE'RE LOOKING FOR:
{{#each industry_config.search_titles}}
- {{this}}
{{/each}}

For each person found in the search results, extract:
- Full name
- Job title (exact as shown)
- Role category (founder/ceo/cfo/coo/director/manager)
- Email address (if visible in search results - rare but capture if found)
- Source URL where found

OUTPUT FORMAT (JSON):
{
  "company": "{{company_name}}",
  "leadership_found": [
    {
      "full_name": "John Smith",
      "job_title": "Chief Financial Officer",
      "role_category": "cfo",
      "email": null,
      "source_url": "https://example.com/article"
    }
  ],
  "search_successful": true,
  "notes": "Found 2 executives from news articles"
}

Only include people you're confident work at this specific company.
```

### JSON Schema

```json
{
  "type": "object",
  "properties": {
    "company": {"type": "string"},
    "leadership_found": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "full_name": {"type": "string"},
          "job_title": {"type": "string"},
          "role_category": {"enum": ["founder", "ceo", "cfo", "coo", "director", "manager", "other"]},
          "email": {"type": ["string", "null"]},
          "source_url": {"type": "string"}
        },
        "required": ["full_name", "job_title", "role_category"]
      }
    },
    "search_successful": {"type": "boolean"},
    "notes": {"type": "string"}
  }
}
```

---

## Stage 3: LinkedIn URL Search

**Batch size:** 10 contacts
**Search grounding:** YES

### Prompt

```
Find LinkedIn profile URLs for these people.

CONTACTS TO FIND:
{{#each contacts}}
{{index}}. {{full_name}} at {{company_name}}
{{/each}}

Search pattern: "{{name}}" "{{company}}" site:linkedin.com/in

For each person, find their LinkedIn profile URL.

OUTPUT FORMAT (JSON):
{
  "results": [
    {
      "full_name": "John Smith",
      "company_name": "AFIC Logistics",
      "linkedin_url": "https://www.linkedin.com/in/john-smith-123456",
      "confidence": "high",
      "match_reason": "Name and company both match"
    }
  ]
}

Confidence levels:
- high: Name and company both match exactly
- medium: Name matches, company is similar/related
- low: Only partial match, may be different person
- not_found: Could not find profile

IMPORTANT: Only return profiles where you're confident it's the right person.
```

### JSON Schema

```json
{
  "type": "object",
  "properties": {
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "full_name": {"type": "string"},
          "company_name": {"type": "string"},
          "linkedin_url": {"type": ["string", "null"]},
          "confidence": {"enum": ["high", "medium", "low", "not_found"]},
          "match_reason": {"type": "string"}
        },
        "required": ["full_name", "company_name", "confidence"]
      }
    }
  }
}
```

---

## Stage 4: Decision Maker Validation

**Batch size:** 10 contacts
**Search grounding:** NO (uses provided data only)

### Prompt

```
Validate these contacts for B2B outreach targeting {{industry_config.name}}.

CONTACTS TO VALIDATE:
{{#each contacts}}
───────────────────────────
PERSON {{index}}:
- Name: {{full_name}}
- Title: {{job_title}}
- Company: {{company_name}}
- LinkedIn: {{linkedin_url}}
- Email: {{work_email}}
{{/each}}

For each person, determine:

1. CURRENT: Are they still at this company?
   - YES: Default if no evidence they left
   - NO: Only if explicit evidence they moved (e.g., LinkedIn shows different company)

2. USEFUL: Does their title match any of these?
   {{#each industry_config.search_titles}}
   - {{this}}
   {{/each}}

   YES = title matches or is similar to one in the list
   NO = title doesn't match (e.g., driver, admin, warehouse)

OUTPUT FORMAT (one line per person):
PERSON 1: CURRENT=YES/NO, USEFUL=YES/NO, CURRENT_REASON=..., USEFUL_REASON=...
PERSON 2: CURRENT=YES/NO, USEFUL=YES/NO, CURRENT_REASON=..., USEFUL_REASON=...

IMPORTANT:
- Default CURRENT=YES unless you have specific evidence they left
- Be strict about USEFUL - must match or be similar to listed titles
- Do NOT invent information - only use what's provided
```

### Output Parsing

Parse line-by-line format into JSON:
```json
{
  "validations": [
    {
      "person_index": 1,
      "full_name": "John Smith",
      "current": "YES",
      "current_reason": "No evidence of job change",
      "useful": "YES",
      "useful_reason": "CFO matches decision_maker_titles"
    }
  ]
}
```

---

## Stage 5: Research (Template-Driven)

**Batch size:** 5 companies
**Search grounding:** YES

> **Template-driven:** Read the selected template's "Research Instructions" section to know what signals to look for.

### Prompt

```
Read the "Research Instructions" section from this template:
"""
{template_content}
"""

Research these companies and find the signals listed above.

COMPANIES TO RESEARCH:
{#each companies}
───────────────────────────
COMPANY {index}: {company_name}
- Domain: {domain}
- Contact: {contact_name} ({contact_title})
{/each}

Output format: Brief bullet points per company, just key facts.
```

### Output Format

```json
{
  "companies": [
    {
      "company_name": "AFIC Logistics",
      "research": {
        "basics": "Ocean + air freight, 2 offices (SG, MY), ~50 employees",
        "signals": "Hiring billing clerk, uses CargoWise, works with Maersk/MSC",
        "contact": "CFO since 2024, NUS alum"
      }
    }
  ]
}
```

---

## Stage 6: Email Generation (Template-Driven)

**Batch size:** 5 companies
**Search grounding:** NO

> **Template-driven:** Read the selected template's "Email Generation" section for structure, hook tiers, P.S. formulas, and tone.

### Prompt

```
Read the "Email Generation" section from this template:
"""
{template_content}
"""

Generate emails for these contacts using the research below.

CONTACTS:
{#each contacts}
───────────────────────────
COMPANY: {company_name}
CONTACT: {contact_name} ({contact_title})
EMAIL: {contact_email}
RESEARCH: {research_output}
───────────────────────────
{/each}

Follow the template's:
- Hook selection (pick first match from tiers)
- P.S. selection (by company type)
- Tone guidelines

Output: Complete email ready to send for each contact.
```

### Output Format

```json
{
  "emails": [
    {
      "company_name": "AFIC Logistics",
      "contact_name": "Ajay Singh",
      "contact_email": "ajay@aficlogistics.com",
      "subject": "Could you sanity-check our startup's thesis on freight?",
      "body": "[complete email]",
      "hook_used": "NUS alum",
      "ps_used": "ocean freight"
    }
  ]
}
```

---

## Stage 7: Subject Line

**From template.** Subject line is defined in the template's Email Template section.

No separate Gemini call needed.

---

## Error Handling

### Gemini Response Parsing

```python
def parse_gemini_response(response):
    """Extract JSON from Gemini response."""
    try:
        # Try direct JSON parse
        return json.loads(response)
    except:
        # Extract JSON from markdown code block
        match = re.search(r'```(?:json)?\n?(.*?)\n?```', response, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        raise ValueError("No valid JSON in response")
```

### Retry Logic

```python
def call_gemini_with_retry(prompt, max_retries=3):
    """Call Gemini with exponential backoff."""
    delay = 3
    for attempt in range(max_retries):
        try:
            response = call_gemini(prompt)
            return response
        except RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
            else:
                raise
```

---

## Batch Processing Example

```python
def process_stage_4(contacts, industry_config, batch_size=10):
    """Process decision maker validation in batches."""
    results = []

    for i in range(0, len(contacts), batch_size):
        batch = contacts[i:i + batch_size]

        # Build prompt with industry config
        prompt = build_stage_4_prompt(batch, industry_config)

        # Call Gemini
        response = call_gemini_with_retry(prompt)

        # Parse results
        batch_results = parse_validation_response(response)
        results.extend(batch_results)

        # Rate limit
        time.sleep(3)

    return results
```
