---
type: raw_capture
source_type: x
title: "Sunder sync: 56-twitter-dhh-beelink-proxmox-FULL.md"
url: "https://x.com/dhh/status/2018937285576638954"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/56-twitter-dhh-beelink-proxmox-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/56-twitter-dhh-beelink-proxmox-FULL.md"
sha256: "2302a24f1fb9a1c4a27860fb9514bfdb2271f4dfa02ffaca017ba3ab81ffb0f5"
duplicate_of: ""
---

# Sunder sync: 56-twitter-dhh-beelink-proxmox-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/56-twitter-dhh-beelink-proxmox-FULL.md`

Primary URL: https://x.com/dhh/status/2018937285576638954

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter - @dhh: Beelink + Proxmox > Mac Mini for Multi-Agent OpenClaw

**URL:** https://x.com/dhh/status/2018937285576638954
**Author:** DHH (@dhh) - Verified (David Heinemeier Hansson)
**Platform:** Twitter/X
**Posted:** 2:38 PM · Feb 4, 2026
**Engagement:** 144 replies, 89 reposts, 1.3K likes, 1.5K bookmarks, 118.1K views

## Tweet Summary

DHH (Ruby on Rails creator) recommends Beelink mini PC + Proxmox instead of Mac Mini for OpenClaw. "Why would you get a Mac Mini for OpenClaw, and restrict yourself to a single agent?" Proxmox virtualization allows running "a whole team of claws on a single cheap box." High engagement (1.5K bookmarks) from tech community.

## Main Tweet

"Why would you get a Mac Mini for OpenClaw, and restrict yourself to a single agent?

Get a @Beelinkofficial, setup Proxmox, and you'll be able to run a whole team of claws on a single cheap box!

proxmox.com"

## Key Recommendation

### Hardware: Beelink Mini PC
**Alternative to:** Mac Mini
**Price:** ~$200-400 (vs Mac Mini $600+)
**Form factor:** Compact mini PC
**Benefit:** Cheaper, runs Linux natively

### Software: Proxmox VE
**What:** Open-source virtualization platform
**Purpose:** Run multiple virtual machines
**Result:** Multiple isolated OpenClaw instances
**Cost:** Free (open-source)

### Outcome: "Whole team of claws"
**Not:** Single agent on Mac Mini
**Instead:** 5-10+ agents on one box
**Each agent:** Isolated VM, independent config

## Why This Matters

### Mac Mini Limitation
**Problem:** Single OS instance = single agent setup (without complex config)
**Cost:** $600-1,200 depending on spec
**Advantage:** macOS (if you need it)

### Beelink + Proxmox Advantage
**Multiple VMs:** Run 10 OpenClaw instances simultaneously
**Isolation:** Each agent in separate VM
**Cost:** $200-400 hardware + $0 software
**Flexibility:** Easy to spin up/down agents

## Proxmox Overview

**Product:** Open-source virtualization platform
**Based on:** Debian Linux + KVM
**Features:**
- Web-based management UI
- VM creation/management
- Container support (LXC)
- Backup/restore
- Clustering

**Use case here:** Run multiple Ubuntu VMs, each with OpenClaw

## Engagement Analysis

**118.1K views:** Very high (DHH has huge following)
**1.5K bookmarks:** High (1.27% rate)
**1.3K likes:** Strong
**144 replies:** Very active (likely questions about setup)

## Author Context: DHH

**Full name:** David Heinemeier Hansson
**Known for:**
- Creator of Ruby on Rails
- Co-founder of Basecamp (37signals)
- Tech thought leader
- Strong opinions on tech/business

**Credibility:** Maximum (legendary developer, successful entrepreneur)

## Architecture Comparison

### Mac Mini (Single Agent)
```
Mac Mini ($600+)
├── macOS
└── OpenClaw instance 1
```

### Beelink + Proxmox (Multi-Agent)
```
Beelink ($300)
├── Proxmox VE (free)
    ├── VM 1 (Ubuntu) → OpenClaw agent 1
    ├── VM 2 (Ubuntu) → OpenClaw agent 2
    ├── VM 3 (Ubuntu) → OpenClaw agent 3
    └── ...VM 10
```

## Use Case: Bhanu's Mission Control (Item 49)

**Bhanu's setup:** 10 agents via sessions
**DHH's suggestion:** 10 agents via separate VMs

**Benefit:**
- Complete isolation (VM-level, not session-level)
- Different OS versions per agent
- Resource allocation per agent
- Easier to manage complex setups

## Cost Breakdown

### Mac Mini Option
- Hardware: $600-1,200
- Software: $0 (macOS included)
- **Total:** $600-1,200

### Beelink + Proxmox Option
- Hardware: $200-400 (Beelink)
- Software: $0 (Proxmox free)
- **Total:** $200-400

**Savings:** $200-800

## Technical Specs

### Beelink Mini PCs (Example)
- CPU: Intel N100 or similar
- RAM: 8-16GB
- Storage: 256-512GB SSD
- Power: 15W TDP (very efficient)
- Size: Tiny (4" x 4")

### Proxmox Requirements
- 64-bit CPU with virtualization support
- 4GB RAM minimum (8GB+ recommended)
- SSD recommended
- Network connection

## Setup Process (Inferred)

1. **Buy Beelink mini PC** (~$300)
2. **Install Proxmox** (download ISO, boot from USB)
3. **Create Ubuntu VMs** (via Proxmox web UI)
4. **Install OpenClaw in each VM** (standard install)
5. **Configure agents** (different personalities/roles)
6. **Run team of agents** (all on one box)

**Total time:** 2-4 hours

## Community Reception

**144 replies likely include:**
- "Which Beelink model do you recommend?"
- "How many VMs can run on a Beelink?"
- "Is Proxmox harder to manage than macOS?"
- "Can I run this on any mini PC?"

**1.5K bookmarks:** Tech-savvy users saving for implementation

## Related Items

**Item 44 (Scott Tolinski):** Mac Mini + Tailscale for remote dev
**Item 49 (Bhanu):** 10 agents via sessions
**Item 56 (DHH):** Beelink + Proxmox for VM isolation

**Different approaches to multi-agent setup**

## Category

OpenClaw, Hardware, Proxmox, Virtualization, Multi-Agent, Beelink, Mac Mini Alternative, DHH

## Related

- **Author:** DHH (@dhh) - Verified, Ruby on Rails creator, Basecamp founder
- **Date:** February 4, 2026
- **Subject:** Beelink + Proxmox for multi-agent OpenClaw
- **Engagement:** 118.1K views, 1.5K bookmarks
- **Hardware:** Beelink mini PC ($200-400)
- **Software:** Proxmox VE (free, open-source)
- **Benefit:** Run "whole team of claws on single cheap box"
- **vs Mac Mini:** Cheaper, better multi-agent support
- **Isolation:** VM-level (not just sessions)
- **Cost savings:** $200-800 vs Mac Mini
- **Use case:** 10+ isolated OpenClaw instances
- **Credibility:** DHH = legendary developer
- **Related:** Item 49 (Bhanu's 10-agent setup), Item 44 (Mac Mini setup)

