---
type: raw_capture
source_type: x
title: "Sunder sync: 41-twitter-levelsio-vps-security-FULL.md"
url: "https://x.com/levelsio/status/2019064437248872647"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/41-twitter-levelsio-vps-security-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/41-twitter-levelsio-vps-security-FULL.md"
sha256: "3834c2d16d05251076574bd0c595acccabde23a94e72b20a8d756712c4339862"
duplicate_of: ""
---

# Sunder sync: 41-twitter-levelsio-vps-security-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/41-twitter-levelsio-vps-security-FULL.md`

Primary URL: https://x.com/levelsio/status/2019064437248872647

Duplicate of existing source-map entry: `none`

## Capture Text

# Twitter - @levelsio: VPS Security Best Practices with Claude Code

**URL:** https://x.com/levelsio/status/2019064437248872647
**Author:** @levelsio (Pieter Levels) - Verified
**Platform:** Twitter/X
**Posted:** 11:04 PM · Feb 4, 2026
**Engagement:** 72 replies, 62 reposts, 1.2K likes, 1.7K bookmarks, 125.2K views

## Tweet Summary

VPS security best practices from @levelsio in response to @LFuckingG. Covers password auth (never use), SSH key-only access, Tailscale/Cloudflare firewalls, auto-updates, obscure SSH ports. Recommends using Claude Code to implement all security measures. Context: Hetzner VPS setup.

## Main Tweet Text

"Hetzner (and most VPS hosts) automatically disable password login if you add an SSH key during creating the server (usually on their web dashboards)

You should never have password login ever because it can be brute forced (they try 1000s of passwords)

So yes:
- Tailscale firewall subnet for SSH
- Cloudflare firewall subnet for HTTPS (web server)
- disable passwordless login
- enable unattended upgrades and auto reboots (for security updates etc)

My personal one that's fun:
- set the SSH port to some obscure number (I like security by obscurity)

You can install Claude Code and just ask to do all these things

