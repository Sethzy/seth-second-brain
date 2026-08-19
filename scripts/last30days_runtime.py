#!/usr/bin/env python3
"""Locate the optional Last30Days runtime without depending on one Mac path."""

from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def candidate_script_dirs() -> list[Path]:
    configured = os.environ.get("LAST30DAYS_SCRIPTS_DIR")
    candidates = [
        Path(configured).expanduser() if configured else None,
        ROOT / ".agents" / "skills" / "last30days" / "scripts",
        Path.home() / ".agents" / "skills" / "last30days" / "scripts",
        Path.home() / ".codex" / "skills" / "last30days" / "scripts",
        Path.home() / "Documents" / "gtm-workspace" / ".agents" / "skills" / "last30days" / "scripts",
        Path.home() / "Documents" / "openai-interview-prep" / "skills" / "last30days" / "scripts",
    ]
    return [path.resolve() for path in candidates if path is not None]


def resolve_last30days_scripts_dir() -> Path:
    for path in candidate_script_dirs():
        if (path / "last30days.py").is_file() and (path / "lib" / "env.py").is_file():
            return path
    searched = "\n  - ".join(str(path) for path in candidate_script_dirs())
    raise RuntimeError(
        "Last30Days is optional but required for this command. Install the "
        "mvanhorn/last30days-skill, or set LAST30DAYS_SCRIPTS_DIR to its scripts directory. "
        f"Searched:\n  - {searched}"
    )


def extract_browser_credentials(profile: str) -> dict[str, str]:
    scripts_dir = resolve_last30days_scripts_dir()
    scripts_value = str(scripts_dir)
    if scripts_value not in sys.path:
        sys.path.insert(0, scripts_value)

    from lib import env  # type: ignore

    credentials = env.extract_browser_credentials(
        {
            "FROM_BROWSER": "chrome",
            "LAST30DAYS_CHROME_PROFILE": profile,
        }
    )
    if not credentials.get("AUTH_TOKEN") or not credentials.get("CT0"):
        raise RuntimeError(f"Could not extract X auth cookies from Chrome {profile}.")
    return credentials


if __name__ == "__main__":
    try:
        print(resolve_last30days_scripts_dir())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
