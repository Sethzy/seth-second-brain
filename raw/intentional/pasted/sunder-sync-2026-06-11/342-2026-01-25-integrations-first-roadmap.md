---
type: raw_capture
source_type: web
title: "Sunder sync: 2026-01-25-integrations-first-roadmap.md"
url: "https://clawd.bot/"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-25-integrations-first-roadmap.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-01-25-integrations-first-roadmap.md"
sha256: "fac8feb82b96a5e24d219d344d9e32e7b7ca03e0f2aa8f73fdc8ff171840faff"
duplicate_of: ""
---

# Sunder sync: 2026-01-25-integrations-first-roadmap.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-25-integrations-first-roadmap.md`

Primary URL: https://clawd.bot/

Duplicate of existing source-map entry: `none`

## Capture Text

# Integrations-First Roadmap: PRD Draft

**Date:** 2026-01-25
**Status:** Draft
**Author:** Claude + Seth

---

## The Clawdbot Insight

People love Clawdbot because **the agent has access to all the tools and autonomously calls them**. It just works.

Key patterns from Clawdbot:
- 50+ integrations (WhatsApp, Slack, Gmail, GitHub, Spotify, Obsidian, etc.)
- Full system access: file read/write, shell commands, browser control
- Persistent memory across 24/7 operations
- Feels like "a smart model with eyes and hands"
- User describes it as "the endgame of digital employees"

**Core realization:** The magic isn't in the AI model itself - it's in the **tool access** that makes it useful.

---

## Current State: Sunder

Sunder today:
- Users upload documents manually
- AI processes (Gemini triage + ExtendAI extraction)
- Users review extractions
- Users generate reports

**The friction:** Users still have to:
1. Manually collect documents from various sources
2. Upload them to Sunder
3. Download reports and put them somewhere else
4. Copy data to spreadsheets, email, etc.

---

## Vision: Sunder as an Agentic Document Orchestrator

```
Today:
  User uploads docs → AI processes → User downloads reports

Tomorrow:
  AI pulls from user's sources → AI processes → AI pushes to user's destinations
```

### The Pitch

"Give Sunder access to where your documents live and where your outputs need to go. The AI handles everything in between."

---

## Integration Categories

### 1. Document Sources (Ingest)

Where documents come from:

| Integration | Use Case |
|-------------|----------|
| **Gmail/Outlook** | Auto-ingest email attachments (receipts, invoices, reports) |
| **Google Drive/OneDrive** | Watch folders for new documents |
| **Dropbox** | Sync document folders |
| **Slack/Teams** | Pull documents from channels |
| **WhatsApp Business** | Receive documents via chat |
| **Web scrapers** | Pull from portals (insurance portals, vendor sites) |
| **API webhooks** | Receive from other systems |

### 2. Data Destinations (Export)

Where outputs go:

| Integration | Use Case |
|-------------|----------|
| **Google Sheets/Excel Online** | Auto-populate extraction data |
| **Notion/Coda** | Push structured data to databases |
| **Slack/Teams** | Notify when processing complete |
| **Email** | Send generated reports |
| **Airtable** | Sync to project databases |
| **QuickBooks/Xero** | Push financial data |
| **CRM (HubSpot, Salesforce)** | Attach to contacts/deals |
| **Custom webhooks** | Push to any system |

### 3. Knowledge Sources (Context)

Where the AI gets domain knowledge:

| Integration | Use Case |
|-------------|----------|
| **Notion/Confluence** | Company SOPs, templates, guidelines |
| **Google Docs** | Reference documents |
| **Internal wikis** | Domain-specific knowledge |
| **Previous cases** | Learn from historical data |

---

## Architecture Concept

