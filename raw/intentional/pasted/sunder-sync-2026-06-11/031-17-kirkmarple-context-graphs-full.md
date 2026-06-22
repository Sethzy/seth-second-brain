---
type: raw_capture
source_type: x
title: "Sunder sync: 17-kirkmarple-context-graphs-FULL.md"
url: "https://x.com/KirkMarple"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/17-kirkmarple-context-graphs-FULL.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/17-kirkmarple-context-graphs-FULL.md"
sha256: "264e2b788a5f099a908b6ce6814e868b5cc181baccedc0e55fd8d74e2b87fb66"
duplicate_of: ""
---

# Sunder sync: 17-kirkmarple-context-graphs-FULL.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/17-kirkmarple-context-graphs-FULL.md`

Primary URL: https://x.com/KirkMarple

Duplicate of existing source-map entry: `none`

## Capture Text

# Kirk Marple - Context Graphs: What the Ontology Debate Gets Wrong

**Author:** Kirk Marple (@KirkMarple)
**Posted:** 3:44 PM · Jan 5, 2026
**URL:** https://x.com/KirkMarple (Twitter article)
**Views:** 109.5K

## Author Background

**Role:** Founder/CEO of Graphlit (@graphlit)
- Building Operational Context Layer for AI Agents
- Creator of @zine_ai app
- Ex-Microsoft, Seattle-based

## Article Title

**"Context Graphs: What the Ontology Debate Gets Wrong"**

This is the third in a series responding to the context graph conversation. Previous posts:
1. "The Context Layer AI Agents Actually Need"
2. "Building the Event Clock"

---

## Core Thesis

**Simple argument:** Entity ontologies are largely solved by existing standards. The real unsolved work is temporal validity, decision traces, and fact resolution. Learning helps there—not at the entity layer.

**The dichotomy isn't prescribed vs learned. It's adopt foundations, then learn what's novel.**

---

## The Debate as Currently Framed

### Two Camps Emerging

**Camp 1: Prescribed Ontologies (Palantir Model)**
- Define schema upfront
- Map messy enterprise data into it
- Deploy forward engineers for customization
- **Result:** Works but expensive, slow, doesn't scale
- **Example:** Palantir's $400B+ company

**Camp 2: Learned Ontologies (The Future Vision)**
- Structure emerges from how work actually happens
- Agent trajectories as training data
- Decision traces compile into organizational world models
- Ontology isn't prescribed—it's discovered

### Key Quote from Jaya Gupta (@JayaGup10)

"The next $50B company will be built on learned ontologies. Structure that emerges from how work actually happens, not how you designed it to happen... Memory assumes you know what to store and how to retrieve it. But the most valuable context is structure you didn't know existed until agents discovered it through use."

### Animesh Koratana's Technical Framing

Five coordinate systems that don't share keys:
1. Timeline
2. Events
3. Semantics
4. Attribution
5. Outcomes

**Argument:** Agent trajectories are training signal for learning embeddings that encode "join-compatibility" across coordinate systems. Ontology emerges from the walks.

---

## The False Dichotomy

**What's missing:** A third option that's been hiding in plain sight:

**Adopt what exists. Extend where needed. Focus learning on what's genuinely novel.**

The conversation ignores twenty years of ontology work that already exists.

---

## The Ontologies That Already Exist

### 1. Schema.org

**What it is:**
- Collaborative vocabulary for structured data on the web
- Founded 2011 by Google, Microsoft, Yahoo, Yandex
- Defines canonical types: Person, Organization, Place, Event, Product, CreativeWork, hundreds more

**Production scale:**
- Billions of web pages use it
- Powers Google rich snippets (event dates, product prices, recipe ratings)
- Well-defined types with established relationships

**Example structure:**
- Person: name, jobTitle, worksFor (→ Organization)
- Organization: name, location, employees
- Event: startDate, endDate, location, organizer

**Status:** Not theoretical—in production, maintained, designed for entity modeling

### 2. WAND and Microsoft Common Data Model

