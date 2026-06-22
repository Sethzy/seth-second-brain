---
type: raw_capture
source_type: pasted
title: "Sunder sync: SKILL.md"
url: "https://example.com/directory"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-2-web-scraper/SKILL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-2-web-scraper/SKILL.md"
sha256: "c67e7e4b55759cc83254fe5eca11adc13885d1b1289495107501761a653f1cf0"
duplicate_of: ""
---

# Sunder sync: SKILL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-2-web-scraper/SKILL.md`

Primary URL: https://example.com/directory

Duplicate of existing source-map entry: `none`

## Capture Text

---
name: sales-2-web-scraper
description: Generate local Playwright scraping scripts for any website. Use when user wants to scrape a website, extract data from a directory, or automate data collection. Triggers on "scrape", "scrape workflow [name]", "extract data from", "get data from [URL]".
---

# Web Scraper

## Execution

**Announce at start:** "I'm creating a scraping script for [URL]."

**Output location:** `02_Areas/Sales/Scraped Data/` - save all scripts and CSV outputs here.

---

## The Basics

**What is scraping?**
Automating "right-click → copy" on a website.

**Why Playwright?**
Some sites load data with JavaScript. Regular HTTP requests get empty pages. Playwright runs a real browser, waits for JS, then extracts.

**The pattern:**
```
1. Open browser
2. Go to URL
3. Wait for content to load
4. Find elements
5. Extract text from each
6. Save to CSV
```

---

## Setup

```bash
pip install playwright
playwright install chromium
```

---

## How Scraping Works

### Step 1: Inspect the Page

Open the target URL in Chrome. Right-click any item → "Inspect".

```html
<div class="member-card">
  <h3>John Tan</h3>
  <p class="company">ABC Corp</p>
  <a href="mailto:john@abc.com">john@abc.com</a>
</div>
```

**Find:**
1. The **container** for each item (`.member-card`)
2. The **fields** inside it (`h3`, `.company`, `a[href^='mailto:']`)

### Step 2: Selectors

| Selector | Finds |
|----------|-------|
| `.member-card` | Elements with class "member-card" |
| `h3` | All h3 elements |
| `a[href^='mailto:']` | Links starting with "mailto:" |

**Test in Chrome:** DevTools → Elements → Ctrl+F → paste selector.

### Step 3: The Script

```python
from playwright.sync_api import sync_playwright

def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible browser by default

        # Use realistic user agent (default gets blocked)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )

        # Navigate with timeout
        page.goto("https://example.com/directory", timeout=30000)

        # Wait for specific element with timeout
        page.wait_for_selector(".member-card", timeout=15000)

        # Find all items
        cards = page.locator(".member-card").all()

        # Extract from each
        data = []
        for card in cards:
            name = card.locator("h3").text_content() or ""
            company = card.locator(".company").text_content() or ""
            data.append({
                "name": name.strip(),
                "company": company.strip(),
            })

        browser.close()
        return data
```

---

## Two-Phase Directory Scraping

Most directories (trade associations, member lists, company databases) require visiting each detail page to get full data. The listing page only shows names/links.

**Pattern:**
```
Phase 1: Collect URLs     → listing pages → list of detail URLs
Phase 2: Scrape Details   → visit each URL → extract full profile
```

### Example Structure

```python
def collect_links(page):
    """Phase 1: Gather all detail page URLs from listing."""
    seen_ids = set()
    all_urls = []

    for page_num in range(1, MAX_PAGES + 1):
        url = BASE_URL.format(page=page_num)
        page.goto(url, timeout=30000)

        links = page.locator("a[href*='/members/']").all()
        if not links:
            break  # End of results

        new_count = 0
        for link in links:
            href = link.get_attribute("href")
            entity_id = extract_id(href)

            if entity_id and entity_id not in seen_ids:
                seen_ids.add(entity_id)
                all_urls.append(href)
                new_count += 1

        if new_count == 0:
            break  # No new entries = exhausted

    return all_urls


def scrape_detail(page, url):
    """Phase 2: Extract data from a single detail page."""
    page.goto(url, timeout=30000)
    page_text = page.locator("body").text_content() or ""

    return {
        "name": get_text(page.locator("h1")),
        "description": extract_section(page_text, "Profile:"),
        "address": extract_section(page_text, "Address:"),
        "phone": get_text(page.locator("a[href^='tel:']")),
        "email": get_text(page.locator("a[href^='mailto:']")),
        "url": url,
    }


# Orchestration
links = collect_links(page)
print(f"Found {len(links)} companies")

all_data = []
for i, url in enumerate(links):
    print(f"[{i+1}/{len(links)}] Scraping...")
    data = scrape_detail(page, url)
    if data:
        all_data.append(data)
    time.sleep(2)  # Be polite
```

