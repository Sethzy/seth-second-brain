---
type: raw_capture
source_type: x
url: https://x.com/alexgroberman/status/2057124993255997799
original_url: https://x.com/alexgroberman/status/2057124993255997799
author: "Alex Groberman"
handle: alexgroberman
status_id: 2057124993255997799
captured_at: 2026-06-20T01:02:41+08:00
published_at: "Wed May 20 15:43:12 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 12
  reposts: 48
  likes: 276
---

# X post by @alexgroberman

## Source

- Original: [https://x.com/alexgroberman/status/2057124993255997799](https://x.com/alexgroberman/status/2057124993255997799)
- Canonical: [https://x.com/alexgroberman/status/2057124993255997799](https://x.com/alexgroberman/status/2057124993255997799)
- Author: Alex Groberman (@alexgroberman)

## Verbatim Text

Google just accidentally revealed how its AI search systems actually work.

Now that none of it is a secret anymore, let’s talk about it.

With the new Google Search rolling out as we speak, it has never been more important to understand how to maximize value from this particular marketing channel. 

(If you want to see where your site stands across Google and AI search, you can do so for free here:

https://t.co/Pn764BHwyL)

Let’s start from the beginning:

Metehan Yesilyurt, who previously went viral when he expertly analyzed Perplexity’s ranking factors, recently broke down Google AI ranking factors in a blog post.

It was fascinating.

And a lot of the leaked ranking factors validate what SEO Stuff has been doing all year to get customers more traffic and sales over the past year.

https://t.co/eh1auroJF7

Basically, as noted by Yesilyurt, by selling the underlying infrastructure through a product called Google Cloud Discovery Engine (Vertex AI Search), Google revealed a lot about how its AI systems work.

If you understand what Discovery Engine exposes, you understand how Google AI Mode, AI Overviews, and future AI search features are likely ranking and retrieving your content.

I’ll talk about the 7 ranking signals below, but I advise you to read the entire blog post I’m linking to because it goes into way more helpful technical detail:

Base Ranking:

The core algorithm’s initial relevance score.

Gecko Score (Embedding Similarity):

Vector similarity between your content and the query.

Semantic match.

Jetstream (Cross-Attention Relevance):

A more advanced model that understands negation, contrast, context, and nuance better than embeddings.

BM25 Keyword Matching:

Kind of self-explanatory. Yes, keyword matching still matters.

PCTR (Predicted Click-Through Rate):

A three-tier prediction model:

Tier 1: Popularity

Tier 2: PCTR

Tier 3: Personalized PCTR (unlocked only after 100,000+ queries)

Freshness:

Time-sensitive recency scoring.

Boost / Bury Rules:

Manual ranking adjustments based on business logic.

This is the most transparent look we’ve ever had into Google’s AI ranking pipeline.

Discovery Engine also exposes the retrieval pipeline:

Max chunk size: 500 tokens (approximately 375 words)

Optional: ancestor headings travel with each chunk

Tables and images get parsed

Layout parser plus Gemini-enhanced understanding (LLM-augmented indexing)

This means every important point needs to live inside a 500-token block with clean headings and clear structure.

If your content is one massive wall of text, you’re done.

Also, I hate to be the “I told you so” guy on this, but schema matters.

For some reason it has become controversial to say this on social media, but it was obvious and now it is confirmed.

Discovery Engine shows Google processes structured data with three separate flags:

Searchable (affects recall)

Indexable (affects filtering and ordering)

Retrievable (affects what the model can output)

These are independent.

Meaning:

A field can influence ranking without being visible, or be visible without influencing ranking.

A massive hint at how Google uses structured data for AI Mode.

Also, Google revealed the 4-stage AI search pipeline:

Prepare:

Query understanding, synonym mapping (time-aware), autocomplete, NLU.

Retrieve:

Chunking, layout parsing, schema extraction, embeddings.

Signal:

The 7 signals above.

Serve:

Gemini 2.5 Flash generates the final answer, applies instructions, safety filters, related questions, and grounding rules.

Traditional Search, AI Overviews, and AI Mode are simply different configurations of this same pipeline.

So what does all this mean?

Well, it means you must optimize for three layers at once:

Layer 1: Semantic similarity (Gecko)

Your content needs to clearly match the intent of the prompts you want.

Layer 2: Cross-attention relevance (Jetstream)

Jetstream rewards:

Clear definitions

Direct answers

Contrast statements

“X vs Y”

“Best for ___”

“Without ___”

Layer 3: Chunk-level clarity

Your content must be extractable in 500-token blocks with:

Question-based headings

Two to three sentence answers

TLDR summaries

Clean HTML

Factual claims

Lists and comparisons

This is exactly what AI systems quote.

And this is exactly why SEO Stuff (https://t.co/wKpf0EILTx) works so well in AI search.

The Discovery Engine findings validate the entire SEO Stuff approach from long before this documentation was public.

Let me break down the packages through the lens of Google’s architecture:

SEO Stuff Gold Plan:

https://t.co/yEFyM0Ze7W

10 long-form, comparison-based, extractable articles

Structured in 500-token blocks

Question H2s

Two to three sentence direct answers

TLDR blocks

FAQ schema plus product schema

3 DR50+ backlinks to strengthen entity signals

Gold Plan maps to:

Gecko (semantic match)

Jetstream (cross-attention relevance)

BM25 (keyword match)

Freshness

Entity trust (for Boost/Bury)

This is the fastest path to appearing in ChatGPT, Gemini, Perplexity, and Google AI Mode.

SEO Stuff Premium Content Bundle:

https://t.co/4CAnUt07PO

60 comparison-driven articles

Structured to match the exact pattern LLMs extract

Category-defining content

Builds topical coverage and entity clarity

Creates a deep corpus for Jetstream and embeddings

Premium Bundle maps to:

Retrieval depth

Structured chunking

Ancestor heading clarity

Embedding similarity

AI model grounding

This is how you train AI systems to associate your brand with your category.

SEO Stuff Premium Backlink Bundle:

https://t.co/Z9m9D7TjES

3 DR50+ backlinks from domains LLMs already trust

Reinforces brand consistency across the web

Boosts entity recognition

Backlinks help with:

Base ranking

PCTR (popularity and trust)

Boost/Bury eligibility

Entity clarity

This is why so many customers reorder.

It works.

Google is not hiding its AI search architecture.

They literally exposed:

The signals

The ranking layers

The chunk sizes

The parsing logic

The semantic models

The engagement tiers

The answer generation flow

The brands that understand this and structure their content accordingly will run through the next era of search like absolute beasts.

And SEO Stuff (https://t.co/wKpf0EILTx) was built specifically to map to this architecture.

If AI is replacing the first click, your content must replace the first impression.

#GoogleIO📷📷 #Google📷📷 #Gemini

## Quoted Post

- URL: https://x.com/alexgroberman/status/2057085084105417187
- Author: Alex Groberman (@alexgroberman)

Google just announced the biggest upgrade to Search in over 25 years. 

For brands the opportunity here is pretty enormous.

Here is what the new Search actually looks like and how you should take advantage:

The search box now accepts text, images, files, videos, and open Chrome tabs. It expands dynamically as you type. It also anticipates your intent before you finish asking. 

This is the version of Search that SEO Stuff has been helping customers build for.   

https://t.co/eh1auroJF7

The biggest opportunity here is what happens after the search.

Google's new information agents run 24/7 in the background on behalf of your buyer. 

And that's why it has never been more important to understand how Google, ChatGPT, Claude and every other AI platform sees your brand.   

(If you want to see where your site stands across Google and AI search, start here:   

 https://t.co/Pn764BHwyL)

Here is exactly how Google's new information agents work:

Step 1: The buyer does a total brain dump of what they want to stay updated on. Essentially a full description of their problem, their category, their needs.

Step 2: The agent breaks down that question and maps out a plan across every relevant sub-topic.

Step 3: It determines urgency and what kind of intel the buyer needs right now versus later.

Step 4: It sets triggers and monitors the web continuously, scanning blogs, news sites, and social posts for relevant information as it changes.

Step 5: It sends the buyer an intelligent synthesized update with links and the ability to take action.

Here is why this is a massive opportunity:

AI Mode already has 1 billion monthly users. Queries are more than doubling every quarter. And multiple studies have shown that users arriving via AI search are more likely to convert. 

With information agents running continuously for over a billion users, the brands in that cited source pool are being recommended around the clock, automatically, to buyers who are actively monitoring their category.

The brands that build content depth and editorial authority now are building a presence that buildings on itself 24 hours a day.

This is what SEO Stuff builds for every customer. 

https://t.co/zvZUfkYWT4

Content that covers every sub-question a buyer in your category asks, so the agent finds you at every step of its plan. 

Authority building from trusted websites that signal credibility to every retrieval system Google has ever built.

One investment. Continuous recommendations. Around the clock.

Check it out:

https://t.co/wKpf0EILTx

Our most popular done-for-you package: https://t.co/yEFyM0Ze7W

Our done-for-you "content only" package: https://t.co/4CAnUt07PO

There is a reason more than 80 percent of SEO Stuff customers reorder. The results continue long after the work is done.

#GoogleIO📷📷📷 #Google📷📷📷

## Media

- photo: https://pbs.twimg.com/media/HIxfTkRaYAAXWpM.jpg
- photo: https://pbs.twimg.com/media/HIxfaxaaoAEzkC8.png
- photo: https://pbs.twimg.com/media/HIxfiMVbIAAlqYh.jpg
- photo: https://pbs.twimg.com/media/HIxfotebkAAfDUP.jpg

## Capture Note

TweetDetail returned complete normal-post text.
