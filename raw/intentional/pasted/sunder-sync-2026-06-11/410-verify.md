---
type: raw_capture
source_type: pasted
title: "Sunder sync: VERIFY.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/VERIFY.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/VERIFY.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "scrapers/sg-insurance/VERIFY.md"
sha256: "61ae28ca5c156a09364c44285420c2b181912bcd10e70358ab950ea261bcab32"
duplicate_of: ""
---

# Sunder sync: VERIFY.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/VERIFY.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/VERIFY.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Verification Guide for Another Developer

## Quick Verification Steps

### 1. Check the database exists and has data

```bash
cd scrapers/sg-insurance
ls -lh output/agents.db
sqlite3 output/agents.db "SELECT COUNT(*) FROM agents; SELECT COUNT(*) FROM firms;"
```

### 2. Run the tests

```bash
cd scrapers/sg-insurance
source .venv/bin/activate
python -m pytest tests/ -v
```

### 3. Verify CSV export

```bash
head -20 output/sg_insurance_agents.csv
wc -l output/sg_insurance_agents.csv  # Should show 1810 (1809 + header)
```

### 4. Sample check - verify data quality

```bash
sqlite3 output/agents.db "
-- Check AIA agents have team codes
SELECT COUNT(*) FROM agents WHERE source='aia' AND team_code IS NOT NULL;

-- Check Manulife agents by tier
SELECT mdrt_status, COUNT(*) FROM agents WHERE source LIKE 'manulife%' GROUP BY mdrt_status;

-- Sample random agents
SELECT agent_name, insurer, source FROM agents ORDER BY RANDOM() LIMIT 10;
"
```

### 5. Re-run a scraper to verify it works

```bash
# Quick test with Manulife (fast)
python -m src.scrape_manulife
```

## Expected Results

- **Tests**: All passing
- **Firms**: ~1,019 records
- **Agents**: ~1,809 records
- **CSV**: 1,810 lines (header + 1,809 data rows)

## Data Breakdown by Source

| Source        | Expected Count |
| ------------- | -------------- |
| aia           | ~1,200-1,300   |
| manulife_mag  | ~150-200       |
| manulife_fa   | ~250-300       |
| fwd           | ~10-30         |
| great_eastern | ~20-50         |
| prudential    | ~50-100        |

## Known Limitations (from Tasklist)

1. **AIA parser** - May have missed some agents due to HTML structure variations
2. **Manulife** - Captured names but not all team/unit details
3. **FWD** - JS-rendered content, may need DynamicFetcher
4. **Prudential** - Search-based, limited results
5. **FIRV verification** - Not yet run (Task 8 skipped)

## To Verify Parser Fixes

If you want to improve any parser:

1. Check `tests/fixtures/` for saved HTML
2. Update the parser in `src/scrape_*.py`
3. Run scraper again: `python -m src.scrape_[name]`
4. Check results in DB
