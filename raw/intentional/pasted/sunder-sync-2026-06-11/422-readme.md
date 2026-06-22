---
type: raw_capture
source_type: pasted
title: "Sunder sync: README.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/scripts/sg-agent-scraper/README.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/scripts/sg-agent-scraper/README.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "scripts/sg-agent-scraper/README.md"
sha256: "811b41729c1a30ceb6f022474a0c308f6f8e4612157766a5bb401a407d1fe22c"
duplicate_of: ""
---

# Sunder sync: README.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/scripts/sg-agent-scraper/README.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/scripts/sg-agent-scraper/README.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Singapore Property Agent Scraper

Data pipeline that ingests Singapore's CEA property agent registry and transaction records from data.gov.sg into Supabase.

## Setup

```bash
cd scripts/sg-agent-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Already has creds pre-filled
```

## Usage

```bash
# Run full pipeline
python run_pipeline.py

# Dry run (no DB writes)
python run_pipeline.py --dry-run

# Individual steps
python run_pipeline.py --agents-only
python run_pipeline.py --txn-only
python run_pipeline.py --movements-only
```

## Data Sources

- **Agent Registry**: ~37,600 agents from CEA
- **Transaction Records**: ~1.3M transactions from data.gov.sg

## License

Public data - open licence from data.gov.sg
