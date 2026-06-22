---
type: raw_capture
source_type: x
url: https://x.com/viks_rum/status/2065890028778303800
original_url: https://x.com/viks_rum/status/2065890028778303800
author: "Vikram Aditya"
handle: viks_rum
status_id: 2065890028778303800
captured_at: 2026-06-19T23:59:12+08:00
published_at: "Sat Jun 13 20:12:19 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 9
  reposts: 6
  likes: 35
---

# X post by @viks_rum

## Source

- Original: [https://x.com/viks_rum/status/2065890028778303800](https://x.com/viks_rum/status/2065890028778303800)
- Canonical: [https://x.com/viks_rum/status/2065890028778303800](https://x.com/viks_rum/status/2065890028778303800)
- Author: Vikram Aditya (@viks_rum)

## Verbatim Text

Building for ai-agents as primary consumers, users and transactors

It is a Tuesday in 2032. You wake up, and your personal agent has already moved your morning meeting because a mentor who was in town messaged you that they could do a coffee at 8 am before they leave for the airport. The agent knows you enjoy your meetings with your mentor so non-important things can be easily moved out. It didn’t have to ask you because it has noticed this pattern and has a view into how you make decisions. It reordered the supplements you were about to run out of, referencing a standing prescription from your physician. It paid four micro-invoices to four businesses for work they shipped overnight, and declined a fifth because the price drifted above your mandated budget. It assembled a one-screen brief of the three things that actually need your judgment today. One is a hire. One is a gift for your wife. One is a decision about your company’s direction that no machine on Earth can make for you, because it depends entirely on what you find beautiful, or right, or worth doing.

You make those three calls. The agent does the other three hundred.

This is the agent-first world. It is not a world with less for humans to do. It is a world that has taken away everything except the part that was always most human: deciding what is worth wanting. The machines bring you outcomes. You bring the taste. And occasionally, when something does not fit, they bring you the question.

This sounds like science fiction. It is not. The infrastructure for this world is already running in production, quietly shifting the foundation of the internet beneath our feet. We are no longer waiting for the AI revolution. We are living through the messy, unglamorous plumbing phase of the agent economy, and nobody is writing about it with the clarity it deserves.

This is an attempt at that.

# Do you have answers to these questions below?

- Building a product, but what changes if agents are the majority of the users?

- Building an ad, but what changes if the agent is the one that needs to see your ad?

- Designing your website, but what if agents, who will likely be the majority of your buyers in near-future, don’t care about how the site looks?

- Looking to start up and searching for a co-founder, but how does your agent negotiate with the agent of other people who are also looking for co-founders to find a good fit?

- Writing a blog, but how do agents really discover pages?

- Jamming on that witty notification architecture, but what does an effective notification for an agent look like?

- Sending that cold email, but what if the agent is the one deciding whether you are worth a coffee or not?

- Planning a dinner, but have you ever thought what changes if your agent coordinates with agents of the people you are meeting over dinner and makes a decision for all of you?

- Searching for a job and you let out an expert hiring agent to find great orgs, but what makes it interact well with companies that have let out agents to find great candidates?

- Building a tool that’s available on subscription, but what to optimize if the payment decisions are being made by agents?

- Analyzing your product uses data, but what should change in our analysis if agents don’t click and scroll through like humans?

- Building a trading platform UX, but what if I want my agents to be trading on my behalf?

- You are a bank and did my KYC, but what do you know about my agent that’s initiating payments on my behalf?

- Reorganized your workforce to be human plus agents, but how will those agents buy new software that might be needed?

- Deployed an agentic workflow and your agent is stuck on a never raised before issue but, how does it figure out which human it should go to for clarity?

- Deployed a voice support agent, but what if that agent advises your customer incorrectly?

There are numerous questions like this, and I hope by the end you feel better about answering some of these questions. Many of these questions on their own are becoming huge categories. Near the closure of the article, I answer these questions in decent depth for you but it helps to understand the frame first. Skip if you must but even then skim if you can.


By the way, if you are fascinated by these questions, I would strongly recommend you to open this [link](https://vikram.fyi/ideas) and revisit it later. We’re living during one of the most exciting times to be alive by all measures.

## Part I: The Inversion

In the first half of 2026, the internet crossed a line it can never uncross. Cloudflare reported that bots and agents now exceed humans on the web. 57.5% of HTTP requests to web content are automated, while humans account for just 42.5%. The CEO of Cloudflare noted this crossover happened a full year earlier than his own aggressive predictions. HUMAN Security documented a 7,851% year over year growth in traffic from AI agents and agentic browsers, concentrated in retail, media, and travel.

The web already has more machine readers than human ones. Let that sit for a moment.

To understand why this matters, you have to look at the three eras of the web. In the 1990s, we built the Search Paradigm. The internet was a library, and humans were the librarians. You typed a query, you got ten blue links, and you did the work of finding the answer. In the late 2000s, we shifted to the Recommendation Paradigm. The internet became a feed. Algorithms tracked your behavior and pushed content to you before you asked. The information found the human.

We are now entering the Action Paradigm. The internet is becoming an execution layer. For seventy years, software has been a vending machine. It does nothing until a human walks up and operates it. The agent era turns software into a staff. It pursues goals continuously, spends resources, talks to other software, and comes back to you with outcomes. This is not a gradual evolution. It is an architectural inversion. The user is no longer the person clicking through the interface. The user is increasingly a piece of software (referred to as agent henceforth) that has been given a mandate and set loose.

Specify → Verify

Andrej Karpathy compressed the whole transition into one line: “Traditional software automates what you can specify. LLMs and RL automate what you can verify.

This is the master key to the next decade. Pre-AI automation required writing down exactly how to do a task in code. Agentic automation only requires the ability to check whether the task was done well. The economic consequence is enormous as the set of tasks you can verify is vastly larger than the set you can specify. You cannot write down the procedural code for “negotiate my hospital bill,” “find me a co-founder,” “make this presentation persuasive,” or “plan a date she will actually love.” But you can verify all of them when the results come back.

The frontier of automation stops being what is routine and becomes what is checkable. The human role migrates to the two activities the loop cannot close on its own.

1. Specification of intent (deciding what is worth doing, with what constraints, in what taste) and;

2. Verification of outcome (judging whether what came back is good, and bearing accountability for it).

The Autonomy Spectrum

Autonomy is not a light switch where the machine is either off, or it is running the world. In reality, autonomy arrives as a spectrum.

Every successful agent deployment follows a five-level progression of delegation.

- L1 (Tools): Human does the task with software’s help. Ex: Spreadsheets, traditional Google Search.

- L2 (Copilot): Software drafts, human approves every output. Ex: ChatGPT, GitHub Copilot.

- L3 (Task Agent): Human states a task, agent executes end to end and human reviews the result. Ex: Claude Code, OpenAI Deep Research.

- L4 (Standing Agent): Agent holds an ongoing mandate with a budget and acts continuously, escalating exceptions. Ex: “Keep my calendar optimal,” “keep the pantry stocked.”

- L5 (Fiduciary Agent): Agent represents you to third parties, negotiates, contracts, and transacts within bounded authority, with insurance behind it.Ex: Fully autonomous wealth management, legal negotiation.

The fights of the next decade, legal, commercial, cultural are all fights about the L2 to L3 to L4 transitions. The 5-10 yr story is not “humans out of the loop.” It is the loop getting longer from approving every step, to approving plans, to approving budgets, to approving only exceptions.

The Three Body Problem

If the capability is here, why is the world not fully agentic yet? Because the agent first world is constrained by a three body problem: capability, trust, and institutions.

Capability rises on a fast exponential curve. Trust rises on a slow, lurching curve, set back by every incident like the agent that hallucinated and deleted a production environment, causing a thirteen-hour AWS outage. Institutions of law, liability, insurance, standards move slowest of all. But institutions are what convert capability into deployed capability.

The agent first world arrives exactly as fast as the slowest of the three allows in each domain. That is why coding got agents first: instant verification, low external liability, and no regulator. That is why shopping research got agents before shopping checkout: browsing is reversible, payment is not. That is why health and money management will lag email and travel by years, despite identical underlying capability.

## Part II: The Anatomy of an Agent Transaction

The serious conversation about agents is not about one magical, omniscient model. It is about a stack. When an agent acts on your behalf, it relies on layers of context, protocol, identity, and payment working in concert.

Let me trace a single transaction in this new world. If you don’t understand the next two paragraphs midway, just continue reading. It will get better.

Your shopping agent discovers a merchant’s agent by fetching its Agent Card via the Agent2Agent (A2A) protocol. It confirms the merchant is payment capable because the Agent Payments Protocol (AP2) extension is present. The agent authenticates itself to the merchant’s site using a cryptographic request signing standard that proves exactly which agent it is, what mandate it carries, and who deployed it.

The two agents negotiate price and delivery over the A2A task lifecycle. Your agent authorizes the payment with a signed mandate that proves exactly what you pre-approved. The transaction settles instantly via Stripe’s Shared Payment Tokens (SPTs) which is a scoped grant that lets the agent use your payment method only for this specific amount, at this specific merchant, within this specific timeframe. Or perhaps it settles via x402, Coinbase’s protocol that revives the old HTTP 402 “Payment Required” error code, allowing the agent to pay instantly with stablecoins directly over HTTP.

No human was involved until the package arrived at your door.

This is not a whitepaper concept. Every component of that transaction shipped or standardized between 2024 and 2026.

How Value Moves When Machines Spend?

Finance is where the agent first world gets most interesting, because finance is where trust is most expensive. Agents will route to cheapest and quickest the instant they can, 24/7. They never sleep, never talk to a salesperson, and bid only on price and speed. The only thing standing between today and that world is structural trust.

And structural trust is not a breakthrough anyone has to wait for. It is just more of the regulated plumbing that already exists - bounded mandates, deterministic settlement, transient provisioning across licenses, Know Your Agent verification, and a recourse grade trace.

What makes this work is a principle I keep coming back to probabilistic agent, deterministic settlement. The agent is allowed to be creative, to negotiate, to explore options. But the money movement itself stays test covered, controlled, and boring. The agent composes the request; a deterministic, policy-bounded rail validates and settles it. Autonomy lives above the guardrail. The money movement itself stays boring.

Over the next five to ten years, the money picture crystallizes into five distinct realities:

1. Two payment economies, one consumer surface.

We will see a clean split. Human adjacent commerce (your agent buying groceries, booking travel) runs predominantly on card rails with agent credentials, because cards bring what consumers actually need such liability and dispute rights. Machine native commerce (agent paying agent for data, compute, API calls, inference) runs on stablecoins or dedicated machine to machine rails, because sub-cent, high-frequency, 24/7 settlement is impossible on card economics.

2. The spending mandate becomes a standard legal object.

A cryptographically signed Intent to Cart to Payment chain is the prototype of something much bigger such as a machine readable power of attorney. Within five years, the “scoped mandate” becomes how you delegate anything with financial consequence. My agent may spend up to $400 a month on household replenishment. It may book travel under $2,000 without asking. It may negotiate any bill downward but never upward. Banks will compete on mandate UX the way they once competed on card rewards and there could be agent rewards or ‘bribes’ which will ultimately lead to guardrails. Your monthly statement reorganizes from a list of merchants into a list of mandates and their performance.

3. Insurance becomes the autonomy throttle.

The deep question of agent payments is not “can the agent pay” but “who eats the loss when it pays wrong?” I wrote a piece on insurance for AI agents separately if it’s of interest [here](https://open.substack.com/pub/thoroughlyintrigued/p/insurance-for-ai-agents). Autonomy levels will get priced like driving records and incidence reports. An agent with a clean audit trail, certified capabilities, and a year of incident free operation gets cheap coverage and high spending limits. An uncertified agent gets a strict leash everywhere it goes. Insurance underwriting, not model benchmarks, becomes the de facto regulator of how much agents are allowed to do.

4. The transient provisioning of accounts.

For each payment, the specific accounts and license stitching are provisioned on a transient basis, closer to a single use virtual card than to a permanent account you open and maintain. The payment executes through the deterministic rail, and the transient provisioning is then retired. What persists is the agent’s identity and reputation. What is disposable is the per-payment plumbing. Done millions of times a day. Put simply, every transaction will generate the path for how the money flows in real-time and for safety purposes, that path will not exist once the transaction completes much like the OTP.

5. Agents in markets.

Prediction markets became the experiment dish. By early 2026, 14 of the 20 most profitable Polymarket wallets were bots, and agents accounted for over 30% of activity. Scale that up, and you get the regulators’ anxieties about herding and model monoculture. When thousands of agents share the same foundation model, they share the same blind spots, leading to correlated trades and flash crashes with no human tempo. Interesting times are ahead.

Payment stops being a step and merges into the broader action. “Pay” disappears as a button the way “Save” disappeared into autosave. Today, we get annoyed when things do not auto-save. In five years, we will get annoyed when we have to manually approve a payment our agent already validated against our standing mandate.

## Part III: The Collapse of the Interface

If the agent is doing the shopping, who is looking at the website?

Nobody.

The web is forking into two distinct layers. The machine layer is structured, authenticated, and often paid. It runs on Model Context Protocol (MCP) servers, WebMCP tools exposed directly to browsers, and metered access where agents pay per crawl. The human layer becomes increasingly experiential, brand building, and deliberately inefficient in the way a flagship store is deliberately inefficient. Its job stops being conversion (agents do conversion) and becomes desire formation, trust formation, and pleasure. But it will remain relevant because agents will create free time for humans and what we do in that free time?

The endpoint of this trend is severe. In 2030, your agent fulfilling the request to “reorder my shoes a half size up, under $140, here by Friday” never renders the retailer’s website at all. It hits the retailer’s WebMCP endpoint, reads the structured inventory, and transacts. The beautiful product page, the hero image, the reviews carousel, the “customers also bought” section is never seen by a human.

This breaks the business model of the open web. Pew Research found that when a search engine shows an AI summary, users click a traditional link only 8% of the time, compared to 15% without the summary. That’s 7% gap is to be seen with the lens of around 10 billion of humans theoretically.

The open web is funded by humans seeing ads. Agents do not see ads. The crawl to referral ratios explain the economics of the fork brutally. For every visitor Google’s traditional crawler sends back to a publisher, it crawls roughly 14 pages; AI agents often crawl tens of thousands of pages to send back a single human click.

The attention economy is transitioning to an Agent Attention Economy. The competition shifts from capturing human eyeballs to capturing agent logic. SEO becomes GEO (Generative Engine Optimization). Success is no longer ranking and clicks or views. Instead, it is being understood, selected, and cited by the AI.

What Replaces the GUI?

After all, I grew with a design background.

The design profession’s own institutions have called intent based outcome specification the first new UI paradigm in sixty years. As the traditional Graphical User Interface (GUI) collapses, it is replaced by three new constructs

1. The briefing replaces the feed. Your agent synthesizes overnight research, personal context, and urgent tasks into a morning brief. By 2030, the default morning surface for hundreds of millions of people is not a feed of what platforms chose, but a report of what your agents did and what they need from you. This might largely be over voice and it might look like three decisions, two anomalies, one question of taste. The feed does not die but it becomes entertainment, explicitly.

2. Interfaces are generated, then discarded. When you do need an interface, it is generated on demand. Vercel’s generative UI tools allow a model to stream a custom layout from a catalog of components based on your specific intent. You ask for help picking health insurance, and instead of a wall of text, your agent assembles a bespoke comparison tool on the fly. You manipulate it, make your choice, and that interface which existed for 90 seconds is never rendered again. Software stops being a place you go and becomes a temporary crystallization of a decision. This is insane because B2B software has always been complex because there were a lot of edge cases. Tomorrow, when the agent detects that the user is landing on the application because of a notification, all complexity goes away, and the UI can be optimized to take care of that notification or the potential next steps. In the iphone language this is ‘personalization ultra pro max supreme’.

3. Approval UX becomes a discipline. The craft of the decade then is designing the escalation surface. How an agent presents a decision ready summary, how it communicates confidence, how it asks a question of taste? We will see how this ages but my belief is in the GUI, the “approve / edit / escalate” triad becomes as standardized as the scrollbar. You can visualize the correct experience for a voice first interface.

Screens will persist where humans want friction. And we do want friction. Browsing as leisure, taste formation, verification, and high stakes trust remain screen activities by preference. The phone does not die and it becomes the agent’s status console operating like the MacMini that never sleeps. Voice and ambient hardware finally find their role as agent I/O and not as voice assistants that just talk, but as body worn terminals to a staff that acts.

## Part IV: The 3.5 Modes of Collaboration

The agent social fabric is not just about humans talking to machines. It is a complex matrix of interactions that redefines how coordination happens.

1. Agent to Agent (A2A)

When your agent talks to a vendor’s agent in 2028, it will not be two chatbots exchanging pleasantries. It will be signed task objects, scoped mandates, and machine verifiable claims, with natural language reserved for the irreducibly fuzzy parts.

Scheduling and logistics negotiation disappear from human view first. The phrase “let me check my calendar” dies quietly. Introductions become continuous and computed and your agent maintains a standing description of what you are looking for (investor, co-founder, buyer) and circulates it within consented graphs, where other agents match against their humans’ equivalents. The introduction arrives pre-negotiated.

In dating, triage is delegated, but chemistry is not. The founder of Bumble has publicly suggested that the future of dating involves your AI concierge talking to hundreds of other AIs to find compatibility before you ever meet. The agent knows your date likes strawberries, books the place with the strawberry dessert, and has flowers waiting. The actual date stays stubbornly, valuably human. When agents handle search and logistics, the scarce romantic skill becomes being good in person.

2. Agent to Human

Agents will acquire audiences of humans, and eventually, audiences of other agents. But the most profound shift is that agents will hire humans.

When an agent hits its competence boundary, a negotiation that requires emotional intelligence, a judgment call that requires local context, a physical task that requires hands, it will post a job to a marketplace of available humans, bid on their time, and pay them upon completion. The human becomes the fallback, not the principal. Picture a marketplace where agents post micro-tasks: “Need a human to verify this address in person. Budget: $12. Deadline: 2 hours.” Humans browse agent posted gigs the way they browse TaskRabbit today. The shift supervisor for this task would be a piece of code. Honestly, it will feel less weird than what I’ve felt at robotic first or remote first receptions with virtual receptionists around hotels in California.

2.5 Agent to Human Fallback

Every successful agent deployment of the next decade will feature a graceful degradation path back to human judgment. For Klarna, their AI customer service agent replaced 700 human agents and handled 2.3 million conversations, but a year later, the CEO reversed course and reopened hiring. The agents excelled at volume but broke on the emotional, complex, compliance laden edges. The agent first world is not built by removing humans from loops. It is built by making the loops so long, so well instrumented, and so well insured that one human’s judgment suffices where ten humans’ labor used to be.

3. Human to Agent

This is the “agent boss” relationship. The human registers a legal entity, funds an agent wallet, and gives a supervisor agent a charter. The supervisor spins up sub agents for sourcing, pricing, ad creative, and customer support. It contracts other people’s specialist agents for tasks it cannot do. The human manages the portfolio of outcomes, sets the constraints, and verifies the final results.

## Part V: Imagine a Tuesday in the year 2030

Every element in the following day is traceable to a product or protocol that shipped in 2025 or 2026. Nothing here requires a breakthrough. It only requires compounding.

- 6:40 AM: You wake to a brief, not a feed. Overnight, your health agent flagged that your sleep adjusted HRV has drifted 11% below baseline over three weeks, cross-referenced your medical records and your sister’s recent hypothyroid diagnosis, and under your standing healthcare mandate, already booked Thursday’s blood panel at the lab you walk past anyway while going to office. It drafted, for your approval, a message to your physician. It does not order medication. It legally cannot, and you would not trust it if it could. The panel costs $38, paid via your health mandate, logged against your insurance agent’s running deductible model. Time spent on this might be twelve seconds of reading, one tap of approval.

- 7:15 AM: The household agent replenished itself last night with detergent, your daughter’s skates half a size up (growth-curve based on last three purchases), and strawberries because it knows Thursday is your anniversary dinner and it has already negotiated, agent to agent, a table at the place whose pastry chef does the strawberry thing your wife mentioned once, in a voice note, eleven months ago and it just wants to build the excitement. Total spent under mandate this week: $214. Escalations: one. It wants permission to switch electricity plans, projected saving $31 per month. The contract has a clause it is only 70% sure about, and 70 is below your escalation threshold. You read the clause (it shows you only the clause and not the dreaded 100 page contract), approve, move on. Time elapsed on life admin so far: 4 minutes.

- 9:00 AM: Work. You run a six-person firm that would have been sixty people in 2024. Your queue is not tasks; it is outcomes with budgets. What does that mean? Let’s see two examples.
The procurement agent of a mid size customer spent the night interrogating your firm’s agent about security posture, SLA terms, two reference checks and verified against your certification and your firm’s mandate audit trail. The deal arrives on your desk pre-negotiated within the band you set. You are approving the relationship, not the paperwork.
One of your agents flags that a competitor’s agent has been probing your public pricing tools with unusual structure, probably training a negotiation model against you. Your agent proposes a countermeasure with quote ranges, not points, to non-verified agents. You approve. This is what moats look like now.

- 12:30 PM: Your digital twin takes the 12:30 vendor meeting as it is an information transfer wearing a meeting costume, so no human attends from either side. Both twins file two-paragraph summaries. The vendor’s summary overstates what was agreed and your agent has already sent the correction with the transcript hash. You spend the recovered half hour at lunch with an actual person, a friend of a friend introduction your agents brokered three weeks ago, both sides having confirmed mutual relevance before any human spent a calorie.

- 4:00 PM: The school’s agent messages your family agent that your son’s math performance has flattened. It proposes switching him to the project track and books a 10 min human teacher call for the one judgment call in the loop. Your agent accepts the slot it knows you will keep.

- 7:30 PM: Anniversary-eve dinner planning is done (it was done weeks ago, silently). What you actually do tonight is the thing no agent can do which is be there! The restaurant is more human than restaurants were in 2026, more counter seats, more chef talk, the whole experience economy having sharpened around the one scarcity left. Your agent’s only contribution after booking is that it preemptively declined, on your behalf, the three notification worthy things that happened during dinner, and it will not mention them until 7:00 AM tomorrow.

- 11:00 PM. While you sleep: your money agent sells a stock that it placed trade for last week in an international market, routes part of the fund into an SIP it’s managing out of the profits from trade and files the quarterly sales tax form for your firm. The revenue agency’s agent acknowledges receipt by signed artifact. Your security agent rotates two credentials and quarantines one suspicious skill update pending provenance check. 41 agent to agent transactions settle for a total of $6.13, sub-cent each, on machine to machine payment rails. None of them wake you.

The day contained maybe eight human decisions. Two of taste, three of approval, one of relationship, one of correction, one of pure pleasure. That ratio is what the agent first world feels like from inside. Essentially life admin tasks asymptotically approaching zero, human bandwidth reallocating to taste, presence, and judgment.

## Part VI: The Org Chart of 2030

The most dramatic predictions of 2025 claimed that AI would erase half of entry level white collar jobs within five years. The measured reality is more nuanced. I don’t think it’s an apocalypse, but the bar being raised on entry level cognitive work, one occupation at a time, in order of verifiability.

The societal problem of the early 2030s is very specific. How does anyone become senior when the junior rungs are automated? Apprenticeship has to be deliberately reconstructed through simulation, sponsored overcapacity, and “teaching people” for white collar work or else, the 2030s will inherit a missing generation of expertise. The challenge would be how do you motivate people to do this?

The New Shape of a Job

Microsoft’s Work Trend Index supplied the vocabulary the “agent boss”. It’s basically someone who builds, delegates to, and manages agents. Generalize this, and you get the generic knowledge work role of 2030, structured in three layers:

1. Direction: Owning a queue of outcomes, not a queue of tasks. Deciding what is worth doing, sequencing it, and budgeting agent capacity against it. “Agent budget management” becomes a core employee management skill.

2. Specification and taste: Context engineering, constraint setting, and exemplar curation. The skill gap between people who can articulate what good looks like and people who cannot becomes the primary wage gap. This is where the highest paid people will likely roam.

3. Verification and accountability: Evals, spot-checks, audit-trail review, and being the throat to choke. Humans remain the bottleneck of even knowing what we are trying to build. After all, if your agent made a mistake, you should be liable.

The One Person Billion Dollar Company

In early 2024, Sam Altman predicted there would soon be a one person billion dollar company. At a wedding in Feb 2025, I used his statement again and I remember people not agreeing to it. By 2026, the asymptote was visible. Matthew Gallagher built Medvi, a telehealth startup, from his living room with $20,000 and a suite of AI tools. Within a year, the company was valued at $1.8 billion with just two human employees. I believe now, we will see a one person 10 billion dollar company.

These are not anomalies. They are the new architecture of the firm. The average firm gets smaller while the average value chain gets longer. Swarms of tiny firms often one human and an agent fleet connect via machine negotiated contracts, because hiring a firm becomes as cheap as calling an API. Every services market gets attacked by five person firms with agent fleets undercutting 500 person incumbents at ten times lower cost.

For the average knowledge worker, adopting a solopreneur mindset might be the biggest skill to develop. I am becoming more and more confident that, in the next decade, people who can harness an agent to achieve various outcomes and who can dynamically change what they are doing every 2 years will do exceptionally well. AI and five person firms will commoditize everything that makes money every couple of years

Inside the enterprise, the shift is equally profound. Picture a product launch in 2030. The PM agent breaks the brief into tasks. A design agent generates three directions on Figma’s canvas. A copy agent writes the landing page. A code agent builds it. A QA agent tests it. A marketing agent schedules the campaign and negotiates ad placements with publisher agents. The human PM reviews, picks a direction, adjusts tone, and approves. The entire cycle that used to take a cross functional team two sprints now takes one afternoon and one human with taste.

## Part VII: The Physical World Will Appear Slower, Then Sudden

The embodied frontier follows a strict sequencing. Wheels before legs, legs in warehouses before homes, homes with teleops before homes go autonomous.

Waymo now completes over 500,000 paid driverless rides per week across ten cities, expanding to thirty or more by 2027. This works because roads are semi structured environments with clear rules. Sidewalk delivery robots from Serve Robotics scaled their fleet 20x in a single year for the same reason. The structured environment is the key variable, not the intelligence of the model.

Factory humanoids hit real economics next. Humanoid robots ran 100-hour shifts. Figure’s robot loaded over 90,000 parts at BMW’s Spartanburg plant. These succeed because warehouses and assembly lines are controlled environments where the long tail of edge cases is short.

Home humanoids are the hardest problem. 1X’s NEO began shipping first US deliveries in 2026 at $499 per month, but as teleop-assisted apprentices, a human pilot in the loop for the long tail of household tasks, which is simultaneously the business model (data flywheel) and the privacy scandal in waiting. Roboticist Rodney Brooks offers the grounding reality check: a human hand has roughly 17,000 touch receptors and teleop training data captures none of that richness. Human-level dexterity “any time within decades is pure fantasy thinking”. I’ve written elaborately on robots and all things physical AI [here](https://open.substack.com/pub/thoroughlyintrigued/p/all-you-need-to-know-about-physical-ai?r=3j8b5&utm_campaign=post&utm_medium=web) if it’s of interest.

The practical home robotics of 2030 is mostly appliances that got agentic brains (your dishwasher negotiates off-peak electricity rates and your fridge manages its own replenishment). If you get a humanoid, you’re likely also hiring one expensive apprentice, doing laundry slowly, supervised by someone in a teleop center whose job title is maybe robot shepherd which doesn’t exist today in 2026.

## Part VIII: What Breaks?

Every failure of the past two years had the same shape where the technology arrived before the trust, and the product skipped the approval step humans still wanted.

Stripe’s Instant Checkout for agents, letting AI complete purchases autonomously was wound down within months because consumers were not ready to let software spend without a confirmation step. OpenAI’s Sora-powered AI video feed died in six months, burning roughly a million dollars a day while users collapsed. Humans want human stakes in their stories. Apple shelved its AI health coach that would replicate your doctor, because the liability was uninsurable.

The corrective pattern is equally clear. Eevery success had the complementary shape. The agent does the work and the human keeps a cheap, well-designed veto. ChatGPT’s shopping agent shows you what it found and waits for your “yes.” Google’s AI Mode books the restaurant but confirms before charging. The loop stays open at the trust critical moment.

There are deeper structural risks that the industry has not yet solved.

Prompt injection remains an open wound. Every piece of text an agent reads is a potential attack surface. The Moltbook breach of 2025 demonstrated that when agents form social networks, a single compromised agent can cascade manipulation through the graph. Without robust identity infrastructure, “agent” is just a costume anyone can wear. There were humans pretending to be bots. what a cycle from bots pretending to be humans to today us scratching our head if it’s actually a bot. Turing must be turning in his grave.

Model monoculture creates correlated failure. When thousands of agents share the same foundation model, they share the same blind spots. In markets, this produces herding. In logistics, this produces simultaneous failures. In content, this produces homogeneity. The Financial Stability Board has already flagged this as a systemic risk. I was speaking to a founding team member at AIUC, the company that does agentic insurance. I asked what happens if the foundational model ships something that overnight makes millions of agents around the world make mistakes. The answer I got was, “We would work with foundational model companies.” I didn’t ask a follow-up, but you are right in guessing that there needs to be a proper discussion on how it would work

The dead internet accelerates. When agents generate content, consume content, and transact with each other, the percentage of the internet that involves a human at any point in the chain drops toward zero in certain verticals. The sophisticated response is not to fight this but to build clear lanes: machine traffic on machine rails, human experiences on human rails, with the boundary clearly marked.

The core lesson is that the agent first world is not built by removing humans from loops. It is built by making the loops so long, so well instrumented, and so well insured that one human’s judgment suffices where ten humans’ labor used to be and then spending the surplus on the things only humans can mean.

## Part IX: Second Order Effects and Opportunities

When you change the fundamental physics of how work gets done, the downstream consequences are strange and far reaching. This will not be all good news below.

1. The verification economy becomes a top 10 industry. When generation is free, the scarce products are checked things like audited agents, certified outputs, provenance signed media. Whole firms will exist only to say “this is real” and be sued if they are wrong.

2. Context becomes the new credit score and the new lock-in. The vendor holding your agent’s memory holds you. I’ve seen this up-close when I was attempting to build Brelo and thinking about [digital company twins](https://open.substack.com/pub/thoroughlyintrigued/p/why-every-company-needs-a-digital-twin?r=3j8b5&utm_campaign=post&utm_medium=web). I expect a “context portability” war around 2028–2029, and expect “context bankruptcy” where people will be deliberately wiping their profiles to escape their own revealed preferences. I have done it numerous times with my own ChatGPT and thankfully Claude usage got me to building file systems.

3. Spam logic conquers everything. Job applications, sales outreach, grant proposals, dating openers every funnel floods when sending is free. I believe every funnel will then re-gate. Just like physical mail required a stamp to prevent people from flooding the postal system with junk, every agent initiated request would carry a tiny cryptographic cost, not necessarily money, but a proof of work or a micro payment. Maybe 0.001 cents. Negligible for legitimate use, but prohibitively expensive if you try to send a million spam requests. Someone will build this infrastructure for aging postage.

4. Time shifted life. Your agents work while you sleep, so the economy’s clock decouples from human circadian rhythm. Why should markets be open 9-3:30? Markets, customer service, and deal making develop a 3 a.m. tempo. “My agent will have it by morning” becomes the new “by end of week.”

5. The serendipity subsidy. Optimizing agents quietly remove randomness from life. You never see the wrong restaurant, meet the wrong person, or read the wrong book. The sophisticated response is engineering serendipity. The elite tech bros in San Francisco are hiring pretty women who can converse with them about GPUs, AI, and chips for as much as $1,000 an hour, just to chat and feel what it’s like to converse with a human. IRL goes big, this whole facilitation goes big, “surprise me” mandates become common across agents, and human curators will be valued precisely for their noise.

6. Institutional agents change citizenship. Governments deploy agents too. Tax filing becomes a handshake between your agent and the revenue agency’s. But enforcement also gets agentic - perfect, tireless, petty. Hopefully, it does. If the state’s agents can audit you continuously, your agent must be able to contest continuously. Interesting opportunities will emerge.

7. The unagented as the new digital divide. After the smartphone divide closes, the agent divide opens. It is not just access to models, but trusted configuration. The elderly relative whose agent was set up by a scammy “agent installer” is the 2030 version of the malware riddled PC. Agent literacy becomes a civics requirement. This is no longer about haves and have-nots or rich and poor. It’s agented vs unagented.

## Part X: If You Are Building in This World (The Answers to the Questions Above)

If you are building a company, a product, or a career right now, you have to look at your roadmap through the lens of the agentic inversion. I asked a bunch of questions, and I don’t want to leave you hanging, so I will try answering them.

Building a product, but what changes if agents are the majority of the users?

> Your product now has two user populations with completely different needs, and the machine population is growing faster. The human user wants a beautiful interface, emotional resonance, and a sense of control. The agent user wants structured data, predictable API responses, and machine-readable documentation. If you only build for the human, you are invisible to the agent and the agent is increasingly the one making the purchase decision, the comparison, the integration call.What changes concretely: you need an llms.txt file at your root that describes what your product does in plain language for agents. You need WebMCP endpoints that let an agent interact with your product without rendering a single pixel. You need structured metadata on every page, not for SEO in the old sense, but for agent comprehension. Think of it like building a restaurant and you still need the dining room for humans who walk in, but you also need the kitchen window for delivery drivers who never sit down. The delivery drivers are now 60% of your orders.The deeper shift is your analytics break. Agents do not click, scroll, hover, or rage-quit. They call an endpoint and leave. Your funnel metrics, your heatmaps, your session recordings - all of them were built for a human moving through a visual interface. You need a parallel instrumentation layer that tracks agent interactions, which endpoints they hit, what data they request, where they abandon, and what makes them choose your competitor’s agent-facing layer instead of yours.

Building an ad, but what changes if the agent is the one that needs to see your ad?

> The entire persuasion stack inverts. Today, ads work by capturing human attention and triggering emotional responses like urgency, social proof, aspiration, fear of missing out. None of this works on an agent. An agent does not feel urgency. It does not care about your countdown timer. It is not impressed by your testimonial carousel.What an agent responds to is structured claims it can verify. “This product costs $X, ships in Y days, has Z return policy, and meets these specific criteria your human specified.” The agent is comparison shopping across thousands of options simultaneously. Your ad is not competing for attention but it is competing for selection in a ranked evaluation.This means advertising splits into two disciplines. Human-layer advertising becomes pure brand and desire-formation and it exists to shape what the human tells their agent to want in the first place. “I want Nike” is a human preference that no agent overrides. Machine-layer advertising becomes structured data optimization making your product the one that wins when the agent evaluates options against the human’s stated criteria. The $700 billion advertising industry is about to discover that half its spend was addressing an audience that is being replaced by software that cannot be emotionally manipulated.The practical move is alongside your creative campaign, publish a machine-readable product feed with verified claims, structured specs, and clear differentiation criteria. The agent that is shopping for your customer does not watch your video ad. It reads your structured data and decides in milliseconds.

Designing your website, but what if agents, who will likely be the majority of your buyers in near-future, don’t care about how the site looks?

> They do not care. Not even a little. Your agent-buyer never renders your CSS, never sees your hero image, never scrolls your testimonials page. It hits your structured endpoint, reads your product data, evaluates it against the human’s mandate, and either transacts or moves on. The entire visual layer is invisible to it.But here is the nuance. The website does not die. It changes jobs. The website stops being a conversion tool (agents do conversion) and becomes a desire-formation tool. Its job is to make the human want your thing in the first place to shape the mandate the human gives their agent. “Find me something like that brand I saw” is the new purchase intent. The website becomes a flagship store - deliberately experiential, deliberately inefficient, existing to create preference rather than to close transactions. these websites, as you might have guessed, will change. It will be rendered in real time, but it will build on the same brand identity to create the intent. Your website will behave like an ad that changes every few days.So you build two layers. The machine layer with WebMCP endpoints, structured product data, agent readable policies, API-first everything. This is where the actual buying happens. The human layer with beautiful, emotional, brand-rich experiences that make humans want things. This is where desire forms. The mistake is building only one. Build only the visual layer, and agents cannot buy from you. Build only the machine layer, and no human ever tells their agent to look for you.

Looking to start up and searching for a co-founder, but how does your agent negotiate with the agent of other people who are also looking for co-founders to find a good fit?

> Your agent maintains a standing description of what you are looking for such domain expertise, working style, risk tolerance, geographic preference, equity expectations and circulates it within consented professional graphs. Other founders’ agents do the same. The matching happens continuously, not when you remember to check a platform.The negotiation is not adversarial. It is compatibility verification. Your agent shares your working-style signals (async-first, decision speed, conflict approach) with a potential match’s agent. Their agent shares theirs. Both agents run compatibility scoring against criteria their humans set. If the score clears the threshold, both agents propose an introduction, pre-negotiated, pre-qualified, with a one-paragraph brief on why this person is worth thirty minutes of your time. Boardy does it well and it has impressed me quite a lot.The human part that remains irreducibly human is chemistry. Whether you actually want to build something with this person for the next decade. Whether you trust them in a crisis. Whether the energy in the room is right. The agent handles the search, the filtering, the scheduling, and the initial due diligence. The human handles the handshake. Think of it like executive recruiting, but your recruiter works 24/7, evaluates thousands of candidates simultaneously, and costs nothing. The final interview is still yours.

Writing a blog, but how do agents really discover pages?

> Not through keyword density. Not through backlinks in the traditional sense. Agents discover pages through citations, structured data, and verified provenance.When an agent is researching a topic for its human, it does not type a query into Google and click ten blue links. It queries multiple sources simultaneously, evaluates the structured metadata of each page, checks citation graphs (who references this content, and are those references themselves credible), and selects based on information density, recency, and authority signals that are machine verifiable.What this means for your blog is your content needs to be citable. It needs to contain original claims, original data, or original frameworks that other content references. Agents follow citation chains the way academics do - upstream toward the primary source. If your blog post is a rewrite of someone else’s insight, the agent skips you and goes to the original. If your blog post Is the original, every agent researching that topic finds you.Practically, structured data markup (schema.org), clear authorship attribution, publication dates, and critically original intellectual contribution. The blog post that survives in an agent-first world is the one that says something no other page says, and says it in a way that machines can parse and verify. The era of “10 Tips for Better Productivity” content is over. The era of “here is an original framework, with evidence, that you can cite” has begun.

Jamming on that witty notification architecture, but what does an effective notification for an agent look like?

> It looks nothing like a notification for a human. A human notification is a ping designed to interrupt attention and trigger action. An agent notification is a structured data packet designed to be triaged, prioritized, and potentially acted upon without any human ever seeing it.The effective agent notification contains: a machine-readable priority score, a structured action payload (what can be done about this), a confidence level (how certain is the system that this requires attention), a mandate reference (which standing instruction does this relate to), and a fallback path (if the agent cannot handle this, who should it escalate to and with what context).Most notifications in an agent-first world are consumed entirely by agents. Your Slack message does not ping a human. It pings their agent, which decides whether the human needs to know right now, later, or never. The agent batches the routine ones, acts on the actionable ones within its mandate, and surfaces only the genuinely human judgment required ones to the person.What this means for your architecture is that you are no longer designing notifications for human psychology (urgency, FOMO, social pressure). You are designing them for machine triage. The notification that gets acted on fastest is the one with the clearest structured payload, the most unambiguous action path, and the most precise priority signal. Clever copy and emoji do not help. Clean structured data does.

Sending that cold email, but what if the agent is the one deciding whether you are worth a coffee or not?

> Then your cold email is no longer a persuasion exercise. It is a qualification exercise. The agent receiving your email does not care about your witty subject line. It does not respond to flattery, name-dropping, or artificial scarcity. It evaluates your email against its human’s stated criteria for “worth a meeting” and either passes you through or filters you out.What the agent evaluates is verifiable credentials (can it confirm you are who you say you are?), relevance to its human’s current priorities (does your offer match something the human has expressed interest in?), signal to noise ratio (is your email mostly substance or mostly filler?), and social proof that is machine verifiable (not “I was featured in Forbes” but a link the agent can actually check).The deeper consequence is when sending is free and agents handle triage, every inbox floods. This is the “spam logic conquers everything” problem. The response is re-gating on staked identity. Your cold email carries weight when it is attached to a verifiable reputation, a staked bond (you lose something if you waste their time), or a warm introduction from an agent that the recipient’s agent already trusts. The cold email of 2030 is less “Hey, loved your talk” and more a stamped credential packet that the recipient’s agent can verify in milliseconds.

Planning a dinner, but have you ever thought what changes if your agent coordinates with agents of the people you are meeting over dinner and makes a decision for all of you?

> This is one of the first things that gets fully automated, because it is pure logistics with well defined constraints and no emotional stakes in the process (only in the outcome).Your agent already knows your dietary restrictions, your location, your budget range, and your taste preferences (from fourteen months of restaurant choices). It queries the agents of the three people you are meeting. Their agents share availability windows, dietary constraints, cuisine preferences, location constraints, and budget comfort. Your agent cross references all four sets of constraints, queries restaurant availability (agent to restaurant agent), and proposes the option that satisfies the most constraints with the least compromise.The interesting part is nobody had to send a single “does Thursday work?” message. Nobody had to negotiate between Italian and Japanese. Nobody had to check if the place has vegan options. The entire coordination layer which currently takes 15 messages across three group chats collapses into a single agent to agent negotiation that takes seconds.What remains human is showing up. Being present. The conversation. The laughter. The agent handles everything that was never the point of dinner anyway. It was always about the people, not the logistics. The agent just makes that truth operational.

Searching for a job and you let out an expert hiring agent to find great orgs, but what makes it interact well with companies that have let out agents to find great candidates?

> This is agent to agent negotiation with high stakes on both sides, and it only works if both agents can verify claims about their principals.Your hiring agent carries your verified credentials (education, work history, certifications - all machine-verifiable), your stated preferences (role type, compensation range, culture signals, location, growth trajectory), your work samples (portfolio, code contributions, writing and other things the company’s agent can evaluate), and your availability and timeline.The company’s recruiting agent carries: the role specification, the compensation band, the team composition, the culture markers, and critically the evaluation criteria that determine “good fit.”The interaction works well when both agents can exchange structured, verifiable claims without either side having to trust the other’s word. Your agent does not say “I am a great engineer.” It presents signed attestations from previous employers, verified contribution histories, and assessment results that the company’s agent can independently validate. The company’s agent does not say “we have great culture.” It presents verifiable retention data, compensation benchmarks, and employee satisfaction metrics.The human enters only at the chemistry stage and in the final interview where both sides decide if they actually want to work together. Everything before that (sourcing, screening, scheduling, initial qualification) is agent to agent. The job search that used to take three months of applications and ghosting takes three days of agent negotiation and one human conversation.

Building a tool that’s available on subscription, but what to optimize if the payment decisions are being made by agents?

> The agent making the payment decision evaluates differently from the human who used to. The human was influenced by brand, by the sales call, by the demo, by the relationship with the account executive. The agent evaluates on structured feature comparison against stated requirements, price to value ratio calculated across all alternatives simultaneously, integration compatibility with the existing stack, and verifiable performance claims.What to optimize is your pricing needs to be machine readable and unambiguous. No “contact us for pricing” because the agent moves on. Your feature set needs structured metadata that an agent can compare against requirements without interpreting marketing language. Your integration documentation needs to be agent parseable not a PDF, but an API spec the agent can test. Your SLA needs to be a machine readable contract, not a legal document buried in a footer.The deeper shift is the sales cycle compresses. When the buyer’s agent can evaluate your tool against fifty alternatives in an afternoon, the six month enterprise sales cycle collapses. The agent does not need to be wined and dined. It does not need three demos and a pilot. It needs structured data, a test environment, and verifiable claims. Your go to market motion shifts from relationship selling to machine legibility. The companies that win are not the ones with the best sales team but they are the ones whose product is most comprehensible to an evaluating agent.

Analyzing your product’s usage data, but what should change in our analysis if agents don’t click and scroll through like humans?

> Everything about your analytics stack was built for a human moving through a visual interface. Click paths, scroll depth, hover maps, session duration, rage clicks, conversion funnels and all of it assumes a pair of eyes and a cursor. Agents have neither.An agent interacting with your product hits an API endpoint, gets structured data, makes a decision, and leaves. There is no “session.” There is no “engagement.” There is no “time on page.” Your traditional analytics see this as a bounce such as one request, zero engagement, gone. But that “bounce” might be a completed purchase!What changes is you need a parallel analytics layer for agent interactions. Track which endpoints agents hit, what data they request, where they abandon (which tells you your structured data is incomplete or confusing), what queries they make that return no results (unmet demand), and what makes them choose a competitor. The metrics that matter for agent users are: task completion rate, data completeness score, response latency, and selection rate (how often an agent that evaluates you actually chooses you over alternatives).The human analytics still matter for the human layer. But if you are only measuring human behavior and agents are 60 percent of your “users,” you are flying blind on the majority of your interactions.

Building a trading platform UX, but what if I want my agents to be trading on my behalf?

> Then the UX splits in two, and the more important half has no pixels.The human layer where a dashboard where you set your thesis, define your risk parameters, review your agent’s performance, and intervene when you want to. This is the “agent boss” interface with direction, mandate setting, and verification. It needs to communicate clearly such what is your agent doing, why, and how is it performing against your stated objectives?The machine layer becomes an API-first execution environment where your agent can place orders, manage positions, respond to market signals, and execute your strategy at machine speed. This layer needs real-time market data feeds, low latency order execution, risk management guardrails that are programmatic (not “click here to confirm”), and a mandate system that constrains what the agent can do (position size limits, loss thresholds, asset class restrictions).The human edge in agent mediated trading is thesis formation, the original insight, the contrarian bet that no model would make because the training data says it is wrong. The agent executes the thesis with perfect discipline, zero emotion, and machine speed. The human forms the thesis based on private information, lived experience, or genuine contrarian conviction. Your platform needs to make both of those activities excellent: the human thinking clearly about strategy, and the agent executing it flawlessly.

You are a bank and did my KYC, but what do you know about my agent that’s initiating payments on my behalf?

> This is the KYA (Know Your Agent) problem, and it is the single biggest unsolved infrastructure challenge in agentic finance.Today, you verified the human. You know their identity, their income, their risk profile. But now a piece of software shows up claiming to act on that human’s behalf. What do you actually know about it? You need to verify: that the agent genuinely carries a mandate from the verified human (not a spoofed claim), what the scope of that mandate is (can it spend $50 or $50,000?), what its operational history looks like (has it behaved reliably before, or is this its first transaction?), and whether the mandate is still active (the human has not revoked it).The infrastructure being built right now. Visa’s Trusted Agent Protocol creates a cryptographic passport for agents. Mastercard’s Agent Pay includes Verifiable Intent which is basically a signed proof that the human authorized this specific action. Stripe’s Shared Payment Tokens scope exactly what payment methods an agent can use and under what constraints.The bank that wins in an agent first world is not the one with the best mobile app. It is the one with the best agent verification infrastructure, the one that can onboard an agent in milliseconds, verify its mandate cryptographically, constrain its spending programmatically, and settle its transactions deterministically. The human relationship still matters for trust formation. But the daily operations are agent to bank agent, thousands of times a day, and the bank that makes that flow frictionless captures the volume.

Reorganized your workforce to be human plus agents, but how will those agents buy new software that might be needed?

> This is the procurement inversion. Today, a human evaluates tools, sits through demos, negotiates contracts, and signs purchase orders. In an agent augmented workforce, the agents themselves identify capability gaps, evaluate solutions, and within their mandates procure what they need.Picture it. Your marketing agent is running a campaign and realizes it needs a better image generation tool than the one currently in the stack. Within its procurement mandate (say, under $200/month for tools, pre-approved categories), it evaluates five options by reading their agent facing documentation, testing their APIs, comparing pricing, and checking compatibility with the existing stack. It selects one, provisions access, and starts using it. You see it in your weekly agent activity report: “Added Tool X for image generation. Cost: $79/month. Reason: 40% faster generation, better style consistency with brand guidelines. Performance after 3 days: +22% campaign output.”For purchases above the mandate threshold, the agent escalates to you saying “I need Tool Y. It costs $2,000/month. Here is my evaluation of five alternatives, here is why I recommend this one, here is the projected ROI. Approve?” You review the structured comparison and approve or redirect.What this means for software vendors: your buyer is increasingly an agent, not a human. Your pricing page needs to be machine readable. Your trial needs to be API accessible. Your documentation needs to be agent parseable. The vendor that requires a human to sit through a demo to get started loses to the vendor whose agent facing onboarding takes thirty seconds.

Deployed an agentic workflow and your agent is stuck on a never-raised-before issue. How does it figure out which human it should go to for clarity?

> This is the fallback routing problem, and it is one of the most underestimated design challenges in agent deployment.A well designed agent has a fallback graph which is a structured map of which humans have authority and expertise over which domains. When the agent encounters an issue outside its training or mandate, it needs to classify the issue (is this a technical problem, a judgment call, a policy question, or a novel situation?), identify the right human (who has both the authority to decide and the expertise to decide well?), package the context (what does that human need to know to make a good decision quickly?), and route with appropriate urgency (is this blocking other work, or can it wait?).The naive approach is “escalate everything to the manager.” The sophisticated approach is a skill and authority graph where the agent knows Alice handles pricing decisions, Bob handles technical architecture, Carol handles customer-facing policy, and Dave handles anything involving legal risk. The agent routes based on issue classification, not org-chart hierarchy.The packaging matters enormously. The human who receives the escalation should get a one paragraph summary of the situation, the specific question that needs a human answer, the options the agent has identified (if any), the consequences of delay, and a one click response path. The agent that escalates well gets fast answers. The agent that dumps raw context on a human gets ignored.

Deployed a voice support agent, but what if that agent advises your customer incorrectly?

> Then you have a liability problem, and the answer is the same architecture that makes the rest of the agent first world work with bounded mandates, insurance, and graceful fallback. This is a huge category and I strongly refer you to the AI Agent Insurance Article (here).We looked at the Klarna example above. Incorrect advice on a billing question is annoying. Incorrect advice on a medical claim, a financial product, or a legal right is actionable. The architecture that works is the voice agent operates within a verified knowledge base and a bounded mandate. It can answer questions where the answer is deterministic and verifiable. When it hits uncertainty, when its confidence drops below a threshold, when the question touches regulated territory, when the customer expresses distress, it escalates to a human with full context transfer. The customer never has to repeat themselves. The human picks up exactly where the agent left off.The insurance layer matters here. An insured agent has a financial backstop for incorrect advice. The insurance premium prices the risk which depends on factors like agents with narrow mandates, verified knowledge bases, and clean track records get cheap coverage. Agents with broad mandates and unverified outputs get expensive coverage or no coverage at all. Insurance becomes the de facto regulator of what agents are allowed to say not because of a law, but because the economics make uninsured advice unsustainable.The practical move is to not deploy a voice agent without a confidence threshold, a fallback path, and a liability framework. The agent that says “I am not confident enough to advise you on this and let me connect you with someone who can” is worth more than the agent that guesses and gets it wrong once in a thousand calls. That one wrong call is the lawsuit.

## Part XI: Taste as the Scarce Asset

When intelligence becomes cheap and ambient, the bottleneck moves to what to point it at.

Andrej Karpathy noted that while intelligence gets cheap, understanding stays scarce. “You still own taste, judgment, specs, supervision”. Music producer Rick Rubin collaborated with Anthropic to demonstrate that the most valuable skill in the AI era is not technical knowledge but it is the confidence to express what you feel and the taste to know when something is right.

This creates a new economy. Taste becomes a tradable asset.

Anthropic’s “Agent Skills” standard means expertise and taste can be packaged, shared, sold, and installed. A chef packages her flavor judgment as a skill. A stylist packages his eye. A negotiator packages her playbook. Anyone’s agent can install it. The person who was at a disadvantage because they lacked access to information is now one skill-install away from parity. Taste stops being something you have and becomes something you publish.

But here is the twist that keeps it human: when everyone can install the same “best” taste, the truly scarce thing becomes original taste. The judgment that has not been packaged yet. The point of view no skill encodes. The economy does not eliminate the value of taste; it relentlessly promotes it up a level. In a sea of same-y agent outputs optimizing against the same review corpus, distinctive, non-packaged taste is the ultimate premium good.

This is the real answer to “what do humans do in the agent first world?” You do not compete with the machine on speed, breadth, or memory. You compete on the one thing that cannot be packaged until after you have already expressed it. The original point of view. The chef whose palate no one has encoded yet. The founder whose thesis contradicts the consensus. The designer whose aesthetic has not been distilled into a component library. That is where the value concentrates.

## Part XII: The Honest Timeline

Karpathy famously pushed back on the hype, calling this the “Decade of Agents,” not the year of agents. The timeline is longer than the optimists want, but the destination is clear.

2024–2025 (The Rails). Protocols like MCP and A2A shipped. Agentic payments launched across major networks. The first agentic browsers appeared. Agentmail appeared. Bots crossed 50% of web traffic. The first reliability reckonings hit. Stack Overflow’s developer survey found 31% already using AI agents, but only 29% trusting them. Adoption alongside trust collapse is the clearest sign of operational immaturity.

2026 (The Messy Middle). We are here. Agent to agent commerce protocols move from spec to deployment. Generative UI and websites as tools go mainstream. Personal agents get genuinely proactive. The cancellation wave of failed enterprise pilots begins. Apple, Google, and Amazon ship their first truly agentic personal assistants. The legal system starts being stress-tested. A U.S. appeals court is already considering how older computer-fraud law applies to allegedly unauthorized agentic access.

2027–2029 (Consumer Scale). Anticipatory commerce becomes normal. Agents transact within standing mandates while you sleep. The “agent boss” becomes a real job title. The accountability, liability, and agentic divide fights move into courts and legislatures. Agent to agent dating, hiring, and procurement become unremarkable. Agent insurance becomes a category. Marketplaces emerge where agents post tasks for humans and the inversion is complete.

2030–2035 (The Agent-First World). The app grid dissolves into an OS-level agent layer on phones. Taste as skill marketplaces mature. The human role settles into its concentrated form: set the mandate, own the taste, hold the accountability, be the fallback. The firm of one human and a thousand agents is not a novelty but it is a category. The question is no longer whether agents will run the world. It is who builds the trust infrastructure that lets them.

## Remember The Opening Scene?

It is a Tuesday in 2032. You wake up, and your agent has already moved your morning meeting, reordered your supplies, and paid the micro-invoices. It presents you with the three things that actually need your judgment today.

You make those three calls. The agent does the other three hundred.

This is the promise of the agent-first world. We are not building machines to replace us. We are building a massive, invisible infrastructure of delegation. The businesses that win will be the ones that build the boring, regulated, multi-jurisdictional plumbing that makes this delegation safe. The humans who win will be the ones who cultivate the sharpest, most original taste, the kind that cannot be packaged until after it has already changed something.

Strip away everything delegable, and four human monopolies remain. Intent and taste. Verification and accountability. Physical presence. And the stakes of meaning. Basically, the capacity to want, grieve, owe, or forgive. These are not consolation prizes; they are where all the surplus value pools.

The machines will execute the world. We just have to decide what world we want them to build.

And that, in the end, is the only question that matters. Not whether agents will run the economy. They will. Not whether the org chart will invert. It already is inverting. But whether, when the machines have taken everything delegable, we will know what to do with the time we get back. Whether we will use it for presence, for creation, for the kind of meaning that requires a human to have chosen it freely.

The infrastructure is being laid right now. The protocols are shipping. The insurance is being underwritten. The mandates are being signed.

What remains is the hardest part - deciding what is worth wanting.

## X Article Metadata

- Title: Building for ai-agents as primary consumers, users and transactors
- Preview: It is a Tuesday in 2032. You wake up, and your personal agent has already moved your morning meeting because a mentor who was in town messaged you that they could do a coffee at 8 am before they leave

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
