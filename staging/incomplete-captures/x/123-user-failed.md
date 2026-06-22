---
type: incomplete_capture
source_type: x
url: https://x.com/user/status/123
original_url: https://x.com/user/status/123
author: "Unknown"
handle: user
status_id: 123
captured_at: 2026-06-19T19:38:24+08:00
published_at: "Unknown"
capture_quality: failed
status: failed
trust_lane: incomplete
---

# Failed X capture for @user

## Source

- Original: [https://x.com/user/status/123](https://x.com/user/status/123)
- Canonical: [https://x.com/user/status/123](https://x.com/user/status/123)

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

- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:5`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:22`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:316`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:318`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:320`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:322`
- `raw/intentional/pasted/sunder-sync-2026-06-11/105-skill.md:356`
