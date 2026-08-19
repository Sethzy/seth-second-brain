---
type: wiki_article
title: Seedance 2 API Provider Selection
created_at: 2026-07-21
updated_at: 2026-07-21
reviewed_at: 2026-07-21
status: active
decision: APIYI
decision_date: 2026-07-21
source_count: 17
tags:
  - workflow-hustle
  - landing-pages
  - ai-video
  - seedance
  - api-providers
  - vendor-risk
related:
  - "[[AI Services Lead Generation]]"
  - "[[Autonomous Websites And Landing Pages]]"
---

# Seedance 2 API Provider Selection

> Point-in-time research snapshot reviewed 2026-07-21. Provider capabilities, prices, policies, and routes can change without notice. Direct vendor documentation is evidence of what a vendor claims, not independent confirmation of authorization, security, or upstream identity.

## Decision Context

Seth's homepage-concept lead magnet needs one high-quality cinematic set piece without turning every concept into a full video-production project. Seedance 2 is a candidate for generating controlled hero video from approved first/last frames or reference assets. The provider should expose enough creative control for that workflow while keeping experimentation affordable and avoiding unnecessary operational, privacy, or continuity risk.

This page compares the official route and third-party API relays discussed for that job. **Working decision: use APIYI as the primary Seedance 2 provider for this project.** APIYI still needs to pass the controlled technical test before prospect-facing use. CCAPI remains a synthetic low-cost benchmark, and the official route remains the production fallback if APIYI's quality, retention, isolation, billing, or continuity is unacceptable.

Related operating context:

- [AI Services Lead Generation](ai-services-lead-generation.md) defines the personalized homepage as free proof of work that earns an AI workflow conversation.
- [Autonomous Websites And Landing Pages](../marketing/autonomous-websites-and-landing-pages.md) treats a landing page as a campaign object with source evidence, audience, offer, review, distribution, and measurement.

## Terminology And Evidence Standard

"Grey-risk provider" means a reseller, relay, account pool, proxy, or white-label storefront whose authorization, upstream routing, corporate identity, data handling, or customer isolation is not fully clear. It does not mean the provider has been proven unlawful.

Provider claims are separated from observed facts:

- **Documented:** present in a current vendor API specification, policy, pricing page, or live pricing response.
- **Vendor claim:** asserted by the provider but not independently confirmed.
- **Inference:** a conclusion from matching model IDs, fields, sample assets, error shapes, prices, or storefront structure.
- **Unknown:** not established by the reviewed public material.

## Active Decision

**Selected provider: APIYI.**

This is a reversible implementation choice, not an exclusive long-term commitment. New integration work should target APIYI behind a provider adapter, retain enough normalized task metadata to support migration, and avoid depending on APIYI-specific behavior outside the adapter.

### Best legitimacy-to-accessibility balance: APIYI

APIYI is the strongest initial candidate because it combines a named operator, detailed Seedance-specific documentation, primary and backup endpoints, a published refund policy, a stated logging policy, full creative controls, and explicit billing behavior. Its Seedance specification covers text-to-video, first-frame, first-and-last-frame, and multimodal reference workflows; 480p, 720p, and 1080p on the standard model; 4-15 second clips; synchronized audio; asynchronous jobs; and rejected-request billing behavior.

APIYI says it uses official mainland Volcengine resources. This is a vendor claim, not independent proof that ByteDance or Volcengine authorizes APIYI as a reseller. Its ordinary price is described as being near official Volcengine list pricing, with potential savings through recharge bonuses. Seedance 2 Mini is described as roughly half the standard model's price. Therefore APIYI is not the lowest-cost option; it is the current best compromise between creative capability, documentation, recourse, and price.

### Cheapest credible experiment: CCAPI

CCAPI documents a Volcengine-compatible Seedance 2 endpoint with the full model identifier `doubao-seedance-2-0-260128`. Its documented route supports first-frame, first-and-last-frame, and multimodal reference generation, with 4-15 second clips at 480p or 720p. Its published rates are ¥8 per million tokens without generated audio and ¥16 per million with audio.

For a 10-second, 720p, 16:9 job, CCAPI's documented formula produces this estimate:

```text
1280 × 720 × 10 seconds × 24 ÷ 1024
= 216,000 tokens

216,000 × ¥8 ÷ 1,000,000
= ¥1.728 without generated audio

216,000 × ¥16 ÷ 1,000,000
= ¥3.456 with generated audio
```

The unusually low headline price makes CCAPI useful as a benchmark. Publicly reviewed material did not establish an equally clear legal operator, refund policy, privacy policy, or independent upstream authorization. It should receive only a minimum balance and synthetic, non-sensitive test assets until those gaps are resolved.

## Provider Landscape

