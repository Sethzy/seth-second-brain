---
type: raw_capture
source_type: pasted
title: "Sunder sync: 2026-03-01-sg-insurance-agent-scraper-tasklist.md"
url: "https://example.com/john"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/docs/tasks/2026-03-01-sg-insurance-agent-scraper-tasklist.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "docs/tasks/2026-03-01-sg-insurance-agent-scraper-tasklist.md"
sha256: "dae0cef070b9f9410491946501c9edcf9baf6d4d1422ea088d1825cbc7e15dcb"
duplicate_of: ""
---

# Sunder sync: 2026-03-01-sg-insurance-agent-scraper-tasklist.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/docs/tasks/2026-03-01-sg-insurance-agent-scraper-tasklist.md`

Primary URL: https://example.com/john

Duplicate of existing source-map entry: `none`

## Capture Text

# Singapore Insurance Agent Scraper - Implementation Plan

**Goal:** Scrape all publicly available Singapore insurance agent data into a unified CSV/SQLite database.

**Architecture:** Sequential scraper pipeline using Scrapling (Python). Each target site gets its own scraper module. All output normalizes to a common agent schema and merges into a single SQLite DB. MAS FIRR verification runs as a final enrichment pass against the aggregated agent list.

**Tech Stack:** Python 3.10+, Scrapling (with fetchers), SQLite, CSV export

**Data Sources (Priority Order):**

| # | Source | Type | Difficulty | Est. Agents | Fetcher Needed |
|---|--------|------|-----------|-------------|----------------|
| 1 | MAS FID (firms) | Static HTML | Trivial | 390 firms | `Fetcher` (HTTP) |
| 2 | AIA Agency Recognition | WordPress/Elementor | Easy | ~2,000 | `Fetcher` (HTTP) |
| 3 | Manulife MAG | Static HTML | Easy | ~100 | `Fetcher` (HTTP) |
| 4 | Manulife FA | Static HTML | Easy | ~40 | `Fetcher` (HTTP) |
| 5 | FWD Elite Advisers | React | Medium | ~75 | `DynamicFetcher` |
| 6 | Great Eastern | React SPA | Hard | Unknown | `DynamicFetcher` |
| 7 | Prudential | Dynamic form | Hard | Unknown | `StealthyFetcher` |
| 8 | MAS FIRR (verification) | SPA + checkbox | Hard | N/A (lookup) | `DynamicFetcher` |

**Output Schema (per agent):**

```
agent_name          TEXT    -- Full name (normalized uppercase)
source              TEXT    -- Which site scraped from (aia, manulife_mag, etc.)
insurer             TEXT    -- Insurance company (AIA, Manulife, Prudential, etc.)
team_code           TEXT    -- SP code / unit / group (nullable)
role_title          TEXT    -- Job title if available (nullable)
mdrt_status         TEXT    -- TOT / COT / MDRT / null
mdrt_years          INT     -- Total MDRT years if available (nullable)
awards              TEXT    -- JSON array of award strings (nullable)
email               TEXT    -- Email if available (nullable)
mas_rep_number      TEXT    -- MAS representative number if verified (nullable)
mas_reg_status      TEXT    -- "Appointed" / "Left" / null
scraped_at          TEXT    -- ISO timestamp
page_url            TEXT    -- Source URL scraped from
```

---

## Bite-Sized Step Granularity

**Each step is one action (2-5 minutes):**
- "Write the failing test" → step
- "Run it to make sure it fails" → step
- "Implement the minimal code to make the test pass" → step
- "Run the tests and make sure they pass" → step
- "Commit" → step

---

## Task 1: Project Setup & Scrapling Installation

**Files:**
- Create: `scrapers/sg-insurance/pyproject.toml`
- Create: `scrapers/sg-insurance/README.md`
- Create: `scrapers/sg-insurance/src/__init__.py`
- Create: `scrapers/sg-insurance/src/models.py`
- Create: `scrapers/sg-insurance/src/db.py`
- Create: `scrapers/sg-insurance/tests/__init__.py`
- Create: `scrapers/sg-insurance/tests/test_db.py`

### Step 1: Create project directory structure

```bash
mkdir -p scrapers/sg-insurance/src scrapers/sg-insurance/tests scrapers/sg-insurance/output
touch scrapers/sg-insurance/src/__init__.py scrapers/sg-insurance/tests/__init__.py
```

### Step 2: Create pyproject.toml

```toml
# scrapers/sg-insurance/pyproject.toml
[project]
name = "sg-insurance-scraper"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "scrapling[fetchers]>=0.4",
]

[project.optional-dependencies]
dev = ["pytest>=8.0", "pytest-asyncio>=0.24"]
```

### Step 3: Create virtual environment and install dependencies

```bash
cd scrapers/sg-insurance
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
scrapling install  # installs Playwright browsers + Camoufox
```

Expected: No errors. `scrapling install` downloads ~400MB of browser binaries.

### Step 4: Write the agent data model

```python
# scrapers/sg-insurance/src/models.py
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone


@dataclass
class Agent:
    agent_name: str
    source: str  # aia, manulife_mag, manulife_fa, fwd, great_eastern, prudential
    insurer: str  # AIA, Manulife, FWD, Great Eastern, Prudential
    team_code: str | None = None
    role_title: str | None = None
    mdrt_status: str | None = None  # TOT, COT, MDRT, null
    mdrt_years: int | None = None
    awards: list[str] = field(default_factory=list)
    email: str | None = None
    mas_rep_number: str | None = None
    mas_reg_status: str | None = None
    scraped_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    page_url: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        import json
        d["awards"] = json.dumps(d["awards"]) if d["awards"] else None
        return d
```

### Step 5: Write the database module

```python
# scrapers/sg-insurance/src/db.py
import sqlite3
import csv
import json
from pathlib import Path
from .models import Agent

DB_PATH = Path(__file__).parent.parent / "output" / "agents.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_name TEXT NOT NULL,
    source TEXT NOT NULL,
    insurer TEXT NOT NULL,
    team_code TEXT,
    role_title TEXT,
    mdrt_status TEXT,
    mdrt_years INTEGER,
    awards TEXT,
    email TEXT,
    mas_rep_number TEXT,
    mas_reg_status TEXT,
    scraped_at TEXT NOT NULL,
    page_url TEXT,
    UNIQUE(agent_name, insurer, source)
);

CREATE TABLE IF NOT EXISTS firms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    website TEXT,
    sector TEXT,
    licence_type TEXT,
    activity TEXT,
    sub_activity TEXT,
    scraped_at TEXT NOT NULL,
    UNIQUE(name, licence_type)
);
"""


def get_db(db_path: Path = DB_PATH) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    return conn


def upsert_agent(conn: sqlite3.Connection, agent: Agent) -> None:
    d = agent.to_dict()
    conn.execute(
        """INSERT INTO agents (agent_name, source, insurer, team_code, role_title,
           mdrt_status, mdrt_years, awards, email, mas_rep_number, mas_reg_status,
           scraped_at, page_url)
           VALUES (:agent_name, :source, :insurer, :team_code, :role_title,
           :mdrt_status, :mdrt_years, :awards, :email, :mas_rep_number, :mas_reg_status,
           :scraped_at, :page_url)
           ON CONFLICT(agent_name, insurer, source) DO UPDATE SET
           team_code=excluded.team_code, role_title=excluded.role_title,
           mdrt_status=excluded.mdrt_status, mdrt_years=excluded.mdrt_years,
           awards=excluded.awards, email=excluded.email,
           mas_rep_number=excluded.mas_rep_number, mas_reg_status=excluded.mas_reg_status,
           scraped_at=excluded.scraped_at, page_url=excluded.page_url""",
        d,
    )


def upsert_agents(conn: sqlite3.Connection, agents: list[Agent]) -> int:
    count = 0
    for a in agents:
        upsert_agent(conn, a)
        count += 1
    conn.commit()
    return count


def export_csv(conn: sqlite3.Connection, path: Path) -> int:
    cur = conn.execute("SELECT * FROM agents ORDER BY insurer, agent_name")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        writer.writerows(rows)
    return len(rows)


def get_agent_count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]


def get_agents_by_source(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute(
        "SELECT source, COUNT(*) FROM agents GROUP BY source"
    ).fetchall()
    return dict(rows)
```

