---
type: raw_capture
source_type: x
url: https://x.com/arpit_bhayani/status/2010923602561077702
original_url: https://x.com/arpit_bhayani/status/2010923602561077702
author: "Arpit Bhayani"
handle: arpit_bhayani
status_id: 2010923602561077702
captured_at: 2026-06-19T19:58:16+08:00
published_at: "Tue Jan 13 03:55:22 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 27
  reposts: 43
  likes: 754
---

# X post by @arpit_bhayani

## Source

- Original: [https://x.com/arpit_bhayani/status/2010923602561077702](https://x.com/arpit_bhayani/status/2010923602561077702)
- Canonical: [https://x.com/arpit_bhayani/status/2010923602561077702](https://x.com/arpit_bhayani/status/2010923602561077702)
- Author: Arpit Bhayani (@arpit_bhayani)

## Verbatim Text

Looks like filesystems are the next big thing in AI :) Everybody is playing with it.

This is happening because models are trained heavily on coding tasks inside sandboxed environments with shells and filesystems. Hence, they get really good at navigating directories, reading files, running shell commands, and chaining operations together.

Now, if your non-coding agent has a similar setup, it inherits all of that capability for free. The model already knows how to work in this environment - we're just giving it different data to work with.

We are now seeing that Anthropic, Vercel, and Turso are all moving in this direction.

To pull this off, you need a virtual filesystem that structures your data. FUSE (Filesystem in Userspace) does exactly this - it looks like a real filesystem to the OS, but you control what's behind it.

The neat part: when your agent runs, say, `ls /workspace/data`, that call hits your FUSE layer, which translates it into a query against your actual backend.

Agents can also create scratch files (like to-do lists) to organize their thoughts, and you can compact old conversation context into files that the agent re-reads when needed. Pretty neat!

And more importantly, the Unix paradigm just gives good tool design. Instead of building separate search, write, move, and list tools, you just give the agent bash and let it figure things out.

This is something I am digging deeper (sorry, exploring) into right now to see if we can come up with something here. If this sounds interesting, FUSE is just a Google search away; it is a pretty popular OSS utility.

Also, look up 'file systems for agents', pretty interesting rabbit hole.

## Capture Note

TweetDetail returned complete normal-post text.