**Surprising fact:** Microsoft's Common Data Model (CDM)—powering Dynamics 365, Power Platform—was licensed from WAND.

**WAND background:**
- Building enterprise taxonomies and ontologies for decades
- Predates current AI wave by years

**When Microsoft needed canonical data model:**
- Account, Contact, Lead, Opportunity, Case, Product, Campaign
- They didn't build from scratch—they licensed from WAND

**CDM defines entities for enterprise software:**
- Not in theory—in production
- Thousands of organizations running Microsoft business applications

**Significance:** Enterprise ontology problem has been worked on for decades by people who deeply understand business operations modeling.

### 3. Industry-Specific Standards

**Healthcare:**
- **FHIR** - Clinical data exchange
- **SNOMED** - Medical terminology
- Defines: patients, conditions, medications, observations, clinical workflows

**Finance:**
- **FIBO** - Financial instruments and business entities

**Other domains:**
- Manufacturing, logistics, energy—each has domain-specific standards
- Not academic exercises—production infrastructure

**Key point:** Work of defining "what is a Patient, Medication, Account" has been done repeatedly, carefully, over decades.

---

## What Palantir Actually Does

### Daniel Davis's Observation

"I don't know why everyone thinks Palantir has ontology tech. They do not. They take months, if not years, building it with 'forward deployed engineers'. This is not the way to achieve context graphs at scale."

### The Real Issue

**Palantir's expense isn't because "prescribed ontologies are hard."**

It's because they build custom for every deployment:
- Not leveraging existing standards
- Creating bespoke models for each customer
- Business model choice, not inherent property of prescribed ontologies

**Alternative approach:**
- Adopt Schema.org types
- Extend with CDM patterns
- Add domain-specific entities
- No need for years of custom modeling

**The bottleneck:** Refusing to leverage what already exists (not the prescribed ontology itself)

---

## Where Learned Ontologies Actually Help

### Not at the Entity Layer

**Entities don't need to be learned:**
- Person, Organization, Account, Contact, Event are stable
- Core relationships well-understood
- Waiting for agent trajectories to "discover" these = waiting for search engine to discover nouns

### The CRM Lesson

**CRM customization = ontology modeling**

When companies set up modern CRMs (Attio, HubSpot, Salesforce):
- Define custom objects and relationships
- VC firm: Funds, Investments, Portfolio Companies, LPs
- Recruiting: Candidates, Positions, Clients, Placements
- Real estate: Properties, Listings, Buyers, Agents

**This is practical ontology design**

### AI-Native CRM Wave

**Startups trying to shortcut this:**
- Lightfield
- Clarify
- Forge AI
- Day.ai

**Pitch:** Don't configure schema upfront—let system figure it out

**But even aggressive "self-building CRM" assumes:**
- "Deal" has stages
- "Contacts" belong to "accounts"
- "Activities" connect people to opportunities

**Core objects are stable** across businesses (Salesforce ≈ HubSpot ≈ Attio standard objects)

### Where Inference Genuinely Helps

**Organizational-specific layer:**
- Which contacts at account actually matter for this deal?
- What's the real decision-making process (vs org chart)?
- Which exceptions get approved?
- What precedents govern decisions?

**This is tacit knowledge:**
- Specific to how this organization operates
- Lives in people's heads, Slack threads, escalation patterns
- Not in any ontology

**Example:** Not "discover that Account is an entity" but "discover that Sarah Chen is actual decision-maker even though CRM says it's her boss"

### Two Different Problems

**1. Entity modeling:** What types exist, how do they relate?
- **Status:** Solved (or solvable with existing standards)

**2. Organizational intelligence:** How does this specific organization work?
- **Status:** Genuinely novel, requires learning

**They're not the same thing. Don't require same approach.**

---

## The Bootstrap Problem

**Catch-22:** Can't learn from agent trajectories until agents run effectively. But agents can't run effectively without foundational context.

### Kirk's Previous Point

"You can't wait for thousands of agentic RAG runs to 'discover' that Sarah Chen is a person who works at Acme Corp. You need to know that before agents start reasoning. Otherwise every agent trajectory is fighting the identity resolution problem anew—and you're paying for that confusion in tokens, latency, and errors."

