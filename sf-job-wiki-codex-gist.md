# Codex Build Prompt: Simple SF Job Wiki Automation

You are Codex. Build a new repo from scratch for a non-technical user who is applying for jobs in San Francisco.

The user should not need to debug anything. If a source breaks, the system should log the failure clearly and continue with the other source. Do not ask the user to inspect selectors, cookies, API responses, browser sessions, or cron manually.

## What To Build

Build a stupid-simple daily job-search wiki.

Sources:

1. LinkedIn Jobs, using `python-jobspy`.
2. YC Jobs, using the public `https://www.ycombinator.com/jobs` page.

Do not add:

- Direct ATS APIs.
- General web search.
- Remote US jobs.
- Auto-apply.
- Outreach automation.
- LinkedIn login, cookies, messages, or browser-cookie hacks.

The output should be local files:

- raw JSONL evidence
- SQLite database
- Markdown wiki
- one daily Markdown brief

## Spike Results To Trust

These source tests were run on 2026-06-22.

LinkedIn via JobSpy worked anonymously:

- Query: `fintech AI`
- Location: `San Francisco, CA`
- Returned 15 rows.
- After filtering out Remote and requiring San Francisco / Bay Area terms:
  - 10 clean Bay Area jobs
  - 5 manual-review jobs with missing location
  - 0 remote rejects in that sample
- Sample rows included Airwallex, Santander, Samsung Next, Hopper, Stripe, Chime, Plaid.

YC public jobs page worked:

- URL: `https://www.ycombinator.com/jobs`
- Plain `requests` returned status 200 and public HTML.
- The page embedded structured `jobPostings` data.
- Parsed 20 unique public jobs from the page.
- After filtering out Remote and requiring San Francisco / Bay Area terms:
  - 3 clean Bay Area jobs
- Sample rows included Shef, Candid Health, Short Story.

Do not use `ycombinator-scraper` as the default. In the spike, the package failed on missing dependency metadata and then required login credentials. The public YC page parser is simpler and better for a non-technical user.

## Interview The User First

Before coding, ask the user these questions. Ask them in a compact way. If the user says "use defaults", proceed with the defaults below.

Questions:

1. What role families should we target?
2. What seniority levels should we include or exclude?
3. Which Bay Area locations count?
4. Which fintech themes matter most?
5. Which AI themes matter most?
6. Which companies should always be watched?
7. Which companies should be blocked?
8. Which keywords should be required?
9. Which keywords should be blocked?
10. Should missing-location LinkedIn jobs go to manual review? Default: yes.

Defaults:

```yaml
target_locations:
  - San Francisco
  - South San Francisco
  - Oakland
  - Berkeley
  - Palo Alto
  - Menlo Park
  - Redwood City
  - San Mateo
  - Mountain View
  - Sunnyvale
  - Santa Clara
  - San Jose
  - Bay Area

exclude_remote: true
manual_review_missing_location: true

target_themes:
  fintech:
    - fintech
    - payments
    - banking
    - finance
    - lending
    - risk
    - fraud
    - compliance
    - treasury
    - accounting
    - insurance
    - crypto
    - trading
  ai:
    - AI
    - artificial intelligence
    - machine learning
    - ML
    - LLM
    - agents
    - automation
    - data scientist
    - analytics

default_search_queries:
  - fintech AI
  - AI product manager fintech
  - fintech operations AI
  - go to market fintech AI
  - customer success fintech AI
  - business operations fintech startup
  - data scientist fintech AI
  - machine learning fintech
```

## Repo Structure

Create this structure:

```text
.
├── README.md
├── AGENTS.md
├── requirements.txt
├── config/
│   └── profile.yaml
├── data/
│   └── jobs.sqlite
├── raw/
│   └── .gitkeep
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── daily/
│   │   └── .gitkeep
│   └── companies/
│       └── .gitkeep
├── logs/
│   └── .gitkeep
├── scripts/
│   ├── daily.py
│   ├── fetch_linkedin.py
│   ├── fetch_yc.py
│   ├── normalize.py
│   ├── score.py
│   ├── storage.py
│   ├── write_wiki.py
│   └── install_cron.sh
├── tests/
│   ├── test_normalize.py
│   ├── test_score.py
│   └── test_dedupe.py
└── .github/
    └── workflows/
        └── daily.yml
```

