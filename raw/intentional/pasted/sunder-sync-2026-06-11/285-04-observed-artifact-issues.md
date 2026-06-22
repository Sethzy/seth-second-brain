---
type: raw_capture
source_type: pasted
title: "Sunder sync: 04-observed-artifact-issues.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/04-observed-artifact-issues.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/04-observed-artifact-issues.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/skills-system/04-observed-artifact-issues.md"
sha256: "3151100fb4afcbc1888411da6e4262a5441507c2f0c0d3fa2f9e7903f1e67e0a"
duplicate_of: ""
---

# Sunder sync: 04-observed-artifact-issues.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/04-observed-artifact-issues.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/skills-system/04-observed-artifact-issues.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Observed Artifact Issues

This file records obvious corruption/truncation artifacts in the pasted source so future cleanup can distinguish source errors from interpretation errors.

## Building Preview Apps Skill

Examples observed in source capture:
- `index.h` appears instead of `index.html` in one rule line.
- `cdnjsloudflare.com` appears instead of `cdnjs.cloudflare.com` in one script URL.
- Snippet fragment `awERT INTO todos...` appears malformed.
- Fragment `returnsync function sqlExec(query)` appears malformed.
- Fragment `runhe full prefixed name` appears truncated.
- Final React line appears malformed: `ReactDOM.createRoot(document.getElementById('root'.render(<App />);`

## Interpretation Policy Used

- `00-source-skills-verbatim.md` preserves pasted text as provided.
- Normalized docs translate intent without silently fixing source artifacts.

## Follow-Up

If you want, I can create a "clean-room corrected" version of the same skill docs in a separate file set for implementation use.


