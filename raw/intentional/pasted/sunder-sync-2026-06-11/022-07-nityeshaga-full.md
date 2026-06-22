---
type: raw_capture
source_type: x
title: "Sunder sync: 07-nityeshaga-FULL.md"
url: "https://x.com/nityeshaga/status/2017128005714530780"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/07-nityeshaga-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/07-nityeshaga-FULL.md"
sha256: "b6a1679586255cb4b4c7b4331ce42ab744342cf20784ab520f45809701f10a29"
duplicate_of: ""
---

# Sunder sync: 07-nityeshaga-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/07-nityeshaga-FULL.md`

Primary URL: https://x.com/nityeshaga/status/2017128005714530780

Duplicate of existing source-map entry: `none`

## Capture Text

# Nityesh - How We Built an AI Project Manager Using Claude Code

**Author:** Nityesh (@nityeshaga)
**Posted:** Jan 30, 2026
**URL:** https://x.com/nityeshaga/status/2017128005714530780

## Thesis

**Claude Code for non-technical work is going to sweep the world by storm in 2026.**

This is how we built Claudie, our internal project manager for the consulting business.

## About the Author

**Role:** Applied AI engineer

**Job description:** Take everything learned about AI (from client work, industry, internal experiments) and turn it into systems that scale: curriculum, automations, frameworks.

## The Problem

### What Consulting Runs On

**Google Sheets** - Every client gets a detailed dashboard with:

- Up to **12 tables per sheet**
- Tracking: people, teams, sessions, deliverables, feedback, open items

### The Challenge

Keeping these sheets accurate and up-to-date is **genuinely a full person's job**.

The consulting lead was doing that job on top of 20 other things.

**Solution:** Automate the second person.

## Version Evolution

### Version 1: Slash Commands (Failed)

**Problem:** Using MCP tools to read data sources was too expensive in terms of context.

By the time the agent understood what was needed, it would be out of context window.

### Version 2: Orchestrator and Sub-Agents

**Architecture:** Main Claude orchestrates sub-agents via Tasks.

**The Fix:** Shared folder where sub-agents output reports that other agents can read directly.

This reduced context overhead and enabled scalable multi-agent coordination.

### Version 3: From Skills to a Handbook

**Major shift:** Replaced eleven fragmented skills with one coherent handbook.

**Handbook structure:**

- **Foundation** — team, tools, data sources, standards
- **Daily Operations** — data gathering procedures
- **Client Dashboards** — structure, tracking, quality checks
- **New Clients** — onboarding and setup workflows

**Result:** Consolidated, maintainable, coherent system that agents can consistently follow.

## Why Now, and Why 2026

**Key insight:** Every piece of the stack that made this possible is brand new.

### Timeline of Enabling Technologies

- **Oct 16, 2025:** MCP Builder skill released
- **Nov 24, 2025:** Claude Opus 4.5 released
- **Jan 23, 2026:** The Tasks feature released

**Conclusion:** The building blocks for non-technical Claude Code automation just arrived.

## Key Takeaways

1. **Non-technical automation** with Claude Code is now viable and powerful
2. **Context management** is critical - direct file sharing beats expensive MCP reads
3. **Orchestrator + sub-agents** pattern scales better than monolithic approaches
4. **Coherent handbooks** > fragmented skills for complex workflows
5. **2026 is the year** - all necessary infrastructure is now in place

## Technical Architecture

### Components

- **Main orchestrator:** Claude Code managing overall workflow
- **Sub-agents:** Specialized agents for specific tasks (via Tasks feature)
- **Shared folder:** Central location for inter-agent communication
- **Handbook:** Single source of truth for procedures and standards
- **MCP integrations:** Controlled access to data sources (Google Sheets, etc.)

### Design Patterns

- **Orchestrator pattern:** Main agent delegates to specialists
- **Shared context:** File-based communication between agents
- **Handbook-driven:** Consolidated documentation replaces scattered skills
- **Multi-agent coordination:** Tasks feature enables parallel work

## Impact

Built Claudie - an AI project manager that can:

- Track client dashboards across 12+ tables
- Gather data from multiple sources
- Update sheets automatically
- Handle onboarding for new clients
- Maintain quality and consistency standards

**Result:** Freed up consulting lead from full-time data management work.

## Category

Claude Code, Non-Technical Automation, Project Management, Multi-Agent Systems

## Related

- **Product:** Claudie (internal AI project manager)
- **Company:** Consulting business (not named)
- **Technologies:** Claude Code, MCP, Tasks, Google Sheets
- **Author role:** Applied AI engineer