## Requirements

Use Python 3.11.

`requirements.txt`:

```text
python-jobspy
requests
beautifulsoup4
pandas
pyyaml
python-dotenv
pytest
```

Do not include `ycombinator-scraper` in v1.

## Data Model

Normalize every job into this schema:

```yaml
id:
source:
source_url:
apply_url:
company:
company_url:
title:
location:
salary:
posted_at:
scraped_at:
description:
tags:
match_score:
score_reasons:
status:
raw:
```

Allowed `status` values:

- `new`
- `interesting`
- `manual_review`
- `applied`
- `interviewing`
- `rejected`
- `ignored`

SQLite table:

```sql
CREATE TABLE IF NOT EXISTS jobs (
  id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  source_url TEXT,
  apply_url TEXT,
  company TEXT,
  company_url TEXT,
  title TEXT,
  location TEXT,
  salary TEXT,
  posted_at TEXT,
  scraped_at TEXT NOT NULL,
  description TEXT,
  tags TEXT,
  match_score INTEGER,
  score_reasons TEXT,
  status TEXT NOT NULL DEFAULT 'new',
  raw_json TEXT NOT NULL,
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL
);
```

Dedupe:

1. If `apply_url` or `source_url` matches an existing job, it is the same job.
2. Else use lowercase `source + company + title + location`.

## LinkedIn Fetcher

Implement `scripts/fetch_linkedin.py` with JobSpy.

Use this exact shape:

```python
from jobspy import scrape_jobs

def fetch_linkedin_jobs(query: str, location: str, results_wanted: int = 50):
    return scrape_jobs(
        site_name=["linkedin"],
        search_term=query,
        location=location,
        results_wanted=results_wanted,
        hours_old=168,
        linkedin_fetch_description=False,
    )
```

Run all configured search queries. Save raw rows to:

```text
raw/YYYY-MM-DD/linkedin.jsonl
```

Each line must be one JSON object.

LinkedIn failure behavior:

- Catch exceptions per query.
- Log the query and error to `logs/daily.log`.
- Continue to the next query.
- If all LinkedIn queries fail, continue to YC.

LinkedIn guardrails:

- Do not log into LinkedIn.
- Do not use cookies.
- Do not message people.
- Do not apply to jobs.
- Do not scrape profiles.
- Do not try to bypass account limits.

## YC Fetcher

Implement `scripts/fetch_yc.py` with `requests`, `html`, `json`, and `BeautifulSoup` only.

Use:

```text
https://www.ycombinator.com/jobs
```

The page embeds JSON-like job data in escaped HTML under `jobPostings`. Do not rely on the visual card layout.

Implementation approach:

1. Fetch the page with a normal browser-like User-Agent.
2. Decode HTML entities with `html.unescape`.
3. Find every `"jobPostings":[...]` array.
4. Parse each array with JSON.
5. Deduplicate by YC job `id`.
6. Normalize fields.

Use this parser shape:

```python
import html
import json
import requests
from urllib.parse import urljoin

YC_JOBS_URL = "https://www.ycombinator.com/jobs"

def extract_json_arrays(text: str, key: str = '"jobPostings":'):
    arrays = []
    pos = 0
    while True:
        i = text.find(key, pos)
        if i == -1:
            break
        start = text.find("[", i + len(key))
        if start == -1:
            break

        depth = 0
        in_str = False
        esc = False
        for j in range(start, len(text)):
            ch = text[j]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            else:
                if ch == '"':
                    in_str = True
                elif ch == "[":
                    depth += 1
                elif ch == "]":
                    depth -= 1
                    if depth == 0:
                        arrays.append(json.loads(text[start:j + 1]))
                        pos = j + 1
                        break
        else:
            break
    return arrays

def fetch_yc_jobs():
    res = requests.get(
        YC_JOBS_URL,
        headers={"User-Agent": "Mozilla/5.0 job-wiki/1.0"},
        timeout=20,
    )
    res.raise_for_status()
    decoded = html.unescape(res.text)

    jobs = []
    for arr in extract_json_arrays(decoded):
        jobs.extend(arr)

    seen = set()
    unique = []
    for job in jobs:
        job_id = str(job.get("id") or "")
        if not job_id or job_id in seen:
            continue
        seen.add(job_id)
        unique.append(job)
    return unique
```

