---
type: raw_capture
source_type: x
url: https://x.com/IgorZIJ/status/2034368877052727683
original_url: https://x.com/IgorZIJ/status/2034368877052727683
author: "Igor Zalutski"
handle: IgorZIJ
status_id: 2034368877052727683
captured_at: 2026-06-19T21:44:56+08:00
published_at: "Wed Mar 18 20:38:31 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 0
  reposts: 1
  likes: 2
---

# X post by @IgorZIJ

## Source

- Original: [https://x.com/IgorZIJ/status/2034368877052727683](https://x.com/IgorZIJ/status/2034368877052727683)
- Canonical: [https://x.com/IgorZIJ/status/2034368877052727683](https://x.com/IgorZIJ/status/2034368877052727683)
- Author: Igor Zalutski (@IgorZIJ)

## Verbatim Text

Agent execution is the new HTTP request

Just the other day in [The Agentic Workload](https://x.com/IgorZIJ/status/2033316871928254530) I managed to finally capture a hunch that bugged me for a while: agents need infrastructure of a fundamentally different “shape” than the distributed primitives we are accustomed to in application development. But re-reading it today I’m realising it misses something even more fundamental that is likely going on - almost like a full-circle moment in the industry. What follows is my attempt to capture this; a “Part 2” of sorts.

# Ground 0: files and scripts

At the dawn of the Web in the 1990s there wasn’t much to it beyond files sitting on computers - actual physical computers with public IP addresses. The first web server, HTTPd created by Tim Berners Lee, literally just mapped a URL to a file. The server's config (httpd.conf) basically defined a document root directory, e.g. /usr/local/www/htdocs/, and if you requested /papers/proposal.html it would read and return that file. This was perfectly fine at because at the time there was just one web server in the world - [info.cern.ch](http://info.cern.ch/).

By December 1991 there was a second one, at SLAC in the US. And by late 1993 there were already ~500 web servers. It was becoming clear that some sort of program on top of bare files would make launching a new server easier. So Rob McCool at NCSA introduced CGI. It was still file-based; but you could now put your program into the cgi-bin directory, and If a URL pointed into cgi-bin/, instead of returning the file, the server would fork a new OS process, exec that script/binary, pass the HTTP request info via environment variables (QUERY_STRING, REQUEST_METHOD, CONTENT_LENGTH, etc.) and stdin, and pipe the script's stdout back as the HTTP response. Such scripts were often written in the Perl programming language, now almost forgotten - but one relict of it that remains in nearly all languages to this day is the Regular Expression pattern-matching. Perl was perfect for CGI because the most common job of a web application was to match some sort of a URL to some sort of a file path on disk.

Worth noting: each request was isolated at process level; filesystem was shared.

# Application servers

CGI scripts had one problem: every request spawned a new process. But there is only so much memory on the server. Back in 1995 a typical web server would be called “powerful” if it had 32MB of ram (megabytes, not gigabytes). It would hardly even load a single photo from a modern iPhone (~20mb) even if it was the only thing the poor server did because there was also OS with a bunch of system programs running. So the number of requests a server could process was limited by the number of CGI processes that would fit in memory simultaneously - which wasn’t many.

The solution was to trade isolation for performance. I’ll skip lots of important developments here for the sake of conciseness - but essentially, by the late 1990s / early 2000s Apache, a fork of HTTPd, emerged as a de-facto standard web server. Extensions like mod_perl and mod_php allowed to handle requests using various programming languages. Instead of giving a full process to each request like the original HTTPd, Apache initially would use a fixed-size pool of “worker processes”, each running a PHP interpreter.

PHP became the most widely used (and arguably the first) “internet programming language”, this Internet thing was clearly here to stay, so many other companies got into the business of sending HTML over HTTP - notably Java Servlets by Sun and ASP by Microsoft. I won’t even attempt to go into the technical design decisions of these, suffice to say that they rather quickly evolved from “web servers” to “enterprise software ecosystems”. Computers became more powerful each year so you could serve more and more users from each computer (or rather VM, as virtualisation tech matured enough to cleanly decouple hardware maintenance from the software running on it).

Ruby on Rails and Django frameworks were created in 2004-05 and arguably perfected the “application server” pattern. Much of the Web as we know it was created with these frameworks: GitHub, Twitter and Shopify were built with Ruby on Rails;  Instagram and Pinterest with Django.

Fundamentally though these all were still processes running on a single machine, keeping some stuff in memory, reading / writing some files. Databases by this time ran on their own machines, perhaps sharded across multiple nodes for extra reliability, but the rest remained surprisingly stable, traceable all the way back to HTTPd! File system is still shared by all requests; but no longer a fresh process for each request - the process stays alive between requests, holds state in memory, manages database connections, owns sessions. That tradeoff we will come back to later.

# Isolation over efficiency: shared-nothing

In early 2000s the number of users that each successful Internet application needed to handle was growing much faster than even the most optimistic versions of the Moore’s law could deliver in terms of compute capacity. The bottleneck that didn’t allow monolithic application servers to utilize more than one VM was state - both in-memory and filesystem.

Long before “the cloud” it became frowned upon to store any data that might be shared across requests anywhere else but in memcached (and later Redis), even though the application server frameworks were literally built for that. The probability of in-memory state breaking is small but never zero, which translates into seemingly unbeatable error rates at high RPS - unless you extract that state.

Same story with files: before object storage, a common pattern was to use a database for all “non-memory” state and never ever rely on any files on disk. Database servers were marvels of engineering designed to keep the representation of the underlying filesystem consistent for all clients - so it made sense to make use of that. You could get even more reliability by using multiple DB instances instead of one, each narrowly scoped to its own domain… so arguably many of the standard backend patterns of today can be traced all the way back to pre-AWS days.

Amazon popularized these patterns by launching commercial services with unheard-of-before reliability guarantees in 2006: first Simple Storage Service for storage (S3, arguably the most important one), followed by Elastic Compute Cloud for compute (EC2). This was a “holy grail” of sorts - you could now go as granular as you wanted with your applications on EC2, and have them all write files to S3, which would ensure consistency. For a few years it looked like “scalability solved” - and the one breakthrough that made this possible was clean separation of storage and compute. In-memory state was also solved because with EC2 you could now reliably add nodes to sharded memcached clusters, which was enough even for Facebook.

Requests were still served by application server frameworks though, sitting on EC2s, keeping some bits of state in memory and reading / writing some files - even if only for system reasons now. Remember the tradeoff that application servers made in the early days of the internet to be able to handle more requests - to forego process-level isolation? This no longer made sense because you could have as much compute as you needed, and the more isolation, the higher the reliability.

I’m obviously omitting lots of important developments, but basically this is how containers came to be - Docker and then Kubernetes. A lot like virtualisation allowed to hot-swap hardware in data centres without software running in the VMs noticing, a fleet of VMs was now running hundreds of thousands of containers, each hosting a highly specialised stateless microservice designed to do one job well and handle failures and restarts gracefully, wired with all sorts of telemetry - this pattern resembling good old division of labour / assembly line, was the way to squeeze even more nines out of the system.

But why stop there? Why so many layers? The stack is now essentially:

1. hypervisor running multiple VMs atop hardware

2. orchestrator running multiple containers atop VMs

3. web server inside each container serving multiple requests

There’s also good old efficiency. Every container takes a fixed amount of RAM - but not every container needs all of it, because so many web servers in containers are idle at any given time. What if…

Yeah. The core idea behind serverless is simple - if you could quickly and reliably provision isolated environments for every request in your data centres, you’d need less RAM! CPU can be time-shared; RAM cannot - so there would be less idle CPU time, and the economics of your data centre would improve significantly.

It also happens to be great for reliability because now the server is recycled after every request. Even before serverless functions it was a best practice to kill containers periodically - because even “pure stateless” services tend to accumulate bits of state here and there (eg because memory leaks in the foundational system libraries). Starting from scratch at the OS level for every request allows to add a couple more nines to your system’s reliability, which is not possible to achieve in any other way.

Finally, we have solved scalability.

# Now scratch all that, back to files and scripts

With agents, we are back at ground 0. The leading harnesses read and write files and use bash, much like those early cgi-bin scripts. MCP is (or should I say was?) a stateful protocol. LLMs seem to want to live in stateful linux environment - perhaps because bash scripts, various *nix utilities and linux itself make a large fraction of the code they’ve been trained on. So if there is any environment that LLMs understand natively without additional tools in the context, it's Linux - files and scripts.

Web servers came a long way since HTTPd; it took ~30 years to reach the “final form” that is modern web frameworks that are now evolving much slower, if at all. But tracing their history shows that every step change was driven by a clear why, a bottleneck that created a practical problem - and sure enough, a solution emerged.

Funnily enough, the evolution of web servers was not the first time these patterns emerged. Just before the Internet, we’ve reached a similar “scalability solved” point at the OS level. Take virtual memory or process scheduling - the designs (and the underlying reasons for them) of these OS-level primitives is strikingly similar to the patterns that emerged organically 30 years later at the datacenter level. Agents are likely to follow a similar arc, perhaps faster, but without skipping steps.

# The new HTTP request

In a web server a “unit of work” is a request; in an agents, it is the execution (aka “session” aka “thread”). Every agent seems to follow a pattern resembling a messaging app: messages / actions grouped into conversations. This pattern likely emerged from the underlying architecture of the chat-like “instruct” variation of LLMs that started the revolution: predicting the next token is cool but post-training it on human dialogs makes it practically useful in a broad range of scenarios - so chat it is.

The internals of the emerging AI stack are likely here to stay just the way they are for a very long time. Apache, which is a fork of the original HTTPd built by Tim Berners Lee, was the #1 web server by popularity all the way until late 2010s, and is still serving roughly 30% of the Internet traffic in 2026. Given the explosive growth of popularity of LLMs with no end in sight, similarly to the early days of the Internet, only small incremental changes to the already-working designs are likely to survive the test of history, even if they seem suboptimal at times. It happened the way it happened; for many years ahead the utility of major changes to how it all works under the hood will be very low; and conversely, the utility of making what already exists work as-is for different problems at hand will be high. Just like it transpired with the Internet.

The implications of it I’m most concerned with are the ones for builders. It is tempting to rethink everything from first principles and show the world the “right way”. But do you remember CORBA? Few do; however it was technically superior to HTTP in almost every way. Same for ATM vs TCP/IP. Same for every attempts to replace JavaScript with something more sensible. With such once-in-a-generation things, the fact that the entire world using them dwarfs every other concern, and seemingly random designs become industry standards just because they were the first.

Specific example: there’s an ongoing debate on merits of running agents inside sandboxes as opposed to using sandboxes as tools with a stateless agent loop outside it. I described it in more detail in [The Agentic Workload](https://x.com/IgorZIJ/status/2033316871928254530). The proponents of the “as tool” approach are probably right - it is, indeed, better in almost every way. But it also couldn’t matter less. CLI agents happened the way they happened almost by accident, likely as an unintended consequence of the way LLMs were trained. But now that’s history. JavaScript was so wrong for the first 20 years of its existence, however that didn’t stop it from becoming the most popular programming language.

So you should absolutely run your agent inside a sandbox. For example in [opencomputer](http://opencomputer.dev/). Embrace the imperfections! They are here to stay.

## X Article Metadata

- Title: Agent execution is the new HTTP request
- Preview: Just the other day in The Agentic Workload I managed to finally capture a hunch that bugged me for a while: agents need infrastructure of a fundamentally different “shape” than the distributed

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