### Helper: Extract ID from URL

```python
import re

def extract_id(url):
    """Extract entity ID from URL like /members/12345"""
    match = re.search(r"/(\d+)/?$", url)
    return match.group(1) if match else None
```

### Helper: Extract Text Section

```python
def extract_section(page_text, header):
    """Extract text after a header like 'Profile:' or 'Address:'"""
    import re
    pattern = rf"{header}\s*(.+?)(?=\n[A-Z][a-z]+:|$)"
    match = re.search(pattern, page_text, re.DOTALL)
    return match.group(1).strip() if match else ""
```

---

## Best Practices

### 1. Always set timeouts

```python
# Navigation - can hang on slow/dead sites
page.goto(url, timeout=30000)

# Waiting for elements - fail fast if wrong selector
page.wait_for_selector(".member-card", timeout=15000)
```

### 2. Use a realistic User-Agent

Default Playwright UA contains "HeadlessChrome" - many sites block it.

```python
page = browser.new_page(
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
```

### 3. Set viewport size

Mobile vs desktop = different layouts/selectors.

```python
page = browser.new_page(viewport={"width": 1920, "height": 1080})
```

### 4. Handle missing data

Not every card has every field:

```python
def get_text(locator):
    """Safely extract text from locator."""
    try:
        if locator.count() > 0:
            text = locator.first.text_content()
            return text.strip() if text else ""
    except Exception:  # NOT bare except:
        pass
    return ""
```

### 5. Browser visibility + screenshots

Scripts run with visible browser by default. Use `--headless` flag for background mode.

```python
# Default: visible browser
browser = p.chromium.launch(headless=False)

# For debugging, take a screenshot
page.screenshot(path="debug.png")
```

### 6. Be polite to servers

```python
import time
time.sleep(1)  # Between pages
```

### 7. Pagination with safeguards

**Option A: URL-based pagination (preferred)**

More reliable - no button detection needed. Look for `page=`, `pageIndex=`, `offset=` in the URL.

```python
BASE_URL = "https://example.com/directory?page={page}&size=50"
MAX_PAGES = 20

for page_num in range(1, MAX_PAGES + 1):
    url = BASE_URL.format(page=page_num)
    page.goto(url, timeout=30000)

    items = page.locator(".item").all()
    if not items:
        break  # No more results

    # Extract data from items...
    time.sleep(1)
```

**Option B: Button-click pagination**

Use when URL doesn't change between pages.

```python
MAX_PAGES = 50
ITEM_SELECTOR = ".member-card"

for page_num in range(MAX_PAGES):
    # Extract current page data...

    next_btn = page.locator("button.next, a.next, [aria-label='Next']")

    # Check both existence and visibility
    if next_btn.count() == 0:
        break
    if not next_btn.first.is_visible():
        break
    if next_btn.first.is_disabled():
        break

    next_btn.first.click()
    page.wait_for_selector(ITEM_SELECTOR, timeout=10000)
```

### 8. Speed up by blocking unnecessary resources

```python
# Block images, fonts, CSS (we only need data)
page.route(
    "**/*.{png,jpg,jpeg,gif,svg,ico,woff,woff2,css}",
    lambda route: route.abort()
)
```

### 9. Handle iframes

If content is inside an iframe:

```python
frame = page.frame_locator("iframe.content-frame")
items = frame.locator(".member-card").all()
```

### 10. Simple retry for flaky sites

```python
def scrape_with_retry(url, max_retries=2):
    for attempt in range(max_retries + 1):
        try:
            return scrape(url)
        except Exception as e:
            if attempt == max_retries:
                raise
            print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            time.sleep(2)
```

### 11. Handle cookie consent banners

Many sites (especially EU) block content until you accept cookies:

```python
# Common cookie consent selectors
COOKIE_SELECTORS = [
    "button:has-text('Accept')",
    "button:has-text('Accept all')",
    "[id*='cookie'] button",
    "[class*='cookie'] button",
    "[id*='consent'] button",
    ".cc-accept",
]

def dismiss_cookie_banner(page):
    """Try to dismiss cookie consent if present."""
    for selector in COOKIE_SELECTORS:
        try:
            btn = page.locator(selector).first
            if btn.is_visible(timeout=1000):
                btn.click()
                return True
        except Exception:
            pass
    return False

# Use after page.goto():
dismiss_cookie_banner(page)
```

