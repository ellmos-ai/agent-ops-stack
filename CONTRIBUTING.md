# Contributing to agent-ops-stack

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

Thank you for your interest in contributing to **agent-ops-stack**!

### Architectural Principles & Quality Invariants

`agent-ops-stack` is a declarative, manifest-driven composition layer engineered for multi-agent CLI coordination (Claude Code, OpenAI Codex, Google Antigravity / Gemini, Moonshot Kimi) on local developer machines. All contributions must respect our foundational architectural and governance invariants:

1. **Local-First & Zero-Egress (`INV-LOCAL-01`)**: Operates 100% offline on local filesystems and local storage mounts; zero telemetry, zero analytics, zero external network calls by default.
2. **Unprivileged User-Mode Execution (`RunAsInvoker` / `INV-USER-02`)**: Executes safely in unprivileged user space (`RunAsInvoker`) without requiring root, sudo, or UAC administrator elevation.
3. **Fail-Closed Lock Integrity (`INV-LOCK-03`)**: Mutating operations halt immediately upon active `LOCK*.txt` files or conflicting sessions, preventing split-brain states or destructive Git index corruption across concurrent AI agent sessions.
4. **Structured Ticket Routing (`INV-ROUT-04`)**: Problem reports, subtasks, and change requests are recorded and dispatched through `ticket-master` prior to workspace modifications.
5. **Empirical Decision-Avatar Fallback (`INV-AVAT-05`)**: When the human operator is away, ambiguous architectural trade-offs resolve via `build-your-users-mind` empirical theory-of-mind models instead of unbounded speculative agent actions.
6. **Deterministic Manifest Blueprint (`INV-MANI-06`)**: All module definitions, wiring, and role boundaries conform strictly to the `ellmos-stack-manifest-v1` schema in `agent-ops.manifest.json`.
7. **Immutable Release-Tag Pinning (`INV-PIN-07`)**: Composed modules reference immutable release tags and verified source repositories; zero unpinned branch drift.
8. **Sandboxed Installer Boundary (`INV-SAND-08`)**: The declarative installer (`install.sh`) clones modules exclusively into the gitignored `./modules/` sandbox directory.
9. **Cross-Device Slot-Gated Sync (`INV-SYNC-09`)**: Multi-host file synchronization relies on dedicated `sync-master` host slots, preventing concurrent cloud collision copies and broken Git trees.
10. **Dual Security Response & Triage SLA (`INV-SLA-10`)**: Committed 48-hour response and 5-business-day triage commitment via canonical security channels (`security@ellmos.ai`, `security@open-bricks.org`).

### Development Guidelines

- **Plan D Architecture**: Development, git operations, and tests occur strictly in the local git repository clone (`C:\_Local_DEV\repos\agent-ops-stack`).
- **Version Freeze Discipline**: Version `1.3.4` is strictly frozen per `T-20260920-167562623`. Do not bump the package version; document all modifications under `## [Unreleased]` in `CHANGELOG.md`.
- **Python Version Support**: Compatible with Python 3.10 through 3.13.
- **Pre-commit Quality Gates**:
  - Bytecode compilation: `python -m compileall -q .`
  - Linting: `python -m ruff check .`
  - Automated contract test suite: `python -m pytest -ra -v` (100% green required)
  - Whitespace & formatting check: `git diff --check`
- **Security Vulnerabilities**: Please do not report security vulnerabilities publicly. Follow our [SECURITY.md](SECURITY.md) guidelines for responsible disclosure (48h response SLA via `security@ellmos.ai`).
- **Statutory Limitation of Liability**: Dieses Projekt ist eine unentgeltliche Open-Source-Schenkung im Sinne der §§ 516 ff. BGB. Die Haftung ist gemäß **§ 521 BGB** auf Vorsatz und grobe Fahrlässigkeit beschränkt.

---

<a id="deutsch"></a>
## Deutsch

Vielen Dank für Ihr Interesse an einer Mitarbeit an **agent-ops-stack**!

### Architektur-Prinzipien & Qualitäts-Invarianten

