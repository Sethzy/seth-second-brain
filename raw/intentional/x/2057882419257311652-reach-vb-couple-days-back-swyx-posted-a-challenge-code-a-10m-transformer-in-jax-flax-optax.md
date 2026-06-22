---
type: raw_capture
source_type: x
url: https://x.com/reach_vb/status/2057882419257311652
original_url: https://x.com/i/status/2057882419257311652
author: "Vaibhav (VB) Srivastav"
handle: reach_vb
status_id: 2057882419257311652
captured_at: 2026-06-19T23:03:49+08:00
published_at: "Fri May 22 17:52:57 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 14
  reposts: 16
  likes: 139
---

# X post by @reach_vb

## Source

- Original: [https://x.com/i/status/2057882419257311652](https://x.com/i/status/2057882419257311652)
- Canonical: [https://x.com/reach_vb/status/2057882419257311652](https://x.com/reach_vb/status/2057882419257311652)
- Author: Vaibhav (VB) Srivastav (@reach_vb)

## Verbatim Text

Couple days back @swyx posted a challenge: code a ~10M transformer in JAX/Flax/Optax, run it in free Colab, and train it on addition w/ your agent!

I gave Codex the screenshot + /goal.

It controlled Colab through Chrome, used my signed-in session, handled runtime/editing weirdness, ran the T4 job, then used subagents to audit the result.

End state: 10,652,557 params, ~19 min train, 99/100 exact random checks 🤯

Still needs cleaner evals, but autonomously babysiting the training run over chrome is pretty wild!

## Quoted Post

- URL: https://x.com/reach_vb/status/2057880274348695995
- Author: Vaibhav (VB) Srivastav (@reach_vb)

A Prompt, a Goal, and a Colab Run with Codex!

Couple days back @swyx [posted a challenge](https://x.com/swyx/status/2056478391008977404): code a roughly 10 million parameter transformer in JAX, Flax, and Optax, run it in free Colab, and train it on simple addition.

I wanted to see if Codex could turn the screenshot into a Colab run I could inspect.

I copied the prompt almost directly and added one instruction: [/goal](https://developers.openai.com/codex/cli/slash-commands#set-an-experimental-goal-with-goal). In Codex, a goal keeps the objective attached to the thread.

TL;DR: Codex created a Colab notebook with a 10,652,557 parameter decoder-only transformer. It trained for 4000 steps in 1139.5s, about 19 minutes, and reached 99/100 exact random-example accuracy plus 199/200 on a verification pass.

The 199/200 verification result came from monitored Colab output. [The source notebook also included the 100-example exact check.](https://gist.github.com/vb-openai/0a1f0dd6ee963338e18f9d2a7bafa94c)

## The prompt

The prompt asked for model code, and the task also required browser work: use the user's authenticated Chrome session, create a new Colab notebook, select runtimes, watch long-running cells, inspect saved outputs, and decide whether the printed results supported the claim.

Colab needed the user's signed-in Google state. Codex used the [Codex Chrome extension](https://developers.openai.com/codex/app/chrome-extension) for that. The extension lets Codex operate the user's Chrome browser, including pages that depend on cookies, login state, or browser-only UI.

## The first failure

The first issue was Colab editing. The notebook editor has state, autosave, runtime dialogs, keyboard focus, and Monaco editor behavior.

Codex first tried to rewrite the cell directly. Some edits appeared to land, then stale content returned. The practical fix was simple: copy the full cell, focus the editor, select all, clear, paste, and verify that the live cell contained the expected markers.

Browser inspection also became brittle while cells were running. Codex used saved notebook output and Drive metadata as a more durable evidence trail.

## The training setup

The vocabulary was exactly 13 characters: the digits 0-9, a space, +, and =. The longest possible example was 999+999=1998, so every generated sequence could be padded to a fixed length of 12. The model was a decoder-only Flax transformer with six layers, six attention heads, width 384, and MLP width 1536.

After initialization, the notebook reported:

> Parameter count: 10,652,557

That put it within the requested ~10M range without tuning the architecture after the fact.

The data generator sampled operands from 0..999 and formatted strings such as 123+456=579. It used a mix of uniform and length-balanced examples, which helped shorter numbers appear often enough during training.

The loss was answer-only: after seeing a+b=, the model learned to generate the answer digits, with a trailing space used as a stop token when there was room.

The notebook gave Codex enough feedback to tell whether training was working. It printed visible JAX devices, generated sample examples, ran three smoke steps, then trained for 4000 full steps while printing loss, token accuracy, and elapsed time every 400 steps.

## TPU, then T4

An earlier run in the session appeared to complete on a free TPU runtime. During the clean monitored rerun, Colab had no TPU backend available.

The original prompt allowed T4 as a fallback. Codex switched runtime, reran the notebook, and monitored the training until completion.

It did work out when it re-ran on T4:

> JAX devices: [CudaDevice(id=0)]
Parameter count: 10,652,557
step 4000 | loss 0.0008 | token acc 100.0% | 1139.5s
Exact random-example accuracy: 99/100 (99.0%)
Verification exact random-example accuracy: 199/200 (99.5%)

The token acc number was same-batch answer-token accuracy during training. The random-example checks gave the sequence-level signal.

The model also passed curated examples chosen to cover simple sums, carries, boundary cases, and the maximum-length result:

> 0+0=0
7+5=12
12+34=46
99+1=100
123+456=579
999+999=1998
500+500=1000
908+95=1003

Those checks showed that the notebook trained successfully and generalized across small random samples. A stronger claim would require larger evaluation buckets, or an exhaustive pass over the full 1,000,000 ordered operand-pair domain from 0..999 + 0..999.

## Audit

After the run, I asked Codex to use [subagents](https://developers.openai.com/codex/concepts/subagents) to audit the result from different angles: requirements compliance, model mechanics, data generation, evaluation quality, Colab reproducibility, notebook usability, and skeptical acceptance.

Subagents are separate agent runs for bounded review tasks. They are useful when the main thread needs several focused checks in parallel while keeping one place for synthesis and decisions.

The audit found the model design was sound for this task. The causal mask was right. The shifted language-model objective matched greedy prediction. The parameter count was in range. The vocabulary and fixed-length padding matched the prompt.

The evals needed work. The final exact checks covered 100 random examples and 200 verification examples. Both came from the same set of examples used during training. Training token accuracy came from the current batch. Space served as both padding and stop token. The notebook also needed pinned package versions, a checkpoint, and a clearer CPU fail-fast path.

P.S. Still loads to improve before this is actually useful but this directionally good!

## What Codex used

- /goal: kept a finish line attached to the thread.

- Chrome: gave Codex access to the signed-in Colab session.

- Local files and shell inspection: gave Codex a stable source to compare with the live notebook and saved outputs.

- Subagents: split the final review into focused audit passes.

## Making it reliable

If I ran this again, I would make the notebook more reliable in five ways.

First, make the runtime explicit. Print the backend, accelerator type, and package versions at the top. Fail fast on CPU. Treat TPU unavailability as a clear branch, then fall back to T4 when available.

Second, separate smoke mode from full mode. Smoke mode should run a few steps and prove the code runs. Full mode should run the actual training loop and print progress at predictable intervals.

Third, strengthen evaluation. Keep the small random check for quick feedback, then add buckets for operand length, carry behavior, result length, and boundary cases like 999+999. Add an optional exhaustive pass over all 1,000,000 operand pairs.

Fourth, save a compact result artifact. Include config, runtime, final metrics, curated examples, random-check results, and ideally a checkpoint. Notebook output is useful, but a result artifact makes the run easier to compare later.

Fifth, use Codex features as part of the run setup. Set /goal with explicit acceptance criteria. Use Chrome for authenticated Colab work. Ask Codex to inspect saved outputs when the browser gets brittle. Use subagents for a skeptical final audit.

For future Codex runs: set a goal with clear acceptance criteria, start with a smoke test, run the full job in the real environment, save a receipt, and ask for a skeptical audit.

btw: codex wrote this blogpost, created the screenshots, the tweet and everything around it, all I did was format and hit publish! 👀

## Capture Note

TweetDetail returned complete normal-post text.
