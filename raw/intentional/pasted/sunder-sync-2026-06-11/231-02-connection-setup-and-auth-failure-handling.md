---
type: raw_capture
source_type: pasted
title: "Sunder sync: 02-connection-setup-and-auth-failure-handling.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/02-connection-setup-and-auth-failure-handling.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/02-connection-setup-and-auth-failure-handling.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/02-connection-setup-and-auth-failure-handling.md"
sha256: "8fd22e7f2fbbf95abdca4e1fdbb62784ae8e310d7e757e3ecec109775d89de9f"
duplicate_of: ""
---

# Sunder sync: 02-connection-setup-and-auth-failure-handling.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/02-connection-setup-and-auth-failure-handling.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/extracted_content/Important Articles/tasklet/complex-multi-integration-workflow/02-connection-setup-and-auth-failure-handling.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Connection Setup and Auth Failure Handling

## Minimal-permission setup path

1. Check existing connections.
2. Discover calendar integration.
3. Verify capability coverage.
4. Create connection with least-required tools activated.

## Expected auth outcomes

1. User approves OAuth
- connection created
- tools activated
- run can proceed

2. User skips OAuth
- cannot execute workflow
- prompt retry/alternative provider path

3. Partial permission grant
- detect missing fields on first API call
- explain missing scope and request reauthorization

4. Expired/revoked token
- detect auth error (401/403-like)
- run reauthorization flow
- preserve trigger configuration (do not destroy pipeline)

## Reliability recommendation

Treat auth failures as operational incidents with explicit logging and user-visible remediation tasks, not silent skips.


