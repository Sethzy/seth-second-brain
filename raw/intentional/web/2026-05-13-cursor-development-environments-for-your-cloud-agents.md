---
type: raw_capture
source_type: web
title: "Development environments for your cloud agents"
url: "https://cursor.com/blog/cloud-agent-development-environments/"
canonical_url: "https://cursor.com/blog/cloud-agent-development-environments/"
vendor_blog: cursor
published_at: 2026-05-13
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Development environments for your cloud agents
Original URL: https://cursor.com/blog/cloud-agent-development-environments/
Published: 2026-05-13
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [product](/blog/topic/product)

May 13, 2026·[product](/blog/topic/product)

# Development environments for your cloud agents

![](/marketing-static/_next/image?url=%2Fmarketing-static%2Fusers%2Fswhitmore.png&w=48&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)

![](/marketing-static/_next/image?url=%2Fmarketing-static%2Fusers%2Fdavid-wetterau.png&w=48&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)

![](/marketing-static/_next/image?url=%2Fmarketing-static%2Fusers%2Fnick-bradford.png&w=48&q=70&dpl=dpl_FFFK2hzxfXJE3i4t5LNZhhoCLGPS)

Samantha Whitmore, David Wetterau & Nick Bradford · 7 min read

### Table of Contents

↑

* [Multi-repo environments](#multi-repo-environments)
* [Environment configuration as code](#environment-configuration-as-code)
* [Improved agent-led environment setup](#improved-agent-led-environment-setup)
* [Environment governance and security controls](#environment-governance-and-security-controls)
* [What's next](#whats-next)

Cloud agents are easier to parallelize than local agents, continue working when your laptop is closed, and can run autonomously in response to programmatic triggers.

But agents are only as capable as the environments they run in. An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work.

To take engineering tasks from start to finish, cloud agents need a development environment similar to the setup on your laptop: cloned repositories, installed dependencies, credentials for internal toolchains, and access to build systems. Effective development environments give agents full context on your codebase and organization, so they can test and verify their work.

![Cloud agent development environment architecture](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-agents-architecture-light.png&w=1920&q=70)![Cloud agent development environment architecture](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fcloud-agents-architecture-dark.png&w=1920&q=70)

Today we're shipping new tools for configuring cloud agent development environments. Cursor also can use these tools to set up and maintain your environments. Together, this release makes it easier for teams to run fleets of parallelized agents that handle tasks end-to-end, inside development environments you fully control.

## [#](#multi-repo-environments)Multi-repo environments

Most engineering work in the enterprise spans multiple codebases and repositories. Larger organizations running microservices often have many repos that need to move in tandem. An agent confined to a single repo has limited usefulness because it can't reason across all the required context.

Cloud agents and automations now support multi-repo environments, building off our work on [multi-root workspaces](https://cursor.com/changelog/04-24-26#multi-root-workspaces-in-agents-window). You can configure a single environment with all the repositories an agent needs for its work, with re-use across sessions. With multiple repos in scope, agents can reason about how a change in one part of the codebase affects others and work across repos to deliver, test, and verify changes.

Hear directly from some of our customers using multi-repo environments:

AmplitudeDecagonSnykBILT

We run Cursor Automations across public Slack channels at Amplitude. Multi-repo support is what makes them actually useful. An agent can investigate a reported issue, figure out which repos it touches, and open a PR with the fix in the right places with full context.

Steven Cheng

Senior Engineering Manager, Amplitude

## [#](#environment-configuration-as-code)Environment configuration as code

To make it easier to change, debug, and review environment definitions, we have improved Dockerfile-based configuration. This includes support for build secrets, making it easy to securely access private package registries directly from Dockerfiles. Build secrets are scoped to the build step and aren't passed to the running agent's environment.

We've also upgraded layer caching, so that only the updated layers of your image rebuild when you change the Dockerfile. Builds that hit the cache run 70% faster.

![Cloud agent development environment Dockerfile configuration](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fmacbook-pro-14-234-1-.png&w=1920&q=70)

For teams that don't want to write Dockerfiles from scratch, Cursor can configure the Dockerfile for you. Cursor will inspect your repos, figure out the tools and dependencies required, and produce a configuration you can edit and version. This feature is in private beta and will be rolling out to Enterprise teams over the coming weeks.

## [#](#improved-agent-led-environment-setup)Improved agent-led environment setup

As Cursor configures your environment, it will ask you questions, flag missing credentials, and validate that your environment is set up properly.

![Cursor asking questions and validating a cloud agent development environment setup](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fimproved-agent-setup.png&w=1920&q=70)

Cursor is also more aware of development environments. It will show you the version of the environment your agent is running in. If your environment configuration fails, Cursor will default to a base image with clear warning signs so that your cloud agents can keep running instead of immediately failing.

## [#](#environment-governance-and-security-controls)Environment governance and security controls

Every development environment now has its own version history that users can review and roll back. Admins can also restrict rollback permissions to admins only. An audit log captures every action team members take on environments, giving security teams full visibility into who changed what.

Egress and secrets can now be scoped at the development environment level. Teams can restrict outbound network access to a specific allowlist for one environment while leaving a different environment more permissive. Additionally, secrets configured for one environment aren't accessible from any other.

## [#](#whats-next)What's next

Today, environments are configured at a point in time and rebuilt when they fall out of sync with the codebase. We are building towards environment setups that evolve autonomously as your codebase evolves.

To get started with cloud agent development environments, read the [docs](https://cursor.com/docs/cloud-agent/setup) or visit your [cloud agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).

Filed under: [product](/blog/topic/product)

Authors: Samantha Whitmore, David Wetterau & Nick Bradford
