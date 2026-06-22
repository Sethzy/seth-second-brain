---
type: raw_capture
source_type: web
title: "Ramp Builders Why We Built Our Own Background Agent"
url: "https://builders.ramp.com/post/why-we-built-our-background-agent"
collected_at: 2026-06-10T17:16:58Z
published_at: 2026-01-12
capture_quality: complete
status: raw
trust_lane: intentional
---

# Ramp Builders Why We Built Our Own Background Agent

Source: https://builders.ramp.com/post/why-we-built-our-background-agent

## Capture Text

Title: Why We Built Our Own Background Agent
URL: https://builders.ramp.com/post/why-we-built-our-background-agent
Authors: Zach Bruggeman, Jason Quense, Rahul Sengottuvelu
Published: 2026-01-12
Description: The craft of engineering is rapidly changing. We built our own coding agent to accelerate faster.
Extraction note: Article body extracted from the public Ramp Builders compiled MDX JavaScript bundle at /assets/index-DpAo9n6i.js. Markup/images were omitted; paragraph and list text preserved.

We built our own background coding agent: Inspect. Inspect writes the code like any other coding agent, but closes the loop on verifying its work by having all the context and tools needed to prove it, as a Ramp engineer would.

For backend work, it can run tests, review telemetry, and query feature flags. For frontend, it visually verifies its work and gives users screenshots and live previews. Agents should have agency, and so we made sure Inspect is never limited by missing context or tools, but only by model intelligence itself.

Because Inspect sessions are fast to start and effectively free to run, you can use them without rationing local checkouts or worktrees. A builder can kick off multiple versions of the same prompt, and just see which one lands. They can try different approaches or swap models without thinking twice. Thereâs no limit to how many sessions you can have running concurrently, and your laptop doesnât need to be involved at all.

This also means you can capture ideas the moment you have them. Notice a bug while winding down for the night? Kick off a session, talk to it if you want (we added voice), and check the PR in the morning.

The interface understands that people rely on a rich variety of workflows. You can chat with Inspect in Slack and send it screenshots, use the Chrome extension to highlight specific changes to elements, prompt it on the web interface, discuss on the Pull Request, and even drop into a web-based VS Code editor to make manual changes. All changes are synced to the session, so you never lose your work while switching around. Plus, every session is multiplayer. Send your session to any colleague, and they can help take it home.

We want Inspect sessions to be fast, and session speed should only be limited by model-provider time-to-first-token. Everything else, like cloning and installing, is done before you start your session. When background agents are fast, theyâre strictly better than local: same intelligence, more power, and unlimited concurrency. You can go home and let Inspect cook (and if youâre so inclined, resume after dinner from your couch and mobile phone).

Internal adoption charts have been vertical: ~30% of all pull requests merged to our frontend and backend repos are written by Inspect. It only took a couple months for us to reach this level of usage, and it continues to grow. We didnât force anyone to use Inspect over their own tools. We built to peopleâs needs, created virality loops through letting it work in public spaces, and let the product do the talking.

We think anyone should be able to build this. Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be. After all, it only has to work on your code. To make this easy to replicate, weâve written a spec of what weâve built so far. Paste the link to this post into a coding agent and let it begin building.

Sandbox

At the core of a hosted coding agent is the execution environment. Whenever you start a new coding session, you want to spin up a new sandbox that has a full development environment. This will allow the agent to work effectively, by having access to all the tools a human would have, while also being isolated from other work. Itâs also crucial that time-to-first-token is as fast as possible.

sandboxes start near instantly

file system snapshots

We have an image registry, defining an image for each code repository

If you use GitHub: You will need to have a GitHub app, and generate a new app installation token on each clone, so that it can clone the repository without knowing what user will consume it

As git operations are not tied to a GitHub user, you will simply update the git configâs user.name and user.email when committing and pushing the changes

We save a snapshot of the image in this completed state

This ensures that at most, the repository is 30 minutes out of date

This makes the synchronization with the latest code in the repository much faster, as thereâs only up to 30 minutes of changes to sync

When the agent is finished making changes, we take another snapshot, and restore to it later if the sandbox has exited and the user sends a follow up

You want the ability to create as many custom clients as possible down the line, as you want to put your coding agent wherever your team works

fully typed SDK

comprehensive plugin system

This is something we believe is highly underrated in development with AI

You want it to be as easy as possible for the agent to understand how it works, without it hallucinating what it believes is its own behaviour

As such, having the code as its source of truth is extremely powerful

you will get the OpenCode team to work with you

Some optimizations you should add for increased speed:

This lets it start cloning the latest changes, and doing any initial setup in the newly created sandbox before the user has even hit enter

If your spin up is fast, it can be ready before the user finishes typing, making the prompt feel as fast as it would on a local machine

Just ensure to expire and recreate the pool as new image builds come in

In a large enough repository, it is unlikely that an incoming prompt is going to modify a file changed in the last 30 minutes

As such, you can let it start researching immediately, and avoid any latency from git here

