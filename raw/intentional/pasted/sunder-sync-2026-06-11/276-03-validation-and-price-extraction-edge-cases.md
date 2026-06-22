---
type: raw_capture
source_type: pasted
title: "Sunder sync: 03-validation-and-price-extraction-edge-cases.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/03-validation-and-price-extraction-edge-cases.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/03-validation-and-price-extraction-edge-cases.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/03-validation-and-price-extraction-edge-cases.md"
sha256: "d11226dd5daa1e0c58a5bcd0bb546cb2f8be486c7b2d01af085d814101189f1b"
duplicate_of: ""
---

# Sunder sync: 03-validation-and-price-extraction-edge-cases.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/03-validation-and-price-extraction-edge-cases.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/simple-price-monitor-workflow/03-validation-and-price-extraction-edge-cases.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Validation and Price Extraction Edge Cases

## Pre-trigger validation run

Run one initial scrape before enabling schedule to verify:
- URL reachable
- price extraction feasible
- response format understood

## High-risk extraction failures

1. JS-rendered prices only
- static scrape misses runtime DOM updates
- may require browser-computer-use path

2. Multiple price candidates
- list price, discounted price, member price
- resolve with explicit heuristic priority

3. Currency mismatch
- threshold currency vs page currency mismatch
- return currency explicitly and avoid silent conversion assumptions

## Extraction strategy order

1. structured product metadata (JSON-LD)
2. semantic attributes/selectors
3. fallback regex patterns
4. ambiguity report if confidence is low


