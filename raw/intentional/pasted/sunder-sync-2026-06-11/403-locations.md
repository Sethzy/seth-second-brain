---
type: raw_capture
source_type: pasted
title: "Sunder sync: locations.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/locations.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/locations.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-instagram-scraper/references/locations.md"
sha256: "2e0562059abde0481de9c521c1ab2f4078c5e7e4c676fe376156661b9974f9a9"
duplicate_of: ""
---

# Sunder sync: locations.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/locations.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/locations.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Default Locations

## US States (50)

All 50 states included by default. Disable with `--no-states`.

## US Cities (100)

Top 100 US cities by population plus high-value smaller markets (Savannah, Charleston, Asheville, Boulder, Santa Fe, Park City, Sedona, Napa, Palm Springs).

Disable with `--no-cities`.

## Location Strategy

**Why both states AND cities?**

Google returns different results for `"California"` vs `"Los Angeles"`. State-level queries catch profiles that mention the state name in their bio. City-level queries catch profiles mentioning their specific city. The deduplication step handles overlap.

**Reducing query volume:**

For a targeted campaign, use `--no-states` and a custom config with only the cities you care about:

```json
{
  "locations": ["Miami", "Austin", "Nashville", "Denver", "Scottsdale"]
}
```

This drops from 150 locations to 5, cutting total queries by ~97%.

## International

Default locations are US-only. For international targeting, pass a config:

```json
{
  "locations": ["London", "Toronto", "Sydney", "Dubai", "Singapore"]
}
```
