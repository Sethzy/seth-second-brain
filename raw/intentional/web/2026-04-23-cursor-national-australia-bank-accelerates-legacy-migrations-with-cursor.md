---
type: raw_capture
source_type: web
title: "National Australia Bank accelerates legacy migrations with Cursor"
url: "https://cursor.com/blog/nab/"
canonical_url: "https://cursor.com/blog/nab/"
vendor_blog: cursor
published_at: 2026-04-23
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# National Australia Bank accelerates legacy migrations with Cursor
Original URL: https://cursor.com/blog/nab/
Published: 2026-04-23
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [customers](/blog/topic/customers)

Apr 23, 2026·[customers](/blog/topic/customers)

# National Australia Bank accelerates legacy migrations with Cursor

NAB standardized 6,000 developers on Cursor after evaluating Amazon Q and GitHub Copilot. Legacy modernizations are now running 3x faster and at higher quality.

9 min read

[Contact sales](/contact-sales?source=customers)

### Table of Contents

↑

* [Evaluating Cursor for an enterprise-wide rollout](#evaluating-cursor-for-an-enterprise-wide-rollout)
* [Refactoring a legacy monolith to microservices](#refactoring-a-legacy-monolith-to-microservices)
* [Migrating core banking apps away from Assembly mainframes](#migrating-core-banking-apps-away-from-assembly-mainframes)
* [Building a hardware-agnostic payment app in 3 weeks](#building-a-hardware-agnostic-payment-app-in-3-weeks)

National Australia Bank is a Financial Services company in Asia-Pacific.

6,000+

Cursor users at NAB, scaling toward 10,000+

3x

Faster legacy migrations and refactors for banking applications

3 weeks

To build a greenfield payment app instead of a four-month scope

National Australia Bank is a Financial Services company in Asia-Pacific.

6,000+

Cursor users at NAB, scaling toward 10,000+

3x

Faster legacy migrations and refactors for banking applications

3 weeks

To build a greenfield payment app instead of a four-month scope

National Australia Bank (NAB) standardized 6,000 developers on Cursor after evaluating Amazon Q and GitHub Copilot. The engineering team is now shipping projects that were previously out of reach faster and at higher quality.

Legacy codebase modernizations like a monolith refactor to microservices and mainframe migrations away from Assembly are running three times faster than expected. Teams are also using Cursor to build greenfield projects, with one merchant services team shipping a hardware-agnostic payment app in three weeks instead of the original four month scope.

## [#](#evaluating-cursor-for-an-enterprise-wide-rollout)Evaluating Cursor for an enterprise-wide rollout

NAB was initially using Amazon Q and GitHub Copilot as their core AI coding assistants. The company then ran a broader evaluation and chose to standardize an initial cohort of 6,000 developers on Cursor for a few reasons:

* **Model flexibility:** Engineers at NAB prefer different models for different tasks based on required cost, latency, and intelligence. Cheaper models are used for routine, straightforward implementations like front-end UI changes while more expensive thinking models are used for complex, long-running tasks like architecture design.
* **Codebase understanding:** NAB has thousands of repos across multiple GitHub accounts that span different tech stacks (for example, Java, React, COBOL, Assembly). Cursor offered the fastest and most accurate agent behavior against this complex footprint.
* **Extensibility and control:** NAB has built an internal context engineering library called NAB CEL using Cursor primitives like rules, skills, and hooks. Centralizing shared knowledge in Cursor has allowed NAB to enforce development standards and set guardrails on agent behavior.

Using plugin-based coding assistants is like trying to bolt AI onto your workflow from the outside. With Cursor, the agent understands our codebase and works the way NAB works.

Chris De Lorenzo

Principal Engineer

NAB is now bringing Cursor to over 10,000 employees across its technology organization, including engineers, product managers, designers, and leadership. Each function has its own dedicated training path, allowing NAB to improve productivity across its entire organization.

We were intentional about enablement from the start, setting up tailored training sessions and sprint days where developers use Cursor on real production projects. This investment is now paying off as teams are shipping useful features to customers faster and with better quality.

Andrew Vaughan

Distinguished Engineer

## [#](#refactoring-a-legacy-monolith-to-microservices)Refactoring a legacy monolith to microservices

NAB's business lending unit uses a fee calculator application called BizCalc to price loans. The application was originally built as an on-prem monolith with the Silverlight/.NET framework. With extended support for Silverlight ending in 2026, NAB set a hard deadline to refactor BizCalc into Java microservices for the backend and React for the front end.

NAB originally scoped six months of work for the entire migration. The first two months were going to be dedicated entirely to pre-development tasks: documenting how the legacy code works, building product requirements, writing user stories, and creating an API spec for the front- and back-end services to communicate.

Coby Paterson, a principal engineer at NAB, used Cursor to complete all pre-development work in just one week. She used Ask Mode to visualize and document business logic, and Plan Mode with a custom NAB-CEL skill to create user stories and corresponding API specs. NAB then fed these artifacts into Cursor to execute the migration development and testing.

Within a week, Cursor produced better user stories and a more detailed API spec than we could have done manually after months of reverse engineering the system.

Coby Paterson

Principal Engineer

Paterson expects the full migration to finish in two months, a 3x improvement against the original estimate.

## [#](#migrating-core-banking-apps-away-from-assembly-mainframes)Migrating core banking apps away from Assembly mainframes

NAB's core banking systems that manage customer balances, interest accrual, and fees run on Assembly-based mainframe infrastructure. NAB wanted to migrate key programs off Assembly to make support, maintenance, and integration with the rest of their systems easier, but the migration project had stalled due to resource constraints.

Before Cursor, we couldn't even think about moving away from Assembly. We just didn't have the expertise or time to tackle an enormous project like this manually.

Harjot Singh

Engineering Manager

The main constraint was the Assembly expertise required to separate low-level machine instructions from business logic before attempting a rewrite. This is a manual, painstaking process that requires living in green screens, the 3270 terminal emulator GUIs that Assembly mainframes use.

With Cursor, Harjot's team generated flowcharts and business summaries directly from Assembly. The agent is fixing program by program. The Assembly migration project is now progressing 3x faster than expected.

Without Cursor, the time and cost of this migration would have been greater than the value we'd get from it.

Harjot Singh

Engineering Manager at NAB

## [#](#building-a-hardware-agnostic-payment-app-in-3-weeks)Building a hardware-agnostic payment app in 3 weeks

NAB's merchant services team wanted to build a hardware-agnostic payment application to avoid vendor lock-in. This greenfield project was originally scoped at a full four months of engineering work, largely because the team had no experience developing in Android frameworks like Kotlin.

Chris De Lorenzo, a principal engineer, used Cursor to build the project in less than three weeks. He first iterated with Cursor to build detailed product requirements and a multi-phase implementation plan that could be parallelized across subagents. He then implemented the plan using Composer and Opus coding models.

We've seen a 5-8x improvement in development velocity. But the main thing is we wouldn't have even tried to build this app without Cursor.

Chris De Lorenzo

Principal Engineer

De Lorenzo also credits Cursor for democratizing software development beyond engineers: "Cursor is the first agent platform I've seen that brings engineers, architects, product, and security into the same workflow. It's changing how we build software as an organization."

NAB is now focused on embedding Cursor into every part of the software lifecycle beyond code generation. "We want to bring Cursor to code review, quality assurance testing, and deployment. Re-thinking our engineering processes around agents is a key area of investment for NAB," said Caroline Trang, NAB's Head of AI Tooling & Delivery.

---

If you're working on automating legacy modernizations or want to move faster on greenfield projects, [reach out to start a Cursor trial](https://cursor.com/contact-sales?source=customers).

Filed under: [customers](/blog/topic/customers)

Author: Cursor Team

National Australia Bank is a Financial Services company in Asia-Pacific.

6,000+

Cursor users at NAB, scaling toward 10,000+

3x

Faster legacy migrations and refactors for banking applications

3 weeks

To build a greenfield payment app instead of a four-month scope

National Australia Bank is a Financial Services company in Asia-Pacific.

6,000+

Cursor users at NAB, scaling toward 10,000+

3x

Faster legacy migrations and refactors for banking applications

3 weeks

To build a greenfield payment app instead of a four-month scope