However, ensure that you block file edits until synchronization is complete

Thoroughly investigate what you need to do to have a complete development environment, and do literally everything you can do beforehand

Even things like running your app and test suite once are helpful, as these may write cached files that a second run will make use of

It doesnât matter if your image build is long, as users are just using the last built image, and therefore will not see how long this step took

You should decide if you want follow up prompts that are sent during an execution to be inserted as soon as possible, or queued to be run after the current prompt is complete. We chose to queue them, as we found it not only easier to manage, but also helpful for sending over thoughts on next steps while the AI is still working. Be sure to build a mechanism to also allow an agent to be stopped mid-way.

Amongst many tools you could build for your agent, a crucial tool is one that allows it to spawn sessions itself. Donât be afraid of the possibility of it spawning too many agents; frontier models are smart enough to contain themselves. Create a tool that starts a new session, and a tool that lets it read the status of any session, so it can check in periodically while the main session still does work. Prompt engineer this so you can either do research tasks (especially across different repositories), or create many smaller pull requests for one major task.

API

You want to build an API that is going to be able to support input from a variety of clients, whether that be a chat interface, a Slack bot, a Chrome extension, or any other input you can think of in the future. You want the state to be synchronized across all clients. You also want to build multiplayer support, which weâll explain shortly.

We believe that multiplayer is a mission-critical feature, and something we have not seen in any other product yet. The idea behind multiplayer should be that any number of people can work in one session together, just as they would in a branch of code. Each personâs prompt that causes code changes should be attributed to them. This is useful for a variety of scenarios:

Teaching non-engineering builders, such as product managers and designers, how to effectively utilize the AI for their own work

Doing live QA sessions with your team, as each person can queue up changes they find in real-time, instead of writing a ticket to do it later

Reviewing another personâs pull request, asking the AI to quickly make requested changes instead of just commenting them and waiting for the original author to pick them up

If you build a system that synchronizes across clients, multiplayer support should be nearly free to add. Just ensure your data model does not strongly tie a session to only one author at a time, and be sure to pass authorship info to each prompt thatâs sent to the coding agent.

You will need to add authentication. Consider using GitHub authentication if your code lives in GitHub, as this will give you a user token that you can then use to open a pull request on behalf of the user. This is strongly preferred over having it open pull requests as the app itself. In the latter scenario, this would allow for any user to approve their own changes. You do not want to knowingly create a vector for unreviewed code to go into the codebase.

Our setup is to have the sandbox push the changes (updating the git user as previously mentioned), and then send an event to the API with the branch name and session ID. The API will then use the userâs GitHub token to call GitHubâs pull request API. You should also set up a GitHub webhook to listen for branch and pull request events, so you can keep track of when a pull request is updated, merged, or closed.

Clients

Client choices should be to taste, focusing on where your organization primarily works. These are just our most effective clients. As you have now built a generic sandbox and API for remote coding, you can build any client on top.

Slack

Choose whatever team communication tool your company uses. We believe this is extremely effective, as it not only lets you quickly tackle issues from a variety of sources, but also introduces a virality loop. As people in your organization use it, others will see it, and theyâll learn how to use it themselves.

Slackâs APIs are not hard to start with, as they have a plethora of client libraries. Your goal here is to make it as seamless as possible to use. Do not force the user to learn syntax to use a chat bot. They should just be able to chat with it, and it should figure it out.

A critical piece is to build a classifier to determine what repository to work in. Take the userâs incoming message, any thread context (if sent in a thread), and the channelâs name. Give that to a fast model (we use GPT 5.2 with no reasoning), along with descriptions of every repository your coding agent can access. Be sure to give it hints on the most common repositories, and example classifications. Be sure to include an âunknownâ option, so the AI can ask the user if unsure. You may need to tweak this at first, but this significantly lowers the barrier for entry.

The Slack bot should also be very clear when itâs working vs. when itâs done. Give the agent a Slack message tool, so it can post updates about what itâs doing at important inflection points. Use Block Kit to design an appealing layout, such as including metadata about the repository and working status as context blocks.

Most importantly: Since this is your own Slack bot, we recommend adding your own emojis for the bot to use. Itâs a lot more fun than just using generic emojis.

Web

You should have a polished web client, so users can work on sessions from anywhere. Ensure it works well on both desktop and mobile. If you use Cloudflareâs Agents SDK, youâll have easy constructs for handling the real-time streaming.

What matters more here is some additional functionality you can expose uniquely in the interface:

It can also take before and after screenshots, which you can append to the pull request descriptions

As well, you should build a statistics page. Include your entire organizationâs usage, particularly surfacing how many sessions result in a merged pull request. This is the most important metric to track, as merged pull requests indicate that the agent is producing valuable work. Show these as metrics over time, so you can inspire more growth. A live âhumans promptingâ count is a good gauge as well, which we base on the number of users that have sent a prompt in the last 5 minutes.

Chrome extension

extension update server