### The node2vec Analogy

**What node2vec does:**
- Learns embeddings from walk patterns over existing edges
- Doesn't discover nodes and edges from scratch
- **The graph must exist first**

**Same for agentic workflows:**
- Agent harness orchestrates tool calls over pre-built map
- Map = operational context (resolved entities, relationships, temporal state)
- **Build map first, then agents walk it effectively**

### The Practical Answer

**Not:** "Run agents and let structure emerge" (no clean bootstrap)

**Instead:**
1. Adopt existing ontologies as foundation
2. Start with Schema.org types for entities
3. Use CDM patterns for enterprise objects
4. Extract entities using established types
5. Resolve identities (Sarah in email = Sarah in Slack)
6. **Build the graph**
7. **Then** run agents
8. **Then** learn from trajectories

**Trajectories teach what ontology couldn't:**
- Which relationships matter most
- Which patterns recur
- Which exceptions become precedent

**This isn't prescribed vs learned. It's adopt, then learn. Foundations first, intelligence on top.**

---

## What's Actually Unsolved

If entity modeling is solved by existing standards, what's genuinely novel?

### 1. Temporal Validity

**The problem:**
- Most systems: what's true now
- Almost none: what was true at specific past point, or how truth evolved

**Example:**
- "Paula works at Microsoft" is incomplete
- When did she start? Does she still? What was true in 2022?

**This is the "event clock"** (Animesh Koratana):
- Infrastructure for tracking state changes over time
- Facts with `validAt` and `invalidAt` timestamps
- Query capability: "What did we believe about this account when we made that decision?"

**Existing ontologies don't solve this:**
- Schema.org defines Person/Organization but not "this relationship was true from date X to Y"
- CDM models Account/Contact but doesn't track attribute evolution

**Status:** Genuinely novel infrastructure that needs to be built

### 2. Decision Traces

**Foundation Capital got this right:**
- Reasoning connecting data to action has never been captured as data

**Example scenario:**
- Renewal agent proposes 20% discount (policy cap = 10%)
- Pulls context from multiple systems
- Finance approves
- CRM records "20% discount"
- **Everything that made decision legible disappears:**
  - The inputs
  - Policy evaluation
  - Exception route
  - Approval chain

**Not an ontology problem—it's instrumentation:**
- Need to be in execution path where decisions commit
- Capture not just what happened but why it was allowed

**Status:** Genuinely new territory

**Missing primitives:** "This decision was made under policy v3.2 with exception approved by VP Sarah Chen based on precedent from Acme deal Q2"

### 3. Fact Resolution

**The problem:**
- Extract facts from content → get assertions (not necessarily truth)
- Content can be wrong, outdated, contradictory

**Example:**
- March email: "Customer is renewing"
- September Slack: "Customer churned"
- Both are facts extracted from content
- Can't both be currently true

**Fact resolution = determining:**
- What's canonical
- What's superseded
- What's corroborated

**Requires judgment about:**
- Temporal validity
- Source authority
- How later information updates earlier assertions

**Status:** Not ontology work—different kind of problem (maintaining coherent beliefs as evidence accumulates)

---

## Why This Matters for Builders

### Demand Side (Aaron Levie, Box)

"In the 21st century, one of the most critical forms of competitive advantage will be a company's ability to capture, manage, and build processes around the right context."

**Reality:** Enterprises waking up to fact that AI agents only as good as context they receive

### Where to Spend Effort

**"Learned ontology" framing suggests:**
- Focus on trajectory capture
- Embedding learning
- Emergent structure
- Build infrastructure for agents to discover ontology through use

**Kirk's alternative:**

**Focus on what's actually unsolved:**

1. **Entity modeling?** Adopt existing standards
   - Don't spend months defining what Account is
   - Microsoft already licensed from WAND

2. **Temporal validity?** This is where the work is
   - Facts that change over time
   - Query historical state
   - The event clock

