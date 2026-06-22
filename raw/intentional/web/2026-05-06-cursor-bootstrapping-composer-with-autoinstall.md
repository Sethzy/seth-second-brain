---
type: raw_capture
source_type: web
title: "Bootstrapping Composer with autoinstall"
url: "https://cursor.com/blog/bootstrapping-composer-with-autoinstall/"
canonical_url: "https://cursor.com/blog/bootstrapping-composer-with-autoinstall/"
vendor_blog: cursor
published_at: 2026-05-06
collected_at: 2026-06-14T02:32:25+00:00
capture_quality: extracted_markdown
status: raw
trust_lane: intentional
scrape_window_start: 2025-12-14
scrape_window_end: 2026-06-14
extraction_method: requests + BeautifulSoup + markdownify
---

# Bootstrapping Composer with autoinstall
Original URL: https://cursor.com/blog/bootstrapping-composer-with-autoinstall/
Published: 2026-05-06
Captured: 2026-06-14T02:32:25+00:00


## Extracted Article Text

[Blog](/blog) / [research](/blog/topic/research)

May 6, 2026·[research](/blog/topic/research)

# Bootstrapping Composer with autoinstall

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fshomil-jain-avatar.png&w=48&q=70)

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjoshua-warner-avatar.jpg&w=48&q=70)

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fandrew-zhai-avatar.jpg&w=48&q=70)

Shomil Jain, Joshua Warner & Andrew Zhai · 6 min read

[![](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/og/autoinstall-og-image-2.png)](https://ptht05hbb1ssoooe.public.blob.vercel-storage.com/assets/blog/og/composer-autoinstall-v4.mp4)

A notable aspect of how we develop [Composer](https://cursor.com/blog/composer-2) is the way we use past versions of the model to improve the training process for future ones.

One of the clearest opportunities for this kind of bootstrapping is environment setup. RL training requires runnable environments, and if the environment is broken at the start, the model wastes tokens debugging setup instead of learning to solve problems. In the worst cases, a bad environment can make a problem unsolvable entirely, which ends up burning compute for no reward signal.

To address this, we built Composer autoinstall, a system that uses earlier Composer models to automatically create working RL environments from unconfigured repository checkouts. During training of the most recent version of the model, Composer 2, we used its predecessor, Composer 1.5, to manage this process. Beyond simply following step-by-step instructions, we found that modern coding models will go to great lengths to successfully configure, mock project dependencies, and test that setup is successful.

## [#](#better-environments-mean-better-training-signal)Better environments mean better training signal

Like many aspects of our model development, autoinstall is inspired by production Cursor systems. In Cursor [cloud agents](https://cursor.com/docs/cloud-agent), we have a feature that automates the setup of cloud environments for users, to allow their agents to work on projects in a mock environment. Starting from a git checkout, the agent works to install packages, configure settings, and run basic checks to ensure that the code is running and stable. This allows future requests to start from the correct setup.

For RL training, the problem is even more central, but can be challenging. Starting from a repository, the goal of autoinstall is to create a runnable mock base version of the codebase in order to solve a future unseen coding problem. This base environment is critical because Composer is trained with a full set of tools, including programming language lint commands, search, and sandboxed use of shell. The failure to correctly set up the environment makes training inefficient and can waste compute for no reward signal.

## [#](#one-agent-defines-success-the-next-attempts-it)**One agent defines success, the next attempts it**

Autoinstall occurs in two stages. In the first “goal setting” stage, we give the Cursor agent the codebase at a fixed checkout and ask it to propose 10 commands and a high-level description of the output that should run if the environment were correctly set up.

The agent will explore any readme or makefiles for the environment, as well as try typical language-specific commands such as project managers like uv or linters like clippy. The agent’s work will typically consist of setup commands, tests if they are available, and launch commands for executables.

In the second stage, we provide a separate Composer agent with the initial state of the environment as well as three target commands selected from the proposed 10. The agent will then explore the codebase, calling tool calls to get the environment set up so that the commands can run. Afterward, we test that all three commands run and that the output matches the target description from the first agent. If not, we restart the second phase again. If, after five repetitions of this process, the agent has not been able to set up the environment to a satisfactory degree, we discard the environment.

![Autoinstall two-stage process diagram](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fautoinstall-diagram-light.png&w=1920&q=70)![Autoinstall two-stage process diagram](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Fblog%2Fautoinstall-diagram-dark.png&w=1920&q=70)

Through autoinstall, Composer aims to correctly set up an environment in as complete a manner as possible. To achieve that, it will mock missing files, create placeholder images, or even create fake database tables. Some projects require installing additional components that are needed to run tests, such as S3 folders or missing sidecar containers. Composer often mocks these as well, creating MinIO configs or Docker containers to get these to work. To support long-running processes, we allowed autoinstall to create a start script to launch these at the beginning of the RL usage.

## [#](#autoinstall-for-real-world-projects)Autoinstall for real-world projects

To illustrate the autoinstall process, we consider a real experiment we ran where we used autoinstall to setup a complex real-world project. The project, Celo implemented in [celo-org/celo-monorepo](https://github.com/celo-org/celo-monorepo), is a large blockchain project with several major dependencies. This project is an interesting test of autoinstall because it requires managing a large set of dependencies for install and then mocking an authentication flow for testing.

During the first autoinstall stage, we observed the agent go through the docs and code of the project to find the key installation commands. However, the included docs for the project are relatively sparse, so it also used web commands to search the project’s documentation site for further setup commands. Most of the commands identified were installations or tests, but it also included a basic minimal application for utilizing the software from the docs.

In the second stage, the agent was tasked with actually getting these commands running. While the set of tasks was clear, the model did not know a priori which problems it would run into. For this specific case, it found it needed to install several other dependencies such as [Foundry](https://github.com/foundry-rs/foundry), a related repo. It used web search to read the docs for this required project. It was also tasked with running a minimal application in this environment. On the first iteration of this stage, it failed to get this test application running, but on a second iteration it found that it could create a mock user to start the application locally and satisfy the requirement.

## [#](#bootstrapping-the-next-generation)Bootstrapping the next generation.

Autoinstall respresents an interesting example of bootstrapping the RL process with a previous model. Notably, Composer 2 now scores significantly higher on [Terminal-Bench](https://www.tbench.ai/) (61.7% versus 47.9% for Composer 1.5), a benchmark that includes tests of a model’s ability to set up developer environments. This indicates that Composer 2 will provide an improved base for autoinstall. We anticipate in future runs, previous Composer instances will play a large role in many other aspects of the training process, including run management, data preprocessing, and architecture tuning.

Learn more about [Composer 2](https://cursor.com/blog/composer-2)

Filed under: [research](/blog/topic/research)

Authors: Shomil Jain, Joshua Warner & Andrew Zhai
