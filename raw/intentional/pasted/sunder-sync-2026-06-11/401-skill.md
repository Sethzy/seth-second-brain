---
type: raw_capture
source_type: pasted
title: "Sunder sync: SKILL.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/SKILL.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/SKILL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-instagram-scraper/SKILL.md"
sha256: "3616548887d36fdcfb46f8dfd56b6b0462a090434981b5c63191b83cf9f31d4f"
duplicate_of: ""
---

# Sunder sync: SKILL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/SKILL.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/SKILL.md

Duplicate of existing source-map entry: `none`

## Capture Text

---
name: sales-instagram-scraper
description: Scrape Instagram profiles at scale using Google Search as a proxy via OpenWeb Ninja API. Generates thousands of targeted queries combining role keywords (founder, CEO), US locations, and niche verticals, then bulk-searches Google for site:instagram.com results to extract usernames, bios, and emails. Outputs Clay-ready CSV. Use when user says "instagram scraper", "scrape instagram", "instagram leads", "find instagram profiles", or wants to build a prospect list from Instagram bios.
---

# Instagram Profile Scraper via Google Search

## Execution

**Announce at start:** "I'm executing the instagram-scraper skill to find Instagram profiles via Google Search."

**Output location:** `02_Areas/Sales/Scraped Data/instagram/` — save all scripts, queries, and CSV outputs here.

---

## How It Works

Instagram blocks direct scraping. Google doesn't — every public Instagram profile is indexed.

```
site:instagram.com "founder" AND "@" AND "Los Angeles" AND "MedSpa"
```

The `"@"` filter biases results toward profiles with an email in their bio. Combining base keywords x locations x niches generates thousands of unique searches that surface different slices of Instagram's index.

**Cost example:** 20 base keywords x 150 locations x 200 niches = 600,000 queries. At $0.001/query (Ultra plan) = $600. Scale down by using fewer locations/niches for cheaper runs. A targeted run (3 keywords x 5 cities x 10 niches = 150 queries) costs $0.15.

---

## Pipeline

### Step 1: Generate Queries

```bash
python scripts/generate_searches.py --output queries.txt
```

Default: 20 base keywords x 150 locations x ~200 niches. Use flags to scope down:

```bash
# Estimate cost without generating
python scripts/generate_searches.py --estimate-only

# Targeted run
python scripts/generate_searches.py \
  --base-keywords founder CEO owner \
  --locations "Miami" "Austin" "Nashville" \
  --niche-keywords MedSpa Wellness Skincare \
  --output queries.txt

# Use JSON config for full control
python scripts/generate_searches.py --config config.json --output queries.txt
```

See [references/keywords.md](references/keywords.md) for all default keywords.
See [references/locations.md](references/locations.md) for location strategy.

### Step 2: Run Scraper

Requires `OPENWEB_NINJA_API_KEY` env var and `pip install requests`.

```bash
export OPENWEB_NINJA_API_KEY="your-key-here"
python scripts/run_scraper.py queries.txt --output instagram_profiles.csv
```

Features:
- **Bulk API:** 20 queries per API call via POST /search-light
- **Real-time dedup:** Skips usernames already seen
- **Resume support:** Interrupted? Run same command again — picks up where it left off
- **Rate limiting:** 0.5s delay between batches (configurable with `--delay`)

```bash
# Dry run to see estimates
python scripts/run_scraper.py queries.txt --dry-run

# Custom settings
python scripts/run_scraper.py queries.txt \
  --output results.csv \
  --delay 1.0 \
  --batch-size 20 \
  --limit 10
```

### Step 3: Parse & Export for Clay

```bash
python scripts/parse_and_export.py instagram_profiles.csv --output clay_ready.csv --stats
```

This:
- Re-extracts emails from bio snippets
- Extracts location and niche from search queries into separate columns
- Final dedup pass
- Filters out thin profiles (configurable `--min-bio-length`)
- Optional `--require-email` flag

Output columns: `instagram_url, username, display_name, bio_snippet, extracted_email, location, niche`

### Step 4: Clay Import

Import `clay_ready.csv` into Clay for:
- Apify Instagram enrichment (full bio, follower count, post count)
- Email validation (ZeroBounce/NeverBounce)
- Additional enrichment (company, LinkedIn profile)

---

## Long-Running Execution

The scraper can take hours for large query sets. Run it as a background process:

```bash
nohup python scripts/run_scraper.py queries.txt --output results.csv > scraper.log 2>&1 &
echo $! > scraper.pid
```

Monitor: `tail -f scraper.log`
Stop: `kill $(cat scraper.pid)`

Resume after interruption — just re-run the same command. Progress is saved automatically.

---

## Quick Start (Small Test)

Generate 27 queries, scrape, and export in under a minute:

```bash
cd 02_Areas/Sales/Scraped\ Data/instagram/

python /path/to/skill/scripts/generate_searches.py \
  --base-keywords founder \
  --locations "Miami" "Austin" "Nashville" \
  --niche-keywords MedSpa Wellness Skincare \
  --output test_queries.txt

export OPENWEB_NINJA_API_KEY="your-key"
python /path/to/skill/scripts/run_scraper.py test_queries.txt --output test_results.csv

python /path/to/skill/scripts/parse_and_export.py test_results.csv --output test_clay.csv --stats
```
