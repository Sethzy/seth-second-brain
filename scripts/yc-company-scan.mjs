#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { execFile } from "node:child_process";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);

const RECENT_BATCHES = [
  "Winter 2024",
  "Summer 2024",
  "Fall 2024",
  "Winter 2025",
  "Spring 2025",
  "Summer 2025",
  "Fall 2025",
  "Winter 2026",
  "Spring 2026",
  "Summer 2026",
];

const OUTPUT_DIR = "staging/yc-company-scan";
const COMPANIES_URL = "https://yc-oss.github.io/api/companies/all.json";
const META_URL = "https://yc-oss.github.io/api/meta.json";
const OFFICIAL_COMPANIES_URL = "https://www.ycombinator.com/companies";
const S26_DIRECTORY_URL = "https://www.ycombinator.com/companies?batch=Summer%202026";
const YC_OSS_REPO = "https://github.com/yc-oss/api";
const YC_SCRAPER_FALLBACK = "https://github.com/corralm/yc-scraper";
const SOURCE_MAP_PATH = "state/source-map.json";
const AGENT_BROWSER_SESSION = "yc-s26-crosscheck";
const AGENT_BROWSER_ALLOWED_DOMAINS =
  "www.ycombinator.com,bookface-static.ycombinator.com,fonts.googleapis.com,fonts.gstatic.com,*.algolia.net";

const CATEGORY_RULES = [
  {
    id: "gtm-revenue-ops",
    label: "GTM / Revenue Ops",
    terms: [
      "sales",
      "revenue",
      "gtm",
      "go-to-market",
      "outbound",
      "lead",
      "prospect",
      "crm",
      "customer engagement",
      "salesforce",
      "marketing automation",
      "pipeline",
      "account intelligence",
      "growth",
    ],
  },
  {
    id: "document-legal-claims",
    label: "Document / Legal / Claims",
    terms: [
      "document",
      "pdf",
      "ocr",
      "invoice",
      "receipt",
      "contract",
      "legal",
      "lawyer",
      "paralegal",
      "claims",
      "evidence",
      "forms",
      "filing",
      "paperwork",
      "dossier",
      "redaction",
    ],
  },
  {
    id: "crm-work-surface",
    label: "CRM / Work Surface",
    terms: [
      "crm",
      "workspace",
      "work surface",
      "copilot",
      "assistant",
      "agent",
      "workbench",
      "second brain",
      "knowledge base",
      "notetaking",
      "meeting",
      "task",
      "workflow",
      "project management",
    ],
  },
  {
    id: "vertical-ops-order-erp",
    label: "Vertical Ops / Order / ERP",
    terms: [
      "erp",
      "order",
      "orders",
      "procurement",
      "supply chain",
      "warehouse",
      "inventory",
      "logistics",
      "freight",
      "manufacturing",
      "restaurant",
      "food",
      "operations",
      "back office",
      "vendor",
      "purchase",
      "quality system",
    ],
  },
  {
    id: "healthcare-admin",
    label: "Healthcare Admin",
    terms: [
      "healthcare",
      "health care",
      "clinic",
      "medical",
      "patient",
      "hospital",
      "radiology",
      "dental",
      "revenue cycle",
      "insurance",
      "payer",
      "prior authorization",
      "claims",
      "pharmacy",
      "provider",
      "clinical",
    ],
  },
  {
    id: "compliance-evals-runtime",
    label: "Compliance / Evals / Runtime",
    terms: [
      "compliance",
      "eval",
      "evaluation",
      "observability",
      "audit",
      "monitoring",
      "guardrail",
      "runtime",
      "security",
      "risk",
      "governance",
      "identity",
      "permission",
      "trust",
      "regulated",
      "policy",
    ],
  },
  {
    id: "agent-infrastructure",
    label: "Agent Infrastructure",
    terms: [
      "agent",
      "agents",
      "llm",
      "inference",
      "model",
      "developer tools",
      "devtools",
      "api",
      "browser",
      "automation",
      "orchestration",
      "workflow automation",
      "tool",
      "sandbox",
      "memory",
      "rag",
      "vector",
    ],
  },
  {
    id: "other-skip",
    label: "Other / Skip",
    terms: [],
  },
];

const CATEGORY_ORDER = CATEGORY_RULES.map((rule) => rule.id);
const CATEGORY_LABELS = new Map(CATEGORY_RULES.map((rule) => [rule.id, rule.label]));

const SETH_ADJACENCY = [
  {
    key: "salescraft_gtm",
    label: "Salescraft / GTM",
    terms: [
      "sales",
      "revenue",
      "gtm",
      "outbound",
      "lead",
      "prospect",
      "crm",
      "customer engagement",
      "marketing",
      "account",
      "pipeline",
      "growth",
    ],
    points: 22,
  },
  {
    key: "sunder_docs",
    label: "Sunder / documents",
    terms: [
      "document",
      "pdf",
      "invoice",
      "contract",
      "legal",
      "claims",
      "evidence",
      "ocr",
      "forms",
      "paperwork",
      "review",
      "extraction",
    ],
    points: 24,
  },
  {
    key: "neo_bot_crm",
    label: "Neo Bot / AI CRM",
    terms: [
      "crm",
      "assistant",
      "agent",
      "meeting",
      "task",
      "client",
      "workflow",
      "follow-up",
      "relationship",
      "sales",
    ],
    points: 20,
  },
  {
    key: "gtm_workspace",
    label: "GTM Workspace / second brain",
    terms: [
      "workspace",
      "knowledge",
      "notion",
      "meeting",
      "workflow",
      "approval",
      "document",
      "operating system",
      "command center",
      "automation",
    ],
    points: 18,
  },
  {
    key: "zhao_orderops",
    label: "Zhao OrderOps",
    terms: [
      "order",
      "erp",
      "inventory",
      "warehouse",
      "food",
      "restaurant",
      "supplier",
      "logistics",
      "procurement",
      "supply chain",
      "invoice",
      "operations",
    ],
    points: 22,
  },
];