3. **Decision traces?** This is where the opportunity is
   - Being in execution path
   - Capturing reasoning as data

4. **Fact resolution?** This is where hard AI problems live
   - Using LLMs to determine canonical truth
   - What's superseded
   - Synthesize timeline facts from scattered observations

5. **Organizational learning?** Trajectories genuinely help here
   - But on top of foundation, not instead of one

**Winners:** Companies that adopt what exists and focus innovation on what's genuinely new

---

## What Graphlit Is Building

**Context:** Building since 2021

### Ontology Was Never the Bottleneck

**Adopted Schema.org types early:**
- Person, Organization, Place, Event
- Serialized as JSON-LD
- Not religious about RDF/triplestores
- Cart types and relationships
- JSON with `@type` field = Schema.org compatibility without semantic web stack learning curve

### What Reality Forced Them to Build

**Hybrid storage system:**
- Entities live simultaneously in:
  - Vector store
  - JSON metadata store
  - Graph store

**Enables querying across multiple axes:**
1. **Temporal:** When was this true?
2. **Geospatial:** Where did this happen?
3. **Semantic:** What's similar?
4. **Full-text:** What mentions this term?
5. **Graph:** How does this connect?

**Why necessary:**
- Most systems pick 1-2 axes
- Organizational knowledge exists across all simultaneously
- Example: Sales meeting
  - Specific time
  - Specific city
  - About specific account
  - Semantic content relating to other conversations
  - Connected to people/products in relationship graph
- **Need to query all together**

### Current Focus Areas

1. **Temporal layer** that existing ontologies lack
2. **Decision traces** extension
3. **MCP server** in context-retrieval path for agents
   - Capture content they access
   - Capture reasoning patterns they exhibit
4. **Fact resolution** - LLM-powered infrastructure
   - Determine what's currently true from accumulated assertions
   - Synthesize timeline facts from scattered observations
   - Maintain coherence as evidence accumulates

**Key insight:** Ontology foundation wasn't the hard part (Schema.org gave them that)

**Hard part:** Everything after—time, decisions, resolution, learning

---

## The Semantic Web Finally Won

### Historical Context

**Semantic web community working on these problems for decades:**
- RDF, OWL, linked data
- Schema.org emerged from this tradition
- Vision: machines reasoning over structured, interoperable data
- Not invented by AI crowd in 2024

### Academic Lineage

**"Context graph" term has pre-existing academic history:**
- June 2024 arXiv paper formally introduces Context Graphs
- Extension of knowledge graphs incorporating:
  - Temporal validity
  - Geographic location
  - Source provenance
- Exactly the dimensions missing from triple-based representations
- Demonstrates: contextual layer significantly improves reasoning performance

**Foundation Capital popularized for enterprise AI what was already formalized in research**

### What Killed Adoption

**Not the ideas—the syntax:**
- RDF, SPARQL, OWL = brutal learning curve
- Most developers never climbed it

### What Changed: LLMs

**LLMs as the enabling layer:**
- Read JSON-LD natively
- Understand Schema.org types from training data
- Reason over structured data without custom query languages or formal inference engines

**Result:** Semantic web's concepts won. Syntax lost.

**JSON-LD:** Benefits without the tax

**Context graph conversation = semantic web conversation resurfacing, with LLMs making it accessible**

---

## Where We Stand

### The Dichotomy Is Too Clean

**Entities don't need to be learned—they need to be adopted:**
- Schema.org
- CDM
- WAND
- The work has been done

### What Does Need to Be Built

**The temporal and decision layer:**
- Facts that change over time
- Reasoning captured as data
- Resolution maintaining coherence

**This is genuinely novel. This is where opportunity lives.**

### Three Principles

**1. Adopt foundations, don't reinvent them**
- Entity modeling problem solved well enough
- Don't spend innovation budget rediscovering it

**2. Build the temporal layer**
- Facts with validity periods
- Queryable history
- Time as first-class dimension

**3. Focus learning on what's genuinely novel**
- Organizational patterns
- Decision dynamics
- Tacit knowledge specific to how this organization works
- Trajectories help here—on top of foundation, not instead of one

