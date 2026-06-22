---
type: raw_capture
source_type: web
title: "Sunder sync: 24-openrouter-auto-FULL.md"
url: "https://openrouter.ai/openrouter/auto"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/24-openrouter-auto-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/24-openrouter-auto-FULL.md"
sha256: "7fe5f07beea29bb145b18d27664ca3934aae6b5540b60ec31ce23d30559a3c9c"
duplicate_of: ""
---

# Sunder sync: 24-openrouter-auto-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/24-openrouter-auto-FULL.md`

Primary URL: https://openrouter.ai/openrouter/auto

Duplicate of existing source-map entry: `none`

## Capture Text

# OpenRouter - Auto Router

**URL:** https://openrouter.ai/openrouter/auto
**Service:** OpenRouter, Inc
**Type:** Model routing service
**Status:** Live (created Nov 8, 2023)

## Title

"Auto Router - API, Providers, Stats | OpenRouter"

## Model Identifier

`openrouter/auto`

## Overview

Meta-model routing service that analyzes prompts and automatically routes to optimal model from 60+ options, optimizing for best possible output while maintaining OpenAI-compatible API.

## Core Specs

| Specification | Value |
|--------------|-------|
| **Context Length** | 2,000,000 tokens |
| **Input Pricing** | $0/M tokens (varied) |
| **Output Pricing** | $0/M tokens (varied) |
| **Actual Cost** | Charged at routed model's rate |
| **Created** | November 8, 2023 |
| **Routing Pool** | 60+ models |

## How It Works

### 1. Meta-Model Analysis
**Process:**
- Your prompt processed by routing meta-model
- Analyzes task requirements, complexity, features needed
- Selects optimal model from pool
- Routes request transparently

### 2. Transparent Routing
**Visibility:**
- Check which model was used via Activity page
- Response contains `model` attribute with actual model used
- Pricing: Charged at routed model's rate (not fixed)

### 3. Customization
**Control:**
- Can customize models available for routing
- See docs: /docs/guides/routing/routers/auto-router
- Filter by capabilities, pricing, providers

## Routing Pool (60+ Models)

### Anthropic (9 models)
- Claude 3 Haiku
- Claude 3.5 Haiku
- Claude 3.7 Sonnet
- **Claude Haiku 4.5**
- **Claude Opus 4**
- Claude Opus 4.1
- **Claude Opus 4.5**
- Claude Sonnet 4
- **Claude Sonnet 4.5**

### OpenAI (20 models)
- GPT-3.5 Turbo
- GPT-4 (multiple variants)
- GPT-4 Turbo
- GPT-4.1 (Standard, Mini, Nano)
- GPT-4o (multiple versions + mini)
- **GPT-5 (Standard, Mini, Nano)**
- **GPT-5.1**
- **GPT-5.2 (Standard + Pro)**
- GPT-OSS-120B

### Google (5 models)
- Gemini 2.0 Flash 001
- **Gemini 2.5 Flash**
- **Gemini 2.5 Pro**
- **Gemini 3 Flash Preview**
- **Gemini 3 Pro Preview**

### Meta (6 models)
- Llama 3 (8B, 70B)
- Llama 3.1 (8B, 70B, 405B)
- Llama 3.3 70B

### Mistral AI (9 models)
- Mistral 7B Instruct
- Mistral Large (multiple versions)
- Mistral Medium 3.1
- Mistral Nemo
- Mistral Small 3.2
- Mixtral 8x7B
- Mixtral 8x22B
- Codestral 2508

### Others
- **Cohere:** Command R, Command R+
- **DeepSeek:** DeepSeek R1
- **Moonshot AI:** Kimi K2 Thinking
- **Perplexity:** Sonar
- **Qwen:** Qwen3 (14B, 32B, 235B)
- **xAI:** Grok 3, Grok 3 Mini, Grok 4

## Recent Activity Stats (Nov 2025 - Jan 2026)

### Top 5 Routed Models by Token Usage

