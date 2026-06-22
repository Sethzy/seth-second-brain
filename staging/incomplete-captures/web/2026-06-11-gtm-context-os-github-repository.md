---
type: incomplete_capture
source_type: web
title: "GTM Context OS GitHub repository"
url: "https://github.com/thesnappingdog/gtm-context-os"
collected_at: 2026-06-11T10:13:00Z
published_at: Unknown
capture_quality: partial
status: partial
trust_lane: incomplete
---

# GTM Context OS GitHub repository

Source: https://github.com/thesnappingdog/gtm-context-os

## Capture Text

Partial repository snapshot captured from a shallow git clone on 2026-06-11. The public repo contains `README.md`, `AGENTS.md`, `context.md`, `demand/pull-framework.md`, setup/status/roadmap docs, `.gtm-os` eval machinery, `.claude` rules and skills, and integration references for Apollo, Clay, datastore, Fireflies, Gong, HubSpot, and lemlist.

The README describes GTM Context OS as an AI-native operating system for go-to-market teams: a git repository that acts as both shared brain and operational backbone. It has two modes:

- Context mode: ingest sales calls, analyze demand, define ICP, understand competitors and buyers, and preserve evidence.
- Operational mode: connect CRM/call-recording/enrichment/campaign tools, write scripts, build pipelines, draft outbound, and feed campaign results back into the repo.

The repo's central method is the Demand-First GTM Framework and PULL scoring:

- Project: the buyer has a real project on their to-do list.
- Unavoidable: the project cannot be ignored or deferred.
- Looking: the buyer is actively evaluating options.
- Lacking: current options do not solve the project well enough.

The template warns that demand cannot be created, only found. It distinguishes active demand from generic pain or benefit, and it requires real prospect language from transcripts or speaker-labeled notes before scoring.

Operational conventions from `AGENTS.md` include:

- `context.md` is the durable strategy foundation and should be read every session.
- `demand/` owns PULL analyses, research evidence, buyer insights, and synthesis.
- `status.md` is the append-only operational log.
- Modules such as `segments/`, `messaging/`, `campaigns/`, `engine/`, `content/`, `scripts/`, and `workflows/` are created only when needed.
- Claims use confidence/provenance tags such as `[VERIFIED]`, `[CLAIMED]`, `[INFERRED]`, and `[UNVERIFIABLE]`; date claims that age.
- Segments, messaging, and campaign sequences must link back to demand evidence.
- Agents should check before creating new structure.
- Data outputs are separated into `_output/`, `samples/`, and `_retained/` based on durability and sensitivity.

The repo includes an upgrade/eval pattern:

- `.gtm-os/eval/` tests instruction-correctness behavior.
- `.gtm-os/upgrade-log.md` is intended as an adoption ledger in cloned instances.
- `/gtm-os-upgrade` fetches template changes as patterns, checks them against the instance, and proposes adopt/adapt/skip decisions.

The integration layer is reference-first. `engine/integrations/README.md` says `/setup-api` should read a tool reference when connecting a known GTM tool, or build a new reference from API docs when the tool is not listed. Existing references cover Apollo, Clay, Fireflies, Gong, HubSpot, lemlist, and optional datastore documentation.

## My Note

Seth said "add this" for the GitHub repo at 6:08 PM. This is a partial staged capture because the wiki now has a repository excerpt and inspected clone context, not a full immutable verbatim copy of every file in the repo.

## Wiki Connections

- wiki/gtm-sales/agentic-gtm-campaign-workflows.md
