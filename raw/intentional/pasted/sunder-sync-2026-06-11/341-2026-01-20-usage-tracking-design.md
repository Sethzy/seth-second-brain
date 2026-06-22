---
type: raw_capture
source_type: pasted
title: "Sunder sync: 2026-01-20-usage-tracking-design.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-20-usage-tracking-design.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-20-usage-tracking-design.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/new roadmap/2026-01-20-usage-tracking-design.md"
sha256: "a16f896c458f5d32232264011fad84a3e439f56a9a268f5202452dc05754d0ed"
duplicate_of: ""
---

# Sunder sync: 2026-01-20-usage-tracking-design.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-20-usage-tracking-design.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/new roadmap/2026-01-20-usage-tracking-design.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Usage Tracking & Caps Design

## Overview

Simple usage tracking and caps for billing purposes. Track and limit:
1. **ExtendAI pages** - pages extracted via ExtendAI API (Parse + Extract)
2. **Claude tokens** - weighted token usage (input + output×5)

**Not tracked:** Gemini API (cost is trivial ~10-20x cheaper than ExtendAI).

## Pricing Tiers

> **Currency note:** Our prices are in SGD. Extend AI and Claude costs are in USD.
> Exchange rate assumption: 1 USD = 1.35 SGD

| Tier | Price (SGD) | Price (USD) | Pages/mo | Tokens/mo | Max Cost (USD) | Margin |
|------|-------------|-------------|----------|-----------|----------------|--------|
| **Growth** | $499/mo | ~$370 | 3,000 | 3M | $39 | **9.5x** |
| **Scale** | $1,500/mo | ~$1,110 | 10,000 | 10M | $130 | **8.5x** |
| **Enterprise** | Custom | Custom | Custom | Custom | - | - |

---

## Cost Basis

### Extend AI (USD)

Every page requires **Parse + Extract**. We don't use Split or Classify.

| Extend AI Tier | Parse | Extract | **Cost/Page** | Min Volume |
|----------------|-------|---------|---------------|------------|
| Starter | $0.003 | $0.007 | **$0.010** | - |
| Scale | $0.0024 | $0.0056 | **$0.008** | ? |
| Growth | $0.0018 | $0.0042 | **$0.006** | ? |

**Current assumption:** Starter tier ($0.01/page) until we negotiate volume discounts.

### Claude Sonnet 4 (USD)

- Input: $3/MTok
- Output: $15/MTok

**Token weighting formula:**
```
weighted_tokens = input_tokens + (output_tokens × 5)
```

Output costs 5x more than input, so weighting maps directly to actual cost.

| User Type | Input | Output | Weighted | Cost (USD) |
|-----------|-------|--------|----------|------------|
| Output-heavy | 0 | 600K | 3M | $9 |
| Balanced | 1.5M | 300K | 3M | $9 |
| Input-heavy | 3M | 0 | 3M | $9 |

Regardless of input/output mix, 3M weighted tokens = ~$9 USD.

### Cost Per Tier (at Starter rates)

| Tier | Pages Cost | Tokens Cost | **Total Max Cost** |
|------|------------|-------------|-------------------|
| Growth (3K pages, 3M tokens) | $30 | $9 | **$39 USD** |
| Scale (10K pages, 10M tokens) | $100 | $30 | **$130 USD** |

---

## Scaling Projections

### Assumptions

| Metric | Assumption | Rationale |
|--------|------------|-----------|
| **Avg utilization** | 60% of quota | Most SaaS users don't hit limits |
| **Tier distribution** | 70% Growth, 25% Scale, 5% Enterprise | Typical SaaS pyramid |
| **Churn** | 5%/mo | Conservative for B2B |
| **Enterprise ARPU** | $5,000 SGD/mo | Custom pricing floor |

### Unit Economics (per client, avg utilization)

| Tier | Revenue (SGD) | Avg Cost (USD) | Gross Margin |
|------|---------------|----------------|--------------|
| Growth | $499 | $23 (60% of $39) | **94%** |
| Scale | $1,500 | $78 (60% of $130) | **93%** |

### Revenue Projections

| Clients | Mix (G/S/E) | MRR (SGD) | Costs (USD) | Gross Profit (SGD) |
|---------|-------------|-----------|-------------|-------------------|
| **10** | 7/2/1 | $11,493 | ~$300 | ~$11,000 |
| **25** | 18/6/1 | $27,482 | ~$720 | ~$26,500 |
| **50** | 35/13/2 | $56,965 | ~$1,500 | ~$54,900 |
| **100** | 70/25/5 | $112,425 | ~$3,000 | ~$108,400 |