const POSITIVE_FACTORS = [
  {
    key: "singapore_start",
    label: "Singapore wedge",
    terms: [
      "singapore",
      "apac",
      "asia",
      "southeast asia",
      "global",
      "remote",
      "fintech",
      "logistics",
      "healthcare",
      "legal",
      "compliance",
      "manufacturing",
    ],
    points: 10,
  },
  {
    key: "non_enterprise_start",
    label: "Non-enterprise starting motion",
    terms: [
      "smb",
      "small business",
      "founder",
      "advisor",
      "broker",
      "clinic",
      "dentist",
      "law firm",
      "restaurant",
      "real estate",
      "operator",
      "team",
      "self-serve",
      "professionals",
    ],
    points: 12,
  },
  {
    key: "offshore_buildable",
    label: "Vietnam-offshore buildable",
    terms: [
      "workflow",
      "dashboard",
      "back office",
      "forms",
      "documents",
      "order",
      "invoice",
      "crm",
      "automation",
      "review",
      "data entry",
      "operations",
      "reporting",
    ],
    points: 10,
  },
  {
    key: "global_market",
    label: "Global market",
    terms: [
      "global",
      "worldwide",
      "remote",
      "b2b",
      "api",
      "platform",
      "workflow",
      "software",
      "operations",
      "finance",
      "healthcare",
      "legal",
    ],
    points: 8,
  },
];

const PENALTY_FACTORS = [
  {
    key: "deep_tech_or_research",
    label: "Deep-tech/research-heavy",
    terms: [
      "drug discovery",
      "therapeutics",
      "biotech",
      "protein",
      "robotics hardware",
      "aerospace",
      "defense",
      "semiconductor",
      "materials",
      "fusion",
      "battery",
      "quantum",
    ],
    points: -16,
  },
  {
    key: "enterprise_only",
    label: "Enterprise-only wedge risk",
    terms: [
      "enterprise",
      "fortune 500",
      "large enterprises",
      "security platform",
      "devsecops",
      "data infrastructure",
      "cloud infrastructure",
    ],
    points: -10,
  },
  {
    key: "consumer_or_creator",
    label: "Consumer/creator distraction",
    terms: [
      "consumer",
      "dating",
      "social",
      "game",
      "gaming",
      "creator",
      "music",
      "video",
      "fitness coach",
      "relationship app",
    ],
    points: -14,
  },
  {
    key: "capital_intensive",
    label: "Capital-intensive",
    terms: [
      "hardware",
      "robot",
      "drone",
      "manufacturing equipment",
      "factory",
      "medical device",
      "vehicle",
      "satellite",
    ],
    points: -12,
  },
];

function normalizeText(value) {
  if (value == null) return "";
  return String(value).replace(/\s+/g, " ").trim();
}

function normalizeYcUrl(value) {
  return normalizeText(value).replace(/\/$/, "");
}

function companyText(company) {
  return [
    company.name,
    company.website,
    company.one_liner,
    company.long_description,
    company.industry,
    company.subindustry,
    company.status,
    company.stage,
    ...(company.tags ?? []),
    ...(company.industries ?? []),
    ...(company.regions ?? []),
  ]
    .filter(Boolean)
    .map(normalizeText)
    .join(" ")
    .toLowerCase();
}

function countMatches(text, terms) {
  const matched = [];
  for (const term of terms) {
    const needle = term.toLowerCase();
    if (text.includes(needle)) matched.push(term);
  }
  return matched;
}

function classify(company) {
  const text = companyText(company);
  let best = { id: "other-skip", score: 0, matched: [] };
  for (const rule of CATEGORY_RULES) {
    if (!rule.terms.length) continue;
    const matched = countMatches(text, rule.terms);
    const score = matched.length;
    if (score > best.score) best = { id: rule.id, score, matched };
  }
  return best;
}

function scoreCompany(company, category) {
  const text = companyText(company);
  const matchedAdjacency = [];
  const matchedFactors = [];
  const riskFactors = [];
  let score = 0;

  for (const adjacency of SETH_ADJACENCY) {
    const matched = countMatches(text, adjacency.terms);
    if (matched.length > 0) {
      const points = Math.min(adjacency.points, 6 + matched.length * 4);
      score += points;
      matchedAdjacency.push({ label: adjacency.label, points, matched });
    }
  }

  for (const factor of POSITIVE_FACTORS) {
    const matched = countMatches(text, factor.terms);
    if (matched.length > 0) {
      const points = Math.min(factor.points, 4 + matched.length * 2);
      score += points;
      matchedFactors.push({ label: factor.label, points, matched });
    }
  }

  for (const penalty of PENALTY_FACTORS) {
    const matched = countMatches(text, penalty.terms);
    if (matched.length > 0) {
      const points = Math.max(penalty.points, penalty.points + Math.max(0, matched.length - 1) * -2);
      score += points;
      riskFactors.push({ label: penalty.label, points, matched });
    }
  }

  if (company.status === "Active") score += 4;
  if (company.stage === "Early") score += 3;
  if (company.isHiring) score += 3;
  if (company.top_company) score += 2;

  if (category.id === "other-skip") score -= 10;
  if (company.industry === "Consumer") score -= 7;

  return {
    score: Math.max(0, Math.min(100, Math.round(score))),
    matchedAdjacency,
    matchedFactors,
    riskFactors,
  };
}