Quote [of @LFuckingG's tweet about SSH security]"

## Quoted Tweet Context

**@LFuckingG (Feb 4):**
"this. also disable password auth for ssh entirely - key-only access saves so much headache. saw someone get owned last week because they left root login enabled"

**Context:** Someone got hacked due to root password login enabled

## Security Recommendations

### 1. SSH Key-Only Access (No Passwords)
**Risk:** Password brute force (attackers try thousands of passwords)
**Solution:** SSH keys only
**Hetzner:** Auto-disables password login when SSH key added during setup

### 2. Tailscale Firewall Subnet for SSH
**Purpose:** Restrict SSH access to Tailscale network only
**Benefit:** SSH not exposed to public internet
**Implementation:** Firewall rule allowing SSH only from Tailscale IPs

### 3. Cloudflare Firewall Subnet for HTTPS
**Purpose:** Web server traffic only through Cloudflare
**Benefit:** DDoS protection, rate limiting, bot filtering
**Implementation:** Firewall allowing HTTPS only from Cloudflare IPs

### 4. Disable Passwordless Login
**Clarification:** Likely means "disable password login" (context suggests)
**Alternative reading:** Disable passwordless SSH (require key passphrase)

### 5. Enable Unattended Upgrades and Auto Reboots
**Purpose:** Automatic security updates
**Risk if disabled:** Unpatched vulnerabilities
**Auto reboots:** Apply kernel updates automatically

### 6. Obscure SSH Port (Pieter's Personal Preference)
**Standard:** Port 22
**Approach:** Change to random high port (e.g., 49223)
**Philosophy:** Security by obscurity
**Benefit:** Reduces automated scanner noise
**Controversy:** Not "real" security, but reduces log spam

## Claude Code Integration

**Quote:** "You can install Claude Code and just ask to do all these things"

**Usage:**
1. Install Claude Code on VPS
2. Prompt: "Configure secure SSH: disable password auth, set up Tailscale firewall, enable unattended upgrades, change SSH port to 49223"
3. Claude Code: Implements all configurations automatically

**Value:** Security hardening without manual configuration

## Key Insights

### 1. Hetzner-Specific Behavior
**Auto-disables passwords:** When SSH key added during server creation
**User-friendly security:** Forces best practice by default
**Contrast:** Some VPS providers leave passwords enabled

### 2. Defense in Depth
**Multiple layers:**
1. SSH keys (not passwords)
2. Tailscale firewall (network level)
3. Cloudflare firewall (web level)
4. Auto-updates (patch level)
5. Obscure SSH port (reconnaissance level)

**No single point of failure:** Compromise one, others still protect

### 3. Obscure Ports: Controversial but Practical
**Security purists:** "Security by obscurity isn't real security"
**Pieter's view:** "fun" and reduces noise
**Reality:** Stops 99% of automated scanners, logs stay clean
**Not substitute for:** Real security (keys, firewalls)

### 4. Claude Code for Security Automation
**Use case:** Server hardening
**Benefit:** Reduces human error in config
**Risk:** Trust AI to implement correctly (needs verification)

### 5. Tailscale for SSH Access
**What is Tailscale:** Zero-config VPN (WireGuard-based)
**Benefit:** SSH over private network, not public internet
**Result:** Attackers can't even attempt connections

## Engagement Analysis

**125.2K views:** High for technical security content
**1.7K bookmarks:** Very high (1.36% rate)
**1.2K likes:** Good engagement
**72 replies:** Active discussion

**Bookmarks:Likes ratio = 1.42** (high utility)
**Interpretation:** People saving for VPS setup reference

## Author Context: Pieter Levels

**Known for:**
- Nomad List, RemoteOK, PhotoAI
- Indie hacker, remote work pioneer
- $3M+ ARR solo founder
- Public building, transparent revenue

**Credibility:** Very high (proven security practices at scale)

## Related Tools Mentioned

### Hetzner
**Type:** VPS provider (European, budget-friendly)
**Reputation:** Good price/performance
**Security:** Auto-disables password login (as noted)

### Tailscale
**Type:** Zero-config VPN
**Use:** Private network for SSH access
**Alternative:** WireGuard (lower-level)

### Cloudflare
**Type:** CDN, DDoS protection, WAF
**Use:** Firewall for web traffic
**Benefit:** Free tier available

### Claude Code
**Type:** AI coding assistant (CLI)
**Use:** Automate security configuration
**Platform:** OpenClaw/Claude Code

## Implementation Example

**Using Claude Code to harden VPS:**

```bash
# Install Claude Code on VPS
curl -fsSL https://openclaw.ai/install.sh | sh

# Run Claude Code
claude

# Prompt:
"Harden this Ubuntu VPS:
1. Disable password SSH auth, keys only
2. Configure UFW to allow only Tailscale IPs for SSH
3. Configure UFW to allow only Cloudflare IPs for HTTPS
4. Change SSH port to 49223
5. Enable unattended-upgrades with auto-reboot
6. Verify all changes"
```

**Claude Code:** Executes all commands, verifies configuration

## Category

VPS Security, SSH Security, Hetzner, Tailscale, Cloudflare, Claude Code, Security Hardening, Server Configuration, @levelsio

## Related

- **Author:** @levelsio (Pieter Levels) - Verified, indie hacker
- **Date:** February 4, 2026
- **Subject:** VPS security best practices
- **Context:** Response to @LFuckingG about SSH security, someone got hacked
- **Engagement:** 1.7K bookmarks (1.36% rate, high utility)
- **Key recommendations:**
  1. SSH keys only (no passwords)
  2. Tailscale firewall for SSH
  3. Cloudflare firewall for HTTPS
  4. Disable password login
  5. Unattended upgrades + auto-reboot
  6. Obscure SSH port (security by obscurity)
- **Claude Code use case:** Automate all security configurations
- **Hetzner-specific:** Auto-disables passwords when SSH key added
- **Philosophy:** Defense in depth (multiple security layers)
- **Controversy:** Security by obscurity (obscure ports) - practical but not "real" security
- **Tools:** Hetzner, Tailscale, Cloudflare, Claude Code
- **Credibility:** Very high (Pieter runs profitable SaaS at scale)