### Step 6: Write the failing test for db module

```python
# scrapers/sg-insurance/tests/test_db.py
import sqlite3
from pathlib import Path
from src.db import get_db, upsert_agent, upsert_agents, get_agent_count, export_csv
from src.models import Agent


def test_get_db_creates_tables(tmp_path):
    db_path = tmp_path / "test.db"
    conn = get_db(db_path)
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    table_names = [t[0] for t in tables]
    assert "agents" in table_names
    assert "firms" in table_names
    conn.close()


def test_upsert_agent(tmp_path):
    conn = get_db(tmp_path / "test.db")
    agent = Agent(
        agent_name="JOHN DOE",
        source="aia",
        insurer="AIA",
        team_code="SP-TEST",
        mdrt_status="MDRT",
        page_url="https://example.com/john",
    )
    upsert_agent(conn, agent)
    conn.commit()
    assert get_agent_count(conn) == 1

    # Upsert same agent updates, no duplicate
    agent.mdrt_status = "COT"
    upsert_agent(conn, agent)
    conn.commit()
    assert get_agent_count(conn) == 1

    row = conn.execute("SELECT mdrt_status FROM agents WHERE agent_name='JOHN DOE'").fetchone()
    assert row[0] == "COT"
    conn.close()


def test_upsert_agents_batch(tmp_path):
    conn = get_db(tmp_path / "test.db")
    agents = [
        Agent(agent_name="ALICE", source="aia", insurer="AIA", page_url=""),
        Agent(agent_name="BOB", source="manulife_mag", insurer="Manulife", page_url=""),
    ]
    count = upsert_agents(conn, agents)
    assert count == 2
    assert get_agent_count(conn) == 2
    conn.close()


def test_export_csv(tmp_path):
    conn = get_db(tmp_path / "test.db")
    upsert_agents(conn, [
        Agent(agent_name="ALICE", source="aia", insurer="AIA", page_url=""),
    ])
    csv_path = tmp_path / "agents.csv"
    rows = export_csv(conn, csv_path)
    assert rows == 1
    assert csv_path.exists()
    content = csv_path.read_text()
    assert "ALICE" in content
    conn.close()
```

### Step 7: Run tests to verify they pass

```bash
cd scrapers/sg-insurance
python -m pytest tests/test_db.py -v
```

Expected: All 4 tests PASS.

### Step 8: Commit

```bash
git add scrapers/sg-insurance/
git commit -m "feat: sg-insurance scraper project setup with models and db"
```

---

## Task 2: MAS FID Firm Scraper (390 Insurance Firms)

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_mas_fid.py`
- Create: `scrapers/sg-insurance/tests/test_mas_fid.py`

**Why first:** This is the reference table of all licensed insurance firms. Trivial to scrape (static HTML print page, no JS). Gives us the canonical list of insurers.

**Target URLs:**
- All insurance firms: `https://eservices.mas.gov.sg/fid/institution/print?sector=Insurance`
- Financial advisers: `https://eservices.mas.gov.sg/fid/institution/print?sector=Financial%20Advisory`

### Step 1: Write the failing test with a saved HTML fixture

```python
# scrapers/sg-insurance/tests/test_mas_fid.py
from pathlib import Path
from src.scrape_mas_fid import parse_fid_print_page

# We'll save a real HTML snippet as a fixture
FIXTURE = Path(__file__).parent / "fixtures" / "fid_insurance_print.html"


def test_parse_fid_print_page_returns_list():
    """Test that parser extracts firm rows from FID print page HTML."""
    if not FIXTURE.exists():
        # Create minimal fixture for testing
        FIXTURE.parent.mkdir(parents=True, exist_ok=True)
        FIXTURE.write_text("""
        <html><body>
        <table>
        <tr><th>No.</th><th>Organisation Name</th><th>Address</th><th>Phone Number</th>
            <th>Website</th><th>Sector</th><th>Licence Type/Status</th>
            <th>Activity/Business Type</th><th>Sub-Activity/Product</th></tr>
        <tr><td>1</td><td>AIA SINGAPORE PRIVATE LIMITED</td>
            <td>1 ROBINSON ROAD #13-00 048542</td><td>+65 6248 8000</td>
            <td>http://www.aia.com.sg</td><td>Insurance</td>
            <td>Direct Insurer (Life)</td><td>Serving General Market</td><td></td></tr>
        <tr><td>2</td><td>GREAT EASTERN LIFE ASSURANCE CO LTD</td>
            <td>1 PICKERING STREET #16-01 GREAT EASTERN CENTRE 048659</td>
            <td>+65 6248 2000</td><td>http://www.greateasternlife.com</td>
            <td>Insurance</td><td>Direct Insurer (Life)</td>
            <td>Serving General Market</td><td></td></tr>
        </table>
        </body></html>
        """)

    firms = parse_fid_print_page(FIXTURE.read_text())
    assert len(firms) == 2
    assert firms[0]["name"] == "AIA SINGAPORE PRIVATE LIMITED"
    assert firms[0]["licence_type"] == "Direct Insurer (Life)"
    assert firms[1]["phone"] == "+65 6248 2000"
```

### Step 2: Run test to verify it fails

```bash
python -m pytest tests/test_mas_fid.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'src.scrape_mas_fid'`

### Step 3: Implement the FID scraper

```python
# scrapers/sg-insurance/src/scrape_mas_fid.py
"""Scrape MAS Financial Institutions Directory (FID) print pages."""
import time
from scrapling.fetchers import Fetcher
from .db import get_db


URLS = {
    "insurance": "https://eservices.mas.gov.sg/fid/institution/print?sector=Insurance",
    "financial_advisory": "https://eservices.mas.gov.sg/fid/institution/print?sector=Financial%20Advisory",
}


def parse_fid_print_page(html: str) -> list[dict]:
    """Parse an FID print page HTML table into a list of firm dicts."""
    from scrapling import Selector

    page = Selector(html)
    rows = page.css("table tr")
    firms = []

    for row in rows:
        cells = row.css("td")
        if len(cells) < 8:
            continue  # skip header row or malformed rows

        firms.append({
            "name": cells[1].get_all_text(strip=True),
            "address": cells[2].get_all_text(strip=True),
            "phone": cells[3].get_all_text(strip=True),
            "website": cells[4].get_all_text(strip=True),
            "sector": cells[5].get_all_text(strip=True),
            "licence_type": cells[6].get_all_text(strip=True),
            "activity": cells[7].get_all_text(strip=True),
            "sub_activity": cells[8].get_all_text(strip=True) if len(cells) > 8 else "",
        })

    return firms


def scrape_fid() -> int:
    """Scrape all FID print pages and store in SQLite."""
    from datetime import datetime, timezone

    conn = get_db()
    total = 0

    for sector_key, url in URLS.items():
        print(f"[FID] Fetching {sector_key}: {url}")
        page = Fetcher.get(url, stealthy_headers=True)

        if page.status != 200:
            print(f"[FID] ERROR: Got status {page.status} for {url}")
            continue

        firms = parse_fid_print_page(page.body.decode(page.encoding or "utf-8"))
        now = datetime.now(timezone.utc).isoformat()

        for firm in firms:
            conn.execute(
                """INSERT INTO firms (name, address, phone, website, sector,
                   licence_type, activity, sub_activity, scraped_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(name, licence_type) DO UPDATE SET
                   address=excluded.address, phone=excluded.phone,
                   website=excluded.website, scraped_at=excluded.scraped_at""",
                (firm["name"], firm["address"], firm["phone"], firm["website"],
                 firm["sector"], firm["licence_type"], firm["activity"],
                 firm["sub_activity"], now),
            )

        conn.commit()
        total += len(firms)
        print(f"[FID] Stored {len(firms)} firms from {sector_key}")
        time.sleep(2)  # polite delay between requests

    conn.close()
    print(f"[FID] Done. Total firms: {total}")
    return total


if __name__ == "__main__":
    scrape_fid()
```

