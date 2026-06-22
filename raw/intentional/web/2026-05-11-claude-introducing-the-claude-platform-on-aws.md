---
type: raw_capture
source_type: web
title: "Introducing the Claude Platform on AWS"
url: "https://claude.com/blog/claude-platform-on-aws/"
canonical_url: "https://claude.com/blog/claude-platform-on-aws/"
vendor_blog: claude
published_at: 2026-05-11
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Introducing the Claude Platform on AWS

Original URL: https://claude.com/blog/claude-platform-on-aws/
Published: 2026-05-11
Captured: 2026-06-14T02:32:25+00:00

Description: The Claude Platform on AWS is now generally available, offering a new way for AWS customers to access the full set of Claude platform features with AWS authentication, billing, and commitment retirement.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# Introducing the Claude Platform on AWS

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  May 11, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-platform-on-aws

The Claude Platform on AWS is now generally available, offering a new way for AWS customers to access the full set of Claude Platform features with AWS authentication, billing, and commitment retirement. Claude also remains available on Amazon Bedrock, where AWS is the data processor.

Starting today, Claude Platform on AWS customers can deploy agents at scale with [Claude Managed Agents](https://claude.com/blog/claude-managed-agents) and build with tools like code execution, skills, the advisor strategy, and more.

## Access the complete Claude Platform via AWS

The Claude Platform on AWS brings the full set of Claude API features to AWS customers for the first time, with all new features and betas shipping the same day they go live on the native Claude API.

Authentication runs through AWS IAM, audit logging through CloudTrail, and billing through a single AWS invoice that fully retires against existing commitments. Customers use their existing AWS credentials and IAM policies, so teams stay within the tools and permissions they already manage.

Claude Platform on AWS will be available in most AWS commercial regions and support global and U.S. inference geographies.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc87b15a611db84c61768_logo_reliaquest-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc89e5fe2e0869c3fead4_logo_reliaquest-dark.svg)

“Claude Platform on AWS helped simplify how we access Claude, improved the experience for key users like our Claude Code engineers, and gave us a practical path to integrate further frontier AI capabilities into our cybersecurity and engineering workflows, while staying within our existing cloud operating model. The Anthropic team was engaged, collaborative, and gave us confidence as we expanded usage.”

Jonathan Echavarria, Principal Research Scientist

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc823ca0eaa97b917abdf_logo_openrouter-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc82ab6096dc10f41e565_logo_openrouter-dark.svg)

“Using Claude Platform on AWS gives OpenRouter and our users direct access to the latest and greatest features of the native Claude API; everything our cutting edge customers and use cases need is available and we control access through the same AWS IAM credentials we use for other AWS services. It has delivered consistent performance on uptime, latency, and throughput, and working directly with the Anthropic team has helped us move faster.”

Tomas Oliva, AI Platform Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692482151d80f9362c5b90c9_emergent-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692482163de140b3aa9e1ebb_emergent-white.svg)

“Claude Platform on AWS gives us the canonical Anthropic API with AWS as the access layer, so we get full feature parity and day-one access to new model capabilities. Support has been one of the best parts, and it felt like one team across both companies, not two separate relationships. That kind of collaboration during scale-up is rare, and it's a big reason we've been able to keep moving as fast as we have.”

Avinash Vishwakarma, Chief Architect

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## What's included

The Claude Platform on AWS includes native platform features, like:

* [**Claude Managed Agents (beta)**](https://platform.claude.com/docs/en/managed-agents/overview)to build and deploy agents at scale
* [**Advisor strategy (beta)**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)to give agents an intelligence boost by consulting an advisor model
* [**Web search**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) **and** [**web fetch**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) to augment Claude’s knowledge with current, real-world data from across the web
* [**Code execution**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) to run Python code, create visualizations, and analyze data directly within API calls
* [**Files API (beta)**](https://platform.claude.com/docs/en/build-with-claude/files) for uploading and referencing documents across conversations
* [**Skills (beta)**](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) to teach Claude best practices so it delivers consistent results
* [**MCP connector (beta)**](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) to connect Claude to any remote MCP server without writing client code
* [**Prompt caching**](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for reducing costs and latency on repeated context
* [**Citations**](https://platform.claude.com/docs/en/build-with-claude/citations) for grounding responses in source documents
* [**Batch processing**](https://platform.claude.com/docs/en/build-with-claude/batch-processing) for high-volume, asynchronous workloads

Claude Platform on AWS customers also get access to the Claude Console, Anthropic's development environment for building and testing with Claude. The Console includes management for agents, skills, environments, vaults, observability tools, and more.

Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5 are available, with new models shipping on the Claude Platform on AWS as they launch.

## Choosing the right path for developers

Both the Claude Platform on AWS and Claude on Amazon Bedrock enable AWS customers to build on Claude models. The difference is in who operates the service and which features are available.

The **Claude Platform on AWS** is a first of its kind offering for Anthropic, giving you all native Claude API features from day one. Anthropic operates the service and data is processed outside the AWS boundary. This is a good option for companies that want the full Claude Platform experience.

**Claude on Amazon Bedrock** keeps AWS as the data processor and operates within the AWS boundary. This is a good fit for companies that have strict regional data residency requirements or need their data processed exclusively within AWS's infrastructure.

## Getting started

The Claude Platform on AWS is available today. To get started, visit the [Claude Platform on AWS](https://aws.amazon.com/claude-platform/) or explore the [documentation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

If you have an existing Bedrock private offer, please contact your Anthropic or AWS account executive before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before a Claude Platform private offer is accepted.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

Apr 14, 2026

### Introducing routines in Claude Code

Product announcements

[Introducing routines in Claude Code](#)Introducing routines in Claude Code

[Introducing routines in Claude Code](/blog/introducing-routines-in-claude-code)Introducing routines in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

May 28, 2026

### Introducing dynamic workflows in Claude Code

Product announcements

[Introducing dynamic workflows in Claude Code](#)Introducing dynamic workflows in Claude Code

[Introducing dynamic workflows in Claude Code](/blog/introducing-dynamic-workflows-in-claude-code)Introducing dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

Jun 9, 2026

### New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

Product announcements

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](#)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](/blog/whats-new-in-claude-managed-agents)New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jun 8, 2026

### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Product announcements

[Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](#)Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

[Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](/blog/claude-for-foundation-models)Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