| Provider | Observed route or positioning | Price signal | Legitimacy and operational signal | Current treatment |
|---|---|---|---|---|
| Official Volcengine / BytePlus | First-party Seedance API | Baseline; verify live regional price before purchase | Highest upstream clarity; regional onboarding and billing may create friction | Production benchmark |
| APIYI / API易 | Claims official mainland Volcengine resources through its relay | Near official list price; recharge bonuses; Mini about half standard price | Named operator, detailed docs, refund and logging policies, backup endpoint | **Selected primary provider; validation pending** |
| CCAPI.ai | Volcengine-compatible Chinese relay | ¥8/M silent; ¥16/M with audio; about ¥1.73/¥3.46 for the worked 10s example | Strong technical docs; weak public legal and privacy transparency in reviewed material | **Cheap benchmark only** |
| 302.AI | Multi-model Volcengine proxy | Standard no-input-video route documented at 7.884 PTC/M; 1 PTC is documented as US$1 | Mature API/help surface and terms; restrictive normal-top-up refund posture; not meaningfully cheaper than official international pricing | Accessible fallback, not value leader |
| KIE.ai | Multi-model commercial API marketplace | Live backend observed at $0.205/s standard 720p without video input, $0.165/s Fast, and $0.1025/s Mini; the $0.057/s headline applies to a narrower 480p/video-input case | Polished surface but unclear official partnership status | Convenient but expensive for first/last-frame work |
| Yunwu API | Chinese model marketplace with supplier groups | Screenshot showed Seedance 1.x/1.5 listings and supplier labels; no verified Seedance 2 offer during this review | Supplier routing and group semantics are opaque | Recheck only if dashboard adds exact Seedance 2 model ID |
| Seedance2.ai | Single-model branded storefront | Credits per second are visible, but public USD conversion was not sufficiently auditable | Polished async API, webhooks, conditional refund policy; terms do not clearly identify a conventional legal entity and address | Small-balance backup experiment |
| Tikdek | Commercial Seedance API storefront | Matches KIE's credit economics and model ID | Exact KIE-like fields, prices, and sample assets suggest shared or white-label infrastructure; inference, not proof | Skip as diversification if KIE is already tested |
| API Atlas | Independent aggregator used as a price comparison in the research | Previously observed around $0.112/s for the relevant class of route; reverify live quote | More conventional aggregator comparison point, but not part of the grey-provider shortlist | Price benchmark only |
| 3AToken, V-API, Cloudpass, Tokaify, 星辰, FastCode, VectorEngine, 云算API, 无限API | Long-tail Chinese relay listings discovered through Hvoy | Published units and group prices are inconsistent and not safely comparable without checkout tests | Several listings repeat `纯AZ`/`官转` groups and identical prices, suggesting shared upstreams or cloned catalogues | Discovery watchlist, not approved |
| DMXAPI, 兔子中转, TopMix, AIOM, DuomiAPI, GeekAI, aipaiai.cn, SenseAudio, LaoZhang API | Additional relays or reseller storefronts found during the search | Mixed per-second, per-token, or absent pricing | Evidence quality varies; several are more expensive than the strongest shortlist or lack enough public documentation | Do not prioritize |

## Why APIYI Currently Leads

APIYI wins this comparison on the combination rather than any single claim:

1. **Creative surface:** first/last frame, first frame, multimodal reference images/video/audio, model-selected or fixed duration, multiple aspect ratios, and up to 1080p on the standard model cover the intended cinematic homepage workflow.
2. **Operational specificity:** the documentation names exact endpoints, model behavior, task states, output expiry, billing timing, limitations, and a backup hostname.
3. **Commercial recourse:** the public terms name MrrBase, LLC, and the refund page describes a 30-day unused-balance process with payment-method conditions.
4. **Data posture:** APIYI says it does not retain customer input/output content by default. This needs empirical and contractual verification before sensitive client use.
5. **Price honesty:** APIYI does not advertise an implausibly large standard-model discount. It says pricing is near the official route and positions Mini and recharge bonuses as the savings mechanisms.

The unresolved weakness is authorization. "Official Volcengine Mainland China resource" could describe the upstream model rather than an authorized reseller relationship. No reviewed independent partner directory or first-party statement confirms the commercial relationship.

## Why The Cheapest Provider Does Not Lead

CCAPI's documented price is compelling, but price alone does not answer:

- Who operates the service and which jurisdiction governs disputes?
- Is the upstream account authorized for resale and stable under load?
- Are prompts, source assets, generated videos, credentials, and task metadata logged?
- Are customers isolated from one another?
- What happens to prepaid funds if the route disappears?
- Does the published price apply to the exact account group available after top-up?
- Are failed jobs automatically credited in practice?

Until those questions have verified answers, CCAPI is suitable for non-sensitive experiments, not prospect production.

## Duplicate-Upstream Risk

Nominal provider count overstates actual redundancy. Matching model identifiers, request fields, credit rates, sample assets, CDN hosts, supplier-group names, error messages, or task schemas can indicate that multiple storefronts share the same upstream or white-label platform. Tikdek's close match with KIE and the repeated `纯AZ`/`官转` listings in the Chinese relay directory are specific warning signs. These are inferences, not proof.

Two storefront accounts should not be treated as two fallback providers until a controlled test shows different upstream characteristics or a provider discloses the relationship.

