---
type: raw_capture
source_type: x
url: https://x.com/AlfieJCarter/status/2021265258283729363
original_url: https://x.com/AlfieJCarter/status/2021265258283729363
author: "Alfie Carter"
handle: AlfieJCarter
status_id: 2021265258283729363
captured_at: 2026-06-19T20:17:44+08:00
published_at: "Tue Feb 10 16:49:25 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 119
  reposts: 10
  likes: 144
---

# X post by @AlfieJCarter

## Source

- Original: [https://x.com/AlfieJCarter/status/2021265258283729363](https://x.com/AlfieJCarter/status/2021265258283729363)
- Canonical: [https://x.com/AlfieJCarter/status/2021265258283729363](https://x.com/AlfieJCarter/status/2021265258283729363)
- Author: Alfie Carter (@AlfieJCarter)

## Verbatim Text

I just personalized 1 million emails with Claude Code.

I didn’t use any enrichment platforms. Here’s my 14-step workflow:

1. Install Python 3.11+

2. Create a GitHub account

3. Install Claude Code

4. Create API keys:
 
 → Anthropic (Claude)
 → Proxy (IPRoyal or Bright Data)
 → Company data (Clearbit, Apollo, Crunchbase)
 → Email verification (NeverBounce or Reoon)
 → Storage (AWS S3 or GCS)
 → Database (Neon, Supabase, Railway)
 → Outreach tool (Instantly, Smartlead, etc.)
 → CRM (Attio, HubSpot, etc.)
 
5. Create a new GitHub repo (“Enrichment”) and clone locally

6. Open terminal in the repo and launch Claude Code

7. Tell Claude your constraints:
 
 → Respect robots.txt
 → Rate limit requests
 → Make it resumable
 
8. Paste this prompt:

“Build a Python project that:

– Takes input.csv with linkedin_url, website_url, or company_name

– Fetches website, careers, blog, pricing

– Extracts: hiring signals, pain signals, and 1-sentence personalization hook

– Outputs output.csv

– Supports concurrency, retries, logging, resume-from-last-row”

9. Test locally:
 
 pip install -r requirements.txt
 
 python https://t.co/Z68kCSdwM7 --input input.csv --limit 10
 
10. Review output.csv and confirm hooks look good

11. Tell Claude to productionize it:
 
 → Env vars
 → Backoff + retries
 → Caching
 → Timeouts
 → do_not_contact flag
 → Unit tests
 
12. Deploy on Railway → connect repo → add API keys → deploy worker

13. Upload lead CSV → process in chunks → download enriched output.csv

14. Push enriched leads directly into your outreach tool

You now have fully personalized leads at scale. No enrichment platforms required.

Found it helpful? I run a GTM community where we share free playbooks and workflows like this weekly.

Reply “JOIN” and I’ll send you an invite.

## Capture Note

TweetDetail returned complete normal-post text.