> At 50+ clients, negotiate Extend AI volume pricing (Scale/Growth tier) to boost margins further.

### Break-Even Analysis

| Fixed Cost | Amount/mo |
|------------|-----------|
| Vercel Pro | ~$20 |
| Supabase Pro | ~$25 |
| Domains/misc | ~$10 |
| **Total** | **~$55/mo** |

**Break-even: 1 Growth client covers infrastructure.**

### Volume Discount Impact

If we negotiate to Extend AI "Growth" tier at 50+ clients:

| Tier | Current Cost | With Volume Discount | Savings |
|------|--------------|---------------------|---------|
| Growth | $39 | $27 | 31% |
| Scale | $130 | $90 | 31% |

Gross margin increases from ~93% to ~95%.

## Requirements

- Hard block when limit reached (no soft warnings)
- Monthly rolling reset (1st of each month)
- Per-user configurable limits
- Modal with "Contact Support" when limit hit
- Billing page showing current usage

## Data Model

### Usage Limits (in code)

Extend `ClientConfig` in `src/config/types.ts`:

```typescript
export interface ClientConfig {
  id: string;
  name: string;
  tags: TagDefinition[];

  /** Monthly usage limits for this client */
  usageLimits: {
    /** Max ExtendAI extraction pages per month */
    pagesPerMonth: number;
    /** Max weighted tokens per month (input + output×5) */
    tokensPerMonth: number;
  };
}
```

### Usage Tracking (in database)

New `user_usage` table:

```sql
CREATE TABLE user_usage (
  user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,

  -- Running totals for current period
  pages_used INT DEFAULT 0,
  tokens_used BIGINT DEFAULT 0,  -- weighted: input + output*5

  -- Period tracking (resets monthly)
  period_start DATE NOT NULL DEFAULT date_trunc('month', now())::date,

  updated_at TIMESTAMPTZ DEFAULT now()
);

-- RLS: users can only read their own usage
ALTER TABLE user_usage ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own usage"
  ON user_usage FOR SELECT
  USING (auth.uid() = user_id);
```

### RPC Functions

```sql
-- Check usage and auto-reset if new period
CREATE FUNCTION get_my_usage()
RETURNS TABLE (pages_used INT, tokens_used BIGINT, period_start DATE)
LANGUAGE plpgsql SECURITY DEFINER
AS $$
DECLARE
  current_period DATE := date_trunc('month', now())::date;
BEGIN
  -- Upsert: create row if not exists, reset if stale period
  INSERT INTO user_usage (user_id, pages_used, tokens_used, period_start)
  VALUES (auth.uid(), 0, 0, current_period)
  ON CONFLICT (user_id) DO UPDATE SET
    pages_used = CASE
      WHEN user_usage.period_start < current_period THEN 0
      ELSE user_usage.pages_used
    END,
    tokens_used = CASE
      WHEN user_usage.period_start < current_period THEN 0
      ELSE user_usage.tokens_used
    END,
    period_start = current_period,
    updated_at = now();

  RETURN QUERY
  SELECT u.pages_used, u.tokens_used, u.period_start
  FROM user_usage u
  WHERE u.user_id = auth.uid();
END;
$$;

-- Increment pages used (call after successful ExtendAI extraction)
CREATE FUNCTION increment_pages_used(page_count INT)
RETURNS void
LANGUAGE plpgsql SECURITY DEFINER
AS $$
BEGIN
  UPDATE user_usage
  SET pages_used = pages_used + page_count, updated_at = now()
  WHERE user_id = auth.uid();
END;
$$;

-- Increment tokens used (call after successful Claude call)
-- Pass weighted tokens: input_tokens + (output_tokens * 5)
CREATE FUNCTION increment_tokens_used(token_count BIGINT)
RETURNS void
LANGUAGE plpgsql SECURITY DEFINER
AS $$
BEGIN
  UPDATE user_usage
  SET tokens_used = tokens_used + token_count, updated_at = now()
  WHERE user_id = auth.uid();
END;
$$;
```

## Enforcement Logic

### Check Flow (both endpoints)

```
1. Get user's client_config_id via get_my_client_config()
2. Get limits from ClientConfig (code) via getClientConfig()
3. Get current usage via get_my_usage() RPC
4. If usage >= limit → return 429 { error: "limit_exceeded", type: "pages" | "tokens" }
5. Else → proceed with API call
6. On success → increment counter via RPC
```

### API Endpoints to Modify

