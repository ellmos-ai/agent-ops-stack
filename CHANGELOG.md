# Changelog

## [Unreleased]

- **Pfad A (Repository Hygiene, CI Lifecycle Workflows & Level 1 SBOM Audit - 2026-09-29)**:
  - Deployed `.github/workflows/auto-assign.yml` with `actions/github-script@v7`, `timeout-minutes: 5`, concurrency control (`cancel-in-progress: true`), and least-privilege `pull-requests: write`.
  - Deployed `.github/workflows/label-sync.yml` with `EndBug/label-sync@v2`, `timeout-minutes: 5`, concurrency control, and least-privilege `issues: write`.
  - Established canonical `.github/labels.yml` with 11 standard governance labels per `GOVERNANCE.md` §4.2 (`bug`, `enhancement`, `good first issue`, `help wanted`, `documentation`, `duplicate`, `wontfix`, `priority: high`, `priority: low`, `needs-triage`, `stale`).
  - Hardened `.gitignore` with `*-IDEAPAD*`, `*-WORKSTATION.*`, `*-WORKSTATION-LG.*`, OS noise (`Desktop.ini`, `ehthumbs.db`, `*.swo`), and isolated test caches (`.pytest_temp/`, `.pytest_tmp*/`).
  - Standardized PEP 621 metadata in `pyproject.toml` with `license-files` including `THIRD_PARTY_LICENSES.txt`, registered `"Third-Party Licenses (Text)"` under `[project.urls]`, and configured `[tool.pytest.ini_options]` with `addopts = "-ra -v --basetemp=.pytest_temp"` and `norecursedirs` protecting `.pytest_temp`, `.pytest_tmp*`, `.tox`, `.hypothesis`.
  - Created canonical Level 1 SBOM plain text companion `THIRD_PARTY_LICENSES.txt` and re-audited `THIRD_PARTY_LICENSES.md` (Stand 2026-09-29) confirming zero copyleft, unprivileged `RunAsInvoker` user-mode non-elevation, and 100% offline zero-egress execution across all 10 invariants (`INV-LOCAL-01` through `INV-SLA-10`).
  - Synchronized canonical `NOTICE` attribution file with cross-reference to both `THIRD_PARTY_LICENSES.md` and `THIRD_PARTY_LICENSES.txt`.
  - Synchronized Shields.io test status badges in `README.md` and `README_de.md` to reflect 49 passed contract tests (100% green).
  - Refreshed machine-readable LLM context (`llms.txt`) with verification timestamp `2026-09-29`, updated test suite count (49 passed), and Level 1 SBOM text companion reference.
  - Appended Section 12 to `MARKETING-LOG.txt` documenting the Pfad A Technical Hygiene, CI Workflow Lifecycle & Level 1 SBOM Audit.
  - Expanded automated contract test suite (`tests/test_metadata.py`) from 42 to 49 tests (100% green).
  - Version freeze discipline: preserved version `1.3.4` strictly unchanged per `T-20260920-167562623`.

- **Pfad B (Marketing & Design / Visual Lifecycle Architecture & SEO Enhancement - 2026-09-26)**:
  - Designed and integrated interactive multi-agent concurrency state machine (`stateDiagram-v2`) across bilingual landing pages (`README.md` and `README_de.md`) detailing complete lifecycle from task ingestion through fail-closed lock acquisition, decision avatar bounds, MCP profile resolution, test gates, lock release, to slot-gated sync.
  - Enriched Section 5 with comprehensive Component Interoperability & Communication Wire Protocols matrix documenting offline transport channels (POSIX/NTFS file atomics, stdio JSON-RPC, markdown queues, YAML skill definitions).
  - Saturated remote GitHub repository topics to full 20/20 limit and synchronized PEP 621 keywords in `pyproject.toml` identically (`agent-ops`, `ellmos-ai`, `local-first`, `manifest`, `mcp`, `multi-agent`, `agent-coordination`, `claude-code`, `cli-agents`, `codex-cli`, `mcp-control-plane`, `agent-orchestration`, `ai-agents`, `developer-tools`, `file-locking`, `file-sync`, `antigravity-cli`, `offline-first`, `open-bricks`, `zero-egress`).
  - Expanded Section 13 discoverability and SEO keywords across bilingual documentation targeting zero-egress multi-agent coding harnesses, write collision mitigation, and cross-agent workspace concurrency.
  - Re-audited `THIRD_PARTY_LICENSES.md` (Stand 2026-09-26) confirming 100% local-first compliance, zero copyleft, and unprivileged user-mode execution across all 10 governance invariants.
  - Synchronized Shields.io test status badges to reflect 42 passed contract tests (100% green).
  - Refreshed machine-readable LLM context (`llms.txt`) with verification timestamp `2026-09-26` and updated test suite count (42 passed).
  - Appended Section 11 to `MARKETING-LOG.txt` documenting the Pfad B Visual Architecture, Interoperability Protocols & Discoverability Audit.
  - Expanded automated contract test suite (`tests/test_metadata.py`) to 42 tests (100% green) adding assertions for state machine diagrams, wire protocols table, PEP 621 20 keywords saturation, updated license audit date 2026-09-26, and Section 11 marketing ledger.
  - Version freeze discipline: preserved version `1.3.4` strictly unchanged per `T-20260920-167562623`.

