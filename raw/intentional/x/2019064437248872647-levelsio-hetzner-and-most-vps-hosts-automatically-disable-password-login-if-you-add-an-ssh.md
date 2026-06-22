---
type: raw_capture
source_type: x
url: https://x.com/levelsio/status/2019064437248872647
original_url: https://x.com/levelsio/status/2019064437248872647
author: "@levelsio"
handle: levelsio
status_id: 2019064437248872647
captured_at: 2026-06-19T20:00:12+08:00
published_at: "Wed Feb 04 15:04:08 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 71
  reposts: 53
  likes: 1189
---

# X post by @levelsio

## Source

- Original: [https://x.com/levelsio/status/2019064437248872647](https://x.com/levelsio/status/2019064437248872647)
- Canonical: [https://x.com/levelsio/status/2019064437248872647](https://x.com/levelsio/status/2019064437248872647)
- Author: @levelsio (@levelsio)

## Verbatim Text

Hetzner (and most VPS hosts) automatically disable password login if you add an SSH key during creating the server (usually on their web dashboards)

You should never have password login ever because it can be brute forced (they try 1000s of passwords)

So yes:
- Tailscale firewall subnet for SSH
- Cloudflare firewall subnet for HTTPS (web server)
- disable passwordless login
- enable unattended upgrades and auto reboots (for security updates etc)

My personal one that's fun:
- set the SSH port to some obscure number (I like security by obscurity)

You can install Claude Code and just ask to do all these things

## Quoted Post

- URL: https://x.com/LFuckingG/status/2019059415467585563
- Author: LFuckingG🌖 (@LFuckingG)

@levelsio this. also disable password auth for ssh entirely - key-only access saves so much headache. saw someone get owned last week because they left root login enabled

## Capture Note

TweetDetail returned complete normal-post text.
