---
type: raw_capture
source_type: web
title: "Sunder sync: 20-usebits-klaus-FULL.md"
url: "https://app.usebits.com/landing-klaus"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/20-usebits-klaus-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/20-usebits-klaus-FULL.md"
sha256: "28bacedb3936ce03a433f1654d6868843bb25b6f5a1d25d598e6456f864bf217"
duplicate_of: ""
---

# Sunder sync: 20-usebits-klaus-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/20-usebits-klaus-FULL.md`

Primary URL: https://app.usebits.com/landing-klaus

Duplicate of existing source-map entry: `none`

## Capture Text

# Usebits Klaus - Hosted OpenClaw Service

**URL:** https://app.usebits.com/landing-klaus
**Company:** Usebits Inc
**Type:** Product landing page
**Status:** Live service

## Title

"Klaus - AI Assistant Hosting"

## Overview

Hosted OpenClaw service that eliminates infrastructure management. Provides turnkey AI assistant with dedicated instance, LLM access, and multi-platform chat.

## Tagline

"Your personal AI assistant. Chat with Klaus in Slack, Telegram, or the web - he learns your workflows, manages tasks, and gets things done."

## Key Value Propositions

### 1. Quick Setup
- **Time:** Under 3 minutes
- **No VMs to manage**
- **No infrastructure headaches**

### 2. Your Own Instance
- Dedicated Klaus instance per user
- Own memory and context
- Isolated environment

### 3. Batteries Included
**Comes with:**
- LLM keys (OpenRouter credits)
- Browser automation
- Web search
- Ready to go out of box

### 4. Chat Anywhere
**Platforms:**
- Slack
- Telegram
- Web interface
- Always available (24/7)

### 5. Secure & Private
- Sandboxed environment
- Your data stays yours
- Powered by OpenClaw

## Pricing

### Standard Plan: $19/month

**Includes:**

1. **$15 OpenRouter credits (one-time)**
   - Access to basically any AI model
   - **Recommendation:** Haiku 4.5 for everyday use
   - **Premium option:** Opus 4.6 (requires buying more credits)

2. **One AgentMail account**
   - Dedicated email for agent
   - Send and receive messages as agent

3. **One OpenClaw cloud instance**
   - Dedicated browser automation infrastructure
   - **Current spec:** t4g.small on AWS EC2
   - Cloud-hosted (no local hardware needed)

### Bring Your Own Key (BYOK)

**Free option:**
- Use your own OpenRouter API key
- No additional cost
- Configure at: app.usebits.com/klaus

### Coming Soon

**Roadmap:**
1. Purchase additional OpenRouter credits directly through Bits
2. First-class support for other model providers

## Technical Stack

### Infrastructure
- **Cloud:** AWS EC2 (t4g.small instances)
- **Isolation:** Sandboxed environments per user
- **Model access:** OpenRouter (multi-model API)

### Capabilities
- Browser automation (built-in)
- Web search (built-in)
- Memory/context per instance
- Multi-platform chat

## How It Differs from Self-Hosted

### Klaus (Hosted)
- 3-minute setup
- No hardware required
- Managed infrastructure
- Included LLM credits
- $19/month

### Self-Hosted OpenClaw
- Manual setup (hours/days)
- Mac Mini or dedicated hardware
- Manage your own infra
- BYOK required
- Hardware cost + API costs

## Target Users

### Primary
- People who want OpenClaw without hardware
- Non-technical users wanting easy setup
- Users prioritizing convenience over control

### Secondary
- Developers testing OpenClaw before self-hosting
- Users needing cloud-based deployment
- Teams wanting managed solution

## Product Family (Usebits Inc)

**Related products:**
- **Bits** (linked from footer)
- **Bittie** (landing page available)
- **Extension** (beta)
- **Klaus** (this product)

**Documentation:** docs.usebits.com

## Key Innovation

**OpenClaw-as-a-Service:** Takes open-source agent (OpenClaw) and provides managed hosting with batteries-included setup. Bridges gap between technical self-hosting and non-technical users.

## Comparison to Cloudflare Moltworker

| Aspect | Klaus (Usebits) | Moltworker (Cloudflare) |
|--------|-----------------|-------------------------|
| Setup | 3 minutes | Custom middleware layer |
| Infra | AWS EC2 t4g.small | Cloudflare Workers |
| Model | OpenRouter (any) | Configurable |
| Price | $19/month + credits | Pay-as-you-go (Workers) |
| Target | End users | Developers |

## Related to Item #21

**Item #21:** Cloudflare Moltworker (self-hosted agent on serverless)
**Klaus:** Commercial managed hosting
**Both:** Eliminate need for local hardware

**Timing:** Both emerged during January 2026 OpenClaw rush

## Use Cases

### For End Users
- Personal assistant without Mac Mini
- Quick experiments with OpenClaw
- Multi-platform chat access
- Managed infrastructure

### For Teams
- Shared agent infrastructure
- Standardized deployment
- Centralized billing

### For Developers
- Test OpenClaw before committing to hardware
- Prototype agent workflows
- Learn OpenClaw capabilities

## Technical Notes

### AgentMail
- Dedicated email address per agent
- Enables email-based workflows
- Agent can send/receive as separate entity

### OpenRouter Integration
- Access to 100+ models
- Unified API for multiple providers
- Credit-based billing
- BYOK option available

### Browser Automation
- Included in base offering
- Cloud-based (no local Chrome needed)
- Handles navigation, forms, scraping

## Business Model

**Core revenue:** $19/month subscriptions
**Additional:** OpenRouter credit top-ups (coming soon)
**Free tier:** BYOK option (bring your own OpenRouter key)

**Unit economics:**
- EC2 t4g.small ~ $0.0168/hour = ~$12/month
- Margin ~ $7/month per user (before support/overhead)
- Credits subsidy: $15 one-time (customer acquisition)

## Category

AI Agent Hosting, OpenClaw, Managed Services, No-Code AI

## Related

- **Company:** Usebits Inc
- **Product:** Klaus
- **Technology:** OpenClaw (open source)
- **Infrastructure:** AWS EC2
- **Model API:** OpenRouter
- **Timing:** January 2026 OpenClaw wave
- **Comparison:** Self-hosted (Item #22 Brandon Wang), Serverless (Item #21 Cloudflare)

