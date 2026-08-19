---
type: raw_capture
source_type: pasted
title: "OpenAI SDR Technical Acumen Interview Pack — Migration Snapshot"
url: "file:/Users/sethlim/Documents/openai-interview-prep/wiki/domains/OpenAI-SDR-technical-acumen-interview-pack.md"
collected_at: 2026-07-23T05:20:00Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
evidence_role: internal-synthesis-seed
---

# OpenAI SDR Technical Acumen Interview Pack — Migration Snapshot

> Origin: /Users/sethlim/Documents/openai-interview-prep/wiki/domains/OpenAI-SDR-technical-acumen-interview-pack.md
> Collected: 2026-07-23
> Evidence note: This is an internal compiled interview-prep document, preserved verbatim as the migration seed. It is not a primary source; durable factual claims in the OpenAI wiki should cite official captures.

---
type: domain
title: "OpenAI SDR Technical Acumen Interview Pack"
created: 2026-07-20
updated: 2026-07-21
address: c-000039
tags:
  - openai-interview-prep
  - strategic-bdr-apac
  - technical-acumen
  - technical-fluency
  - canonical-answers
status: canonical
maturity: active
related:
  - "[[OpenAI-SDR-sales-acumen-interview-pack]]"
  - "[[OpenAI-SDR-comprehensive-answer-expansion-bank]]"
  - "[[OpenAI-SDR-recruiter-screen-learnings-and-interview-strategy-2026-07-11]]"
  - "[[OpenAI-SDR-hiring-leader-interview-debrief-2026-07-17]]"
sources:
  - "[[OpenAI-recruiter-screen-Seth-2026-07-08]]"
  - "[[OpenAI-SDR-recruiter-screen-learnings-and-interview-strategy-2026-07-11]]"
  - "[[OpenAI-SDR-hiring-leader-interview-debrief-2026-07-17]]"
  - "[[OpenAI-SDR-comprehensive-answer-expansion-bank]]"
subdomain_of: "OpenAI Strategic BDR APAC interview prep"
page_count: 0
---

# OpenAI SDR Technical Acumen Interview Pack

## Purpose

This is the canonical execution pack for Phase 3B, which the recruiter described as a separate 30-minute Technical Fluency interview.

It has one job: show that Seth can earn a technical buyer's respect while helping a business executive understand why the decision matters commercially.

This is not a Solutions Architect examination and it is not the Sales Acumen pack. The expected altitude is a technically credible Strategic BDR who can:

- explain a difficult idea simply;
- diagnose the customer's workflow before recommending a product;
- make fit and non-fit calls;
- handle existing competitors without becoming tribal;
- connect technology to measurable business value;
- identify risk and the next proof step; and
- know when to bring in a technical partner.

> [!important] Recruiter-derived pass question
> Can Seth make a technical buyer respect his fluency while making a business executive understand why the decision matters commercially?

## How To Answer Live

Use this sequence:

1. **Answer the noun first.** Define the concept or make the recommendation immediately.
2. **Use one clear explanation or accurate metaphor.** Use a metaphor only when it clarifies the mechanism.
3. **Give one workflow example.** Show what a user is trying to accomplish.
4. **Name fit and non-fit.** Technical judgment is more persuasive than product enthusiasm.
5. **Land the business consequence.** Revenue, time, capacity, quality, risk, adoption, or customer experience.
6. **Name the control or next proof step.** Evals, a bounded pilot, human approval, or technical validation.
7. **Stop.** The first answer should usually be 20–45 seconds. Let the interviewer pull for depth.

### The plain-language rule

Prefer the clearest available explanation. When a metaphor genuinely helps, it should have three parts:

`familiar object → technical mechanism → where the metaphor breaks`

Example:

> An LLM is like a very well-read junior analyst: capable across many tasks, but still dependent on good context, clear instructions, and review when the stakes are high.

Do not force or stack metaphors. Use one clear mechanism, one workflow, and one business consequence.

## Rapid Question Map

The twelve highest-probability questions are:

1. Explain an LLM simply.
2. Explain RAG simply.
3. What is an agent?
4. What are evals?
5. How do you reduce hallucinations?
6. What is Codex?
7. Codex, ChatGPT Workspace Agent, or API?
8. Prompting, retrieval, tools, or fine-tuning?
9. Agent or deterministic automation?
10. How do you select the right OpenAI surface?
11. Why would a customer choose OpenAI if they already use a competitor?
12. How do you translate technology into business value?

---

## Part I — Highest-Probability Answers

### 1. Explain an LLM to a nontechnical executive

**Recommended answer — 30–45 seconds:**

> The simplest metaphor is a very well-read junior analyst. An LLM has studied enormous amounts of language, code, and other patterns, and it generates an answer by predicting the next small piece of information that best fits the task and context.
>
> Like that junior analyst, it can summarize, compare, draft, classify, and work through problems remarkably well. But it does not automatically know which company document is current, whether it has enough evidence, or when a confident-sounding answer is wrong.
>
> That is why the enterprise product is bigger than the model. You give it the right approved context, permissioned tools, clear instructions, evaluations, and human review where the stakes are high. The business value is faster knowledge work and greater employee capacity, with controls around quality and risk.

**If pushed technically:**

> Underneath that metaphor, it is a neural network trained to predict tokens, which are small units of text or data. The model is the intelligence layer; the surrounding context, tools, permissions, evals, and review process turn it into a useful enterprise system.

### 2. Explain RAG simply. When would you use it?

**Short answer — about 20 seconds:**

> RAG gives a model access to knowledge it was not trained on. Before answering, the system finds relevant information from the company's own data and adds it to the model's context. It is especially useful for private or changing knowledge, although you still need permissions, source quality, citations, and evals because retrieval can be wrong.

**Recommended answer — 35–45 seconds:**

> RAG stands for retrieval-augmented generation. The simplest way I think about it is that a model can only work with what it learned during training and the context you give it.
>
> RAG improves that context. Before the model answers, the system searches the company's own knowledge—documents, policies, account notes, or product manuals—retrieves the most relevant pieces, and adds them to the prompt.
>
> That makes it useful for private or changing knowledge the model was never trained on. But retrieval can still surface the wrong, stale, or unauthorized source, so an enterprise system also needs permissions, freshness, citations, and evals.
>
> The business value is that employees can get answers based on the company's actual knowledge rather than relying only on generic model memory.

