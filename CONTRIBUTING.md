# Contributing to agent-ops-stack

[English](#english) | [Deutsch](#deutsch)

---

<a id="english"></a>
## English

Thanks for contributing. This repository maintains a JSON source manifest, a Bash fetch script, tests, CI, and documentation. Contributions should describe the files and behavior that are actually present. The manifest's `boundaries` and `wiring` values are descriptive; they are not enforced access controls or proof of module integration.

### Development

Work from a Git checkout. The installer fetches public repositories over the network, so review its target path and manifest refs before running it. It runs with the calling user's permissions and Git configuration.

Before submitting a change, run the checks relevant to it:

```sh
python -m pytest -o addopts='' -ra
python -m ruff check .
python -m compileall -q tests
bash -n install.sh
git diff --check
```

Also validate edited JSON or TOML with the corresponding parser. Do not start provider CLIs as part of routine documentation checks.

### Changes and reports

Keep changes focused and explain their effect in the pull request. Do not change the project version unless a maintainer explicitly requests a release change. Report security issues using [SECURITY.md](SECURITY.md), not a public issue.

This project has no runtime package installed by its Python wheel. The supported project workflow is the Git checkout and `install.sh`; its metadata and test extra support development tasks.

### License note

The repository's own license is in [`LICENSE`](LICENSE). Whether statutory rules such as sections 516 or 521 BGB apply depends on the legal relationship and applicable law. This file does not classify every use as a gift or make a blanket statement about liability.

---

<a id="deutsch"></a>
## Deutsch

Danke für deinen Beitrag. Dieses Repository pflegt ein JSON-Quellmanifest, ein Bash-Abrufskript, Tests, CI und Dokumentation. Beiträge sollen die tatsächlich vorhandenen Dateien und Funktionen beschreiben. `boundaries` und `wiring` im Manifest sind beschreibende Angaben; sie setzen keine Zugriffskontrollen durch und belegen keine Modul-Integration.

### Entwicklung

Arbeite in einem Git-Checkout. Der Installer ruft öffentliche Repositories über das Netzwerk ab. Prüfe deshalb vor dem Start den Zielpfad und die Manifest-Referenzen. Der Installer läuft mit den Rechten und der Git-Konfiguration des aufrufenden Benutzers.

Führe vor einem Beitrag die dafür passenden Prüfungen aus:

```sh
python -m pytest -o addopts='' -ra
python -m ruff check .
python -m compileall -q tests
bash -n install.sh
git diff --check
```

Validiere bearbeitetes JSON oder TOML zusätzlich mit dem passenden Parser. Starte Provider-CLIs nicht für übliche Dokumentationsprüfungen.

### Änderungen und Meldungen

Halte Änderungen fokussiert und erläutere ihre Wirkung im Pull Request. Ändere die Projektversion nur auf ausdrückliche Bitte eines Maintainers im Rahmen einer Releaseänderung. Melde Sicherheitsprobleme gemäß [SECURITY.md](SECURITY.md), nicht als öffentliches Issue.

Das Python-Wheel dieses Projekts installiert keine Laufzeit. Der vorgesehene Projektablauf verwendet den Git-Checkout und `install.sh`; Metadaten und Test-Extra dienen Entwicklungsaufgaben.

### Lizenzhinweis

Die eigene Projektlizenz steht in [`LICENSE`](LICENSE). Ob gesetzliche Vorschriften wie §§ 516 oder 521 BGB gelten, hängt von der Rechtsbeziehung und dem anwendbaren Recht ab. Diese Datei ordnet nicht jede Nutzung als Schenkung ein und trifft keine pauschale Aussage zur Haftung.
