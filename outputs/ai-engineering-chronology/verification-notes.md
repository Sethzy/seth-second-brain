# AI Engineering Big Shifts Verification Notes

Date: 2026-06-14

## Retrieval Checks

- Used QMD first across the updated Seth Second Brain corpus.
- Retrieved local synthesis pages and raw captures for agent platforms, OpenClaw/Clawchief, Codex use cases/security, Cursor third-era/Cursor 3, agentic engineering practices, vendor-blog sweep, and Claude context engineering.
- Used external primary pages only where local raw captures were missing or where current product/model state mattered.
- Treated incomplete captures and noisy sweep material as leads only.

## Static Checks

- Confirmed `index.html` now contains 9 high-level timeline milestones rather than the previous 73 dated micro-events.
- Confirmed 9 filters: all, model, surface, open, harness, workflow, context, verify, and governance.
- Confirmed all 9 milestones include at least one source chip.
- Confirmed `research-ledger.md` has one source-map row for each shift.
- Checked for common draft/debug markers and viewport-scaled type rules; no matches.

## Browser Checks

Served the standalone folder locally at `http://127.0.0.1:8765/` for browser verification.

Desktop audit at 1280px viewport:

- Page title: `AI Engineering: Six-Month Progression`.
- 9 timeline milestones rendered.
- 28 source chips rendered.
- 0 old `.shift` grid cards rendered.
- No page-level horizontal overflow.
- Screenshot: `screenshots/desktop-timeline-viewport.png`.

Mobile audit at 390px viewport:

- 9 timeline milestones rendered.
- 28 source chips rendered.
- No page-level horizontal overflow.
- No offscreen DOM nodes detected.
- Screenshot: `screenshots/mobile-timeline-viewport.png`.

Interaction audit:

- Clicking `Open/local OS` narrows the timeline to the OpenClaw milestone.
- Clicking `Work surfaces` narrows the timeline to the two surface milestones.
- Resetting to `All` restores all 9 milestones.

## Remaining Notes

- The artifact intentionally prioritizes scanability over exhaustive chronology.
- OpenClaw is labeled as an emerging open/local agent-OS signal, not an industry-wide adoption proof.
- The model milestone is phrased as a frontier coding-model jump rather than pinning the whole story to one exact model point release.
