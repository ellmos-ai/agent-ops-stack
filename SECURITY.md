# Security Policy / Sicherheitsrichtlinie

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

### Scope and behavior

This repository contains a manifest, documentation, tests, and `install.sh`. The installer parses the manifest and invokes `git clone` for its listed public GitHub sources. It uses Bash and either `jq` or Python 3. Git and the parser inherit the invoking environment and permissions. The target directory is writable by the current user.

The installer does not enforce manifest `boundaries`, apply an operating-system sandbox, drop privileges, filter network access, or coordinate concurrent writers. It does not start provider CLIs or configure fetched modules. Each fetched repository has its own code, data flows, security policy, setup, and release process; review those separately.

### Reporting a vulnerability

Please report security issues privately through [GitHub Security Advisories](https://github.com/ellmos-ai/agent-ops-stack/security/advisories/new). If that route is unavailable, contact:

- `security@ellmos.ai`
- `security@open-bricks.org`
- `support@lukasgeiger.com`

Include the affected repository commit or manifest ref, the relevant files, and a reproducible description. Do not include live credentials or unrelated personal data. Avoid public disclosure until a maintainer has had a chance to assess the report.

### Maintainer response policy

The maintainer policy is to acknowledge a report within **48 hours** and provide an initial triage assessment within **five business days**. These are response targets. They do not promise a remediation date, a security certification, or a particular outcome.

### License and legal scope

This repository is provided under the MIT license. Whether statutory rules such as sections 516 or 521 BGB apply depends on the legal relationship and applicable law; this policy does not classify every use as a gift or state a blanket liability rule.

---

<a id="deutsch"></a>
## Deutsch

### Umfang und Verhalten

Dieses Repository enthält ein Manifest, Dokumentation, Tests und `install.sh`. Der Installer liest das Manifest und ruft `git clone` für die aufgeführten öffentlichen GitHub-Quellen auf. Er verwendet Bash und entweder `jq` oder Python 3. Git und der Parser übernehmen Umgebung und Rechte des aufrufenden Prozesses. Das aktuelle Benutzerkonto kann in das Zielverzeichnis schreiben.

Der Installer setzt die `boundaries` des Manifests nicht durch, richtet keine Betriebssystem-Sandbox ein, senkt keine Prozessrechte ab, filtert keinen Netzwerkzugriff und koordiniert keine gleichzeitigen Schreiber. Er startet keine Provider-CLIs und konfiguriert keine abgerufenen Module. Jedes abgerufene Repository hat eigenen Code, eigene Datenflüsse, Sicherheitsrichtlinien, Einrichtungsschritte und Releases; prüfe diese getrennt.

### Sicherheitslücke melden

Melde Sicherheitsprobleme vertraulich über [GitHub Security Advisories](https://github.com/ellmos-ai/agent-ops-stack/security/advisories/new). Falls dieser Weg nicht verfügbar ist, wende dich an:

- `security@ellmos.ai`
- `security@open-bricks.org`
- `support@lukasgeiger.com`

Nenne den betroffenen Repository-Commit oder die Manifest-Referenz, die relevanten Dateien und eine reproduzierbare Beschreibung. Füge keine aktiven Zugangsdaten oder sachfremden personenbezogenen Daten bei. Veröffentliche Details nach Möglichkeit erst, wenn Maintainer den Bericht prüfen konnten.

### Reaktionsrichtlinie der Maintainer

Die Maintainer-Richtlinie sieht eine Eingangsbestätigung innerhalb von **48 Stunden** und eine erste Triage-Einschätzung innerhalb von **fünf Werktagen** vor. Das sind Reaktionsziele. Sie versprechen weder einen Behebungstermin noch eine Sicherheitszertifizierung oder ein bestimmtes Ergebnis.

### Lizenz und rechtlicher Umfang

Dieses Repository steht unter der MIT-Lizenz. Ob gesetzliche Vorschriften wie §§ 516 oder 521 BGB gelten, hängt von der Rechtsbeziehung und dem anwendbaren Recht ab; diese Richtlinie ordnet nicht jede Nutzung als Schenkung ein und formuliert keine pauschale Haftungsregel.
