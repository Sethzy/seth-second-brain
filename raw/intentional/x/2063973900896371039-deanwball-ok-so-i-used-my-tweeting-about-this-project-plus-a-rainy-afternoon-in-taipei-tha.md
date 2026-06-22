---
type: raw_capture
source_type: x
url: https://x.com/deanwball/status/2063973900896371039
original_url: https://x.com/deanwball/status/2063973900896371039
author: "Dean W. Ball"
handle: deanwball
status_id: 2063973900896371039
captured_at: 2026-06-20T00:14:10+08:00
published_at: "Mon Jun 08 13:18:19 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 12
  reposts: 5
  likes: 121
---

# X post by @deanwball

## Source

- Original: [https://x.com/deanwball/status/2063973900896371039](https://x.com/deanwball/status/2063973900896371039)
- Canonical: [https://x.com/deanwball/status/2063973900896371039](https://x.com/deanwball/status/2063973900896371039)
- Author: Dean W. Ball (@deanwball)

## Verbatim Text

Ok, so I used my tweeting about this project—plus a rainy afternoon in Taipei that kept me indoors—to experiment with more sophisticated multi-agent teams stuff.

For context: the goal of this topic is to create book-ish length (50-75k word) histories of arbitrary topics from as little as a single word (e.g. “Taiwan”). This was an early project I did with Opus 4.5 when that model first came out. It was structured largely in the way I thought about AI at the time: there are agents, and then there are chatbots. So: (1) CLI interface that allows me to pass <topic> to an LLM api (2) insert <topic> into pre-written “book outline” prompt (3) as part of the outline prompt, instruct LLM to generate prompts for each topic and subtopic within the outline (4) pass those topic prompts, along with broader context about the overall goal, to LLMs (5) format those outputs into a web UI well-suited for long form text. 

But after I tweeted about this old project, I realized that I now think of AI in an importantly different way: teams of agents collaborating rather than isolated agents that use LLMs as part of their software toolkit (though the latter is still a useful modality, tbc, it is not as primary as it used to be for me).

So I experimented with this notion: rather than “agents designing scripts to process information by deterministically bouncing text between LLM APIs,” could I design a digital organization or firm whose job is to produce books I would like on arbitrary topics? A publishing house, just for me?

Fortunately I keep quite extensive records with agents of my reading, favorite quotes from hundreds of books, and my entire library. So reasonably high-quality context for “what I would like” was extant.

As I played around with multi-agent orchestration within the coding agent apps, I found that Claude Code’s dynamic workflows feature (activated by including the word “workflow” in your prompt) had the best ergonomics. It causes the model to produce a script that defines a multi-agent hierarchy, though the complexity can be more like a corporate org chart than a simple hierarchy. The model does this, runs it, and the Claude Code CLI app gives you an elementary UI for overseeing the operations of the autonomous digital firm you have instantiated. It “just works.”

Purely as a nerd, it is incredible to watch 100s of agents go to work. In my case, I went with Opus’ off-the-bat organizational structure at first, which involved panels of fact-checkers, editors, researchers, writers, etc. Later I added additional roles and processes, including a group of “submitters” who were placed in competition with one another to write the best proposals.

It is, at the very least, a hell of a way to spend tokens—a bit more than 10 million, in the case of my refined structure.

The output was FAR better than what I used to get with decentralized LLM calls, but probably not worth a ~two OOM increase in token use. The main flaw was cybernetic in nature: the “virtual firm” still behaves too much like a bunch of isolated agents deterministically passing information between one another.

What you want, in any firm virtual or real, is for information to pass in an almost electrochemical fashion between the firm’s constitutive agents. You don’t want each agent to just have context for “the broad project as we conceived of it when we started” but rather the work as it evolves in real time. Eureka moments over here need to make their way over there; a misconception baked into the original proposal needs to be flagged and actioned in a way that is legible to all agents. Very little of this happens, and it is not easy to do as of yet without creating, essentially, layers of bureaucracy which increase costs (ha!).

In short, the way it all works is not very deep-learning-pilled. It is what Hayek would call rationalistic. Perhaps @polynoamial’s research program will push us to deep-learning-pilled, electrochemically linked multi-agent architectures.

## Quoted Post

- URL: https://x.com/deanwball/status/2063841724771053644
- Author: Dean W. Ball (@deanwball)

One of my standard agent uses is to create “mini-books” on historical topics, such as countries I visit. I have an app that allows me to name a topic or place. This feeds into a pre-written prompt that generates a syllabus written by 5.5 Pro, which is itself composed of prompts for each topic. These prompts are then fed into 5.5 Thinking, and the outputs are put into a nicely formatted website. The full output is usually the length of a short book. All I have to do is write the topic and press enter, and the whole thing appears a handful of minutes later. This is a very vanilla use of coding agents and LLMs, but it’s a remarkable capability that continues to blow my mind. I have never felt more joy in using computers than I do these days.

## Capture Note

TweetDetail returned complete normal-post text.
