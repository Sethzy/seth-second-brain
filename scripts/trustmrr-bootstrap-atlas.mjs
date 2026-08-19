#!/usr/bin/env node

import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";

const API_BASE = "https://trustmrr.com/api/v1";
const TODAY = new Date().toISOString().slice(0, 10);
const OUT_DIR = path.join("outputs", "bootstrap-company-atlas");
const KEY = process.env.TRUSTMRR_API_KEY;
const LIMIT = Number(process.env.TRUSTMRR_LIMIT || 50);
const INPUT_JSON = process.env.TRUSTMRR_INPUT_JSON;
const MAX_PAGES = process.env.TRUSTMRR_MAX_PAGES
  ? Number(process.env.TRUSTMRR_MAX_PAGES)
  : Infinity;

if (!KEY && !INPUT_JSON) {
  console.error("Missing TRUSTMRR_API_KEY in environment.");
  process.exit(1);
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchJson(url) {
  const response = await fetch(url, {
    headers: {
      Authorization: `Bearer ${KEY}`,
      Accept: "application/json",
    },
  });

  const text = await response.text();
  if (!response.ok) {
    throw new Error(`TrustMRR ${response.status}: ${text.slice(0, 300)}`);
  }

  return {
    json: JSON.parse(text),
    rate: {
      limit: response.headers.get("x-ratelimit-limit"),
      remaining: response.headers.get("x-ratelimit-remaining"),
      reset: response.headers.get("x-ratelimit-reset"),
    },
  };
}

function money(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) {
    return "";
  }
  const n = Number(value);
  if (Math.abs(n) >= 1_000_000) return `$${(n / 1_000_000).toFixed(1)}M`;
  if (Math.abs(n) >= 1_000) return `$${(n / 1_000).toFixed(1)}k`;
  return `$${Math.round(n).toLocaleString("en-US")}`;
}

function csvCell(value) {
  const s = value === null || value === undefined ? "" : String(value).replace(/\s+/g, " ").trim();
  return `"${s.replaceAll('"', '""')}"`;
}

const themeRules = [
  {
    name: "GTM / Revenue Ops",
    categories: new Set(["Sales", "Marketing", "Analytics"]),
    keywords:
      /\b(gtm|sales|lead|leads|outbound|crm|email|campaign|ads|seo|marketing|revenue|pipeline|prospect|appointment|booking|conversion|agency)\b/i,
  },
  {
    name: "Document / Compliance Workflow",
    categories: new Set(["Legal", "Security", "Fintech"]),
    keywords:
      /\b(document|pdf|contract|legal|compliance|invoice|audit|tax|permit|form|filing|claim|claims|policy|regulatory|court|license|certificate)\b/i,
  },
  {
    name: "AI CRM / Inbox-To-Workflow",
    categories: new Set(["Customer Support", "Sales", "Productivity"]),
    keywords:
      /\b(crm|inbox|chat|whatsapp|telegram|slack|support|ticket|conversation|follow[- ]?up|meeting|calendar|call|voice|assistant|agent)\b/i,
  },
  {
    name: "Local / Service Business Ops",
    categories: new Set([
      "Real Estate",
      "Recruiting & HR",
      "Health & Fitness",
      "E-commerce",
      "Travel",
      "Education",
    ]),
    keywords:
      /\b(local|agency|client|shopify|merchant|restaurant|clinic|property|real estate|recruiting|candidate|appointment|order|inventory|fulfillment|delivery|booking|review)\b/i,
  },
];

function themesFor(startup) {
  const text = [startup.name, startup.description, startup.category, startup.targetAudience]
    .filter(Boolean)
    .join(" ");
  const themes = [];

  for (const rule of themeRules) {
    if (rule.categories.has(startup.category) || rule.keywords.test(text)) {
      themes.push(rule.name);
    }
  }

  return themes;
}

function scoreStartup(startup) {
  const themes = themesFor(startup);
  const last30 = Number(startup.revenue?.last30Days || 0);
  const mrr = Number(startup.revenue?.mrr || 0);
  let score = 0;

  score += themes.length * 3;
  if (last30 > 0 || mrr > 0) score += 2;
  if ((mrr >= 500 && mrr <= 50_000) || (last30 >= 500 && last30 <= 100_000)) {
    score += 2;
  }
  if (startup.onSale) score += 1;
  if (startup.website) score += 1;
  if (startup.description && startup.description.length >= 35) score += 1;
  if (last30 > 500_000 || mrr > 500_000) score -= 3;
  if (startup.name?.toLowerCase().includes("anonymous")) score -= 2;
  if (themes.length === 0) score -= 1;

  return score;
}

function toRow(startup) {
  const themes = themesFor(startup);
  return {
    name: startup.name || "",
    website: startup.website || "",
    trustmrr_url: startup.url || "",
    description: startup.description || "",
    category: startup.category || "",
    themes: themes.join("; "),
    country: startup.country || "",
    target_audience: startup.targetAudience || "",
    last_30_days_revenue: startup.revenue?.last30Days ?? "",
    mrr: startup.revenue?.mrr ?? "",
    total_revenue: startup.revenue?.total ?? "",
    growth_30d: startup.growth30d ?? "",
    growth_mrr_30d: startup.growthMRR30d ?? "",
    customers: startup.customers ?? "",
    active_subscriptions: startup.activeSubscriptions ?? "",
    on_sale: startup.onSale ? "yes" : "no",
    asking_price: startup.askingPrice ?? "",
    multiple: startup.multiple ?? "",
    x_handle: startup.xHandle || "",
    score: scoreStartup(startup),
  };
}

