---
type: raw_capture
source_type: pasted
title: "Sunder sync: FIXES_NEEDED.md"
url: "https://mag.manulife.com.sg/en/awards2024/mdrt.html"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/FIXES_NEEDED.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "scrapers/sg-insurance/FIXES_NEEDED.md"
sha256: "1d0ea2fb6c19c419d4f6ffd14de16522cfe607befc29cdf0fd1ec1ea74b027f9"
duplicate_of: ""
---

# Sunder sync: FIXES_NEEDED.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/scrapers/sg-insurance/FIXES_NEEDED.md`

Primary URL: https://mag.manulife.com.sg/en/awards2024/mdrt.html

Duplicate of existing source-map entry: `none`

## Capture Text

# Scraper Fixes Needed

Live browser verification was run against all 6 target sites. Three of them have significant coverage gaps.
Here's what's broken and exactly how to fix it.

---

## TL;DR
do i
| Source | DB Count | Real Count | Status |
|---|---|---|---|
| AIA | ~1,200–1,300 | ~1,200+ | OK |
| Manulife MAG | ~150–200 | ~300+ | Missing 7 pages |
| Manulife FA | ~250–300 | ~400–500+ | Missing team profiles |
| FWD | ~10–30 | 0 real agents | Dead end — data doesn't exist on page |
| Great Eastern | ~20–50 | 200–500+ | Critical — pagination never handled |
| Prudential | ~50–100 | Unknown | Acceptable for now |

---

## Fix 1 (Critical): Great Eastern — Handle Infinite Scroll

**Problem:** `scrape_great_eastern.py` makes a single `DynamicFetcher.fetch()` call and parses whatever HTML comes back. The GE listing uses infinite scroll — each "View more" click loads 9 more agents. After a single page load you get 9 agents. There are **200+ confirmed in the directory, button still showing at 200**.

**Fix:** Use Playwright directly to click "View more" until the button disappears.

```python
# scrape_great_eastern.py — replace scrape_great_eastern()

from playwright.sync_api import sync_playwright

def scrape_great_eastern() -> int:
    conn = get_db()
    all_agents = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="networkidle", timeout=60000)

        while True:
            # Parse what's currently loaded
            html = page.content()
            batch = parse_ge_page(html, URL)
            all_agents = batch  # parse_ge_page reads the full DOM each time

            # Click "View more" if it exists
            view_more = page.query_selector("button:has-text('View more')")
            if not view_more:
                print(f"[GE] No more pages. Total agents in DOM: {len(all_agents)}")
                break

            print(f"[GE] {len(all_agents)} loaded so far, clicking View more...")
            view_more.click()
            page.wait_for_timeout(3000)  # wait for batch to render

        browser.close()

    if all_agents:
        count = upsert_agents(conn, all_agents)
        print(f"[GE] Stored {count} agents")

    conn.close()
    return len(all_agents)
```

**Also fix `parse_ge_page`** — the current regex `^[A-Z][a-zA-Z\s\.\-']+$` will miss names like "Lim Xiao Zhuang, Cheryl" (comma) and Chinese names with parentheses e.g. "Ong Kim Leong (Wang Jinlong)". The GE listing also shows the firm entity and join date on the same card, so you should target the actual name element more precisely instead of regex-matching all text lines.

The rendered DOM has a clear structure — each card contains the name, entity (Great Eastern Life vs Great Eastern Financial Advisers), join date, and optional bio. Parse the name element directly instead of text-dumping.

**Expected uplift:** 9 → 200+ agents.

---

## Fix 2 (High): Manulife MAG — Add the 7 Missing Pages

**Problem:** `scrape_manulife.py` only hits `/en/awards2024/mdrt.html`. The site has 7 award pages under Awards 2024, all with agent data:

```
/en/awards2024/tier-i.html       — individual FSC award winners (~20 names)
/en/awards2024/tier-ii.html      — unit leader awards (~15 names)
/en/awards2024/tier-iii.html     — branch leader awards (~10 names)
/en/awards2024/titans-tier-i.html — LARGEST: 30+ agents across 4/3/2/1-star tiers
/en/awards2024/titans-tier-ii.html — ~15–20 agents
/en/awards2024/titans-tier-iii.html — ~10 agents
/en/awards2024/mdrt.html         — already scraped ✓
```

**Fix:** Update `MAG_URLS` in `scrape_manulife.py`:

```python
MAG_URLS = [
    "https://mag.manulife.com.sg/en/awards2024/mdrt.html",
    "https://mag.manulife.com.sg/en/awards2024/titans-tier-i.html",
    "https://mag.manulife.com.sg/en/awards2024/titans-tier-ii.html",
    "https://mag.manulife.com.sg/en/awards2024/titans-tier-iii.html",
    "https://mag.manulife.com.sg/en/awards2024/tier-i.html",
    "https://mag.manulife.com.sg/en/awards2024/tier-ii.html",
    "https://mag.manulife.com.sg/en/awards2024/tier-iii.html",
]
```

**Also fix the `source` field** — right now everything goes in as `manulife_mag`. The Titans pages contain managers/unit leaders, not just individual agents. Consider tagging them differently (e.g. `manulife_mag_titans`) so you can filter by role later.

**Also note:** Tier I/II/III pages show award rankings (1st/2nd/3rd) in a prose format like `1ST Tiffany Ng Kenn Loh's Unit Affluence Wealth Advisory`. Your current `parse_mag_page()` text-line parser will likely pick up "1ST" as a name candidate. Add `"1st", "2nd", "3rd", "1ST", "2ND", "3RD"` to `skip_patterns`.