1. **Google Gemini 2.5 Flash Lite** - 440M tokens (67.8%)
2. **Claude Opus 4.5** - 55.5M tokens (8.6%)
3. **Mistral Nemo** - 39.8M tokens (6.1%)
4. **Gemini 3 Pro Preview** - 22.8M tokens (3.5%)
5. **GPT-5 Nano** - 17.2M tokens (2.7%)

### Insights
- **Extreme skew:** Flash Lite dominates (2/3 of traffic)
- **Cost optimization:** Router favors cheap, fast models
- **Premium usage:** Claude Opus 4.5 still significant for complex tasks
- **Long tail:** 55+ other models handle remaining ~11%

## API Integration

### OpenAI-Compatible

**Base concept:**
OpenRouter normalizes requests/responses across 300+ models & providers. Use OpenAI SDK or call directly.

### Example Code (OpenRouter SDK)

```typescript
import { OpenRouter } from "@openrouter/sdk";

const openrouter = new OpenRouter({
  apiKey: "<OPENROUTER_API_KEY>"
});

const stream = await openrouter.chat.send({
  model: "openrouter/auto",
  messages: [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "What is in this image, audio and video?" },
        { "type": "image_url", "image_url": { "url": "https://..." } },
        { "type": "input_audio", "input_audio": { "data": "UklGR...", "format": "wav" } },
        { "type": "video_url", "video_url": { "url": "https://..." } }
      ]
    }
  ],
  stream: true
});

for await (const chunk of stream) {
  const content = chunk.choices[0]?.delta?.content;
  if (content) {
    process.stdout.write(content);
  }
}
```

### Multi-Modal Support
- **Text** (all models)
- **Images** (vision models)
- **Audio** (supported models)
- **Video** (supported models)

Router automatically filters for models that support requested features.

### Headers
**Optional OpenRouter-specific headers:**
- Allow your app to appear on OpenRouter leaderboards
- See: /docs/requests#request-headers

### SDKs Available
- **@openrouter/sdk** (TypeScript)
- **openai-python**
- **openai-typescript**
- Standard OpenAI SDK (any language)
- Third-party frameworks (LangChain, etc.)

## Related OpenRouter Products

### 1. Free Models Router (`openrouter/free`)
**Concept:** Random selection from free models
- Filters for required features (vision, tools, structured output)
- No cost
- Good for experimentation

### 2. Body Builder (`openrouter/bodybuilder`)
**Concept:** Natural language → API request objects
- Example: "count to 10 using gemini and opus" → structured API calls
- **Use case:** Multi-model requests, custom routers, programmatic generation
- **Status:** Beta, currently free

### 3. Pony Alpha
Foundation model with strong coding, agentic workflows, reasoning, roleplay.
**Note:** Logs prompts/completions for training.

### 4. Cloaked Models (Alpha/Beta Testing)
**Pattern:** OpenRouter provides early access to unreleased models with code names:

- **Bert-Nebulon Alpha** → Was early Mistral Large 3
- **Sherlock Dash Alpha** → Was early Grok 4.1 Fast (no reasoning)
- **Sherlock Think Alpha** → Was early Grok 4.1 Fast (reasoning)
- **Polaris Alpha** → Was early GPT-5.1 (minimal reasoning)
- **Andromeda Alpha** → Revealed as NVIDIA Nemotron Nano 2 VL
- **Sonoma Dusk/Sky Alpha** → 2M context frontier models
- **Horizon Beta** → Improved version of Horizon Alpha
- **Cypher, Optimus, Quasar Alpha** → Various all-purpose models

**Pattern benefits:**
- Community feedback without brand bias
- Free usage during testing
- Early access to frontier models

**Trade-off:** All prompts/completions logged for training.

## Use Cases

### 1. Cost Optimization
**Pattern:** Let router choose cheapest model that works
- 67.8% traffic → Flash Lite (cheapest)
- Complex tasks → Premium models automatically
- No manual model switching

### 2. Best-of-Breed Routing
**Pattern:** Get optimal model for each prompt type
- Coding → GPT-5, Claude Opus 4.5
- Simple QA → Gemini Flash
- Reasoning → DeepSeek R1, Kimi K2 Thinking
- Vision → Gemini 3 Pro, GPT-4o

