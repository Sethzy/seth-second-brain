---
type: raw_capture
source_type: x
title: "Sunder sync: built-a-pretty-sick-and-simple-meeting-prep-tool-with-claude-code-twitter-mfishbein-2024159602934173866-FULL.md"
url: "https://x.com/mfishbein/status/2024159602934173866?s=46"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/built-a-pretty-sick-and-simple-meeting-prep-tool-with-claude-code-twitter-mfishbein-2024159602934173866-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/built-a-pretty-sick-and-simple-meeting-prep-tool-with-claude-code-twitter-mfishbein-2024159602934173866-FULL.md"
sha256: "b3e524801895d0fee3db991b44161c6d7c1b79c93cb5c2af8edb5abd23c6d824"
duplicate_of: ""
---

# Sunder sync: built-a-pretty-sick-and-simple-meeting-prep-tool-with-claude-code-twitter-mfishbein-2024159602934173866-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/built-a-pretty-sick-and-simple-meeting-prep-tool-with-claude-code-twitter-mfishbein-2024159602934173866-FULL.md`

Primary URL: https://x.com/mfishbein/status/2024159602934173866?s=46

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter Article - @mfishbein: Built a pretty sick (and simple!) meeting prep tool with Claude Code.

**URL:** https://x.com/mfishbein/status/2024159602934173866?s=46
**Author:** Mike Fishbein (@mfishbein)
**Posted:** Feb 18, 2026, 4:30 PM UTC
**Engagement:** 4 replies, 1 reposts, 32 likes, 3.1K views

## Summary
Near-verbatim extraction of the original X/Twitter post. The body below preserves the original wording and line breaks as closely as possible.

## Full Article

### Original Post (Near-Verbatim)

Built a pretty sick (and simple!) meeting prep tool with Claude Code. 

Every morning at 7am it researches everyone I'm meeting with that day and drops a dossier in my inbox. 

Here's the exact workflow (copy-paste to Claude Code to build your own): 

- Railway cron triggers the workflow before your meetings tart for the day 

- use Unipile's calendar API to pull today's Google Calendar events (filter out your own email and skip cancelled meetings to isolate external attendees)

- run Exa in parallel on each attendee to find their LinkedIn URL and company website using the email domain as a search hint

- hit Perplexity simultaneously for a live 2-3 sentence bio on the person and a 2-3 sentence company summary so both requests fire at the same time per attendee

- pipe all four research outputs to Claude and get back a clean plain text dossier with one section per person and one per company (can do JS formatter that strips markdown and slots everything into a template if you want simpler) 

- Resend delivers one email per meeting with the title and time in the subject line so it's instantly scannable when it hits your inbox

## Metadata
- Tweet ID: 2024159602934173866
- Canonical URL: https://x.com/mfishbein/status/2024159602934173866
- Source tier used: tier1
- Embedded X article extracted: no