function normalizeCompany(company, meta) {
  const category = classify(company);
  const scoring = scoreCompany(company, category);
  const oneLiner = normalizeText(company.one_liner);
  const longDescription = normalizeText(company.long_description);
  const description =
    oneLiner ||
    longDescription ||
    `${normalizeText(company.industry) || "Uncategorized"} YC company; description missing from source.`;
  return {
    id: company.id,
    name: normalizeText(company.name),
    website: normalizeText(company.website),
    description,
    one_liner: oneLiner,
    long_description: longDescription,
    batch: normalizeText(company.batch),
    industry: normalizeText(company.industry),
    subindustry: normalizeText(company.subindustry),
    tags: Array.isArray(company.tags) ? company.tags.map(normalizeText).filter(Boolean) : [],
    status: normalizeText(company.status),
    stage: normalizeText(company.stage),
    team_size: Number.isFinite(company.team_size) ? company.team_size : "",
    yc_url: normalizeText(company.url),
    primary_category: category.id,
    category_label: CATEGORY_LABELS.get(category.id),
    category_terms: category.matched,
    seth_fit_score: scoring.score,
    seth_adjacency: scoring.matchedAdjacency,
    fit_factors: scoring.matchedFactors,
    risk_factors: scoring.riskFactors,
    is_hiring: Boolean(company.isHiring),
    top_company: Boolean(company.top_company),
    source_description_missing: !oneLiner && !longDescription,
    source_origin: normalizeText(company.source_origin) || "yc-oss/api",
    api_last_updated: meta.last_updated,
  };
}