### Step 4: Run test to verify it passes

```bash
python -m pytest tests/test_mas_fid.py -v
```

Expected: PASS

### Step 5: Run the actual scraper against the live site

```bash
cd scrapers/sg-insurance
python -m src.scrape_mas_fid
```

Expected: `[FID] Done. Total firms: ~460` (390 insurance + ~70 financial advisory)

### Step 6: Commit

```bash
git add scrapers/sg-insurance/src/scrape_mas_fid.py scrapers/sg-insurance/tests/
git commit -m "feat: MAS FID firm scraper - insurance + financial advisory firms"
```

---

## Task 3: AIA Agent Directory Scraper (~2,000 Agents)

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_aia.py`
- Create: `scrapers/sg-insurance/tests/test_aia.py`

**Why this is the biggest target:** AIA is 37.9% of the SG insurance market. Their recognition site is WordPress/Elementor (server-rendered HTML, no JS needed). Multiple page types with rich data.

**Target URLs:**
- Directory: `https://aiagency.com.sg/directory/` (paginated)
- TOT: `https://aiagency.com.sg/tot/` → `/tot/page/2/` (2 pages)
- COT: `https://aiagency.com.sg/cot/` → `/cot/page/8/` (8 pages)
- MDRT & Life: `https://aiagency.com.sg/mdrt-mdrt-life/` → `/mdrt-mdrt-life/page/52/` (52 pages)
- 1st Time MDRT: `https://aiagency.com.sg/1st-time-mdrt-qualifiers/` → 11 pages
- Hall of Fame: `https://aiagency.com.sg/hall-of-fame/` → 2 pages
- Top Producers (multiple sub-pages for FSD, FSAD, FSM, FSC)

**Crawl delay:** robots.txt says `crawl-delay: 60` - we MUST respect this.

### Step 1: Write failing test with HTML fixture for MDRT/COT page

```python
# scrapers/sg-insurance/tests/test_aia.py
from src.scrape_aia import parse_mdrt_page, parse_directory_page, build_page_urls


def test_build_page_urls():
    urls = build_page_urls("https://aiagency.com.sg/cot/", max_pages=8)
    assert urls[0] == "https://aiagency.com.sg/cot/"
    assert urls[1] == "https://aiagency.com.sg/cot/page/2/"
    assert urls[7] == "https://aiagency.com.sg/cot/page/8/"
    assert len(urls) == 8


def test_parse_mdrt_page_extracts_agents():
    """Test with minimal fixture simulating AIA MDRT page structure.
    Actual page uses Elementor widgets. Each agent is in an elementor-widget
    with name, SP code, and membership years."""
    # In practice, run the scraper against the live site first,
    # save a page as fixture, then write this test against that HTML.
    # For now, test the URL builder and basic parse contract.
    pass
```

### Step 2: Run test to verify it fails

```bash
python -m pytest tests/test_aia.py -v
```

Expected: FAIL with `ModuleNotFoundError`

### Step 3: Implement the AIA scraper

```python
# scrapers/sg-insurance/src/scrape_aia.py
"""Scrape AIA Singapore agency recognition pages for agent data."""
import time
import re
from scrapling.fetchers import Fetcher
from .models import Agent
from .db import get_db, upsert_agents

BASE = "https://aiagency.com.sg"
CRAWL_DELAY = 60  # from robots.txt

# Page configs: (base_url, max_pages, mdrt_tier)
MDRT_PAGES = [
    (f"{BASE}/tot/", 2, "TOT"),
    (f"{BASE}/cot/", 8, "COT"),
    (f"{BASE}/mdrt-mdrt-life/", 52, "MDRT"),
    (f"{BASE}/1st-time-mdrt-qualifiers/", 11, "MDRT"),
    (f"{BASE}/hall-of-fame/", 2, None),
]

TOP_PRODUCER_PAGES = [
    f"{BASE}/top-producers/top-financial-services-directors-2024/",
    f"{BASE}/top-producers/top-financial-services-associate-directors-2024/",
    f"{BASE}/top-producers/top-financial-services-managers-2024/",
    f"{BASE}/top-producers/top-financial-services-consultants-2024/",
]


def build_page_urls(base_url: str, max_pages: int) -> list[str]:
    """Build paginated URLs. Page 1 = base, page 2+ = base/page/N/."""
    urls = [base_url]
    for i in range(2, max_pages + 1):
        urls.append(f"{base_url}page/{i}/")
    return urls


def parse_mdrt_page(html: str, page_url: str, default_tier: str | None) -> list[Agent]:
    """Parse an AIA MDRT/COT/TOT page.

    Agent cards typically contain:
    - Name (uppercase, bold)
    - SP code (e.g., "SP-GALAXY-CREST ADVISORY")
    - Award tier detail (e.g., "TOT - Life", "COT - Qualifying")
    - Years breakdown (e.g., "39 years", "TOT: 5, COT: 10, MDRT: 24")

    The exact HTML structure is Elementor-based and needs to be discovered
    on first live run. This parser handles the common patterns.
    """
    from scrapling import Selector

    page = Selector(html, url=page_url)
    agents = []

    # Strategy: find all text blocks that look like agent entries.
    # AIA pages use elementor-widget-wrap containers per agent card.
    # Each card has: name, SP code, tier info, years info.
    #
    # We look for patterns: uppercase name lines, SP- prefixed team codes,
    # and "years" mentions.

    # Try Elementor widget containers first
    cards = page.css(".elementor-widget-wrap")
    if not cards:
        # Fallback: try finding by text pattern
        cards = page.css("article, .entry-content > div")

    for card in cards:
        text_blocks = [t.strip() for t in card.css("::text").getall() if t.strip()]
        if len(text_blocks) < 2:
            continue

        name = None
        team_code = None
        tier = default_tier
        years = None
        awards = []

        for text in text_blocks:
            # Name: all uppercase, at least 2 words, no SP- prefix
            if re.match(r"^[A-Z][A-Z\s\.\-\'\,]{3,}$", text) and "SP-" not in text:
                name = text.strip()
            # SP code
            elif text.startswith("SP-") or text.startswith("sp-"):
                team_code = text.strip()
            # Tier detail
            elif any(t in text for t in ["TOT", "COT", "MDRT"]) and any(
                w in text for w in ["Qualifying", "Life", "-"]
            ):
                awards.append(text.strip())
                # Extract highest tier mentioned
                if "TOT" in text:
                    tier = "TOT"
                elif "COT" in text:
                    tier = "COT"
                elif "MDRT" in text and tier is None:
                    tier = "MDRT"
            # Years
            elif "year" in text.lower():
                match = re.search(r"(\d+)\s*years?", text, re.IGNORECASE)
                if match:
                    years = int(match.group(1))

        if name:
            agents.append(Agent(
                agent_name=name,
                source="aia",
                insurer="AIA",
                team_code=team_code,
                mdrt_status=tier,
                mdrt_years=years,
                awards=awards,
                page_url=page_url,
            ))

    return agents


def parse_directory_page(html: str, page_url: str) -> list[Agent]:
    """Parse the AIA main directory page. Simpler: just names + SP codes."""
    from scrapling import Selector

    page = Selector(html, url=page_url)
    agents = []
    text_blocks = [t.strip() for t in page.css(".entry-content ::text").getall() if t.strip()]

    i = 0
    while i < len(text_blocks):
        text = text_blocks[i]
        # Look for uppercase name pattern
        if re.match(r"^[A-Z][A-Z\s\.\-\'\,]{3,}$", text) and "SP-" not in text:
            name = text.strip()
            team_code = None
            # Check if next text is an SP code
            if i + 1 < len(text_blocks) and text_blocks[i + 1].startswith("SP-"):
                team_code = text_blocks[i + 1].strip()
                i += 1

            agents.append(Agent(
                agent_name=name,
                source="aia",
                insurer="AIA",
                team_code=team_code,
                page_url=page_url,
            ))
        i += 1

    return agents


def scrape_aia() -> int:
    """Scrape all AIA pages. Respects 60s crawl delay."""
    conn = get_db()
    total = 0

    # 1. MDRT tier pages (TOT, COT, MDRT, 1st time, Hall of Fame)
    for base_url, max_pages, tier in MDRT_PAGES:
        urls = build_page_urls(base_url, max_pages)
        for url in urls:
            print(f"[AIA] Fetching: {url}")
            page = Fetcher.get(url, stealthy_headers=True)
            if page.status != 200:
                print(f"[AIA] WARN: Status {page.status} for {url}")
                # If 404, we've hit the end of pagination
                if page.status == 404:
                    print(f"[AIA] End of pagination at {url}")
                    break
                time.sleep(CRAWL_DELAY)
                continue

            agents = parse_mdrt_page(
                page.body.decode(page.encoding or "utf-8"), url, tier
            )
            if agents:
                count = upsert_agents(conn, agents)
                total += count
                print(f"[AIA] Stored {count} agents from {url}")
            else:
                print(f"[AIA] No agents parsed from {url} - check HTML structure")

            time.sleep(CRAWL_DELAY)

    # 2. Top Producer pages
    for url in TOP_PRODUCER_PAGES:
        print(f"[AIA] Fetching top producers: {url}")
        page = Fetcher.get(url, stealthy_headers=True)
        if page.status == 200:
            agents = parse_mdrt_page(
                page.body.decode(page.encoding or "utf-8"), url, None
            )
            if agents:
                count = upsert_agents(conn, agents)
                total += count
                print(f"[AIA] Stored {count} top producers from {url}")
        time.sleep(CRAWL_DELAY)

    # 3. Directory (discover pagination dynamically)
    directory_base = f"{BASE}/directory/"
    page_num = 1
    while True:
        url = directory_base if page_num == 1 else f"{directory_base}page/{page_num}/"
        print(f"[AIA] Fetching directory page {page_num}: {url}")
        page = Fetcher.get(url, stealthy_headers=True)

        if page.status == 404 or page.status != 200:
            print(f"[AIA] Directory pagination ended at page {page_num}")
            break

        agents = parse_directory_page(
            page.body.decode(page.encoding or "utf-8"), url
        )
        if not agents:
            print(f"[AIA] No more agents on directory page {page_num}")
            break

        count = upsert_agents(conn, agents)
        total += count
        print(f"[AIA] Stored {count} agents from directory page {page_num}")
        page_num += 1
        time.sleep(CRAWL_DELAY)

    conn.close()
    print(f"[AIA] Done. Total agents stored: {total}")
    return total


if __name__ == "__main__":
    scrape_aia()
```