**Expected uplift:** 150 → 300+ agents.

---

## Fix 3 (Medium): Manulife FA — Scrape Team Leader Profiles

**Problem:** `scrape_manulife.py` only hits `/mdrt.html`. The FA site has a `/leaders.html` page listing ~15 team leaders, each with a profile page (`/team-leader-*.html`) that likely contains their full team roster.

**Fix:** Add a new function to scrape leader profiles:

```python
FA_LEADERS_URL = "https://manulifefa.com.sg/leaders.html"

def scrape_fa_leaders() -> int:
    """Scrape FA team leaders page and each leader's profile page."""
    from scrapling.fetchers import Fetcher
    from scrapling import Selector
    import re

    conn = get_db()
    total = 0

    page = Fetcher.get(FA_LEADERS_URL, stealthy_headers=True)
    if page.status != 200:
        print(f"[Manulife FA Leaders] ERROR: {page.status}")
        conn.close()
        return 0

    selector = Selector(page.body.decode(page.encoding or "utf-8"), url=FA_LEADERS_URL)

    # Extract team leader names + profile URLs directly
    profile_links = selector.css("a[href*='team-leader']")

    for link in profile_links:
        name = link.css("h4 ::text").get("").strip()
        role = link.css("h5 ::text").get("").strip()
        href = link.attrib.get("href", "")
        profile_url = f"https://manulifefa.com.sg/{href}" if href else None

        if name:
            agents = [Agent(
                agent_name=name.upper(),
                source="manulife_fa_leader",
                insurer="Manulife",
                role_title=role,
                page_url=FA_LEADERS_URL,
            )]
            total += upsert_agents(conn, agents)

        # Scrape the profile page for team members if URL exists
        if profile_url:
            time.sleep(3)
            profile_page = Fetcher.get(profile_url, stealthy_headers=True)
            if profile_page.status == 200:
                # Parse team members from profile — structure TBD, inspect fixtures
                team_agents = parse_fa_page(
                    profile_page.body.decode(profile_page.encoding or "utf-8"),
                    profile_url
                )
                if team_agents:
                    total += upsert_agents(conn, team_agents)
                    print(f"[Manulife FA] {len(team_agents)} team members from {profile_url}")

    conn.close()
    return total
```

Then call `scrape_fa_leaders()` from `scrape_manulife()`.

**Note:** Each profile page structure needs to be verified — save a fixture HTML first (`tests/fixtures/fa_leader_sample.html`) and write a unit test before assuming the parser works.

**Expected uplift:** 250 → 400–500+ agents.

---

## Fix 4 (Cleanup): FWD — Remove or Quarantine the Fake Data

**Problem:** `scrape_fwd.py` claims 10–30 FWD agents but `fwd.com.sg/elite-advisers/` shows **only firms** — 7 advisory companies with a "Email me" mailto link per firm. There are no individual agent names on the page. The `personalised-financial-advice/` URL is a product landing page with zero agents.

The parser is producing false positives — likely matching role words ("director", "adviser") against nav text and extracting garbage.

**Fix options:**

**Option A (recommended):** Delete both FWD URLs from `URLS`, log a comment, done.
```python
# FWD does not publish individual agent names on their public site.
# /elite-advisers/ lists 7 advisory firms (firm-level only).
# /personalised-financial-advice/ is a product page with no agent data.
# Leaving this scraper as a stub in case they add an agent directory later.
URLS = []
```

**Option B:** Scrape the 7 firm names + contact info as firm-level records if that's still useful, but store them separately from agent records so they don't pollute your agent count.

Either way, **delete the 10–30 FWD entries currently in the DB** — they are not real agents.

```sql
DELETE FROM agents WHERE source = 'fwd';
```

---

## Fix 5 (Minor): AIA — You're Fine, But Know Your Gaps

The AIA scraper is actually solid. The directory covers thousands of agents alphabetically. A few notes:

**Pages the scraper doesn't hit that only contain duplicates (don't bother):**
- `/top-awards/` — 5 agents, all already in MDRT/Top Producers pages
- `/top-new-awards/` — 4 agents, all duplicates
- `/top-business-lines/` — ~10 agents, all duplicates
- `/top-mdrt-district-and-agency-awards-2024/` — 4 agents, all duplicates

**Known parser fragility:** The text-based SP-code regex works but is brittle. If a page doesn't have `SP-` codes (e.g. the directory pages for some agents), names get dropped. Run a spot check:
```sql
SELECT COUNT(*) FROM agents WHERE source = 'aia' AND team_code IS NULL;
```
If that's non-zero, those are agents the parser found a name for but no team code — verify they're real and not nav/heading text.

---

## Priority Order

1. **Great Eastern** — fix the pagination loop. Biggest absolute gain (9 → 200+).
2. **Manulife MAG** — add 6 URLs to the list. 10-minute fix. 150 → 300+.
3. **FWD** — delete the fake data. 5-minute fix.
4. **Manulife FA** — scrape leader profiles. More work but high value contacts.

---

## How to Verify After Fixes

```bash
sqlite3 output/agents.db "
SELECT source, COUNT(*) as count
FROM agents
GROUP BY source
ORDER BY count DESC;
"
```

Expected after fixes:

| source | count |
|---|---|
| aia | ~1,200–1,400 |
| manulife_fa | ~400–500 |
| manulife_mag | ~300+ |
| great_eastern | ~200+ |
| prudential | ~50–100 |
| fwd | 0 (deleted) |
