# Changelog

## Unreleased

- Add `sync-master` (dev-bricks/sync-master) as seventh module: serverless
  cross-machine file-sync yard (`file-sync`), making the stack multi-machine
  capable — closes the gap between the agent-ops preset definition and this
  manifest. Updated manifest, READMEs (EN/DE) and wiring diagram.

- Technical hygiene audit: updated `llms.txt` timestamp to 2026-07-21.
- Validated `agent-ops.manifest.json` schema composition and `install.sh` syntax.
- Confirmed repository alignment with `ellmos-stack-manifest-v1` standards.

## 1.0.0 (2026-07-04)

- Initial release: `agent-ops.manifest.json` (schema `ellmos-stack-manifest-v1`)
  composing six modules — `ticket-master`, `lock-master`, `build-your-users-mind`,
  `skills`, `ellmos-controlcenter-mcp`, `ellmos-homebase-mcp` — plus `install.sh`
  (clone + wiring-report installer) and README documentation of the wiring and
  module roles.
