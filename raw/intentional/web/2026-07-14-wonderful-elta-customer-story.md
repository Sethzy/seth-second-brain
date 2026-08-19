---
type: raw_capture
source_type: web
title: "Wonderful — ELTA Hellenic Post Customer Story"
url: "https://www.wonderful.ai/blog-articles/elta"
collected_at: 2026-07-23T05:20:00Z
published_at: 2026-07-14
capture_quality: complete
status: raw
trust_lane: intentional
---

# Wonderful — ELTA Hellenic Post Customer Story

> Source: https://www.wonderful.ai/blog-articles/elta
> Collected: 2026-07-23
> Published: 2026-07-14

The Wonderful Team

The Wonderful Team

|

|

![](https://framerusercontent.com/images/T54k4EojvVEexFsts17jVM2y2g.jpg?width=3000&height=2000)

Wonderful built a Greek-language AI voice agent for ELTA Hellenic Post that handles delivery tracking calls at 4X previous capacity with an 86% success rate, going from kickoff to production in 5 weeks.

ELTA Hellenic Post is Greece’s national postal operator, running a countrywide delivery network that serves millions of customers across mail, parcel, and logistics services. At that scale, delivery tracking is one of the highest-volume drivers of inbound calls, and one of the trickiest to automate. Spoken Greek tracking numbers mix alphabets and phonetics, and regional pronunciation variations in ways that trip up standard speech recognition.

ELTA’s call center was under sustained pressure. During peak periods, roughly 40% of inbound calls were dropped or abandoned because demand routinely exceeded available human agents. A previous attempt at automation had failed to reliably capture spoken tracking numbers in Greek, leaving customers frustrated and agents skeptical of automated systems. ELTA needed a production-grade solution that could handle real customer interactions reliably.

  

### Five weeks from kickoff to live customer calls

When Wonderful started scoping the project, the core challenge was clear: Greek tracking numbers combine letters and digits, and callers pronounce them differently depending on accent, pacing, and whether they’re reading off a screen or a physical receipt. Standard speech-to-text accuracy alone wasn’t going to cut it. The agent needed a structured interaction model that could collect, validate, and recover from input errors without asking the caller to start over from scratch.

### Building it

Wonderful built an AI voice agent integrated directly with ELTA’s live courier and tracking systems, enabling real-time delivery status lookup on every call. The agent collected tracking numbers through guided conversation flows, gathering long alphanumeric codes in structured digit and letter groups rather than asking for the full string in one go. For letters, it used familiar reference words to distinguish acoustically similar characters. When a customer self-corrected or mispronounced a segment, the recovery logic targeted only the incorrect portion rather than restarting the flow from the top.

The agent was built for Greek from the ground up: it handled mixed alphabets, regional accents, background noise, and the irregular pacing of real phone calls. Before the live pilot, Wonderful ran 10 days of user acceptance testing at 100 tests per day, identifying and fixing edge cases in pronunciation, digit grouping, and phonetic fallback logic. When real callers introduced new pacing patterns after go-live, the team iterated quickly and stabilized performance above 80% within weeks of launch.

### Results

- 86% resolution rate in production, sustained under full live call volume
- 4X increase in calls handled per day (from ~500 to ~2,000), with no additional headcount
- Peak waiting time cut from 10 minutes to 0 minutes
- 24/7 delivery tracking coverage, including during previously unmanageable peak demand
- Human agents freed from repetitive tracking inquiries to focus on outbound sales and complex cases
- Full production rollout completed within 5 weeks of kickoff

The ELTA deployment shows what AI in production looks like when the hard parts are taken seriously. Getting speech recognition to work reliably in Greek, under real call conditions, with real callers who don’t follow scripts, required careful agent design, structured error recovery, and fast iteration after go-live.

  
*“In less than 2 months since going live with Wonderful, we’ve scaled agentic handling of customer support by nearly 4X, while maintaining an 86% success rate in production. Because Wonderful agents now reliably handle support, the same team that used to split time between sales and service can now fully focus on revenue-generating work.”*

**Marios Tempos, Deputy CEO at ELTA Hellenic Post SA**

[![](https://framerusercontent.com/images/kQh8hfxecGXS1OsWtfuYtIRA6g8.png?width=2250&height=1500)](./wonderful-australia) [![](https://framerusercontent.com/images/4tAEEBQDDSyChrW3rYxwlJn8.png?width=2250&height=1500)](./wonderful-singapore) [![](https://framerusercontent.com/images/YNyGW3Gka5yQSpibbUltJecpdc4.png?width=3600&height=1920)](./mckinsey-and-wonderful-team-up-to-deliver-enterprise-ai-transformation-from-strategy-to-scale)

[![](https://framerusercontent.com/images/kQh8hfxecGXS1OsWtfuYtIRA6g8.png?width=2250&height=1500)](./wonderful-australia) [![](https://framerusercontent.com/images/4tAEEBQDDSyChrW3rYxwlJn8.png?width=2250&height=1500)](./wonderful-singapore) [![](https://framerusercontent.com/images/YNyGW3Gka5yQSpibbUltJecpdc4.png?width=3600&height=1920)](./mckinsey-and-wonderful-team-up-to-deliver-enterprise-ai-transformation-from-strategy-to-scale) [![](https://framerusercontent.com/images/G50hXhXGeNUNlwwrfU1aaoFlE.png?width=2250&height=1500)](./why-enterprise-ai-gets-stuck-in-pilot-mode)