### Step 4: Run test to verify it passes

```bash
python -m pytest tests/test_aia.py -v
```

Expected: PASS (the URL builder test)

### Step 5: Do a test run against ONE live page to validate parsing

```bash
cd scrapers/sg-insurance
python -c "
from scrapling.fetchers import Fetcher
page = Fetcher.get('https://aiagency.com.sg/tot/', stealthy_headers=True)
print(f'Status: {page.status}')
print(f'Length: {len(page.body)}')
# Save as fixture for tests
from pathlib import Path
Path('tests/fixtures').mkdir(parents=True, exist_ok=True)
Path('tests/fixtures/aia_tot_page1.html').write_bytes(page.body)
print('Saved fixture')
"
```

Expected: Status 200, HTML saved. Then inspect the HTML to verify our parsing logic matches the actual DOM structure. **Adjust `parse_mdrt_page` if the Elementor structure differs from our assumptions.**

### Step 6: Run full AIA scrape (will take ~60+ minutes due to crawl delay)

```bash
python -m src.scrape_aia
```

Expected: ~1,500-2,000 agents across all pages. **Note:** 75 pages x 60s delay = ~75 minutes minimum runtime.

### Step 7: Commit

```bash
git add scrapers/sg-insurance/src/scrape_aia.py scrapers/sg-insurance/tests/
git commit -m "feat: AIA agency recognition scraper - MDRT, directory, top producers"
```

---

## Task 4: Manulife Scrapers (MAG + FA, ~140 Agents)

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_manulife.py`
- Create: `scrapers/sg-insurance/tests/test_manulife.py`

**Target URLs:**
- MAG: `https://mag.manulife.com.sg/en/awards2024/mdrt.html` (single page, all agents)
- MAG historical: `https://mag.manulife.com.sg/en/awards2023/mdrt.html`
- FA: `https://manulifefa.com.sg/mdrt.html` (1-2 pages)

### Step 1: Write failing test

```python
# scrapers/sg-insurance/tests/test_manulife.py
from src.scrape_manulife import parse_mag_page, parse_fa_page


def test_parse_mag_page_contract():
    """Test that parse_mag_page returns Agent list from HTML string."""
    # Will use live fixture after first run
    pass


def test_parse_fa_page_contract():
    """Test that parse_fa_page returns Agent list from HTML string."""
    pass
```

### Step 2: Run test to verify it fails

```bash
python -m pytest tests/test_manulife.py -v
```

Expected: FAIL with `ModuleNotFoundError`

### Step 3: Implement the Manulife scraper

```python
# scrapers/sg-insurance/src/scrape_manulife.py
"""Scrape Manulife Singapore MDRT recognition pages."""
import time
import re
from scrapling.fetchers import Fetcher
from .models import Agent
from .db import get_db, upsert_agents

MAG_URLS = [
    "https://mag.manulife.com.sg/en/awards2024/mdrt.html",
    # Add historical years as needed:
    # "https://mag.manulife.com.sg/en/awards2023/mdrt.html",
]

FA_URLS = [
    "https://manulifefa.com.sg/mdrt.html",
]


def parse_mag_page(html: str, page_url: str) -> list[Agent]:
    """Parse Manulife Advisory Group MDRT page.

    Expected data per agent: Name, Unit, Group, Tier.
    Format example: "Marcus Xu / Marcus Xu's Unit / Affluence Wealth Advisory / MDRT"
    """
    from scrapling import Selector

    page = Selector(html, url=page_url)
    agents = []

    # MAG page structure: agents listed in sections by tier (TOT, COT, MDRT)
    # Each agent entry typically has name, unit name, group name
    # Try finding text blocks or table rows

    # Strategy 1: Look for structured content sections
    sections = page.css("section, .content-section, .award-section, div")

    # Strategy 2: Find all text and parse agent entries
    all_text = page.css("body").get_all_text() if page.css("body") else ""

    # Look for patterns like: NAME / Unit / Group
    # Split by common delimiters and look for agent patterns
    lines = [line.strip() for line in all_text.split("\n") if line.strip()]

    current_tier = None
    for line in lines:
        # Detect tier headers
        if re.match(r"^(TOT|COT|MDRT)\b", line, re.IGNORECASE):
            tier_match = re.match(r"^(TOT|COT|MDRT)", line, re.IGNORECASE)
            if tier_match:
                current_tier = tier_match.group(1).upper()
            continue

        # Agent lines often have "/" separating name/unit/group
        if "/" in line and len(line) > 5:
            parts = [p.strip() for p in line.split("/")]
            if len(parts) >= 2:
                name = parts[0]
                unit = parts[1] if len(parts) > 1 else None
                group = parts[2] if len(parts) > 2 else None

                # Skip if name looks like a URL or nav element
                if name.startswith("http") or len(name) < 3:
                    continue

                agents.append(Agent(
                    agent_name=name.upper(),
                    source="manulife_mag",
                    insurer="Manulife",
                    team_code=f"{unit} / {group}" if group else unit,
                    mdrt_status=current_tier,
                    page_url=page_url,
                ))

    return agents


def parse_fa_page(html: str, page_url: str) -> list[Agent]:
    """Parse Manulife Financial Advisers MDRT page.

    Similar structure but may differ in HTML layout.
    """
    from scrapling import Selector

    page = Selector(html, url=page_url)
    agents = []
    all_text = page.css("body").get_all_text() if page.css("body") else ""
    lines = [line.strip() for line in all_text.split("\n") if line.strip()]

    current_tier = None
    for line in lines:
        if re.match(r"^(TOT|COT|MDRT)\b", line, re.IGNORECASE):
            tier_match = re.match(r"^(TOT|COT|MDRT)", line, re.IGNORECASE)
            if tier_match:
                current_tier = tier_match.group(1).upper()
            continue

        if "/" in line and len(line) > 5:
            parts = [p.strip() for p in line.split("/")]
            if len(parts) >= 2 and not parts[0].startswith("http") and len(parts[0]) >= 3:
                agents.append(Agent(
                    agent_name=parts[0].upper(),
                    source="manulife_fa",
                    insurer="Manulife",
                    team_code=parts[1] if len(parts) > 1 else None,
                    mdrt_status=current_tier,
                    page_url=page_url,
                ))

    return agents


def scrape_manulife() -> int:
    """Scrape all Manulife pages."""
    conn = get_db()
    total = 0

    for url in MAG_URLS:
        print(f"[Manulife MAG] Fetching: {url}")
        page = Fetcher.get(url, stealthy_headers=True)
        if page.status == 200:
            agents = parse_mag_page(page.body.decode(page.encoding or "utf-8"), url)
            if agents:
                count = upsert_agents(conn, agents)
                total += count
                print(f"[Manulife MAG] Stored {count} agents")
            else:
                print(f"[Manulife MAG] No agents parsed - check HTML structure")
        else:
            print(f"[Manulife MAG] ERROR: Status {page.status}")
        time.sleep(5)

    for url in FA_URLS:
        print(f"[Manulife FA] Fetching: {url}")
        page = Fetcher.get(url, stealthy_headers=True)
        if page.status == 200:
            agents = parse_fa_page(page.body.decode(page.encoding or "utf-8"), url)
            if agents:
                count = upsert_agents(conn, agents)
                total += count
                print(f"[Manulife FA] Stored {count} agents")
            else:
                print(f"[Manulife FA] No agents parsed - check HTML structure")
        else:
            print(f"[Manulife FA] ERROR: Status {page.status}")
        time.sleep(5)

    conn.close()
    print(f"[Manulife] Done. Total agents: {total}")
    return total


if __name__ == "__main__":
    scrape_manulife()
```

