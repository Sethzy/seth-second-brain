---
type: raw_capture
source_type: x
title: "Sunder sync: SKILL.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-domain-buyer/SKILL.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-domain-buyer/SKILL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-domain-buyer/SKILL.md"
sha256: "8af532b9184d6b6bd382ac317202be5e3dce95ae78abb8f77cbecedf334a4872"
duplicate_of: ""
---

# Sunder sync: SKILL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-domain-buyer/SKILL.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-domain-buyer/SKILL.md

Duplicate of existing source-map entry: `none`

## Capture Text

---
name: sales-domain-buyer
description: Buy domains and set up cold email inboxes end-to-end. Automates Namecheap purchase, Google Workspace setup, DNS configuration, and email signatures. Use when user says "buy domains", "domain buyer", "set up domain", "new outreach domain".
---

# Sales Domain Buyer

Automates the full pipeline: keyword → domain names → purchase → Google Workspace → DNS → email signatures.

## Quick Start

```bash
SCRIPTS=".claude/skills/sales-domain-buyer/scripts"

# 1. Generate + check availability
python3 $SCRIPTS/phase1_generate_domains.py --keywords "sunder consulting" --tlds "com,co"

# 2. Approve domains
python3 $SCRIPTS/phase1_generate_domains.py --approve "getsunder.com,trysunder.co"

# 3. Purchase
python3 $SCRIPTS/phase2_purchase_domains.py          # or --dry-run

# 4. Google Workspace (add domain + create email + get DKIM)
python3 $SCRIPTS/phase3_google_workspace.py --headed  # use --headed first time

# 5. DNS (MX, SPF, DKIM, DMARC)
python3 $SCRIPTS/phase4_dns_configure.py              # or --dry-run

# 6. Verify DNS propagation (wait 15-60 min after step 5)
python3 $SCRIPTS/phase4_dns_configure.py --verify

# 7. Set up email signatures
python3 $SCRIPTS/phase5_signatures.py --setup
python3 $SCRIPTS/phase5_signatures.py --assign "seth@getsunder.com" \
  --template default --vars '{"name":"Seth Lim","title":"Co-founder"}'
```

## Pipeline Overview

```
Keywords → Generate Names → Check Availability → User Approves
    → Purchase (Namecheap API)
    → Add to Google Workspace (Playwright)
    → Configure DNS (Namecheap API)
    → Assign Signatures (JSON)
    → Ready for Outreach
```

## Domain Status Flow

```
suggested → approved → purchased → workspace_added → dns_configured → ready
```

## Phase Details

### Phase 1: Generate + Check (`phase1_generate_domains.py`)

| Flag | Description |
|------|-------------|
| `--keywords "word1 word2"` | Space-separated keywords (required) |
| `--tlds "com,co,io"` | Comma-separated TLDs (default: com,co,io) |
| `--prefixes-only` | Only generate prefix variations |
| `--suffixes-only` | Only generate suffix variations |
| `--max-check 50` | Limit domains to check (default: 50) |
| `--approve "d1.com,d2.co"` | Approve specific domains |
| `--approve-all` | Approve all suggested domains |

**Prefixes:** get, try, use, go, hey, with, meet, join
**Suffixes:** hq, mail, ai, app, team, labs, works

### Phase 2: Purchase (`phase2_purchase_domains.py`)

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview without spending money |
| `--domain "x.com"` | Purchase a specific domain |

### Phase 3: Google Workspace (`phase3_google_workspace.py`)

| Flag | Description |
|------|-------------|
| `--headed` | Visible browser (use for first run / debugging) |
| `--domain "x.com"` | Process specific domain |
| `--email "seth"` | Email username (default: seth) |
| `--name "Seth Lim"` | Full name for account |

**What it does:**
1. Adds domain as secondary domain in Google Admin
2. Creates email account (e.g. seth@domain.com)
3. Generates DKIM record, saves public key to DB

**If Playwright breaks:** Use `agent-browser` MCP interactively as fallback.

### Phase 4: DNS (`phase4_dns_configure.py`)

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview DNS changes without applying |
| `--domain "x.com"` | Configure specific domain |
| `--verify` | Check DNS propagation via dig |

**Records set:** MX, SPF, DKIM, DMARC (see `references/dns-records.md`)

**Critical:** Always reads existing records first, merges, then sets. Namecheap `setHosts` replaces ALL records.

### Phase 5: Signatures (`phase5_signatures.py`)

| Flag | Description |
|------|-------------|
| `--setup` | Create default template |
| `--list-templates` | Show all templates |
| `--add-template NAME` | Create new template |
| `--delete-template NAME` | Remove template |
| `--assign EMAIL` | Assign template to email |
| `--template NAME` | Template name for assignment |
| `--vars '{...}'` | JSON variables for assignment |
| `--render EMAIL` | Preview rendered signature |
| `--render-all` | Preview all signatures |

**Template variables:** `{{name}}`, `{{title}}`, `{{company}}`, `{{phone}}`, `{{email}}`, `{{website}}`

## Environment Variables

```bash
# Namecheap API
NAMECHEAP_API_USER=xxx
NAMECHEAP_API_KEY=xxx
NAMECHEAP_CLIENT_IP=xxx        # Your public IP (whitelisted in Namecheap)
NAMECHEAP_SANDBOX=false        # true for testing

# Registrant Contact (for domain purchase)
REGISTRANT_FIRST_NAME=Seth
REGISTRANT_LAST_NAME=Lim
REGISTRANT_ADDRESS=xxx
REGISTRANT_CITY=Singapore
REGISTRANT_STATE=Singapore
REGISTRANT_ZIP=xxx
REGISTRANT_COUNTRY=SG
REGISTRANT_PHONE=+65.xxx
REGISTRANT_EMAIL=xxx

# Google Workspace Admin
GOOGLE_WORKSPACE_ADMIN_EMAIL=xxx
GOOGLE_WORKSPACE_ADMIN_PASSWORD=xxx
DEFAULT_EMAIL_PASSWORD=xxx
```

## Dependencies

```bash
pip install PyNamecheap playwright python-dotenv
playwright install chromium
```

## Data Files

| File | Purpose |
|------|---------|
| `data/domains-db.json` | Domain tracking (status, purchase info, workspace, DNS) |
| `data/signatures-db.json` | Signature templates + email assignments |
| `screenshots/` | Error screenshots from Playwright (auto-created) |

## Long-Running Scripts

**Run these via Bash tool with `run_in_background: true`:**

| Script | Why |
|--------|-----|
| `phase1_generate_domains.py` | Checks many domains via API |
| `phase3_google_workspace.py` | Browser automation, multi-step |

**Command template:**
```bash
cd "/Users/sethlim/Documents/Sunder Workspace" && python3 .claude/skills/sales-domain-buyer/scripts/SCRIPT.py ARGS 2>&1
```

**Progress check:**
```bash
tail -20 {output_file_path}
```

## Testing Checklist

- [ ] Phase 1: `--keywords "test" --tlds "xyz"` → shows available cheap domains
- [ ] Phase 2: `--dry-run` → logs what would be purchased
- [ ] Phase 3: `--headed` → visually verify Google Admin navigation
- [ ] Phase 4: `--dry-run` then `--verify` → confirm DNS records
- [ ] Phase 5: `--setup`, assign, render → verify JSON output
- [ ] End-to-end: Buy cheap `.xyz` ($1), full pipeline, verify email works