**Raw-source basis:** Condensed from captured explanations by [Khairallah AL-Awady](https://x.com/eng_khairallah1/status/2069341916798369801), [Avid](https://x.com/Av1dlive/status/2057142081018315116), and [Tobi Lütke](https://x.com/tobi/status/1935533422589399127). This is a source-faithful synthesis, not a verbatim quotation.

**Next proof step:** Test retrieval on representative questions and score source selection, citation quality, answer correctness, and permission behavior.

### 3. What is an AI agent, and how is it different from a chatbot?

> The cleanest distinction is that a chatbot waits for a prompt, while an agent works toward a goal. Technically, an agent is a model using tools in a loop based on instructions.
>
> It decides what to do, takes an action, inspects the result, and continues until the task is complete or it reaches a stop condition.
>
> For example, a support chatbot might explain the refund policy. An agent could retrieve the policy, check the customer's account and payment record, draft the response, and route the refund to a manager for approval.
>
> The business shift is from attention to delegation—the system can complete more of the workflow. But because it can act in real systems, the risk also changes. That makes narrow permissions, logs, evals, stopping rules, and approval gates essential.

**Reference definitions:**

- **Tool:** An approved capability the model can request, such as searching documents, looking up an account, running a calculation, or updating a ticket. The surrounding application executes the request under defined permissions and returns the result to the model.
- **Loop:** The repeated cycle in which the model reviews the current state, chooses a next step, uses a tool, inspects what happened, and decides whether to continue. A reliable loop has both a success condition and a stopping rule, such as escalation to a person or a hard attempt limit.

**Raw-source basis:** Condensed from captured explanations by [Rohit](https://x.com/rohit4verse/status/2009663737469542875), [Sydney Runkle](https://x.com/sydneyrunkle/status/2062217190724579673), [Anatoli Kopadze](https://x.com/AnatoliKopadze/status/2068328135611822149), and [Ollo Brains](https://x.com/ollobrains/status/2062451606197825614). This is a source-faithful synthesis, not a verbatim quotation.

### 4. What are evals, and why should a business care?

> Evals are repeatable tests that define what good looks like for an AI system. You start with representative scenarios from the real workflow, score the system against explicit criteria, and rerun those tests whenever the system changes.
>
> For a support agent, the scenarios might include normal tickets, policy exceptions, missing information, and cases that must escalate. You could test objective behavior—whether it retrieved the correct source, used the right tool, and followed the required process—as well as judgment-based qualities like accuracy, tone, and helpfulness.
>
> They matter because an AI system can be technically operational and still produce an answer that is wrong, off-brand, or harmful. Evals turn “this looks good” into measurable quality. They help a business compare approaches, catch regressions, and decide whether the workflow is reliable and valuable enough to expand.

**How a repeatable eval runs:**

1. Create a frozen test case: save the representative input, such as a transcript, along with the same source documents, account data, mocked tool responses, expected behavior, and scoring rubric.
2. Run the AI workflow against that controlled case and capture both the final answer and the path it took: sources retrieved, tools called, order of actions, and escalation decisions.
3. Score objective requirements with rules and judgment-based qualities with the fixed rubric, using a human reviewer or an LLM judge where appropriate.
4. Change the system being tested—the prompt, model, retrieval configuration, tools, or workflow—while keeping the test case and rubric unchanged. Where possible, change one component at a time so the cause of any difference is clear.
5. Rerun the same suite, compare its scores with the previous version, and investigate any regression before rollout. Add new production failures and edge cases over time, but retain the old cases so previously solved behavior stays solved.

**Simple example:**

> Save the same support transcript, customer record, refund-policy snapshot, mocked tool responses, and expected escalation behavior. Run the current system against that frozen case, then rerun it after changing one component—for example, the system prompt. The test passes only if the agent retrieves the policy, checks the account, avoids issuing the refund automatically, explains the restriction accurately, and escalates the exception. If the revised version skips a step or approves the refund, the fixed test exposes the regression before customers encounter it.

**Raw-source basis:** Condensed from captured explanations by [LangChain](https://x.com/LangChain/status/2031055593360990358), [Braintrust](https://x.com/braintrust/status/2036467431917408681), and [Garry Tan](https://x.com/garrytan/status/2046876981711769720). This is a source-faithful synthesis, not a verbatim quotation.

### 5. How would you reduce hallucinations in an enterprise workflow?

> An AI hallucination is when a model generates a plausible-sounding claim that is false or not grounded in the source or context it was supposed to use. It might invent a fact, quote, citation, or source—or contradict the supplied evidence—while still sounding fluent and confident.
>
> I would not promise to eliminate hallucinations. I would treat them as a system-level risk: the model produces something plausible but unsupported, and the surrounding workflow either catches it or allows it through.
>
> I would reduce that risk in layers. First, ground the model in approved, current sources and show where important claims came from.
>
> Second, do not ask the model to guess facts or perform work that a trusted system can do precisely. Have it retrieve the balance from the billing system, perform calculations with a calculator, or check the policy in the approved database. Then limit what it can return and what actions it can take—for example, require specific fields in its response and prevent it from issuing a refund without authorization.
>
> Third, make the system ask for clarification, abstain, or escalate when the evidence is missing or ambiguous. For high-impact decisions, I would require human approval. Then I would trace the workflow and run repeatable evals against representative failure cases.
>
> For example, if a finance assistant is asked for a customer's current balance, the model should not infer it. It should query the system of record, return the verified value with its source and timestamp, and say it cannot verify the answer if that system is unavailable.
>
> The goal is not artificial certainty. It is preventing a plausible but unsupported output from becoming an unverified business decision or action.

**Reference definitions:**

- **Deterministic tool:** A trusted system that performs an exact lookup or calculation rather than asking the model to generate the result.
- **Schema:** A required output structure, such as customer ID, balance, currency, and source.
- **Permission:** A restriction on which information or actions the agent can access.

**Source boundary:** The definition was verified against [OpenAI's hallucination research](https://openai.com/index/why-language-models-hallucinate/) and the [NIST AI terminology and taxonomy](https://www.nist.gov/document/eu-us-terminology-and-taxonomy-artificial-intelligence-second-edition) on 2026-07-21. The mitigation sequence is a source-faithful synthesis of the verified definition and captured enterprise reliability material, not a verbatim quotation.

### 6. How would you explain Codex simply?

> Codex is OpenAI's coding agent for software development.
>
> The simplest distinction is that a chatbot can tell you how it would fix a bug; Codex can work on the bug inside a development environment. It can inspect the actual codebase, edit files, run commands and tests, read the results, and keep iterating until it has produced a change for review.
>
> For example, an engineer could ask Codex to fix a failed login flow. Codex could trace the relevant code, make the change, run the tests, and present the diff. The engineer still reviews the work and decides whether to merge and release it.
>
> I think of it as giving a software engineer a ticket and a controlled workstation, rather than asking a tutor a coding question. The business value is compressing the loop from understanding a task to producing tested, reviewable work—while keeping permissions, review, and deployment decisions with people.

**If pushed on where it runs:** Codex is available through interfaces including the IDE, CLI, desktop app, web and cloud experiences, and programmatic workflows through its SDK. The exact surfaces and entitlements should be checked for the customer's current plan.

**Official verification — 2026-07-22:** [OpenAI code-generation guide](https://developers.openai.com/api/docs/guides/code-generation#use-codex) · [Codex best practices](https://learn.chatgpt.com/guides/best-practices)

### 7. How do you choose between Codex, a ChatGPT Workspace Agent, and building with the API?

> I would use a least-custom-surface ladder: Codex for individual and team work, Workspace Agents for shared company workflows, and the API for fully custom products and systems.
>
> First, I would use Codex when a person or team needs an agentic work surface for either technical or knowledge work. That could include understanding and changing code, running tests, conducting research, analyzing data, creating reports, spreadsheets or presentations, building internal tools, and producing reviewable work products. The person is still directing the work and reviewing the result.
>
> Second, I would use a ChatGPT Workspace Agent when that work becomes a repeated company process. A team can encode its SOP, connect the approved sources and tools, define the output and approval rules, test it, and share the resulting workflow. It is a good fit when the process is bounded, repeatable, team-facing, and needs consistent judgment rather than every employee maintaining their own prompts.
>
> Third, I would use the API when AI needs to be embedded inside the customer's own product or operating system. That is the better fit when the customer must control the interface, orchestration, state, data flow, tool behavior, latency, and economics—and when that control creates meaningful differentiation.
>
> For example, a salesperson might use Codex to research an account and prepare a deal brief. If the entire sales team repeats that process, it could become a Workspace Agent triggered by a CRM event, following the same qualification rubric and requesting approval before updating anything. If the company wants that intelligence embedded directly into its own sales platform with a proprietary customer experience and workflow logic, that points toward the API.
>
> I would not treat this as a maturity ladder where the API is automatically better. The goal is to choose the least-custom surface that meets the requirement without taking on unnecessary engineering. The three can coexist, and I would route the customer after understanding the users, workflow, systems, required actions, governance, time-to-value, and where the experience genuinely needs to be differentiated.

**Two additional API examples — choose one if pushed:**

> Stripe's Minions are a good example. They are custom coding agents that engineers can start from Slack or other internal tools. Each Minion is designed to take a task—such as fixing a bug—from the initial request to a tested pull request in one shot, ready for human review. Stripe says Minions produce more than 1,000 merged pull requests a week.
>
> That requires much more than a generic chat interface. A Minion must work inside Stripe's codebase and isolated developer environment, follow Stripe's required testing and CI steps, and access a curated selection from nearly 500 internal MCP tools. Stripe therefore needs to control the entire workflow: where the task starts, which context and tools the agent receives, what steps it must complete, and where the human reviews the result. That is the kind of deeply customized system that points toward an API and custom orchestration.
>
> A second example would be a bank embedding an assistant inside its mobile app. The customer should not have to leave the bank's interface. The bank may need the assistant to use the signed-in customer's permitted account context, explain a transaction, check a dispute, or propose freezing a card through tightly controlled tools. The bank's application must own authentication, authorization, session state, deterministic policy checks, audit logs, latency, and approval for consequential actions. The API supplies the model capability inside the bank's product; the bank keeps control of the customer experience and execution boundary.

**Example boundaries:** Stripe's Minions are an independently documented example of a custom internal agent system, not a claim that Stripe built them with OpenAI's API. The banking assistant is hypothetical. Any production banking deployment would require product-, plan-, geography-, data-, security-, and regulatory-specific validation.

**Stripe source:** [Minions: Stripe's one-shot, end-to-end coding agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) and [Part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2), checked 2026-07-22.

**Likely follow-up: When does an opportunity become a Frontier or deeper deployment conversation?**

> I would bring in deeper deployment support when the customer is no longer configuring one bounded workflow or building one isolated application. They are trying to redesign a core business operation across multiple teams, systems, and decision paths.
>
> The signals would be executive sponsorship, a high-value production workflow, complex system integrations, shared company context, identity and permission requirements, rigorous evals, regulated or high-impact actions, and meaningful change management.
>
> For example, one sales team using a Workspace Agent for lead qualification is a bounded workflow. If the customer wants sales, customer success, finance, legal, and support agents to operate from the same customer definitions, policies, approval history, and decision records, that becomes a broader deployment problem.
>
> As the BDR, my role would be to qualify the business value, executive sponsor, workflow owner, systems involved, governance requirements, and readiness to act. Then I would bring in the Account Director and relevant technical or deployment partners. I would not promise Frontier eligibility, scope, or delivery terms without account-team confirmation.

**Source boundary:** The surface ladder was reconciled with the comprehensive answer bank and current official OpenAI documentation on 2026-07-21. Product availability, plan entitlements, API behavior, billing, and Frontier or deployment eligibility require current account-specific confirmation.

### 8. How do you decide between prompting, retrieval, tools, and fine-tuning?

> I start with an eval and diagnose the failure, because each lever solves a different problem.
>
> If the model can do the task but misunderstands the instructions or format, I improve the prompt and examples. If it lacks private, current, or source-backed knowledge, I use retrieval. If it needs live data, an exact calculation, or the ability to act in another system, I give it a tool.
>
> Fine-tuning comes later—when the model already has the right instructions, knowledge, and tools but keeps failing the same stable behavior across many examples.
>
> In customer support, use prompting for a consistent response format, retrieval for the latest refund policy, a tool to check the order or issue an approved refund, and consider fine-tuning only if the same escalation mistake persists despite correct context.
>
> My rule is to choose the smallest lever that fixes the measured failure, then rerun the same eval.

**Simple reference:**

- **Prompting** improves the instructions.
- **Retrieval** supplies the knowledge.
- **Tools** provide live capabilities and actions.
- **Fine-tuning** changes repeated model behavior.

**What is fine-tuning?**

Fine-tuning continues training a base model on examples, preferences, or reward signals so it performs a specific repeated task or behavior more consistently. It is generally not the first choice for storing current company knowledge, because that knowledge changes and may need permissions, citations, and auditing.

**Source boundary:** The decision sequence was reconciled with the comprehensive answer bank, captured source material, and [OpenAI's model-optimization guidance](https://developers.openai.com/api/docs/guides/model-optimization#model-optimization-workflow) on 2026-07-21. The framework is a source-faithful synthesis rather than a verbatim quotation.

### 9. When should a workflow use an agent versus deterministic automation?

> I ask whether the path can be defined reliably in advance.
>
> If the process follows known rules—validate fields, calculate a number, call an API, retry a failure, and update a record—I would use deterministic automation. It is usually faster, cheaper, easier to test, and more predictable.
>
> I would use an agent when the system must interpret messy context, apply judgment, handle exceptions, or decide which step is needed next. That flexibility is valuable, but it adds latency, cost, and variance, so the role should be bounded.
>
> Lead assignment by employee count and territory rules should be deterministic. Deciding whether an account is strategically worth pursuing may require an agent to assess its website, CRM history, recent signals, and likely use cases.
>
> In production, I would usually combine them: deterministic software runs the rails, the agent handles bounded judgment, and a person approves sensitive actions.

**Simple reference:**

- **Deterministic automation** follows a predefined path.
- **An agent** decides how to navigate toward the goal.
- **A hybrid workflow** places each responsibility where it is most reliable.

**Source boundary:** The distinction was grounded in captured source material defining workflows as predefined code paths and agents as model-directed processes. The final answer is a concise synthesis adapted to the interview context, not a verbatim quotation.

### 10. How would you identify the right OpenAI product or approach for a customer?

> I would start with the workflow, not the product catalogue.
>
> First, I would map who does the work, what triggers it, where the source of truth lives, where judgment is required, and where the process is slow, costly, risky, or difficult to scale.
>
> Then I would establish the business baseline and desired outcome: revenue, capacity, cycle time, quality, customer experience, or risk.
>
> I would also test readiness: an accountable owner, usable data, integration access, users who will adopt it, and clear approval and failure boundaries.
>
> Only then would I choose the least-complex surface that fits: a governed ChatGPT workspace for broad employee work, Codex for technical or artifact-heavy work, a shared agent for a repeatable company process, the API for a differentiated embedded experience, or conventional automation for known rules.
>
> I would finish with the smallest proof that resolves the biggest uncertainty, using representative data, explicit success metrics, and a human-review path.

**Memorable lines:**

> I would not prescribe the surface before discovery.

> The recommendation should connect the workflow, owner, business value, risk boundary, and next proof step.

**Source boundary:** The discovery sequence follows the recruiter-screen canon and was reconciled with the comprehensive answer bank. Product names, availability, packaging, and deployment eligibility require current account-specific confirmation.

### 11. Why would a customer choose OpenAI if they already use a competitor?

> I would not ask the customer to replace something that already works. I would explain where OpenAI may offer a clear advantage, then prove it using their work.
>
> For engineering, Sam Altman summarized the case well: GPT-5.6 Sol is half the price and roughly twice as token-efficient as Fable in many cases when completing the same task. In simple terms, it can deliver the result for roughly one-quarter of the cost. That makes Sol a strong everyday workhorse, not simply a model reserved for the hardest problems.
>
> For knowledge work, the advantage is the breadth of the OpenAI ecosystem. A company gets leading models alongside voice, image generation, computer use, company knowledge, connected applications, Codex, and tools for producing documents, spreadsheets, presentations, and other finished work.
>
> ChatGPT Work adds another practical advantage: it is a cloud-first agent available on web and mobile. Someone can start a longer task from their phone, let it keep working, then check progress, answer a question, change direction, or approve an important action between meetings. The same cloud Work chat continues across mobile, web, and desktop.
>
> That matters because longer agent workflows often stall on small human decisions. Mobile lets people unblock the work in a few minutes without sitting at a desk, while keeping them in control.
>
> I would then compare OpenAI and the incumbent on a few real customer tasks: which produces the better result, how long it takes, what it costs, and how much human correction it needs.
>
> If OpenAI creates a meaningful advantage, it can begin with that workflow and expand from there. It does not need to replace everything on day one.

**Simple framing:**

> For engineering, OpenAI offers a better workhorse. For knowledge work, it offers a broader multimodal platform. ChatGPT Work makes that platform available wherever the user is. Prove the advantage on the customer's real work.

**Product boundary:** Work on web and mobile runs in the cloud and cloud Work chats sync across web, mobile, and desktop. It cannot directly use files stored on the user's computer; that requires the desktop experience and permission. Availability also depends on plan, rollout, and workspace controls.

**Official verification — 2026-07-21:** [ChatGPT Work announcement](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) · [ChatGPT Work and Codex guide](https://help.openai.com/en/articles/20001275) · [GPT-5.6 launch and benchmark details](https://openai.com/index/gpt-5-6/)

### 12. How do you translate technical capability into measurable business value?

> I use a simple chain: technical capability, workflow change, operating metric, and business result.
>
> I start with the customer's current workflow and baseline, not the model feature. If retrieval brings an approved support answer into the case faster, the workflow change is less searching. The operating metric might be lower handle time or more cases per agent. The business result might be lower cost-to-serve or faster response—provided quality and customer satisfaction do not fall.
>
> I would test that in a narrow pilot, compare it with the baseline, and translate the validated improvement using the customer's actual case volume and loaded cost. Then I would subtract software, implementation, adoption, and continuing review costs.
>
> The customer's controlled pilot supplies the number, not a generic industry benchmark.

**Memorable line:**

> A technical capability becomes business value when it changes a metric the customer already cares about.

---

## Part II — Core Technical Concepts

### 13. Explain tokens and context windows simply

> Tokens are the small pieces of information a model reads and produces. A token may be a whole word, part of a word, punctuation, or another encoded unit.
>
> The context window is the model's working-memory budget for the current task. Instructions, conversation history, retrieved documents, tool results, and the answer all consume that budget.
>
> A larger window lets the model consider more material, but more is not automatically better. If the useful evidence is buried in noise, the model can lose focus, while cost and often latency rise.
>
> I think of it as a larger desk: it helps you spread out more relevant material, but covering it with every document in the company does not help you find the answer.
>
> The practical goal is the smallest set of high-signal context that lets the model do the job reliably.

**Currentness boundary:** Exact limits, input/output allocations, pricing, and tokenization vary by model and product surface. Verify them only if a specific current model is asked about. A context window is not persistent long-term memory.

### 14. Explain embeddings and semantic search

> Think of embeddings as a map of meaning. An embedding turns each passage into a point on that map, so passages that mean similar things land in the same neighborhood even when they use different words.
>
> A search question becomes a point too. Semantic search finds the passages nearest to it. So "How do we handle refunds?" can find a page called "Chargeback policy" even if the word *refund* never appears.
>
> The business value is that employees can find relevant knowledge without knowing the exact wording or document title.
>
> But similarity does not guarantee correctness. Keyword search is often better for exact names, IDs, dates, and policy titles. A strong enterprise system combines both, then applies permissions, freshness checks, reranking, and citations.

**If pushed technically:**

> The point is actually a vector—a long list of numbers—and the system compares those vectors to estimate which meanings are closest.

**Raw-source basis:** The map, neighborhood, and refund-versus-chargeback explanation comes from [[2026-07-02-seth-note-on-gbrain-embeddings-and-hybrid-retrieval]]. The hybrid-search boundary is supported by [[llm-foundations]] and the comprehensive answer bank.

### 15. Explain APIs and function calling to a business stakeholder

> An API is a defined way for one software system to request data or an action from another. Think of a controlled service counter with a menu and an order form. Function calling lets the model choose an approved item and fill in the required details.
>
> If a customer asks where an order is, the model might request `look_up_order` with the order ID. That is only a request. The customer's application checks the user, permissions, and inputs; it—not the model—calls the order system and returns the result.
>
> For a higher-impact action like issuing a refund, the application can require manager approval first.
>
> The business value is moving from generated text to controlled workflow action without giving the model unrestricted access to core systems.

**Memorable boundary:**

> The model proposes the action; the customer's application decides whether and how it happens.

**Source boundary:** This execution boundary applies to customer-defined functions. OpenAI-hosted tools may execute on the platform. Current function-calling behavior was verified against the [official OpenAI guide](https://developers.openai.com/api/docs/guides/function-calling#how-it-works) on 2026-07-21.

### 16. Explain MCP or connectors simply

> MCP is a common language between an AI system and outside tools. A connector is the ready-made translator for a specific service.
>
> For example, if I ask ChatGPT to prepare an account brief, a Google Drive connector can expose approved tools for searching and retrieving files. ChatGPT discovers those tools, finds the documents the signed-in user can access, and uses the relevant account plan and meeting notes to create the brief.
>
> The business value is faster integration and reuse. Companies do not need to custom-build every model-to-system connection from scratch.
>
> But MCP standardizes the connection; it does not make it safe by itself. You still need trusted servers, narrow permissions, logging, and approval gates for consequential actions.

**Memorable distinction:**

> MCP is the common language; a connector is the translator for a specific system.

**Source boundary:** In the Responses API, OpenAI defines connectors as OpenAI-maintained MCP wrappers for supported services. Remote MCP servers may be third-party and require separate trust review. Current terminology and security boundaries were verified against the [official OpenAI MCP and connectors guide](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) on 2026-07-21.

### 17. What is the difference between a CLI and MCP, and when would you use each?

> A CLI lets an agent control software by typing commands into a shell—the command-running environment a developer normally uses through a terminal. MCP gives an AI assistant a defined set of tools for connecting to an external system.
>
> For a simple task, such as finding a Notion page or updating a record, I would usually use MCP. The user can sign in normally, and the managed connection can work across employees and supported AI products without everyone installing software or configuring terminal credentials.
>
> For a complex workflow, I would use the CLI if the agent has access to a secure shell. The agent can write a script that searches hundreds of pages, filters the results, combines Notion with other systems, handles failures, and produces one final report. The computer performs the repetitive steps without sending every intermediate result back to the model.
>
> MCP tools are often called one at a time: the model calls a tool, reads the result, and chooses the next action. A CLI is naturally easier to program because the agent can write the entire sequence as one script.
>
> So my rule is: use MCP for simple, shared, controlled access. Use the CLI for complex, programmable work inside a secure shell. For advanced workflows, the two can also be combined.

**Concrete Notion example:**

> Imagine the request is: “Find our Notion notes about Acme, identify the latest objections, and create an account brief.”
>
> With Notion MCP, the employee connects their workspace through OAuth. The assistant uses approved Notion tools to search for Acme, fetch the relevant pages, summarize them, and create the brief. That is the simpler route for a shared employee workflow.
>
> If the request expands into a batch job—search hundreds of pages, filter the results to titles, URLs, dates, and page IDs, fetch only the useful pages, combine them with a CRM export, retry failures, and save source snapshots locally—the CLI is stronger. The agent can write one script that performs the repetitive processing and returns a compact evidence packet to the model.
>
> The two can also combine: MCP supplies the governed Notion connection, while code handles the loops, filtering, and composition.

**Memorable distinction:**

> MCP gives the agent approved buttons. A CLI lets it write a program and run it through the shell.

**Technical boundary:** Both paths still require authentication and permission to the relevant Notion content. The CLI advantage comes from code execution, not from typing terminal commands by itself. Newer agent systems can expose MCP tools to code, combining MCP's governed access with the filtering, loops, and composition of a script.

**Official verification — 2026-07-22:** [Notion CLI overview](https://developers.notion.com/cli/get-started/overview) · [CLI authentication](https://developers.notion.com/cli/get-started/authentication) · [CLI API requests](https://developers.notion.com/cli/guides/api-requests) · [Notion MCP overview](https://developers.notion.com/guides/mcp/overview) · [Notion MCP tools](https://developers.notion.com/guides/mcp/mcp-supported-tools)

### 18. What is the difference between a reasoning model and a general-purpose model?

> The clean distinction is increasingly between more reasoning effort and faster response, rather than two completely separate kinds of model.
>
> A model using more reasoning effort spends more compute working through a difficult problem before answering. That can help with multi-step analysis, coding, planning, and complex tool use. For a simple lookup, extraction, or formatting task, that extra effort may only add latency and cost.
>
> So I would choose based on task complexity, the cost of a wrong answer, response-time requirements, and eval results. I might use low reasoning for high-volume classification, then increase it for an ambiguous exception or a complex plan.
>
> Commercially, the goal is not maximum reasoning everywhere. It is the fastest, lowest-cost configuration that reliably clears the workflow's quality bar.

**Currentness boundary:** Model families, names, and reasoning controls change quickly. More reasoning can improve some tasks, but only customer-specific evals establish the right setting.

### 19. What is fine-tuning, and when is it the wrong solution?

> Fine-tuning adapts a base model using examples, preferences, or reward signals so it performs a repeated task or behavior more consistently. It can help with stable style, terminology, classification patterns, or output behavior.
>
> It is usually the wrong first answer when the problem is current company knowledge. Policies, prices, account notes, and product documentation should stay external, refreshable, permissioned, and auditable through retrieval or tools.
>
> I would consider fine-tuning only when the model already has the right instructions and context but keeps failing the same measurable pattern across enough high-quality examples. Before training, I would want a clean dataset, a held-out validation set, and an eval that proves the tuned model improved without breaking other behavior.
>
> The simplest distinction is: retrieval supplies changing facts; fine-tuning changes repeated behavior.

**Rehearsal note:** This is the direct follow-up to Q8, not a second decision framework to memorize.

**Currentness boundary:** Fine-tuning can complement retrieval. Exact methods, supported models, cost, and availability require current official verification.

---

## Part III — Product, Architecture, And Proof Judgment

### 20. How would you choose between models with different accuracy, speed, and cost?

> I would define the workflow's quality bar first, then test candidate models on representative cases. I would score task success, groundedness, tool use, latency, cost, and the severity of failure—not just benchmark accuracy.
>
> I would start with the fastest, lowest-cost model that might clear that bar. That may be right for high-volume classification or extraction. I would pay for a stronger reasoning model where ambiguity and the cost of a wrong answer justify it, such as complex exception handling or coding work.
>
> I would choose the simplest setup that passes the customer's evals. Routing can help, but it adds monitoring and maintenance, so I would add it only when the measured gain is worth that complexity. Model choice is an operating decision, not a leaderboard contest.

### 21. What is the difference between a prototype, a proof of value, and production?

> A prototype asks, “Can it work?” It is a thin feasibility test and can use controlled data or clearly labelled mocks.
>
> A proof of value asks, “Does it improve a real outcome?” It needs representative users and cases, a baseline, buyer-defined success and guardrail metrics, and an explicit go, iterate, or stop decision.
>
> Production asks, “Can we run it safely every day?” That requires hardened integrations, identity and permissions, monitoring, support and incident ownership, cost controls, training, and change management. I would never present success at one stage as proof of the next.

### 22. How would you scope a credible enterprise AI pilot?

> I would start with one falsifiable decision question, then choose one user group, one bounded workflow, a representative data set, and a clear baseline.
>
> With the customer, I would define the integrations, quality and business metrics, guardrails, security boundary, human-review path, owners, timeline, and what is explicitly out of scope. I would also agree in advance what result means go, iterate, or stop.
>
> For example: can this document workflow reduce first-pass review time on these file types while maintaining field and citation accuracy and routing uncertain cases to a reviewer? A good pilot is narrow enough to finish and serious enough to support a decision.

### 23. What would you measure during that pilot?

> I would measure four layers. Model quality: correctness, groundedness, completeness, and appropriate refusal. Workflow quality: tool selection, state handling, escalation, and end-to-end task completion. Operational quality: latency, reliability, cost, and integration errors. Business value and adoption: whether users actually use the workflow and whether it changes the customer metric we targeted, such as cycle time, throughput, quality, customer experience, or cost-to-serve.
>
> I would compare the results with a baseline or control and pair every efficiency metric with a guardrail. Faster support is not a win if repeat contacts or customer frustration rise. The conclusion should state what the pilot proved and what it did not.

### 24. How do you design human review into an AI workflow?

> I design human review around consequence, ambiguity, and reversibility. I think of it like signing authority.
>
> Low-risk, high-confidence preparation can move automatically. Ambiguous or medium-risk cases should arrive as a review packet: the proposed answer, source evidence, tool results, uncertainty, and unresolved questions. High-impact actions—payments, legal conclusions, customer commitments, regulated decisions, or irreversible writes—require explicit approval or escalation.
>
> The reviewer should be able to correct the result without losing the original output, and the system should capture why it changed. That reduces the reviewer's search cost while keeping responsibility and the audit trail clear.

**Truth boundary:** Source-grounded does not mean correct. Do not claim calibrated confidence thresholds, production-grade evals, or measured reviewer-time savings unless verified.

### 25. What does production readiness require beyond a good model?

> Production readiness is an operating-system question around the model.
>
> I would look for four things: controlled access—identity, permissions, and data boundaries; reliable execution—hardened integrations, structured outputs, queues, retries, and recovery; observable quality—logs, monitoring, regression evals, and cost limits; and operating ownership—incident response, support, rollout, training, and change control.
>
> The test is not whether the model looks impressive. It is whether failures are visible, containable, recoverable, and owned.

### 26. How would you speak credibly with a CTO or engineer without pretending to be the implementation engineer?

> I would earn credibility by making the workflow and the open questions precise.
>
> At Boxo, I would start with the user journey, then map which system owned identity, data, payment, status, and support. With engineering, I would walk through each handoff: what context is passed, when authentication is needed, what gets written back, and what happens if one system succeeds and the other fails. I would capture unanswered questions instead of improvising, assign an owner, and return with the evidence or a proposed test.
>
> I can discuss the workflow, data flow, source of truth, tools, permissions, evals, failure modes, human review, and commercial outcome. I would not invent an exact architecture, security, residency, or roadmap commitment. My job is to make the decision inspectable and bring in the right technical partner when the answer affects feasibility or contractual risk.

**Ownership boundary:** I commercially orchestrated technical discovery and stakeholder alignment at Boxo. I did not design Boxo's SDK, authentication, payment architecture, or production integration.

### 27. Which questions would you answer directly, and when would you bring in a technical partner?

> I would answer durable conceptual and workflow questions directly: what an LLM, RAG, agent, API, tool, or eval is; which product category may fit; what discovery questions matter; and how business value could be measured.
>
> I would bring in a technical partner for customer-specific architecture, security reviews, data residency, regulated-data eligibility, networking, identity, scale limits, migration design, benchmark interpretation, or any commitment that could enter a contract or implementation plan.
>
> Before escalating, I would summarize what I understand, state the exact open question, and explain why the answer changes the decision. My role is to move the opportunity forward without creating technical debt in the sales process.

### 28. When would you lead with an employee workspace versus the API?

> I would lead with a managed employee workspace when the goal is to improve how employees work—research, analysis, writing, coding, meeting preparation, or shared internal workflows—with enterprise administration and a familiar work surface.
>
> I would lead with the API when AI must be embedded in the customer's own product, customer experience, or deeply customized internal system, and the customer wants to control the interface, orchestration, tools, data flow, and unit economics.
>
> My first question is: are we changing how employees work, or building a system that customers or operations will use? Many strategic accounts need both, but each motion needs its own owner, success metric, and adoption plan.

### 29. When is Codex the right wedge?

> Codex is the right wedge when the owned, measurable pain is in software delivery: understanding a codebase, implementing changes, running tests, reviewing diffs, debugging failures, migrations, maintenance, or backlog throughput.
>
> I would qualify whether the customer wants individual developer productivity or a repeatable, governed engineering workflow across teams. The proof should use the customer's repositories, task types, review standards, and security boundaries.
>
> I would measure adoption, task or cycle time, review quality, regressions, and developer trust—not generated lines of code. If developers prefer another tool, I would run a workload-specific evaluation rather than argue by brand.

### 30. When should a customer build a custom application?

> A custom application makes sense when AI must live inside the customer's own product or proprietary workflow, and when the user experience, state, integrations, security boundary, or unit economics are strategically differentiating.
>
> The customer should be honest about what it is choosing to own: authentication, tools, data flows, prompts, state, evals, monitoring, approvals, migrations, and support.
>
> If the real goal is a repeatable internal workflow, a managed work surface or shared agent may reach value faster. I would build when that extra control is strategically valuable and the customer has the team to operate it—not because custom architecture sounds sophisticated.

### 31. When is a shared agent workflow appropriate?

> A shared agent workflow is appropriate when a team repeats a bounded process with an owned SOP, approved sources and tools, clear review rules, and a measurable destination.
>
> Good examples include account briefing, support triage, vendor review, weekly operating reports, or document-intake preparation. The business team should own the rubric and success metric; the platform supplies the agent infrastructure and governance surface.
>
> It is a weak fit when the workflow needs a low-latency response inside a proprietary product, most of the logic is deterministic, the action boundary is unsafe, or nobody owns the process. I would prove one workflow first, including its exception and approval path, before scaling it across a team.

**Currentness boundary:** Treat “shared agent” as a solution category in the live answer. Exact naming, packaging, plan eligibility, and availability require current confirmation.

### 32. When should the customer keep a workflow engine such as n8n, Workato, or Salesforce Flow?

> Keep the workflow engine for stable orchestration: schedules, webhooks, credentialed API calls, field transformations, retries, system writes, and failure alerts. Those are deterministic operations and should be cheap, visible, and predictable.
>
> Add an agent where the process requires reading messy context, applying a changing rubric, handling exceptions, or drafting a recommendation. A practical hybrid is: the workflow engine receives the event and validates it; the agent applies judgment; a human approves; and the workflow engine performs the final write and logs it.
>
> The decision is about which layer should own judgment and which should own execution.

### 33. How would you approach a regulated bank, healthcare organization, or legal workflow?

> I would start with the decision and its consequences, not with the model. What decision are we supporting, what data does it require, who is allowed to see it, which system is authoritative, and what must remain with a licensed or accountable human?
>
> Then I would choose a narrow, reviewable workflow where AI prepares the work rather than owns the final decision. In Sunder, for example, we did not ask AI to decide a personal-injury claim. We used it to classify messy evidence, extract typed fields, attach source citations, flag missing or suspicious information, and prepare a first-draft review pack. The lawyer retained legal judgment and sign-off.
>
> I would define the proof around one operational outcome—such as time to a reviewable file, exception rate, or reviewer effort—and require permissions, source grounding, validation, logs, exception routing, and approval gates appropriate to the risk. Before promising privacy, residency, retention, HIPAA, or other regulated-data coverage, I would verify the exact product, plan, geography, and contract with the relevant OpenAI specialist.

**Truth boundary:** Sunder was a review-first paid pilot, not a compliant production legal system. Do not imply that its controls automatically satisfy banking, healthcare, or legal requirements.

### 34. How would you distinguish a compelling use case from an AI science project?

> A compelling use case has an owner, a repeated painful workflow, usable data, a reviewer who can tell good from bad, and a business metric that changes if the workflow improves.
>
> A science project usually starts with an impressive capability and then searches for a problem. Nobody owns the operating change, there is no baseline, and the pilot cannot answer a decision such as whether to deploy, expand, or stop.
>
> Sunder is a good example. We began with the broad idea of AI for lawyers. After close to 50 lawyer conversations, we learned that routine legal knowledge was not the bottleneck. The repeated pain was preparing messy personal-injury evidence. It had recognizable inputs, high volume, visible admin effort, a reviewable output, and lawyers who could judge the result. We rejected legal autopilot and chose a cited review pack instead; that narrower wedge led to a paid pilot.
>
> My test is simple: if we can name the owner, current baseline, workflow endpoint, risk boundary, and decision the pilot will support, it is probably a real use case. If we cannot, it is still exploration.

**Truth boundary:** “Close to 50 lawyer conversations” and the paid Hoh Law pilot are supported. Do not turn that pilot into audited ROI, broad deployment, or repeatable product-market fit.

### 35. When would you tell a customer that OpenAI is not the right immediate solution?

> I would say “not yet” when there is no owned problem, no usable source of truth, no reviewer, no measurable baseline, or no safe boundary for the decision the customer wants to automate.
>
> I would also say it when deterministic software is the simpler answer. If stable rules, a workflow engine, or the customer's current platform already solves the job reliably, adding a model may increase cost and failure modes without adding value.
>
> I would not end with a rejection. I would identify the missing prerequisite: clean the data, map the workflow, write the SOP, establish a baseline, or choose a smaller assistive step such as retrieval, drafting, or triage with human approval. That gives the customer a credible path back later.

---

## Part IV — Competitive And Coexistence Scenarios

### 36. A customer has standardized on Microsoft Copilot or Azure. What do you do?

> First I would clarify what “standardized” means. Is it employee access through Copilot, Azure procurement, a model endpoint, developer tooling, or production workflows? Those are different decisions.
>
> Then I would ask what is live, what is working, and where there is an unmet workflow. If the current environment is doing the job, I would not propose replacement. I would look for a distinct use case where OpenAI could create incremental value and test it with the customer's own users, data, security requirements, and success metric.
>
> The decision is economic: does the measured improvement justify another vendor, integration path, and operating model? If not, I would leave the existing standard in place.

**Truth boundary:** Do not treat Copilot, Azure procurement, model access, and production architecture as one thing. Make no universal quality, cost, or security comparison.

### 37. Their developers prefer Claude, Cursor, or another coding tool. How do you respond?

> I would respect developer preference. For an individual coding-tool decision, I would not ask engineers to trust a seller's benchmark claim. I would run the tools on representative work from their own repositories.
>
> I would agree the test before the bake-off: task success, time to a reviewed change, test pass rate, rework, security and permission fit, and whether developers actually keep using it. I would include real tasks such as fixing a bug, adding a feature, generating tests, or reviewing a change—not a toy prompt.
>
> I would also clarify whether the buyer is choosing an individual IDE or terminal tool, or a governed engineering workflow across repositories, permissions, review, and organizational rollout. If Codex wins the customer's workload and adoption test, there is a defensible reason to adopt it. If another tool wins, that is useful evidence too.

**Currentness boundary:** Do not claim Codex universally beats Claude, Cursor, or another tool. Recheck product availability, packaging, and any benchmark or price claim before using it.

### 38. They use AWS Bedrock or another model-platform layer. Why consider OpenAI directly?

> I would not assume direct is better. A model-platform layer can be valuable for cloud alignment, centralized procurement, provider choice, and a consistent architecture.
>
> I would ask what the customer is optimizing for. If it is portability and central control across providers, keep the platform layer. If a specific OpenAI workload would benefit from a first-party model-and-tool path, a managed work surface, or a simpler support and integration boundary, test that directly on the workload.
>
> The comparison should include task success, latency, cost per completed outcome, prompt and tool compatibility, observability, security review, migration work, and who owns regressions. If the direct path does not produce a material improvement after those costs, there is no reason to add it.

**Truth boundary:** Do not make unverified claims about Bedrock feature lag, model availability, pricing, SLAs, data paths, or support quality. Compare the customer's actual architecture and contract.

### 39. They want to use several model providers. Is that a problem?

> No. Multi-model can be a rational design when different workloads genuinely need different quality, latency, modality, cost, deployment, or governance characteristics.
>
> The issue is the operating tax. “Best model” is workload-specific, so the customer needs representative evals for each route, prompt and tool compatibility, regression monitoring, fallback behavior, data-handling rules, and an owner for model changes. A provider switch is production work, not a dropdown.
>
> I would ask what the second or third provider buys in measurable terms. If it lowers cost or improves an important workflow enough to cover the extra engineering and governance burden, use it. If it only creates theoretical optionality that nobody can operate reliably, simplify.

### 40. They believe an open-source model will be cheaper. How do you evaluate that claim?

> It may be cheaper, but I would separate inference price from cost per successful outcome.
>
> I would run the target workflow on representative inputs and measure quality, latency, failure and escalation rate, human-review time, and infrastructure cost. Then I would add the work the customer owns: hosting, optimization, security, orchestration, evals, monitoring, upgrades, incident response, and any extra scaffolding needed to close a quality gap.
>
> If the open model clears the customer's quality and risk bar at lower end-to-end cost—or if self-hosting and control are strategic—it may be the right answer. If the token savings return as engineering, reviewer effort, or operational risk, it is not cheaper for that workflow.

### 41. They already have an internal AI team. What value could OpenAI still provide?

> I would treat an internal AI team as a positive signal. They understand the business and should own the parts that differentiate the company: workflow logic, proprietary context, user experience, approval policy, system-of-record decisions, and business KPIs.
>
> The discovery question is which other layers are strategic to own. OpenAI may provide models, APIs and tools, coding and employee work surfaces, agent orchestration patterns, eval capabilities, and enterprise administration. The internal team can then spend more time on the company-specific workflow instead of rebuilding every shared platform component.
>
> The answer may still be hybrid or fully custom. I would map the stack, identify where the team is spending undifferentiated effort, and prove whether an OpenAI layer improves delivery speed, quality, governance, or operating cost. The positioning is acceleration and leverage, not replacement.

**Currentness boundary:** “May provide” is deliberate. Exact product availability, packaging, and deployment support require current confirmation.

### 42. What evidence would justify switching platforms?

> I would switch only for a meaningful, repeatable advantage on an important workload.
>
> First I would define the incumbent baseline and the full switching cost: migration, integrations, retraining, security review, procurement, operational risk, and the minimum improvement required. Then I would run the same representative eval set and real-user trial across both approaches.
>
> I would measure task success, quality, latency, cost per completed outcome, failure and review burden, adoption, governance fit, and ongoing maintenance. A benchmark headline is not enough. The advantage has to survive real use and pay back the cost and risk of change.

### 43. When is coexistence better than replacement?

> Coexistence is better when the incumbent works well, switching cost is high, and OpenAI has a distinct workload with different users, economics, or technical requirements.
>
> I would start with the smallest non-overlapping use case, define its owner and success metric, and prove whether the extra platform creates enough value to justify another integration and operating model. That lets the customer learn without disturbing a working system.
>
> Replacement becomes reasonable when fragmentation itself creates material cost or risk, the incumbent repeatedly misses critical requirements, and a representative evaluation shows that one platform can consolidate the workload without degrading outcomes. I would earn that discussion through measured value, not make replacement the opening demand.

**Operating boundary:** Coexistence can create duplicate spend, fragmented governance, and operational overhead. Replacement also carries migration, retraining, integration, and organizational risk.

---

## Part V — Seth's Proof Stories

### 44. Tell me about the most technically complex AI workflow you helped build

**15-second setup:**

> My strongest example is Sunder: a review-first legal document workflow that turned messy personal-injury evidence into cited, structured, editable work products while keeping legal judgment with lawyers.

**Recommended answer — 75–90 seconds:**

> My strongest example is Sunder, a three-month paid pilot with Hoh Law for personal-injury document operations. The hard part was that the input was messy—combined PDFs, scans, medical bills, reports, income evidence, duplicates, and documents arriving over time—but the output still had to be inspectable by a lawyer.
>
> I helped design it as a stateful review workflow: case, source document, classified split, typed extraction, validation, human review, and report. Gemini handled classification and splitting, Extend handled schema-based extraction and citations, and Sunder owned the case state, permissions, validation, review UI, corrections, and final artifact.
>
> For each split, we stored the original extraction separately from the reviewer-edited value, plus source metadata, citations, low-confidence fields, and validation failures. Client-specific rules checked required fields, suspicious amounts, payer categories, and duplicate or missing evidence before a reviewer generated the work product.
>
> I personally owned the product framing, workflow mapping, data contracts, review logic, pilot sale, and agent-supervised implementation. I did not train the underlying models or make the legal decisions. The pilot produced a functional case-to-report workflow that real users could inspect and correct. My main lesson was that the model call was only one component; the product was the state, provenance, exception handling, and human-review loop around it.

**What this proves:** Workflow discovery, technical translation, trust design, and honest ownership.

**Likely follow-up — Why did you build a review-first workflow rather than legal autopilot?**

> I chose review-first because our discovery showed that legal judgment was not the main bottleneck.
>
> Across close to 50 lawyer conversations, the repeated pain was evidence preparation: splitting and classifying messy documents, extracting medical expenses and income information, finding missing or duplicated evidence, reconciling inconsistent values, and turning the file into something a lawyer could review.
>
> A legal-autopilot design would have introduced risk around liability, causation, precedent, negotiation strategy, and client advice without solving that underlying operational problem.
>
> So we automated the evidence layer instead. Extracted information stayed linked to its source. Missing, contradictory, or low-confidence information was flagged for review. Original extractions and reviewer corrections remained separate, and the lawyer retained responsibility for the legal conclusion and anything sent externally.
>
> Commercially, that narrower promise was also easier to trust and pilot. The customer did not have to believe that AI could replace a lawyer. They only had to believe that it could prepare the file more quickly and consistently while making the lawyer's review easier.
>
> That is what I mean by selling trust through constraint: narrow the system to the work AI can do credibly, make the output inspectable, and leave consequential judgment with the professional.

**Truth boundary:** A real three-month paid pilot and review-first workflow are verified. Do not claim broad deployment, final legal advice, lawyer or paralegal replacement, production-grade evals, or measured ROI without recovered evidence.

### 45. How did you make the Sunder/Hoh Law workflow trustworthy?

> We made trust visible at five levels: scope, sources, validation, history, and approval.
>
> First, we constrained the scope. Sunder prepared the evidence and first-draft work product; it did not issue final legal advice or make the lawyer's decision.
>
> Second, important extracted fields stayed connected to their supporting document and citation metadata. A reviewer could inspect where a medical expense, income figure, date, or claimant detail came from instead of accepting a black-box answer.
>
> Third, we used typed extraction schemas and client-specific validation rules. Missing payer categories, suspicious values, duplicated documents, inconsistent claimant details, missing supporting files, and low-confidence extractions moved into `needs review` rather than appearing as clean output.
>
> Fourth, we preserved the history. The original extraction, reviewer-edited value, validation status, and correction reason remained separate. A correction did not silently overwrite what the model originally produced.
>
> Finally, the lawyer or document reviewer approved the evidence before it became part of the work product. The system helped prepare and structure the file, but the professional remained responsible for the legal conclusion and anything sent externally.
>
> For example, if Sunder extracted a medical expense, the reviewer could see the amount, payer, date, and source page. If the payer was missing or the invoice appeared twice, the field would be flagged. The reviewer could correct it while preserving both the original extraction and the reason for the change.
>
> That is what made the workflow trustworthy: the user could see the evidence, understand the uncertainty, correct the result, and retain responsibility for the final decision.

**Truth boundary:** These source, schema, validation, state, and review controls are grounded in the Sunder build. A formal eval suite, production monitoring, broad deployment, and measured ROI remain proposed next steps unless supporting evidence is recovered.

### 46. How did Salescraft use AI beyond writing outbound emails?

> My best example is the account-intelligence system I built for Uptick. The problem was not writing emails. Their CRM did not give them one clean view of the wider US fire-protection market.
>
> Data from the CRM, Google Maps, company websites, and other sources contained duplicate listings, broken websites, companies outside the target market, false positives like fire departments or equipment sellers, and multiple branches of the same business.
>
> I built the workflow in three layers: rules for obvious decisions, AI for messy judgment, and people for uncertain cases.
>
> First, deterministic rules removed records with clear problems, such as broken websites, out-of-country results, and exact duplicates.
>
> Then AI read the website evidence. It judged whether the company actually provided relevant fire-protection services and classified it as maintenance-led, installation-led, or mixed. We calibrated that judgment using around 50 strong CRM customers and by observing how Uptick's reps evaluated company websites.
>
> Finally, uncertain decisions—such as whether two branches belonged to the same parent company—went into a review queue with the supporting sources. The output was routed into four paths: update an existing CRM account, create a net-new account, send it for manual review, or suppress it.
>
> The business value was a cleaner view of the real market and a higher-confidence account queue for sellers. I would not claim that the system autonomously created pipeline or produced a verified revenue lift.

**Reference definition:**

> **Entity resolution:** Determining whether messy records, trading names, branches, and website listings represent the same real company.

**Source boundary:** The safe outcome is improved TAM visibility, CRM quality, account routing, source evidence, and a QA-safe seller queue. Parent, branch, headcount, and LinkedIn signals remain evidence with confidence rather than guaranteed facts. Do not attach unverified pipeline or revenue lift to this workflow.

### 47. What did Boxo teach you about communicating with product and engineering buyers?

> Boxo taught me that product and engineering buyers need different evidence, and that technical products are easier to understand when you explain the user journey, system boundaries, and failure cases—not merely the features.
>
> At UNA, I started with the desired user journey. A customer would open the UNA app, enter a merchant experience, browse products, check out using UNA's BNPL option, and receive a clear payment and order status without feeling that they had left UNA.
>
> Then I clarified ownership. UNA remained responsible for customer identity, login, BNPL eligibility, payment approval, and the financial record. The merchant owned its catalog, inventory, order details, fulfilment, and product support. Boxo provided the connecting layer that allowed the merchant journey to operate inside UNA and passed the required context and status between the two systems.
>
> With engineering, I walked through every handoff: what context was passed when the merchant opened, when authentication was required, how payment was initiated, how payment and order status returned, and what each system recorded.
>
> Then we pressure-tested the failure cases. What happens if payment succeeds but the merchant cannot create the order? What gets logged? Can the action be retried safely? Who supports the customer? Which team owns the resolution?
>
> I captured unanswered questions instead of improvising. Each question received an internal owner, the evidence required, and a next step. I translated those concerns into clear requirements for our product team, then returned to the buyer with precise answers or a proposed test.
>
> Product received a clear story about user experience and roadmap control. Engineering received an inspectable integration flow, ownership boundaries, failure handling, and a path from demo to testing and production.
>
> My role was not to design the architecture myself. It was to make the workflow concrete enough that engineering could evaluate it, make uncertainty visible, and bring in the right technical person when the question exceeded my boundary. That is what I mean by making a technical decision underwriteable.

**Communication method:**

1. Start with the desired user journey.
2. Define which system owns each piece of data and each action.
3. Walk through every integration handoff.
4. Pressure-test failures and exceptions.
5. Record unknowns instead of improvising.
6. Assign owners and agree on the next proof step.
7. Translate the same system into each stakeholder's definition of value.

**Truth boundary:** Seth commercially orchestrated the technical deal and owned product and engineering conversations. Do not imply that he engineered the SDK or personally designed the authentication and payment architecture. If asked for commercial proof, use the current user-confirmed figures: UNA expanded from approximately USD 200K to USD 300K ARR, and Epon was approximately USD 300K ARR.

### 48. How do you use Codex in practice?

> Codex is my main workbench. I use it in three broad ways: building and verifying software, conducting source-backed research and knowledge work, and turning repeated tasks into reusable workflows.
>
> For software, I can give it an objective, let it inspect the codebase, implement the change, run tests, and produce a diff for me to review. For GTM work, it can search my source-backed Second Brain, retrieve the relevant account or project context, and produce a review-ready brief, proposal, or research artifact. When a process becomes repeatable, I turn the instructions and review rules into a reusable skill.
>
> The biggest shift is that the unit of work is no longer one prompt and one answer. It becomes an operating loop around persistent context, tools, verification, and a concrete artifact I can inspect.
>
> I still retain approval over customer-facing, legal, pricing, commercial, and other consequential decisions. Codex removes the manual searching and blank-page work while leaving judgment with me.

**Raw-source basis:** Condensed from Seth's canonical Codex daily-driver answer in the comprehensive answer bank. This is a personal-use account; current product availability and interface details remain subject to official verification.

### 49. How have you connected an AI system to a real operational or commercial outcome?

> One operational outcome I measured in my company-brain and GTM workspace was proposal-preparation cycle time.
>
> Before the system, a typical proposal involved roughly 30 minutes gathering account and deal context. Producing the first draft took approximately another 30 minutes.
>
> I built a workflow that retrieved the relevant source material, assembled the account context, and produced a source-backed first draft in roughly two minutes. I then spent around ten minutes reviewing the evidence, correcting the draft, and making the commercial decisions.
>
> Those are internally observed estimates from my own workflow, not a universal benchmark. The value was also broader than speed: outputs became more consistent, the supporting sources were easier to inspect, and customer-facing decisions remained with the human operator.
>
> That shaped how I evaluate enterprise AI. I would measure the time and quality of the reviewed business outcome—along with errors, rework, adoption, and downstream impact—rather than celebrating how quickly the model generated something.

**Source boundary:** The timing figures are Seth's internally observed estimates preserved in the comprehensive answer bank. They are safe as a bounded personal-workflow comparison, not as an audited study, universal time-saving percentage, or verified revenue result.

---

## Part VI — Reserve OpenAI Product-Fluency Answers

These are important coverage questions, but they are less likely than the first eleven to lead the 30-minute panel. Keep the answer durable and confirm current packaging before using plan-specific detail.

### 50. How would you explain ChatGPT Business versus ChatGPT Enterprise?

> ChatGPT Business and ChatGPT Enterprise are both managed ChatGPT workspaces for organizations. The main distinction is the complexity of the deployment.
>
> Business fits a team or growing company that wants to adopt a shared, secure workspace quickly with essential administration. Enterprise becomes relevant when the customer is coordinating a broader organizational rollout with more business units, centralized identity and user management, deeper governance and reporting requirements, and a formal security, procurement, support, or deployment process.
>
> For example, a growing company that wants one managed workspace for its employees may fit Business. A global bank rolling ChatGPT out across multiple regions, employee groups, and regulatory environments is more likely to require an Enterprise conversation.
>
> I would qualify the customer on rollout scope, identity and provisioning, data and security requirements, governance and reporting, procurement, support, and change management. Then I would verify the current plan-specific controls rather than reciting a feature checklist from memory.
>
> The seller takeaway is that Business is a straightforward organizational adoption surface, while Enterprise is an organization-wide deployment motion. I would also clarify that a ChatGPT workspace subscription and API usage are separate commercial surfaces.

**Raw-source basis:** The durable buyer distinction is condensed from the current [OpenAI pricing documentation](https://learn.chatgpt.com/docs/pricing), the [ChatGPT Enterprise page](https://chatgpt.com/business/enterprise/), and the captured [workspace-agents announcement](https://openai.com/index/introducing-workspace-agents-in-chatgpt/). Exact features, entitlements, pricing, and controls should be verified before an interview.

### 51. What is the Responses API?

> The Responses API is an OpenAI building surface for developers who want to put model capabilities inside their own product or workflow.
>
> The application sends the model input and instructions. The model produces an answer and, when appropriate, can use OpenAI-hosted tools or request a customer-defined function to retrieve information or complete a bounded step.
>
> For example, a support application could send in a customer's question, let the model search approved support content, and request an account lookup through a function. For a customer-defined function, the customer's application validates whether the request is authorized, executes it, and sends the result back so the model can produce the final response.
>
> The important business distinction is that the Responses API supplies model and tool capabilities, while the customer still owns the application experience, authentication, business logic, permissions, approval gates, data handling, evals, and success metric. ChatGPT is a finished user workspace; the Responses API is a developer surface for building AI into the customer's own experience.

**Simple flow:**

1. The application sends input, instructions, and the tools the model may use.
2. The model answers directly or requests an approved tool.
3. An OpenAI-hosted tool runs on the platform, or the customer's application validates and executes its own function.
4. The model uses the tool result to produce the final response or request another permitted step.

**Reference definition:**

> **Customer-defined function:** A capability described to the model but implemented and executed by the customer's application—for example, looking up an account, checking inventory, or creating a support ticket. The model requests the call; the application controls whether and how it runs.

**Raw-source basis:** Condensed from the current [Responses API overview](https://developers.openai.com/api/reference/responses/overview), [function-calling guide](https://developers.openai.com/api/docs/guides/function-calling#how-it-works), and the captured [one-year Responses API retrospective](https://developers.openai.com/blog/one-year-of-responses/). Current tool availability and execution behavior should be verified before an interview.

### 52. What are Structured Outputs, and why do they matter?

> Structured Outputs let a developer define the exact shape the model must return. Instead of receiving unpredictable free text, the application specifies required fields, data types, allowed values, and nested objects through a schema.
>
> For example, an account-qualification workflow might require `account_fit`, an array of `evidence`, identified `risks`, and a permitted `next_step`. Because every successful response follows that structure, the application can reliably display it, validate it, route it, or write approved fields into a CRM without trying to extract information from a paragraph.
>
> The important limitation is that Structured Outputs guarantee the shape, not the truth. The model can still place an incorrect account classification or unsupported claim inside a perfectly valid field. You still need source grounding, application-level validation, evals, and human review for consequential decisions.
>
> The business value is more reliable automation between the AI and existing systems, with fewer formatting errors and less custom parsing.

**Reference definition:**

> **Schema:** A contract that defines which fields must appear, what type of data each field may contain, which values are allowed, and how the fields are organized.

**Simple example:**

Unstructured answer:

> This account looks promising, although procurement risk remains. We should probably arrange technical discovery.

Structured answer:

```json
{
  "account_fit": "high",
  "evidence": ["Relevant workflow identified"],
  "risks": ["Procurement requirements unknown"],
  "next_step": "technical_discovery"
}
```

The application can reliably process the second answer. It still needs to verify that the evidence and classification are correct.

**Raw-source basis:** Condensed from [current OpenAI Structured Outputs documentation](https://developers.openai.com/api/docs/guides/structured-outputs) and a captured [Jerry Liu explanation](https://x.com/jerryjliu0/status/2009784608590873075). This is a source-faithful synthesis, not a claim that schema compliance guarantees factual accuracy.

### 53. How would you explain company knowledge, apps, or connected sources?

> Company knowledge lets an AI retrieve relevant information from approved internal sources instead of relying only on generic model knowledge or asking employees to copy and paste everything into the conversation.
>
> An app or connection is the path into a system such as a document repository, CRM, support platform, or other business application. It may let the AI search and retrieve information, or it may expose additional tools that can take actions. Those are different permission boundaries: being allowed to read an account record should not automatically mean being allowed to update it.
>
> For example, before an account review, the AI could combine the current opportunity status, recent support issues, product usage, and relevant correspondence into one sourced summary. If the user then asks it to update the CRM or send a message, that becomes an action and may require separate authorization or approval.
>
> The business value is less tab-switching and manual copy-paste, with more complete context around the decision. The enterprise questions are whether the sources are authoritative and fresh, whether the system respects each user's existing permissions, whether answers provide traceable sources, and which actions require confirmation.
>
> I would verify the current product name, plan availability, synchronization behavior, administrative controls, and action permissions before making a customer-specific claim.

**Reference distinction:**

| Concept | What it provides | Primary control |
|---|---|---|
| Company knowledge | Relevant internal information | Sources, freshness, permissions, citations |
| App or connected source | Access path into another system | Authentication and permitted capabilities |
| Read tool | Search or retrieve information | User and source-system permissions |
| Action tool | Change or trigger something | Separate authorization, approval, and audit trail |

**Raw-source basis:** Condensed from captured agent-harness and connected-system explanations plus [current OpenAI MCP and apps documentation](https://developers.openai.com/api/docs/mcp). This is a source-faithful synthesis, not a promise that every app supports the same retrieval, synchronization, action, or administrative behavior.

### 54. How would you handle security, privacy, administration, and spend questions?

> I would avoid treating “Is it secure?” as a single yes-or-no question. I would structure the conversation around four flows: data, access, actions, and spend.
>
> First, follow the data: what information enters the system, where it is processed and retained, whether it is used for training, how it is encrypted, and whether the customer has residency or regulated-data requirements.
>
> Second, follow the access: how users are authenticated and provisioned, what roles they have, and whether the AI respects their permissions in the underlying source systems.
>
> Third, follow the action: which tools are read-only, which can write or trigger something, what requires approval, what is logged, and who owns incident response. Permission to read a policy should never automatically mean permission to change an account.
>
> Finally, follow the spend: who can consume usage, how administrators monitor it, which limits or alerts are required, and whether cost is being measured against a successfully completed business outcome.
>
> I can structure those requirements and explain the relevant control categories, but I would verify the exact surface, plan, configuration, region, and contract against current official documentation and bring in the appropriate security or solutions specialist before making an assurance. Commercially, governance is what allows the customer to move from scattered experimentation to trusted adoption.

**Reference framework:**

| Flow | Core question | Typical requirements |
|---|---|---|
| Data | What enters the system, and where does it go? | Data use, training, retention, encryption, residency, regulated data |
| Access | Who can see which information? | Authentication, provisioning, roles, tenant isolation, source-system permissions |
| Actions | What can the system do, and who approves it? | Read versus write, tool scopes, approvals, audit logs, incident responsibility |
| Spend | Who can consume what, at what value? | Usage visibility, project or user controls, limits, alerts, cost per successful outcome |

**Raw-source basis:** Condensed from captured production-agent guidance, Garrett Lord's [evals and AI strategy article](https://x.com/garrettlord/status/2068754262440767500), [current OpenAI enterprise privacy guidance](https://learn.chatgpt.com/docs/enterprise/work-admin-faq#how-does-work-mode-support-enterprise-privacy-and-data-commitments), and [OpenAI Admin API documentation](https://developers.openai.com/api/docs/guides/admin-apis). This is a source-faithful synthesis, not a contractual assurance. Recheck the customer's surface, plan, configuration, features, region, and agreement.

### 55. How would you explain a production voice-agent system?

> A production voice agent is a tool-using agent with a live audio interface. The customer speaks through a phone or application, and the system listens, reasons, uses approved tools where needed, and responds in voice.
>
> There are two main architectures. A direct speech-to-speech system works with live audio and is usually the better fit for natural, low-latency conversation. A chained system converts speech to text, runs the text through the agent workflow, and converts the answer back into speech. That provides more control when you need visible transcripts, policy checks, deterministic logic, or approvals between stages.
>
> For example, an appointment-booking agent might understand the caller's request, verify the caller where required, check availability through a calendar tool, book the appointment, confirm it aloud, and transfer the caller to a person if it cannot complete the task safely.
>
> In production, I would evaluate three things: did it complete the customer's goal, did it follow the correct process and use the right tools, and did the conversation work under noise, silence, accents, and interruptions? The business metric is quality and cost per successfully completed outcome—not simply how human the voice sounds.

**Architecture reference:**

- **Direct speech-to-speech:** The model works with live audio input and output. Prioritize it when natural turn-taking, interruption handling, and low first-audio latency matter most.
- **Chained voice pipeline:** The application explicitly manages speech-to-text, the agent workflow, and text-to-speech. Prioritize it when intermediate transcripts, policy checks, replaceable stages, or approval-heavy logic matter more.

**Raw-source basis:** Condensed from [current OpenAI voice-agent documentation](https://developers.openai.com/api/docs/guides/voice-agents), Brooke Hopkins's [Coval interview](https://www.youtube.com/watch?v=eSm_9tb5ZbY), and OpenAI's [Perplexity voice case study](https://developers.openai.com/blog/realtime-api). This is a source-faithful synthesis, not a verbatim quotation. Recheck current architecture and SDK guidance before using implementation-specific detail.

---

## Part VII — Reusable Technical-Buyer Cards

### Product-routing card

| Customer situation | Likely starting surface | What to qualify |
|---|---|---|
| Broad employee productivity and internal knowledge work | Managed ChatGPT workspace | User groups, governance, data sources, adoption, measurable workflow |
| Engineering productivity and software-delivery work | Codex | Repository/task fit, developer adoption, review standards, permissions, cycle time |
| Customer-facing product or custom internal application | API, Responses, and tools | UX ownership, data flow, functions, state, latency, economics, evals |
| Current company knowledge | Retrieval/File Search or approved connected sources | Source authority, freshness, permissions, citations, retrieval evals |
| Repeatable shared internal workflow | Governed shared agent workflow | SOP, owner, tools, approvals, measurable destination, current availability |
| Stable systems orchestration | Workflow engine or deterministic service | Trigger, rules, retries, logging, credentials, system of record |
| Complex cross-functional transformation | Account team plus technical/deployment support | Executive sponsor, workflow value, systems, governance, change, eligibility |

### Business-value card

Use the customer's baseline. Do not import a generic benchmark.

| Value category | Example measures | Guardrail |
|---|---|---|
| Productivity | Cycle time, preparation time, throughput, capacity released | Quality and adoption |
| Revenue | Conversion, qualified pipeline, retention, expansion, speed to launch | Margin and attribution |
| Customer experience | First-contact resolution, response time, completion, satisfaction | Repeat contacts and escalation quality |
| Risk and quality | Error rate, citation accuracy, policy adherence, review exceptions | False confidence and missed escalation |
| Developer velocity | Lead time, review time, test coverage, maintenance throughput | Defects, security, developer trust |
| Economics | Cost per completed outcome, net savings, implementation cost | Ongoing review and operating burden |

### Technical-buyer discovery card

1. What exact workflow are we changing?
2. Who uses it, who owns the outcome, and who governs the risk?
3. What is the current baseline and cost of the problem?
4. Which sources and systems are authoritative?
5. What does the system need to read, decide, write, or trigger?
6. Which actions require confirmation or approval?
7. What are the common exceptions and unacceptable failures?
8. What would the eval set contain?
9. What metric and guardrail define success?
10. What proof would support a go, iterate, stop, coexist, or switch decision?

### Seller-versus-technical-partner boundary

**Seth should own:**

- plain-language concept explanations;
- workflow discovery;
- product-category routing;
- stakeholder and business-value translation;
- high-level architecture and risk questions;
- pilot hypothesis and decision criteria; and
- capturing open technical questions accurately.

**Bring in the relevant OpenAI specialist for:**

- customer-specific security and compliance commitments;
- data residency and regulated-data eligibility;
- networking, identity, permissions, and detailed architecture;
- exact packaging, entitlements, limits, pricing, or availability;
- benchmarks and migration design;
- custom deployment scope; and
- roadmap or contractual commitments.

---

## Part VIII — Truth And Freshness Boundaries

### Stable claims safe to rehearse

- LLM, token, context, embedding, RAG, agent, API, tool, structured output, eval, and fine-tuning concepts.
- Workflow-first discovery and product-fit logic.
- Agent-versus-deterministic-automation judgment.
- Prototype-versus-PoV-versus-production distinctions.
- Competitor diagnosis and coexistence posture.
- Business-value measurement from customer baselines.
- Seth's source-backed proof stories and explicit ownership boundaries.

### Claims that require a current official check

- model names, benchmarks, context limits, prices, and rate limits;
- ChatGPT Business, Enterprise, Edu, Codex, or shared-agent packaging;
- feature availability by plan, region, or customer;
- security, compliance, retention, privacy, and data-residency details;
- regulated-data eligibility and contractual terms;
- deployment-support eligibility, scope, and commercial terms; and
- competitor feature comparisons.

> [!warning] Seller-safe rule
> If the question could create a contractual, security, or implementation commitment, say what is directionally true, label what needs confirmation, and bring in the appropriate OpenAI specialist.

### Evidence basis for the Q8–Q44 research pass

The 2026-07-21 pass evaluated every answer independently against the canonical recruiter strategy, the hiring-leader debrief, the comprehensive answer bank, and full local sources retrieved from Seth Second Brain. The paths below are relative to `/Users/sethlim/Documents/Seth Second Brain/`. The most-used evidence clusters were:

- `wiki/llm-foundations/llm-foundations.md` for RAG, tools, evals, and fine-tuning boundaries;
- `wiki/gtm-sales/high-signal-enterprise-sales.md` for buyer-owned proof, baselines, and business-value logic;
- `wiki/gtm-sales/openai-enterprise-product-framing.md` for workspace, Codex, shared-workflow, and API routing;
- `wiki/ai-coding/harness-engineering-and-runtime-control.md` for managed-versus-custom and multi-provider ownership tradeoffs;
- `wiki/ai-knowledge-work/auditable-structured-document-extraction.md` for source grounding, review, and production measurement;
- captured official OpenAI material under `raw/intentional/web/` for tools, agents, Codex, workspace agents, and current platform terminology; and
- the Sunder architecture sources named in Q44–Q45 for workflow state, provenance, validation, review, and Seth's ownership boundary.

These sources support the decision frameworks and examples. They do not override the current-product freshness rule below, and source-backed architecture patterns should not be presented as audited customer outcomes unless the answer contains that explicit boundary.

### Official verification basis checked on 2026-07-21

- [OpenAI API documentation](https://developers.openai.com/api/docs)
- [Model optimization](https://developers.openai.com/api/docs/guides/model-optimization)
- [Using tools](https://developers.openai.com/api/docs/guides/tools)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [MCP and connectors](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)
- [Agents SDK](https://developers.openai.com/api/docs/guides/agents)
- [Working with evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [What is ChatGPT Enterprise?](https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise)
- [ChatGPT Business FAQ](https://help.openai.com/en/articles/8542115-chatgpt-business-faq)
- [Security and privacy at OpenAI](https://openai.com/security-and-privacy/)
- [ChatGPT business pricing and plan comparison](https://openai.com/business/pricing/)

These links support the broad product boundaries in this pack. Recheck them before using plan-specific or customer-specific detail live.

## Final Rehearsal Rule

For every answer, Seth should be able to deliver:

1. a one-sentence direct answer;
2. one clear explanation or useful, accurate metaphor;
3. one customer workflow;
4. the fit and non-fit boundary;
5. one business outcome;
6. one risk or control; and
7. the next proof step.

The goal is not to sound like the most technical person in the room. The goal is to sound like the seller whom technical and commercial buyers both trust to move the decision forward.