- **Pfad A (Repository Hygiene, CI Lifecycle Hardening & Multi-Host Protection Audit - 2026-09-21)**:
  - Deployed `.github/workflows/stale.yml` lifecycle automation with `actions/stale@v9`, daily cron `30 1 * * *`, 10-minute runaway timeout guardrail (`timeout-minutes: 10`), concurrency control (`cancel-in-progress: true`), and least-privilege permissions (`issues: write`, `pull-requests: write`).
  - Deployed `.github/workflows/welcome.yml` first-interaction onboarding automation with `actions/first-interaction@v3`, 5-minute timeout (`timeout-minutes: 5`), concurrency control, and least-privilege permissions (`issues: write`, `pull-requests: write`).
  - Hardened `.gitignore` with extended canonical lock defense (`LOCK.user.*`, `LOCK.until.*`, `LOCK.condition.*`, `.automation-lock`), multi-host cloud-sync collision protection (`*conflicted copy*`, `* (Kopie)*`, `* (Copy)*`, `*-ASUS*`, `*-LAPTOP*`, `*-Mac Studio*`, `*-MacBook*`, `*.rej`), and testing framework artifacts (`.hypothesis/`).
  - Established canonical root attribution file `NOTICE` documenting copyright for Lukas Geiger, `ellmos-ai`, and umbrella ecosystem `open-bricks`.
  - Standardized PEP 621 metadata in `pyproject.toml` with `license-files = ["LICENSE", "NOTICE", "THIRD_PARTY_LICENSES.md"]`, canonical `"Notice"` URL under `[project.urls]`, and `[tool.pytest.ini_options]` options `minversion = "7.0"` and `norecursedirs` guarding `.git`, `.pytest_cache`, `__pycache__`, `build`, `dist`, `.venv`.
  - Re-audited `THIRD_PARTY_LICENSES.md` (Stand 2026-09-21) confirming Level 1 SBOM transparency, zero-copyleft guarantee, unprivileged `RunAsInvoker` non-elevation, and 100% offline zero-egress architecture.
  - Updated machine-readable LLM context (`llms.txt`) with verification timestamp `2026-09-21`, updated test suite count, and canonical `NOTICE` attribution link.
  - Recorded Section 10 in local `MARKETING-LOG.txt` documenting the 2026-09-21 Pfad A Technical Hygiene & Multi-Host Security Audit.
  - Expanded automated contract test suite in `tests/test_metadata.py` validating CI lifecycle workflows, NOTICE attribution, pyproject PEP 621 metadata, extended `.gitignore` patterns, and unreleased CHANGELOG / MARKETING-LOG entries.
  - Version freeze discipline: preserved version `1.3.4` strictly unchanged per `T-20260920-167562623`.

## 1.3.4 (2026-09-16)

