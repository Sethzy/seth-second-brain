import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


def load_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "wiki_maintenance.py"
    spec = importlib.util.spec_from_file_location("wiki_maintenance", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def write_source_map(root, sources):
    write(
        root / "state" / "source-map.json",
        json.dumps({"version": 1, "sources": sources}, indent=2),
    )


def write_source_map_with_captures(root, captures):
    write(
        root / "state" / "source-map.json",
        json.dumps({"version": 1, "sources": [], "captures": captures}, indent=2),
    )


class WikiMaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.wm = load_module()

    def tearDown(self):
        self.tmp.cleanup()

    def test_lint_allows_legacy_complete_raw_declared_in_source_map(self):
        raw_path = "raw/intentional/web/legacy-complete.md"
        write(self.root / raw_path, "---\ntype: raw_capture\n---\n# Legacy complete capture\n")
        write_source_map(
            self.root,
            [
                {
                    "id": raw_path,
                    "source_type": "web",
                    "capture_quality": "complete",
                    "raw_path": raw_path,
                    "status": "raw",
                }
            ],
        )

        self.assertEqual(self.wm.find_intentional_raw_quality_errors(self.root), [])

    def test_lint_allows_legacy_complete_raw_declared_in_captures_map(self):
        raw_path = "raw/intentional/web/legacy-captures-map.md"
        write(self.root / raw_path, "---\ntype: raw_capture\n---\n# Legacy capture-map capture\n")
        write_source_map_with_captures(
            self.root,
            {
                raw_path: {
                    "source_type": "web",
                    "trust_lane": "intentional",
                    "status": "raw_captured_compiled",
                    "compiled_to": ["wiki/example.md"],
                }
            },
        )

        self.assertEqual(self.wm.find_intentional_raw_quality_errors(self.root), [])

    def test_lint_flags_legacy_raw_missing_source_map_complete_entry(self):
        raw_path = "raw/intentional/web/untracked-legacy.md"
        write(self.root / raw_path, "---\ntype: raw_capture\n---\n# Untracked legacy capture\n")
        write_source_map(self.root, [])

        errors = self.wm.find_intentional_raw_quality_errors(self.root)

        self.assertEqual(len(errors), 1)
        self.assertIn(raw_path, errors[0])
        self.assertIn("capture_quality: complete", errors[0])

    def test_organization_proposal_groups_raw_only_x_into_existing_pages(self):
        write(
            self.root / "wiki" / "index.md",
            "\n".join(
                [
                    "# Knowledge Base Index",
                    "| [Agentic Engineering Practices](ai-coding/agentic-engineering-practices.md) | AI coding | 2026-06-18 |",
                    "| [SEO/AEO/GEO Content Systems](marketing/seo-aeo-geo-content-systems.md) | Search | 2026-06-19 |",
                ]
            ),
        )
        write_source_map(
            self.root,
            [
                {
                    "id": "x-1",
                    "title": "Claude Code agents skill workflow",
                    "source_type": "x",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/x/111-claude-code-agent.md",
                    "status": "raw",
                },
                {
                    "id": "x-2",
                    "title": "Google AI search SEO visibility",
                    "source_type": "x",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/x/222-google-ai-search-seo.md",
                    "status": "raw",
                },
                {
                    "id": "x-3",
                    "title": "Already compiled",
                    "source_type": "x",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/x/333-compiled.md",
                    "status": "compiled",
                },
            ],
        )

        report = self.wm.build_organization_proposal(self.root, limit=25, source_type="x", include_qmd=False)

        self.assertIn("Raw-only X sources selected: 2", report)
        self.assertIn("Agentic Engineering Practices", report)
        self.assertIn("SEO/AEO/GEO Content Systems", report)
        self.assertIn("raw/intentional/x/111-claude-code-agent.md", report)
        self.assertNotIn("raw/intentional/x/333-compiled.md", report)

    def test_health_report_counts_raw_only_and_duplicate_x_staging(self):
        write(self.root / "wiki" / "index.md", "# Knowledge Base Index\n")
        write(self.root / "wiki" / "ai-coding" / "agentic-engineering-practices.md", "# Agentic Engineering Practices\n")
        write(self.root / "raw" / "intentional" / "x" / "123-topic.md", "# Raw X\n")
        write(self.root / "staging" / "incomplete-captures" / "x" / "2026-06-10-topic-123.md", "# Staged X\n")
        write_source_map(
            self.root,
            [
                {
                    "id": "raw/intentional/x/123-topic.md",
                    "source_type": "x",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/x/123-topic.md",
                    "status": "raw",
                },
                {
                    "id": "raw/intentional/web/compiled.md",
                    "source_type": "web",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/web/compiled.md",
                    "status": "compiled",
                },
            ],
        )

        report = self.wm.build_health_report(self.root, include_qmd=False)

        self.assertIn("| x | 1 |", report)
        self.assertIn("Duplicate X capture/staging records", report)
        self.assertIn("123", report)

    def test_health_report_ignores_superseded_x_staging_duplicates(self):
        write(self.root / "wiki" / "index.md", "# Knowledge Base Index\n")
        write(self.root / "raw" / "intentional" / "x" / "123-topic.md", "# Raw X\n")
        write(
            self.root / "staging" / "incomplete-captures" / "x" / "2026-06-10-topic-123.md",
            "---\nstatus: superseded\n---\n# Staged X\n",
        )
        write_source_map(
            self.root,
            [
                {
                    "id": "raw/intentional/x/123-topic.md",
                    "source_type": "x",
                    "capture_quality": "complete",
                    "raw_path": "raw/intentional/x/123-topic.md",
                    "status": "raw",
                },
            ],
        )

        report = self.wm.build_health_report(self.root, include_qmd=False)

        self.assertIn("Duplicate X capture/staging records", report)
        self.assertIn("- None detected.", report)

    def test_wiki_lint_report_flags_core_structural_issues(self):
        write(
            self.root / "wiki" / "index.md",
            "\n".join(
                [
                    "# Knowledge Base Index",
                    "| Article | Summary | Updated |",
                    "|---|---|---|",
                    "| [Page One](topic/page-one.md) | One | 2026-06-01 |",
                    "| [Missing Page](topic/missing-page.md) | Gone | 2026-06-01 |",
                ]
            ),
        )
        write(
            self.root / "wiki" / "topic" / "page-one.md",
            "\n".join(
                [
                    "---",
                    "type: wiki_article",
                    "title: Page One",
                    "updated_at: 2026-06-01",
                    "status: active",
                    "---",
                    "",
                    "# Page One",
                    "",
                    "This links to [Missing](missing.md), [Missing Raw](../../raw/intentional/web/missing.md), and [[Ghost Note]].",
                    "",
                    "## Empty Section",
                    "",
                    "## Filled Section",
                    "Useful content.",
                ]
            ),
        )
        write(
            self.root / "wiki" / "topic" / "page-two.md",
            "\n".join(
                [
                    "---",
                    "type: wiki_article",
                    "title: Page Two",
                    "updated_at: 2026-06-01",
                    "status: active",
                    "tags:",
                    "  - example",
                    "---",
                    "",
                    "# Page Two",
                    "",
                    "> Sources: test",
                ]
            ),
        )
        write_source_map(self.root, [])

        report = self.wm.build_wiki_lint_report(self.root, stale_days=999)

        self.assertIn("Frontmatter Gaps", report)
        self.assertIn("tags", report)
        self.assertIn("Broken Links", report)
        self.assertIn("missing.md", report)
        self.assertIn("Ghost Note", report)
        self.assertIn("Empty Sections", report)
        self.assertIn("Stale Index Entries", report)
        self.assertIn("topic/missing-page.md", report)
        self.assertIn("Pages Missing From Index", report)
        self.assertIn("wiki/topic/page-two.md", report)

    def test_wiki_lint_report_detects_repeated_unpaged_phrase(self):
        write(self.root / "wiki" / "index.md", "# Knowledge Base Index\n")
        for name in ["one", "two", "three"]:
            write(
                self.root / "wiki" / "topic" / f"{name}.md",
                "\n".join(
                    [
                        "---",
                        "type: wiki_article",
                        f"title: Page {name.title()}",
                        "updated_at: 2026-06-01",
                        "status: active",
                        "tags:",
                        "  - example",
                        "---",
                        "",
                        f"# Page {name.title()}",
                        "",
                        "Acme Platform is important in this workflow.",
                        "",
                        "> Sources: test",
                    ]
                ),
            )
        write_source_map(self.root, [])

        report = self.wm.build_wiki_lint_report(self.root, stale_days=999)

        self.assertIn("Repeated Concepts / Entities Without Pages", report)
        self.assertIn("Acme Platform", report)

    def test_wiki_lint_report_detects_duplicate_overlap_candidates(self):
        write(self.root / "wiki" / "index.md", "# Knowledge Base Index\n")
        pages = [
            ("ai-sales-workflows", "AI Sales Workflows"),
            ("ai-sales-workflow-patterns", "AI Sales Workflow Patterns"),
        ]
        for slug, title in pages:
            write(
                self.root / "wiki" / "topic" / f"{slug}.md",
                "\n".join(
                    [
                        "---",
                        "type: wiki_article",
                        f"title: {title}",
                        "updated_at: 2026-06-01",
                        "status: active",
                        "tags:",
                        "  - ai-sales",
                        "  - workflows",
                        "  - gtm",
                        "---",
                        "",
                        f"# {title}",
                        "",
                        "> Sources: test",
                        "",
                        "Sales agents manage account research, outreach, and approval gates.",
                    ]
                ),
            )
        write_source_map(self.root, [])

        report = self.wm.build_wiki_lint_report(self.root, stale_days=999)

        self.assertIn("Duplicate / Overlap Candidates", report)
        self.assertIn("ai-sales-workflows.md", report)
        self.assertIn("ai-sales-workflow-patterns.md", report)


if __name__ == "__main__":
    unittest.main()
