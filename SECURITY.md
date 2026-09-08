# Security Policy / Sicherheitsrichtlinie

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

### Supported Versions

The following versions of `agent-ops-stack` currently receive security, compatibility, and integrity updates:

| Version | Supported | Status |
| :--- | :---: | :--- |
| `1.3.x` | :white_check_mark: Yes | Active Release / Manifest Maintenance |
| `1.2.x` | :white_check_mark: Yes | Maintenance Mode |
| `< 1.2` | :x: No | Unsupported |

### Reporting a Vulnerability

We treat all security issues, integrity breaches, and coordination faults with utmost priority. If you identify a vulnerability or security risk in `agent-ops-stack` or its manifest composition, please follow these steps:

1. **Preferred Method (GitHub Security Advisory):**
   Submit a private advisory report directly via GitHub:
   [Report a Vulnerability](https://github.com/ellmos-ai/agent-ops-stack/security/advisories/new)

2. **Direct Contact via Email:**
   If GitHub Advisories is unavailable, please email our security team with full reproduction details:
   - Primary Security Contact: `security@ellmos.ai`
   - Umbrella Security: `security@open-bricks.org`
   - Lead Maintainer: `support@lukasgeiger.com` / `lukas@open-bricks.org`

### Response SLA & Disclosure Timeline

- **Initial Acknowledgment:** Within **48 hours** of receiving your report.
- **Triage & Status Assessment:** Within **5 business days** with an initial remediation assessment.
- **Coordinated Disclosure:** Security patches and manifest pin updates are validated locally and published via GitHub releases. We adhere to responsible, coordinated disclosure practices.

### Core Security & Governance Invariants

- **100% Local-First & Zero Egress:** The manifest, composition tools, and coordination workflows operate strictly local-first. Zero telemetry, tracking, or unexpected outbound network calls.
- **Non-Elevation User-Mode:** The entire stack operates strictly under standard, unprivileged user permissions. Elevation to administrative or root privileges is never required or requested.
- **Sandboxed Installer Boundaries:** `install.sh` clones public module repositories strictly into `./modules/` (gitignored). It reads no credentials, modifies no host agent configs silently, and writes only within the specified target directory.
- **Fail-Closed File Lock Integrity:** Multi-agent operations rely on `lock-master` conventions (`LOCK*.txt`). Active locks immediately halt any conflicting agent or automation write actions.
- **Structured Ticket Routing:** Workflows require `ticket-master` routing before code mutations, preventing uncoordinated modifications across workspaces.
- **Empirical Decision-Avatar Fallback:** When the human operator is away, `build-your-users-mind` provides empirical, grounded decision bounds instead of unbounded speculative agent actions.
- **Cross-Host Slot Isolation:** `sync-master` maintains distinct slots per machine, preventing split-brain states and concurrent conflict corruption during cloud file synchronization.

---

<a id="deutsch"></a>
## Deutsch

### Unterstützte Versionen

Die folgenden Versionen von `agent-ops-stack` erhalten aktiv Sicherheits- und Integritäts-Patches:

| Version | Unterstützt | Status |
| :--- | :---: | :--- |
| `1.3.x` | :white_check_mark: Ja | Aktive Version / Manifest-Wartung |
| `1.2.x` | :white_check_mark: Ja | Eingeschränkte Wartung |
| `< 1.2` | :x: Nein | Nicht mehr unterstützt |

### Meldung von Sicherheitslücken

Wir nehmen Sicherheits- und Koordinationsmeldungen sehr ernst. Sollten Sie eine Sicherheitslücke oder ein Integritätsrisiko entdecken, bitten wir um folgende Vorgehensweise:

1. **Bevorzugter Weg (GitHub Security Advisory):**
   Erstellen Sie einen vertraulichen Bericht über GitHub Security Advisories:
   [Sicherheitslücke privat melden](https://github.com/ellmos-ai/agent-ops-stack/security/advisories/new)

2. **Direkter E-Mail-Kontakt:**
   Falls GitHub Advisories nicht genutzt werden kann, wenden Sie sich bitte per E-Mail an unser Team:
   - Primärer Sicherheitskontakt: `security@ellmos.ai`
   - Dachorganisation: `security@open-bricks.org`
   - Lead Maintainer: `support@lukasgeiger.com` / `lukas@open-bricks.org`

### Reaktionsfristen (SLA) & Disclosure-Prozess

- **Erste Eingangsbestätigung:** Innerhalb von maximal **48 Stunden**.
- **Triage & Bewertungs-Update:** Innerhalb von **5 Werktagen** mit konkreter Analyse.
- **Koordinierte Behebung:** Sicherheits-Fixes und Manifest-Aktualisierungen werden lokal getestet und über koordinierte Releases publiziert.

### Zentrale Sicherheits- & Governance-Invarianten

- **100% Local-First & Zero-Egress:** Manifest, Installationshelfer und Koordinationsworkflows arbeiten strikt lokal. Keine Telemetrie, kein Tracking, keine unerwarteten Netzwerkverbindungen.
- **Unprivilegierter User-Mode (Non-Elevation):** Der Betrieb erfolgt ausnahmslos mit regulären Benutzerrechten ohne Admin- oder Root-Rechte.
- **Isolierte Installer-Grenzen:** `install.sh` klont öffentliche Modul-Repositories ausschließlich in das git-ignorierte `./modules/`-Verzeichnis. Es liest keine Zugangsdaten und manipuliert keine globalen Agenten-Configs.
- **Fail-Closed Dateisperren-Integrität:** Multi-Agenten-Betrieb nutzt `lock-master`-Sperren (`LOCK*.txt`). Aktive Sperren blockieren schreibende Zugriffe sofort und verbindlich.
- **Strukturiertes Ticket-Routing:** Aufgaben und Fehler werden über `ticket-master` strukturiert erfasst und geroutet, bevor Quellcode mutiert wird.
- **Empirischer Entscheidungs-Avatar:** Bei Abwesenheit des Nutzers liefert `build-your-users-mind` empirisch gestützte Entscheidungsgrenzen statt unkontrollierter KI-Mutmaßungen.
- **Multi-Host-Slot-Isolation:** `sync-master` garantiert getrennte Maschinen-Slots und verhindert Split-Brain-Sync-Konflikte bei Dateisynchronisation über Cloud-Ordner.
