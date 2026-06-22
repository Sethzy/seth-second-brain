---
type: raw_capture
source_type: x
url: https://x.com/viks_rum/status/2062505722068500626
original_url: https://x.com/viks_rum/status/2062505722068500626
author: "Vikram Aditya"
handle: viks_rum
status_id: 2062505722068500626
captured_at: 2026-06-19T23:26:01+08:00
published_at: "Thu Jun 04 12:04:18 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 1
  reposts: 0
  likes: 6
---

# X post by @viks_rum

## Source

- Original: [https://x.com/viks_rum/status/2062505722068500626](https://x.com/viks_rum/status/2062505722068500626)
- Canonical: [https://x.com/viks_rum/status/2062505722068500626](https://x.com/viks_rum/status/2062505722068500626)
- Author: Vikram Aditya (@viks_rum)

## Verbatim Text

All you need to know about Physical AI

A strange thing has started showing up in founder conversations.

People who could build software very fast are not as excited by software alone anymore. Not because software has become unimportant.

Software by itself is starting to feel less defensible.

A SaaS product that would have taken twelve engineers and eighteen months now looks like something two cracked people can build in a quarter. Moats have disappeared. A workflow tool does not feel like a company unless it owns distribution, data, or a painful business process. A lot of Indian founders learned this the hard way. I did too, in my own way.

It is no longer just, what software can I build.

It becomes, what part of the real world is still broken enough that software alone cannot fix it.

That question is the door into Physical AI.

I want to spend this piece doing something specific. I want to take the words Physical AI, which are getting used in a hundred ways at the same time, and put them on a table, take them apart, look at what each piece is doing, and put them back together in a way that lets you tell a sharp story about it. Not so you can sound smart at a dinner. So you can decide what to build, what to invest in, what to bet your career on, and what to stay away from.

I also want to do it from a particular position, which is not the position of a robotics researcher and not the position of a VC. I am an enterprise software operator. I have sold to enterprises. I have shipped products. I have shut down a company and returned the money. I have watched markets that looked obvious turn into traps and markets that looked like jokes turn into a hundred billion dollars. I think the same lens applies here. Most of the things people are arguing about in physical AI are actually the same arguments that played out in software ten years ago, just translated. Once you see the translation, the noise quiets down.

This piece is long. The category deserves length, because most of what is being written about it is too short to be useful and too excited to be honest. If you read it end to end, you should walk away with a worldview, a mental framework for sorting companies into boxes, a real read on where each country is positioned, a view on the data economy that is forming around training agents to act in the physical world, a defensible take on which industries actually matter for the next decade of compounding, and the questions you should be asking when a founder tells you their robot can do anything. If you only want one section, scroll to the framework. If you want the full story, sit with it.

Before I go anywhere, one ground level definition.

When I say Physical AI in this piece, I mean software that decides and acts in the real world, with the consequence of that action mattering. It is not just AI that sees the world. A camera that detects defects in a factory is computer vision and useful, but it is not Physical AI in the sense that matters here. Physical AI is the agent that takes the action. The robot arm that picks up the part and puts it down in a new place. The humanoid that walks into the warehouse and starts moving things. The autonomous tractor that decides which row to spray. The drone that decides which target is real and which is a decoy. The autonomous vehicle that decides whether to brake. The Cloud Kitchen robot that assembles the bowl. The system in the hospital that takes the medicine from one floor to another. All of it shares a common skeleton. There is a perception layer that takes in the world. There is a reasoning layer that decides what to do. There is an action layer that does it. There is a feedback layer that measures whether it worked and adjusts.

If you remember nothing else from this piece, remember that skeleton. Every company in this space is positioning itself on some part of that skeleton. Every investor is implicitly betting on which layer captures the value. Every founder is choosing which layer they will own. The reason the category is confusing is that every company describes itself in maximalist language and every layer overlaps with every other layer. Once you draw the skeleton, you can see who is actually doing what.

Let me start with what most people get wrong.

## The wrong way to think about Physical AI

If you read the press, Physical AI looks like a single race. A bunch of well funded American and Chinese labs are building humanoid robots. Whoever ships first wins everything.

That is wrong in two ways.

First, the race is not one race. There are at least four races happening at the same time, and they will not finish at the same place. The winner of each race captures a different kind of value.

Second, the humanoid is not the destination. The humanoid is the most legible form factor for a much deeper bet, which is that intelligence can finally cross into the real world at scale. If the deeper bet is right, the humanoid is one expression of it. There will be many other expressions. Some of them will look like a single arm bolted to a workbench. Some of them will look like a tractor. Some of them will look like a drone. Some of them will look like a vending machine that builds you a burger. Some of them will not look like a robot at all.

The reason people keep collapsing the category into the humanoid is that the humanoid is photogenic. A humanoid robot doing a backflip on grass produces a clip that goes viral. A robot arm packing boxes in a Foxconn factory does not. Both of them are Physical AI. The second one is making more money today. The first one might make more money in 2030. Neither outcome is decided.

The framing I keep coming back to is this. Physical AI is not a vertical. Physical AI is a transition. The way the economy talks about it now, it sounds like a slot you can compare to fintech or healthtech. It is not that. It is closer to what mobile was in 2008 or what cloud was in 2010. Mobile was not a category. Mobile was a transition that hit every category. Cloud was not a category. Cloud was a transition that re-architected every category. Physical AI is a transition that hits every category where something physical has to happen. Manufacturing. Logistics. Construction. Agriculture. Defense. Healthcare. Hospitality. Cleaning. Personal services. Mining. Food production. Some of these get hit hard and early. Some get hit late. Some get hit in ways nobody predicts. But they all get hit.

The mistake of treating Physical AI as one race against one finish line leads to the mistake of evaluating companies against the wrong scale. If you are evaluating a vertical robot company by the standard of a humanoid foundation model lab, the vertical company will look small. If you are evaluating a humanoid foundation model lab by the standard of revenue today, it will look ridiculous. The two are running in different races for different prizes. Both of them can be right at the same time. Both of them can be wrong.

## There are four races happening at the same time

#1 The first race is for the generalist robot foundation model. The belief is that the same algorithmic insight that gave the world GPT will give the world a single brain that can be transplanted into different bodies and adapted to different tasks. Physical Intelligence in San Francisco is one of the most public bets on this. Skild AI out of Pittsburgh is another. NVIDIA is positioning Project GR00T as the developer infrastructure that the rest of the field will train against. Google DeepMind has been working on Gemini Robotics. Meta has its own bets in JEPA and embodied agents. The prize, if these bets works, is something like operating system level economics for the entire physical economy. Whoever ships the foundation model that every other robot company licenses or builds on becomes the Microsoft of the next decade. The downside is that nobody knows if such a model is possible, and even if it is, the data required to train it may not exist yet.

#2 The second race is for the humanoid as a product. The belief here is that the human shaped body is a clever choice, not a vanity choice, because every workspace and tool in the world was designed around a human. If you have a robot that fits where a human fits and grips what a human grips, you can drop it into existing factories, warehouses, hospitals, and kitchens without redesigning anything. Figure in Silicon Valley, Tesla with Optimus, 1X out of Norway, Apptronik in Austin, Agility Robotics in Oregon, Sanctuary AI in Vancouver, Boston Dynamics now owned by Hyundai, and a long list of Chinese players including Unitree, AgiBot, Fourier, UBTech, and XPeng are all racing here. The prize is definitely over a hundred billion dollar consumer or enterprise product. The downside is that the unit economics of the humanoid are brutal. Today, the actuators alone cost forty to sixty percent of the bill of materials. Battery life is two to four hours under industrial workloads. Safety in human spaces is hard. Reliability is harder.

#3 The third race is for vertical specialization. The belief is that the right form factor for most of the value is not a general humanoid. It is a purpose built machine for a single workflow that can be sold to a known buyer with a clear payback. Niqo Robotics in Bengaluru building agricultural spraying robots. CynLr in Bengaluru building an object intelligence platform for assembly. Mowito working on automotive and electronics assembly. GreyOrange running fulfillment software for warehouses. Anduril building autonomous defense systems. Atoms, Travis Kalanick’s new company, building Bowl Builder for kitchens. The prize here is not a hundred billion dollars per company, but it could be hundreds of billion dollar verticals collectively. The downside is that vertical robots historically have not compounded the way software did, because each deployment was custom.

#4 The fourth race is for the substrate. The data, the simulation, the synthetic environments, the manufacturing supply chain, the actuators, the sensors, the chips, the energy. NVIDIA selling compute and Isaac Sim to everyone else. Scale AI, Surge AI, Mercor, and dozens of newer plays paying gig workers to wear cameras and record actions. Human Archive raising 8.2 million dollars to put cameras on Indian gig workers and ship data to robotics labs. Pronto, the home services company, fielding cameras inside Indian kitchens. China owning sixty three percent of key component manufacturing and ninety percent of heavy rare earth processing. This race is the pick axes during the gold rush. The picks are sometimes more durable than the gold mines.

I think the mistake most outside observers make is to pick one of these races and treat it as the whole category. The four races feed each other. The substrate enables the foundation model. The foundation model enables the humanoid. The humanoid drives demand for the substrate. The vertical specialist absorbs cash and pays for the data that trains the next foundation model. The whole thing turns together. If you want to be useful in this category, you have to hold all four in your head at once.

## Let’s get familiar with some language

The phrases that get thrown around in physical AI carry weight and often confuse beginners.

1. When someone says VLA, vision language action, they are pointing at the architectural insight that you can string together a vision model that perceives the world, a language model that reasons about it, and an action head that turns the reasoning into motor commands. The architecture is real and impressive. It is not a guarantee that the system will work in your warehouse next Tuesday.

2. When someone says generalist, they usually mean a model that has shown some ability to handle a small number of tasks in a small number of environments it was not trained on. They are pointing at a real and important capability. They are not pointing at a robot that can be dropped into your factory and figure out how to work there.

3. When someone says world model, they mean a system that has learned a representation of how the world behaves so it can predict what happens next given an action. The representation is genuinely useful for planning. It does not mean the system has a complete understanding of physics.

4. When someone says embodied AI, they mean AI that has a body. The body matters because it constrains what the AI can do and what data it can collect. The body does not, by itself, give the AI new abilities.

Every one of these phrases is doing work. Every one of them is also being used to dress up things. The way you tell the difference is to ask the question the seller does not want, which is, what is the demo doing that the deployment cannot? The gap between the two is where the truth lives.

Inside that glossary, there are two architectural debates worth knowing about, because they decide what kind of robot company you are looking at.

- The first debate is about how the action is generated. The early VLA models tried to predict robot actions the way a language model predicts the next word, one token at a time. That worked for simple tasks and broke on smooth multi step motion. The breakthrough that made real manipulation possible was the diffusion policy, which generates an entire short action sequence at once by starting with noise and denoising it into a clean trajectory. Most of the systems you read about today, including Physical Intelligence’s pi zero and pi 0.5, Toyota Research Institute’s Large Behavior Models with Boston Dynamics, and the next wave of academic work, sit on some flavor of this idea. If a founder tells you they have a VLA but cannot tell you how the action head is structured, the model is probably not where the moat is.

- The second debate is about how reasoning and reflex are split. The most useful architecture pattern in 2026 is the two model stack. A slower vision language model thinks about the goal and the scene. A faster sensorimotor model takes that goal and turns it into joint commands at high frequency. Figure’s Helix, NVIDIA’s GR00T direction, and several academic systems all converge on this. It is the robotics version of the system one and system two split that cognitive scientists have argued about for decades. A robot that tries to do everything inside one giant model usually falls over because it cannot react fast enough. A robot that splits thinking and reflex can do both.

If you remember just one thing from this section, remember that the company that says generalist is doing one of two things. It is either betting on a single end to end model that scales with data, or it is betting on a two model stack that splits reasoning from reflex. The first is more elegant. The second is what works today.

## The question changes when software stops advising and starts acting

There is a deeper shift happening underneath the noise.

For most of software’s history, software advised humans. The human did the work. The software made the work faster or more legible. Even ChatGPT, by default, is an advisor. You ask it something. It tells you something. You decide what to do.

In Physical AI, the software does not advise. It acts. The agent enters the chain of consequence. The chatbot answers the customer and the customer takes action based on that answer. The picking robot picks the part and puts it on the production line. The autonomous vehicle decides whether to brake. The medical AI flags a case and a regulator sees it.

The difference is not philosophical. It changes everything downstream. A copilot can be wrong without much liability. A robot or physical agent that acts cannot. A copilot can be uncertain and offload the decision to the human. A physical agent has to decide and live with the decision. A copilot can be slow because the human will wait. A physical agent has to be fast because the world will not. A copilot can be deployed by a single developer in a single afternoon. A physical agent has to be tested in simulation, in controlled environments, in pilots, in production, with monitoring, with fallbacks, with safety systems, with insurance, with a chain of accountability that the regulator can audit. Copilots that are inaccurate even 50% of the time get the job done. Physical agents that make mistakes even 5% of the time can halt supply lines. That is a hundred to a thousand times higher bar on reliability, and there is no marketing copy that can cover it.

This is why the physical AI category looks much harder than the software AI category. It is harder. The difficulty is not a bug. It is the source of the moat. Anything that hard to build is hard to copy. The companies that successfully cross from demo to deployment will not face the kind of margin compression that pure software AI is facing right now, because the substrate they live on is too physical, too expensive, and too operationally complex for fast followers to replicate.

The companies that take this category lightly will burn out. The companies that take it seriously will compound in ways software has not been able to in a decade.

## What the big players are really doing

Let me actually walk through who is doing what. Because most of the writing on this skips this part, and you cannot evaluate the category without knowing the players.

I will group by which race each company is primarily running. Some companies are in more than one race. That is intentional and important.

The foundation model labs.

Modern generalist robotics community is a small tree, and Pieter Abbeel sits near the root. Abbeel founded Covariant, sold its foundation model team to Amazon in 2024, and trained a generation of researchers at Berkeley who are now leading or seeding most of the labs in this race.

Physical Intelligence is the cleanest example. The company was started in 2023 by Karol Hausman from Google’s robotics team, Sergey Levine from Berkeley, and Lachy Groom, a former Stripe executive. The company has raised approximately one billion dollars across rounds, including a Series B of six hundred million dollars in November 2025 led by CapitalG at a 5.6 billion dollar valuation. Their model originally was a generalist robot policy that combined vision, language, and action. Their next model, made a real leap. It showed meaningful generalization to entirely new environments, controlling mobile manipulators to perform household tasks in homes that were never seen during training. The belief here is that the algorithmic insight from large language models can transfer to robotics if you can solve the data problem.

Skild AI, founded by former Carnegie Mellon professors Deepak Pathak and Abhinav Gupta, raised 1.4 billion in Series C in January 2026 led by SoftBank, with NVIDIA, Bezos Expeditions, Macquarie, and Lightspeed in the round. Valuation hit fourteen billion. The Skild Brain is positioned as the industry’s first unified robotics foundation model that can control any robot regardless of body form, from quadrupeds to humanoids to tabletop arms to mobile manipulators. The belief is that the right architecture can be embodiment agnostic.

NVIDIA’s Project GR00T is the third axis. Jensen Huang has been saying for two years that the age of generalist robotics is here, and NVIDIA is building the picks and shovels. Isaac Sim for simulation, Isaac Lab for parallel reinforcement learning, Cosmos for world foundation models, Omniverse for synthetic data generation. GR00T N1, then N1.7, then GR00T N2 previewed at GTC 2026. The belief is that the foundation model layer will commoditize, and NVIDIA will own the layer underneath that every commoditized model has to train on.

Google DeepMind has Gemini Robotics, the architecture for VLA that they have been working with Apptronik to deploy on the Apollo humanoid. Meta has been investing in V-JEPA and embodied agent work. Microsoft is closer to the application layer through OpenAI’s stake in Figure. xAI has not committed publicly to a robotics push but Elon Musk has Optimus.

The humanoid builders.

Tesla Optimus is the most ambitious humanoid bet on paper. Elon Musk has committed to mass production of Gen 3 starting in summer 2026 at the Fremont factory, with a target of one hundred thousand to three hundred thousand units in the first year, priced at 20k-30k dollars. Tesla is converting Model S and Model X lines to make room for Optimus. The plan is to scale to a million units a year, eventually ten million. Whether this happens is a different question. Musk has missed deadlines on autonomous driving by years at a time. The interesting thing is the production decision. Tesla is treating Optimus the way it treated the Model 3, which is to say, the manufacturing line is the bet.

Figure AI raised 1 one billion dollars in September 2025 at a 39 billion dollar valuation, with Brookfield, Intel, Macquarie, NVIDIA, Parkway, Qualcomm, Salesforce, and T-Mobile in the round. The company is on its third humanoid, Figure 03, and its second internally developed VLA, Helix 02. BMW has been running an eleven month pilot with Figure 02 at its Spartanburg plant, the first publicly documented production scale humanoid deployment in automotive manufacturing.

1X Technologies, the Norwegian American company backed by OpenAI, opened a Hayward, California factory in April 2026 to build humanoids at scale. Their NEO consumer humanoid sold out its first year’s production capacity in five days when preorders opened in October 2025, at twenty thousand dollars per unit or 499 dollars per month. The first year capacity is 10k units. The company is also doing teleoperation directly on customer sites, which is a clever way to close the embodiment gap that we will come back to.

Apptronik in Austin raised approximately 935 million dollars and is at a 5 billion dollar valuation. Apollo, their humanoid, is deployed at Mercedes-Benz. The partnership with Jabil to manufacture Apollo at scale is the structural play. The partnership with Google DeepMind for the AI is the model play.

Boston Dynamics, owned by Hyundai, unveiled the production version of electric Atlas at CES January 2026 and began production immediately. The entire 2026 production run is committed to Hyundai’s Robotics Metaplant Application Center and Google DeepMind. Hyundai announced a twenty six billion dollar investment in US operations including a robotics factory capable of 30k robots per year. This is the most concrete capacity buildout in the West.

Unitree out of Hangzhou plans to ship 29k humanoids in 2026, four times what they shipped in 2025. They have placed robots on the factory floors of Nio and Geely. Their G1 humanoid lists at 13.5k dollars. AgiBot, Fourier, UBTech, XPeng AeroHT, and a dozen others are scaling.

The number to internalize is that Chinese humanoid makers in aggregate are shipping at volumes Western humanoid makers have not yet contemplated, while Western humanoid makers are valued at multiples Chinese makers have not yet hit. Both are true. Both are interesting. Neither tells you who wins.

The vertical specialists.

There are too many to list completely. The shape of the belief is however clear. Pick a workflow. Pick a vertical. Build a robot that does that workflow inside that vertical with reliability that traditional automation cannot reach. Niqo Robotics for agricultural spraying. CynLr for assembly object intelligence. Mowito for automotive and electronics assembly. GreyOrange for warehouse fulfillment. Addverb for industrial automation including their own humanoid for hazardous environments. Locus Robotics for warehouse mobile robots. Symbotic for warehouse automation at hyperscale. Berkshire Grey, acquired by SoftBank, for warehouse picking. Cobalt Robotics for autonomous security patrols. Brain Corp for autonomous floor cleaning. Picnic for pizza assembly. Sweetgreen and Chipotle running their own robotic kitchens through Hyphen and Autoocado. The list is long. The pattern is the same. Pick the workflow. Own the deployment loop. Compound on the data.

The substrate companies.

NVIDIA is the obvious one. Compute, sim, world models, synthetic data. The substrate company that gets paid no matter who wins the race above it. Apple is sitting on its own substrate with Vision Pro and AR data, but has not yet declared a robotics intent publicly. Anduril is the substrate for defense, with the Lattice platform now under a 20 billion dollar US Army contract for Army wide integration. Palantir, Anduril’s distant cousin, sits in adjacent territory with deployments across allied forces. ABB, KUKA, Fanuc, and the old industrial robot OEMs are the substrate that the new physical AI gets layered on top of. Their incumbent advantage is real and is often underweighted by the press.

The data plays.

This is the part most external commentators are missing, and the part that, in my view, is most under priced as an opportunity inside the category. We will spend a whole section on it later.

Now. With the player landscape on the table, the question becomes, which race actually wins, and how?

I think the honest answer is that all four win, but the prizes are different sizes and the prize timing is different. The substrate companies are winning now and will keep winning regardless of what happens above them. The vertical specialists will compound steadily through the next decade, with a small number of category leaders emerging in each major industry. The humanoid builders will face brutal unit economics for the next three to five years and then, if and only if the actuators get cheap enough and the data gets rich enough, they will start producing the headline outcomes. The foundation model labs are the highest risk and the highest potential prize. They look like AGI bets with a robot wrapper. Most of them will not return the capital. The ones that do will produce ten figure outcomes.

The interesting question is not which company wins. The interesting question is where the value compounds fastest and where the moat is deepest. Both lead to the same answer, which is, look at the substrate.

## What it actually costs to build a humanoid right now, and why that matters?

A humanoid robot today costs between 30k and 150k dollars per unit to manufacture, depending on capability level and production volume. In 2023 and 2024 the same units cost 150k to 500k USD because production runs were small and components were custom.

The bill of materials breaks down roughly as follows. Actuators and motion systems are forty to sixty percent of the cost. Sensing and perception systems are ten to twenty percent. Compute and control platforms are ten to fifteen percent. Structural components are five to ten percent. Battery modules are five to ten percent.

The actuator number is the one that controls everything else. High torque actuators for hip and knee joints currently cost 500 to 2000 dollars per unit at low volumes. At Tesla’s target of one million units per year, those same actuators could drop to 100 to 300 USD each through dedicated production lines. That is a single line item potentially saving 15k to 25k dollars per robot. The unit economics of a humanoid depend almost entirely on whether the manufacturer can get to that volume.

The supply chain math is even more brutal. Building Tesla Optimus Gen 2 without Chinese suppliers would have cost approximately three times as much, with the bill of materials rising from 46k to 131k dollars per unit. China controls sixty three percent of key component manufacturing for humanoid robotics. China controls ninety percent of heavy rare earth processing. China dominates harmonic drive production. China owns approximately seventy seven percent of global battery production capacity. Battery energy density limits continuous operation to two to four hours under industrial workloads.

Companies like Schaeffler and Ziehl Abegg have started shipping actuators that use ferrite magnets instead of neodymium, because that is the early signal that the rare earth dependency will be engineered around over the next decade.

There is a phrase in the trade press about humanoid economics that I think is half right and half wrong. The phrase is that humanoids will follow Moore’s law down to a 1000 dollar consumer product. The cost will come down. The Moore’s law framing is wrong because Moore’s law was about a single process node and a single industry that consolidated in two countries. Humanoid cost reduction depends on actuators, batteries, sensors, and compute, each with its own supply chain and its own innovation pace, none of which are coupled the way semiconductor processes were. The cost will come down on the order of five to ten times over the next five years, not five hundred times. That is still a huge unlock though. Is it a consumer phone level unlock though??

Cost is only half the unit economics. Reliability is the other half, and it is the half that most public commentary leaves alone because the numbers are embarrassing.

Industrial buyers measure equipment by mean time between failures. A traditional Fanuc or KUKA arm in a car plant will run for tens of thousands of hours between meaningful interventions. That is the bar a humanoid is being judged against. The actual humanoid bar today is not even close. Most public deployments report continuous operation in the range of two to four hours before the battery needs swapping, and meaningful operator intervention every thirty to ninety minutes during real tasks. Gripper failures sit in the five to fifteen percent range whenever the robot meets an object it was not trained on. A humanoid that drops one item out of ten on a packing line is not a productivity gain. It is a liability.

This is why every credible humanoid pilot you read about today, including Figure at BMW, Apptronik at Mercedes, and Agility at GXO, is a supervised pilot with an engineering team on site. Tesla has been honest about Optimus being in data collection mode rather than productive mode. None of this is a failure. It is the expected shape of a real industrial product in its first five years. But it should reset what anyone expects when a CEO says the humanoid is ready. Ready means ready inside a tightly bounded shift, under supervision, on a task the robot has seen many times. Ready for an unsupervised eight hour shift on a task list the robot has never seen is at least five years away, probably ten.

The lesson for an evaluator is to ask for one number. What is the longest continuous shift this robot has run in production, on a customer site, without operator intervention. If the answer is anything less than a full shift, the company is still in the demo phase regardless of what the website says.

The lesson for evaluating a humanoid company is that you should be looking at three things in this order. First, the actuator supply chain. Who builds their actuators, where, at what cost, with what redundancy. Second, the manufacturing line. Do they have a real plan to get to ten thousand units a year and then a hundred thousand. Third, the model. The model matters but it is downstream. If you cannot make the robot at scale at a defensible price, the model does not matter.

This is also why Hyundai’s commitment to a 30k units per year factory for Boston Dynamics Atlas is more strategically important than the model partnerships Boston Dynamics is announcing. Same for Tesla’s conversion of Model S and Model X production lines. Same for Apptronik’s Jabil partnership. Same, painfully, for the entire Chinese supply chain advantage. The humanoid race is, at heart, a manufacturing race. Models are necessary. Manufacturing is decisive.

## Why vertical robots are not a small ambition?

A lot of people make a mistake when they talk about vertical robotics. They treat it as the safe, less ambitious version of humanoids.

I think that is wrong.

A vertical robot company can become very large if the workflow has four properties.

The workflow repeats constantly. Failure is expensive. The buyer has a clear way to measure ROI. And every deployment teaches the system something that makes the next deployment better.

That last part is the whole game.

A robot that learns only inside one customer’s site is not enough. A services team that solves the same customer problem manually again and again is not enough. A founder who keeps saying every deployment is different is probably telling you the company is not compounding yet.

The real question is that after the tenth deployment, is the eleventh deployment cheaper, faster, and more reliable?

If yes, you may have a robotics company. If no, you may have a high margin services company that thinks it is a robotics company. The difference is enormous over a decade.

Most of the verticals worth thinking about right now sit at the boundary between heavy industry and software adoption. Picking and packing in warehouses. Sub assembly in electronics. Specific stations in automotive plants. Spraying and harvesting in agriculture. Cleaning in commercial spaces. Logistics inside hospitals. Surveillance and inspection in industrial sites. Defense ISR, intelligence surveillance and reconnaissance. Food service prep work. Each of these can be a billion dollar plus opportunity if the company gets the loop right.

The painful truth is that most of them will not. Vertical robotics companies have historically had a brutal time. The reason is structural. Robots are sold one workstation at a time. Each new sale requires custom development. The system integrator does most of the deployment work. The startup carries the deployment cost, not the integrator. Sales cycles run three to six months minimum. Ford takes three years to even register a vendor. By the time you have built a referenceable customer, you have spent your entire seed round.

The companies that win at vertical robotics will be the ones that learn to act more like software companies than traditional automation companies. The unit of repeatability is the model, not the install. The unit of distribution is the integrator partner network, not the direct sales engineer. The unit of compounding is the deployment dataset, not the customer logo.

I had a long conversation recently with Puru Rastogi, the founder of Mowito. He is a college friend. The company was doing warehouse automation for years and recently pivoted to automotive and electronics assembly. The pivot did not require changing the team because the team was a robotics engineering team and the model architecture transfers. What changed was the optimization parameter. Warehouses tolerate 1-2% failure because of volume. Manufacturing demands six to nine sigma. The same algorithm now has to be five orders of magnitude more reliable. He told me, almost in passing, the thing that I think is the deepest insight from anyone working in this category. He said, the cars are made every day, 24*7*365. No factory will shut down to try out your solution. The plant will entertain you in the lab. They will not deploy you in the production line. It will take three years just to register you as a vendor. Even Ford takes three years.

If you have read about Coalition and how cyber insurance got built, you know the rhythm. The first two years are spent paying for trust. The next two years are spent earning enough trust to be invited into the room. The next two are spent compounding inside the room. You cannot compress this timeline. You can only choose whether to invest in it.

There is a separate trap in vertical robotics that I want to call out, because I have watched it kill companies. The trap is to confuse R&D progress with company progress. A robotics company with a great demo and no contract is not a robotics company yet. It is a research project that has not yet found its buyer. The transition from research project to company happens when the company finds a buyer who will pay for outcomes the buyer can measure, and the buyer keeps paying as the next deployment compounds on the last. Until that flywheel is visible, the company is still in research mode. Most vertical robotics companies that fail, fail because they spent the seed round on the research without ever turning it into the company.

The companies that get past this trap tend to do three things differently. First, they pick a vertical where the buyer is already paying someone to do the work and the cost of failure is high enough that they will pay a premium for reliability. Second, they aim for the system integrator partnership, not the direct sale, after the first reference customer is in. Third, they treat every deployment as a data event, not a project event. The deployment is over when the data has improved the model, not when the install is done.

## The hard problems are not the ones in the demo

The single biggest mistake I see people make when they evaluate physical AI companies, especially as outside observers, is to confuse the demo with the product.

Demos are designed to look impressive. They run on the best hardware, in the best lighting, with the best operator. They use cherry picked tasks that the model was trained on or that the human teleoperator has been practicing. They are short, so the system has not had time to drift. They are filmed for clip length, not run for shift length.

The product has none of these advantages. The product has to run for eight hours, then ten, then twelve. It has to deal with lighting it has not seen. It has to handle dust on the camera, scratches on the lens, vibration from the surrounding machines. It has to fail gracefully when an unexpected object enters the workspace. It has to be reset by a worker who did not write the model. It has to be maintained by a technician who does not know what a VLA is.

The single most useful question you can ask anyone building a humanoid or a vertical robot is this. “What is your robot’s mean time between failures, in production, in a customer environment, on a real shift, not in your lab?” The answer separates the real product that deployable at scale from the demos.

A second useful question is, “what part of your robot needs a human operator standing nearby?” Most demos have a human within five meters who is ready to grab the kill switch. Production deployments cannot afford that. If the human is part of the deployment, the unit economics do not work and the customer is paying twice for the work.

A third useful question is, “how much data do you need to train the robot to do a new task, once you are deployed?”. If the answer is, we need to retrain the model with a hundred hours of new demonstrations every time the customer asks for a new SKU, you are not selling automation. You are selling a service that uses a robot. There is a real business there, but it is a different business than the one most founders are pitching.

The reason these questions matter is that they expose the gap between the prototype and the product. The prototype is what raised the money. The product is what makes the money. The companies that close the gap will compound. The ones that do not will run out of capital before they figure out why.

There is a reason this gap keeps showing up across companies and decades. It is called Moravec’s paradox. Hans Moravec wrote it down in 1988. The things humans find easy, like picking up a crumpled t shirt or walking on uneven ground, are the things machines find hardest. The things humans find hard, like beating a grandmaster at chess, are easier for machines than they look. The reason is that perception, balance, and dexterous manipulation are the oldest layers of the human brain and the most heavily tuned. We do them without thinking, so we underestimate how much computation they take.

Physical AI is the field that has to pay the bill for that paradox. The bill is mostly paid in two places that do not get enough attention.

- The first place is touch. Almost every demo you see runs on vision and language. The robot looks, the robot reasons, the robot moves. What is missing is the sense that lets a human pick up a soft tomato without crushing it, or feel that a screw is one quarter turn from being tight. Researchers at Meta, MIT, and a handful of academic labs have been building tactile sensors like GelSight and DIGIT that turn touch into something a model can learn from. Without good touch, dexterous manipulation in cluttered environments stays brittle. With good touch, the robot starts to behave less like a programmed arm and more like a hand. Anyone evaluating a humanoid or a manipulation company should ask one extra question. What does the robot feel, and how is that signal used.

- The second place is the long tail of edge cases. This has been touched upon in the autonomous driving section. It is the same problem here. The reason the demo to deployment gap is so large is that the demo only has to survive a few minutes inside the distribution the robot was trained on. The deployment has to survive eight hours inside a distribution the world keeps editing. Closing that gap is not a software fix. It is a years long grind on data, on hardware, on monitoring, and on touch.

There is a separate set of hard problems that lives below the model and above the hardware. People in the field call it the embodiment gap. The idea is that even if you have a perfect generalist model trained on perfect data, the model still has to be translated into commands for a specific physical body. The body has its own quirks. The actuators have their own latencies. The sensors have their own noise. The same model on two different humanoids will perform very differently. Closing the embodiment gap is the kind of grinding engineering work that does not get written about, but it is where most of the deployment effort actually goes.

One way companies are starting to close this gap is by doing teleoperation directly on the customer’s robot. 1X is the most public example. Instead of training a model in a lab and then deploying it onto a customer site, they are putting the robot on the site, having a human operator drive it remotely, and using the data from that operation to train the model in place. The advantage is that you are training on the actual embodiment in the actual environment. The disadvantage is that scaling teleoperators is its own logistics problem. Traditional automation companies that have already deployed tens of thousands of robotic arms, like the players Puru competes with, are starting to add this approach to their existing fleets. Teleoperation is the bridge between the model layer and the physical layer that nobody talks about and everybody is now investing in.

The cleanest way to think about the role of humans in the deployment loop is as a ladder with four rungs, and every physical AI company is on one of them whether they admit it or not.

1. The first rung is full teleoperation. A human is driving the robot in real time. The robot has no autonomy. The output is data. This is where most humanoid pilots are today, even when the marketing says otherwise.

2. The second rung is shared autonomy. The robot does most of the motion on its own and a human takes over for the hard parts or the high stakes parts. Surgical robotics has lived on this rung for two decades. Most warehouse pilots run here.

3. The third rung is supervised autonomy. The robot runs by itself for a full task or a full shift. A human watches, can intervene, but rarely does. The robot is allowed to fail in low stakes ways without anyone stepping in.

4. The fourth rung is full autonomy. No human is in the loop. The robot is responsible for its own actions. Almost nothing in physical AI is here yet. Waymo gets close inside its operational design domain. Nothing in the humanoid world is anywhere near it.

The ladder matters because the unit economics, the insurance treatment, and the regulatory exposure all change at every rung. A company that says it sells full autonomy when its robots are actually on rung one or two is mispricing the product and exposing the customer. A company that owns where it is on the ladder and has a credible plan to climb is usually a better bet than a company that claims to be already at the top.

## Lessons from twenty one years of autonomous driving

I want to spend a section on autonomous driving, because almost everyone in physical AI has either internalized the wrong lessons from it or has not engaged with it at all.

Autonomous driving is the only large scale physical AI category that has been live for more than two decades. It’s phenomenal because I read a book on this almost 7-8 yrs back and I still get fascinated when I reflect on the contribution DARPA, as a defense research agency, has made to world innovation. DARPA’s Grand Challenge was 2004. The Urban Challenge was 2007. Sebastian Thrun’s team at Stanford that won the 2005 race became the seed of Waymo. Waymo, in its various names, has been working continuously since 2009. Today in San Francisco, I still get amazed by the volume of Waymo that will pass you if you just stand at one spot for 5 minutes. Tesla started Autopilot development in 2014. Cruise was founded in 2013. Mobileye was founded in 1999 and went public in 2014, then was acquired by Intel for fifteen billion in 2017, then spun back out as a public company. Aurora, Argo, Zoox, Nuro, Pony AI, WeRide, Baidu Apollo, and a long list of others have raised tens of billions of dollars combined.

Here is what twenty one years of capital and effort have produced. Waymo is operating commercially in a handful of US cities. Its safety record is now better than human drivers on the routes it covers, with eighty four percent fewer airbag deployments and seventy three percent fewer injury causing crashes across twenty two million miles. Cruise shut down most of its operations after a 2023 incident in which a Cruise vehicle dragged a pedestrian twenty feet after a human driven car had hit her into its path. Tesla still has no vehicles permitted to operate at SAE Level 4 anywhere in the world. Mobileye has a profitable advanced driver assistance business but has not produced a true self driving vehicle. The category exists, but the prize, full Level 5 driving anywhere on any road, is still ahead.

The lessons from this body of work are important for physical AI more broadly. They include the following.

First, demos take ten years to become deployments. The first Tesla Autopilot demo was 2014. The first commercial Waymo robotaxi service was 2018. Eleven years from Stanford’s win to commercial deployment. Six more years to material scale. People who tell you the humanoid will be in homes by 2027 should be asked, in the same breath, what timeline they expect from the autonomous vehicle category that started fifteen years earlier and is still not done.

Second, the long tail of edge cases eats your timeline. Waymo’s recent freeway suspension after construction zone issues. School bus recalls. Flooded streets in Atlanta. The first ninety nine percent of cases takes a quarter of the time. The last one percent takes three quarters of the time. Anyone selling a physical AI deployment without a plan for the long tail is selling something they have not finished building.

Third, the safety pyramid is real. For every fatal accident there are dozens of injuries. For every injury, hundreds of property damage events. For every property damage event, thousands of close calls. Companies that survive in this space build monitoring all the way down the pyramid, not just at the top. Cruise died in part because it could not act on close calls fast enough.

There is a quieter consequence of this safety pyramid that does not show up in the autonomous driving headlines but that every physical AI company will run into. The pyramid is what creates the demand for insurance and certification in physical AI, and that demand is going to be much harder to meet than the same demand was in software AI.

I wrote a longer piece on this category in the agent context, called Insurance for AI Agents. The argument was that any system that takes action on behalf of a company creates a liability question that existing insurance lines were not designed to absorb, and that a new category gets built when four conditions become true at once. Adoption at scale, losses materializing on a curve, existing carriers walking away through exclusions, and regulators forcing buyers to acquire coverage that does not yet exist. All four conditions are now true for software agents. They are becoming true for physical AI faster than people realize.

Physical AI is the harder version of the same problem. When a chatbot is wrong, the loss is usually economic and the proof is in the logs. When a humanoid is wrong, the loss can be physical and the proof requires sensor data, camera data, joint state data, control data, and the chain of inputs that led to the action. ISO has already started moving. ISO 13482 covers service robots that operate in human spaces. ISO 10218 covers industrial robots. UL 3300 covers service robots around untrained people. These are the standards a serious physical AI company has to map to before any major enterprise customer will sign. Carriers are starting to write affirmative coverage. EY has written publicly that physical AI will be more disruptive to the insurance industry than generative AI ever was, because the liability shifts from human operators to the system itself.

For a founder, the practical lesson is that the insurance and certification layer is not paperwork you do at the end. It is the layer that decides whether the buyer can sign. The companies that build to a known standard from day one, instrument their robots so claims investigations are possible, and partner early with carriers and standards bodies, will close enterprise deals faster than the companies that try to retrofit later. The same flywheel that is forming around agent insurance is going to form around physical AI insurance, and it is going to form first in healthcare, defense, and industrial deployment, where the cost of a bad action is too large to absorb without a financial backstop.

Fourth, regulation moves slower than the technology. Waymo and Tesla are still operating under a patchwork of state by state rules in the US. The EU has been gradually clarifying its position. China has been more aggressive about deployment but is still finding its footing. The regulatory environment for physical AI more broadly will look similar. Slower than founders expect. Faster than they say in their pitch deck.

Fifth, capital intensity is the dominant feature. Waymo has burned through approximately 30 billion dollars over its life. Cruise burned through over 10 billion before it was effectively shut down. Aurora has burned over 5 billion. The companies that survived had a parent willing to keep funding them through bad years. The category leader, Waymo, has Google. The companies without a deep pocketed parent did not make it. Physical AI in general is going to require the same kind of patient capital and that’s another reason why countries like India can aspire but they are dreaming before they have truly deserved the innovation. If a vertical physical AI startup is raising a typical software round of fifteen million and aiming for a typical software outcome in three years, they have priced the wrong opportunity. The companies that win in this category will look Mobileye’s two decade arc, than like a Series A SaaS company.

Sixth, the model improvements compound, but only when the data scales. Tesla’s Autopilot improved when Tesla started collecting fleet data at scale. Waymo’s safety statistics improved when they accumulated million mile multiples. The implication for physical AI is that the data layer is not optional. It is the precondition for the compounding to start.

There is one more lesson that I think is the deepest. The companies that succeeded at autonomous driving did not succeed because they had the best model. They succeeded because they had the best deployment loop. The model was necessary but the loop was decisive. The loop is the closed cycle that runs from sensor data to model training to deployment to monitoring to incident response back to sensor data. The companies with a tight, well instrumented loop got better faster than the companies that did not. The same will be true for physical AI broadly. Whoever has the tightest loop wins.

## The bitter lesson and what it means for robotics

The bitter lesson ([a must-read)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), as Rich Sutton wrote it in 2019, is that general methods that leverage computation are ultimately the most effective. Hand crafted features and clever engineering tricks lose to large models trained on lots of data on lots of compute. The lesson is bitter because it implies that decades of careful human engineering can be wiped out by an undergraduate with enough compute. It has been right about almost every category in AI it has been applied to.

The question for physical AI is whether the bitter lesson holds here too. The answer, I think, is yes, with one critical caveat.

The caveat is data.

In language and vision, the data for the bitter lesson to compound on was already on the internet. Trillions of tokens of text. Hundreds of billions of images. Decades of human content waiting to be ingested. The bitter lesson worked because the data was free. Compute was the constraint. Once compute became affordable, the data did the work.

In robotics, the data is not on the internet. Robot data is the combination of perception, language description, and motor command that lets a model learn to act. It does not exist in nature. It has to be collected, either by deploying robots and recording what they do, or by simulating environments and synthesizing trajectories, or by putting cameras on humans and recording how humans do things. All three approaches are active right now. None of them have solved the data problem yet.

Sergey Levine, one of the co founders of Physical Intelligence and a professor at Berkeley, has written extensively on the data scale problem in robotics. His framing is that internet scale data used to train modern vision language models is on the order of one hundred thousand years of human viewing time. The data needed to train robots is a multiple of that, because robots have to learn the action component as well as the perception component. The data does not exist. It has to be generated. Levine has estimated that if every McDonald’s in the US had one robot working two hours a day, you could generate ten million hours of robot experience in a year. Multiply that by all environments, embodiments, and tasks and you can credibly close the data gap in 5-10 years. The math is not crazy but it is also not free.

It helps to make the data layer concrete by naming the bricks that already exist. Open X-Embodiment, released by Google DeepMind and a coalition of thirty plus university labs, is a federated dataset of more than one million robot trajectories across twenty two different robot bodies. DROID is a single embodiment dataset of about seventy six thousand demonstrations collected on the same Franka arm across hundreds of household and tabletop scenes. AgiBot World, which the Chinese humanoid company AgiBot is releasing in 2026, is the first real attempt at a humanoid scale dataset from real environments. On the human side, Meta’s Project Aria glasses are pulling in egocentric video from real wearers, EgoMimic showed that ninety minutes of Aria recordings can boost a robot’s task performance by four times, and Build AI released Egocentric one million in April 2026 with one million hours of first person video including factory workers in Southeast Asia.

This list matters for two reasons. First, you can now see what people mean when they say robot data is small. The largest open robot dataset on earth has about a million trajectories. A language model trained on the internet sees something like ten trillion tokens. The gap is six orders of magnitude. Second, you can see where the active debate is. The newest research, in particular a wave of papers in 2025 and 2026, has shown that the diversity of environments and objects matters more than the raw count of demonstrations. After a certain threshold, the next demonstration in the same kitchen teaches the model almost nothing. The next demonstration in a new kitchen teaches it a lot. This is why the Indian data play, if it focuses on the variety of Indian settings rather than on the cheapest possible hour of video, has a structural advantage that volume alone could not produce.

The thing to keep an eye on, if you only have time to track one shift, is the move from raw egocentric video to multi sensor egocentric capture with hand pose, body pose, tactile signal, and gaze. The buyers of data are not asking for hours anymore. They are asking for clips where every sensor on a human body has been captured cleanly. The operators who can produce that are getting paid two to three times more than the operators who can only produce video. The shift is happening this year.

This is the framing that explains why the data economy in physical AI is so important and why it is the layer that, in my honest opinion, captures the most under priced value in the entire category right now. Whoever can credibly produce the next 100 million to 1 billion hours of high quality, sensor fused, embodiment relevant robot data will be sitting on a substrate that every foundation model lab has to buy from. The supply is currently a small fraction of that.

There are roughly three ways the data is going to get generated.

1. The first is teleoperation. Humans drive robots remotely. The robots collect data on the actual embodiment in the actual environment. The advantage is high fidelity. The disadvantage is cost. Each hour of teleoperated data costs roughly the same as an hour of human labor, plus the cost of the robot. This works at a small scale and does not scale to a billion hours.

2. The second is simulation. Robots are trained in synthetic worlds, generating millions of trajectories at near zero cost. NVIDIA’s Cosmos and Isaac platforms are betting on this. The advantage is scale. The disadvantage is the sim to real gap. A robot trained perfectly in simulation often fails in reality because the simulation never quite matches the physics, the noise, the friction, the dust. Closing the sim to real gap is one of the active research frontiers, and progress has been real, but the gap still exists.

3. The third is wearable data collection. Put cameras on humans. Record how humans do things. Use the human data to pre train a model, then fine tune the model on robot data. The advantage is that humans are everywhere and cheap. The disadvantage is the embodiment gap. Human bodies are not robot bodies. Data collected from human action does not perfectly map to robot action. But for the perception side of the stack and for general world understanding, human data is enormously useful. This is the layer where the Indian gig worker data economy is forming.

The bitter lesson says that whichever method generates the most data fastest will win. The honest answer is that the winning system will use all three. Simulation for scale and edge cases. Teleoperation for fidelity. Wearable data for breadth. The companies that figure out how to combine all three will produce the data substrate that the foundation models train on. The substrate is more valuable than the models themselves over a long enough time horizon, because models can be replicated and substrates compound.

There is a version of this debate happening in public this year that you should know about, because it tells you which way the smart money is moving.

On one side, Sergey Levine and the Physical Intelligence camp have been arguing that the only way out of the data gap is to commit fully to real world robot deployment as the source of training data. The robot learns by doing. The fleet learns by sharing. The substrate compounds. In a recent interview, Levine put the median date for general purpose home robots at 2030, conditional on the data flywheel kicking in.

On the other side, Yann LeCun left Meta in early 2026 to raise more than a billion dollars for AMI Labs, on the explicit bet that pixel prediction will never get you to a model that understands the world. He has been arguing for almost a decade that systems should predict in abstract latent space, which is the JEPA approach, rather than try to predict every pixel. V-JEPA 2, the second version of that approach, reported eighty percent zero shot robot control performance from sixty two hours of unlabeled video. If that result holds at scale, it bends the data curve in a way that makes simulation and abstract pretraining far more powerful than they are today.

In the middle sits NVIDIA, which is shipping the Cosmos world foundation models and Isaac GR00T as the substrate that lets anyone, in either camp, train and deploy faster. NVIDIA does not have to be right about the architecture. NVIDIA just has to be the layer everyone else trains against. That is the same position they held in language models.

The honest read of the debate is that the Bitter Lesson holds in robotics, but with a twist. The general method that wins will not be the one with the most compute. It will be the one that produces or consumes the most diverse data fastest, in whatever combination of real, simulated, and egocentric it can stitch together. The companies that bet on one source alone are taking on more risk than they need to. The companies that build for all three are running the safer version of the same bet.

## The country question matters more in robotics than in software

You can build a SaaS company anywhere. You can build a robot company in fewer places.

The reason is that robots have to be manufactured. They have a supply chain. They have to be installed and maintained. The countries that have a deep manufacturing base, a working component supply chain, and an industrial buying class have a structural advantage in the robotics race that they did not have in the software race.

China has the most complete stack. They make the actuators. They make the batteries. They make the sensors. They make the chips. They have the harmonic drives. They have the magnets. They have the rare earths. They have factories that have been running for decades and have automation buyers built into the procurement function. They have a national policy that is explicit and well funded.

That policy is worth understanding in detail, because it is the most aggressive industrial policy bet in the world right now. The Ministry of Industry and Information Technology issued the Guiding Opinions on the Innovative Development of Humanoid Robots in November 2023. In March 2025, embodied AI was named in China’s Government Work Report for the first time, alongside biomanufacturing, quantum technology, and 6G. In the 15th Five Year Plan covering 2026 to 2030, robotics is one of eight strategic emerging industries, which triggers mandatory coordination across all central ministries, provincial governments, and state financial institutions. Beijing announced a 1.4 billion dollar robotics fund. Shanghai issued China’s first plan for embodied intelligence in 2024 with shared infrastructure including compute, testing, pilot production, and financing. Shenzhen launched a 10 billion yuan AI and Robotics Industry Fund in early 2025. In the first quarter of 2026 alone, the embodied intelligence sector recorded 210 financing events totalling over 30 billion yuan, roughly 4.2 billion dollars.

The capital is real. The policy is well coordinated. The industrial base is intact. The cost of producing a humanoid in China is, as we covered above, roughly a third of producing the same humanoid elsewhere. The supply chain advantage compounds with each production cycle.

The United States has the model layer. Most of the credible foundation model labs are American or based in the US. The compute is American. The capital markets are American. NVIDIA is American. The defense market is American. The AI talent market is concentrated in the Bay Area and a small handful of other US hubs. Where the United States has the disadvantage is in industrial manufacturing of the actuator stack. The US has not made high precision actuators at scale for 30 years. Restoring that capability is an industrial policy question that the US is only beginning to address. Hyundai’s 26 billion dollar investment in US manufacturing is interesting precisely because Hyundai is closing a gap that the US has not closed itself.

Japan has the legacy industrial robotics base. Fanuc, Yaskawa, Kawasaki Heavy Industries. The traditional robot OEM business is concentrated here. The newer wave of physical AI has not yet flowed back into Japanese leadership in the way one might expect, but the country still ships an enormous share of global industrial robots. Toyota Research Institute has been doing serious robotics research for years. Honda has Asimo’s legacy and is rebuilding around it.

Korea has Hyundai and Samsung. Hyundai bought Boston Dynamics in 2021 and is now investing the kind of capital you would expect from a country trying to capture humanoid manufacturing at home. Samsung has substantial robotics R&D and a parallel push in semiconductors that supports the substrate.

Europe has the engineering culture and several niche players. 1X is technically Norwegian. Festo, KUKA which is owned by Chinese Midea, ABB which is Swiss Swedish, and a network of academic labs in Germany, Switzerland, and the Netherlands have the engineering depth. The challenge for Europe is the same challenge it has had in every category of recent AI. The capital does not flow at the scale required.

India is in a different and interesting position, which I want to walk through carefully because being from India, I keep vibrating on a spectrum of extreme pessimism to unrealistic optimism.

## India’s opportunity is not the universal robot

Let me be blunt about this.

India is not going to build the Physical Intelligence of robotics. The capital for that does not exist in India and is unlikely to materialize in the next few years. Krutrim tried to build a large language model and ran into the painful reality that you cannot out spend OpenAI and Anthropic with 100 million dollars when they have tens of billions. The same math applies to robotics foundation models. The all in cost of training a frontier robot foundation model is going to be measured in billions of dollars over the next five years, and most of that has to come from a small set of countries with enormous capital pools and aligned industrial policy. India is not one of those countries.

India is also unlikely to win the humanoid manufacturing race against China, at least not in the next decade. The supply chain advantage China has is structural and would take many years and many billions of dollars to replicate. Addverb is making a credible effort and has shipped to 150 facilities in India, the US, the Netherlands, and Singapore. But the unit economics of competing with Chinese humanoid makers at price points the Chinese can hit is brutal.

What India can do, and what I think the smart Indian operators are correctly positioning around, is play three different games at the same time.

#1 The first game is vertical specialization for the Indian and adjacent markets. India has unique workflows in agriculture, in construction, in healthcare, in informal commerce, in textile manufacturing, in mid sized industrial production, that are large enough to support local champions. Niqo Robotics for agriculture. CynLr for object intelligence in assembly. GreyOrange for warehouse operating systems. Addverb for industrial automation. Mowito for assembly. The pattern is the same. Pick a workflow. Solve it for India and then extend to South Asia, Southeast Asia, the Middle East, and parts of Africa where the unit economics resemble India’s. The TAM is not the universal robot. The TAM is the workflows of three billion people that the West and China are not focused on. That is a credible local champion play with global expansion as the second act.

#2 The second game is the data layer. India has the gig workforce. India has the labor cost structure. India has the cultural diversity inside the data that no other country can produce. If the next billion hours of robot training data is going to be generated by humans wearing cameras, India is one of the cheapest places on earth to do that work, and the variation per kilometer of Indian geography produces unique data that Western and Chinese settings cannot. Human Archive has raised eight point two million dollars to do this with Indian gig workers. Pronto has been piloting it inside Indian homes. Snabbit has confirmed it is exploring with Human Archive but has denied a home rollout. Mercor, Micro1, and other global data players have substantial India operations. Scale AI has a Bengaluru lab. The picture that emerges is that the Indian gig economy is rapidly becoming a real layer of the global physical AI substrate. The opportunity for Indian operators is to capture the high value portion of that data layer. Not the raw collection. The collection plus the validation plus the proprietary annotation tooling plus the embodiment specific data products that command higher prices.

#3 The third game is the niche foundation work and this one is the one with the biggest impact in my view. Not the universal foundation model. The Indian specific foundation work that becomes the underlay for vertical deployment in India and adjacent geographies. World action models that handle Indian construction sites, Indian kitchens, Indian small store fronts, Indian roads, Indian factories. The model that knows what a tea stall looks like and how a person navigates the chaos of an Indian street. The model that knows what the inside of an Indian factory floor looks like and how to pick a part from a bin that does not look like a Foxconn bin. The model is not generalist. It is regional. The regional model can then be a substrate for vertical deployments inside the region. The customer is Indian first, expanding to South Asia and Southeast Asia.

None of these three games is the universal robot. All three of them are good businesses. All three of them play to India’s actual advantages rather than India’s wishful thinking about being a foundation model power.

The single most important thing I want to say to Indian founders thinking about Physical AI is this. Do not try to compete with Physical Intelligence on the foundation model layer. Do not try to compete with Unitree on humanoid unit cost. Pick the layer where India’s structural advantages give you a real edge and compound there. The data layer and the vertical layer and the regional model layer all have room for billion dollar Indian companies. The foundation layer probably does not.

## The Indian examples are still early, but they matter

A few of the live Indian plays in this category deserve to be named, because the press has been writing about the headline ones without engaging with the structure.

Addverb Technologies, based in Noida, has been the most quietly ambitious of the Indian players. The company has shipped industrial robotics, autonomous mobile robots, and now a six foot humanoid that carries fifteen kilograms. They have a planned production of around one hundred humanoids over the next year for collaboration with five to six customers in solar, battery, and electronics manufacturing, plus hazardous environments including nuclear and chemical. They are global. They have deployed in 150 facilities across India, the US, the Netherlands, and Singapore. They are an example of an Indian company that has chosen verticals where India’s manufacturing customer base is real and adjacent regional buyers are accessible.

CynLr, based in Bengaluru, is doing something genuinely interesting. They have built an object intelligence platform for assembly that lets robots learn and adapt to new objects in real time without months of retraining. The company has raised 15.2 dollars from Pavestone Capital, Athera, Speciale Invest, and InfoEdge’s Redstart Labs. The belief is that the missing piece in vertical automation is not the model and not the robot, it is the layer that lets a single robot be reconfigured to handle new SKUs without retraining. If they are right, the layer compounds, because every customer adds to the platform.

Niqo Robotics, also Bengaluru, makes agricultural spraying and thinning robots. Founded in 2015 as Tartan Sense, rebranded in 2022. Series B funded. Fifty plus units operating in India and eleven in California, Arizona, and Georgia. The pattern is the right one. Start with the Indian customer base. Use Indian operating cost. Expand to adjacent geographies where the unit economics work, starting with the US where farmers will pay for proven ROI on labor saving.

GreyOrange, with headquarters in the US for commercial proximity but with deep R&D in Gurugram, has effectively become a fulfillment operating system rather than just a robotics company. The hardware has been commoditized. The software is the moat. This is one of the most mature Indian robotics businesses by revenue and by deployment count.

Mowito, working on automotive and electronics assembly with the team based out of Bengaluru with US operations, is an example of the painful early stage of a vertical robotics company that is doing the right thing but has not yet hit the inflection. They are paying for trust the way Coalition paid for trust in cyber. The next eighteen months will tell whether the business model compounds.

On the data side, the picture is more chaotic. Pronto, founded by Anjali Sardana in 2025, was being written about as a home services platform and is now also positioning as a real world data layer for physical AI, with Glade Brook Capital documenting in an investor memo that Pronto is piloting real world training data with leading physical AI labs. The workforce wears small outward facing cameras during select opt in jobs. The customer receives the footage afterward. The company has acknowledged the pilot publicly. Snabbit has confirmed it is exploring something with Human Archive but has denied any home rollout. Human Archive raised 8.2 million dollars in 2026 to put cameras on Indian gig workers. Mercor and Micro1 are running their own mobile applications where individuals can record data with their phones and get paid in dollars. A company called Magic Lead is collaborating on head and back camera setups. The Indian gig economy is in the process of becoming the cheapest large scale supplier of egocentric training data on earth.

I want to flag something important about the data economy that I have heard repeatedly from operators in this space. The market is shifting fast. Twelve months ago the buyers wanted volume and were happy with raw egocentric video. Today the buyers want quality, sensor fusion, motion capture, hand pose, head pose, full body pose, audio synchronization, and validated clip lengths of ten to fifteen minutes rather than two to three minutes. The price of low quality raw data is collapsing. The price of high quality multi sensor data is rising. The operators who built their business on the first phase are going to get squeezed out. The operators who can credibly produce the second phase data will keep raising and keep growing. The transition from phase one to phase two is happening right now. Some of the well funded Indian companies in this space were built for phase one. They will not survive phase two unless they pivot quickly.

There is a related operational reality that does not get enough attention. I was speaking to a friend Ashish Noel from IIT Madras (ex Humyn Labs) about this and he said something sad. The companies that are buying data from Indian operators are reporting quality issues that have pushed some of them to test alternative geographies, particularly Latin America and the Philippines, where operators are reportedly more responsive to research protocols and produce higher quality clips. India’s price advantage is real. India’s quality advantage is conditional on the operator. The Indian data layer is not automatically a winner. The Indian data operators who invest seriously in quality processes, in training their workforce on protocols, in building proper validation pipelines, will win and will expand. The ones who chase volume at the cost of quality will be replaced by operators in other low cost geographies inside two years.

## Could India build its own robot foundation model?

The naive answer is yes, because India has talent and ambition and the success or however you judge the progress of Krutrim is not a fatal precedent. The honest answer is, probably not, and chasing the question wastes capital that could compound in better places.

The foundation model bet, even at the regional level, requires three things India does not currently have at scale. It requires enormous capital, because the data, the compute, the talent, and the infrastructure to train a robot foundation model is going to cost on the order of a billion dollars at a credible level over the next five years. It requires a state coordinated industrial policy that funds the long arc, the way China is funding its humanoid push. It requires a domestic industrial buyer base for the model’s output, because foundation models compound on real deployment data and India’s domestic robotics demand is still small.

What India can do is a narrower version of the same idea. India can build the regional world model. A world model is a system that has learned how the world behaves and can predict what happens next given an action. A regional world model is one that is trained specifically on the variation of a region. An Indian regional world model would know how Indian streets, Indian kitchens, Indian factories, Indian construction sites, and Indian hospitals actually look. It would be a substrate that an Indian vertical robotics company could fine tune on top of, rather than starting from a Western or Chinese world model and dealing with the embodiment gap and the cultural gap.

The economics of a regional world model are very different from a generalist foundation model. The training data is more accessible. The compute is meaningful but not in the tens of billions range. The customer is closer at hand. The TAM is narrower but more legible. A few hundred million dollars of patient capital, plus academic partnerships at IIT Madras, IIIT Hyderabad, IIT Bombay, and a small set of others, plus deep ties to domestic vertical robotics companies, could produce a real Indian regional world model in three to five years. That is a credible bet. The full generalist play is probably not.

There is one more thing the Indian government could do that would change the math. Ashish made this point sharply when I spoke to him. India spends large amounts of money on academic research that does not flow toward applied robotics. A 500 hundred crore competitive research pool, deployed specifically on embodied AI work at the best Indian labs over a five year period, would meaningfully change the talent retention math. Indian robotics researchers currently leave for Stanford, DeepMind, and the US labs because the capital for the kind of work they want to do does not exist in India. Bringing back a few dozen of those researchers, with real capital and real autonomy, would be the most leveraged spend the Indian government could make in this category. The investment is small relative to what China is spending. The return on talent retention compounds for decades.

## The defense layer is its own physical AI story, and India should be paying attention

Defense is a major and underweighted part of the physical AI category, and because India in particular has a structural opportunity here that no Indian operator has yet captured at scale.

The US defense robotics build out is happening at industrial scale. Anduril secured a 20 billion dollar US Army contract in March 2026 for Lattice integration across the service’s command and control infrastructure. Anduril raised 4 billion dollars at a 60 billion dollar valuation in March 2026, led by Andreessen Horowitz and Thrive. The company expects to roughly double its revenue to 4.3 billion dollars in 2026. Their Arsenal one facility in Ohio will produce tens of thousands of autonomous systems annually, including drones, loitering munitions, electronic warfare systems, and autonomous underwater vehicles. The Roadrunner M counter drone interceptor has shipped over 350 million in orders. The Pulsar electronic warfare system fits in a backpack. The Bolt M loitering munition was ordered by the Marines at 600+ units.

Shield AI deployed Hivemind in February 2026 for the US Air Force Collaborative Combat Aircraft program. Saronic Technologies is building autonomous surface vessels. Helsing is doing the same in Europe. Skydio has consumer drones and a defense pivot. Each of these companies is a physical AI company in a different domain.

The pattern that matters for India is that defense is the one market where governments will pay premium prices for autonomous physical systems, where the cost of failure justifies high reliability investments, where the data has both intelligence value and training value, and where the strategic interest aligns with industrial policy. India spends approximately 76 billion dollars on defense annually. India is the world’s third largest defense buyer. India is increasingly trying to indigenize defense procurement under the Atmanirbhar Bharat policy and post Op Sindoor. India does not yet have an Anduril or a Shield AI. The opportunity is sitting there.

The catch is that defense procurement is slow, relationship driven, and politically loaded. The companies that win in this space tend to have founders who can navigate the Ministry of Defence as effectively as they can ship technology. Building an Indian Anduril requires founders who understand both domains. There are a small number of Indian operators capable of this work, including some who as unintuitive it sounds, have spent time at Indian SaaS companies and now have the technical depth and the operational seriousness to attempt it. There is currently more capital looking for defense plays in India than there are credible founders to absorb it.

A separate angle worth surfacing. Indian SaaS founders who have built and sold to enterprises now have a unique transferable skill set. They have navigated long sales cycles. They have built revenue from procurement heavy buyers. They have managed relationships with bureaucratic decision makers. Those skills are the exact skills needed to build a defense physical AI company in India. The technology is increasingly available. The defense buyer is increasingly receptive. The capital is increasingly waiting. What is missing is the founder bridge, and that bridge is being built right now by a handful of people. If you are an Indian operator who has done enterprise SaaS and is wondering what to do next, defense physical AI is a category worth taking very seriously.

## The companies that matter may not call themselves robotics companies

Some of the most consequential physical AI companies of the next decade will not call themselves robotics companies. They will call themselves vertical platforms, or operations companies, or services companies, that happen to use robots inside their stack.

This is not a small distinction. It changes how you evaluate them.

Travis Kalanick’s Atoms is a good example. Atoms, which absorbed CloudKitchens in March 2026, is positioned as a robotics and food technology company. The flagship product, Bowl Builder, is a food assembly machine developed by Lab37, the company’s food robotics division based in Pittsburgh, run by Eric Meyhofer, a former Carnegie Mellon robotics professor who also ran Uber’s self driving unit. The interesting thing is that Atoms is not selling robots to restaurants. It is operating restaurants. It is also acquiring Pronto, the autonomous mining and industrial vehicle company started by Anthony Levandowski, a former Uber colleague of Kalanick’s. The company that emerges will run kitchens, drive vehicles, and operate adjacent verticals all from the same physical AI substrate.

Note for clarity because I’m not a big fan of hyperlinking every name and sending people away from the core topic (they will do it anyway if they really want to). There are two companies named Pronto in this story. One is Anjali Sardana’s Indian home services platform that is also generating data for physical AI labs. The other is Levandowski’s American autonomous vehicle company that Kalanick is acquiring. They are unrelated. The naming is unfortunate. If you only remember one, remember that Indian Pronto is collecting data inside homes and American Pronto is doing autonomous vehicles for mining sites.

A different version of the same pattern is happening in agriculture. Niqo Robotics is selling agricultural spraying as a service in some segments rather than selling robots directly. The robot is the substrate and the service is the product.

A different version again is happening in commercial cleaning. Brain Corp powers autonomous floor cleaners that are owned and operated by janitorial service companies, not by Brain Corp directly. The robot is the substrate and again service is the product.

A different version is happening in restaurants. Sweetgreen’s Infinite Kitchen, Chipotle’s Autocado, and various other vertical robotic deployments are operated by the restaurant chain, not sold as standalone robotics. The robot is the substrate and yet again, the service is the product.

The pattern that emerges is that vertical physical AI does not always look like a robotics company. Sometimes it looks like a kitchen company that runs robots, or a janitorial company that uses robots, or a logistics company that operates robots. The economic value flows to whichever layer owns the customer relationship and the operations. The robot is the substrate. The customer relationship and the operations layer is the product.

For an evaluator, this means that you have to ask, who owns the customer in this category. The company that owns the customer captures the most value. If the customer is buying robots, the robotics company captures the value. If the customer is buying the service, the service company captures the value and the robotics company becomes a commoditized supplier. The same robot can be on either side of this line, depending on who structured the relationship.

For a founder, this means that the choice of business model is itself a strategic bet. Selling robots to industrial buyers is one model. Operating robots and selling the service is a different model. The unit economics are different. The capital requirements are different. The defensibility is different. Many of the most interesting physical AI companies will choose the operations model rather than the robot sale model, because the operations model captures more of the value and protects the moat against commoditization of the underlying hardware.

## What should a founder build?

If you are a founder reading this and you are trying to decide where in physical AI to play, the first question is not what you are excited about. The first question is what unfair advantage you actually have.

If you are a deep technical researcher with publication credentials in robotics or VLA architectures, the foundation model bet is open to you, but you should know that the capital required is enormous and the path runs through Silicon Valley or Beijing. If you are not willing to relocate and not willing to spend the next decade fundraising, the foundation model bet is probably not the right one.

If you have manufacturing experience, real production line experience, and access to component supply chains, the humanoid race is open to you. You will need a co founder with model capability. You will need to be in a region with a working supply chain. You will need patience for an arc that runs 5-10 years before commercial scale.

If you have deep domain knowledge in a specific industrial workflow, the vertical specialist bet is the most accessible. You have a customer who already pays someone to do the work you are replacing. You have a measurable ROI. You have a sales motion you understand. The downside is that the capital efficiency is lower than software, and the deployment cycle is brutal. You will need patient capital and you will need to compound through data, not just through customer count.

If you have operational experience running large workforces or services businesses, the operations layer is the underweighted opportunity. You build the operating company that uses robots inside. You own the customer relationship. You compound through operations not through technology. The technology becomes commoditized over time and you still own the moat.

If you have defense industry relationships and a strong technical co founder, the defense physical AI bet is the while not overlooked, definitely underserved opportunity right now, particularly outside the US. The capital is waiting and this is true even for India. The buyer is receptive. The technical stack is increasingly accessible. The Indian defense market alone is large enough to fund a multi billion dollar company. So is the Israeli, the UAE, and the South Korean market.

If you are early in your career and want to learn the category from inside, the data layer is the most accessible entry point. You build the operation that collects, validates, and structures the data that the foundation model labs need. The barrier to entry is lower than building a foundation model. The defensibility comes from the operational tooling you build around the data, not the data itself. The path can lead you into the model layer over time if your data becomes proprietary enough.

If you want to be a category investor rather than a founder, focus on the substrate. The data, the actuators, the simulation, the world models, the manufacturing infrastructure. These compound regardless of which model or which humanoid wins. You will not get the headline outcomes of betting on Figure or Physical Intelligence. You will get more consistent compounding with less correlated risk.

The wrong move, in my view, is to take a typical software venture playbook and apply it to physical AI. 3 year build, 15 million seed, 50 million Series A, expectation of revenue within 18 months. This playbook does not fit the category. The companies that try it will run out of capital before they reach the inflection. The companies that win will look more like patient capital plays than typical venture plays. Hyundai investing twenty six billion dollars in US manufacturing. SoftBank putting 1.4 billion into Skild. CapitalG and Bezos putting a billion plus into Physical Intelligence. The check sizes are larger and the time horizons are longer than typical venture comfort. This is what physical AI requires.

## What should a student do?

If you are a student or an early career engineer or designer trying to decide whether to spend the next decade on physical AI, here is my honest answer.

It is one of the few categories with the structural potential to compound across multiple decades. Software has commoditized faster than anyone expected. AI agents are eating SaaS faster than anyone expected. The frontier of value is moving toward the categories where the work is physical and the cost of action is high. That frontier is going to need every kind of skill. Robotics engineering, mechanical engineering, manufacturing engineering, simulation engineering, AI research, hardware design, sensor design, supply chain operations, sales to industrial buyers, regulatory work, safety engineering, deployment operations, customer success in the field, and the operational glue that holds a physical AI company together.

If you are an undergraduate, take robotics seriously. Take controls. Take signal processing. Take optimization. Take reinforcement learning. Take embedded systems. Take mechanical engineering courses even if you are a CS major. Build something physical. The advantage of working in this category is that the skill base is broader than software and the talent supply is narrower.

If you are doing a PhD in robotics or related AI fields, you have a stronger position than you probably realize. The foundation model labs and the humanoid builders are paying premium prices for PhD level talent. Sergey Levine, Pieter Abbeel, Chelsea Finn, Russ Tedrake and a small network of academic researchers have effectively become a talent pipeline that feeds the entire commercial sector. If you can credibly publish in this area, you have the option to either join a top lab or to start your own. Both are real options.

If you are mid career in software and wondering how to transition, the most credible path is through the operations or vertical specialist layer. Find a company that needs a customer success or operations leader for a robotics product and join. The robotics knowledge can be learned. The operations knowledge cannot. Companies will pay for operations talent that understands enterprise sales motions, customer onboarding, deployment cycles, and the unglamorous work of making real systems run reliably.

If you are wondering whether to build for India, build for India and design for global. The Indian customer base is the right primary market for many physical AI plays, but the second market should be a developed economy buyer who will validate the unit economics and pay premium prices. Niqo selling to California farmers after building for Indian farmers is the right model. The Indian customer is the entry point. The global customer is the proof of pricing power.

If you are wondering whether to take a job at a humanoid company, ask one question. What is the company’s path to a 100k units of production. If the answer is not credible, the company is going to run out of capital before it gets there. If the answer is credible, the company is one of the small number of legitimate humanoid plays and joining is a defensible bet. There are roughly 5-7 legitimate humanoid plays globally right now. The rest are research projects with humanoid wrappers and will not survive the next funding cycle.

If you are wondering whether to take a job at a foundation model lab in robotics, ask one question. How are they planning to get to 1 billion hours of training data. If the answer is, we are going to scale teleoperation, the answer is probably wrong because teleoperation does not scale to a billion hours. If the answer is, we have a data partnership with a deployment partner who is producing data at scale, the answer is more credible. If the answer is, we are going to use simulation and then close the sim to real gap, the answer is plausible but the timing is uncertain. The right answer is, we are using all three.

If you are wondering whether to start your own company in this space, the simplest test is, do you have a customer who has told you they will pay for the outcome you are building. If yes, start. If no, get one before you start. Vertical robotics in particular is brutal without an initial customer because the cost of building without a customer is enormous and the cost of building with a customer is bearable. Most vertical robotics companies that have failed in the last five years failed because they built without a customer.

## A framework for sorting any physical AI company into a box

I want to give you something you can use, which is a simple framework for taking any physical AI company you encounter and sorting it into a box that tells you what you are actually looking at.

The framework has five axes. Each axis is a question. Each question has a small number of answers. The combination of answers tells you what kind of company you are dealing with. I call it ‘The Five Axis Sort’.

1. The first axis is the layer. Which layer of the physical AI stack does the company live on. The choices are foundation model, humanoid platform, vertical robot, substrate, or operations. A company that lives across multiple layers is interesting and possibly risky. Most successful companies live primarily on one layer and have partnerships on adjacent ones.

2. The second axis is the data position. How does the company get its training data. The choices are owned deployment data, partnered deployment data, simulation, teleoperation, gig worker collection, or none of the above. A company with no real answer to this question is going to struggle to compound. A company with multiple data sources has the makings of a substrate position.

3. The third axis is the customer. Who pays the company. The choices are industrial buyer, consumer, defense, services operator, other businesses, or the company runs the operation directly and consumers pay for the service. The customer determines the unit economics, the sales cycle, and the regulatory exposure. A company that is unclear about its customer is probably unclear about its business model.

4. The fourth axis is the moat. What protects the company from the next entrant. The choices are proprietary data, regulatory or certification position, customer relationships, supply chain control, model capability, or brand. Most companies will claim multiple moats. The most defensible moat in this category, in my view, is proprietary data combined with deep customer relationships. Model capability is real but commoditizes faster than people expect. Brand is real but takes a decade to build.

5. The fifth axis is the time horizon. When does the company expect to be at scale. The choices are eighteen months, three years, five years, or ten years. The time horizon should match the layer. Foundation model labs and humanoid platforms have ten year horizons. Vertical robotics has three to five year horizons. Operations and substrate plays can compound on three year horizons but really compound on ten. A founder who is selling a humanoid bet with a three year horizon is selling a fantasy. A founder who is selling a vertical bet with a ten year horizon is selling something but it is not a venture investment.

Once you have placed a company on all five axes, the picture clears. A foundation model company with no real data partner is a research project. A humanoid company with no manufacturing plan is a prototype shop. A vertical robotics company with industrial customers and a credible data loop is a real business in early innings. A substrate company that captures actuator supply or simulation environments or training data at scale is potentially the best returns in the category if it executes.

I have run this framework against most of the companies I have looked at in this space and it has not failed me yet. It will not tell you which company wins. It will tell you which companies are actually playing the game.

If you are a founder, pick your layer. If you are an investor, pick your time horizon. If you are an operator, pick the substrate or the operations layer if you want to compound, or pick the vertical if you want to own a customer relationship. If you are a student, pick robotics and embodied AI even if it looks less glamorous than the latest LLM trend. The category will reward depth, patience, and operational seriousness over a decade in a way few other categories will.

The next AI company might look like a factory. It might look like a kitchen. It might look like an operating system that runs a hospital. It might look like an Indian fulfillment platform. It might look like a defense systems integrator. It will rarely look like what people imagine when they hear the words AI company today.

The rest, as always, takes care of itself.

## X Article Metadata

- Title: All you need to know about Physical AI
- Preview: A strange thing has started showing up in founder conversations.
People who could build software very fast are not as excited by software alone anymore. Not because software has become unimportant.

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