### 12. Handle infinite scroll / lazy loading

Some sites load content as you scroll:

```python
def scroll_to_load_all(page, item_selector, max_scrolls=20):
    """Scroll down until no new items load."""
    previous_count = 0

    for _ in range(max_scrolls):
        current_count = page.locator(item_selector).count()

        if current_count == previous_count:
            break  # No new items loaded

        previous_count = current_count

        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Wait for potential new content
        try:
            page.wait_for_timeout(1500)  # Give time for lazy load
        except Exception:
            break

    return page.locator(item_selector).all()
```

### 13. Handle rate limiting

Sites may block you after too many requests. Detect and retry.

```python
RATE_LIMIT_PATTERNS = [
    "rate limit",
    "too many requests",
    "restricted due to exceeding",
    "please try again later",
    "access denied",
]

def is_rate_limited(page_text):
    """Check if page shows rate limit message."""
    text_lower = page_text.lower()
    return any(p in text_lower for p in RATE_LIMIT_PATTERNS)


def scrape_with_retry_queue(page, urls):
    """Scrape URLs, collecting failed ones for retry."""
    results = []
    failed = []

    for url in urls:
        page.goto(url, timeout=30000)
        page_text = page.locator("body").text_content() or ""

        if is_rate_limited(page_text):
            failed.append(url)
            print(f"Rate limited, will retry: {url}")
        else:
            results.append(extract_data(page))

        time.sleep(2)

    # Retry failed URLs with longer delays
    if failed:
        print(f"\nRetrying {len(failed)} rate-limited URLs...")
        for url in failed:
            time.sleep(5)  # Longer delay
            page.goto(url, timeout=30000)
            page_text = page.locator("body").text_content() or ""

            if not is_rate_limited(page_text):
                results.append(extract_data(page))

    return results
```

### 14. Deduplicate by entity ID

When multiple links point to the same entity (e.g., different badges linking to same company), deduplicate by extracting IDs from URLs.

```python
import re

def extract_id(url):
    """Extract entity ID from URL like /members/12345 or /company/abc-123"""
    # Numeric ID at end
    if match := re.search(r"/(\d+)/?$", url):
        return match.group(1)
    # Slug ID at end
    if match := re.search(r"/([^/]+)/?$", url):
        return match.group(1)
    return None


def deduplicate_urls(urls):
    """Remove duplicate URLs pointing to same entity."""
    seen_ids = set()
    unique = []

    for url in urls:
        entity_id = extract_id(url)
        if entity_id and entity_id not in seen_ids:
            seen_ids.add(entity_id)
            unique.append(url)

    return unique
```

---

## Common Problems

| Problem | Cause | Fix |
|---------|-------|-----|
| Timeout waiting for selector | Wrong selector or JS didn't load | Check selector in DevTools, increase timeout |
| Empty data | Content loaded after your wait | Use `wait_for_selector` on actual content |
| Script hangs forever | No timeout set, or using `networkidle` | Add `timeout=` to goto and wait_for_selector; avoid `networkidle` |
| Can't Ctrl+C to stop | Bare `except:` clause | Use `except Exception:` |
| Site looks different | Headless vs headed difference | Run `headless=False` to debug |
| Blocked/403 error | Bot detection | Add realistic User-Agent |
| Wrong layout | Viewport too small | Set explicit viewport size |
| Cookie banner blocks content | EU sites require consent | Use `dismiss_cookie_banner()` helper |
| Only partial data | Lazy loading / infinite scroll | Use `scroll_to_load_all()` helper |
| Rate limited / blocked | Too many requests too fast | Use `scrape_with_retry_queue()`, increase delays |
| Duplicate entries in output | Multiple links to same entity | Use `deduplicate_urls()` with ID extraction |

---

## Process

When user provides a URL:

### 1. Analyze

- Static HTML or JavaScript SPA?
- What's the repeating element?
- What fields in each?
- Pagination?

### 2. Generate Script

Using the template below. Fill in:
- URL
- Item selector
- Field selectors
- Pagination logic if needed

### 3. Explain

- How to run
- What selectors were chosen
- How to debug if it fails

---

## Template

