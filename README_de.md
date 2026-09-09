<img src="assets/banner.svg" alt="agent-ops-stack" width="100%">

<p align="center">
  <a href="https://github.com/ellmos-ai/agent-ops-stack"><img src="https://img.shields.io/badge/Manifest-ellmos--stack--manifest--v1-blue.svg" alt="Manifest Schema"></a>
  <a href="https://github.com/ellmos-ai/agent-ops-stack"><img src="https://img.shields.io/badge/version-1.3.1-blue.svg" alt="Version"></a>
  <a href="https://github.com/ellmos-ai/agent-ops-stack/actions/workflows/ci.yml"><img src="https://img.shields.io/badge/CI-GitHub%20Actions-brightgreen.svg" alt="CI-Status"></a>
  <a href="tests/"><img src="https://img.shields.io/badge/tests-15%20passed%20%7C%20100%25-brightgreen.svg" alt="Tests"></a>
  <a href="agent-ops.manifest.json"><img src="https://img.shields.io/badge/Composed__Modules-7-informational.svg" alt="Komponierte Module"></a>
  <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg" alt="Python Versionen">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg" alt="Plattformen">
  <img src="https://img.shields.io/badge/architecture-100%25%20Local--First%20%7C%20Zero--Egress-success.svg" alt="Local-First Architektur">
  <img src="https://img.shields.io/badge/security-Non--Elevation%20%7C%20Sandboxed-informational.svg" alt="Sicherheits-Invariante">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="Lizenz"></a>
  <a href="https://github.com/ellmos-ai"><img src="https://img.shields.io/badge/Ecosystem-ellmos--ai-purple.svg" alt="Ökosystem"></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/Umbrella-open--bricks-blue.svg" alt="Dachorganisation"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/LLM--Ready-llms.txt-success.svg" alt="LLM-Bereit"></a>
</p>

# agent-ops-stack

**🇬🇧 [English version](README.md)**

Eine manifest-getriebene Komposition des lokalen **Agent-Ops**-Ökosystems: die
Koordinationsschicht, die es einem oder mehreren KI-Coding-Agenten (Claude Code, Codex,
Gemini/Antigravity, Kimi oder jedem anderen CLI-Agenten) erlaubt, effektiv und ohne
Rennbedingungen auf derselben Entwickler-Maschine zusammenzuarbeiten, Aufgaben deterministisch
zu routen, in Abwesenheit des menschlichen Operators fundierte Entscheidungen zu treffen
und Multi-Device-Workflows sicher abzugleichen.

