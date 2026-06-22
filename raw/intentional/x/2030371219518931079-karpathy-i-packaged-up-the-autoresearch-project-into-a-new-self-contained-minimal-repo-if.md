---
type: raw_capture
source_type: x
url: https://x.com/karpathy/status/2030371219518931079
original_url: https://x.com/i/status/2030371219518931079
author: "Andrej Karpathy"
handle: karpathy
status_id: 2030371219518931079
captured_at: 2026-06-19T21:43:07+08:00
published_at: "Sat Mar 07 19:53:15 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1053
  reposts: 3623
  likes: 28324
---

# X post by @karpathy

## Source

- Original: [https://x.com/i/status/2030371219518931079](https://x.com/i/status/2030371219518931079)
- Canonical: [https://x.com/karpathy/status/2030371219518931079](https://x.com/karpathy/status/2030371219518931079)
- Author: Andrej Karpathy (@karpathy)

## Verbatim Text

I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then:

- the human iterates on the prompt (.md)
- the AI agent iterates on the training code (.py)

The goal is to engineer your agents to make the fastest research progress indefinitely and without any of your own involvement. In the image, every dot is a complete LLM training run that lasts exactly 5 minutes. The agent works in an autonomous loop on a git feature branch and accumulates git commits to the training script as it finds better settings (of lower validation loss by the end) of the neural network architecture, the optimizer, all the hyperparameters, etc. You can imagine comparing the research progress of different prompts, different agents, etc.

https://t.co/YCvOwwjOzF
Part code, part sci-fi, and a pinch of psychosis :)

## Media

- photo: https://pbs.twimg.com/media/HC1KyorbEAAoGWr.jpg

## Capture Note

TweetDetail returned complete normal-post text.
