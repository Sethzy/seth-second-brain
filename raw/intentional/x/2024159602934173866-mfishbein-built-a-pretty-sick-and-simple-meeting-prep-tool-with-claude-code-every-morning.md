---
type: raw_capture
source_type: x
url: https://x.com/mfishbein/status/2024159602934173866
original_url: https://x.com/mfishbein/status/2024159602934173866
author: "Mike Fishbein"
handle: mfishbein
status_id: 2024159602934173866
captured_at: 2026-06-19T21:22:24+08:00
published_at: "Wed Feb 18 16:30:31 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 5
  reposts: 2
  likes: 32
---

# X post by @mfishbein

## Source

- Original: [https://x.com/mfishbein/status/2024159602934173866](https://x.com/mfishbein/status/2024159602934173866)
- Canonical: [https://x.com/mfishbein/status/2024159602934173866](https://x.com/mfishbein/status/2024159602934173866)
- Author: Mike Fishbein (@mfishbein)

## Verbatim Text

Built a pretty sick (and simple!) meeting prep tool with Claude Code. 

Every morning at 7am it researches everyone I'm meeting with that day and drops a dossier in my inbox. 

Here's the exact workflow (copy-paste to Claude Code to build your own): 

- Railway cron triggers the workflow before your meetings tart for the day 

- use Unipile's calendar API to pull today's Google Calendar events (filter out your own email and skip cancelled meetings to isolate external attendees)

- run Exa in parallel on each attendee to find their LinkedIn URL and company website using the email domain as a search hint

- hit Perplexity simultaneously for a live 2-3 sentence bio on the person and a 2-3 sentence company summary so both requests fire at the same time per attendee

- pipe all four research outputs to Claude and get back a clean plain text dossier with one section per person and one per company (can do JS formatter that strips markdown and slots everything into a template if you want simpler) 

- Resend delivers one email per meeting with the title and time in the subject line so it's instantly scannable when it hits your inbox

## Media

- photo: https://pbs.twimg.com/media/HBc_WTEXEAA0ZeB.jpg

## Capture Note

TweetDetail returned complete normal-post text.