### Step 4: Run tests

```bash
python -m pytest tests/test_manulife.py -v
```

### Step 5: Test against live site, save fixtures, refine parser

```bash
python -c "
from scrapling.fetchers import Fetcher
from pathlib import Path
Path('tests/fixtures').mkdir(parents=True, exist_ok=True)

page = Fetcher.get('https://mag.manulife.com.sg/en/awards2024/mdrt.html', stealthy_headers=True)
print(f'MAG Status: {page.status}, Length: {len(page.body)}')
Path('tests/fixtures/manulife_mag_mdrt.html').write_bytes(page.body)

page = Fetcher.get('https://manulifefa.com.sg/mdrt.html', stealthy_headers=True)
print(f'FA Status: {page.status}, Length: {len(page.body)}')
Path('tests/fixtures/manulife_fa_mdrt.html').write_bytes(page.body)
"
```

**Inspect the saved HTML.** Adjust `parse_mag_page` and `parse_fa_page` to match the actual DOM. The "/" delimiter pattern is an assumption from research - the actual HTML may use `<table>`, `<div>`, or other structures.

### Step 6: Run full scrape

```bash
python -m src.scrape_manulife
```

Expected: ~100-140 agents total.

### Step 7: Commit

```bash
git add scrapers/sg-insurance/src/scrape_manulife.py scrapers/sg-insurance/tests/
git commit -m "feat: Manulife MAG + FA MDRT agent scraper"
```

---

## Task 5: FWD Elite Advisers Scraper (~75 Agents)

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_fwd.py`
- Create: `scrapers/sg-insurance/tests/test_fwd.py`

**Notes:** FWD uses React. Content MAY be in initial HTML or may need JS rendering. We'll try `Fetcher` first, fall back to `DynamicFetcher`.

**Target URLs:**
- `https://www.fwd.com.sg/elite-advisers/`
- `https://www.fwd.com.sg/personalised-financial-advice/`

### Step 1: Write test skeleton

```python
# scrapers/sg-insurance/tests/test_fwd.py
from src.scrape_fwd import parse_fwd_page


def test_parse_fwd_contract():
    pass
```

### Step 2: Implement the FWD scraper

```python
# scrapers/sg-insurance/src/scrape_fwd.py
"""Scrape FWD Singapore elite advisers and FA partner pages."""
import time
import re
from scrapling.fetchers import Fetcher, DynamicFetcher
from .models import Agent
from .db import get_db, upsert_agents

URLS = [
    "https://www.fwd.com.sg/elite-advisers/",
    "https://www.fwd.com.sg/personalised-financial-advice/",
]


def parse_fwd_page(html: str, page_url: str) -> list[Agent]:
    """Parse FWD adviser page.

    Expected fields: Name, job title, photo, email, partner firm.
    Partners are grouped by firm in accordion/card components.
    """
    from scrapling import Selector

    page = Selector(html, url=page_url)
    agents = []

    # FWD uses card/accordion components per FA partner firm
    # Each card has adviser name, title, and sometimes email
    # Try multiple CSS strategies

    # Strategy 1: Look for name-like headings inside card containers
    cards = page.css("[class*='adviser'], [class*='partner'], [class*='card']")

    if not cards:
        # Strategy 2: Text-based extraction
        all_text = page.css("main, .content, body").get_all_text() if page.css("main") else ""
        lines = [l.strip() for l in all_text.split("\n") if l.strip()]

        for line in lines:
            # Look for email patterns to identify agent entries
            email_match = re.search(r"[\w\.\-]+@[\w\.\-]+\.\w+", line)
            if email_match:
                # Name is likely on a preceding line
                pass

        return agents

    for card in cards:
        name_el = card.css("h3, h4, [class*='name'], strong")
        title_el = card.css("[class*='title'], [class*='role'], p")
        email_el = card.css("a[href^='mailto:']")

        name = name_el[0].get_all_text(strip=True) if name_el else None
        title = title_el[0].get_all_text(strip=True) if title_el else None
        email = email_el[0].attrib.get("href", "").replace("mailto:", "") if email_el else None

        if name and len(name) > 2:
            agents.append(Agent(
                agent_name=name.upper(),
                source="fwd",
                insurer="FWD",
                role_title=title,
                email=email,
                page_url=page_url,
            ))

    return agents


def scrape_fwd() -> int:
    """Scrape FWD pages. Try HTTP first, fall back to browser."""
    conn = get_db()
    total = 0

    for url in URLS:
        print(f"[FWD] Fetching: {url}")

        # Try simple HTTP first
        page = Fetcher.get(url, stealthy_headers=True)
        agents = []

        if page.status == 200:
            agents = parse_fwd_page(page.body.decode(page.encoding or "utf-8"), url)

        # If no agents found, content likely JS-rendered
        if not agents:
            print(f"[FWD] No agents via HTTP, trying DynamicFetcher...")
            page = DynamicFetcher.fetch(url, headless=True, network_idle=True)
            if page.status == 200:
                agents = parse_fwd_page(
                    page.body.decode(page.encoding or "utf-8"), url
                )

        if agents:
            count = upsert_agents(conn, agents)
            total += count
            print(f"[FWD] Stored {count} agents from {url}")
        else:
            print(f"[FWD] No agents parsed from {url} - needs manual inspection")

        time.sleep(5)

    conn.close()
    print(f"[FWD] Done. Total agents: {total}")
    return total


if __name__ == "__main__":
    scrape_fwd()
```

### Step 3: Test against live site, save fixture, refine parser

```bash
python -c "
from scrapling.fetchers import Fetcher, DynamicFetcher
from pathlib import Path
Path('tests/fixtures').mkdir(parents=True, exist_ok=True)

# Try HTTP first
page = Fetcher.get('https://www.fwd.com.sg/elite-advisers/', stealthy_headers=True)
print(f'HTTP Status: {page.status}, Length: {len(page.body)}')
Path('tests/fixtures/fwd_elite.html').write_bytes(page.body)

# If body is small/empty, try DynamicFetcher
if len(page.body) < 5000:
    page = DynamicFetcher.fetch('https://www.fwd.com.sg/elite-advisers/', headless=True, network_idle=True)
    print(f'Dynamic Status: {page.status}, Length: {len(page.body)}')
    Path('tests/fixtures/fwd_elite_dynamic.html').write_bytes(page.body)
"
```