function csvEscape(value) {
  const str = Array.isArray(value) ? value.join("; ") : normalizeText(value);
  if (/[",\n\r]/.test(str)) return `"${str.replace(/"/g, '""')}"`;
  return str;
}

function toCsv(rows) {
  const headers = [
    "name",
    "website",
    "description",
    "one_liner",
    "long_description",
    "batch",
    "industry",
    "subindustry",
    "tags",
    "status",
    "stage",
    "team_size",
    "yc_url",
    "primary_category",
    "category_label",
    "seth_fit_score",
    "seth_adjacency",
    "fit_factors",
    "risk_factors",
    "is_hiring",
    "top_company",
    "source_description_missing",
    "source_origin",
  ];
  const lines = [headers.join(",")];
  for (const row of rows) {
    lines.push(
      headers
        .map((header) => {
          if (header === "seth_adjacency") return csvEscape(row.seth_adjacency.map((x) => x.label));
          if (header === "fit_factors") return csvEscape(row.fit_factors.map((x) => x.label));
          if (header === "risk_factors") return csvEscape(row.risk_factors.map((x) => x.label));
          return csvEscape(row[header]);
        })
        .join(","),
    );
  }
  return `${lines.join("\n")}\n`;
}

function mdEscape(value) {
  return normalizeText(value).replace(/\|/g, "\\|");
}

function truncate(value, length = 128) {
  const text = normalizeText(value);
  if (text.length <= length) return text;
  return `${text.slice(0, length - 1).trim()}...`;
}

function batchCounts(rows) {
  const counts = new Map();
  for (const row of rows) counts.set(row.batch, (counts.get(row.batch) ?? 0) + 1);
  return counts;
}

function categoryCounts(rows) {
  const counts = new Map();
  for (const row of rows) counts.set(row.primary_category, (counts.get(row.primary_category) ?? 0) + 1);
  return counts;
}

function renderScan(rows, meta, generatedAt, crosscheck) {
  const counts = batchCounts(rows);
  const catCounts = categoryCounts(rows);
  const partialNote = rows.some((row) => row.batch === "Summer 2026")
    ? "Summer 2026 is included but should be treated as partial and moving."
    : "Summer 2026 was not present in this run.";

  const lines = [];
  lines.push("---");
  lines.push("type: staging_digest");
  lines.push('title: "YC Recent Companies Scan"');
  lines.push(`generated_at: ${generatedAt}`);
  lines.push("status: staged");
  lines.push("source:");
  lines.push(`  - ${COMPANIES_URL}`);
  lines.push(`  - ${META_URL}`);
  lines.push("trust_lane: staging");
  lines.push("capture_quality: derived_from_public_api");
  lines.push("---");
  lines.push("");
  lines.push("# YC Recent Companies Scan");
  lines.push("");
  lines.push("This is a scan-first derived artifact from the open-source `yc-oss/api` dataset. It is not compiled wiki knowledge yet.");
  lines.push("");
  lines.push("## Source And Scope");
  lines.push("");
  lines.push(`- Primary source: [yc-oss/api](${YC_OSS_REPO}) via [companies/all.json](${COMPANIES_URL}).`);
  lines.push(`- API metadata endpoint: [meta.json](${META_URL}).`);
  lines.push(`- API last updated: ${meta.last_updated}.`);
  lines.push(`- Fallback if founder/profile fields are needed later: [corralm/yc-scraper](${YC_SCRAPER_FALLBACK}).`);
  lines.push(`- Summer 2026 cross-check: official YC directory rendered at [S26 directory](${S26_DIRECTORY_URL}) using the same link-extraction path as \`corralm/yc-scraper\`.`);
  if (crosscheck.status === "passed") {
    lines.push(
      `- S26 cross-check result: yc-oss/api had ${crosscheck.api_s26_count} S26 rows; official YC directory had ${crosscheck.directory_s26_count}; added ${crosscheck.added_from_directory_count} directory-only rows.`,
    );
  } else {
    lines.push(`- S26 cross-check result: ${crosscheck.status} (${crosscheck.error || "no error detail"}).`);
  }
  lines.push(`- Batch scope: ${RECENT_BATCHES.join(", ")}.`);
  lines.push(`- Companies in scope: ${rows.length}. ${partialNote}`);
  lines.push("");
  lines.push("## Batch Counts");
  lines.push("");
  lines.push("| Batch | Companies |");
  lines.push("|---|---:|");
  for (const batch of RECENT_BATCHES) lines.push(`| ${batch} | ${counts.get(batch) ?? 0} |`);
  lines.push("");
  lines.push("## Category Counts");
  lines.push("");
  lines.push("| Category | Companies |");
  lines.push("|---|---:|");
  for (const id of CATEGORY_ORDER) lines.push(`| ${CATEGORY_LABELS.get(id)} | ${catCounts.get(id) ?? 0} |`);
  lines.push("");
  lines.push("## Scan Tables");
  for (const id of CATEGORY_ORDER) {
    const group = rows
      .filter((row) => row.primary_category === id)
      .sort((a, b) => b.seth_fit_score - a.seth_fit_score || a.name.localeCompare(b.name));
    if (!group.length) continue;
    lines.push("");
    lines.push(`### ${CATEGORY_LABELS.get(id)}`);
    lines.push("");
    lines.push("| Score | Company | Batch | Website | Description |");
    lines.push("|---:|---|---|---|---|");
    for (const row of group) {
      const website = row.website ? `[site](${row.website})` : "";
      const yc = row.yc_url ? `[YC](${row.yc_url})` : "";
      const links = [website, yc].filter(Boolean).join(" / ");
      const description = truncate(row.description, 150);
      lines.push(
        `| ${row.seth_fit_score} | ${mdEscape(row.name)} | ${mdEscape(row.batch)} | ${links} | ${mdEscape(description)} |`,
      );
    }
  }
  lines.push("");
  lines.push("## Notes");
  lines.push("");
  lines.push("- `seth_fit_score` is a heuristic triage score, not a claim about company quality.");
  lines.push("- Follow-on fundraising is intentionally not enriched in this pass; use the shortlist for phase-two verification.");
  lines.push("- Categories are deliberately light and are meant to support fast scanning.");
  if (crosscheck.missing_from_yc_oss?.length) {
    lines.push(
      `- S26 directory-only rows added in this run: ${crosscheck.supplemented_companies.map((company) => company.name).join(", ")}.`,
    );
  }
  lines.push("");
  return `${lines.join("\n")}\n`;
}

function topShortlist(rows, limit = 50) {
  const seen = new Set();
  const selected = [];
  const preferredCategories = new Set([
    "gtm-revenue-ops",
    "document-legal-claims",
    "crm-work-surface",
    "vertical-ops-order-erp",
    "healthcare-admin",
    "compliance-evals-runtime",
  ]);

  const candidates = rows
    .filter((row) => preferredCategories.has(row.primary_category))
    .sort((a, b) => b.seth_fit_score - a.seth_fit_score || a.name.localeCompare(b.name));

  for (const row of candidates) {
    if (seen.has(row.id)) continue;
    seen.add(row.id);
    selected.push(row);
    if (selected.length >= limit) break;
  }
  return selected;
}

function strongest(items, fallback) {
  if (!items.length) return fallback;
  return items
    .sort((a, b) => b.points - a.points)
    .slice(0, 2)
    .map((item) => item.label)
    .join(" + ");
}

function whyItMatters(row) {
  const category = row.category_label.toLowerCase();
  const factors = strongest(row.seth_adjacency, "adjacent workflow");
  if (row.primary_category === "gtm-revenue-ops") {
    return `Looks like a revenue workflow wedge where Seth can reuse Salescraft-style list building, enrichment, prioritization, and review loops. Strongest adjacency: ${factors}.`;
  }
  if (row.primary_category === "document-legal-claims") {
    return `Document-heavy workflow that maps to Sunder-style extraction, citation review, validation, and human approval. Strongest adjacency: ${factors}.`;
  }
  if (row.primary_category === "crm-work-surface") {
    return `Work-surface/CRM pattern that could reuse Neo Bot and GTM Workspace ideas around tools, memory, approvals, tasks, and reviewed actions. Strongest adjacency: ${factors}.`;
  }
  if (row.primary_category === "vertical-ops-order-erp") {
    return `Boring operations category with possible OrderOps-style exception queues, source-of-truth matching, exports, and operator review. Strongest adjacency: ${factors}.`;
  }
  if (row.primary_category === "healthcare-admin") {
    return `Healthcare admin is painful, document-heavy, and trust-sensitive; good place to study deployment rather than generic agents. Strongest adjacency: ${factors}.`;
  }
  if (row.primary_category === "compliance-evals-runtime") {
    return `Trust, compliance, evals, or runtime layer for agents in live workflows; useful as infrastructure around the deployment bottleneck. Strongest adjacency: ${factors}.`;
  }
  return `High-scoring ${category} candidate with reusable workflow patterns. Strongest adjacency: ${factors}.`;
}

function singaporeWedge(row) {
  if (row.primary_category === "vertical-ops-order-erp") {
    return "Start with Singapore SMEs or regional operators with WhatsApp/email/spreadsheet handoffs, then offshore repeatable operations to Vietnam.";
  }
  if (row.primary_category === "gtm-revenue-ops") {
    return "Start with Singapore-based B2B teams selling regionally, using a concierge workflow audit before productizing.";
  }
  if (row.primary_category === "document-legal-claims") {
    return "Start with Singapore legal, compliance, fintech, or regional-HQ operations teams that already feel paperwork and audit pressure.";
  }
  if (row.primary_category === "healthcare-admin") {
    return "Start with Singapore clinics, specialist groups, insurers, or regional healthcare admin teams where workflow trust matters more than model novelty.";
  }
  if (row.primary_category === "compliance-evals-runtime") {
    return "Start with Singapore regulated buyers and AI-forward teams that need approval, audit, and deployment safety before autonomy.";
  }
  const text = companyText(row);
  if (/healthcare|clinic|radiology|dental|patient|payer/.test(text)) {
    return "Start with Singapore clinics, specialist groups, insurers, or regional healthcare admin teams where workflow trust matters more than model novelty.";
  }
  if (/legal|contract|law|claims|compliance/.test(text)) {
    return "Start with Singapore legal, compliance, fintech, or regional-HQ operations teams that already feel paperwork and audit pressure.";
  }
  if (/sales|revenue|gtm|crm|marketing|customer/.test(text)) {
    return "Start with Singapore-based B2B teams selling regionally, using a concierge workflow audit before productizing.";
  }
  if (/order|erp|warehouse|logistics|supply chain|procurement|food/.test(text)) {
    return "Start with Singapore SMEs or regional operators with WhatsApp/email/spreadsheet handoffs, then offshore repeatable operations to Vietnam.";
  }
  if (/eval|security|identity|governance|runtime|observability/.test(text)) {
    return "Start with Singapore regulated buyers and AI-forward teams that need approval, audit, and deployment safety before autonomy.";
  }
  return "Start with one Singapore operator segment and run a concierge version before deciding whether this deserves software.";
}

function likelyBuyer(row) {
  if (row.primary_category === "vertical-ops-order-erp") return "operations manager, warehouse lead, procurement head, or founder-operator";
  if (row.primary_category === "gtm-revenue-ops") return "founder, head of sales, revenue ops lead, or GTM operator";
  if (row.primary_category === "document-legal-claims") return "law-firm partner, legal ops lead, paralegal manager, or in-house counsel";
  if (row.primary_category === "healthcare-admin") return "clinic ops lead, provider group COO, revenue-cycle owner, or admin manager";
  if (row.primary_category === "compliance-evals-runtime") return "compliance lead, security lead, risk owner, or AI governance owner";
  if (row.primary_category === "crm-work-surface") return "founder, operator, advisor, sales lead, or relationship-driven practitioner";
  const text = companyText(row);
  if (/\b(dental|clinic|radiology|hospital|patient|provider)\b/.test(text)) return "clinic ops lead, provider group COO, revenue-cycle owner, or admin manager";
  if (/\b(legal|law|contract|claims|paralegal)\b/.test(text)) return "law-firm partner, legal ops lead, paralegal manager, or in-house counsel";
  if (/\b(sales|crm|revenue|gtm|outbound)\b/.test(text)) return "founder, head of sales, revenue ops lead, or GTM operator";
  if (/\b(order|warehouse|inventory|erp|procurement|supply chain|logistics)\b/.test(text)) return "operations manager, warehouse lead, procurement head, or founder-operator";
  if (/\b(compliance|risk|security|identity|audit)\b/.test(text)) return "compliance lead, security lead, risk owner, or AI governance owner";
  if (/\b(developer|api|agent|runtime|eval)\b/.test(text)) return "AI engineering lead, platform lead, or developer-tools founder";
  return "founder or operator closest to the manual workflow";
}

function doNotBuildIf(row) {
  const risks = row.risk_factors.map((factor) => factor.label);
  if (risks.includes("Enterprise-only wedge risk")) {
    return "Do not build if the first buyer requires long enterprise security/procurement before any small paid pilot.";
  }
  if (risks.includes("Deep-tech/research-heavy")) {
    return "Do not build if the core value depends on proprietary science or deep domain credentials rather than workflow execution.";
  }
  if (risks.includes("Capital-intensive")) {
    return "Do not build if the wedge requires hardware, regulated deployment, or inventory-heavy operations before software learning.";
  }
  if (risks.includes("Consumer/creator distraction")) {
    return "Do not build if distribution depends on consumer virality or brand taste rather than a painful repeat workflow.";
  }
  return "Do not build if there is no tired operator who already pays in time, errors, or missed revenue for this exact workflow.";
}

function renderShortlist(rows, meta, generatedAt, crosscheck) {
  const lines = [];
  lines.push("---");
  lines.push("type: staging_digest");
  lines.push('title: "YC Shortlist For Seth Startup Ideas"');
  lines.push(`generated_at: ${generatedAt}`);
  lines.push("status: staged");
  lines.push("source:");
  lines.push(`  - ${COMPANIES_URL}`);
  lines.push(`  - ${META_URL}`);
  lines.push("trust_lane: staging");
  lines.push("capture_quality: derived_from_public_api");
  lines.push("---");
  lines.push("");
  lines.push("# YC Shortlist For Seth Startup Ideas");
  lines.push("");
  lines.push(`Generated from [yc-oss/api](${YC_OSS_REPO}) data last updated ${meta.last_updated}. This is a heuristic shortlist for idea discovery, not investment advice and not compiled wiki knowledge.`);
  if (crosscheck.status === "passed" && crosscheck.added_from_directory_count > 0) {
    lines.push(
      `Summer 2026 was cross-checked against the official YC directory and supplemented with ${crosscheck.added_from_directory_count} directory-only companies before scoring.`,
    );
  }
  lines.push("");
  lines.push("## How To Read This");
  lines.push("");
  lines.push("- Look for adjacency to Salescraft/GTM, Sunder document processing, Neo Bot AI CRM, GTM Workspace, and Zhao OrderOps.");
  lines.push("- Prefer a Singapore-starting concierge wedge with global market potential and work that can later be supported by a Vietnam offshore team.");
  lines.push("- Follow-on fundraising is phase two; use this list to decide which companies or categories deserve deeper verification.");
  lines.push("");
  lines.push("## Shortlist");
  lines.push("");
  rows.forEach((row, index) => {
    const desc = row.description;
    const links = [
      row.website ? `[website](${row.website})` : null,
      row.yc_url ? `[YC](${row.yc_url})` : null,
    ]
      .filter(Boolean)
      .join(" / ");
    lines.push(`### ${index + 1}. ${row.name}`);
    lines.push("");
    lines.push(`- Score: ${row.seth_fit_score}`);
    lines.push(`- Batch/category: ${row.batch} / ${row.category_label}`);
    lines.push(`- Links: ${links}`);
    lines.push(`- What they do: ${desc}`);
    lines.push(`- Why it matters: ${whyItMatters(row)}`);
    lines.push(`- Singapore starting wedge: ${singaporeWedge(row)}`);
    lines.push(`- Likely buyer: ${likelyBuyer(row)}.`);
    lines.push(`- Do not build this if: ${doNotBuildIf(row)}`);
    if (row.risk_factors.length) {
      lines.push(`- Watchouts: ${row.risk_factors.map((x) => x.label).join(", ")}.`);
    }
    lines.push("");
  });
  return `${lines.join("\n")}\n`;
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      "user-agent": "Seth Second Brain YC company scan (personal research)",
      accept: "application/json",
    },
  });
  if (!response.ok) throw new Error(`Fetch failed for ${url}: ${response.status} ${response.statusText}`);
  return response.json();
}