`agent-ops-stack` ist eine deklarative, manifest-gesteuerte Kompositionsschicht für die Multi-Agenten-CLI-Koordination (Claude Code, OpenAI Codex, Google Antigravity / Gemini, Moonshot Kimi) auf lokalen Entwicklungsrechnern. Alle Beiträge müssen unsere grundlegenden Invarianten einhalten:

1. **100% Local-First & Zero-Egress (`INV-LOCAL-01`)**: Vollständige lokale Ausführung auf lokalen Dateisystemen; null Telemetrie, null Cloud-Zwang, null Egress-Aufrufe.
2. **Unprivilegierter Ausführungsmodus (`RunAsInvoker` / `INV-USER-02`)**: Läuft sicher im normalen Benutzerkontext (`RunAsInvoker`) ohne Root-, Sudo- oder Administrator-Elevation.
3. **Fail-Closed Lock-Integrität (`INV-LOCK-03`)**: Mutierende Operationen brechen bei aktiven `LOCK*.txt`-Dateien oder Sperren sofort fail-closed ab, um Split-Brain-Zustände und Git-Index-Beschädigungen bei konkurrierenden Agenten zu verhindern.
4. **Strukturierte Ticket-Steuerung (`INV-ROUT-04`)**: Fehlermeldungen, Teilaufgaben und Änderungsanträge werden vor Datei-Mutationen über `ticket-master` strukturiert erfasst und zugewiesen.
5. **Empirischer Entscheidungs-Avatar (`INV-AVAT-05`)**: Bei Abwesenheit des menschlichen Entwicklers löst `build-your-users-mind` architektonische Mehrdeutigkeiten empirisch fundiert auf, statt spekulative Blindänderungen durchzuführen.
6. **Deterministischer Manifest-Bauplan (`INV-MANI-06`)**: Alle Moduldefinitionen, Schnittstellen und Rollengrenzen folgen strikt dem `ellmos-stack-manifest-v1`-Schema in `agent-ops.manifest.json`.
7. **Unveränderliche Release-Tag-Bindung (`INV-PIN-07`)**: Komponierte Module referenzieren unveränderliche Release-Tags; kein unkontrollierter Branch-Drift.
8. **Isolierte Installer-Grenzen (`INV-SAND-08`)**: Der deklarative Installer (`install.sh`) klont Module ausschließlich in das git-ignorierte Verzeichnis `./modules/`.
9. **Geräteübergreifender Slot-Sync (`INV-SYNC-09`)**: Dateiabgleiche zwischen mehreren Rechnern nutzen dedizierte Host-Slots via `sync-master`, um Cloud-Konfliktkopien und Git-Kollisionen auszuschließen.
10. **Zweisprachige Sicherheits-SLA (`INV-SLA-10`)**: Verbindliche 48-Stunden-Reaktionszeit und 5 Tage Triage-Zusage über offizielle Sicherheitskontakte (`security@ellmos.ai`, `security@open-bricks.org`).

### Richtlinien für Entwickler

- **Plan D Entwicklung**: Entwicklung, Git-Aktionen und Tests erfolgen ausschließlich im lokalen Git-Repository (`C:\_Local_DEV\repos\agent-ops-stack`).
- **Version-Freeze Disziplin**: Version `1.3.4` bleibt gemäß Richtlinie `T-20260920-167562623` eingefroren; Neuerungen werden unter `## [Unreleased]` im `CHANGELOG.md` gepflegt.
- **Python-Unterstützung**: Python 3.10 bis 3.13.
- **Qualitäts-Tore vor Commits**:
  - Bytecode-Prüfung: `python -m compileall -q .`
  - Linter: `python -m ruff check .`
  - Testsuite: `python -m pytest -ra -v` (100% grün erforderlich)
  - Whitespace-Prüfung: `git diff --check`
- **Sicherheitsmeldungen**: Sicherheitslücken bitte nicht öffentlich melden, sondern gemäß [SECURITY.md](SECURITY.md) vertraulich einreichen (48h Reaktions-SLA via `security@ellmos.ai`).
- **Gesetzlicher Haftungsausschluss**: Dieses Projekt ist eine unentgeltliche Open-Source-Schenkung im Sinne der §§ 516 ff. BGB. Die Haftung ist gemäß **§ 521 BGB** auf Vorsatz und grobe Fahrlässigkeit beschränkt.