function writeCsv(rows) {
  const headers = [
    "name",
    "website",
    "description",
    "category",
    "themes",
    "country",
    "target_audience",
    "last_30_days_revenue",
    "mrr",
    "total_revenue",
    "growth_30d",
    "growth_mrr_30d",
    "customers",
    "active_subscriptions",
    "on_sale",
    "asking_price",
    "multiple",
    "x_handle",
    "trustmrr_url",
    "score",
  ];
  return [
    headers.join(","),
    ...rows.map((row) => headers.map((header) => csvCell(row[header])).join(",")),
  ].join("\n");
}

function categorySummary(rows) {
  const grouped = new Map();
  for (const row of rows) {
    const item = grouped.get(row.category) || {
      category: row.category || "Unknown",
      count: 0,
      withRevenue: 0,
      totalLast30: 0,
      totalMrr: 0,
      topScore: -Infinity,
    };
    item.count += 1;
    if (Number(row.last_30_days_revenue) > 0 || Number(row.mrr) > 0) item.withRevenue += 1;
    item.totalLast30 += Number(row.last_30_days_revenue || 0);
    item.totalMrr += Number(row.mrr || 0);
    item.topScore = Math.max(item.topScore, Number(row.score || 0));
    grouped.set(row.category, item);
  }
  return [...grouped.values()].sort((a, b) => b.count - a.count);
}

function mdTable(rows) {
  const lines = [
    "| Company | Category | Themes | Revenue / MRR | Website | Why scan |",
    "|---|---|---|---:|---|---|",
  ];

  for (const row of rows) {
    const revenue = [money(row.last_30_days_revenue), row.mrr ? `${money(row.mrr)} MRR` : ""]
      .filter(Boolean)
      .join(" / ");
    const why = row.description.replaceAll("|", "\\|").slice(0, 150);
    const website = row.website ? `[site](${row.website})` : "";
    lines.push(
      `| [${row.name.replaceAll("|", "\\|")}](${row.trustmrr_url}) | ${row.category} | ${row.themes || "-"} | ${revenue || "-"} | ${website} | ${why} |`,
    );
  }

  return lines.join("\n");
}

function buildMarkdown(rows, meta) {
  const byScore = [...rows].sort((a, b) => b.score - a.score);
  const categoryRows = categorySummary(rows);
  const themeSections = themeRules.map((rule) => {
    const picked = byScore.filter((row) => row.themes.includes(rule.name)).slice(0, 25);
    return [
      `## ${rule.name}`,
      "",
      mdTable(picked),
      "",
    ].join("\n");
  });

  const categoryLines = [
    "| Category | Count | With revenue | Last 30d revenue | MRR |",
    "|---|---:|---:|---:|---:|",
    ...categoryRows.map(
      (row) =>
        `| ${row.category} | ${row.count} | ${row.withRevenue} | ${money(row.totalLast30)} | ${money(row.totalMrr)} |`,
    ),
  ];

  return [
    "# TrustMRR Bootstrap Company Atlas",
    "",
    `Collected: ${TODAY}`,
    "",
    "Source: TrustMRR API (`/api/v1/startups`). API key was used only for collection and is not stored in this output.",
    "",
    "## Summary",
    "",
    `- Rows collected: ${rows.length.toLocaleString("en-US")}`,
    `- API-reported total: ${meta.total?.toLocaleString("en-US") || "Unknown"}`,
    `- Categories observed: ${categoryRows.length}`,
    "- Ranking bias: companies near Seth's GTM, document/compliance, AI CRM, and local/service-ops lanes are intentionally pushed up.",
    "- Use the CSV for scanning; use this Markdown file for theme-first browsing.",
    "",
    "## Category Breadth",
    "",
    categoryLines.join("\n"),
    "",
    "## Highest Seth-Adjacency Reference Points",
    "",
    mdTable(byScore.slice(0, 75)),
    "",
    ...themeSections,
  ].join("\n");
}

async function main() {
  await mkdir(OUT_DIR, { recursive: true });

  let startups = [];
  let meta = null;

  if (INPUT_JSON) {
    const snapshot = JSON.parse(await import("node:fs/promises").then((fs) => fs.readFile(INPUT_JSON, "utf8")));
    startups = snapshot.data || [];
    meta = snapshot.meta || { total: startups.length };
    console.log(`Loaded ${startups.length} startups from ${INPUT_JSON}`);
  } else {
    let page = 1;

    while (page <= MAX_PAGES) {
      const url = new URL(`${API_BASE}/startups`);
      url.searchParams.set("page", String(page));
      url.searchParams.set("limit", String(LIMIT));
      url.searchParams.set("sort", "revenue-desc");

      const { json, rate } = await fetchJson(url);
      meta = json.meta;
      startups.push(...json.data);

      console.log(
        `Fetched page ${page} (${startups.length}/${json.meta.total}); remaining=${rate.remaining ?? "?"}`,
      );

      if (!json.meta.hasMore) break;
      page += 1;

      if (Number(rate.remaining) <= 1 && rate.reset) {
        const waitMs = Math.max(Number(rate.reset) * 1000 - Date.now() + 1000, 3_500);
        console.log(`Rate window nearly exhausted; waiting ${Math.ceil(waitMs / 1000)}s`);
        await sleep(waitMs);
      } else {
        await sleep(3_200);
      }
    }
  }

  const rows = startups.map(toRow);
  const stem = path.join(OUT_DIR, `${TODAY}-trustmrr-startups`);

  await writeFile(
    `${stem}.json`,
    JSON.stringify({ collected_at: new Date().toISOString(), meta, data: startups }, null, 2),
  );
  await writeFile(`${stem}.csv`, `${writeCsv(rows)}\n`);
  await writeFile(`${stem}.md`, buildMarkdown(rows, meta));

  console.log(`Wrote ${stem}.json`);
  console.log(`Wrote ${stem}.csv`);
  console.log(`Wrote ${stem}.md`);
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});