async function extractS26DirectoryUrls() {
  const evalScript = `JSON.stringify(Array.from(document.querySelectorAll('a[href^="/companies/"],a[href*="ycombinator.com/companies/"]')).map(a=>a.href).filter(h=>/\\/companies\\//.test(h)&&!/founders/.test(h)).map(h=>h.replace(/\\/$/,'')).filter((v,i,a)=>a.indexOf(v)===i).sort())`;

  await execFileAsync(
    "agent-browser",
    [
      "--session",
      AGENT_BROWSER_SESSION,
      "--allowed-domains",
      AGENT_BROWSER_ALLOWED_DOMAINS,
      "open",
      S26_DIRECTORY_URL,
    ],
    { timeout: 30000, maxBuffer: 1024 * 1024 },
  );
  await execFileAsync("agent-browser", ["--session", AGENT_BROWSER_SESSION, "wait", "5000"], {
    timeout: 15000,
    maxBuffer: 1024 * 1024,
  });
  const { stdout } = await execFileAsync("agent-browser", ["--session", AGENT_BROWSER_SESSION, "eval", evalScript], {
    timeout: 30000,
    maxBuffer: 1024 * 1024,
  });
  const lastLine = stdout
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .at(-1);
  if (!lastLine) throw new Error("agent-browser returned no directory URL payload");
  return JSON.parse(JSON.parse(lastLine));
}