**Inspect HTML and adjust parser accordingly.**

### Step 4: Run full scrape, commit

```bash
python -m src.scrape_fwd
git add scrapers/sg-insurance/src/scrape_fwd.py scrapers/sg-insurance/tests/
git commit -m "feat: FWD elite advisers scraper"
```

---

## Task 6: Great Eastern Financial Rep Scraper

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_great_eastern.py`
- Create: `scrapers/sg-insurance/tests/test_great_eastern.py`

**Notes:** React SPA ("You need to enable JavaScript to run this app"). MUST use `DynamicFetcher`. Likely fetches data from a REST API under the hood - intercept it if possible.

**Target URL:** `https://www.greateasternlife.com/sg/adviser/financial-representative-listing.html`

### Step 1: Implement Great Eastern scraper

```python
# scrapers/sg-insurance/src/scrape_great_eastern.py
"""Scrape Great Eastern financial representative listing."""
import time
import json
from scrapling.fetchers import DynamicFetcher
from playwright.sync_api import Page
from .models import Agent
from .db import get_db, upsert_agents

URL = "https://www.greateasternlife.com/sg/adviser/financial-representative-listing.html"


def intercept_api(page: Page) -> None:
    """Try to discover the underlying API by intercepting network requests.

    Great Eastern's React app likely calls a REST API to fetch rep data.
    We capture those API responses for direct parsing.
    """
    # This is a discovery step. On first run, inspect browser DevTools
    # Network tab to find the API endpoint.
    # Common patterns: /api/representatives, /api/advisers, GraphQL
    pass


def parse_ge_page(html: str, page_url: str) -> list[Agent]:
    """Parse Great Eastern representative listing from rendered HTML."""
    from scrapling import Selector
    import re

    page = Selector(html, url=page_url)
    agents = []

    # React app renders rep cards after JS execution.
    # Look for common card patterns with name, join date, entity
    cards = page.css(
        "[class*='representative'], [class*='adviser'], "
        "[class*='card'], [class*='profile'], [class*='listing-item']"
    )

    for card in cards:
        name_el = card.css("h3, h4, [class*='name'], strong")
        name = name_el[0].get_all_text(strip=True) if name_el else None

        if name and len(name) > 2:
            # Try to extract additional fields
            text = card.get_all_text(strip=True)
            join_date = None
            date_match = re.search(r"(\d{1,2}\s\w+\s\d{4})", text)
            if date_match:
                join_date = date_match.group(1)

            agents.append(Agent(
                agent_name=name.upper(),
                source="great_eastern",
                insurer="Great Eastern",
                role_title=join_date,  # store join date in role_title for now
                page_url=page_url,
            ))

    return agents


def scrape_great_eastern() -> int:
    """Scrape Great Eastern rep listing using browser rendering."""
    conn = get_db()

    print(f"[GE] Fetching (browser): {URL}")
    page = DynamicFetcher.fetch(
        URL,
        headless=True,
        network_idle=True,
        timeout=60000,
        wait=5000,  # extra 5s for React hydration
    )

    if page.status != 200:
        print(f"[GE] ERROR: Status {page.status}")
        conn.close()
        return 0

    agents = parse_ge_page(page.body.decode(page.encoding or "utf-8"), URL)

    if agents:
        count = upsert_agents(conn, agents)
        print(f"[GE] Stored {count} agents")
    else:
        print("[GE] No agents parsed - inspect rendered HTML")
        # Save debug HTML
        from pathlib import Path
        Path("tests/fixtures").mkdir(parents=True, exist_ok=True)
        Path("tests/fixtures/ge_listing_rendered.html").write_bytes(page.body)
        print("[GE] Saved rendered HTML to tests/fixtures/ge_listing_rendered.html")

    conn.close()
    return len(agents)


if __name__ == "__main__":
    scrape_great_eastern()
```

### Step 2: Test against live site

```bash
python -m src.scrape_great_eastern
```

**This is exploratory.** If no agents parsed, inspect `tests/fixtures/ge_listing_rendered.html` to understand the DOM. The React app may need:
- Scrolling to load more reps (infinite scroll)
- Clicking a "Load More" button
- Interacting with search/filter controls

If so, use `page_action` parameter with DynamicFetcher to automate those interactions.

### Step 3: Commit

```bash
git add scrapers/sg-insurance/src/scrape_great_eastern.py scrapers/sg-insurance/tests/
git commit -m "feat: Great Eastern financial rep listing scraper"
```

---

## Task 7: Prudential Find PRUAdviser Scraper

**Files:**
- Create: `scrapers/sg-insurance/src/scrape_prudential.py`

**Notes:** Dynamic search form with no browsable directory. We need to try searching with common names or explore if the form accepts empty/wildcard searches. May use `StealthyFetcher` if Prudential has bot protection.

**Target URL:** `https://www.prudential.com.sg/find-pruadviser`

### Step 1: Implement Prudential scraper (discovery-first approach)

```python
# scrapers/sg-insurance/src/scrape_prudential.py
"""Scrape Prudential Singapore PRUAdviser search.

This is a DISCOVERY scraper. The search form requires input.
Strategy: submit common Singapore surnames to discover advisers.
"""
import time
from scrapling.fetchers import DynamicFetcher, StealthyFetcher
from playwright.sync_api import Page
from .models import Agent
from .db import get_db, upsert_agents

URL = "https://www.prudential.com.sg/find-pruadviser"

# Common Singapore surnames to search (covers majority of population)
SEARCH_TERMS = [
    "Tan", "Lim", "Lee", "Ng", "Ong", "Wong", "Goh", "Chua", "Chan",
    "Koh", "Teo", "Ang", "Yeo", "Ho", "Sim", "Tay", "Loh", "Low",
    "Wee", "Seah", "Chong", "Yap", "Cheong", "Phua", "Soh", "Quek",
    "Foo", "Leong", "Chen", "Mohamed", "Ahmad", "Ali", "Kumar", "Singh",
]


def search_pruadviser(search_term: str) -> list[Agent]:
    """Search Prudential's Find PRUAdviser form with a name."""

    def fill_and_search(page: Page):
        # Wait for search form to render
        page.wait_for_selector("input[type='text'], input[name*='search'], input[placeholder*='search']",
                               timeout=10000)
        # Find and fill the search input
        search_input = page.query_selector(
            "input[type='text'], input[name*='search'], input[placeholder*='search']"
        )
        if search_input:
            search_input.fill(search_term)
            # Try clicking search button
            search_btn = page.query_selector(
                "button[type='submit'], button:has-text('Search'), "
                "button:has-text('Find'), input[type='submit']"
            )
            if search_btn:
                search_btn.click()
            else:
                search_input.press("Enter")
            # Wait for results
            page.wait_for_timeout(3000)

    result = DynamicFetcher.fetch(
        URL,
        headless=True,
        network_idle=True,
        page_action=fill_and_search,
        timeout=30000,
    )

    agents = []
    if result.status == 200:
        from scrapling import Selector
        page = Selector(result.body.decode(result.encoding or "utf-8"), url=URL)

        # Parse result cards - structure unknown, discover on first run
        cards = page.css(
            "[class*='adviser'], [class*='result'], [class*='card'], "
            "[class*='profile'], [class*='listing']"
        )
        for card in cards:
            name_el = card.css("h3, h4, [class*='name'], strong, a")
            name = name_el[0].get_all_text(strip=True) if name_el else None
            if name and len(name) > 2:
                agents.append(Agent(
                    agent_name=name.upper(),
                    source="prudential",
                    insurer="Prudential",
                    page_url=URL,
                ))

    return agents


def scrape_prudential() -> int:
    """Search Prudential with common surnames to discover advisers."""
    conn = get_db()
    total = 0

    for term in SEARCH_TERMS:
        print(f"[Prudential] Searching: '{term}'")
        try:
            agents = search_pruadviser(term)
            if agents:
                count = upsert_agents(conn, agents)
                total += count
                print(f"[Prudential] Found {count} agents for '{term}'")
            else:
                print(f"[Prudential] No results for '{term}'")
        except Exception as e:
            print(f"[Prudential] ERROR for '{term}': {e}")

        time.sleep(10)  # polite delay

    conn.close()
    print(f"[Prudential] Done. Total unique agents: {total}")
    return total


if __name__ == "__main__":
    scrape_prudential()
```

