---
type: raw_capture
source_type: pasted
title: "Sunder sync: README.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/README.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/README.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "scrapers/sg-insurance/README.md"
sha256: "0244831b32e86e1be1ee63b73b5ae8a26a74a16f09319973bd085416f8bf20fa"
duplicate_of: ""
---

# Sunder sync: README.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/README.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/README.md

Duplicate of existing source-map entry: `none`

## Capture Text

# SG Insurance Scraper

Scraper for Singapore insurance agent data from multiple sources.

## Usage

```bash
cd scrapers/sg-insurance
source .venv/bin/activate
pip install -e ".[dev]"

# Run individual scrapers
python -m src.scrape_mas_fid
python -m src.scrape_aia
python -m src.scrape_manulife
python -m src.scrape_fwd
python -m src.scrape_great_eastern
python -m src.scrape_prudential

# Run pipeline
python -m src.run_all --skip-verify
```