function decodeHtmlEntities(value) {
  return value
    .replace(/&#x([0-9a-f]+);/gi, (_, hex) => String.fromCodePoint(Number.parseInt(hex, 16)))
    .replace(/&#(\d+);/g, (_, decimal) => String.fromCodePoint(Number.parseInt(decimal, 10)))
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&apos;/g, "'");
}

async function fetchOfficialCompany(url) {
  const html = await fetch(url, {
    headers: {
      "user-agent": "Seth Second Brain YC company scan official-page supplement (personal research)",
      accept: "text/html",
    },
  }).then(async (response) => {
    if (!response.ok) throw new Error(`Fetch failed for ${url}: ${response.status} ${response.statusText}`);
    return response.text();
  });
  const match = html.match(/data-page="([^"]+)"/);
  if (!match) throw new Error(`No data-page company payload found at ${url}`);
  const page = JSON.parse(decodeHtmlEntities(match[1]));
  const company = page.props?.company;
  if (!company) throw new Error(`No company object found in data-page payload at ${url}`);
  return {
    id: company.id,
    name: company.name,
    website: company.website,
    one_liner: company.one_liner,
    long_description: company.long_description,
    batch: company.batch_name,
    industry: "",
    subindustry: "",
    tags: Array.isArray(company.tags) ? company.tags : [],
    status: company.ycdc_status,
    stage: "Early",
    team_size: company.team_size,
    url: company.ycdc_url || url,
    isHiring: false,
    top_company: false,
    source_origin: "official-yc-directory-supplement",
  };
}

async function crosscheckS26(sourceCompanies) {
  const apiUrls = new Set(
    sourceCompanies
      .filter((company) => company.batch === "Summer 2026")
      .map((company) => normalizeYcUrl(company.url))
      .filter(Boolean),
  );

  const result = {
    status: "skipped",
    method: "agent-browser official directory extraction, matching corralm/yc-scraper link-discovery behavior",
    directory_url: S26_DIRECTORY_URL,
    scraper_repo: YC_SCRAPER_FALLBACK,
    api_s26_count: apiUrls.size,
    directory_s26_count: 0,
    added_from_directory_count: 0,
    missing_from_yc_oss: [],
    missing_from_directory: [],
    supplemented_companies: [],
    error: "",
  };

  try {
    const directoryUrls = new Set(await extractS26DirectoryUrls());
    result.status = "passed";
    result.directory_s26_count = directoryUrls.size;
    result.missing_from_yc_oss = [...directoryUrls].filter((url) => !apiUrls.has(url)).sort();
    result.missing_from_directory = [...apiUrls].filter((url) => !directoryUrls.has(url)).sort();

    const supplemented = [];
    for (const url of result.missing_from_yc_oss) {
      supplemented.push(await fetchOfficialCompany(url));
    }
    result.added_from_directory_count = supplemented.length;
    result.supplemented_companies = supplemented.map((company) => ({
      name: company.name,
      yc_url: company.url,
      one_liner: company.one_liner,
    }));
    return { result, supplemented };
  } catch (error) {
    result.status = "failed";
    result.error = error.message;
    return { result, supplemented: [] };
  }
}

function asciiEscapeJson(text) {
  return Array.from(text, (char) => {
    const code = char.codePointAt(0);
    if (code <= 0x7f) return char;
    if (code <= 0xffff) return `\\u${code.toString(16).padStart(4, "0")}`;
    const offset = code - 0x10000;
    const high = 0xd800 + (offset >> 10);
    const low = 0xdc00 + (offset & 0x3ff);
    return `\\u${high.toString(16)}\\u${low.toString(16)}`;
  }).join("");
}

