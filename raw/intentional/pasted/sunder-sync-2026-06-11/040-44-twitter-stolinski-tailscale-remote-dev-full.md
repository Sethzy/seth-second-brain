---
type: raw_capture
source_type: x
title: "Sunder sync: 44-twitter-stolinski-tailscale-remote-dev-FULL.md"
url: "https://x.com/stolinski/status/2019408944016584759"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/44-twitter-stolinski-tailscale-remote-dev-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/44-twitter-stolinski-tailscale-remote-dev-FULL.md"
sha256: "25a56766de3d9b03b03859bc9cd5f559b4d8ed33e688355034acb069bc8ed499"
duplicate_of: ""
---

# Sunder sync: 44-twitter-stolinski-tailscale-remote-dev-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/44-twitter-stolinski-tailscale-remote-dev-FULL.md`

Primary URL: https://x.com/stolinski/status/2019408944016584759

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter - @stolinski: Remote Dev Workflow with Tailscale + Zed + OpenCode

**URL:** https://x.com/stolinski/status/2019408944016584759
**Author:** Scott Tolinski (@stolinski) - Verified, Syntax.fm co-host
**Platform:** Twitter/X
**Posted:** 9:53 PM · Feb 5, 2026
**Engagement:** 13 replies, 27 reposts, 458 likes, 928 bookmarks, 149.1K views

## Tweet Summary

Scott's remote development workflow: Host dev process on Mac Mini, access from phone/computer via Tailscale + Zed + OpenCode. "No crappy mobile terminal apps." Also hosts OpenClaw UI without Discord/WhatsApp. Includes YouTube video "You Should Be Using Tailscale" and links to tools.

## Main Tweet Text

"This is how I host my dev process on my Mac Mini and work on it from my phone, computer, anything.

No crappy mobile terminal apps, just Tailscale, Zed & OpenCode.

This is also how I host my personal OpenClaw UI without having to use Discord/WhatsApp

[YouTube link: You Should Be Using Tailscale]

Links:
https://tailscale.com/
https://zed.dev/
DNS settings: https://login.tailscale.com/admin/dns
https://opencode.ai/

This is how I have my Openclaw (clawdbot) ..."

## Tool Stack

### 1. Mac Mini
**Role:** Host machine
**Benefit:** Always-on, home server
**Use:** Runs dev environment, OpenClaw, etc.

### 2. Tailscale
**Type:** Zero-config VPN (WireGuard-based)
**Purpose:** Secure remote access to Mac Mini
**Benefit:** Access from anywhere (phone, laptop, etc.)

### 3. Zed
**Type:** Code editor (multiplayer, fast)
**Purpose:** Remote code editing
**Benefit:** Better than mobile terminal apps

### 4. OpenCode
**Type:** (Not specified, likely web-based code editor or OpenClaw UI)
**Purpose:** Access development environment
**Benefit:** Works from any device

### 5. OpenClaw
**Hosted on:** Mac Mini
**Accessed via:** Custom UI (not Discord/WhatsApp)
**Benefit:** Personal interface, not dependent on chat apps

## Workflow

**Setup:**
1. Mac Mini at home (always on)
2. Tailscale VPN connects all devices
3. Zed editor for code
4. OpenCode for environment access
5. OpenClaw runs on Mac Mini

**Access:**
- From phone: Tailscale → Zed/OpenCode
- From laptop: Tailscale → Zed/OpenCode
- From anywhere: Same workflow

**Result:** "No crappy mobile terminal apps"

## Key Benefits

### 1. Device Flexibility
**Access from:** Phone, computer, tablet, anything
**Same experience:** Consistent dev environment
**No mobile-specific tools:** Avoid limited mobile terminal apps

### 2. Always-On Development
**Mac Mini:** Home server, always available
**Benefit:** Start work from any device, pick up where left off

### 3. Better Than Discord/WhatsApp for OpenClaw
**Traditional:** OpenClaw via chat apps
**Scott's setup:** Custom UI hosted on Mac Mini
**Benefit:** Dedicated interface, not mixed with messages

### 4. Secure Access
**Tailscale:** Encrypted VPN
**Benefit:** Safe remote access, no exposed ports

## YouTube Video

**Title:** "You Should Be Using Tailscale"
**Channel:** Likely Syntax.fm or Scott's personal channel
**Content:** (Not accessible) Likely tutorial on Tailscale setup

## Links Provided

1. **https://tailscale.com/** - VPN service
2. **https://zed.dev/** - Code editor
3. **https://login.tailscale.com/admin/dns** - DNS settings
4. **https://opencode.ai/** - OpenCode platform

## DNS Settings Note