| Endpoint | Check | Increment |
|----------|-------|-----------|
| `/api/gemini/process.ts` | `pages_used` vs `pagesPerMonth` | `increment_pages_used(split_count)` |
| `/api/chat.ts` | `tokens_used` vs `tokensPerMonth` | `increment_tokens_used(weighted)` |

**Token calculation in chat.ts:**
```typescript
// After streaming completes, get usage from final message
const inputTokens = message.usage.input_tokens;
const outputTokens = message.usage.output_tokens;
const weightedTokens = inputTokens + (outputTokens * 5);

await supabase.rpc('increment_tokens_used', { token_count: weightedTokens });
```

**Note:** Increment after success, not before - failed calls don't count against quota.

### 429 Response Format

```typescript
{
  error: "limit_exceeded",
  type: "pages" | "tokens",
  usage: { used: number, limit: number },
  message: "Monthly limit reached. Contact support to increase your quota."
}
```

## Frontend

### Limit Exceeded Modal

Shared component triggered on 429 response:

```typescript
// src/components/limit-exceeded-modal.tsx
interface LimitExceededModalProps {
  type: "pages" | "tokens";
  isOpen: boolean;
  onClose: () => void;
}
```

**Content:**
- Title: "Usage Limit Reached"
- Body: "You've reached your monthly {pages/AI} limit. Contact support to increase your quota."
- Button: "Contact Support" (mailto link)

### Billing Page

New route at `/billing`:

- Current usage vs limits with progress bars
- Period info (e.g., "Resets Feb 1, 2026")
- "Contact Support" link
- No self-service purchasing

**UI Example:**
```
┌─────────────────────────────────────────┐
│ Usage This Month                        │
├─────────────────────────────────────────┤
│ Document Pages                          │
│ ████████████░░░░░░░░  1,420 / 3,000    │
│                                         │
│ AI Usage                                │
│ ██░░░░░░░░░░░░░░░░░░  312K / 3M        │
│                                         │
│ Resets: February 1, 2026                │
│                                         │
│ Need more? [Contact Support]            │
└─────────────────────────────────────────┘
```

### Usage Hook

```typescript
// src/hooks/use-user-usage.ts
export function useUserUsage() {
  return useQuery({
    queryKey: ["userUsage"],
    queryFn: async () => {
      const { data, error } = await supabase.rpc("get_my_usage");
      if (error) throw error;
      return data;
    },
  });
}
```

## Default Limits

In `src/config/clients/default.ts` (Growth tier as default):

```typescript
usageLimits: {
  pagesPerMonth: 3_000,
  tokensPerMonth: 3_000_000,
}
```

Per-client overrides in their config files for Scale tier:

```typescript
// hoh-law.ts (if on Scale tier)
usageLimits: {
  pagesPerMonth: 10_000,
  tokensPerMonth: 10_000_000,
}
```

## Onboarding Integration

Update `3-onboard-config` skill to include `usageLimits` in generated config files.

Template addition:
```typescript
usageLimits: {
  pagesPerMonth: 3_000,      // Growth tier default, adjust per agreement
  tokensPerMonth: 3_000_000,
},
```

## Files to Modify

| File | Change |
|------|--------|
| `src/config/types.ts` | Add `usageLimits` to `ClientConfig` |
| `src/config/clients/default.ts` | Add default limits (Growth tier) |
| `src/config/clients/hoh-law.ts` | Add client-specific limits |
| `api/gemini/process.ts` | Add limit check before processing |
| `api/chat.ts` | Add limit check + token tracking |
| `.claude/templates/3-onboard-config/SKILL.md` | Add usageLimits to template |

## Files to Create

| File | Purpose |
|------|---------|
| `supabase/migrations/xxx_create_user_usage.sql` | Table + RPC functions |
| `src/components/limit-exceeded-modal.tsx` | Shared modal |
| `src/routes/billing.tsx` | Billing page |
| `src/hooks/use-user-usage.ts` | Usage data hook |

## Resolved Questions

1. **Pricing tiers:** Growth ($499), Scale ($1,500), Enterprise (custom)
2. **Limits:** Growth = 3K pages + 3M tokens, Scale = 10K pages + 10M tokens
3. **Token tracking:** Weighted formula (input + output×5)
4. **Billing page:** New route `/billing`

## Unresolved Questions

1. **Support contact:** Email address or support form URL for "Contact Support" link?

## Future Considerations (not in scope)

- Move limits to database for runtime changes
- Usage event logging for analytics
- Soft warnings at 80% threshold
- Self-service plan upgrades via Stripe