```python
"""
[Site] Scraper
==============
Scrapes [description] from [URL]

Setup:
    pip install playwright
    playwright install chromium

Run:
    python scrape_[site].py

Note:
    Browser is visible by default. Add --headless for background mode.
"""

import csv
import time
from playwright.sync_api import sync_playwright

URL = "https://example.com/directory"
OUTPUT = "output.csv"
MAX_PAGES = 50


def get_text(locator):
    """Safely extract text from locator."""
    try:
        if locator.count() > 0:
            text = locator.first.text_content()
            return text.strip() if text else ""
    except Exception:
        pass
    return ""


def get_attr(locator, attr):
    """Safely extract attribute from locator."""
    try:
        if locator.count() > 0:
            return locator.first.get_attribute(attr) or ""
    except Exception:
        pass
    return ""


def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible by default

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )

        # Optional: block images/fonts for speed
        # page.route("**/*.{png,jpg,jpeg,gif,svg,woff,woff2}", lambda r: r.abort())

        print(f"Opening {URL}")
        try:
            page.goto(URL, timeout=30000)
        except Exception as e:
            print(f"Failed to load page: {e}")
            browser.close()
            return []

        # Wait for content
        try:
            page.wait_for_selector(".item", timeout=15000)
        except Exception as e:
            print(f"Content didn't load: {e}")
            page.screenshot(path="debug.png")
            print("Screenshot saved: debug.png")
            browser.close()
            return []

        all_data = []

        for page_num in range(MAX_PAGES):
            print(f"Page {page_num + 1}...")

            items = page.locator(".item").all()
            print(f"  Found {len(items)} items")

            for item in items:
                row = {
                    "name": get_text(item.locator("h3, .name")),
                    "company": get_text(item.locator(".company")),
                    "email": get_text(item.locator("a[href^='mailto:']")),
                    "phone": get_text(item.locator("a[href^='tel:']")),
                    "link": get_attr(item.locator("a"), "href"),
                }
                # Only add if we got some data
                row = {k: v for k, v in row.items() if v}
                if row:
                    all_data.append(row)

            # Pagination
            next_btn = page.locator("button.next, a.next, [aria-label='Next']")
            if next_btn.count() == 0:
                break
            if not next_btn.first.is_visible():
                break

            try:
                next_btn.first.click()
                page.wait_for_selector(".item", timeout=10000)
                time.sleep(1)  # Be polite
            except Exception as e:
                print(f"Pagination stopped: {e}")
                break

        browser.close()
        return all_data


def save_csv(data, filename):
    if not data:
        print("No data to save")
        return

    # Collect all possible keys across all rows
    all_keys = set()
    for row in data:
        all_keys.update(row.keys())

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sorted(all_keys))
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} rows to {filename}")


if __name__ == "__main__":
    print("=" * 50)
    print("Scraper")
    print("=" * 50)

    try:
        data = scrape()
        save_csv(data, OUTPUT)
        if data:
            print(f"\nDone! Check {OUTPUT}")
        else:
            print("\nNo data extracted. Check debug.png if it exists.")
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"\nError: {e}")
```

---

## Quick Reference

```python
# Navigate with timeout
page.goto(url, timeout=30000)

# Wait for element with timeout
page.wait_for_selector(".item", timeout=15000)

# Get text safely
text = locator.text_content() or ""

# Check element exists before using
if locator.count() > 0:
    locator.first.click()

# Screenshot for debugging
page.screenshot(path="debug.png")

# Block resources for speed
page.route("**/*.{png,jpg}", lambda r: r.abort())
```

---

## Pre-Built Scrapers

### MyCareersFuture (Singapore Jobs)

Scrapes job postings from mycareerfuture.gov.sg to find companies hiring.

**Location:** `scripts/scrape-mycareerfuture.py`

**Usage:**
```bash
python scrape-mycareerfuture.py "search term 1" "search term 2" --name output-name
```

**Examples:**
```bash
# Freight forwarders
python scrape-mycareerfuture.py "freight billing" "freight forwarder" "3PL" --name freight-forwarders

# Food manufacturing
python scrape-mycareerfuture.py "food QA" "food safety" "HACCP" --name food-manufacturing

# With debug mode (visible browser)
python scrape-mycareerfuture.py "logistics" --name test --debug
```

**Output:**
- `02_Areas/Sales/Scraped Data/mcf-{name}-jobs.csv` - All job postings
- `02_Areas/Sales/Scraped Data/mcf-{name}-companies.csv` - Companies aggregated by job count

**Data extracted per job:**
- company_name, job_title, location, salary
- employment_type, seniority, category
- applications count, posted_date
- search_term (which query found it)