async function updateSourceMap(manifest, generatedAt) {
  let sourceMap;
  try {
    sourceMap = JSON.parse(await fs.readFile(SOURCE_MAP_PATH, "utf8"));
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }

  const id = "staging/yc-company-scan/yc_scan_manifest.json";
  const entry = {
    id,
    title: "YC recent company scan for startup ideas",
    url: COMPANIES_URL,
    source_type: "web_api",
    trust_lane: "staging",
    capture_quality: "derived_from_public_api",
    raw_path: null,
    staging_path: manifest.outputs.scan,
    status: "staged_uncompiled",
    wiki_paths: [],
    staging_paths: [
      manifest.outputs.csv,
      manifest.outputs.scan,
      manifest.outputs.shortlist,
      manifest.outputs.validation,
      id,
    ],
    created_at: generatedAt,
    updated_at: generatedAt,
    notes:
      "Derived from yc-oss/api companies/all.json and meta.json, with Summer 2026 cross-checked against the official YC directory using corralm/yc-scraper-style link discovery. Covers YC Winter 2024 through current Summer 2026; follow-on fundraising intentionally deferred to shortlist phase two.",
  };

  if (!Array.isArray(sourceMap.sources)) sourceMap.sources = [];
  const sourceIndex = sourceMap.sources.findIndex((source) => source.id === id);
  if (sourceIndex >= 0) {
    entry.created_at = sourceMap.sources[sourceIndex].created_at ?? generatedAt;
    sourceMap.sources[sourceIndex] = entry;
  } else {
    sourceMap.sources.push(entry);
  }

  if (!sourceMap.captures || typeof sourceMap.captures !== "object" || Array.isArray(sourceMap.captures)) {
    sourceMap.captures = {};
  }
  sourceMap.captures[id] = {
    url: COMPANIES_URL,
    title: entry.title,
    source_type: entry.source_type,
    trust_lane: entry.trust_lane,
    capture_quality: entry.capture_quality,
    status: entry.status,
    staging_paths: entry.staging_paths,
    compiled_to: [],
    api_last_updated: manifest.api_last_updated,
    row_count: manifest.row_count,
    shortlist_count: manifest.shortlist_count,
    s26_crosscheck: manifest.s26_crosscheck,
    notes: entry.notes,
    updated_at: generatedAt,
  };
  sourceMap.updated_at = generatedAt.slice(0, 10);

  await fs.writeFile(SOURCE_MAP_PATH, asciiEscapeJson(`${JSON.stringify(sourceMap, null, 2)}\n`), "utf8");
}

async function spotCheck(rows) {
  const byBatch = new Map();
  for (const row of rows) {
    if (!byBatch.has(row.batch)) byBatch.set(row.batch, []);
    byBatch.get(row.batch).push(row);
  }
  const candidates = [];
  for (const batch of RECENT_BATCHES) {
    const group = byBatch.get(batch) ?? [];
    if (group[0]) candidates.push(group[0]);
    if (group[Math.floor(group.length / 2)]) candidates.push(group[Math.floor(group.length / 2)]);
  }
  const unique = [...new Map(candidates.map((row) => [row.id, row])).values()].slice(0, 20);
  const checks = [];
  for (const row of unique) {
    try {
      const response = await fetch(row.yc_url, {
        headers: {
          "user-agent": "Seth Second Brain YC company scan validation (personal research)",
          accept: "text/html",
        },
      });
      await response.arrayBuffer();
      checks.push({
        name: row.name,
        batch: row.batch,
        yc_url: row.yc_url,
        status: response.status,
        ok: response.ok,
      });
    } catch (error) {
      checks.push({
        name: row.name,
        batch: row.batch,
        yc_url: row.yc_url,
        status: "error",
        ok: false,
        error: error.message,
      });
    }
  }
  return checks;
}

