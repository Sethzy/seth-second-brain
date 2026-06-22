---
type: raw_capture
source_type: web
title: "Understand Claude Code’s impact with contribution metrics"
url: "https://claude.com/blog/contribution-metrics/"
canonical_url: "https://claude.com/blog/contribution-metrics/"
vendor_blog: claude
published_at: 2026-01-29
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Understand Claude Code’s impact with contribution metrics

Original URL: https://claude.com/blog/contribution-metrics/
Published: 2026-01-29
Captured: 2026-06-14T02:32:25+00:00

Description: Measure how Claude Code impacts your team's velocity. Track PRs shipped and code committed with GitHub integration—no extra tools required.

## Extracted Article Text

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# Understand Claude Code’s impact with contribution metrics

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code
* Date

  January 29, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/contribution-metrics

Today, we're introducing contribution metrics in Claude Code, available in public beta. Engineering teams can now measure how Claude Code impacts their team’s velocity, tracking PRs shipped and code committed with Claude's help.

## **How we're shipping at Anthropic**

Engineering teams at Anthropic use Claude Code extensively, and contribution data has helped us quantify its impact. As Claude Code adoption has increased internally, we've seen a 67% increase in PRs merged per engineer per day. Across teams, 70–90% of code is now being written with Claude Code assistance.

While pull requests alone are an incomplete measure of developer velocity, we’ve found them to be a close proxy for what engineering teams care about: shipping features, fixing bugs, and delighting users faster.

The new contribution metrics in Claude Code help you measure this impact in your own organization.

## **Measure velocity with Claude Code**

By integrating with GitHub, contribution metrics surface the following data points:

* **Pull requests merged**: Track PRs created with and without Claude Code assistance
* **Code committed**: See lines of code committed to your repositories with and without Claude Code assistance
* **Per-user contribution data**: Identify adoption patterns across your team

Contribution data is calculated by matching Claude Code session activity with GitHub commits and PRs. We calculate this conservatively, and only code where we have high confidence in Claude Code's involvement is counted as assisted.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697aba6d44c54e6710747e68_contribution-metrics-2.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697aba633790d097ad08c6fc_contribution-metrics-1.png)

The metrics appear in your existing Claude Code analytics dashboard, accessible to workspace admins and owners. No external tools or data pipelines are required. Simply install our GitHub App and authenticate to your organization’s GitHub account, and metrics will automatically populate on the dashboard.

Contribution metrics are designed to complement your existing engineering KPIs. Use them alongside DORA metrics, sprint velocity, or other measures to understand directional changes from bringing Claude Code to your team.

## **Getting started**

Code contribution metrics are available now in beta for Claude Team and Enterprise customers. To enable them:

1. Install the [Claude GitHub App](https://github.com/apps/claude) for your organization
2. Navigate to [Admin settings > Claude Code](http://claude.ai/admin-settings/claude-code) and toggle on GitHub Analytics
3. Authenticate to your GitHub organization

Metrics begin populating automatically as your team uses Claude Code. View the [documentation](https://code.claude.com/docs/en/analytics) for detailed setup instructions and guidance on interpreting your metrics.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Oct 8, 2025

### Beyond permission prompts: making Claude Code more secure and autonomous

Claude Code

[Beyond permission prompts: making Claude Code more secure and autonomous](#)Beyond permission prompts: making Claude Code more secure and autonomous

[Beyond permission prompts: making Claude Code more secure and autonomous](/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous)Beyond permission prompts: making Claude Code more secure and autonomous

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