Dieses Repository ist Komposition und Dokumentation, kein monolithischer Quellcode: Es listet
sieben fokussierte, eigenständig gepflegte Module in [`agent-ops.manifest.json`](agent-ops.manifest.json)
auf und liefert einen schlanken Installer ([`install.sh`](install.sh)), der ihre Verdrahtung
klont und visualisiert. Siehe [ellmos-ai/stacks](https://github.com/ellmos-ai/stacks) für
die gemeinsame Stack-Manifest-Spezifikation und den Katalog aller Stacks.

Maschinenlesbarer Kontext für LLMs und agentische Coding-Tools: [`llms.txt`](llms.txt).

> [!NOTE]
> **KI-Agenten- & LLM-Kontext**: Dieses Repository bietet strukturierten, maschinenlesbaren Kontext via [`llms.txt`](llms.txt). Autonome CLI-Agenten (Claude Code, Codex, Gemini/Antigravity, Kimi) können diese manifest-gesteuerte Komposition parsen, um lokale Koordination, Sperren, Ticket-Routing, Entscheidungs-Avatare und MCP-Server-Steuerungsebenen zu verstehen.

---

### Schnellnavigation

1. [Architektur & Überblick](#1-architektur--überblick)
2. [Was ist Agent-Ops?](#2-was-ist-agent-ops)
3. [Komponierte Module (Die 7 Säulen)](#3-komponierte-module-die-7-säulen)
4. [Systemarchitektur-Flussdiagramm](#4-systemarchitektur-flussdiagramm)
5. [Multi-Agenten-Lebenszyklus-Sequenz](#5-multi-agenten-lebenszyklus-sequenz)
6. [Governance- & Laufzeit-Invarianten](#6-governance--laufzeit-invarianten)
7. [Wie ein Agent diesen Stack nutzt](#7-wie-ein-agent-diesen-stack-nutzt)
8. [Schnellstart & Installation](#8-schnellstart--installation)
9. [Manifest-Schema-Spezifikation](#9-manifest-schema-spezifikation)
10. [Geschwister-Ökosystem & Integrationsmatrix](#10-geschwister-ökosystem--integrationsmatrix)
11. [Suche & Begriffsklärung](#11-suche--begriffsklärung)
12. [Sicherheit & Verifikation](#12-sicherheit--verifikation)
13. [Lizenz](#13-lizenz)
14. [Haftung / Liability](#14-haftung--liability)

---

## 1. Architektur & Überblick

Wenn mehrere autonome oder interaktive CLI-Coding-Agenten gleichzeitig auf dem lokalen System
eines Entwicklers arbeiten, fehlen Standard-Dateisystemen native Nebenläufigkeitskontrollen,
gemeinsame Aufgabenregister und sitzungsübergreifende Gedächtnisse. `agent-ops-stack` bündelt
die unverzichtbaren lokalen Werkzeuge in einem kohärenten, deklarativen Stack:

| Dimension | Spezifikation |
|:---|:---|
| **Manifest-Schema** | `ellmos-stack-manifest-v1` ([`agent-ops.manifest.json`](agent-ops.manifest.json)) |
| **Komponierte Säulen** | 7 spezialisierte Module für Koordination, Sync, Entscheidungen, Skills und MCP |
| **Netzwerk-Profil** | 100% Local-First & Zero Egress (vollständig offline, keine externe Telemetrie) |
| **Rechte-Modell** | Unprivilegierter User-Mode (Non-Elevation; keinerlei Root-/Admin-Rechte erforderlich) |
| **Ziel-Laufzeit** | Linux, macOS und Microsoft Windows (vollständige plattformübergreifende Parität) |
| **Agenten-Unterstützung** | Claude Code, OpenAI Codex, Google Antigravity / Gemini, Moonshot Kimi, CLI-Agenten |

```
dein KI-Coding-Agent
├── MCP-Zugänge (direkter stdio-Kontakt)
│   ├── controlcenter-mcp   → control-plane (nutzt: skill-pack)
│   └── homebase-mcp        → mcp-runtime, memory-facade, task-facade (nutzt: locking, ticket-routing)
└── datei-/protokollbasierte Konventionen (Agent liest & befolgt direkt)
    ├── ticket-master           → ticket-routing
    ├── lock-master             → locking
    ├── sync-master             → file-sync
    ├── build-your-users-mind   → decision-avatar (nutzt: interaction-logs)
    └── skills                  → skill-pack
```

---

## 2. Was ist Agent-Ops?

Jeder KI-Coding-Agent, der auf dem lokalen System des Nutzers operiert, stößt wiederholt auf
dieselben Fragestellungen, bevor er Quellcodedateien modifiziert:
- *Bearbeitet gerade ein anderer Agent oder eine Automation denselben Arbeitsbereich?*
- *Wo werden entdeckte Fehler, Änderungswünsche oder Teilaufgaben nachvollziehbar erfasst und geroutet?*
- *Wie würde der menschliche Operator bei unklaren Architekturentscheidungen in seiner Abwesenheit entscheiden?*
- *Welche wiederverwendbaren Skills, Workflows oder MCP-Server-Bündel stehen bereit?*
- *Wie werden Dateiänderungen über mehrere Rechner synchronisiert, ohne lokale Git-Locks zu beschädigen?*

`agent-ops-stack` löst diese Herausforderungen mit sieben fokussierten, zusammensetzbaren
Modulen statt eines monolithischen Frameworks. Jedes Modul ist unabhängig nutzbar und versioniert,
jedoch über deklarative Schnittstellen harmonisiert.

---

## 3. Komponierte Module (Die 7 Säulen)

| Modul | Rolle | Liefert (`provides`) | Nutzt (`consumes`) | Repository |
|:---|:---|:---|:---|:---|
| **ticket-master** | Plattformübergreifende Workflow-Engine: Erfasst Problembeschreibungen, bewertet Prioritäten und routet Tickets an die zuständigen Repositories oder Delegaten | `ticket-routing` | — | [dev-bricks/ticket-master](https://github.com/dev-bricks/ticket-master) |
| **lock-master** | Abhängigkeitsfreies Datei-Sperrsystem (`LOCK*.txt`): Signalisiert Projektbenutzung, um nebenläufige Schreibkonflikte zuverlässig zu verhindern | `locking` | — | [dev-bricks/lock-master](https://github.com/dev-bricks/lock-master) |
| **sync-master** | Serverlose Datei-Synchronisation: Verwaltet Rechner-Slots und tägliche Abgleichs-Rituale über Multi-Geräte-Setups | `file-sync` | — | [dev-bricks/sync-master](https://github.com/dev-bricks/sync-master) |
| **build-your-users-mind** | Empirischer Nutzer-Entscheidungsavatar: Baut aus Interaktionslogs ein Theory-of-Mind-Modell auf, um bei Abwesenheit im Sinne des Nutzers zu entscheiden | `decision-avatar` | `interaction-logs` | [ellmos-ai/build-your-users-mind](https://github.com/ellmos-ai/build-your-users-mind) |
| **skills** | Portable KI-Skill-Bibliothek im Anthropic-`SKILL.md`-Format: Eigenständige Prozess-Skills, Entwickler-Workflows und Utility-Tools | `skill-pack` | — | [ellmos-ai/skills](https://github.com/ellmos-ai/skills) |
| **controlcenter-mcp** | MCP-Steuerebene: Erkennt lokale MCP-Server, liest Profil-Dateien, bildet Fähigkeitsbündel und empfiehlt Werkzeugkonfigurationen | `control-plane` | `skill-pack` | [ellmos-ai/ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp) |
| **homebase-mcp** | Local-First-MCP-Server für gemeinsamen Zustand, Wissensspeicher, Routing und Task-Fassade über kanonischen lokalen Speichern | `mcp-runtime`, `memory-facade`, `task-facade` | `locking`, `ticket-routing` | [ellmos-ai/ellmos-homebase-mcp](https://github.com/ellmos-ai/ellmos-homebase-mcp) |

---

## 4. Systemarchitektur-Flussdiagramm

Das folgende interaktive Mermaid-Flussdiagramm visualisiert die funktionale Schichtenarchitektur
der sieben Module im Zusammenspiel mit den aktiven Coding-Agenten:

```mermaid
flowchart TD
  subgraph AGENTS ["Active Coding Agents"]
    A1["Claude Code"]
    A2["Codex"]
    A3["Gemini / Antigravity"]
    A4["Kimi / CLI Agent"]
  end

  subgraph COORDINATION ["Coordination & Locks"]
    TM["dev-bricks/ticket-master\n(ticket-routing)"]
    LM["dev-bricks/lock-master\n(locking)"]
  end

  subgraph DECISION ["Decision & Memory Layer"]
    BYUM["ellmos-ai/build-your-users-mind\n(decision-avatar)"]
    SK["ellmos-ai/skills\n(skill-pack)"]
  end

  subgraph MCP ["MCP Control Plane & Runtime"]
    CC["ellmos-ai/ellmos-controlcenter-mcp\n(control-plane)"]
    HB["ellmos-ai/ellmos-homebase-mcp\n(mcp-runtime)"]
  end

  subgraph SYNC ["Cross-Host File Synchronization"]
    SM["dev-bricks/sync-master\n(file-sync)"]
  end

  AGENTS -->|1. Check Locks| LM
  AGENTS -->|2. Route Requests| TM
  AGENTS -->|3. Evaluate Intent| BYUM
  AGENTS -->|4. Discover Profiles| CC
  CC -->|Loads Packs| SK
  AGENTS -->|5. Store Memory & State| HB
  LM -->|Guards Access| HB
  TM -->|Provides Routing| HB
  AGENTS -->|6. Align Machines| SM
```

---

## 5. Multi-Agenten-Lebenszyklus-Sequenz

Das folgende Sequenzdiagramm zeigt den vollständigen Lebenszyklus eines agentischen
Coding-Auftrags innerhalb des `agent-ops-stack`-Ablaufs:

```mermaid
sequenceDiagram
  autonumber
  participant User as User / Operator
  participant Agent as AI Coding Agent (CLI)
  participant LockMaster as lock-master (Locks)
  participant TicketMaster as ticket-master (Tickets)
  participant BYUM as build-your-users-mind (Avatar)
  participant ControlCenter as controlcenter-mcp (MCP)
  participant Homebase as homebase-mcp (Runtime)

  User->>Agent: Submit goal or code alteration task
  Agent->>TicketMaster: Check or create structured ticket (score & route)
  TicketMaster-->>Agent: Ticket confirmed & assigned
  Agent->>LockMaster: Verify project unlock & acquire lock (LOCK*.txt)
  LockMaster-->>Agent: Lock granted (exclusive edit boundary)
  alt Decision Needed & User Unreachable
    Agent->>BYUM: Query empirical decision-avatar
    BYUM-->>Agent: Grounded decision bounds & preferences
  end
  Agent->>ControlCenter: Discover MCP servers & resolve tool bundles
  ControlCenter-->>Agent: Bound MCP profile & available toolsets
  Agent->>Homebase: Persist task checkpoint & coordination state
  Agent->>Agent: Execute code modifications & run local test gates
  Agent->>TicketMaster: Mark ticket resolved & document evidence
  Agent->>LockMaster: Release lock & clean lockfile
  LockMaster-->>Agent: Project scope released
  Agent-->>User: Report completed execution & test results
```

---

## 6. Governance- & Laufzeit-Invarianten

Die Architektur von `agent-ops-stack` unterliegt zehn unveränderlichen Governance- und
Sicherheitsinvarianten, um Arbeitsbereiche vor Beschädigung und unkontrollierten Aktionen zu schützen:

| ID | Governance-Invariante | Betriebsvorschrift | Fehlerzustands-Garantie |
|:---:|:---|:---|:---|
| **01** | **100% Local-First & Zero Egress** | Sämtliche Koordination, Manifeste und Tools laufen strikt lokal und offline. | Keinerlei Telemetrie, Tracking oder externe API-Übertragungen. |
| **02** | **Unprivilegierter User-Mode** | Skripte, Installer und Agentenroutinen laufen ausschließlich mit Standardrechten. | Admin- oder Root-Rechte werden niemals angefordert oder benötigt. |
| **03** | **Fail-Closed Dateisperren-Integrität** | Agenten müssen vor Schreibaktionen `lock-master` `LOCK*.txt` prüfen und achten. | Bei aktiver Sperre stoppen mutierende Aktionen sofort fail-closed. |
| **04** | **Strukturiertes Ticket-Routing** | Offene Aufgaben und Fehler müssen über `ticket-master` erfasst werden. | Verhindert unkoordinierte und ungetrackte Codeänderungen. |
| **05** | **Empirischer Entscheidungs-Avatar** | Bei Abwesenheit des Nutzers konsultiert der Agent `build-your-users-mind`. | Verhindert spekulative Mutmaßungen und unerwünschte Abweichungen. |
| **06** | **Deterministischer Manifest-Bauplan** | Die Komposition wird ausnahmslos durch `agent-ops.manifest.json` definiert. | Keine impliziten Abhängigkeiten; Installer arbeitet rein deklarativ. |
| **07** | **Unveränderliche Release-Tag-Pins** | Manifest-Quellen referenzieren feste Release-Tags (`v1.11.3`, `v2026.09.03`). | Schließt Upstream-Drift und unvorhersehbare Versionsbrüche aus. |
| **08** | **Isolierte Installer-Grenzen** | `install.sh` klont Module ausschließlich in das git-ignorierte `./modules/`. | Keine unbemerkte Modifikation globaler Nutzer- oder Agenten-Configs. |
| **09** | **Multi-Host Slot-Isolation** | `sync-master` weist dedizierte Rechner-Slots für den Cloud-Abgleich zu. | Verhindert Split-Brain-Kollisionen und nebenläufige Überschreibungen. |
| **10** | **Plattformübergreifende Parität** | Workflows und Verifikationen laufen identisch auf Linux, Windows und macOS. | Einheitliches Koordinationsverhalten unabhängig vom Host-OS. |

---

## 7. Wie ein Agent diesen Stack nutzt

Beim Start einer Arbeitssitzung in einem neuen oder bestehenden Projekt folgt der Agent
diesem standardisierten Ablauf:

1. **Vor jeder Dateiänderung:** Prüfe über `lock-master` auf aktive `LOCK*.txt`-Dateien. Bei bestehender Sperre bleibt der Bereich strikt schreibgeschützt.
2. **Rechte & Richtlinien:** Falls das Projekt ein Rechteprofil definiert, prüfe geplante Operationen gegen die deklarierten Erlaubnisse.
3. **Entscheidungen bei Unsicherheit:** Ist der Nutzer abwesend und eine Entwurfsentscheidung erforderlich, frage `build-your-users-mind` nach empirischer Orientierung.
4. **Aufgaben erfassen & routen:** Dokumentiere Bugs, Feature-Wünsche oder delegierte Aufgaben über `ticket-master`, um Transparenz zu wahren.
5. **Skill-Wahl & MCP-Konfiguration:** Prüfe `skills` auf bewährte Arbeitsabläufe; wähle über `controlcenter-mcp` passende Werkzeugbündel; sichere Zustände via `homebase-mcp`.
6. **Geräteübergreifender Abgleich:** Beachte bei Multi-Device-Umgebungen die Slot-Regeln und täglichen Sync-Routinen von `sync-master` vor dem Pushen.

> [!TIP]
> **Multi-Agenten-Koordinations-Praxis**: Führe vor Codeänderungen in geteilten Repositories stets eine `lock-master`-Prüfung durch und nutze `ticket-master` zur strukturierten Weitergabe offener Aufgaben an andere Agenten oder den Nutzer.

---

## 8. Schnellstart & Installation

Klone `agent-ops-stack` und starte das Installationsskript, um die lokalen Module einzurichten:

```bash
# 1. Kompositions-Repository klonen
git clone https://github.com/ellmos-ai/agent-ops-stack.git
cd agent-ops-stack

# 2. Deklarativen Installer ausführen (klont Module nach ./modules/)
./install.sh

# 3. Optional: Zielverzeichnis explizit übergeben
./install.sh mein-zielverzeichnis
```

`install.sh` liest [`agent-ops.manifest.json`](agent-ops.manifest.json), klont die sieben
Repositories und gibt eine Übersicht aller gelieferten (`provides`) und benötigten
(`consumes`) Fähigkeiten aus. Es nimmt keine systemweiten Eingriffe vor.

---

## 9. Manifest-Schema-Spezifikation

[`agent-ops.manifest.json`](agent-ops.manifest.json) folgt der `ellmos-stack-manifest-v1`-Spezifikation:

```json
{
  "schema": "ellmos-stack-manifest-v1",
  "name": "agent-ops-stack",
  "description": "Local-first coordination layer for one or more CLI coding agents...",
  "modules": [
    {
      "name": "ticket-master",
      "source": { "type": "github", "repo": "dev-bricks/ticket-master", "ref": "v1.11.3" },
      "kind": "coordination",
      "boundaries": { "net": "none", "paths": ["./"], "tools": [] },
      "wiring": { "provides": ["ticket-routing"], "consumes": [] }
    }
  ]
}
```

- `schema`: Kennzeichnet die Spezifikationsversion (`ellmos-stack-manifest-v1`).
- `modules`: Liste der Moduldefinitionen mit Git-Quelle, Typ und Sicherheitsgrenzen.
- `boundaries`: Harte Restriktionen bezüglich Netzwerkzugriff, Pfadreichweite und Werkzeugen.
- `wiring`: Deklariert bereitgestellte Fähigkeiten (`provides`) und Abhängigkeiten (`consumes`).

---

## 10. Geschwister-Ökosystem & Integrationsmatrix

`agent-ops-stack` verbindet die Koordinations- und Entwicklungsbausteine der Ökosysteme
`ellmos-ai`, `dev-bricks` und `open-bricks`:

| Repository | Organisation | Rolle im Ökosystem & Integration |
|:---|:---|:---|
| [dev-bricks/ticket-master](https://github.com/dev-bricks/ticket-master) | `dev-bricks` | Position-0 Ticket-Erfassung, Scoring und aufgabenbezogenes Routing |
| [dev-bricks/lock-master](https://github.com/dev-bricks/lock-master) | `dev-bricks` | Datei-Sperrsystem (`LOCK*.txt`), Rechte-Evaluation und Kollisionsschutz |
| [dev-bricks/sync-master](https://github.com/dev-bricks/sync-master) | `dev-bricks` | Rechner-Slot-Synchronisation und gated tägliche Sync-Rituale |
| [ellmos-ai/build-your-users-mind](https://github.com/ellmos-ai/build-your-users-mind) | `ellmos-ai` | Empirischer Entscheidungs-Avatar auf Basis realer Interaktionshistorie |
| [ellmos-ai/skills](https://github.com/ellmos-ai/skills) | `ellmos-ai` | Portable Skill-Bibliothek im standardisierten `SKILL.md`-Format |
| [ellmos-ai/ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp) | `ellmos-ai` | MCP-Steuerebene, Server-Erkennung und Werkzeug-Fähigkeitsbündel |
| [ellmos-ai/ellmos-homebase-mcp](https://github.com/ellmos-ai/ellmos-homebase-mcp) | `ellmos-ai` | Geteilter Zustand, Gedächtnis-Fassade und Koordinationslaufzeit |
| [ellmos-ai/stacks](https://github.com/ellmos-ai/stacks) | `ellmos-ai` | Gemeinsame Stack-Manifest-Schemas, Prüfwerkzeuge und Stack-Katalog |
| [ellmos-ai/convergence-reconciler](https://github.com/ellmos-ai/convergence-reconciler) | `ellmos-ai` | Reziproke Code-Evaluation, Variantenverpflanzung und Pareto-Fitness |
| [ellmos-ai/ellmos-chat](https://github.com/ellmos-ai/ellmos-chat) | `ellmos-ai` | Local-First Chat- und Agenten-Orchestrierungsoberfläche |
| [dev-bricks/CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | `dev-bricks` | Hintergrundwartung, Zustandsmonitoring und SQLite-Optimierung |
| [open-bricks/open-bricks](https://github.com/open-bricks/open-bricks) | `open-bricks` | Dachorganisation für quelloffene Entwicklerwerkzeuge und Standards |

---

## 11. Suche & Begriffsklärung

- **Kanonische Identität**: `ellmos-ai/agent-ops-stack` ist ein deklarativer, lokaler Koordinations-Stack für Multi-Agenten-Workflows (Dateisperren, Ticket-Routing, Entscheidungsavatar, Skills, MCP-Steuerebene).
- **Begriffsklärung**: Nicht verwandt mit Cloud-Observability-SaaS-Produkten (wie AgentOps.ai), generischen AgentStack-Templates oder externen LLMOps-Servern.
- **Suchbegriffe**: `ellmos-ai agent-ops-stack`, `local CLI agent coordination stack`, `MCP control plane for coding agents`, `manifest-driven agent ops stack`, `lock-master ticket-master sync-master stack`.

---

## 12. Sicherheit & Verifikation

`agent-ops-stack` erzwingt standardisierte statische Analysen und automatisierte Vertragstests:

```bash
# 1. Automatisierte Metadaten-, Schema- und Vertragstests ausführen
pytest -v

# 2. Linter-Standards prüfen
ruff check .

# 3. Shell-Skript-Syntax prüfen
bash -n install.sh

# 4. Manifest-JSON validieren
python -c "import json; json.load(open('agent-ops.manifest.json', encoding='utf-8'))"
```

Ausführliche Richtlinien zur Meldung von Sicherheitsbedenken finden sich in [`SECURITY.md`](SECURITY.md).

---

## 13. Lizenz

Dieses Repository steht unter der permissiven **MIT-Lizenz**. Siehe [`LICENSE`](LICENSE). Jedes komponierte Modul unterliegt seiner eigenen Open-Source-Lizenz.

---

## 14. Haftung / Liability

Dieses Projekt ist eine **unentgeltliche Open-Source-Schenkung** im Sinne der §§ 516 ff. BGB. Die Haftung des Urhebers ist gemäß **§ 521 BGB** auf **Vorsatz und grobe Fahrlässigkeit** beschränkt. Die komponierten Module unterliegen jeweils ihrer eigenen Lizenz (siehe verlinkte Repositories).
