# Changelog

## 1.2.0 (2026-09-03)

- Pin authority (decision E06 = A, ticket T-20260902-508860389): the two previously mutable sources now reference immutable release tags instead of branches — `skills` pins `ellmos-ai/skills@v2026.09.03` (the regenerated public catalog, `registry/components.json` sha256 `6fed91bf…`) and `ticket-master` pins `dev-bricks/ticket-master@v1.11.3` (latest release tag; `main` already carries the unreleased 1.12.0). Tags are maintained by the respective repository owner; a stack re-pin is a deliberate manifest change, never a silent snapshot.

## 1.1.4 (2026-08-01)

- Technical Hygiene & Maintenance Check: Updated `llms.txt` verification timestamp to `2026-08-01`.
- Verified manifest syntax (`agent-ops.manifest.json`), installer script syntax (`install.sh`), GFM callouts, Shields.io badges, Mermaid architecture diagram, and bilingual README parity (EN/DE).

## 1.1.3 (2026-07-29)

- Discoverability & Visibility Maintenance: Updated `llms.txt` verification timestamp to `2026-07-29`.
- Verified GFM callouts, Shields.io badges, Mermaid architecture diagram, and bilingual README parity (EN/DE).

## 1.1.2 (2026-07-27)

- Discoverability & Visibility Maintenance: Refreshed `llms.txt` verification timestamp to `2026-07-27`.
- Verified GFM callouts (`> [!NOTE]`, `> [!TIP]`), SVG banner asset, Shields.io badges, and Mermaid multi-agent architecture diagram across `README.md` and `README_de.md`.

## 1.1.1 (2026-07-26)

- Discoverability & Marketing Audit: Integrated Shields.io status badges (Manifest Schema, 7 Composed Modules, LLM-Ready, MIT License, Ecosystem & Umbrella orgs) in `README.md` and `README_de.md`.
- Added GFM AI Agent Note callouts (`> [!NOTE]`) and Multi-Agent Coordination Tips (`> [!TIP]`) in `README.md` and `README_de.md`.
- Updated `llms.txt` Last-checked timestamp to `2026-07-26`.
- Documented external marketing & visibility recommendations in `MARKETING-LOG.txt`.

## 1.1.0 (2026-07-25)

Seven modules. `sync-master` joins the stack and makes it multi-machine capable —
the first capability added since the initial release.

- Add `sync-master` (dev-bricks/sync-master) as seventh module: serverless
  cross-machine file-sync yard (`file-sync`), making the stack multi-machine
  capable — closes the gap between the agent-ops preset definition and this
  manifest. Updated manifest, READMEs (EN/DE) and wiring diagram.
- After-care: finish the `sync-master` rollout. Added the missing link, the
  `file-sync` capability in summary/positioning/search phrases, and a sixth
  checklist step for multi-machine setups (EN/DE).
- After-care: replaced the leftover `<USER>`/`<AGENT>` anonymization placeholders in
  both READMEs with plain wording — they read like unfilled template slots.

## 1.0.0 (2026-07-04)

- Initial release: `agent-ops.manifest.json` (schema `ellmos-stack-manifest-v1`)
  composing six modules — `ticket-master`, `lock-master`, `build-your-users-mind`,
  `skills`, `ellmos-controlcenter-mcp`, `ellmos-homebase-mcp` — plus `install.sh`
  (clone + wiring-report installer) and README documentation of the wiring and
  module roles.
