---
type: raw_capture
source_type: web
title: "Sunder sync: openclaw-agentmail-email-for-agents.md"
url: "https://www.agentmail.to"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-agentmail-email-for-agents.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/openclaw-agentmail-email-for-agents.md"
sha256: "192ebe43c32c8a3485c902583c44855071a80b8a8864176cc1132daaede3af15"
duplicate_of: ""
---

# Sunder sync: openclaw-agentmail-email-for-agents.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-agentmail-email-for-agents.md`

Primary URL: https://www.agentmail.to

Duplicate of existing source-map entry: `none`

## Capture Text

# AgentMail - Email Inboxes for AI Agents

**URL:** https://www.agentmail.to
**Type:** Product page (YC-backed)
**Tags:** openclaw, email, agent-infrastructure, api, MCP

---

## What it is

AgentMail is the email inbox API for AI agents. It gives agents their own email inboxes, like Gmail does for humans. API-first email platform for two-way conversations.

**Not** AI for your email. It's **email for your AI**.

## Key Features

- **Inboxes API** — Create, manage, and operate email inboxes entirely via API
- **Threads + replies** — Two-way conversation support
- **Attachments** — Parse invoices, receipts, attachments automatically
- **Realtime events** — Webhooks
- **Custom domains** — Use your own domain
- **SDKs + MCP** — Python, TypeScript, cURL
- **Semantic search** — Search through email content
- **Data extraction** — Extract structured data from emails

## Use Cases

1. **Browser Agents** — Extract 2FA/OTP codes from email for signup flows
2. **Scheduling Executive Assistant** — Manage calendar, schedule meetings, send summaries
3. **Doc Processing** — Parse invoices, receipts, attachments automatically
4. **Customer Service** — Smart routing, ingest support emails

## Quick Start

```python
from agentmail import AgentMail

client = AgentMail()
inbox = client.inboxes.create(
    username="support",
    domain="apple.com"
)
```

```bash
npm install agentmail
# or
pip install agentmail
```

## Scale

- 20M+ emails delivered
- Enterprise-grade reliability
- Instant inbox creation (one API call)
- SOC2 Type II Certified

## Testimonials

- **Garry Tan (CEO, Y Combinator):** "It's a no brainer, agents into email. Everyone is going to be using AgentMail."
- **Garrett Scott (CEO, Pipedream Labs):** "AgentMail took email from the thing I worried most about to the thing I worried the least about."
- **Zach Schefska (Co-Founder, CarEdge):** "We provision 25,000 inboxes via AgentMail and handle millions of emails."

## Links

- **Console:** https://console.agentmail.to
- **Docs:** https://docs.agentmail.to
- **GitHub:** https://github.com/agentmail-to
- **Discord:** https://discord.gg/ZYN7f7KPjS
- **Status:** https://status.agentmail.to