- **Pfad B (Marketing & Design / Discoverability Upgrade)**:
  - Standardized bilingual documentation architecture across `README.md` and `README_de.md` to 18-Point Quick Navigation with 100% reciprocal anchor parity, supporting both English and German anchor tags alongside legacy navigation anchors.
  - Added dedicated Section 3 "Target Personas & Discoverability" defining 4 target personas (`[PERSONA-01]` Autonomous AI Agent Framework & Multi-Agent Swarm Engineers, `[PERSONA-02]` Multi-Host & Edge Infrastructure Systems Engineers, `[PERSONA-03]` Solo Developers & Tool Builders, `[PERSONA-04]` Enterprise Tooling, Safety & Governance Compliance Officers) and bilingual high-intent search queries.
  - Added dedicated Section 4 "Comparative Matrix vs. Alternatives" evaluating `agent-ops-stack` against 4 alternatives (Cloud SaaS Agent Hubs / Telemetry SaaS, Monolithic Agent Orchestration Frameworks, Ad-Hoc Shell Scripts & Uncoordinated Worktrees, Traditional Message Queues / Heavy Brokers) across 10 architectural and governance dimensions mapped to `INV-LOCAL-01` through `INV-SLA-10`.
  - Re-audited `THIRD_PARTY_LICENSES.md` (Stand 2026-09-16) confirming all 10 governance & runtime invariants, zero copyleft, and unprivileged user-mode `RunAsInvoker`.
  - Refreshed machine-readable LLM context (`llms.txt`) with verification timestamp `2026-09-16`, version `1.3.4`, and updated contract test suite count (31 tests passed | 100% green).
  - Synchronized Shields.io status badges across bilingual landing pages to reflect version `1.3.4` and 31 passed contract tests (100% green).
  - Appended Section 9 to `MARKETING-LOG.txt` documenting the Pfad B Discoverability, 18-Point Navigation & Comparative Matrix Audit Record (Stand 2026-09-16).
  - Expanded automated contract test suite (`tests/test_metadata.py`) from 25 to 31 tests (100% green) covering 18-point navigation, reciprocal anchor parity, personas, 10-dimension comparative matrix, license inventory, invariants, and version parity.

## 1.3.3 (2026-09-12)

- **Pfad A (Repository Hygiene, CI Timeout Hardening & Lock Defense)**:
  - Hardened GitHub Actions CI (`.github/workflows/ci.yml`) with 15-minute execution timeout guardrail (`timeout-minutes: 15`), least-privilege security block (`permissions: contents: read`), and standardized `python -m pytest -ra -v` execution across Ubuntu, Windows, and macOS.
  - Hardened `.gitignore` against multi-host cloud sync conflicts and canonical lock patterns (`* (kopie)*`, `* (copy)*`, `*-WORKSTATION*`, `*-WORKSTATION-LG*`, `*-ASUS-GEI*`, `*.orig`, `uv.lock`, `!package-lock.json`, `.coverage.*`, `.tox/`, `.turbo/`, `.nyc_output/`, `.mypy_cache/`).
  - Standardized PEP 621 metadata in `pyproject.toml` by registering `"LLM Ready"` and `"Bug Tracker"` in `[project.urls]` and expanding Ruff linting rule sets to include `UP`, `B`, `SIM`, `C4`, `RUF`.
  - Refreshed machine-readable LLM context (`llms.txt`) with verification timestamp `2026-09-12`, version `1.3.3`, and updated contract test suite count (25 tests passed | 100% green).
  - Synchronized Shields.io status badges across bilingual landing pages (`README.md` and `README_de.md`) to reflect version `1.3.3` and 25 passed contract tests.
  - Expanded automated contract test suite (`tests/test_metadata.py`) from 19 to 25 tests (100% green) adding assertions for CI timeout guardrail, PEP 621 URLs, Ruff rulesets, extended `.gitignore` patterns, and CHANGELOG Pfad A release entry.
  - Recorded Pfad A hygiene operations in local `MARKETING-LOG.txt`.

## 1.3.2 (2026-09-10)

- **Pfad B (Marketing & Design / Discoverability) Upgrade**:
  - Expanded Quick Navigation to 15 points with deep anchors across bilingual `README.md` and `README_de.md`, adding dedicated Section 13 for Third-Party Licenses & Transparency.
  - Added comprehensive `THIRD_PARTY_LICENSES.md` inventory detailing Python standard library runtime modules (PSFL-2.0), packaging/build tooling (`setuptools`), contract test harness (`pytest`), code formatting/linter (`ruff`), and composed stack modules under permissive open-source licenses with zero-egress guarantees.
  - Upgraded Shields.io badge suite with Security SLA (`48h / 5d triage`), Third-Party Audited (`Audited`), Marketing Log (`Active`), Code style Ruff, Version `1.3.2`, and updated contract test badge (`19 passed | 100%`).
  - Standardized PEP 621 URLs in `pyproject.toml` with `"Third-Party Licenses"` and `"Marketing Log"`.
  - Comprehensive refresh of `MARKETING-LOG.txt` with 4 detailed developer personas, high-intent bilingual search queries, competitive positioning analysis vs. cloud SaaS and monolithic frameworks, and canonical governance invariant mapping.
  - Expanded automated contract test suite in `tests/test_metadata.py` to 19 tests (100% green) validating third-party license notices, marketing log personas, pyproject URLs, 15-point quick navigation, and version parity.
  - Updated `llms.txt` timestamp to `2026-09-10`, version `1.3.2`, 19 tests count, and links to license and marketing ledgers.