**Link to:** Tailscale admin DNS settings
**Purpose:** Custom DNS configuration for VPN
**Use case:** Route specific domains through Tailscale network

## Engagement Analysis

**149.1K views:** Very high
**928 bookmarks:** High (0.62% rate)
**458 likes:** Moderate
**13 replies:** Lower (suggests straightforward, less debate)

**Interpretation:** High interest in remote dev workflow

## Author Context: Scott Tolinski

**Known for:**
- Co-host of Syntax.fm (popular web dev podcast)
- LevelUp Tutorials
- Web development educator
- React/Svelte expert

**Credibility:** Very high (established developer, educator)

## Use Cases

### 1. Travel Development
**Scenario:** Away from home, need to work
**Solution:** Access Mac Mini via phone/tablet

### 2. Multi-Device Workflow
**Scenario:** Switch between devices throughout day
**Solution:** Same environment everywhere

### 3. Home Lab
**Scenario:** Mac Mini as personal server
**Solution:** Host all dev tools, access remotely

### 4. OpenClaw Access
**Scenario:** Want to use OpenClaw from anywhere
**Solution:** Host on Mac Mini, custom UI via Tailscale

## Comparison to Alternatives

| Approach | Tools | Pros | Cons |
|----------|-------|------|------|
| **Scott's** | Mac Mini + Tailscale + Zed | Always-on, secure, flexible | Requires Mac Mini |
| **Cloud IDE** | Replit, Codespaces | Easy setup | Monthly cost, less control |
| **Mobile terminal** | Termius, Blink | Native app | "Crappy" UX (Scott's view) |
| **Discord/WhatsApp** | Chat-based OpenClaw | Easy | Mixed with messages, limited UI |

## Key Insights

### 1. Mac Mini as Home Server
**Trend:** Using Mac Mini for always-on hosting
**Benefits:** Power-efficient, quiet, full macOS
**Cost:** One-time hardware vs ongoing cloud fees

### 2. Tailscale Everywhere
**Pattern across community:**
- Item 41: @levelsio uses Tailscale for VPS SSH
- Item 44: @stolinski uses Tailscale for remote dev
**Adoption:** Becoming standard for secure remote access

### 3. Disdain for Mobile Terminal Apps
**Quote:** "No crappy mobile terminal apps"
**View:** Mobile terminals have poor UX
**Solution:** Browser-based tools (Zed, OpenCode) via VPN

### 4. Custom OpenClaw UI
**Alternative:** Discord/WhatsApp bots
**Scott's approach:** Dedicated web UI
**Benefit:** Better UX, not mixed with chat

### 5. Zed Editor for Remote Work
**What is Zed:** Multiplayer code editor (from Atom creators)
**Use case:** Remote pair programming, solo remote editing
**Benefit:** Better than SSH + vim/nano

## Implementation

**Steps to replicate:**
1. Set up Mac Mini (or any always-on machine)
2. Install Tailscale on Mac Mini
3. Install Tailscale on all devices (phone, laptop)
4. Install Zed on Mac Mini (or web-accessible editor)
5. Access Mac Mini via Tailscale IP from any device
6. Configure OpenClaw to run on Mac Mini with web UI

## Tailscale DNS Settings

**Purpose:** Custom DNS for Tailscale network
**Use cases:**
- Route internal domains (e.g., macmini.local)
- Ad blocking via DNS
- Split DNS (some domains local, some public)

**Link provided:** https://login.tailscale.com/admin/dns

## Category

Remote Development, Tailscale, Zed, OpenCode, OpenClaw, Mac Mini, Home Server, VPN, Mobile Development

## Related

- **Author:** Scott Tolinski (@stolinski) - Verified, Syntax.fm co-host
- **Date:** February 5, 2026
- **Subject:** Remote dev workflow with Tailscale + Zed + OpenCode
- **Engagement:** 928 bookmarks (0.62% rate, high interest)
- **Tools:** Mac Mini, Tailscale, Zed, OpenCode, OpenClaw
- **Key benefit:** Access dev environment from phone/computer/anywhere
- **Alternative rejected:** "Crappy mobile terminal apps"
- **OpenClaw:** Custom UI hosted on Mac Mini (vs Discord/WhatsApp)
- **Video:** "You Should Be Using Tailscale" on YouTube
- **Links:** tailscale.com, zed.dev, DNS settings, opencode.ai
- **Pattern:** Tailscale becoming standard for secure remote access
- **Related item:** Item 41 (@levelsio using Tailscale for VPS SSH)
- **Use case:** Travel development, multi-device workflow, home lab
- **Mac Mini:** Always-on home server trend
- **Credibility:** Very high (established web dev educator)