Normalize YC fields:

```python
{
  "id": f"yc:{job['id']}",
  "source": "yc",
  "source_url": urljoin("https://www.ycombinator.com", job.get("url") or ""),
  "apply_url": job.get("applyUrl") or job.get("ctaUrl") or "",
  "company": job.get("companyName") or "",
  "company_url": urljoin("https://www.ycombinator.com", job.get("companyUrl") or ""),
  "title": job.get("title") or "",
  "location": job.get("location") or "",
  "salary": job.get("salaryRange") or "",
  "posted_at": job.get("createdAt") or "",
  "description": job.get("companyOneLiner") or "",
  "tags": [job.get("prettyRole"), job.get("roleSpecificType"), *job.get("skills", [])],
  "raw": job,
}
```

Save raw rows to:

```text
raw/YYYY-MM-DD/yc.jsonl
```

YC failure behavior:

- If fetch or parse fails, log it to `logs/daily.log`.
- Continue with LinkedIn results if LinkedIn worked.
- Do not require YC login.
- Do not use `workatastartup.com` directly in v1, because it returned 406 in the spike.

## Location Filter

No Remote US.

Implement strict location bucketing:

```python
BAY_AREA_TERMS = [
    "san francisco",
    "south san francisco",
    "oakland",
    "berkeley",
    "palo alto",
    "menlo park",
    "redwood city",
    "san mateo",
    "mountain view",
    "sunnyvale",
    "santa clara",
    "san jose",
    "bay area",
]

def location_bucket(title: str, location: str, is_remote=None) -> str:
    text = f"{title or ''} {location or ''}".lower()
    if is_remote is True or "remote" in text:
        return "reject_remote"
    if any(term in text for term in BAY_AREA_TERMS):
        return "keep_bay_area"
    if not (location or "").strip():
        return "manual_review_missing_location"
    return "reject_location"
```

Rules:

- Keep `keep_bay_area`.
- Put `manual_review_missing_location` in the daily brief, but do not count it as a top match.
- Reject `reject_remote`.
- Reject `reject_location`.

## Scoring

Score kept jobs from 0 to 100.

Default scoring:

- +25 fintech match
- +25 AI match
- +20 role match
- +15 location match
- +10 seniority match
- +5 freshness

Penalties:

- -50 remote
- -30 wrong location
- -25 blocked company
- -20 blocked keyword
- -15 internship if not requested
- -10 missing location

Every scored job must include `score_reasons`, for example:

```text
Matches fintech keyword "payments"; matches AI keyword "machine learning"; location is San Francisco; role family matches product.
```

## Daily Pipeline

Implement `scripts/daily.py`.

Steps:

1. Load `config/profile.yaml`.
2. Create date folder under `raw/YYYY-MM-DD/`.
3. Fetch LinkedIn jobs for each query.
4. Fetch YC jobs from `https://www.ycombinator.com/jobs`.
5. Save raw JSONL for each source.
6. Normalize all jobs.
7. Apply location filter.
8. Dedupe.
9. Score kept jobs.
10. Upsert into SQLite.
11. Write daily wiki brief.
12. Update `wiki/index.md`.
13. Append `wiki/log.md`.
14. Exit successfully if at least one source worked.
15. Exit with failure only if both LinkedIn and YC fail.

## Daily Brief Format

Write:

```text
wiki/daily/YYYY-MM-DD.md
```

Format:

```md
# Daily Job Brief: YYYY-MM-DD

## Source Health

| Source | Status | Rows | Notes |
|---|---:|---:|---|
| LinkedIn | OK/FAILED | N | ... |
| YC | OK/FAILED | N | ... |

## Top Matches

| Score | Company | Role | Location | Source | Why | Link |
|---:|---|---|---|---|---|---|

## Best Fintech + AI Matches

| Score | Company | Role | Why | Link |
|---:|---|---|---|---|

## Manual Review

Jobs that may be relevant but have missing or ambiguous location.

| Company | Role | Location | Reason | Link |
|---|---|---|---|---|

## Rejected

Summarize counts only:

- Remote: N
- Wrong location: N
- Blocked company: N
- Blocked keyword: N

## Next Actions

- Review the top 10.
- Mark statuses manually in the wiki or SQLite.
- Apply manually. No auto-apply.
```