### 3. Reliability
**Pattern:** Automatic failover
- If model down, router picks alternative
- No API changes needed
- Transparent handling

### 4. Future-Proofing
**Pattern:** New models automatically available
- No code changes
- Routing improves over time
- Always using best available

### 5. Multi-Modal Workflows
**Pattern:** Single API for text/image/audio/video
- Router filters for capability
- Handles format differences
- Unified error handling

## Key Innovations

### 1. Zero-Configuration Routing
**Different from:** Manual model selection
- No need to track model releases
- No need to benchmark
- Router handles optimization

### 2. Cost-Aware Selection
**Evidence:** 67.8% traffic to cheapest model
- Doesn't default to most expensive
- Balances cost vs. quality
- Transparent pricing (pay routed model rate)

### 3. OpenAI-Compatible Standard
**Benefit:** Drop-in replacement
- Change base URL only
- No code rewrite
- Access to 300+ models

### 4. Cloaked Model Testing
**Innovation:** Unbranded early access
- Removes brand bias from feedback
- Community-driven improvement
- Accelerates model launches

## Pricing Model

### Base Cost
**Display:** $0/M tokens (input + output)

### Actual Cost
**Reality:** Charged at routed model's rate
- Flash Lite: ~$0.001/M tokens (very cheap)
- Claude Opus 4.5: ~$15-30/M tokens (expensive)
- Average cost depends on prompt mix

### Transparency
**Verification:**
- Activity page shows actual models used
- Response `model` attribute
- Billing shows per-model costs

## Technical Details

### Context Length
**Max:** 2,000,000 tokens
- Routes to models with sufficient context
- Some models in pool support full 2M
- Others less (router handles)

### Routing Algorithm
**Undisclosed specifics, but evidence suggests:**
- Analyzes prompt complexity
- Checks required capabilities (vision, tools, etc.)
- Balances cost vs. quality
- Prefers fast, cheap models when appropriate
- Escalates to premium for complex tasks

### Third-Party SDK Support
**Available via:**
- LangChain
- LlamaIndex
- Continue.dev
- Other frameworks

See: /docs/guides/community/frameworks-and-integrations-overview

## Comparison to Other Routing Services

| Feature | OpenRouter Auto | Martian | Not Diamond | Direct API |
|---------|----------------|---------|-------------|------------|
| **Models** | 60+ | Limited | Limited | Single |
| **Cost** | Routed model | Fixed margin | Fixed margin | Provider rate |
| **Customization** | Yes | Limited | No | N/A |
| **OpenAI Compatible** | Yes | Yes | Yes | Varies |
| **Free tier** | Via /free router | No | No | Varies |
| **Cloaked models** | Yes | No | No | No |

## Feature Flags

### Smart Filtering
Router automatically checks if requested features supported:
- **Tool calling** → Filters to models with function calling
- **Vision** → Filters to multimodal models
- **Structured output** → Filters to JSON mode models
- **Video** → Filters to video-capable models

### Customization Options
Per docs (/docs/guides/routing/routers/auto-router):
- Restrict to specific providers
- Set price limits
- Require certain capabilities
- Exclude specific models

## Observability

### Broadcast (Now GA)
**Feature:** Send traces to observability platforms
- Announcement: Banner on site
- Integration with monitoring tools
- Production-ready

### Activity Tracking
**Built-in:**
- Per-model token usage breakdown
- Historical graphs
- Cost analysis
- Model performance

## Category

AI Routing, Model Orchestration, Multi-Model API, Cost Optimization, OpenAI-Compatible

## Related

- **Service:** OpenRouter, Inc
- **Router models:** Auto, Free, Body Builder
- **Cloaked models:** 10+ alpha/beta testing models
- **SDK:** @openrouter/sdk
- **Competitors:** Martian, Not Diamond, Portkey
- **Integration:** OpenAI SDK, LangChain, LlamaIndex
- **Stats:** 67.8% traffic to Gemini 2.5 Flash Lite (cost optimization)
- **Pricing:** $0 shown, actually charges routed model rate