function renderValidation(rows, meta, generatedAt, checks, crosscheck) {
  const counts = batchCounts(rows);
  const missingRequired = rows.filter((row) => !row.name || (!row.website && !row.yc_url) || !row.description);
  const sourceDescriptionMissing = rows.filter((row) => row.source_description_missing);
  const missingCategory = rows.filter((row) => !row.primary_category);
  const metaBatchCounts = [];
  for (const batch of RECENT_BATCHES) {
    const key = batch.toLowerCase().replace(/\s+/g, "-");
    metaBatchCounts.push({
      batch,
      local: counts.get(batch) ?? 0,
      meta: meta.batches?.[key]?.count ?? null,
    });
  }

  const lines = [];
  lines.push("---");
  lines.push("type: staging_digest");
  lines.push('title: "YC Company Scan Validation"');
  lines.push(`generated_at: ${generatedAt}`);
  lines.push("status: staged");
  lines.push("trust_lane: staging");
  lines.push("---");
  lines.push("");
  lines.push("# YC Company Scan Validation");
  lines.push("");
  lines.push("## Summary");
  lines.push("");
  lines.push(`- API metadata last updated: ${meta.last_updated}.`);
  lines.push(`- Companies in scope: ${rows.length}.`);
  lines.push(`- Rows missing required fields: ${missingRequired.length}.`);
  lines.push(`- Rows with fallback descriptions because YC source description was missing: ${sourceDescriptionMissing.length}.`);
  lines.push(`- Rows missing category: ${missingCategory.length}.`);
  lines.push(`- Official YC URL spot checks attempted: ${checks.length}.`);
  lines.push(`- Official YC URL spot checks passed: ${checks.filter((check) => check.ok).length}.`);
  lines.push(`- S26 cross-check status: ${crosscheck.status}.`);
  if (crosscheck.status === "passed") {
    lines.push(`- S26 rows in yc-oss/api: ${crosscheck.api_s26_count}.`);
    lines.push(`- S26 rows in official YC directory: ${crosscheck.directory_s26_count}.`);
    lines.push(`- S26 directory-only rows added: ${crosscheck.added_from_directory_count}.`);
  } else if (crosscheck.error) {
    lines.push(`- S26 cross-check error: ${crosscheck.error}.`);
  }
  lines.push("");
  lines.push("## Batch Count Check");
  lines.push("");
  lines.push("| Batch | Local Rows | Metadata Count | Official Directory Count | Match Metadata |");
  lines.push("|---|---:|---:|---:|---|");
  for (const item of metaBatchCounts) {
    const directoryCount =
      item.batch === "Summer 2026" && crosscheck.status === "passed" ? crosscheck.directory_s26_count : "";
    lines.push(
      `| ${item.batch} | ${item.local} | ${item.meta ?? ""} | ${directoryCount} | ${item.local === item.meta ? "yes" : "no"} |`,
    );
  }
  if (crosscheck.status === "passed" && crosscheck.added_from_directory_count > 0) {
    lines.push("");
    lines.push(
      "Summer 2026 local rows can exceed metadata because this run supplements `yc-oss/api` with official YC directory rows found by the fallback cross-check.",
    );
  }
  lines.push("");
  lines.push("## Category Coverage");
  lines.push("");
  lines.push("| Category | Rows |");
  lines.push("|---|---:|");
  const catCounts = categoryCounts(rows);
  for (const id of CATEGORY_ORDER) lines.push(`| ${CATEGORY_LABELS.get(id)} | ${catCounts.get(id) ?? 0} |`);
  lines.push("");
  lines.push("## Official YC Spot Checks");
  lines.push("");
  lines.push("| Result | Company | Batch | Status | URL |");
  lines.push("|---|---|---|---:|---|");
  for (const check of checks) {
    lines.push(
      `| ${check.ok ? "pass" : "fail"} | ${mdEscape(check.name)} | ${mdEscape(check.batch)} | ${check.status} | [YC](${check.yc_url}) |`,
    );
  }
  lines.push("");
  if (crosscheck.status === "passed") {
    lines.push("## Summer 2026 Directory Cross-Check");
    lines.push("");
    lines.push(`- Directory URL: [Summer 2026](${S26_DIRECTORY_URL}).`);
    lines.push(`- Fallback scraper reference: [corralm/yc-scraper](${YC_SCRAPER_FALLBACK}).`);
    lines.push(`- Missing from yc-oss/api: ${crosscheck.missing_from_yc_oss.length}.`);
    lines.push(`- Missing from official directory: ${crosscheck.missing_from_directory.length}.`);
    lines.push("");
    if (crosscheck.supplemented_companies.length) {
      lines.push("| Added Company | YC URL | One-Liner |");
      lines.push("|---|---|---|");
      for (const company of crosscheck.supplemented_companies) {
        lines.push(`| ${mdEscape(company.name)} | [YC](${company.yc_url}) | ${mdEscape(company.one_liner)} |`);
      }
      lines.push("");
    }
  }
  if (missingRequired.length) {
    lines.push("## Missing Required Rows");
    lines.push("");
    lines.push("| Company | Batch | Missing |");
    lines.push("|---|---|---|");
    for (const row of missingRequired.slice(0, 50)) {
      const missing = [];
      if (!row.name) missing.push("name");
      if (!row.website && !row.yc_url) missing.push("website_or_yc_url");
      if (!row.description) missing.push("description");
      lines.push(`| ${mdEscape(row.name)} | ${mdEscape(row.batch)} | ${missing.join(", ")} |`);
    }
    lines.push("");
  }
  return `${lines.join("\n")}\n`;
}

async function main() {
  const now = new Date().toISOString();
  const [meta, allCompanies] = await Promise.all([fetchJson(META_URL), fetchJson(COMPANIES_URL)]);
  const batchSet = new Set(RECENT_BATCHES);
  const sourceCompanies = allCompanies.filter((company) => batchSet.has(company.batch));
  const { result: s26Crosscheck, supplemented } = await crosscheckS26(sourceCompanies);
  const rows = [...sourceCompanies, ...supplemented]
    .map((company) => normalizeCompany(company, meta))
    .sort((a, b) => RECENT_BATCHES.indexOf(a.batch) - RECENT_BATCHES.indexOf(b.batch) || a.name.localeCompare(b.name));

  await fs.mkdir(OUTPUT_DIR, { recursive: true });

  const csvPath = path.join(OUTPUT_DIR, "yc_recent_companies.csv");
  const scanPath = path.join(OUTPUT_DIR, "yc_recent_companies_scan.md");
  const shortlistPath = path.join(OUTPUT_DIR, "yc_shortlist.md");
  const validationPath = path.join(OUTPUT_DIR, "yc_scan_validation.md");
  const manifestPath = path.join(OUTPUT_DIR, "yc_scan_manifest.json");

  const shortlist = topShortlist(rows, 50);
  const checks = await spotCheck(rows);
  const manifest = {
    generated_at: now,
    primary_source: COMPANIES_URL,
    metadata_source: META_URL,
    source_repo: YC_OSS_REPO,
    fallback_scraper_repo: YC_SCRAPER_FALLBACK,
    api_last_updated: meta.last_updated,
    batches: RECENT_BATCHES,
    row_count: rows.length,
    shortlist_count: shortlist.length,
    s26_crosscheck: s26Crosscheck,
    outputs: {
      csv: csvPath,
      scan: scanPath,
      shortlist: shortlistPath,
      validation: validationPath,
    },
  };

  await Promise.all([
    fs.writeFile(csvPath, toCsv(rows), "utf8"),
    fs.writeFile(scanPath, renderScan(rows, meta, now, s26Crosscheck), "utf8"),
    fs.writeFile(shortlistPath, renderShortlist(shortlist, meta, now, s26Crosscheck), "utf8"),
    fs.writeFile(validationPath, renderValidation(rows, meta, now, checks, s26Crosscheck), "utf8"),
    fs.writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8"),
  ]);
  await updateSourceMap(manifest, now);

  console.log(`Generated ${rows.length} YC company rows.`);
  console.log(`Shortlisted ${shortlist.length} companies.`);
  console.log(`API last updated: ${meta.last_updated}`);
  console.log(
    `S26 cross-check: ${s26Crosscheck.status}; yc-oss/api=${s26Crosscheck.api_s26_count}, directory=${s26Crosscheck.directory_s26_count}, added=${s26Crosscheck.added_from_directory_count}.`,
  );
  console.log(`Outputs written to ${OUTPUT_DIR}/`);
  console.log(`Official YC spot checks: ${checks.filter((check) => check.ok).length}/${checks.length} passed.`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