## Controlled Provider Test

No prospect-specific or sensitive assets should be used in the first evaluation. The minimum test uses synthetic frames and a safe prompt.

### Standard fixture

- 5 seconds.
- 720p, 16:9.
- First and last frame supplied.
- Generated audio off.
- Identical prompt and source files for every provider.
- No faces, client logos, private facilities, unreleased products, or customer data.

### Measurements

- Quoted price before submission and actual balance deduction after completion.
- Whether the correct model ID is accepted.
- Queue time, generation time, success rate, and retry behavior.
- First-frame fidelity, last-frame fidelity, temporal coherence, camera control, artifacts, text/logo corruption, and watermarking.
- Whether failed or rejected tasks are charged and how quickly credit returns.
- Output URL hostname, expiry, and whether the file remains accessible after the stated window.
- Request/response schema, task IDs, error text, and CDN behavior for shared-upstream clues.
- Support response to one technical and one billing question.

### Initial test sequence

1. Add only the minimum viable balance to the selected APIYI account after operator approval.
2. Run three safe fixtures: first-frame, first-and-last-frame, and multimodal reference.
3. Repeat the first-and-last-frame fixture through CCAPI with the minimum viable balance.
4. Compare quality and realized cost rather than advertised cost.
5. Ask both vendors, in writing, about operator identity, upstream authorization, asset retention, log retention, customer isolation, refunds, and model/version continuity.
6. Confirm APIYI for prospect-facing use or fall back to the official route if any approval criterion fails.

## Project Integration Guardrails

- Wrap video generation behind a provider adapter so the landing-page builder does not depend on one vendor's request schema.
- Record provider, exact model ID, prompt, input hashes, parameters, generation timestamp, task ID, billed amount, and output provenance for every accepted clip.
- Treat generated footage as concept material, not evidence about the prospect.
- Require operator approval before media spend and before hosting a generated concept.
- Use a poster frame, reduced-motion presentation, and non-video fallback on every homepage concept.
- Keep client assets out of grey-risk routes until retention, isolation, and contractual use rights are acceptable.
- Do not count multiple storefronts as redundancy without testing for shared upstream infrastructure.

## Operational Approval Gate

APIYI is the selected primary provider, but it is not yet approved for prospect-facing assets or sensitive inputs. Operational approval requires:

- Successful first/last-frame and reference-video tests at acceptable quality.
- Realized price within the pre-agreed per-concept media budget.
- A satisfactory answer on asset retention and customer isolation.
- Confirmed failed-job credit behavior.
- A provider-independent adapter and fallback path.
- Operator approval for top-up, generation spend, and any prospect-facing use.

## Source Registry

### Primary and vendor documentation

- [Volcengine Seedance 2 API launch notice](https://developer.volcengine.com/articles/7628567056649125942)
- [APIYI Seedance 2 overview](https://docs.apiyi.com/en/api-capabilities/seedance2/overview)
- [APIYI Seedance 2 video-generation specification](https://docs.apiyi.com/en/api-capabilities/seedance2/video-generation)
- [APIYI Seedance 2 Mini launch and billing verification](https://docs.apiyi.com/en/live/2026-07/seedance2-mini-launch)
- [APIYI refund policy](https://docs.apiyi.com/faq/refund-policy)
- [APIYI logging policy](https://docs.apiyi.com/en/faq/user-logs-control)
- [APIYI terms](https://cf-index.apiyi.com/terms)
- [CCAPI Seedance documentation](https://ccapi.ai/docs/zh)
- [302.AI Seedance pricing](https://doc.302.ai/437932283e0)
- [302.AI pricing-unit help](https://help.302.ai/en/docs/liao-tian-ji-qi-ren-jia-ge)
- [302.AI refund policy](https://302.ai/refund-policy)
- [Seedance2.ai API documentation](https://seedance2.ai/zh/api-docs)
- [Seedance2.ai pricing](https://seedance2.ai/zh/pricing)
- [Seedance2.ai terms](https://seedance2.ai/zh/terms-of-service)
- [Tikdek Seedance 2 API](https://tikdek.com/seedance-2-0-api)
- [Yunwu Seedance pricing search](https://yunwu.ai/pricing?keyword=seedance)

### Discovery directories and weaker secondary evidence

- [Hvoy Seedance 2 relay directory](https://www.hvoy.ai/models/seedance-2-0/)

Directory listings are discovery leads only. Their provider counts, prices, verification badges, and route descriptions require direct confirmation before use.

## Open Questions

- What is APIYI's exact realized cost for the project's standard 5-second and 10-second first/last-frame fixtures?
- Does APIYI have written authorization to resell or proxy the mainland Volcengine route?
- Does APIYI's no-content-retention statement cover access logs, metadata, upstream providers, backups, and abuse-review copies?
- Can CCAPI identify its legal operator and publish enforceable retention and refund terms?
- Does Seedance 2 Mini meet the visual-quality bar for a cinematic homepage hero, or is Fast/standard necessary?
- Which independent fallback provides genuinely separate upstream infrastructure?
