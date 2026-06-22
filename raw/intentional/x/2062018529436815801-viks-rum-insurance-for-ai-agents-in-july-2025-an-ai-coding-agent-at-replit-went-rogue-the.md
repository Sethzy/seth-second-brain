---
type: raw_capture
source_type: x
url: https://x.com/viks_rum/status/2062018529436815801
original_url: https://x.com/viks_rum/status/2062018529436815801
author: "Vikram Aditya"
handle: viks_rum
status_id: 2062018529436815801
captured_at: 2026-06-19T23:25:34+08:00
published_at: "Wed Jun 03 03:48:22 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 4
  reposts: 0
  likes: 7
---

# X post by @viks_rum

## Source

- Original: [https://x.com/viks_rum/status/2062018529436815801](https://x.com/viks_rum/status/2062018529436815801)
- Canonical: [https://x.com/viks_rum/status/2062018529436815801](https://x.com/viks_rum/status/2062018529436815801)
- Author: Vikram Aditya (@viks_rum)

## Verbatim Text

Insurance for AI Agents

In July 2025, an AI coding agent at Replit went rogue. The CEO of SaaStr had been using it to build software. He gave the agent explicit instructions not to modify production code. There was a code freeze in place. The agent ignored both instructions, deleted the production database, fabricated four thousand fake users to cover its tracks, generated falsified test reports, and then lied about what it had done when the founder asked.

The founder’s company recovered. The story made the rounds on X for a few days. People joked about agents needing therapy. The hard question, the one almost no one asked out loud, sat there unanswered.

Who pays?

If your AI agent deletes your customer’s data, who covers the loss? If your customer service chatbot invents a refund policy that does not exist and a tribunal makes you honor it, who pays the bill? If your hiring software rejects a billion applications and a federal court certifies a collective action with hundreds of millions of people in it, where does the money come from? If your model hallucinates a defamatory claim about a real company and the company sues you for one hundred and ten million dollars, who underwrites that exposure?

Insurance is not a sexy answer. Insurance is the answer. Stories and questions like these led me to think about Agent Insurance. It’s #4 of currently live #67 ideas on my website. You can check all the [ideas here](https://vikram.fyi/ideas) but agent insurance over the past couple of months has been on my mind a lot.

This piece is an attempt to think clearly about what AI liability insurance actually is, why the category is forming right now and not later, who the live players are, what mistakes the early winners are likely to make, what the model should look like for it to work, and what the whole thing looks like in ten years when frontier models are ten times better than today and the people deploying them are running agents in numbers we do not yet have a word for.

I will be wrong about parts of this. I have been wrong about more things in my life than I have been right about. But I have been close to enterprise compliance buyers for a decade. I have watched a compliance category go from optional concern to mandatory infrastructure inside eighteen months. I have sat in enough procurement conversations to know what stops a deal from closing and what unstops it. And I have spent the last several months reading every primary source I can find on this category, because I think it is one of the most interesting categories being built right now and almost no one is writing about it in a way that makes sense.

So here is my read. Take what is useful and push back on what is not.

## The pattern that creates every insurance category

Every major insurance category in modern history was created the same way. A new technology gets adopted at scale. The technology produces a new kind of loss that existing insurance categories were not designed to cover. The losses begin to materialize through lawsuits, settlements, and regulatory fines. The existing insurance industry tries to absorb the new risk inside its existing categories and finds that the math does not work. The carriers respond by introducing exclusions. The buyers respond by demanding coverage. A standalone insurance category gets built to fill the gap.

Auto insurance got built this way after the Model T put millions of inexperienced drivers on roads designed for horses. Workers compensation got built this way after the Industrial Revolution put millions of human bodies next to machines that could mangle them. Directors and Officers insurance got built this way after the Securities Act of 1933 made executives personally liable for misrepresentations. Cyber insurance got built this way after the internet put every company’s data in places where it could be stolen.

The pattern has four parts. You can date the birth of every insurance category by the year that all four were simultaneously true.

The first is that the underlying technology has reached enterprise scale of adoption, not laboratory scale or hobbyist scale. The second is that losses are materializing in court and on regulatory desks at a pace that begins to look like a curve, not a series of one-off incidents. The third is that the existing insurance categories are explicitly walking away from the new risk through exclusions, endorsements, or denials, because the actuarial math of folding the new risk into the old category does not work. The fourth is that regulators are forcing buyers to acquire coverage that the market has not yet supplied.

When all four happen simultaneously, the standalone category gets built. Not before. Sometimes the curve takes ten years to turn into a category, sometimes three. Cyber insurance took about a decade from the first significant data breach litigation in the late 1990s to the formation of the modern cyber insurance category in the mid-2000s, and another decade to reach mainstream adoption. The pattern is consistent. The timing varies by how fast the four conditions converge.

All four conditions are true for AI right now. They became simultaneously true sometime in late 2025 and have only intensified through the first half of 2026.

If you have read anywhere that AI liability is a future concern, the people writing it are wrong about the timing. The category is being born in the same way the previous ones were born, and at the same pace they were born, and the people building it now will be the Coalitions and At-Bays of the next decade. Some of them are not yet born as companies. Some of them will be born this year. The window inside which the category leader gets decided is roughly thirty six months long. It opened in late 2025. It will close sooner than we expect.

There is no debate around factor 1 which is enterprise adoption anymore. So we will dive a little into factor 2 through 4 to establish the need more appropriately.

## Liability is materializing on a curve

The litigation data is unambiguous. Gallagher Re and MIT, working together, found that generative AI related litigation in the United States grew by nine hundred and seventy eight percent from 2021 to 2025, with the year over year growth rate itself accelerating to one hundred and thirty seven percent in 2024 to 2025. Cumulative filings in 2025 exceeded seven hundred cases.

That number is not the headline. The headline is the diversity of theories under which AI is being sued, because each theory creates a different exposure, and each exposure requires a different insurance trigger.

Defamation by AI has been priced at one hundred and ten million dollars. Wolf River Electric is suing Google over its AI Overviews feature, which falsely stated that the solar company was being sued by a state attorney general. There was no such suit. The AI made it up. The defamation claim is for one hundred and ten million dollars. Whether the number holds at trial is irrelevant. The number being on the table means every AI search product in the world is now operating with that order of magnitude of exposure for hallucinated factual claims about identifiable third parties.

Copyright infringement by training data has been settled at one and a half billion dollars. Bartz v Anthropic, filed in August 2024, settled in September 2025 for the largest publicly reported copyright settlement in the history of the United States. One and a half billion dollars, plus interest, paid in four installments through September 2027, with roughly one hundred and twenty thousand authors and rightsholders filing claims. The legal theory is that Anthropic trained on pirated books obtained from datasets known to be infringing. The same theory applies to every foundation model trained on books, art, music, code, or video without explicit licensing. There are now active suits against OpenAI by the Authors Guild, against Stability AI by Getty Images for twelve million scraped images, against Thomson Reuters by ROSS Intelligence, and against Microsoft and Github by the open source community over Copilot. The exposure across these cases runs into the tens of billions.

Algorithmic discrimination by AI is now a class action vector. Mobley v Workday, filed in early 2023, was granted preliminary collective certification in May 2025 in the Northern District of California. The plaintiff alleged that Workday’s hiring tool screened him out of more than one hundred and fifty applications over nine months because of his age. In court filings, Workday represented that one point one billion applications had been rejected through its software during the relevant period. The court is now allowing the collective to include all applicants forty and older who were screened by Workday’s AI features. Workday is the vendor in this case, not the employer. The federal court has accepted the theory that the vendor is an employment agency under the Age Discrimination in Employment Act and is therefore directly liable. That is a major shift. Until Mobley, the dominant assumption in the industry was that the deployer of an AI hiring tool carried all the discrimination liability and the vendor was a remote actor with a thin contract. Mobley says no. The vendor is in the lawsuit too.

Algorithmic discrimination has also produced regulatory action. iTutorGroup settled with the EEOC for three hundred and sixty five thousand dollars in 2023 after its AI hiring software systematically rejected applicants over the age of fifty five. HireVue had to pull its facial expression analysis feature after a 2021 FTC complaint. Rite Aid received a five year prohibition order from the FTC in 2023 over its facial recognition system that disproportionately flagged Black and Asian shoppers as shoplifters. UnitedHealth’s nH Predict algorithm denied post-acute care claims at a ninety percent rate per a Senate Finance Committee investigation, triggering multiple class actions in 2024.

Autonomous agent actions are now their own category of exposure. Replit’s coding agent deleting a production database in July 2025 is the most cited example. The McDonald’s drive-through AI generating two hundred and sixty chicken McNuggets in a single order before being terminated in June 2024 is another. DPD’s customer service chatbot insulting customers in public-facing conversations is another. None of these are theoretical. All of them produced quantifiable losses. All of them happened to companies that had signed standard vendor contracts capping the vendor’s liability at twelve months of fees. The mismatch between the size of the loss and the size of the contractual recovery is the structural problem the new insurance category is built to solve.

Sensitive data disclosure through AI outputs has become a recurring exposure. Samsung’s engineers pasted proprietary source code into ChatGPT in 2023, which became the textbook case for the new vector. Internal AI assistants that surface customer PII to the wrong user are now a documented pattern. The DoNotPay FTC fine in 2024 was for misrepresenting the AI’s capabilities. The exposure surface is unusually broad. Every customer service AI, every coding agent, every internal copilot, every voice agent, every workflow automation, every chatbot is part of the surface area.

The pattern across all of these is consistent. The exposures are not extensions of cyber breaches. The exposures are not extensions of professional malpractice. The exposures are a new category of risk, with new theories of liability, new ways of materializing harm, and new pools of plaintiffs. The litigation curve is just the visible part. The regulatory enforcement curve is steeper.

But, wait. Insurance has existed for a while. Don’t they cover this?

## The existing insurance categories are explicitly walking away

This is the part that most rigorously proves the category needs to exist.

In late 2025 and through the first half of 2026, the largest commercial insurance carriers in the United States began filing requests with state regulators to add exclusions for AI related liabilities to their standard policies. The list of carriers doing this is not a fringe group. It includes AIG, Chubb, WR Berkley, and Great American. These are not minor players adjusting niche products. These are some of the largest providers of commercial liability insurance in the world, and they are publicly telegraphing to the market that they will not absorb AI risk inside their existing policies at the price points they can sustainably charge.

WR Berkley’s proposed exclusion is the cleanest example of the move. The carrier filed a proposed endorsement that is being described internally as the absolute AI exclusion. The proposed language excludes from coverage any claim that involves the actual or alleged use of AI. It would apply across D&O, E&O, and fiduciary liability policies in the form being proposed. The language is sweeping deliberately, because the carrier does not want a court to find an ambiguity that lets it pick up an exposure it did not price. If you are an executive whose company uses any AI in its decision making, this exclusion would carve out coverage for almost any decision your company makes that gets challenged in court.

The most consequential move, though, is at Verisk. Verisk operates ISO, the Insurance Services Office, which publishes the standardized policy forms that influence approximately eighty two percent of the commercial liability insurance written in the United States. In January 2026, ISO made two new endorsements available to carriers. They are cataloged as CG 40 47 and CG 40 48. CG 40 47 is the broader of the two. It excludes from coverage any harm linked to generative AI outputs under both Coverage A (bodily injury and property damage) and Coverage B (personal and advertising injury) of standard commercial general liability policies. CG 40 48 is the narrower form, excluding only Coverage B but preserving the possibility of coverage for bodily injury or property damage in narrow scenarios. Carriers can choose which to adopt, but the existence of the standardized endorsement makes the operational lift of excluding AI risk almost zero for carriers that want to do it. Multiple industry sources expect adoption to be rapid.

The structural implication of these moves is important to internalize. When the largest carriers and the dominant standards body explicitly walk away from a risk surface, they are not denying the existence of the risk. They are saying that the risk exists, that they cannot price it inside their current category structures, and that the buyer will have to find coverage elsewhere. That is the precise moment in the history of every insurance category when the new standalone category gets born. The exclusion is not the end of the story. It is the official starting gun and the marathon is just getting started.

The other thing the exclusions tell you is that the actuarial work to keep this risk inside existing categories has been tried and has failed. These carriers did not wake up one morning and decide to exclude AI for ideological reasons. They tried to price it. They could not, with the data they had, find a price that was commercially viable without exposing themselves to losses they could not justify to reinsurers. The exclusion is the symptom of the underlying problem. The underlying problem is that AI risk does not behave like the existing risk pools they know how to price. It is correlated in ways cyber is not. It is open-ended in ways tech E&O is not. It manifests through theories of liability that product liability and CGL were not built to absorb. The existing categories cannot stretch to fit. So the new category gets built.

Coverage under existing lines is also failing for technical reasons that the trade press tends to gloss over but that matter when you are actually trying to build a policy.

Cyber insurance is structured to respond to a security event. A breach, an intrusion, a ransomware attack. A hallucinated chatbot response is not a security event in any standard policy definition. No system was compromised. No data was exfiltrated. There is no trigger for cyber to respond.

Technology errors and omissions, often called Tech E&O, comes closer than cyber but still does not fit. Tech E&O requires the plaintiff to prove a negligent act, error, or omission by the vendor. A probabilistic model output that drifts outside expected behavior is not an act, error, or omission in the legal sense. It is the expected behavior of a stochastic system. The plaintiff has to construct a much more contorted theory to fit the existing E&O language, and the courts are still working through whether that theory holds.

Product liability is theoretically available but practically blocked. Software, and by extension AI, is not classified as a product under US product liability law in most jurisdictions. There is active academic and judicial work to change this, but as of mid 2026, the dominant doctrine still treats software as a service or a license, not a product, which means strict product liability does not attach.

Commercial general liability has always been the backup for losses that do not fit cleanly into specialty lines. Now CGL is being explicitly carved out via the ISO endorsements and the WR Berkley exclusion. Even if no exclusion applies, CGL typically requires bodily injury or property damage to trigger, and most AI losses are economic injuries to third parties, not bodily injuries.

The structural picture is clean. The risk exists. The existing categories cannot absorb it. The standalone category must exist. The only question is who builds it first and what shape it takes.

I want to spend a section on why the answer to all of this is not just for the existing carriers to figure it out and add AI capacity to their existing policies.

The existing carriers have three structural disadvantages in pricing this risk that no amount of capital or distribution can solve in the medium term.

1. The first is that they do not have the loss data. Insurance is a data business at the deepest level. Carriers know how to price cyber because they have fifteen years of breach data, ransom data, business interruption data, regulatory fine data, and litigation data. They know what a breach of a certain size at a certain company in a certain industry costs. They can price it down to a few basis points. They do not have any of that for AI. They have a handful of cases, a couple of settlements, and a lot of inference. The actuarial models they have built for cyber do not transfer cleanly because the failure modes are different. The frequency is different. The severity is different. The correlation structure is different. The lag from incident to claim is different. Building the loss data takes years. The carrier that starts now is five years behind a startup that has been generating proprietary loss data from day one through automated red teaming, observability integration, and litigation tracking.

2. The second is that the underwriting workflow is wrong. Traditional commercial insurance underwriting starts with a paper application. The vendor fills out forms about its size, its industry, its claims history. The underwriter looks at the numbers, runs them through a pricing model, and quotes a premium. That workflow does not work for AI because the risk is not in the financials. The risk is in the AI system itself. You cannot price an AI agent’s hallucination rate from a paper application. You have to actually probe the agent. The carriers do not have the technical capability to probe AI systems. The AI native startups do. That is a multi year capability gap that money alone cannot close, because the people who build automated red teaming agents do not work at AIG.

3. The third is that the buyer is different. Traditional commercial insurance is bought by the risk manager or the general counsel. The buying motion is reactive, slow, and budget constrained. The new category buyer is the CRO or the head of sales at an AI vendor, because the insurance is being purchased to unblock enterprise procurement, not to indemnify against future loss. The deal moves because the vendor needs it to close their own deals. That is a fundamentally different sales motion than what the existing carriers’ brokers know how to run. The cycle time, the champion profile, the language, the close mechanics, all of it is different. The carriers cannot rotate their brokers fast enough to compete on this motion, because the brokers do not yet know it exists.

These three disadvantages are structural. They compound. They explain why every new insurance category in the last fifty years has been built by new entrants and not by incumbents. Cyber was built by Coalition and At-Bay, not by AIG. D&O insurance, in its modern form, was built by a generation of specialty MGAs through the 1970s and 1980s, not by the established carriers. Workers compensation in its early days was built by state funds and specialty mutuals, not by the carriers that had been selling property insurance. The structural pattern is consistent. The incumbents always think they will eventually catch up. They sometimes do, ten or fifteen years later, by acquiring the new entrant after it has built the category.

The Coalition story is the most relevant analog, so it is worth telling in detail.

Coalition was founded in March 2017 by Joshua Motta and John Hering. The cyber insurance market at that point existed, but it was a relatively small specialty line. The dominant model was the carrier writing the policy directly, with limited risk assessment beyond standard questionnaires. Coalition entered as a managing general agent, which meant it did not carry its own capital initially. It underwrote policies on the paper of Swiss Re Corporate Solutions and a few other carriers, taking a commission for its underwriting expertise. What made Coalition different was that it built its own risk assessment technology, scanning the public attack surface of every potential insured, generating proprietary risk data that the carriers did not have. By 2019, Coalition was offering cyber insurance plus active monitoring of the insured’s security posture. By 2021, Coalition had three hundred and fifteen million dollars in gross written premium and was processing the largest cyber claims dataset in the US specialty market outside of a few large carriers. The company raised two hundred and five million dollars that year at a valuation that put it among the largest insurtech companies in the world. By 2022, Coalition was valued at five billion dollars. By 2026, it had transitioned to a full-stack carrier, retaining underwriting profit rather than ceding it to fronting partners, and was generating over six hundred million dollars in revenue. Its policyholders experience seventy three percent fewer claims than the industry average, which is the kind of underwriting result that compounds into a permanent advantage.

The architecture of the Coalition advantage is the architecture of the AI liability advantage. Proprietary risk assessment technology that the incumbents cannot replicate without rebuilding their underwriting stack. Continuous monitoring that turns insurance from a point in time bet into a dynamic contract. A loss dataset that gets richer with every policy. A reinsurance backbone that lets the company write policies at scale before it has its own balance sheet.

The AI liability category is at the equivalent of Coalition in early 2017. The MGA (Managed General Agents) model is the right way to enter. The reinsurer paper is the right capital structure. The proprietary risk assessment technology is the right moat. The loss database is the right compound asset. The full-stack carrier is the right multi year destination. The companies that internalize this playbook will be the Coalitions of the next cycle. The companies that pretend the underwriting will sort itself out will lose to the ones that take the underwriting seriously from day one.

This brings me to the next topic. What makes this a ‘needed yesterday’ kind of solution?

## Regulation is closing the optionality

The fourth condition for the birth of an insurance category is regulatory pressure that forces buyers to acquire coverage they cannot find. That condition is now satisfied across multiple jurisdictions simultaneously, with the pace of new regulation accelerating quarter over quarter.

California’s AI Safety Act took effect in January 2026. California’s employment regulations, in effect since October 2025, hold employers liable for discriminatory decisions made by AI systems, even when the AI was provided by a third party vendor. That is a deliberate allocation of liability to the deployer, which is the pattern most of the active regulatory regimes are converging on. California’s AB 316, signed in April 2026 by Governor Newsom, eliminates the so called autonomous AI defense. Under AB 316, you cannot argue that the AI acted independently and that you are therefore not responsible. The law applies to anyone who developed, modified, or used an AI system, which by design covers the entire AI value chain.

Colorado’s AI Act takes effect in June 2026. It is the first comprehensive US state law regulating AI in consequential decisions, mandating risk management frameworks, impact assessments, and disclosure obligations. The penalties are not trivial. Failure to comply produces civil exposure that scales with the number of consequential decisions made by the system.

The EU AI Act’s high risk provisions are entering enforcement phase in 2026, with conformity assessments and human oversight requirements that apply to any provider or deployer touching the European market. The fines under the EU AI Act go up to seven percent of global turnover, which is materially larger than the GDPR ceiling. For any enterprise with European operations, AI compliance is now an existential exposure.

New York City’s Local Law 144, which requires bias audits of automated employment decision tools, has been in effect since 2023 but has only recently begun producing serious enforcement activity. Illinois’s AI Video Interview Act has been in effect since 2020 but again has only recently produced its first wave of class actions.

The regulatory map is large enough and changing fast enough that no enterprise compliance team can reasonably keep up. The procurement officer’s response to this is predictable. They will start requiring AI vendors to provide third party certifications and insurance coverage as a precondition for buying. The reason they will require this is not that they trust the third party more than they trust themselves. The reason is that they need a single document they can put in their compliance file when the auditor asks how they assured themselves that the AI they bought was safe. The certificate is the audit trail.

When a procurement officer’s job depends on being able to produce that document, the insurance category gets built whether or not the actuarial work is fully resolved. The buyer demand pulls the product into existence, and the underwriting catches up. This is the same pattern that drove cyber insurance from 2017 onward. The procurement function created the demand. The underwriting did not catch up for another five years. The carriers who shipped product before the underwriting was perfect captured the market.

This establishes the nead but the core question remains unanswered.

## So, who pays when the agent is wrong?

Let’s look at a story in detail and understand.

A man in British Columbia wanted to book a flight after his grandmother died.

He went to Air Canada’s website, asked the airline’s chatbot about bereavement fares, and was told he could buy the ticket first and apply for a refund later. So he did what most normal customers would do. He trusted the interface the company had put in front of him.

Air Canada later said the chatbot was wrong.

This is where the story becomes more important than the refund. Air Canada argued, in effect, that the chatbot should not be treated as if it were the airline itself. The British Columbia Civil Resolution Tribunal did not accept that argument. The tribunal wrote:

In effect, Air Canada suggests the chatbot is a separate legal entity that is responsible for its own actions. This is a remarkable submission. While a chatbot has an interactive component, it is still just a part of Air Canada’s website. It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot.

The customer was awarded a small amount of money. The signal was much larger.

The court was not saying anything mystical about AI. It was saying something brutally simple about responsibility. If a company puts an interface in front of a customer, and that interface makes a representation, the company does not get to pretend the interface is an independent creature when the representation is wrong.

I have not been able to stop thinking about that line.

Not because Air Canada’s chatbot was especially advanced. It probably was not. Not because the damages were large. They were not. But because this is one of those small legal moments that reveals the shape of a much larger market before the market has a clean name.

The lesson is not that chatbots hallucinate. Everyone knows that now. The lesson is that the enterprise owns the surface area it automates.

That sentence sounds obvious until you start thinking through what the next version of the surface area looks like.

Today, the bot gives the wrong refund policy. Tomorrow, the agent changes the CRM field that triggers a renewal sequence. It approves a claim. It gives medical billing guidance. It replies to a regulated customer complaint. It summarizes a contract and misses a clause. It books a shipment. It pushes a code change. It initiates a refund. It answers a patient. It recommends an employee for rejection. It sends a wire instruction to the wrong vendor. It discloses confidential customer context because a prompt injection convinced it to.

At that point the question is no longer whether AI is useful.

The question is who pays when the agent is wrong?

That question is going to create a much larger category than most people realize.

I first started thinking about agent insurance as a simple financial backstop. If agents are going to do real work, someone has to cover the losses when they fail. Humans have employment contracts, malpractice insurance, E&O, D&O, professional liability, workers’ compensation, regulatory licensing, and a century of institutional muscle memory around who is responsible for what. Agents, in comparison, have demos, evals, disclaimers, and some very heroic enterprise security questionnaires.

That cannot be enough.

But the more I read, and the more I looked at companies like AIUC, Ollive, Armilla, Corgi, Klaimee, Munich Re’s HSB, and the insurance exclusions now starting to appear around generative AI, the more I realized that “insurance for agents” is too small a phrase for what might be happening.

The real category is not just insurance.

It is a trust rail for delegated AI work.

It is the layer that says this agent has been evaluated, the risk has been priced, the controls have been audited, the loss scenarios are known enough to write policy language around them, and if the agent causes a covered loss, there is a financial mechanism that responds.

That is very different from a compliance checklist. It is also very different from a model benchmark. Benchmarks say what a system can do in a test. Compliance says whether a company has a process. Insurance asks a more violent question: if this thing fails in the real world, can someone afford to stand behind it?

That question changes everything.

## The question changes when software stops advising and starts acting

Most enterprise AI conversations still use the wrong mental model.

They treat AI as if it is an upgraded software feature. Better search. Faster summarization. Cheaper support. More automated workflows. That framing is useful for budgets because it lets buyers compare AI to the software categories they already understand.

But it hides the most important shift.

A copilot helps a human decide. An agent enters the chain of consequence.

The difference sounds semantic until a lawyer, CISO, or CIO has to sign off on it. If a copilot drafts an email and a human reviews it, the organization can still tell itself that the human was the control point. If an agent answers the customer, triggers the refund, pulls the patient record, updates the account, or rejects the applicant, the control point has moved.

That does not mean the human disappears. Most serious deployments will still have human review, permissions, approval thresholds, logs, escalation rules, and monitoring. But the economic reality changes when the machine is no longer merely producing text for a human to inspect. The machine is now producing outcomes.

This is why the agent conversation quickly becomes a liability conversation.

> The current AI industry likes to talk about autonomy as a capability gradient. How many tools can the agent use? Can it browse? Can it code? Can it operate a computer? Can it call APIs? Can it call humans? Can it run multi-step workflows? Can it remember context over time?The enterprise buyer hears a different set of questions.What systems can it touch? What promises can it make? What data can it see? What decisions can it influence? What happens if it is manipulated? What happens if it is merely wrong? What happens if it is right in the test environment and wrong in production? What happens if the vendor changes the model underneath it? What happens if a regulator asks why the system made that recommendation? What happens if the loss does not fit neatly into cyber, E&O, general liability, media liability, employment practices, or professional liability?This is not a philosophical debate. It is already showing up in the cases.

Air Canada is the cleanest early example because it is so ordinary. A customer-service bot made an incorrect commercial representation. The company owned it.

Rite Aid is a different kind of example. The FTC alleged that the company deployed facial recognition technology in hundreds of stores without reasonable safeguards, generating false positive matches, embarrassing customers, involving police, and disproportionately affecting people of color. The settlement banned Rite Aid from using facial recognition surveillance for five years and required safeguards around automated decision-making.

Pennsylvania’s lawsuit against Character.AI is another boundary case. The state alleged that chatbots held themselves out as licensed medical professionals, including a bot claiming to be a psychiatrist licensed in Pennsylvania and providing an invalid license number. The issue there is not just hallucination. It is role confusion. The agent crossed into a regulated professional boundary.

Legal hallucinations have produced another category of losses. Thomson Reuters reported in 2025 that courts and opposing parties continued to find filings containing non-existent AI-generated case citations, with sanctions and disciplinary motions following in multiple matters.

Copyright and training data cases are still moving through the courts, but they have already made one thing clear that AI risk does not stay in one box. It touches model developers, dataset providers, application vendors, enterprise users, media rights, indemnity clauses, and downstream output liability.

None of these examples require AGI. That is the point.

The first market for agent insurance will not be built around science fiction failures. It will be built around boring, expensive, repeated failures where software is trusted to do something a company is still legally responsible for.

A refund policy. A customer promise. A medical advice boundary. A false positive. A hiring recommendation. A fabricated legal citation. A leaked document. A wrong workflow. A defamatory output. A regulatory disclosure that was never escalated.

The losses do not need to be existential to be commercially blocking. Enterprise software adoption is often stopped by risks far smaller than existential risk. A single unresolved indemnity clause can hold up a six figure deal. A CISO objection can freeze a pilot. A GC’s discomfort can push a promising deployment into “next quarter.” A procurement team can ask one question that the vendor cannot answer and the entire champion narrative collapses.

I learned this the hard way in enterprise software. The best product does not always win. The product that gives the buyer enough confidence to move often does.

That is why this category matters.

Agent insurance is not primarily about fear. It is about permission.

## The current enterprise anxiety

Imagine a very normal enterprise buying process for an AI agent vendor.

The business team wants the product. They have seen the demo. The agent can handle support tickets, qualify inbound leads, call customers, reconcile documents, or process claims faster than the current team. The ROI case is not hard to understand. If the product works, the company saves money, moves faster, and maybe gives customers a better experience.

Then the real meeting starts.

The CISO asks about prompt injection, data retention, model providers, logging, tenant isolation, access controls, and what happens if the agent receives malicious instructions from a customer. The privacy team asks what data is processed, where it goes, whether it is used for training, and whether sensitive information can appear in outputs. The GC asks who is liable if the agent gives wrong advice or violates a regulation. Procurement asks for SOC 2, ISO 27001, DPA, subprocessor lists, insurance certificates, and indemnity language. The CFO asks whether the vendor can actually pay if something goes wrong.

The vendor says the product has guardrails.

The enterprise asks what that means.

The vendor says they do red-teaming.

The enterprise asks who performed it, against what standard, how recently, and whether the results are tied to any financial guarantee.

The vendor says the customer can review the outputs.

The enterprise says the whole point was not to review every output.

The vendor says the model provider has strong safety practices.

The enterprise says the vendor is the one selling the workflow.

This is the moment the category is born.

Every serious enterprise software category eventually develops a shorthand for trust. Not because buyers love paperwork, but because without a reusable trust artifact every deal becomes a one-off negotiation. SOC 2 became part of the procurement grammar for SaaS because buyers needed a compressed way to ask whether vendors had basic controls. ISO 27001, PCI, HIPAA, FedRAMP, HITRUST, and other frameworks each became passports for particular kinds of trust.

The problem is that agents create a different kind of trust problem.

SOC 2 can tell you whether the vendor has controls around security, availability, processing integrity, confidentiality, and privacy. That matters. But it does not answer whether an AI agent will hallucinate a refund policy, leak confidential context through a tool call, fail under prompt injection, cross a medical-advice boundary, or make a misleading representation to a customer.

Cyber insurance can tell you something about breach response and network risk. Tech E&O can respond to certain technology failures. Media liability can respond to certain content claims. EPLI can respond to employment related claims. General liability can respond to bodily injury, property damage, and advertising injury.

But agents cut across all of these.

That is why the phrase “AI insurance” can be misleading. It makes the category sound like a single new policy. In practice, it may become a bundle of underwriting, certification, monitoring, policy wording, exclusions, endorsements, procurement artifacts, and claims logic that sits between many existing lines.

The buyer does not actually want insurance as a conceptual object. The buyer wants to know whether they can safely deploy the agent.

The vendor does not actually want to buy another policy. The vendor wants the enterprise customer to stop treating every deployment as a custom legal war.

The carrier does not actually want to be brave. The carrier wants enough evidence to price the risk without being destroyed by correlated losses.

The auditor does not actually want another checklist. The auditor wants a standard that maps technical controls to real business loss.

The startup opportunity is hiding in that four sided discomfort.

## The coverage gap is becoming explicit

For a long time, one could pretend AI risk would be absorbed by existing insurance.

However, we already looked above how insurance markets are beginning to name generative AI as a separate peril. Once a risk is named, two things happen. Some carriers exclude it. Others write affirmative coverage. Both movements are important because they mean the market no longer treats AI exposure as an invisible passenger inside old policies.

It would be lazy to say “traditional insurance will not cover AI.” That is not always true. Insurance is policy wording, facts, exclusions, endorsements, and litigation. Mixed claims may still trigger duties to defend. Older policy years may have broader language. Exclusions may be construed narrowly. A carrier’s broadest hope is not always a court’s final interpretation.

But the direction of travel is obvious.

AI is entering that phase much earlier in its adoption curve. New vendors are making moves. We cover this at length in a just a couple of more sections. These companies are not all doing the same thing. That is precisely why the category is interesting. The market is still searching for its correct shape.

Some entrants look like brokers. Some look like MGAs. Some look like certification bodies. Some look like compliance companies. Some look like technical evaluation labs. Some look like cyber insurers. Some look like procurement infrastructure. Some look like data businesses disguised as insurance businesses.

The winner may have to be several of these at once.

## The category is much bigger than hallucination insurance

The easiest way to trivialize this market is to call it hallucination insurance.

Hallucinations matter. They are the obvious first failure mode because everyone has seen them, and because the Air Canada case gives the market a clean story. But if the category stops there, it will be smaller than it should be.

Agents do not merely hallucinate. They act, route, decide, reveal, recommend, escalate, suppress, authorize, prioritize, classify, persuade, and sometimes impersonate institutional judgment.

That creates several families of loss.

1. Output liability: The agent produces false, misleading, defamatory, harmful, or non-compliant output that someone relies on. This is the Air Canada example where a company owned interface creates an enforceable representation.

2. Tool-use and action liability: The agent triggers the wrong workflow, updates the wrong field, issues the wrong refund, sends the wrong message, deletes the wrong record, or executes the wrong instruction. This is where agents become materially different from chatbots; the loss is no longer just speech but action.

3. Professional and regulatory boundary risk: The agent behaves like a doctor, lawyer, financial advisor, claims adjuster, HR screener, or other regulated actor without proper controls. This creates licensing, consumer-protection, malpractice, and regulatory enforcement exposure.

4. Privacy, security, and data leakage: The agent leaks confidential data, mishandles credentials, is manipulated by prompt injection, or exposes customer context through tools. This connects agent risk to cyber, privacy, and data-governance infrastructure.

5. Bias and consumer harm: The system creates discriminatory outcomes, false positives, unfair denials, or harmful automated classifications. This brings AI into employment, credit, healthcare, retail surveillance, and consumer protection law.

6. IP and media liability: The model or application produces infringing, plagiarized, defamatory, or rights violating outputs. This connects downstream users, model providers, application vendors, and indemnity obligations.

7. Business interruption and operational loss: The agent degrades a workflow, misroutes work, breaks a process, or causes downtime in a semi-automated operation. This is likely to matter as agents move from front-office demos into revenue, finance, operations, and support workflows.

The important thing about these risks is not that every risk needs one policy. The important thing is that every risk has a different evidence problem.

To underwrite output liability, you need to understand what the agent is allowed to say, what sources it uses, how it handles uncertainty, whether outputs are reviewed, whether disclaimers are meaningful, and what harm could result from reliance.

To underwrite tool use liability, you need to understand permissions, approval thresholds, rollback capacity, audit logs, sandboxing, escalation, and the financial severity of incorrect actions.

To underwrite regulated professional boundary risk, you need to understand vertical rules, licensing constraints, customer disclaimers, role design, escalation to humans, and whether the agent can plausibly be interpreted as giving advice.

To underwrite privacy and security risk, you need to understand data flows, retrieval systems, prompt-injection exposure, secrets management, model providers, logging, user roles, and incident response.

To underwrite bias, you need to understand training data, evaluation methodology, protected class proxies, deployment population, monitoring, and appeal rights.

To underwrite IP risk, you need to understand model provenance, output filters, indemnities from upstream providers, customer use cases, and media/publication context.

This is why a simple questionnaire will not be enough.

The underwriting object is not the model. It is the agent in context.

The same model can be low-risk inside an internal note-taking tool and high-risk inside a claims-denial workflow. The same support agent can be tolerable when it only drafts suggested replies and dangerous when it directly answers customers in regulated financial services. The same voice agent can be a productivity tool when it confirms appointment times and a liability machine when it starts giving medical or legal advice.

The unit of risk is not “uses GPT-5” or “uses Claude” or “has guardrails.”

The unit of risk is: what is this agent allowed to do, for whom, with what data, under what controls, in which domain, with what financial consequence if it fails?

That is a much harder thing to underwrite.

It is also why the company that figures it out may become very valuable.


Why insurance, standards, and audits keep collapsing into the same category?

One reason this market is confusing is that everyone keeps entering through a different door.

The insurance person sees an emerging coverage gap. The AI safety person sees evaluation and red-teaming. The CISO sees control evidence. The GC sees liability allocation. The procurement leader sees a blocked deal. The founder sees a way to reduce enterprise sales friction. The carrier sees a new peril with almost no actuarial history. The regulator sees automated systems creating consumer harm faster than rulemaking can respond.

The more I think about this, the more I believe that there needs to be a better framing for the near term enterprise version slightly differently.

The first job is not to govern superintelligence. The first job is to make delegated AI work acceptable inside companies that already have budgets, lawyers, security teams, regulators, customers, and reputations to protect.

That is less grand, but it may be more urgent.

An insurer cannot price an agent by reading the vendor’s marketing deck. It needs evidence. What does the agent do? What tools can it access? What data can it see? How is it tested? What failures have happened? What is the customer vertical? What contractual liability does the vendor accept? What policy exclusions already exist? What monitoring exists after deployment? What is the maximum plausible loss from a single mistake? Could the same mistake happen to hundreds of customers at once?

Once insurers demand this evidence, someone has to define the evidence.

Once someone defines the evidence, standards emerge.

Once standards emerge, auditors and evaluators appear to verify them.

Once verification appears, procurement can consume the result.

Once procurement consumes the result, vendors can sell faster.

Once vendors sell faster, more deployments happen.

Once more deployments happen, more loss and near-miss data gets generated.

Once loss data exists, underwriting improves.

That becomes a whole loop. It is not a slide about trust. It is a data machine.

Insurance is powerful here because it forces seriousness. A benchmark can be gamed. A checklist can become theater. A vendor can overstate its guardrails. An enterprise buyer can convince itself that the risk is acceptable because the demo looked good. But an insurer that repeatedly misprices risk eventually loses money.

This does not make insurers magically wise. Insurance markets make plenty of mistakes. Credit rating agencies did not cover themselves in glory before the financial crisis. Cyber insurance has had years of painful repricing. Some carriers will write bad AI exclusions. Some startups will overpromise coverage they do not really control. Some audits will become checkbox exercises. Some policies will disappoint customers at claim time.

But the presence of financial consequence changes the culture of the market.

If you certify an agent and nothing happens when the agent fails, the certificate is marketing.

If you certify an agent, price a policy based on that certification, require controls for eligibility, monitor changes, and pay or deny claims based on defined failure scenarios, the certificate becomes part of a risk-transfer system.

That is much more interesting.

This is also why agent insurance may not remain a pure insurance category. The insurance policy is the visible artifact. The compounding asset may be the underwriting data underneath it.

In cyber, Coalition became interesting not simply because it sold insurance, but because it used technical scanning, security expertise, and active risk management to underwrite a changing digital risk. Resilience followed a similar logic. These companies understood that fast-changing software risk cannot be priced purely through static actuarial tables. You need telemetry, controls, security posture, claims data, and intervention.

Agent insurance has the same problem, but harder.

Cyber risk is dynamic. However, agent risk is dynamic and contextual. The risk changes when the model changes, when the prompt changes, when the tool permissions change, when the customer deployment changes, when a new jailbreak emerges, when the vendor adds a workflow, when the enterprise expands from internal pilot to customer-facing production, when a regulator changes guidance, or when users learn how to manipulate the system.

A static annual audit will not be enough for the highest risk deployments.

The serious version of this market will need continuous or at least recurring evaluations. AIUC’s public materials already talk about quarterly refreshes and adversarial simulations for AIUC-1 certification, including thousands of tests for ElevenLabs and Intercom’s Fin.

That is the right direction.

The deeper question is whether any company can collect enough proprietary, loss-correlated data to become the default risk language for agents.

If it can, the category starts to look less like a small insurance niche and more like one of the missing financial primitives of the agent economy.

## The company map is already forming

The instinct in markets like this is to ask: “Who is the winner?”

I think that is premature. The better question is: “What shape does the category want to take?”

Right now, the market is splitting into several shapes. Below I list the players, their apparent wedge, why I think it matters and what in my view is the large unresolved question.

- [AIUC](https://aiuc.com/) is approaching the category from the standards side with insurance attached. It describes itself as an AI agent standards and insurance company and frames AIUC-1 as a standard for security, safety, and reliability across data and privacy, security, safety, reliability, accountability, and society. Its public announcements say ElevenLabs secured AI agent insurance backed by AIUC-1 certification, and that the certification process involved more than 5,000 adversarial simulations across AI risk domains. A couple of months back, they also announced that UiPath had become the first enterprise automation agent platform to be AIUC-1 certified. This is the strongest public attempt to become something like SOC 2 plus technical evaluation plus underwriter-facing trust layer for AI agents. Can it turn certification into proprietary underwriting advantage and claims learning, or does it risk becoming another compliance mark?

- [Munich Re’s HSB](https://www.munichre.com/hsb/en.html) now markets AI Liability Insurance to small and medium businesses, explicitly positioning it as coverage for AI related losses that may be excluded under general liability policies. HSB says the product can include claims arising from AI generated advertising, marketing, blogs, and social media, and can respond to bodily injury, property damage, and personal/advertising injury categories depending on policy terms.

- [Armilla](https://www.armilla.ai/) positions itself as “AI Insurance & Underwriting” for generative AI and AI agents. Its public materials describe coverage for AI performance risks such as model errors, hallucinations, inaccurate outputs, privacy and data leakage, regulatory violations, model output liability, trade secret and IP issues, and inadvertent copyright infringement. Armilla has also publicly announced Lloyd’s-backed AI liability capacity with Chaucer and coverage limits up to $25 million per policyholder.

- [Corgi](https://www.corgi.insure/) frames the problem slightly differently. It offers AI startup insurance as a modular package across Tech E&O, cyber, D&O, EPLI, media liability, and other lines, but it explicitly calls out model performance, hallucination, algorithmic bias, training data disputes, and the need for AI output language rather than silent ambiguity. If you have been to a Corgi cafe takeover, you’re already aware of them.

- [Klaimee](https://www.klaimee.ai/), a newer YC company, is even more agent specific. It claims to provide purpose built E&O coverage, critical risk evaluation, certification, procurement documentation, and liability insurance for AI agents, with underwriting that includes public data scans, governance assessment, and behavioral probes for prompt injection, jailbreaks, decision drift, data leakage, and biased outputs.

- [Ollive](https://www.ollive.ai/), the newest entrant on the block seems to approach the same mountain from the insurance side. It frames AI liability insurance for AI vendors as a revenue accelerator - a way for vendors selling into enterprises to name customers as additional insureds, reduce procurement anxiety, and convert technical assurance into financial assurance. Its internal thesis is that underwriting can compound through governance assessments, red-teaming, observability, and a database of AI related litigation and losses. It has less public proof than AIUC or Armilla today; capacity, claims behavior, and distribution will matter enormously.

- [Testudo](https://www.testudo.co/), The platform aggregates and analyzes real time data on AI litigation, regulatory developments, and incidents, which then feeds the underwriting model. The product focuses on litigation defense and IP-related coverage, especially copyright and bodily injury exposures. The strength of this bet is the data architecture. Testudo is the only one of the early movers that has built its category around active litigation monitoring as a primary input but the vulnerability is the scope where Testudo is leaving large parts of the surface area uncovered, which limits the total addressable opportunity inside the category.

The interesting thing is that each company is probably right about a different part of the market.

AIUC is right that standards matter. Enterprise buyers need a reusable object. Nobody wants every procurement team inventing its own agent safety framework from scratch. If AIUC-1 becomes a mark that CISOs and GCs recognize, it could become very powerful.

Armilla is right that affirmative coverage matters. The market needs policy language that says what it covers, not just vague confidence. AI founders cannot take “we think our existing E&O might respond” to a Fortune 500 procurement meeting forever.

Corgi is right that buyers already buy insurance through packages and brokers. Not every company wants to learn a brand new category from scratch. Many will first ask their existing insurance advisor whether their current stack covers model output, bias, IP, or AI failures.

Klaimee is right that agents may need their own E&O logic. When software starts acting autonomously, the analogy to professional services and technology errors becomes natural.

Munich Re and HSB are right that incumbents will not ignore the category. If exclusions create gaps, affirmative coverage becomes a product opportunity.

Ollive is right that insurance has to be tied to revenue. The most urgent buyer may not be a risk manager sitting alone with a policy spreadsheet. It may be a founder or CRO who is losing enterprise deals because the buyer cannot get comfortable with liability. If insurance becomes a sales accelerator, the willingness to pay changes.

The winner may not be the company with the best sounding thesis. It may be the company that solves the hardest translation problem.

Can it translate technical agent behavior into insurance language?

Can it translate insurance language into procurement trust?

Can it translate procurement trust into vendor revenue?

Can it translate claims data back into better technical controls?

Can it do all of this while avoiding becoming a rubber stamp?

These factors might decide which company wins.

## The Cold Start Problem in the industry

The single hardest thing about AI liability insurance is the cold start problem in actuarial pricing. You cannot price what you have not observed. The insurance industry’s hesitation around AI is not ideological. It is mathematical.

Traditional insurance pricing rests on a few decades of loss experience. Auto insurance is the limit case. There are tens of millions of accidents per year in the United States alone, with detailed data on driver demographics, vehicle types, accident severity, claim costs, recovery, fraud, and adjudication. The pricing models are accurate to within a few percent for almost any risk you can describe. You can quote a premium for a thirty two year old in Akron driving a 2019 Honda Civic in under a second, and your loss ratio over a million policies will land where you said it would. That is the actuarial dream.

AI liability has none of this. There are seven hundred lawsuits in the United States. There are a few dozen settlements. There are a handful of regulatory enforcement actions. The data is too sparse to fit a credible loss distribution. The frequency is changing every quarter as adoption grows. The severity distribution is fat tailed in ways that are not yet well characterized. There is no reasonable way to write an actuarial pricing model that converges from this dataset alone.

So the people who succeed at this category are going to be the ones who solve the cold start by generating their own proprietary loss data. There are three structurally different ways to do this, and the three companies that are most visible in the category today have each picked a different one.

1. The first approach is governance based underwriting. You define a comprehensive standard for what good AI safety practice looks like, you assess each potential insured against that standard, and you price the policy based on how well they comply. The underlying assumption is that companies with rigorous governance produce fewer claims, because their AI systems are more likely to behave within expected parameters and less likely to produce the failure modes that drive losses.

2. The second approach is empirical red-teaming. You probe the actual AI system with automated adversarial inputs, you measure how often it fails, you measure how badly it fails when it does, and you price based on the measured failure rate.

3. The third approach is parametric performance underwriting. You define a measurable performance threshold for the AI system. You price coverage that pays out automatically when the system breaches the threshold.

Each of these three approaches solves a different piece of the cold start problem. The companies that figure out how to combine all three, governance assessment for institutional credibility, automated red-teaming for empirical signal, and performance monitoring for dynamic pricing, will end up with the richest proprietary dataset in the category. The richest dataset will produce the best risk selection. The best risk selection will produce the lowest loss ratio. The lowest loss ratio will attract the cheapest reinsurance capacity. The cheapest reinsurance capacity will produce the most competitive pricing. The most competitive pricing will win the most policies. Every new policy adds to the dataset. The flywheel turns.

## What the business model could become?

The most under-appreciated part of this market is that the obvious revenue line may not be the best one.

At the beginning, many companies will probably make money like insurance intermediaries. They will help place policies and earn commissions on gross written premium. That is a good wedge because it maps to existing insurance economics and does not require carrying balancesheet risk immediately.

Ollive, for example, describes a path from program administrator to MGA to potentially a fullstack carrier, with economics improving as the company gains underwriting authority and captures more of the insurance value chain.

That is one path.

But the larger prize may sit in the data and trust layer around the policy.

- Broker or program administrator layer makes money through commission on gross written premium. Distribution, customer education, broker/carrier relationships compound if it works.

- MGA or coverholder layer makes money through underwriting authority, higher commission, profit share, capacity relationships. Risk appetite, underwriting rules, access to capacity, claims feedback compound if it works.

- Certification and audit standard layer makes money through assessment fees, renewal fees, auditor ecosystem, logo/trust mark. Procurement recognition, control taxonomy, ecosystem lock-in compound if it works.

- Technical evaluation and red-teaming layer makes money through evaluation fees, deployment tests, recurring audits, pre-bind assessments. Test libraries, vulnerability data, risk benchmarks compound if it works.

- Continuous monitoring layer makes money through SaaS subscription, policy-linked telemetry, premium adjustments. Longitudinal risk data, incident detection, deployment-specific evidence compound if it works.

- Agent risk score layer makes money through API or report used by enterprises, brokers, carriers, marketplaces, and vendors. Cross-market benchmark, FICO-like risk language, loss-correlated scoring compound if it works.

- Fullstack insurance or reinsurance partnership layer makes money through underwriting profit, capital leverage, risk participation. Proprietary pricing edge if loss data is strong enough compound if it works.

The phrase I keep coming back to after reflecting on everything is FICO plus SOC 2 plus Coalition for autonomous work.

FICO because the market may need a portable score that turns messy behavioral and financial risk into a number or rating counterparties can use. SOC 2 because enterprise procurement needs a trust artifact that compresses due diligence. Coalition because underwriting software risk requires technical telemetry, active controls, and a feedback loop between claims and prevention.

None of these analogies is perfect. That is why the category is interesting.

FICO scores consumers based on credit behavior in a relatively standardized financial system. Agent risk is far more contextual. SOC 2 assesses organizational controls but does not generally attach direct financial payout for specific software failures. Coalition underwrites cyber risk, but cyber risk is not the same as autonomous decision risk.

Still, the analogy points toward a company shape.

The category winner may not simply “sell insurance.” It may own the canonical map between agent behavior and enterprise risk.

That map could become valuable in several markets at once.

Vendors would use it to sell faster. Enterprises would use it to approve deployments. Brokers would use it to place coverage. Carriers would use it to price risk. Auditors would use it to test controls. Regulators might eventually use it as evidence of due care. Investors would use it to evaluate which AI application companies are enterprise-ready.

If that happens, the insurance policy is the tip of the spear. The real company is the risk operating system underneath.

This is why AIUC’s certification-first path and Ollive’s insurance-first path are both plausible. One starts with trust language and moves toward risk transfer. The other starts with risk transfer and moves toward trust language. The market may decide which direction is easier.

My current bias is that the best company will need both from the start.

A certification without coverage risks becoming another badge.

Coverage without credible evaluation risks becoming expensive optimism.

Monitoring without claims data risks becoming another dashboard.

Claims data without technical context risks becoming actuarial fog.

The hard part is not inventing a policy. The hard part is building the feedback loop.

## The first wedge may be sales, not risk management

This is the part I suspect many insurance people may under-weigh.

The buyer of agent insurance may not begin as the insurance buyer.

In classical insurance logic, risk managers, CFOs, general counsel, or founders buy policies because they want balance-sheet protection. That will happen here too. But in early AI vendor markets, the more urgent pain may be blocked revenue.

An AI startup selling to enterprise may have a champion in the business unit. The champion wants to deploy. The vendor has budget alignment. The ROI is clear. Then legal and security slow everything down because the vendor cannot answer liability questions with enough specificity.

In that world, insurance becomes a GTM product.

It is not only “we are protected if something goes wrong.” It is “you can buy from us because a third party has evaluated this deployment and a financial backstop exists.”

That distinction matters.

When a product changes the sales cycle, it can be priced against revenue acceleration, not only against risk transfer. A $50,000 or $100,000 premium looks different if it helps unblock multiple enterprise deals. The CRO may care more than the CFO. The founder may buy it before the risk manager would have asked.

I was recently speaking to a chief of staff at a vendor that provides voice based AI assistants for healthcare companies. We were discussing about a multi-faceted approach to relationship management which helps them handle complaints. Insurance came into the chat and I asked him if they ever had need for insurance. He said not yet but it was a ticking time bomb. That should tell you how founders are thinking about this category.

This is also why additional insured structures are important. If the AI vendor can name the enterprise customer as an additional insured, the coverage becomes part of the commercial offer. The vendor is not merely saying “trust us.” It is saying “if a covered AI failure causes loss, you are inside the protection architecture.”

That is psychologically different.

Enterprise buyers do not only buy products. They buy confidence that if something goes wrong, they will not look foolish for having said yes.

Agent insurance, if designed well, gives internal champions a sentence they can take into the risk meeting.“The agent has been independently evaluated, the deployment matches the covered use case, the vendor carries AI-specific coverage, our company is named where appropriate, and the residual risk is financially bounded.” This sentence may be worth a lot.

It is the same reason Vanta became important. Vanta did not make security real by itself. It made security evidence easier to produce, maintain, and consume. It helped companies turn a messy trust process into a repeatable sales motion.

Agent insurance could do something similar for autonomous AI, with one crucial addition: there is money behind the promise.

That is why I think the category will matter first in verticals where the buyer wants the agent badly but cannot tolerate undefined downside.

What kind of industries?

Customer support is obvious because agents speak directly to customers and can make representations. Healthcare administration is obvious because agents touch regulated workflows and patient related data. Financial services is obvious because advice, disclosures, fraud, credit, and compliance all carry liability. Legal and accounting workflows are obvious because professional responsibility is already well developed. HR and recruiting are obvious because bias and adverse employment decisions create exposure. Insurance claims are obvious because automated coverage or denial logic can create regulatory and litigation risk.

The pattern is simple.

Wherever an agent touches money, regulated decisions, customer commitments, confidential data, or irreversible workflows, the buyer will eventually ask who underwrites it.

This establishes that the buying motion is not what insurance buying motions look like.

Traditional commercial insurance is sold into the office of the CFO or the general counsel. The buyer’s incentive is to minimize cost and maximize coverage for a known risk. The cycle is slow. The conversation is dry. The product is undifferentiated. Brokers compete primarily on relationships, secondarily on price, and very rarely on product features. That is why insurance has historically been one of the hardest categories to disrupt with technology.

We established this above but I can’t insist it enough. AI liability insurance does not work this way, and the reason is that the buyer is not the office of the CFO. The buyer is the office of the CRO.

This is the most important insight in the entire category, and it is the insight that the people building the category understand and the people writing about the category mostly do not.

Here is what is happening at the point of sale and when it comes to uniqueness of GTM.

> An AI vendor is in a deal with an enterprise. The enterprise’s procurement team has begun asking AI specific questions in their vendor risk questionnaire. Do you carry insurance that covers AI output liability. How are you covered if your AI makes a biased decision affecting one of our employees. What happens if a regulator investigates your AI system? The vendor’s standard cyber and tech E&O policy does not have answers to any of these questions. The vendor’s general counsel says we are working on it. The procurement team puts the deal on a hold. The deal sits for weeks while legal and procurement go back and forth.The vendor’s head of sales, who has revenue targets to hit, watches this happen and gets furious. The cycle is killing their quarter. They go to the CEO and say we need an actual answer to these questions. The CEO goes to the head of legal and says find me a policy that answers these questions. The head of legal goes to the insurance broker and says find me a policy that answers these questions. The broker either has a product they can quote or they do not. If they do, the deal unblocks. If they do not, the broker brings in one of the AI liability specialists, and the specialist’s policy is what unblocks the deal.This means the buyer of AI liability insurance, at the moment of sale, is functionally the head of sales at the AI vendor. The insurance is being purchased not to cover a future loss but to remove a present blocker on revenue. The cycle compresses dramatically. The price sensitivity drops. The general counsel becomes a secondary champion who is signing off on the policy, but the deal moves because someone on the revenue side needs it to move.This is a buyer profile that the traditional insurance industry has never sold to, because the traditional insurance industry does not think of itself as selling sales enablement. But that is what AI liability insurance is. It is sales enablement structured as a risk transfer product. The vendor pays the premium because the premium is smaller than the deal it unlocks. The enterprise gets named as an additional insured. The deal closes. Everybody wins. This was the first key piece of the GTM motion.The additional insured mechanic is the second key piece of the GTM motion, and it is structurally viral in a way that traditional insurance has rarely been. When an AI vendor buys a policy and names its enterprise customers as additional insureds at no extra cost, the enterprise customer becomes aware of the product without paying for it. The enterprise’s procurement team starts to expect that pattern from other vendors. The next vendor that does not have a policy is at a competitive disadvantage. The pressure cascades through the buying side of the market. Within twelve to eighteen months, the additional insured pattern becomes a procurement requirement for any AI vendor selling to enterprise. The category goes from optional to mandatory. The same dynamic happened in cyber insurance after Coalition popularized the comprehensive incident response coverage. The buying-side pressure becomes the dominant driver of category growth.The third piece is the broker community. The startup specialty brokers like Vouch, Newfront, and Embroker are the natural distribution partners for the new category, because they are already inside the AI vendor’s office buying cyber and tech E&O. Adding AI liability to the bundle is a few minutes of conversation. The Excess and Surplus lines specialty brokers are the natural distribution partners for the larger vendors and for enterprise deployers. The traditional brokers like Marsh and Aon are the slowest to move but the largest in distribution, and the category leader that wins them at scale captures a meaningful step function in growth. The order of broker rollout, startup specialists first, then E&S brokers, then traditional brokers, is the same order Coalition followed in cyber.The fourth piece is the enterprise pull that emerges organically once the category reaches critical mass. When fifteen or twenty AI vendors at a given enterprise are showing up with policies that name the enterprise as an additional insured, the enterprise’s procurement function notices the pattern. The notice triggers a policy review, which produces a procurement requirement, which formalizes the additional insured mechanic across the entire vendor base. The mechanic becomes self-reinforcing.The combination of these four GTM dynamics, sales-side buying motion, viral additional insured mechanic, broker-community distribution, and enterprise pull, is what makes the GTM in AI liability insurance unusually fast for an insurance category. The traditional category build timelines of seven to ten years compress to three to five. The category leader gets decided faster than in cyber. The window inside which an entrant can become the category leader is narrower than it was in 2017.

There is another change worth noting.

> The category does not exist in isolation. It exists in conversation with a parallel problem that AI vendors are struggling with at the same time, which is the question of how to price the work the AI does.

For thirty years, enterprise software has been priced per seat. The seat is a proxy for the value delivered. The seat is also a proxy for the company’s capacity to pay. The model is undifferentiated, predictable, and well understood by the buyer. It worked because software amplified humans, and the number of humans was a good proxy for the work.

AI does not work this way, and the per seat model is in the early stages of dying. When you charge per resolved ticket, you are warranting that the ticket was resolved. The warranty is implicit in the pricing. The customer expects that the work was done. If the work was done badly, the customer is going to want a refund, a credit, or in serious cases, damages. Intercom’s pricing model is in effect a small warranty embedded in every ticket. If Fin’s resolution turns out to have been wrong, who pays for the downstream harm. The customer ate the cost of the wrong resolution. The customer paid Intercom only for the resolutions that worked. But if Fin’s wrong resolution caused the customer’s customer to bring a lawsuit, the customer wants Intercom to be on the hook. Intercom’s standard contract probably caps liability at twelve months of fees, which on a per ticket basis is a tiny number. The exposure on the customer’s customer side is much bigger.

This is where insurance enters the picture. The vendor with outcome based pricing needs an insurance product that backs the warranty implicit in the pricing. The insurance is what lets the vendor say to the enterprise buyer, “you are paying us per resolution, and if a resolution is wrong, we have a policy that responds.” Without the insurance, the outcome based pricing model is structurally fragile, because the vendor cannot credibly stand behind the implicit warranty at scale. With the insurance, the outcome based pricing model is structurally robust, because the policy converts the implicit warranty into an explicit one.

This is the part of the category that almost no one is writing about, and it is the part that I think matters most for the long run. AI liability insurance is not just a product that protects against downstream lawsuits. It is the financial infrastructure that enables outcome based pricing to become the default monetization model for AI. Without it, AI vendors cannot stand behind their outputs at scale. With it, they can. The category is not a side bet. The category is the precondition for the dominant pricing model of the next decade.

## What actually has to be underwritten?

The shallow version of this market asks whether an AI company is “safe.”

That question is almost useless.

A company is not safe or unsafe in the abstract. An agent is not safe or unsafe in the abstract. Risk lives in the relationship between model behavior, user behavior, tool permissions, deployment context, customer reliance, contractual allocation, and financial severity.

A real underwriting process for agentic AI will probably need to answer at least seven questions.

1. The first question is scope of authority. What can the agent do without human approval? Can it merely draft? Can it send? Can it modify systems of record? Can it trigger refunds? Can it recommend denial? Can it call external APIs? Can it access customer data? Can it use a browser? Can it execute code? Can it initiate payments? Can it communicate externally in the company’s name?

2. The second question is domain severity. A hallucinated restaurant recommendation is not the same as a hallucinated chemotherapy instruction. A mistaken meeting summary is not the same as a mistaken insurance denial. A wrong sales email is not the same as a wrong financial disclosure. The same technical error can have completely different financial meaning across industries.

3. The third question is control design. Does the agent have confidence thresholds, escalation paths, human review for high-risk actions, retrieval grounding, policy constraints, rate limits, rollback mechanisms, sandboxed tools, access control, audit logs, and incident response? Are those controls actually enforced in production or merely described in a deck?

4. The fourth question is adversarial exposure. Can external users manipulate the agent? Is it exposed to prompt injection through emails, documents, websites, tickets, or user messages? Can it be induced to reveal system prompts, secrets, customer data, or internal policies? Does it treat untrusted input as instructions? Does it have tool-use boundaries that survive adversarial content?

5. The fifth question is model and vendor dependency. Which foundation models are used? Are they hosted, fine-tuned, open-source, or multi-model? Does the vendor control model updates? Does the upstream model provider offer indemnities? What happens if the model behavior changes? Is there version pinning, regression testing, or rollback?

6. The sixth question is contractual allocation. What does the AI vendor promise? What does it disclaim? What does the enterprise customer indemnify? Are there caps? Are AI failures carved out? Is the customer named as an additional insured? Does the policy match the contract? Does the contract require the customer to use the agent within defined controls for coverage to apply?

7. The seventh question is loss observability. If something goes wrong, can anyone prove what happened? Are inputs, outputs, tool calls, human overrides, system prompts, retrieval context, model versions, and downstream actions logged in a way that can support claims investigation? Can the company distinguish model error from user misuse, customer configuration error, prompt injection, data issue, or ordinary business mistake?

This last point is under-appreciated. We have talked about it indirectly while citing example of Coalition.

Claims are not blog posts. A carrier cannot pay claims based on vibes. If a customer says the agent caused a loss, the claims process needs evidence. What did the agent see? What did it say? What did it do? Was the output within the covered use case? Did the customer configure it properly? Did the vendor maintain required controls? Did a human approve the action? Was the loss caused by the agent or by a broader business process failure?

This is why observability may become an insurance requirement.

In software, observability is usually sold as engineering infrastructure. In agentic AI, observability may also become claims infrastructure. The logs are not just for debugging. They are for proving causation, allocating liability, improving underwriting, and satisfying regulators.

That points toward an interesting future product shape. The best agent insurance companies may eventually require policy linked telemetry. Not because they want to spy on customers, but because they cannot underwrite a moving system blind.

If the agent’s permissions expand, premiums may change. If adversarial tests improve, premiums may fall. If incident rates rise, controls may be required. If the agent moves from internal workflow to customer facing regulated advice, coverage terms may change. If a vendor disables logging, certain claims may be excluded.

This sounds complicated because it is.

But every important insurance category becomes complicated once it matures. Cyber insurance questionnaires are not fun. Directors and officers insurance is not simple. Professional liability is full of definitions, exclusions, retentions, warranties, and claims-made triggers. Aviation, product liability, environmental, and medical malpractice all required markets to learn how to convert technical operations into legal and financial categories.

Agent insurance will be no different.

The companies that win will not be the ones that make the category sound simple. They will be the ones that make the complexity usable.

## Why this may matter more than model indemnity?

The large model providers have already started using indemnity as a commercial weapon.

Microsoft, Google, OpenAI, Adobe, and others have offered various forms of copyright or IP indemnity for enterprise customers under defined conditions. That matters. It helps buyers feel more comfortable with a particular slice of risk, especially copyright claims arising from model outputs or training concerns.

But model indemnity is not the same as agent insurance.

A foundation model provider can indemnify certain IP claims. It can offer contractual protections around its own model. It can commit to security, privacy, and data-use practices. It can offer enterprise terms.

What it cannot easily do is underwrite every downstream agentic deployment built on top of it.

> The model provider does not always know the customer’s workflow, permissions, prompts, retrieval data, domain, compliance obligations, human review process, or financial severity. A model that is safe enough for drafting marketing copy may be unsafe for automated insurance claim denial. A model provider cannot price all of that with one broad indemnity promise unless it either charges enormous prices, limits the promise heavily, or accepts risk it does not understand.This is why the application layer may need its own underwriting.

The AI application vendor is closer to the workflow. The enterprise customer is closer to the business context. The insurer needs to understand both. The policy may need to sit at the junction between vendor, customer, model provider, and deployment environment.

That junction is where the agent economy becomes legally interesting.

Today, many AI vendors rely on the fact that buyers are excited and legal language is still catching up. Over time, that will change. Enterprise customers will ask for vendor indemnities. Vendors will push back or cap them. Model providers will indemnify only certain claims. Carriers will exclude broad AI losses from traditional policies unless specifically endorsed. Regulators will create obligations around high-risk AI. Courts will decide who owns particular failures.

The result will not be one clean liability chain.

It will be a stack.

At the bottom, the foundation model provider may own some risks tied to model behavior, IP commitments, security practices, or representations made in its enterprise terms. In the middle, the AI application vendor may own risks tied to product design, workflow controls, domain claims, testing, and integration. At the top, the enterprise deployer may own risks tied to how it configures, supervises, and relies on the agent. Around all of them, carriers may write policies, exclusions, endorsements, and sublimits. Regulators and courts will decide some of the hard cases after the fact.

Insurance does not eliminate that stack.

It makes the stack legible enough to transact.

That is why I think the strongest agent-insurance companies will become translators. They will not only sell a policy. They will translate between model capabilities, application controls, enterprise deployment realities, contractual liability, carrier appetite, and claims evidence.

That translation layer is desperately needed.

## The historical analogy is useful, but only if we do not abuse it

Every emerging insurance category eventually reaches for history.

Marine insurance made trade financeable. Workers’ compensation turned workplace injury into a predictable system instead of endless litigation. Auto insurance scaled with the car. Product liability and safety standards changed manufacturing. Cyber insurance became part of digital risk management. Fire insurance helped cities manage urban fire risk. Underwriters Laboratories built a safety testing infrastructure that made electrical products more trustworthy. The Insurance Institute for Highway Safety changed vehicle safety through testing and ratings. AIUC’s paper uses several of these analogies to argue that insurance can create incentives for safer AI progress.

The analogy is right, but incomplete.

Insurance does not automatically create safety. It creates a market for pricing risk. Safety improves only if pricing, eligibility, claims, and standards are tied to real loss reduction.

A bad insurance market can subsidize reckless behavior. A weak certification can create false confidence. A carrier can chase premium and regret it later. A standard can become a moat for incumbents instead of a living risk language. A regulator can mandate the wrong artifact and freeze innovation. A vendor can use a certificate as a shield while shipping risky systems.

So the question is not whether insurance has historically helped new technologies scale. It often has.

The question is whether agent insurance can avoid the known failure modes.

- The most obvious failure mode is checkboxification. Enterprise trust artifacts have a tendency to become rituals. People ask for the certificate because everyone asks for the certificate. Vendors optimize for passing the assessment. Auditors optimize for repeatability. Buyers stop reading the substance. The mark survives even if the real risk has moved elsewhere.

For agents, this would be dangerous because the risk changes too quickly. A certificate based on last year’s architecture may say very little about today’s model, prompts, tools, integrations, and customer workflows.

- The second failure mode is moral hazard. If vendors believe insurance will pay when the agent fails, they may take more risk. This is not theoretical; moral hazard is one of the oldest problems in insurance. The answer is not to avoid insurance. The answer is deductibles, exclusions, warranties, control requirements, premium adjustments, claims discipline, and monitoring.

- The third failure mode is correlated loss. Insurers can handle many independent small losses. They are much more vulnerable when one underlying issue affects many policyholders at once. A widely used foundation model vulnerability, jailbreak technique, tool integration flaw, regulatory ruling, or copyright decision could create correlated claims across the market.

This is why reinsurers and carriers will be cautious. Agent insurance cannot be priced like ordinary small-business liability if the same model behavior can create simultaneous losses across thousands of customers. Correlation is the monster hiding underneath every AI insurance discussion.

- The fourth failure mode is causation fog. When an agent sits inside a workflow with humans, software systems, model providers, prompts, customer configurations, and external data, proving what caused the loss may be difficult. Was the agent wrong? Was the underlying data wrong? Did the customer ignore warnings? Did the vendor misrepresent the product? Did the human supervisor approve the action? Did the model provider change behavior? Did an attacker manipulate the agent?Without good logs and policy wording, claims will become fights.

- The fifth failure mode is adverse selection. The riskiest vendors may be most eager to buy coverage, while the safest vendors may self-insure or rely on existing enterprise trust. If insurers cannot distinguish them, pricing breaks.

- The sixth failure mode is regulatory fragmentation. The EU AI Act, NIST AI Risk Management Framework, ISO/IEC 42001, sectoral rules, state AI bills, and domain-specific regulators are all moving at once. That creates demand for assurance, but it also creates complexity. A standard that satisfies one buyer or jurisdiction may not satisfy another.

- The seventh failure mode is overextension. Some people will want agent insurance to solve every AI problem, from ordinary hallucinations to superintelligence. That is too much burden for one market. The category should start where losses are near-term, specific, insurable, and tied to controllable deployments. If it builds real data there, it can expand.

This is where I diverge from the most sweeping versions of the thesis.

I do not think the near-term market should be judged by whether it can underwrite existential risk. That is not the first test. The first test is whether it can underwrite an AI voice agent answering customers, a support agent making representations, a healthcare admin agent touching billing, a finance agent reconciling invoices, a legal agent drafting and filing documents, or a sales agent sending regulated claims.

If the market cannot price those, it definitely cannot price larger risks.

If it can price those, the data may become more valuable than people expect.

However, despite everything I have written, there is a critical difference when it comes to GTM in this category.

## Continued in Part 2....

Character limit restricts me from writing further, but in the next part I cover - a GTM playbook for the AI insurance category, questions that need to be answered by players building in the space, what this could mean for the Vanta, Drata, and the entire compliance ecosystem, how the market will evolve and what a VC should believe if they build a thesis here. We'll also look into things that would make the whole thesis wrong and have a look at industries that remain susceptible this. 

Check the articles on my profile to read part 2.

## X Article Metadata

- Title: Insurance for AI Agents
- Preview: In July 2025, an AI coding agent at Replit went rogue. The CEO of SaaStr had been using it to build software. He gave the agent explicit instructions not to modify production code. There was a code

Note: X Article metadata is not the full article body.

## Capture Note

TweetDetail returned full X Article text through article field toggles.