## Wiki Index

Write `wiki/index.md`:

```md
# Job Wiki Index

## Current Profile

- Location: San Francisco / Bay Area only
- Remote US: excluded
- Sources: LinkedIn, YC
- Themes: fintech, AI

## Daily Briefs

| Date | Top Match Count | Manual Review Count | Sources |
|---|---:|---:|---|

## Companies

| Company | Best Score | Roles Seen | Last Seen |
|---|---:|---:|---|
```

## Company Pages

For companies with score >= 70, write or update:

```text
wiki/companies/<company-slug>.md
```

Format:

```md
# Company Name

## Why It Matches

- ...

## Jobs Seen

| Date | Score | Role | Location | Source | Link |
|---|---:|---|---|---|---|

## Notes

Manual notes go here.
```

## Cron / Automation

Create GitHub Actions schedule:

```yaml
name: Daily Job Wiki

on:
  schedule:
    - cron: "17 15 * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python scripts/daily.py
      - run: |
          git config user.name "job-wiki-bot"
          git config user.email "job-wiki-bot@example.com"
          git add raw data wiki logs
          git commit -m "Daily job wiki update" || echo "No changes"
          git push
```

Note: GitHub Actions cron is UTC. `17 15 * * *` is 7:17 AM Pacific during daylight saving time and 8:17 AM Pacific during standard time. That is fine for v1.

Also create `scripts/install_cron.sh` for local fallback:

```bash
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="${PYTHON:-python3}"
LOG="$ROOT/logs/daily.log"
mkdir -p "$ROOT/logs"

CRON_LINE="17 7 * * * cd \"$ROOT\" && $PYTHON scripts/daily.py >> \"$LOG\" 2>&1"

(crontab -l 2>/dev/null | grep -v "scripts/daily.py" || true; echo "$CRON_LINE") | crontab -

echo "Installed daily local cron:"
echo "$CRON_LINE"
```

The README should explain both options:

1. GitHub Actions, recommended if the repo is on GitHub.
2. Local cron, fallback if LinkedIn scraping is flaky on GitHub runners.

## README Requirements

The README must be dummy-proof:

```md
# SF Job Wiki

## Setup

1. Install Python 3.11.
2. Run `python -m venv .venv`.
3. Run `source .venv/bin/activate`.
4. Run `pip install -r requirements.txt`.
5. Edit `config/profile.yaml`.
6. Run `python scripts/daily.py`.
7. Open `wiki/index.md`.

## Daily Automation

Use GitHub Actions if this repo is on GitHub.
Use `scripts/install_cron.sh` if running locally.

## Safety

This tool never applies to jobs.
This tool never logs into LinkedIn.
This tool never messages anyone.
This tool excludes Remote US jobs by default.
```

## Tests

Add tests for:

1. Location bucketing excludes Remote.
2. Location bucketing keeps San Francisco and Bay Area.
3. Missing LinkedIn location becomes manual review.
4. Dedupe collapses same URL.
5. Scoring rewards fintech + AI.
6. YC embedded `jobPostings` parser can parse a fixture.

## Definition Of Done

The project is done when:

- `python scripts/daily.py` runs end-to-end.
- LinkedIn via JobSpy returns rows or logs a clean source failure.
- YC public page parser returns rows or logs a clean source failure.
- Remote jobs are excluded.
- Missing-location LinkedIn jobs go to manual review.
- Raw JSONL files are written.
- SQLite is populated.
- `wiki/index.md` exists.
- `wiki/daily/YYYY-MM-DD.md` exists.
- GitHub Actions cron exists.
- Local cron installer exists.
- Tests pass.
- README is clear enough for a non-technical user.

Do not stop at a plan. Implement the repo, run the tests, run one real daily scrape, and show the generated `wiki/daily/YYYY-MM-DD.md`.
