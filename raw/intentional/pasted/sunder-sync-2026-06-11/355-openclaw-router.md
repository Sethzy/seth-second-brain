---
type: raw_capture
source_type: web
title: "Sunder sync: openclaw-router.md"
url: "https://github.com/BlockRunAI/ClawRouter"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-router.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/openclaw-router.md"
sha256: "abab53b2c89382ddd7fbc1496528f730b1d95e743bd7d09ca48aa0abc8666dbe"
duplicate_of: ""
---

# Sunder sync: openclaw-router.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/openclaw-router.md`

Primary URL: https://github.com/BlockRunAI/ClawRouter

Duplicate of existing source-map entry: `none`

## Capture Text

# ClawRouter - Smart LLM Router for OpenClaw

**Repository:** BlockRunAI/ClawRouter
**URL:** https://github.com/BlockRunAI/ClawRouter
**Stars:** 1.9k
**Forks:** 178
**Issues:** 2
**Latest commit:** Feb 9, 2026 (4 hours ago)
**Version:** 0.4.7

## Tagline

**"Smart LLM router — save 78% on inference costs. 30+ models, one wallet, x402 micropayments."**

## Description

Route every request to the cheapest model that can handle it. **One wallet, 30+ models, zero API keys.**

## Key Features

- **Cost savings:** Save 78% on inference costs
- **Smart routing:** Automatically routes to cheapest capable model
- **30+ models** supported
- **One wallet:** x402 micropayments via BlockRun
- **Zero API keys:** No need to manage individual provider keys
- **OpenClaw plugin:** Integrates as OpenClaw plugin

## Tech Stack

- **Language:** TypeScript
- **Platform:** Node.js
- **License:** MIT
- **Package:** @blockrun/clawrouter (npm)

## Repository Structure

### Directories

- **.github/workflows** - CI/CD (GitHub Actions with ESLint, Prettier, typecheck)
- **assets** - Banner and branding
- **docs** - Documentation
- **scripts** - Utility scripts
- **skills/clawrouter** - OpenClaw skill definition
- **src** - Source code
- **test** - Test files

### Key Files

- **openclaw.plugin.json** - OpenClaw plugin configuration
- **openclaw.security.json** - Security documentation
- **package.json** - NPM package configuration
- **tsconfig.json** - TypeScript configuration
- **eslint.config.js** - ESLint configuration
- **.prettierrc** - Prettier formatting config

## Recent Activity

**Latest commits (Feb 2026):**
- Replace external banner with BlockRun branded version (4 hours ago)
- Fix: normalize messages for Google models (14 hours ago)
- Add German language support for smart routing (7 hours ago)
- Revert cost savings dashboard feature (5 hours ago)
- Fix: proper SSE streaming format for Discord (2 days ago)
- Add GitHub Actions CI workflow (4 days ago)

## Installation

OpenClaw plugin ID: `clawrouter`

Install via OpenClaw:
```bash
openclaw plugins install clawrouter
```

NPM package:
```bash
npm install @blockrun/clawrouter
```

## x402 Micropayments

Uses BlockRun's x402 micropayment system:
- Pay per request
- No upfront API subscriptions
- Single wallet for all models
- Automatic routing to cheapest option

## Model Support

**30+ models** including support for:
- Google models (with message normalization)
- German language routing
- Multiple providers via single interface

## Testing

Test files included:
- **test-balance.ts** - Balance testing
- **test-balance-integration.ts** - Integration testing
- **test-e2e.ts** / **test-e2e.mjs** - End-to-end testing
- **test-retry.ts** - Retry logic testing

## Documentation

- **Docs:** https://blockrun.ai/docs
- **Models:** https://blockrun.ai/models

## Development

**CI/CD:**
- GitHub Actions workflow
- ESLint for linting
- Prettier for formatting
- TypeScript type checking
- Automated testing

**Code quality:**
- TypeScript strict mode
- ESLint enforcement
- Prettier formatting
- Comprehensive test suite

## Use Cases

### For OpenClaw Users
- Reduce AI inference costs by 78%
- Access 30+ models through single plugin
- No API key management
- Automatic smart routing

### For Cost-Conscious Developers
- Pay only for what you use (micropayments)
- Automatic selection of cheapest capable model
- No provider lock-in
- Single wallet across all models

### For Multi-Model Applications
- Support many models without managing keys
- Failover and retry logic
- Load balancing across providers
- Cost optimization built-in

## Key Innovation

**Smart routing algorithm:** Analyzes request requirements and routes to the cheapest model that can handle the task, rather than always using expensive flagship models.

**x402 micropayments:** Eliminates need for subscriptions or API keys by using blockchain-based micropayments per request.

## Category

LLM Infrastructure, Cost Optimization, OpenClaw Plugin, Model Routing, Micropayments

## Related

- **Company:** BlockRun AI
- **Platform:** OpenClaw/Clawdbot integration
- **Technology:** x402 micropayment protocol
- **Competitors:** Traditional API key-based model access