**Options:**
| Flag | Description |
|------|-------------|
| `--name, -n` | Output file prefix (required) |
| `--debug, -d` | Run with visible browser |
| `--max-pages` | Max pages per search (default: 10) |

---

## Workflow-Driven Scraping

When user says **"scrape workflow [name]"**, this mode reads a Clay workflow file and walks through building all required scrapers.

### How It Works

**Trigger:** `scrape workflow DistributorPricing` (explicit workflow name required)

**Workflow location:** `02_Areas/Sales/Clay Workflows/[name].md` or `[name]-Combined.md`

### Phase 1: Parse Workflow

Read the Clay workflow file and extract:

1. **Segment name** from frontmatter (`segment:`)
2. **Industry Directories** from `## Secondary Sources` section
   - Source name, URL, notes
   - Flag as scrapable vs manual-only
3. **Job Board searches** from `### Job Board Mining` table
4. **Champion titles** from `## Step 6: Contact Finding`
5. **Decision maker titles** from Step 6

### Phase 2: Generate Job Titles (15-20)

From workflow context, generate MCF search terms (conservative expansion):

| Source | Expansion Rule |
|--------|---------------|
| Job Board Mining section | Copy verbatim |
| Champion roles | Add: Senior [Role], [Role] Manager, [Role] Specialist |
| Decision maker roles | Add: Senior [Role], Head of [Function], Director [Function] |

**Example for DistributorPricing:**
```
From Job Board Mining:
1. "pricing analyst" Singapore
2. "category manager" wholesale Singapore
3. "procurement" distributor Singapore
4. "purchasing manager" construction Singapore
5. "buyer" building materials Singapore
6. "product manager" electronics distributor Singapore
7. "pricing specialist" IT Singapore
8. "catalog manager" Singapore
9. "category manager" industrial Singapore
10. "pricing manager" MRO Singapore

From Champion roles (Pricing Analyst, Category Manager, Purchasing Manager):
11. "senior pricing analyst" Singapore
12. "pricing manager" Singapore
13. "senior category manager" Singapore
14. "purchasing executive" Singapore
15. "senior purchasing manager" Singapore

From Decision Maker roles:
16. "sales director" distributor Singapore
17. "general manager" wholesale Singapore
18. "commercial director" Singapore
```

### Phase 3: Present Source Checklist

Show interactive checklist:

```markdown
## Sources to Scrape for [Segment]

### Industry Directories
☐ BCA Registered Suppliers - bca.gov.sg - Building materials
☐ SEIA Members - seia.org.sg - Electronics industry
☐ Singapore Manufacturing Federation - smf.org.sg - Industrial/MRO
☐ Singapore Business Federation - sbf.org.sg - All segments

### Job Board (MCF)
Search terms (18):
1. "pricing analyst" Singapore
2. "category manager" wholesale Singapore
...

### Already Scraped (skip)
✓ [Source] - [Date] - [Row count]

---
Which sources should I build scrapers for? (Enter numbers or "all")
```

### Phase 4: Build Scrapers

For each selected source:

1. **Analyze** - Visit site, identify selectors, pagination
2. **Generate script** → `scripts/scrape-[source].py`
3. **Test** - Run on 5 rows first
4. **Execute** - Full scrape
5. **Output** → `Scraped Data/[Segment]/[Source]-Raw.csv`

### Output Structure

```
02_Areas/Sales/Scraped Data/
└── [Segment]/
    ├── BCA-Registered-Suppliers.csv
    ├── SEIA-Members.csv
    ├── SMF-Members.csv
    ├── MCF-[Segment]-Jobs.csv
    └── MCF-[Segment]-Companies.csv
```

### Example Execution

```
User: scrape workflow DistributorPricing

Claude: Reading Clay workflow: DistributorPricing-Combined.md

## Sources to Scrape for Distributor Pricing (Combined)

### Industry Directories
1. ☐ Singapore Business Federation - sbf.org.sg
2. ☐ BCA Registered Suppliers - bca.gov.sg (Building Materials)
3. ☐ Singapore Contractors Association - scal.com.sg
4. ☐ SEIA Members - seia.org.sg (Electronics)
5. ☐ Singapore Manufacturing Federation - smf.org.sg (MRO)

### Job Board (MCF) - 18 search terms
1. "pricing analyst" Singapore
2. "category manager" wholesale Singapore
3. "procurement" distributor Singapore
...

Which sources should I build scrapers for?

User: 1, 2, and MCF

Claude: Building scrapers for:
- Singapore Business Federation
- BCA Registered Suppliers
- MCF (18 search terms)

Starting with SBF...
```