## 1.3.1 (2026-09-09)

- **Pfad A (Repository Hygiene & CI/Metadata Hardening)**:
  - Hardened `.gitignore` with comprehensive multi-host sync conflict patterns (`*-conflict-*`, `*.sync-temp-*`, `*.sync-conflict-*`, `*.conflict`, `*-CONFLIT-*`), multi-agent lock patterns (`LOCK`, `LOCK.*`, `*.lock`, `LOCK*.txt`, `LOCK.permissions.json`), and test/packaging caches (`wheelhouse/`, `.wheel-smoke/`, `build/`, `dist/`, `coverage/`).
  - Standardized `[tool.pytest.ini_options]` in `pyproject.toml` with `addopts = "-ra -v"`.
  - Hardened GitHub Actions CI (`.github/workflows/ci.yml`) with Python bytecode compilation gate (`python -m compileall -q tests`) and standardized `pytest -ra -v` execution across Ubuntu, Windows, and macOS on Python 3.10-3.13.
  - Expanded automated contract test suite in `tests/test_metadata.py` with 4 new contract tests (15/15 passed | 100% green) verifying `.gitignore` hygiene rules, pytest CLI flags, CI workflow compilation steps, and Security SLA/contact parity.
  - Bumped version to `1.3.1` across `pyproject.toml`, `README.md`, `README_de.md`, `llms.txt`, `CHANGELOG.md`, and contract test assertions.
  - Refreshed `llms.txt` verification timestamp to `2026-09-09`.

## 1.3.0 (2026-09-08)

- **Pfad B (Marketing & Design / Discoverability) Upgrade**:
  - Implemented 14-Point Quick Navigation architecture across bilingual `README.md` and `README_de.md`.
  - Expanded Shields.io status badge suite: Manifest Schema, Version 1.3.0, CI GitHub Actions, 11 Contract Tests passed (100% green), 7 Composed Modules, Python 3.10-3.13, Multi-Platform (Linux/Windows/macOS), 100% Local-First Zero-Egress, Non-Elevation Sandboxed Security, MIT License, Ecosystem `ellmos-ai`, Umbrella `open-bricks`, and LLM-Ready `llms.txt`.
  - Integrated dual interactive Mermaid diagrams: System Architecture Flowchart (`flowchart TD` with `AGENTS`, `COORDINATION`, `DECISION`, `MCP`, `SYNC` subgraphs) and Multi-Agent Operational Lifecycle (`sequenceDiagram` depicting the 10-step coordination cycle).
  - Established Governance & Runtime Invariants table defining 10 formal operational rules and failure-state guarantees.
  - Integrated 12 Sibling Ecosystem and Cross-Integration Matrix connecting tools across `ellmos-ai`, `dev-bricks`, and `open-bricks`.
  - Hardened bilingual Security Policy (`SECURITY.md`) with 48h response SLA, 5-day triage commitment, GitHub Security Advisories private reporting link, official security contacts, and 7 core invariants.
  - Standardized PEP 621 packaging metadata in `pyproject.toml` with standard repository URLs, classifiers, and tool configurations.
  - Added Multi-OS CI workflow (`.github/workflows/ci.yml`) validating Python 3.10-3.13 across Ubuntu, Windows, and macOS, with bash script syntax checks and manifest validation.
  - Implemented automated metadata and contract test suite (`tests/test_metadata.py`) covering manifest integrity, installer parsing, bilingual README parity, badges, navigation anchors, Mermaid syntax, and PEP 621 parity.
  - Refreshed `llms.txt` timestamp to `2026-09-08` and created local `MARKETING-LOG.txt`.

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
