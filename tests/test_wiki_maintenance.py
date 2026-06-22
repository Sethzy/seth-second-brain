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


if __name__ == "__main__":
    unittest.main()
