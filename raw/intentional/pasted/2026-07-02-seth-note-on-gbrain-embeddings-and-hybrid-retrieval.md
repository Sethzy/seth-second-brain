---
type: raw_capture
source_type: pasted
title: "Seth note on GBrain embeddings and hybrid retrieval"
url: "https://x.com/ArtemXTech/status/2028330693659332615"
collected_at: 2026-07-02T07:03:24Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Seth note on GBrain embeddings and hybrid retrieval

Source: https://x.com/ArtemXTech/status/2028330693659332615

## Capture Text

how embeddings make Gbrain smarter than a plain LLM wiki

a plain LLM wiki finds pages by matching the words you typed. if the wording doesn't match, it misses the right page. gbrain adds embedding models, and that's the real upgrade

think of it as a map of meaning

an embedding turns each page into a point on that map. things that mean the same thing land in the same neighborhood, even when they use completely different words

so when you ask "how do we handle refunds", your question becomes a point too, and it lands right next to the page called "chargeback policy", because they mean the same thing. the word refund never has to appear

to answer, gbrain grabs the nearest points on the map. those are the pages you want, ranked and with sources, whether or not they share your exact words

that's the whole edge. a keyword wiki needs the word, embeddings find it by meaning

I use openai's text-embedding-3-large. $0.13 per 1M tokens, about $10 to map 100k pages. cheap for making your whole brain searchable by meaning

the wiki holds the knowledge. the embedding model is what makes it findable, at any size

wikis less than 10k pages doesn´t really need Gbrain embeddings, but when you go over that it gets much better at finding things.
