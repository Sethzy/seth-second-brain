---
type: staging_digest
title: "YC Company Scan Validation"
generated_at: 2026-06-24T08:52:10.865Z
status: staged
trust_lane: staging
---

# YC Company Scan Validation

## Summary

- API metadata last updated: 2026-06-24T02:27:39.599Z.
- Companies in scope: 1642.
- Rows missing required fields: 0.
- Rows with fallback descriptions because YC source description was missing: 7.
- Rows missing category: 0.
- Official YC URL spot checks attempted: 20.
- Official YC URL spot checks passed: 20.
- S26 cross-check status: passed.
- S26 rows in yc-oss/api: 28.
- S26 rows in official YC directory: 31.
- S26 directory-only rows added: 3.

## Batch Count Check

| Batch | Local Rows | Metadata Count | Official Directory Count | Match Metadata |
|---|---:|---:|---:|---|
| Winter 2024 | 249 | 249 |  | yes |
| Summer 2024 | 248 | 248 |  | yes |
| Fall 2024 | 94 | 94 |  | yes |
| Winter 2025 | 167 | 167 |  | yes |
| Spring 2025 | 143 | 143 |  | yes |
| Summer 2025 | 166 | 166 |  | yes |
| Fall 2025 | 149 | 149 |  | yes |
| Winter 2026 | 198 | 198 |  | yes |
| Spring 2026 | 197 | 197 |  | yes |
| Summer 2026 | 31 | 28 | 31 | no |

Summer 2026 local rows can exceed metadata because this run supplements `yc-oss/api` with official YC directory rows found by the fallback cross-check.

## Category Coverage

| Category | Rows |
|---|---:|
| GTM / Revenue Ops | 170 |
| Document / Legal / Claims | 98 |
| CRM / Work Surface | 167 |
| Vertical Ops / Order / ERP | 200 |
| Healthcare Admin | 143 |
| Compliance / Evals / Runtime | 96 |
| Agent Infrastructure | 594 |
| Other / Skip | 174 |

## Official YC Spot Checks

| Result | Company | Batch | Status | URL |
|---|---|---|---:|---|
| pass | 14.ai | Winter 2024 | 200 | [YC](https://www.ycombinator.com/companies/14-ai) |
| pass | Marblism | Winter 2024 | 200 | [YC](https://www.ycombinator.com/companies/marblism) |
| pass | &AI | Summer 2024 | 200 | [YC](https://www.ycombinator.com/companies/ai-2) |
| pass | Mineflow | Summer 2024 | 200 | [YC](https://www.ycombinator.com/companies/mineflow) |
| pass | Abundant | Fall 2024 | 200 | [YC](https://www.ycombinator.com/companies/abundant) |
| pass | Kilvin | Fall 2024 | 200 | [YC](https://www.ycombinator.com/companies/kilvin) |
| pass | 10x | Winter 2025 | 200 | [YC](https://www.ycombinator.com/companies/10x) |
| pass | Mastra | Winter 2025 | 200 | [YC](https://www.ycombinator.com/companies/mastra) |
| pass | Acolite | Spring 2025 | 200 | [YC](https://www.ycombinator.com/companies/acolite) |
| pass | Labric | Spring 2025 | 200 | [YC](https://www.ycombinator.com/companies/labric) |
| pass | Acrely | Summer 2025 | 200 | [YC](https://www.ycombinator.com/companies/acrely) |
| pass | MangoDesk | Summer 2025 | 200 | [YC](https://www.ycombinator.com/companies/mangodesk) |
| pass | Absurd | Fall 2025 | 200 | [YC](https://www.ycombinator.com/companies/absurd) |
| pass | Lunavo | Fall 2025 | 200 | [YC](https://www.ycombinator.com/companies/lunavo) |
| pass | 10x Science | Winter 2026 | 200 | [YC](https://www.ycombinator.com/companies/10x-science) |
| pass | Maven | Winter 2026 | 200 | [YC](https://www.ycombinator.com/companies/maven) |
| pass | 9 Mothers | Spring 2026 | 200 | [YC](https://www.ycombinator.com/companies/9-mothers-corporation) |
| pass | Lab0 | Spring 2026 | 200 | [YC](https://www.ycombinator.com/companies/lab0) |
| pass | Agentcard | Summer 2026 | 200 | [YC](https://www.ycombinator.com/companies/agentcard) |
| pass | LATO | Summer 2026 | 200 | [YC](https://www.ycombinator.com/companies/lato) |

## Summer 2026 Directory Cross-Check

- Directory URL: [Summer 2026](https://www.ycombinator.com/companies?batch=Summer%202026).
- Fallback scraper reference: [corralm/yc-scraper](https://github.com/corralm/yc-scraper).
- Missing from yc-oss/api: 3.
- Missing from official directory: 0.

| Added Company | YC URL | One-Liner |
|---|---|---|
| Insurf | [YC](https://www.ycombinator.com/companies/insurf) | The AI-Native Decision Infrastructure for Health Insurance |
| Markov | [YC](https://www.ycombinator.com/companies/markov) | Data for computer-use ai |
| Parasma | [YC](https://www.ycombinator.com/companies/parasma) | Training human brain cells for AI compute |

