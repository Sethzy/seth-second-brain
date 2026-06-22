---
type: raw_capture
source_type: x
url: https://x.com/jeffzwang/status/2032533039746822540
original_url: https://x.com/jeffzwang/status/2032533039746822540
author: "Jeffrey Wang"
handle: jeffzwang
status_id: 2032533039746822540
captured_at: 2026-06-19T21:43:55+08:00
published_at: "Fri Mar 13 19:03:33 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 23
  reposts: 13
  likes: 142
---

# X post by @jeffzwang

## Source

- Original: [https://x.com/jeffzwang/status/2032533039746822540](https://x.com/jeffzwang/status/2032533039746822540)
- Canonical: [https://x.com/jeffzwang/status/2032533039746822540](https://x.com/jeffzwang/status/2032533039746822540)
- Author: Jeffrey Wang (@jeffzwang)

## Verbatim Text

In my opinion, MCP is not redundant and bad performance owes mainly to skill issue:

Redundancy
The most important leverage an agent can have is amazing context engineering, and CLIs/APIs simply aren't designed to expose precise, concise interfaces for specific use cases. To achieve that, you need a client-server relationship where the client (agent) tells a server about itself and the server exposes an intelligent selection of capabilities (tools), or if the client (agent) post-filters the set of tools (in MCP, what is returned by `initialize`).

Well, MCP is such a technology! Could you hack CLIs/APIs to achieve the same thing? Sure, but they're not designed for selective exposure that minimizes an agent's context pollution. You need some new protocol layer thing that allows for that, even if that just wraps CLIs/APIs, because of this agent-specific problem. MCP!

Performance
Most of the performance issues I see in MCPs owe to bad implementation. That they promote good context engineering is a moot point if they're designed such that context gets mega polluted, and unfortunately many MCPs mega pollute context. One way this happens is exposing way too many tools - it's pretty common right now for API-wrapping MCPs to just expose every single API endpoint and request field, with some MCPs in the tens of thousands of tokens size because of this. This wouldn't be an issue if agent harnesses allowed for selective tool filtering per MCP, but most agent harnesses (e.g., Claude Code)  don't support this.

Also developers are not mindful enough of tool call response token payloads, which also need to be minimized to avoid context pollution - it is all too common for responses to constitute of the full API response payload. This has been partially mitigated by the rise of subagents but is still a major issue that often APIs/CLI based tool implementations may not have because in those implementations there are existing patterns to filter payloads.

In my personal Claude Code setup, I address these problems by 1) implementing an "MCP proxy" layer that lets me manually remove tools from MCPs, 2) implementing post tool call hooks that filter response payloads. And in the Exa MCP, we are careful to 1) return only fields that an agent needs 2) filter parsed HTML to only relevant tokens using models that we train. But these features need to be built into MCPS and agent harnesses as first class citizens.

Lastly, I will note that it is obviously the case that agents know how to use APIs/CLIs that are in their training data very well, almost always better than MCPs. But that issue should get fixed over time as LLMs get trained on more MCP data.

Overall
I tend to be relatively pro when it comes to new shit that needs to be built specifically for AIs (after all, our company is in the business of building a search engine from scratch for AIs lol). But this is my experience as someone who has thought about this way too much.

Curious for people's thoughts! Maybe I am missing something.

## Capture Note

TweetDetail returned complete normal-post text.
