---
type: raw_capture
source_type: web
title: "HAL: Holistic Agent Leaderboard"
url: "https://hal.cs.princeton.edu/"
collected_at: 2026-06-13T10:56:01Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# HAL: Holistic Agent Leaderboard

Source: https://hal.cs.princeton.edu/

## Capture Text

# HAL: Holistic Agent Leaderboard

Original URL: https://hal.cs.princeton.edu/
Fetched URL: https://hal.cs.princeton.edu/

## Fetched Content

The HAL paper has been accepted to ICLR 2026!
[Read the paper →](https://arxiv.org/pdf/2510.11977)

Explore the Reliability Dashboard — evaluate agents on consistency, robustness, safety & more.
[Explore now →](/reliability)

# HAL: Holistic Agent Leaderboard

### The standardized, cost-aware, and third-party leaderboard for evaluating agents. **Read the paper introducing HAL [here](https://arxiv.org/pdf/2510.11977).**

By the [SAgE team](https://sage.cs.princeton.edu) at Princeton University

26 597

Rollouts

9

Benchmarks

[View Leaderboards ↓](#leaderboards)
[GitHub](https://github.com/princeton-pli/hal-harness)

![HAL Hero](/static/hal_flow.png)

## Performance Highlights

Top performing agents across different benchmarks

**Update:** Running Opus 4.5 with an updated scaffold that uses Claude Code drastically outperforms the CORE-Agent scaffold we used, especially after fixing a few grading errors via manual scoring. We have now declared [CORE-Bench solved](https://x.com/sayashk/status/1996334941832089732?t=1tFle-jfHsDHFEOSjyo9mg&s=19).

**Note:** We have paused updating HAL leaderboard with new models and are currently focusing on measuring [reliability](/reliability) in AI agents.

[### AssistantBench

Web Assistance

Top 3 performing agents

Browser-Use

o3 Medium (April 2025)

38.8%

$15.15

Browser-Use

GPT-5 Medium (August 2025)

35.2%

$41.69

Browser-Use

o4-mini Low (April 2025)

28.1%

$9.22

View Full Leaderboard](/assistantbench)
[### CORE-Bench Hard

Scientific Programming

Top 3 performing agents

Claude Code

Submitted by Nicholas Carlini

Download main.py

Claude Opus 4.5

77.8%

95.5% manual

$87.16

Claude Code

Submitted by Nicholas Carlini

Download main.py

Claude Sonnet 4.5 (September 2025)

62.2%

$68.33

CORE-Agent

Claude Opus 4.1 (August 2025)

51.1%

$412.42

View Full Leaderboard](/corebench_hard)
[### GAIA

Web Assistance

Top 3 performing agents

HAL Generalist Agent

Claude Sonnet 4.5 (September 2025)

74.5%

$178.20

HAL Generalist Agent

Claude Sonnet 4.5 High (September 2025)

70.9%

$179.86

HAL Generalist Agent

Claude Opus 4.1 High (August 2025)

68.5%

$562.24

View Full Leaderboard](/gaia)
[### Online Mind2Web

Web Assistance

Top 3 performing agents

SeeAct

GPT-5 Medium (August 2025)

42.3%

$171.07

Browser-Use

Claude Sonnet 4 (May 2025)

40.0%

$1577.26

Browser-Use

Claude Sonnet 4 High (May 2025)

39.3%

$1609.92

View Full Leaderboard](/online_mind2web)
[### SWE-bench Verified Mini

Software Engineering

Top 3 performing agents

SWE-Agent

Claude Sonnet 4.5 High (September 2025)

72.0%

$463.90

SWE-Agent

Claude Opus 4.1 (August 2025)

68.0%

$1351.35

SWE-Agent

Claude Sonnet 4.5 (September 2025)

68.0%

$505.92

View Full Leaderboard](/swebench_verified_mini)
[### Scicode

Scientific Programming

Top 3 performing agents

Scicode Tool Calling Agent

o3 Medium (April 2025)

9.2%

$111.11

Scicode Zero Shot Agent

o4-mini Low (April 2025)

9.2%

$1.74

Scicode Tool Calling Agent

Claude Opus 4.1 (August 2025)

7.7%

$625.13

View Full Leaderboard](/scicode)
[### ScienceAgentBench

Scientific Programming

Top 3 performing agents

SAB Self-Debug

o3 Medium (April 2025)

33.3%

$11.69

SAB Self-Debug

Claude Sonnet 4.5 High (September 2025)

30.4%

$7.47

SAB Self-Debug

Claude-3.7 Sonnet High (February 2025)

30.4%

$11.74

View Full Leaderboard](/scienceagentbench)
[### TAU-bench Airline

Customer Service

Top 3 performing agents

HAL Generalist Agent

Claude-3.7 Sonnet (February 2025)

56.0%

$42.11

TAU-bench Tool Calling

o4-mini High (April 2025)

56.0%

$11.36

HAL Generalist Agent

Claude Opus 4.1 (August 2025)

54.0%

$180.49

View Full Leaderboard](/taubench_airline)
[### USACO

Programming

Top 3 performing agents

USACO Episodic + Semantic

GPT-5 Medium (August 2025)

69.1%

$116.63

USACO Episodic + Semantic

o4-mini High (April 2025)

64.8%

$77.28

USACO Episodic + Semantic

o4-mini Low (April 2025)

53.1%

$24.60

View Full Leaderboard](/usaco)








## Who is it for?

HAL serves four key user groups in the AI ecosystem

### Downstream Users & Procurers

* • Discover useful but less known benchmarks related to tasks you care about
* • Find out who is building strong agents on these benchmarks
* • Identify the state of the art for both cost and accuracy on these tasks

[View Leaderboards](#leaderboards)

### Benchmark Developers

* • Gain improved visibility for your benchmark
* • Incentivize agent developers to build agents for your benchmark
* • Enable cost-controlled evaluations by default without extra effort

[Add a Benchmark](https://github.com/princeton-pli/hal-harness/tree/main/hal/benchmarks)

### Agent Developers

* • Easily reproduce existing agents and perform unbiased comparisons
* • Compete on a leaderboard in a straightforward way
* • Use HAL harness for framework-agnostic agent evaluation

[Submit an Agent](https://github.com/princeton-pli/hal-harness/tree/main/agents)
[View Leaderboards](#leaderboards)

### Safety Researchers

* • Understanding agent capabilities on real-world safety threats and their associated costs

## Cost-Controlled Agent Evaluations

Understanding the cost-performance trade-off

### Why looking at the Pareto frontier matters

* •
  Agents can be 100x more expensive while only being 1% better
* •
  Downstream developers can't tell the difference from 1D leaderboards

[View full USACO leaderboard](/usaco)

Cost ($)
Performance (%)





Agent A
Agent B
Agent C





Cost-performance
frontier

## The HAL Evaluation Harness

A unified framework for reproducible agent evaluation

### Standardized Evaluation

* One-stop shop evaluation harness for all benchmarks and agents
* Flexible execution environments for running parallel evaluations locally or in the cloud

### Comprehensive Logging

* Automatic logging of agent traces with [W&B Weave](https://wandb.ai/site/weave/)
* Detailed cost tracking of token usage with minimal edits to agent code

### Developer Friendly

* Easy agent integration that does not require a specific agent framework
* Modular architecture that allows for easy extentions with new benchmarks and agents

[Get Started with HAL →](https://github.com/princeton-pli/hal-harness)

## Reliability Evaluation

Accuracy isn't enough — we evaluate agents on consistency, predictability, robustness, safety, and self-awareness

The HAL Reliability Dashboard provides a multi-dimensional view of agent behavior beyond raw accuracy scores. Explore how agents perform across reliability dimensions for every benchmark.

[View Reliability Dashboard →](/reliability)

## Agent Traces

Enabling rapid development and debugging while protecting benchmark integrity

### Complete Agent Traces

We make available the full traces of agent evaluations, including every single model call as logged by W&B Weave.

### Encrypted Distribution

All agent traces are encrypted to prevent benchmark contamination through automated scraping.

To decrypt downloaded traces:

1. Install prerequisite:
`pip install cryptography`

2. Download the script:

[Download hal-decrypt.sh](/static/downloads/hal-decrypt.sh)

3. Decrypt:

`./hal-decrypt.sh -F trace.zip`
`./hal-decrypt.sh -D traces/`

[Download on Leaderboards →](#leaderboards)

## Meet the Team

The people behind HAL

### Authors

Sayash Kapoor

Princeton University

Benedikt Stroebl

Princeton University

Peter Kirgis

Princeton University

Nitya Nadgir

Independent Researcher

Zachary S Siegel

Princeton University

Boyi Wei

Princeton University

Tianci Xue

The Ohio State University

Ziru Chen

The Ohio State University

Felix Chen

Princeton University

Saiteja Utpala

Microsoft Research

Franck Ndzomga

Independent Researcher

Dheeraj Oruganty

Amazon

Sophie Luskin

Princeton University

Kangheng Liu

Georgetown University

Botao Yu

The Ohio State University

Amit Arora

Georgetown University

Dongyoon Hahm

KAIST

Harsh Trivedi

Stony Brook University

Huan Sun

The Ohio State University

Juyong Lee

KAIST

Tengjun Jin

University of Illinois Urbana-Champaign

Yifan Mai

Stanford University

Yifei Zhou

xAI

Yuxuan Zhu

University of Illinois Urbana-Champaign

Rishi Bommasani

Stanford University

Daniel Kang

University of Illinois Urbana-Champaign

Dawn Song

University of California, Berkeley

Peter Henderson

Princeton University

Yu Su

The Ohio State University

Percy Liang

Stanford University

Arvind Narayanan

Princeton University

Stephan Rabanser

Princeton University

Andrew Schwartz

Cornflower Labs

### Acknowledgments

Aymeric Roucher

Hugging Face

Ayush Thakur

Weights & Biases

Hailey Schoelkopf

Anthropic

Iason Gabriel

Google DeepMind

Jelena Luketina

UK AISI

JJ Allaire

UK AISI

Laura Weidinger

Google DeepMind

Madhur Prashant

Amazon

Marius Hobbhahn

Apollo Research

Maximillian Kaufmann

UK AISI

Morgan McGuire

Weights & Biases

Omar Khattab

MIT

Parth Asawa

UC Berkeley

Shreya Shankar

UC Berkeley

Shayne Longpre

MIT

Veniamin Veselovsky

Princeton University

William Isaac

Google DeepMind

Charles Teague

UK AISI

Clémentine Fourrier

Hugging Face

Kevin Meng

Transluce

### Want to Contribute?

HAL is an open-source project and we welcome contributions from the community.

[GitHub](https://github.com/princeton-pli/hal-harness/blob/main/CONTRIBUTING.md)

### Cite HAL

```
@inproceedings{hal,
title =     {Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation},
author =    {Sayash Kapoor and Benedikt Stroebl and Peter Kirgis and Nitya Nadgir and Zachary S Siegel and Boyi Wei and Tianci Xue and Ziru Chen and Felix Chen and Saiteja Utpala and Franck Ndzomga and Dheeraj Oruganty and Sophie Luskin and Kangheng Liu and Botao Yu and Amit Arora and Dongyoon Hahm and Harsh Trivedi and Huan Sun and Juyong Lee and Tengjun Jin and Yifan Mai and Yifei Zhou and Yuxuan Zhu and Rishi Bommasani and Daniel Kang and Dawn Song and Peter Henderson and Yu Su and Percy Liang and Arvind Narayanan},
booktitle = {The Fourteenth International Conference on Learning Representations (ICLR)},
url =       {https://arxiv.org/pdf/2510.11977},
year =      {2026}}
```

### Funding

HAL is funded by [Coefficient Giving](https://coefficientgiving.org/), [Schmidt Sciences](https://www.schmidtsciences.org/), the [Princeton AI Lab](https://ai.princeton.edu/ai-lab), the [Princeton Language and Intelligence](https://pli.princeton.edu/) Initiative, and the [Princeton Catalysis Initiative](https://chemistry.princeton.edu/faculty-research/collaborations/princeton-catalysis-initiative/). We are grateful to OpenAI and Google for providing API credits to evaluate their models.

[![Princeton AI Lab Logo](/static/ailab.png)](https://ai.princeton.edu/ai-lab)
[![Princeton Language and Intelligence Logo](/static/pli.png)](https://pli.princeton.edu/)