### The Choice

**Context graph vision is achievable.**

**Question:** Build on what exists or waste years rediscovering it?

**Graphlit's approach:** Clear which path they're taking

---

## Appendix: AI-Native CRMs and Learned Ontology Thesis

**Worth examining as real-world test of learned ontology thesis**

### Two Buckets

**Bucket A: Schema-evolving**

**Lightfield** (from Tome founders):
- Most explicit about inferring/evolving data structures from unstructured inputs
- "Flexible, backfilled schemas"
- "Schematizing unstructured data according to organization's needs"
- Closest to literal "learned ontology"

**Bucket B: AI-assisted configuration**

"Classic CRM model, but AI makes setup/hygiene feel zero-config":

**Clarify:**
- "The CRM that configures itself"
- Name field → AI selects type, writes instructions, autofills

**Forge AI:**
- "Describe your process, watch CRM build itself"

**Day.ai:**
- Captures communications
- Structures into CRM records automatically

**Still operates within recognizable objects:**
- Accounts, contacts, deals, activities
- AI reduces friction
- Doesn't eliminate underlying schema

### Key Distinction

**Even most aggressive "learned" approaches rely on stable foundational objects**

**Learning happens at organizational layer:**
- Which fields matter
- Which relationships get used

**Not at entity-type layer**

**Matters for broader ontology debate**

---

## Engagement Stats

- **Views:** 109.5K
- **Date:** January 5, 2026
- Part of trending context graphs discussion

---

## Key Takeaways

1. **False dichotomy:** Not prescribed vs learned—it's adopt foundations, then learn novel aspects
2. **20 years of ontology work exists:** Schema.org, CDM, WAND, industry standards (FHIR, FIBO)
3. **Palantir's cost:** Bespoke consulting, not inherent to prescribed ontologies
4. **Entity modeling:** Largely solved—don't reinvent
5. **Actually unsolved:** Temporal validity, decision traces, fact resolution
6. **Bootstrap problem:** Need foundation before learning from trajectories
7. **Learning helps at:** Organizational intelligence layer, not entity layer
8. **CRM lesson:** Even "AI-native" assumes stable core objects
9. **Semantic web won:** Concepts survived, syntax died, LLMs enabled adoption
10. **Graphlit's approach:** Schema.org foundation + temporal/decision/resolution layers

---

## Related Concepts

**Context Graphs:** Knowledge graphs + temporal validity + geographic location + source provenance

**Operational Context Layer:** Pre-built map of entities, relationships, temporal state for agents to walk

**Event Clock:** Infrastructure for tracking state changes over time with validity timestamps

**Decision Traces:** Capturing reasoning that connects data to action as structured data

**Fact Resolution:** Maintaining coherent beliefs as evidence accumulates from multiple sources

**Organizational Intelligence:** Tacit knowledge about how specific organization actually operates

---

## Technical Architecture (Graphlit)

**Storage:** Hybrid system
- Vector store (semantic similarity)
- JSON metadata store (structured data)
- Graph store (relationships)

**Query axes:**
- Temporal
- Geospatial
- Semantic
- Full-text
- Graph

**Standards adopted:**
- Schema.org types
- JSON-LD serialization

**Novel layers being built:**
- Temporal validity
- Decision traces
- Fact resolution
- Organizational learning from agent trajectories

---

## Category

Context Graphs, Knowledge Graphs, Ontologies, AI Infrastructure, Enterprise AI, Temporal Data, Decision Intelligence

---

## Related Companies/Projects

- **Graphlit** - Author's company (operational context layer)
- **Palantir** - Prescribed ontology approach
- **Microsoft** - Common Data Model (licensed from WAND)
- **WAND** - Enterprise taxonomy/ontology provider
- **Schema.org** - Web structured data vocabulary
- **AI-Native CRMs:** Lightfield, Clarify, Forge AI, Day.ai
- **Foundation Capital** - Published "Context Graphs: AI's Trillion-Dollar Opportunity"

