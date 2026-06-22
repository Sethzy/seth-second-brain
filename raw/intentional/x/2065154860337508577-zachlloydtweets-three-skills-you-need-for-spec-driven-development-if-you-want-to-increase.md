---
type: raw_capture
source_type: x
url: https://x.com/zachlloydtweets/status/2065154860337508577
original_url: https://x.com/zachlloydtweets/status/2065154860337508577
author: "Zach Lloyd"
handle: zachlloydtweets
status_id: 2065154860337508577
captured_at: 2026-06-12T20:01:15+08:00
published_at: "Thu Jun 11 19:31:02 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 7
  reposts: 33
  likes: 322
---

# X post by @zachlloydtweets

## Source

- Original: [https://x.com/zachlloydtweets/status/2065154860337508577](https://x.com/zachlloydtweets/status/2065154860337508577)
- Canonical: [https://x.com/zachlloydtweets/status/2065154860337508577](https://x.com/zachlloydtweets/status/2065154860337508577)
- Author: Zach Lloyd (@zachlloydtweets)

## Verbatim Text

Three skills you need for spec-driven development

If you want to increase the chances of your agent building the right thing, you should be writing specs to guide the agent.

It’s pretty simple: write product specs that describe user behavior, and tech specs that describe implementation strategy. They should be written as MD files and checked into the implementation PR so your teammates can review them.

You should use Skills for encoding this whole process.

Here’s the flow. It works inside or outside of Warp and [is all open-sourced](https://github.com/warpdotdev/common-skills/tree/main/.agents/skills/write-product-spec) to adapt as specs for your projects.

## 1. Start with a product spec using [/write-product-spec](https://github.com/warpdotdev/common-skills/blob/main/.agents/skills/write-product-spec/SKILL.md)

This Skill creates a PRODUCT.md file in a specs/<issue> directory in the current repo.

The goal of the PRODUCT.md is to specify a feature from the user’s perspective. It’s the “what” of the feature.

It should include references to Figma mocks, screenshots, etc.

The format is user stories + a very detailed list of product invariants that an agent can verify in code and potentially using computer use.

## 2. Next create a tech spec using [/write-tech-spec](https://github.com/warpdotdev/common-skills/blob/main/.agents/skills/write-tech-spec/SKILL.md)

This Skill creates a TECH.md file in the same specs directory.

The goal of the TECH.md is to specify the implementation strategy for the feature.  It’s the “how” of the feature.

It should include overall architecture guidance, specific code locations, and anything else that the agent should know when writing the code.

## 3. Ask the agent to implement the specs.

This should work with any agent, even on a lower reasoning level.

## 4. Validate the implementation matches the specs

It’s not enough to ask an agent to implement specs, you also need to make sure it did it correctly.

When reviewing the implementation PR, I use a skill in Warp for this called [/validate-changes-match-specs](https://github.com/warpdotdev/common-skills/blob/main/.agents/skills/validate-changes-match-specs/SKILL.md) that asks the agent to double check its work and respond back with any inconsistencies.

The agent then walks me through those inconsistencies and how I want to address them.

## 5. Validate using computer use

Finally, we have a specific skill we use internally for using Oz to do computer use to validate UX changes. This creates a cloud sandbox for agents to verify their work with mouse and keyboard access. We build a native desktop application in Rust, so this sandboxing is needed for agents to verify end-to-end.

You can see this in action here.

You can find these skills here [https://github.com/warpdotdev/common-skills](https://github.com/warpdotdev/common-skills) and install them:

npx skills add warpdotdev/common-skills

Would love to hear how other folks are doing this!

## X Article Metadata

- Title: Three skills you need for spec-driven development
- Preview: If you want to increase the chances of your agent building the right thing, you should be writing specs to guide the agent.
It’s pretty simple: write product specs that describe user behavior, and

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
