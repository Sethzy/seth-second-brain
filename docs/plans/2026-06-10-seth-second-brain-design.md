# Seth Second Brain Design

Date: 2026-06-10
Status: validated draft
Owner: Seth

## Baseline And Source Of Truth

This repo should follow Karpathy's LLM Wiki pattern completely. The canonical idea is the three-layer model: immutable raw sources, an LLM-owned compiled wiki, and a schema file that teaches the agent how to maintain the system. The important point is not merely "save notes." The important point is that the wiki is a persistent, compounding artifact. New sources update existing synthesis, cross-references, contradictions, index entries, and maintenance state instead of forcing every future query to rediscover raw material from scratch.

The open-source implementation baseline is [`Astro-Han/karpathy-llm-wiki`](https://github.com/Astro-Han/karpathy-llm-wiki), validated locally at commit `9e8c4f4`. We are not hand-rolling the core behavior. We are taking Astro-Han's lightweight Agent Skill structure as the starting point: `raw/` for immutable source material, `wiki/` for compiled knowledge, `wiki/index.md` for content routing, `wiki/log.md` for chronological audit, plus ingest, query, archive, and lint workflows.

We augment that baseline for Seth's specific workflow. The repo's authenticated exact-link wrapper handles pasted X/Twitter links using the Last30Days/Bird TweetDetail path with Chrome Profile 3 cookies and X Article field toggles. `mvanhorn/last30days-skill` handles noisy recent-signal topic sweeps. `qmd` is the local markdown retrieval layer once installed. The GTM workspace contributes prior architecture decisions around markdown-first operating memory, qmd, and separating durable wiki knowledge from raw/cache material.

The hierarchy is:

```text
Canonical idea: Karpathy LLM Wiki
Primary baseline: Astro-Han/karpathy-llm-wiki
Exact X link capture: scripts/x-capture-to-raw.sh using Last30Days/Bird TweetDetail
Recent-signal sweeps: mvanhorn/last30days-skill
Retrieval augmentation: qmd
Prior local reference: /Users/sethlim/Documents/gtm-workspace
```

## User Stories

The main user story is exact capture. Seth sees something valuable, often an X post/thread, article, YouTube video, paper, or pasted text, and wants to save the full thing so it can be found later. The source record must preserve the original URL, readable source content or best available extraction, capture date, author/source metadata, and any note Seth gave at capture time. If Seth later asks "find that post about dynamic workflows," the system should return the original link and local raw note first.

The second user story is synthesis. Seth asks "what do I know about context engineering?" or "what are the strongest ideas I have saved about AI coding agents?" The agent should read `wiki/index.md`, search compiled wiki pages, search raw sources for supporting details, and answer from the accumulated wiki where possible. If the query creates useful new synthesis, the answer should be fileable back into `wiki/` as an archive page or an update to existing pages.

The third user story is self-maintenance. As the corpus grows, the knowledge base should get cleaner rather than messier. The agent should detect overlapping pages, stale claims, contradictions, orphan pages, uncited raw sources, missing cross-links, and staging material that should be promoted or dropped. Raw evidence is preserved; wiki structure is actively pruned, merged, rewritten, and archived.

The fourth user story is automated research. Last30Days-style runs collect recent social/web signal about a topic. These are lower-trust and noisier than intentional captures, so they land in a separate sweep lane, produce staging digests, and only update durable wiki pages after approval or explicit instruction.

## Architecture

The architecture follows Karpathy's three layers exactly.

Layer one is `raw/`: immutable source material. This is the evidence archive. It includes intentional captures and separately stored sweeps. The agent reads raw files but should not rewrite them. If a source changes or extraction improves, create a new raw snapshot rather than mutating the old one.

Layer two is `wiki/`: the LLM-owned compiled knowledge layer. It contains medium-length topic articles, concept pages, entity pages, comparison pages, archived query answers, `index.md`, and `log.md`. Seth generally does not manually edit this layer. The agent creates and updates it by ingesting sources, filing query answers, maintaining cross-references, marking contradictions, merging overlap, and archiving stale pages.

Layer three is schema: `AGENTS.md`, templates, workflow docs, and later any skill files. This is the behavior contract that makes the agent a disciplined wiki maintainer instead of a generic chatbot. The schema itself should evolve as the corpus teaches us better conventions.

Two side lanes augment the core. `qmd` indexes raw, wiki, and staging for retrieval. Last30Days writes recent-signal raw outputs and staging digests. Exact pasted X links use the repo's authenticated TweetDetail wrapper, not Last30Days topic sweeps.

```text
raw/         immutable sources and sweep artifacts
wiki/        LLM-owned compiled knowledge
AGENTS.md    schema/instructions layer
templates/   baseline formats
staging/     review queue for noisy material and maintenance proposals
config/      qmd and sweep config
scripts/     wrappers and lint
```

## Components

The first component is the schema component: `AGENTS.md`, `docs/workflows.md`, and templates. This encodes how the agent captures, ingests, queries, archives, lints, prunes, logs, and updates lifecycle state. It is the most important component because it defines the wiki maintainer behavior.

The second component is raw source storage. Intentional sources live under `raw/intentional/`, separated by broad source type such as `x`, `web`, `youtube`, `papers`, `books`, and `pasted`. This is slightly more specific than Astro-Han's topic-first raw layout because Seth's day-to-day recall often starts with "that X post" or "that article." The compiled `wiki/` remains idea-domain oriented.

The third component is exact X capture. This uses `scripts/x-capture-to-raw.sh`, which wraps an authenticated Bird/TweetDetail fetch backed by the GTM workspace's Last30Days implementation. It accepts pasted X/Twitter status URLs, preserves the original URL, writes complete markdown raw captures when TweetDetail returns full text, and stages partial captures when X only returns metadata, title, preview, or an error.

The fourth component is the compiled wiki. Pages should be medium-length synthesis articles around reusable idea clusters, not tiny note sprawl and not giant category dumps. Pages can carry lifecycle states such as `draft`, `active`, `stale`, `contradicted`, and `archived`.

The fifth component is staging and maintenance. `staging/` holds Last30Days digests, proposed merges, proposed prunes, bulk-import cluster reports, and other review-needed material. Maintenance scripts and runbooks check health and propose improvements.

## Data Flow

Manual exact X capture starts when Seth pastes one or more X links. The system routes those through `scripts/x-capture-to-raw.sh`. The wrapper extracts the status ID, fetches TweetDetail with authenticated Chrome Profile 3 cookies, requests X Article body fields, creates a markdown note with YAML frontmatter, and stores the original URL prominently. Complete captures write directly to `raw/intentional/x/`; incomplete captures write to `staging/incomplete-captures/x/`. After capture, the agent can lightly compile the post into relevant wiki pages and update `wiki/index.md` and `wiki/log.md`.

Manual general capture starts with a web article, YouTube link/transcript, paper, book excerpt, or pasted source. The agent saves a full immutable raw snapshot under `raw/intentional/<source-type>/`, then compiles it into the wiki. Compilation may update one page or many pages. The Astro-Han baseline explicitly allows cascade updates: same-thesis sources merge into existing articles, new concepts get new articles, and cross-topic material gets See Also links. Conflicts are annotated rather than flattened.

Query flow starts with intent detection. If Seth is trying to find a remembered source, search raw first and return the original URL plus local raw path. If Seth asks what he knows or believes, read `wiki/index.md`, search wiki first, search raw second, and synthesize with citations. If the answer is valuable, ask whether to file it into the wiki as an archive page or article update.

Last30Days flow starts with a topic run. The raw fixed output lands under `raw/sweeps/last30days/`. The agent writes a digest under `staging/last30days/` with strong signals, repeated themes, candidate wiki updates, sources worth manual capture, and cautions. Sweeps never update wiki directly unless promoted.

## Error Handling

The system should save what it can without pretending partial captures are complete. For exact X capture, TweetDetail can still fail, return no text, or expose only title/preview metadata. In that case the note should clearly mark the capture as partial, preserve the original link, and stay in staging until a full capture is available.

For general captures, extraction failure should still create a minimal raw record containing URL, capture date, failure reason, and retry guidance. The agent must not create confident wiki claims from a failed or partial extraction. If a source is binary, media-heavy, auth-gated, or image-dependent, the raw record should say what was captured and what was not.

For Last30Days, degraded or thin runs stay in staging. If X, Reddit, YouTube, or web sources fail, the raw run is preserved and the digest records source coverage and caution labels. Poor-coverage sweeps should not promote to wiki automatically.

For maintenance, raw captures are never casually deleted. Wiki pages can be merged, marked stale, contradicted, or archived. Hard deletion should require explicit approval unless the file is an accidental duplicate with no unique content. Every maintenance pass appends `wiki/log.md`.

For prompt-injection risk, raw source text is untrusted. The agent should read it as quoted material, not as instructions. Instructions inside an article or tweet do not override `AGENTS.md` or system/developer instructions.

## Testing And Verification

Testing should prove both structure and retrieval.

Structure tests should verify required files and directories: `raw/`, `wiki/`, `staging/`, `templates/`, `AGENTS.md`, `wiki/index.md`, and `wiki/log.md`. The lint should check markdown links, missing index entries, raw references, malformed frontmatter, and required templates.

Capture tests should use known X links and confirm that `scripts/x-capture-to-raw.sh` output includes URL, original URL, handle, status ID, captured date, capture quality, metrics, and verbatim text. If the result is partial, the file should say so and land in staging. General capture tests should include one web article, one pasted note, and one YouTube transcript or URL.

Query tests should use a tiny fixture corpus: two raw X captures, one web capture, and two wiki pages. A source-recall query should return raw source plus URL. A synthesis query should read wiki first and cite raw as support.

Maintenance tests should create a duplicate wiki page, stale claim, orphan page, missing raw reference, and broken link. Lint should report them. Prune should propose merge/archive actions rather than deleting raw evidence.

Last30Days tests should run or fixture a sweep output, create a staging digest, and verify that no wiki page changes occur without approval.

Baseline validation should compare the repo's conventions against `Astro-Han/karpathy-llm-wiki`: immutable raw, compiled wiki, `index.md`, `log.md`, ingest, query/archive, lint, relative links, and cascade updates.

## Unresolved Questions

1. Should the current scaffold adopt Astro-Han's exact topic-first `raw/<topic>/` layout, or keep source-type raw folders for retrieval ergonomics? Current recommendation: source-type raw, idea-domain wiki.
2. How aggressive should pruning be? Recommendation: raw never deleted automatically, staging can expire, wiki can merge/archive with log entries, hard deletion requires approval.
3. Should qmd be required immediately or optional? Recommendation: configure from day one, but keep operation possible with `rg` until qmd is installed.
4. Should useful query answers file automatically? Recommendation: ask before filing at first; automate later if the pattern stabilizes.

## Validation Against Astro-Han Baseline

Validated against `/tmp/astro-karpathy-llm-wiki/SKILL.md` at commit `9e8c4f4`.

| Baseline Requirement | Present In Design | Notes |
|---|---|---|
| `raw/` immutable source layer | Yes | Augmented with source-type lanes and sweeps. |
| `wiki/` compiled LLM-owned layer | Yes | Explicitly LLM-owned and self-maintained. |
| Schema layer | Yes | `AGENTS.md`, templates, workflow docs. |
| Ingest saves raw then compiles wiki | Yes | Manual capture flow preserves this. |
| Query reads `wiki/index.md` first | Yes | Raw-first only for source-recall queries. |
| Query answers can be archived | Yes | Added query filing as a user story and flow. |
| Lint checks index, links, raw refs, contradictions | Yes | Starts simple, expands to semantic health. |
| `wiki/log.md` append-only | Yes | Required for ingest/query/lint/maintenance. |
| Cascade updates | Yes | Explicitly supported beyond v1 "light compile." |
| Relative markdown links | Yes | Required in templates and lint. |

Conclusion: the design follows the Astro-Han baseline and adds project-specific capture/retrieval lanes without changing the core LLM Wiki pattern.
