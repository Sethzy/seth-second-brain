---
type: raw_capture
source_type: x
url: https://x.com/dw_hensley/status/2021649993677885663
original_url: https://x.com/dw_hensley/status/2021649993677885663
author: "Daniel Hensley"
handle: dw_hensley
status_id: 2021649993677885663
captured_at: 2026-06-19T20:18:10+08:00
published_at: "Wed Feb 11 18:18:13 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 0
  reposts: 2
  likes: 4
---

# X post by @dw_hensley

## Source

- Original: [https://x.com/dw_hensley/status/2021649993677885663](https://x.com/dw_hensley/status/2021649993677885663)
- Canonical: [https://x.com/dw_hensley/status/2021649993677885663](https://x.com/dw_hensley/status/2021649993677885663)
- Author: Daniel Hensley (@dw_hensley)

## Verbatim Text

Beyond your specific point about dependencies and to the broader pre-computed information in-the-loop for agents point here: This is exactly the thesis we have.

We pre-compute context for codebases to make it impossible for agents to “not know what they don’t know” when working with a codebase. We strive to solve the exhaustiveness limitations of ad hoc or search-only methods. And we build off the raw source code (the source of truth as you say) plus stay up-to-date with each commit.

We heavily use it to research + plan for some time with Claude using our MCP before moving to implementation.

The specific flow of data, what we “pre-compute” with our “compiler,” and how it is exposed via MCP has also been a fun problem to work on:

- Symbol-level documentation with static analysis in the loop.
- Hierarchical code map with pre-computed terse descriptions for each file and folder.
- Higher-level documentation (we call these “deep context docs”) such as codebase-wide architecture docs and an LLM Onboarding Guides that are computed by exhaustive review of the codebase ahead of time and provided as an atomic reference.

The flow we find really effective: an agent (or sub-agent) first consults the codebase-wide content which, in addition to providing directly useful context, makes it aware of all of the places to go look in subsequent iterations (the benefit of exhaustiveness) for the particular task at hand. The symbol/file and navigational tools like the code map are then helpful in these subsequent iterations.

## Capture Note

TweetDetail returned complete normal-post text.