```
┌─────────────────────────────────────────────────────────────┐
│                     SUNDER AGENT                            │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Sources   │  │  Processing │  │    Destinations     │ │
│  │             │  │             │  │                     │ │
│  │  Gmail      │  │  Gemini     │  │  Google Sheets     │ │
│  │  Drive      │──│  ExtendAI   │──│  Slack notifications│ │
│  │  Dropbox    │  │  Claude     │  │  Email reports      │ │
│  │  Slack      │  │             │  │  Webhooks           │ │
│  │  WhatsApp   │  │             │  │  CRM                │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│                                                             │
│              ┌───────────────────────┐                      │
│              │   User Instructions   │                      │
│              │   "When I receive an  │                      │
│              │   invoice from X,     │                      │
│              │   extract and push    │                      │
│              │   to Sheet Y"         │                      │
│              └───────────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation Approach

### Phase 1: Foundation (Auth + Basic Integrations)

**Goal:** Prove the model works with 2-3 key integrations

1. **OAuth infrastructure**
   - Google OAuth (Gmail, Drive, Sheets)
   - Supabase to store tokens securely
   - Token refresh handling

2. **Gmail Integration (Source)**
   - Watch for new emails with attachments
   - Filter by sender/subject rules
   - Auto-create cases from email threads

3. **Google Sheets Integration (Destination)**
   - Export extraction data to specified sheet
   - Append mode (add rows) or sync mode (update)
   - Column mapping configuration

4. **Slack Integration (Notifications)**
   - Send completion notifications
   - Include summary + link to case

### Phase 2: Automation Layer

**Goal:** Let users define rules/triggers

1. **Automation Rules Engine**
   ```
   WHEN: New email from *@insurance.com with attachment
   THEN:
     - Create case with subject as name
     - Process documents
     - Push extractions to "Claims" sheet
     - Notify #claims-team on Slack
   ```

2. **Rule Builder UI**
   - Trigger selection (source + conditions)
   - Action selection (processing + destinations)
   - Test/preview before activating

3. **Execution Logs**
   - Track what ran, when, results
   - Error handling and retry

### Phase 3: More Integrations

Based on user demand, add:
- Microsoft ecosystem (Outlook, OneDrive, Teams, Excel Online)
- Dropbox
- WhatsApp Business API
- Notion
- Airtable
- Custom webhooks

### Phase 4: Agentic Chat Actions

Let the AI Analyst trigger actions:

> User: "Send this month's medical expenses summary to accounting@company.com"
>
> AI: "I've generated the summary and sent it to accounting@company.com. They should receive it shortly."

Tool capabilities:
- `send_email(to, subject, body, attachments)`
- `update_sheet(sheet_id, data)`
- `send_slack_message(channel, message)`
- `create_notion_page(database_id, properties)`

---

## Why This Wins

### For Users
- **Zero manual document collection** - documents flow in automatically
- **Zero manual data entry** - extractions push to where they're needed
- **Zero context switching** - stay in Slack/email, Sunder works in background
- **Feels like having a document assistant** - not another tool to manage

### For Sunder Business
- **Stickiness** - more integrations = harder to leave
- **Usage growth** - automations run 24/7, not just when user is active
- **Enterprise appeal** - IT loves OAuth, audit logs, automation
- **Platform potential** - users can "vibe" their own document workflows

---

## Open Questions

1. **Pricing model for integrations?**
   - Per-integration fee?
   - Usage-based (documents processed)?
   - Tier-based (Starter: 3 integrations, Pro: unlimited)?

2. **Security/compliance?**
   - SOC 2 requirements for enterprise
   - Data residency concerns
   - Audit logging requirements

3. **Which integrations first?**
   - Survey existing users?
   - Google ecosystem seems most universal

4. **Build vs. buy?**
   - Nango/Merge/Paragon for managed OAuth?
   - Or build native integrations?

5. **How deep do automations go?**
   - Simple rules first (IFTTT-style)?
   - Or jump to full agentic (let AI decide)?

---

## Next Steps

1. [ ] Validate with 3-5 existing users - would they use this?
2. [ ] Research: Nango vs Merge vs building native
3. [ ] Prototype: Gmail → Sunder → Sheets flow
4. [ ] Define MVP scope for Phase 1

---

## References

- [Clawdbot](https://clawd.bot/) - Inspiration for integrations-first approach
- [Nango](https://www.nango.dev/) - Managed OAuth infrastructure
- [Merge](https://merge.dev/) - Unified API for integrations
- [Paragon](https://www.useparagon.com/) - Embedded integration platform

