---
type: incomplete_capture
source_type: x
url: https://x.com/founder/status/123456789
original_url: https://x.com/founder/status/123456789
author: "Unknown"
handle: founder
status_id: 123456789
captured_at: 2026-06-19T19:38:25+08:00
published_at: "Unknown"
capture_quality: failed
status: failed
trust_lane: incomplete
---

# Failed X capture for @founder

## Source

- Original: [https://x.com/founder/status/123456789](https://x.com/founder/status/123456789)
- Canonical: [https://x.com/founder/status/123456789](https://x.com/founder/status/123456789)

## Capture Failure

The authenticated X capture path could not retrieve this status during the batch capture run.

```text
Traceback (most recent call last):
  File "/Users/sethlim/Documents/Seth Second Brain/scripts/x-capture-authenticated.py", line 247, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "/Users/sethlim/Documents/Seth Second Brain/scripts/x-capture-authenticated.py", line 223, in main
    detail = tweet_detail(status_id, creds)
  File "/Users/sethlim/Documents/Seth Second Brain/scripts/x-capture-authenticated.py", line 52, in tweet_detail
    raise RuntimeError(result.stderr.strip() or "TweetDetail failed")
RuntimeError: HTTP 422: {"errors":[{"code":"GRAPHQL_VALIDATION_FAILED","extensions":{"code":"GRAPHQL_VALIDATION_FAILED"},"message":"Internal server error"}]}
```

## Referenced From

- `raw/intentional/pasted/sunder-sync-2026-06-11/379-architecture-v2-addendum-openclaw-gaps.md:5`
- `raw/intentional/pasted/sunder-sync-2026-06-11/379-architecture-v2-addendum-openclaw-gaps.md:22`
- `raw/intentional/pasted/sunder-sync-2026-06-11/379-architecture-v2-addendum-openclaw-gaps.md:1651`