### Step 2: Discovery run with single search term

```bash
python -c "
from src.scrape_prudential import search_pruadviser
agents = search_pruadviser('Tan')
print(f'Found {len(agents)} agents')
for a in agents[:5]:
    print(f'  {a.agent_name}')
"
```

**This will likely need iteration.** The search form structure is unknown. After the first run, inspect what the rendered page looks like and adjust selectors.

### Step 3: Run full scrape, commit

```bash
python -m src.scrape_prudential
git add scrapers/sg-insurance/src/scrape_prudential.py
git commit -m "feat: Prudential PRUAdviser search scraper"
```

---

## Task 8: MAS FIRR Verification (Enrichment Pass)

**Files:**
- Create: `scrapers/sg-insurance/src/verify_mas_firr.py`
- Create: `scrapers/sg-insurance/tests/test_mas_firr.py`

**Notes:** This is a VERIFICATION pass, not a discovery scraper. We take agent names already in our DB and look them up on MAS FIRR to get their representative numbers and confirm registration status. The FIRR is a JS SPA with a mandatory checkbox.

**Target URL:** `https://eservices.mas.gov.sg/rr`

### Step 1: Implement FIRR verification scraper

```python
# scrapers/sg-insurance/src/verify_mas_firr.py
"""Verify agents against MAS Financial Institution Representatives Register.

Takes agent names from our SQLite DB, searches FIRR one-by-one,
and updates records with MAS representative numbers.
"""
import time
from scrapling.fetchers import DynamicFetcher
from playwright.sync_api import Page
from .db import get_db

URL = "https://eservices.mas.gov.sg/rr"
DELAY_BETWEEN_SEARCHES = 5  # seconds


def search_firr(agent_name: str) -> dict | None:
    """Search MAS FIRR for a representative by name.

    Returns dict with rep_number, name, company if found. None otherwise.
    """

    def fill_and_search(page: Page):
        # Wait for the form to load (JS SPA)
        page.wait_for_selector("input[type='text']", timeout=15000)

        # Fill the search field
        search_input = page.query_selector("input[type='text']")
        if search_input:
            search_input.fill(agent_name)

        # Click the mandatory checkbox
        checkbox = page.query_selector("input[type='checkbox']")
        if checkbox:
            checkbox.click()

        # Click search button
        search_btn = page.query_selector(
            "button:has-text('Search'), input[type='submit'], "
            "button[type='submit'], .btn-search"
        )
        if search_btn:
            search_btn.click()

        # Wait for results
        page.wait_for_timeout(3000)

    result = DynamicFetcher.fetch(
        URL,
        headless=True,
        network_idle=True,
        page_action=fill_and_search,
        timeout=30000,
    )

    if result.status != 200:
        return None

    from scrapling import Selector
    page = Selector(result.body.decode(result.encoding or "utf-8"), url=URL)

    # Parse results table
    rows = page.css("table tr, [class*='result'] tr")
    for row in rows:
        cells = row.css("td")
        if len(cells) >= 3:
            return {
                "rep_number": cells[1].get_all_text(strip=True) if len(cells) > 1 else None,
                "name": cells[2].get_all_text(strip=True) if len(cells) > 2 else None,
                "company": cells[3].get_all_text(strip=True) if len(cells) > 3 else None,
            }

    # Check for "No record found"
    no_record = page.find_by_text("No record found", partial=True)
    if no_record:
        return None

    return None


def verify_agents(limit: int = 50) -> int:
    """Look up unverified agents in MAS FIRR and update DB."""
    conn = get_db()

    # Get agents without MAS rep numbers
    rows = conn.execute(
        "SELECT id, agent_name FROM agents WHERE mas_rep_number IS NULL LIMIT ?",
        (limit,),
    ).fetchall()

    print(f"[FIRR] {len(rows)} agents to verify")
    verified = 0

    for agent_id, agent_name in rows:
        print(f"[FIRR] Searching: {agent_name}")
        try:
            result = search_firr(agent_name)
            if result and result.get("rep_number"):
                conn.execute(
                    "UPDATE agents SET mas_rep_number=?, mas_reg_status='Appointed' WHERE id=?",
                    (result["rep_number"], agent_id),
                )
                conn.commit()
                verified += 1
                print(f"[FIRR] Verified: {agent_name} -> {result['rep_number']}")
            else:
                # Mark as searched but not found
                conn.execute(
                    "UPDATE agents SET mas_reg_status='Not Found' WHERE id=?",
                    (agent_id,),
                )
                conn.commit()
                print(f"[FIRR] Not found: {agent_name}")
        except Exception as e:
            print(f"[FIRR] ERROR for {agent_name}: {e}")

        time.sleep(DELAY_BETWEEN_SEARCHES)

    conn.close()
    print(f"[FIRR] Done. Verified {verified}/{len(rows)} agents")
    return verified


if __name__ == "__main__":
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    verify_agents(limit)
```

### Step 2: Test with a single known agent name

```bash
python -c "
from src.verify_mas_firr import search_firr
result = search_firr('Kevin Goh')
print(result)
"
```

**Inspect results.** The FIRR SPA structure needs to be verified. Adjust selectors based on actual DOM.

### Step 3: Run batch verification (start with 10 to test)

```bash
python -m src.verify_mas_firr 10
```

### Step 4: Commit

```bash
git add scrapers/sg-insurance/src/verify_mas_firr.py scrapers/sg-insurance/tests/
git commit -m "feat: MAS FIRR agent verification pass"
```

---

## Task 9: Main Pipeline Runner & CSV Export

**Files:**
- Create: `scrapers/sg-insurance/src/run_all.py`
- Modify: `scrapers/sg-insurance/src/db.py` (add summary stats function)

### Step 1: Create the pipeline runner

```python
# scrapers/sg-insurance/src/run_all.py
"""Main pipeline: run all scrapers in sequence and export results."""
import time
from pathlib import Path
from .db import get_db, export_csv, get_agent_count, get_agents_by_source


def run_pipeline(skip_verification: bool = False):
    """Run the full scraping pipeline."""
    print("=" * 60)
    print("SINGAPORE INSURANCE AGENT SCRAPER PIPELINE")
    print("=" * 60)

    # Phase 1: Firms (fast, <1 min)
    print("\n--- Phase 1: MAS FID Firms ---")
    from .scrape_mas_fid import scrape_fid
    fid_count = scrape_fid()
    print(f"Phase 1 complete: {fid_count} firms\n")

    # Phase 2: AIA (slow, ~75 min due to 60s crawl delay)
    print("\n--- Phase 2: AIA Agents ---")
    from .scrape_aia import scrape_aia
    aia_count = scrape_aia()
    print(f"Phase 2 complete: {aia_count} AIA agents\n")

    # Phase 3: Manulife (fast, <1 min)
    print("\n--- Phase 3: Manulife Agents ---")
    from .scrape_manulife import scrape_manulife
    manulife_count = scrape_manulife()
    print(f"Phase 3 complete: {manulife_count} Manulife agents\n")

    # Phase 4: FWD (medium, <5 min)
    print("\n--- Phase 4: FWD Agents ---")
    from .scrape_fwd import scrape_fwd
    fwd_count = scrape_fwd()
    print(f"Phase 4 complete: {fwd_count} FWD agents\n")

    # Phase 5: Great Eastern (medium, ~5 min)
    print("\n--- Phase 5: Great Eastern Agents ---")
    from .scrape_great_eastern import scrape_great_eastern
    ge_count = scrape_great_eastern()
    print(f"Phase 5 complete: {ge_count} Great Eastern agents\n")

    # Phase 6: Prudential (slow, ~10 min)
    print("\n--- Phase 6: Prudential Agents ---")
    from .scrape_prudential import scrape_prudential
    pru_count = scrape_prudential()
    print(f"Phase 6 complete: {pru_count} Prudential agents\n")

    # Phase 7: MAS FIRR Verification (optional, slow)
    if not skip_verification:
        print("\n--- Phase 7: MAS FIRR Verification ---")
        from .verify_mas_firr import verify_agents
        verified = verify_agents(limit=100)
        print(f"Phase 7 complete: {verified} agents verified\n")

    # Export
    print("\n--- Export ---")
    conn = get_db()
    output_dir = Path(__file__).parent.parent / "output"
    csv_path = output_dir / "sg_insurance_agents.csv"
    row_count = export_csv(conn, csv_path)

    # Summary
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(f"Total agents in DB: {get_agent_count(conn)}")
    print(f"By source:")
    for source, count in sorted(get_agents_by_source(conn).items()):
        print(f"  {source}: {count}")
    print(f"\nExported {row_count} rows to {csv_path}")
    conn.close()


if __name__ == "__main__":
    import sys
    skip_verify = "--skip-verify" in sys.argv
    run_pipeline(skip_verification=skip_verify)
```

