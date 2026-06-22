---
type: raw_capture
source_type: x
url: https://x.com/PawelHuryn/status/2031801444064543156
original_url: https://x.com/PawelHuryn/status/2031801444064543156
author: "Pawe\u0142 Huryn"
handle: PawelHuryn
status_id: 2031801444064543156
captured_at: 2026-06-19T21:43:35+08:00
published_at: "Wed Mar 11 18:36:27 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 3
  reposts: 18
  likes: 152
---

# X post by @PawelHuryn

## Source

- Original: [https://x.com/PawelHuryn/status/2031801444064543156](https://x.com/PawelHuryn/status/2031801444064543156)
- Canonical: [https://x.com/PawelHuryn/status/2031801444064543156](https://x.com/PawelHuryn/status/2031801444064543156)
- Author: Paweł Huryn (@PawelHuryn)

## Verbatim Text

Error Analysis: The Highest-ROI Activity in AI Engineering

85% of AI initiatives fail (Gartner, 2024).

The teams that succeed don't start by picking metrics. They start by staring at LLM traces.

Metrics like "hallucination," "helpfulness," or "toxicity" — promoted by eval vendors — are too generic. They miss domain-specific failures that actually kill products.

The teams that ship working AI do the opposite. They look at actual data. Identify failure modes. Let app-specific metrics emerge bottom-up.

I've spent 3+ months researching how — studying approaches from @HamelHusain, @sh_reya, @AndrewYNg , and Google’s PAIR  team.

This is what works in 2026.

---

# 1. How to Perform Error Analysis

Error analysis is the highest-ROI AI engineering activity.

The process is straightforward. You look at the data, label LLM logs, and classify the errors into failure modes. We repeat it until no new significant failure modes emerge:

In case you wonder, LLM traces are just full records of the LLM pipeline execution: user query, reasoning, tool calls, and the output.

For example (simplified):

> As a rule of thumb, before going further, you need ~100 high-quality, diverse traces. Those can be real data, synthetic data, or both coded with failure modes.

## Step 1: (Optional) Generate Synthetic Traces

If you have data from production, that’s great. But often, when starting product development, there is no data you can rely on.

> Warning: Don't generate synthetic data without hypotheses about where AI might fail. You can build intuition by using the product. Involve domain experts, especially in complex domains.

Very complex domains aside, as an AI PM, you should become a domain expert too.

Next:

1. Prerequisite: Start with defining at least 3 dimensions that represent where the app is likely to fail (your hypotheses)

2. Generate Tuples: You need 10-20 random combinations of those dimensions

3. Human Review: Remove duplicates and unrealistic combinations

4. Generate Queries: Generate a natural language query for each tuple

5. Human Review: Discard awkward or unrealistic queries

An example for a finance chatbot:

Finally, we run these synthetic queries through our LLM pipeline to generate traces.

In Chapter 4, I’ve shared LLM prompts to:

- Prompt 1: Generate Synthetic Tuples

- Prompt 2: Generate Synthetic Queries

---

Before we proceed, I recommend [AI Evals For Engineers & PMs](https://bit.ly/aievals2026) course I took last year:

I've participated in the first cohort together with 700+ AI engineers and PMs.  I wouldn't write this without it.

---

## Step 2: Read and Open Code Traces

The next step is using the [Open Coding](https://www.researchgate.net/publication/387687208_Open_Coding_In_Qualitative_Research) technique known from qualitative research.

For every LLM trace, write brief, descriptive notes with problems, surprises, and incorrect behaviors. At this stage, this data is messy and unstructured.

For example:

## Step 3: Axial Coding, Refine Failure Modes

Next, we want to identify patterns. Cluster similar notes and let failure modes (error categories) naturally emerge.

For example:

As Shraya Shankar and Hamel Husain notice in their book, Application-Centric AI Evals for Engineers and Technical PMs:

> “Axial coding requires careful judgment. When in doubt, consult a domain expert. The goal is to define a small, coherent, non-overlapping set of binary failure types, each easy to recognize and apply consistently during trace annotation”

You can automate the process with an LLM. In that case, always review its output.

In Chapter 4, I’ve shared an LLM prompt that will help you Refine Failure Taxonomy.

## Step 4: Re-Code Traces With Failure Modes

Go back and re-code LLM traces with new failure modes. For example:

Next, quantify failure modes. For example:

With each new iteration and more traces, you'll refine definitions and merge or split categories.

> Repeat the process (Steps 1-4) until no new failure modes & no changes in re-coding appear. We call this state theoretical saturation.

---

# 2. How to Turn Failure Modes Into App-Specific AI Metrics

Once you perform initial error analysis, you can define automated evaluators.

A good practice is that each evaluator tackles a single failure mode, evaluating a single metric.

## Step 1: Start With Analyzing Failure Type

There are two types of failure types we need to consider:

Specification Failure:

- Condition: Your instructions were unclear or incomplete.

- Action: Fix the prompt first. Don't build an evaluator yet.

Generalization Failure:

- Condition: LLM fails to apply clear, precise instructions correctly.

- Action: These are prime candidates for automated evaluators.

For example:

## Step 2: Consider Two Types of App-Specific Evaluators

There are two types of automatic evaluators to consider:

Code-Based Evals

- They are based on the logic AI engineers write (e.g., Python script)

- They evaluate objective, rule-based checks such as XML, SQL, Regex

- They are fast, cheap, objective, and deterministic

LLM-as-Judge Evals

- This type of evaluator uses another LLM as a judge

- They are perfect for complex or subjective checks

- A single, narrow failure mode

- Start with binary checks (fail/pass) - this radically simplifies the setup and eliminates problems with building alignment between human experts

Importantly, using LLM-as-Judge evals might involve significant cost. What to track and what to ignore is a product, not just engineering decision. Use common sense (#errors, impact) and consider tradeoffs.

> Each automatic evaluator targets a single failure mode. And that's how you get app-specific AI metrics you were looking for.

How do we know we can trust our Judges?

---

# 3. How to Evaluate the Evaluators

Like any model, LLM-as-Judges may hallucinate or provide incorrect information. That’s why it’s critical to align them with labels from human experts.

When it comes to quantifying the alignment, the key metrics include:

- TPR (True Positive Rate): How often does judge say "Pass" when human said "Pass"? It’s the most impactful metric to maximize alignment (statistical arguments, I don’t include them in this post)

- TNR (True Negative Rate): How often does judge say "Fail" when human said "Fail"?

Other common metrics are all based on True Positives and True Negatives:

---

# 4. LLM Prompts That Support Error Analysis

Here are three most impactful prompts to semi-automate error analysis.

Those examples are from the book Application-Centric AI Evals for Engineers and Technical PMs by Shraya Shankar and Hamel Husain, shared with authors’ permission.

## Prompt 1: Generate Synthetic Tuples

Generate 10 random combinations of (feature, client persona, scenario) for a real estate CRM assistant.

The dimensions are:

- Feature – what task the agent wants to perform.
Possible values: property search, market analysis, scheduling, email drafting.

- Client persona – the type of client the agent is working with.
Possible values: first-time homebuyer, investor, luxury buyer.

- Scenario – how well-formed or challenging the query is.
Possible values:
- exact match (clearly specified and feasible)
- ambiguous request (unclear or underspecified)
- shouldn’t be handled (invalid or out-of-scope)

Output each tuple in the format: (feature, client persona, scenario)

Avoid duplicates. Vary values across dimensions. The goal is to create a diverse set of queries for our assistant.

## Prompt 2: Generate Synthetic Queries

We are generating synthetic user queries for a real estate CRM assistant. The assistant helps agents manage client requests by searching listings, analyzing markets, drafting emails, and reading calendars.

Given:

- Feature: Scheduling

- Client Persona: First-time homebuyer

- Scenario: Ambiguous request

Write a realistic query that an agent might enter into the system to fulfill this client’s request. The query should reflect the client’s needs and the ambiguity of the scenario.

Example:
"Find showings for affordable homes with short notice availability."

Now generate a new query.

## Prompt 3: Refine Failure Taxonomy

Below is a list of open-ended annotations describing failures in an LLM-driven real estate CRM assistant.

Please group them into a small set of coherent failure categories, where each category captures similar types of mistakes. Each group should have a short descriptive title and a brief one-line definition.

Do not invent new failure types; only cluster based on what is present in the notes.

---

You can never stop looking at data.

The teams that fail outsource evals to vendors and generic metrics. The teams that win read traces, label failures, and build evaluators around what they find.

AI evals isn't engineering. It's product judgment.

The team that won't read traces is the team whose product joins the 85%.

## X Article Metadata

- Title: Error Analysis: The Highest-ROI Activity in AI Engineering
- Preview: 85% of AI initiatives fail (Gartner, 2024).
The teams that succeed don't start by picking metrics. They start by staring at LLM traces.
Metrics like "hallucination," "helpfulness," or "toxicity" —

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
