---
type: raw_capture
source_type: x
url: https://x.com/cramforce/status/2010516747070349709
original_url: https://x.com/cramforce/status/2010516747070349709
author: "Malte Ubl"
handle: cramforce
status_id: 2010516747070349709
captured_at: 2026-06-19T19:58:13+08:00
published_at: "Mon Jan 12 00:58:40 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 2
  reposts: 0
  likes: 50
---

# X post by @cramforce

## Source

- Original: [https://x.com/cramforce/status/2010516747070349709](https://x.com/cramforce/status/2010516747070349709)
- Canonical: [https://x.com/cramforce/status/2010516747070349709](https://x.com/cramforce/status/2010516747070349709)
- Author: Malte Ubl (@cramforce)

## Verbatim Text

The latest version of `just-bash` is much faster when operating on real filesystems (not in-memory) with large-ish number of files.

This is thanks to @ankrgyl correctly complaining things were slow when operating on the GitHub Archive dataset.

Optimizations:
- Removed lots of stat calls in find when the caller doesn't need them
- Made find, ls -r, glob, and friends do concurrent directory traversal
- Added support for concurrent jq processing

## Capture Note

TweetDetail returned complete normal-post text.