### Step 2: Test the pipeline runner (with a quick smoke test)

```bash
# Quick test: just run FID + Manulife (fast ones)
python -c "
from src.scrape_mas_fid import scrape_fid
from src.scrape_manulife import scrape_manulife
from src.db import get_db, export_csv, get_agent_count
from pathlib import Path

scrape_fid()
scrape_manulife()

conn = get_db()
print(f'Total agents: {get_agent_count(conn)}')
export_csv(conn, Path('output/test_export.csv'))
conn.close()
"
```

### Step 3: Run the full pipeline

```bash
cd scrapers/sg-insurance
python -m src.run_all --skip-verify
```

Expected runtime: ~90 minutes (dominated by AIA's 60s crawl delay across ~75 pages).

### Step 4: Commit

```bash
git add scrapers/sg-insurance/src/run_all.py
git commit -m "feat: full pipeline runner with CSV export"
```

---

## Task 10: Parser Refinement Pass (Post-Discovery)

**Files:**
- Modify: All `scrape_*.py` files as needed
- Modify: All `test_*.py` files with real fixtures

**This task happens AFTER running each scraper at least once against the live sites.**

### Step 1: For each scraper that returned 0 agents, inspect the saved fixture HTML

```bash
# List all saved fixtures
ls -la tests/fixtures/

# Open each in browser to inspect DOM structure
open tests/fixtures/aia_tot_page1.html
open tests/fixtures/manulife_mag_mdrt.html
open tests/fixtures/fwd_elite.html
open tests/fixtures/ge_listing_rendered.html
```

### Step 2: Update CSS selectors / parsing logic in each scraper to match actual DOM

For each scraper:
1. Open the fixture HTML in a browser
2. Use browser DevTools to identify the correct CSS selectors for agent name, team, tier, etc.
3. Update the `parse_*` function
4. Write a proper test using the saved fixture
5. Run the test
6. Re-run the scraper against the live site
7. Verify agent count is reasonable

### Step 3: Write fixture-based tests for each working parser

```python
# Example: update tests/test_aia.py with real fixture
def test_parse_mdrt_page_with_fixture():
    fixture = Path("tests/fixtures/aia_tot_page1.html")
    if not fixture.exists():
        pytest.skip("No fixture - run scraper first")
    html = fixture.read_text()
    agents = parse_mdrt_page(html, "https://aiagency.com.sg/tot/", "TOT")
    assert len(agents) > 0, "Should parse at least 1 agent from TOT page"
    assert all(a.insurer == "AIA" for a in agents)
    assert all(a.mdrt_status == "TOT" for a in agents)
```

### Step 4: Run full test suite

```bash
python -m pytest tests/ -v
```

### Step 5: Commit

```bash
git add scrapers/sg-insurance/
git commit -m "fix: refine parsers based on live site HTML structure"
```

---

## Relevant Files Summary

| File | Purpose |
|------|---------|
| `scrapers/sg-insurance/pyproject.toml` | Project config + dependencies |
| `scrapers/sg-insurance/src/__init__.py` | Package init |
| `scrapers/sg-insurance/src/models.py` | Agent dataclass |
| `scrapers/sg-insurance/src/db.py` | SQLite DB setup, upsert, export |
| `scrapers/sg-insurance/src/scrape_mas_fid.py` | MAS FID firm scraper |
| `scrapers/sg-insurance/src/scrape_aia.py` | AIA recognition pages scraper |
| `scrapers/sg-insurance/src/scrape_manulife.py` | Manulife MAG + FA scraper |
| `scrapers/sg-insurance/src/scrape_fwd.py` | FWD elite advisers scraper |
| `scrapers/sg-insurance/src/scrape_great_eastern.py` | Great Eastern rep listing scraper |
| `scrapers/sg-insurance/src/scrape_prudential.py` | Prudential PRUAdviser search scraper |
| `scrapers/sg-insurance/src/verify_mas_firr.py` | MAS FIRR verification pass |
| `scrapers/sg-insurance/src/run_all.py` | Full pipeline runner |
| `scrapers/sg-insurance/tests/test_db.py` | DB module tests |
| `scrapers/sg-insurance/tests/test_aia.py` | AIA parser tests |
| `scrapers/sg-insurance/tests/test_manulife.py` | Manulife parser tests |
| `scrapers/sg-insurance/tests/test_fwd.py` | FWD parser tests |
| `scrapers/sg-insurance/tests/test_mas_fid.py` | MAS FID parser tests |
| `scrapers/sg-insurance/tests/test_mas_firr.py` | FIRR verification tests |
| `scrapers/sg-insurance/tests/fixtures/` | Saved HTML fixtures from live sites |
| `scrapers/sg-insurance/output/agents.db` | SQLite database (generated) |
| `scrapers/sg-insurance/output/sg_insurance_agents.csv` | Final CSV export (generated) |

---

## Estimated Yield

| Source | Est. Agents | Data Richness |
|--------|------------|---------------|
| AIA | ~1,500-2,000 | Name, SP code, MDRT tier, years, awards |
| Manulife MAG | ~80-100 | Name, unit, group, MDRT tier |
| Manulife FA | ~20-40 | Name, team, MDRT tier |
| FWD | ~75 | Name, title, email, partner firm |
| Great Eastern | Unknown (50-500?) | Name, join date |
| Prudential | Unknown (100-1,000?) | Name |
| **Total** | **~2,000-3,500+** | |

## Estimated Runtime

| Phase | Time |
|-------|------|
| Setup | 5 min |
| MAS FID | 1 min |
| AIA (75 pages x 60s delay) | ~75 min |
| Manulife | 1 min |
| FWD | 2 min |
| Great Eastern | 5 min |
| Prudential (35 searches x 10s) | 6 min |
| MAS FIRR verification (100 agents x 5s) | 8 min |
| **Total** | **~100 min** |

---

## Notes

1. **Parser refinement is expected.** The CSS selectors in Tasks 3-7 are educated guesses based on research. After the first live run, each parser will likely need adjustments. Task 10 handles this.

2. **AIA dominates runtime.** Their `crawl-delay: 60` in robots.txt means ~75 minutes just for AIA. Consider running AIA separately: `python -m src.scrape_aia`.

3. **Scrapling escalation pattern.** We try `Fetcher` (HTTP only) first for speed. Only escalate to `DynamicFetcher` (browser) when content is JS-rendered. Only use `StealthyFetcher` if anti-bot is detected.

4. **Deduplication.** The UNIQUE constraint on `(agent_name, insurer, source)` prevents duplicates within a source. An agent appearing on both AIA MDRT and AIA directory will be upserted (MDRT data wins since it has richer fields).

5. **MAS FIRR is rate-limited by design.** It opens a new browser per search. For full DB verification, run in batches: `python -m src.verify_mas_firr 50` over multiple sessions.
