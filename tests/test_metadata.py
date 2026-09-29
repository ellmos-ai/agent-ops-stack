"""Automated metadata, discoverability, documentation, and parity contract tests."""

import json
import re
import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_manifest_schema_and_integrity():
    manifest_file = REPO_ROOT / "agent-ops.manifest.json"
    assert manifest_file.exists(), "agent-ops.manifest.json must exist"

    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("schema") == "ellmos-stack-manifest-v1"
    assert data.get("name") == "agent-ops-stack"
    assert "description" in data

    modules = data.get("modules", [])
    assert len(modules) == 7, f"Manifest must contain exactly 7 modules, found {len(modules)}"

    expected_modules = {
        "ticket-master": "coordination",
        "lock-master": "coordination",
        "sync-master": "sync",
        "build-your-users-mind": "decision",
        "skills": "skills",
        "controlcenter-mcp": "mcp",
        "homebase-mcp": "mcp",
    }

    found = {}
    for mod in modules:
        name = mod.get("name")
        found[name] = mod.get("kind")
        assert "source" in mod, f"Module {name} missing source"
        assert "boundaries" in mod, f"Module {name} missing boundaries"
        assert "wiring" in mod, f"Module {name} missing wiring"
        assert "provides" in mod["wiring"], f"Module {name} missing wiring.provides"
        assert "consumes" in mod["wiring"], f"Module {name} missing wiring.consumes"

    assert found == expected_modules, f"Mismatch in module kinds: {found} vs {expected_modules}"


def test_installer_script_syntax_and_integrity():
    installer = REPO_ROOT / "install.sh"
    assert installer.exists(), "install.sh must exist"

    text = installer.read_text(encoding="utf-8")
    assert "agent-ops.manifest.json" in text
    assert "json_names()" in text
    assert "json_repo()" in text
    assert "git clone" in text
    assert "Wiring summary" in text


def test_readme_and_readme_de_exist_and_bilingual_parity():
    readme_en = REPO_ROOT / "README.md"
    readme_de = REPO_ROOT / "README_de.md"
    assert readme_en.exists(), "README.md must exist"
    assert readme_de.exists(), "README_de.md must exist"

    text_en = readme_en.read_text(encoding="utf-8")
    text_de = readme_de.read_text(encoding="utf-8")

    assert len(text_en) > 2000, "README.md must be comprehensive"
    assert len(text_de) > 2000, "README_de.md must be comprehensive"

    # Verify language switchers
    assert "[Deutsche Version](README_de.md)" in text_en
    assert "[English version](README.md)" in text_de


def test_readme_badges_present():
    expected_badges = [
        "img.shields.io/badge/Manifest-ellmos--stack--manifest--v1-blue.svg",
        "img.shields.io/badge/version-1.3.4-blue.svg",
        "img.shields.io/badge/CI-GitHub%20Actions-brightgreen.svg",
        "img.shields.io/badge/tests-49%20passed%20%7C%20100%25-brightgreen.svg",
        "img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg",
        "img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg",
        "img.shields.io/badge/architecture-100%25%20Local--First%20%7C%20Zero--Egress-success.svg",
        "img.shields.io/badge/security-Non--Elevation%20%7C%20Sandboxed-informational.svg",
        "img.shields.io/badge/Security%20SLA-48h%20%7C%205d%20triage-informational.svg",
        "img.shields.io/badge/Third--Party-Audited-blue.svg",
        "img.shields.io/badge/Marketing%20Log-Active-informational.svg",
        "img.shields.io/badge/code%20style-ruff-000000.svg",
        "img.shields.io/badge/License-MIT-green.svg",
        "img.shields.io/badge/Attribution-NOTICE-blue.svg",
        "img.shields.io/badge/Ecosystem-ellmos--ai-purple.svg",
        "img.shields.io/badge/Umbrella-open--bricks-blue.svg",
        "img.shields.io/badge/LLM--Ready-llms.txt-success.svg",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        for badge in expected_badges:
            assert badge in text, f"Missing badge {badge} in {filename}"


def test_quick_navigation_18_points_and_reciprocal_anchor_parity():
    readme_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    # Match numbered markdown list items 1. through 18.
    en_nav_items = re.findall(r"^\d+\.\s+\[.+?\]\(#.+?\)", readme_en, flags=re.MULTILINE)
    de_nav_items = re.findall(r"^\d+\.\s+\[.+?\]\(#.+?\)", readme_de, flags=re.MULTILINE)

    assert len(en_nav_items) == 18, (
        f"README.md must have 18 quick nav items, found {len(en_nav_items)}"
    )
    assert len(de_nav_items) == 18, (
        f"README_de.md must have 18 quick nav items, found {len(de_nav_items)}"
    )

    # Check that major target sections 1 through 18 exist in both
    for section_num in range(1, 19):
        assert f"## {section_num}. " in readme_en, f"Missing section ## {section_num}. in README.md"
        assert f"## {section_num}. " in readme_de, (
            f"Missing section ## {section_num}. in README_de.md"
        )

    # Check reciprocal anchor parity between English and German READMEs
    reciprocal_anchor_pairs = [
        ("1-overview--architecture", "1-ueberblick--architektur"),
        ("2-what-is-agent-ops", "2-was-ist-agent-ops"),
        ("3-target-personas--discoverability", "3-zielgruppen--auffindbarkeit"),
        ("4-comparative-matrix-vs-alternatives", "4-vergleichsmatrix-gegenueber-alternativen"),
        ("5-composed-modules-the-7-pillars", "5-komponierte-module-die-7-saeulen"),
        ("6-system-architecture-flowchart", "6-systemarchitektur-flussdiagramm"),
        ("7-multi-agent-operational-lifecycle-sequence", "7-multi-agenten-lebenszyklus-sequenz"),
        ("8-governance--runtime-invariants", "8-governance--laufzeit-invarianten"),
        ("9-how-an-agent-uses-this-stack", "9-wie-ein-agent-diesen-stack-nutzt"),
        ("10-quickstart--installation", "10-schnellstart--installation"),
        ("11-manifest-schema-specification", "11-manifest-schema-spezifikation"),
        (
            "12-sibling-ecosystem--cross-integration-matrix",
            "12-geschwister-oekosystem--integrationsmatrix",
        ),
        ("13-search-seo--disambiguation", "13-suche-seo--begriffsklaerung"),
        ("14-security-model--threat-mitigation", "14-sicherheitsmodell--bedrohungsabwehr"),
        ("15-third-party-licenses--transparency", "15-drittanbieter-lizenzen--transparenz"),
        ("16-verification--automated-test-suite", "16-verifikation--automatisierte-testsuite"),
        ("17-security-policy--slas", "17-sicherheitsrichtlinie--slas"),
        ("18-license--liability--haftung", "18-lizenz--haftung--liability"),
    ]
    for en_anchor, de_anchor in reciprocal_anchor_pairs:
        # Check that both anchors exist in both README files
        assert f'id="{en_anchor}"' in readme_en, f"Missing en anchor {en_anchor} in README.md"
        assert f'id="{de_anchor}"' in readme_en, f"Missing de anchor {de_anchor} in README.md"
        assert f'id="{en_anchor}"' in readme_de, f"Missing en anchor {en_anchor} in README_de.md"
        assert f'id="{de_anchor}"' in readme_de, f"Missing de anchor {de_anchor} in README_de.md"


def test_mermaid_diagrams_syntax_and_subgraphs():
    expected_subgraphs = ["COORDINATION", "MCP", "DECISION", "AGENTS", "SYNC"]
    expected_participants = [
        "User",
        "Agent",
        "LockMaster",
        "TicketMaster",
        "BYUM",
        "ControlCenter",
        "Homebase",
    ]

    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "```mermaid\nflowchart TD" in text, f"{filename} must contain a flowchart TD"
        assert "```mermaid\nsequenceDiagram" in text, f"{filename} must contain a sequenceDiagram"

        for subgraph in expected_subgraphs:
            assert f"subgraph {subgraph}" in text, (
                f"{filename} missing flowchart subgraph {subgraph}"
            )

        for participant in expected_participants:
            assert participant in text, f"{filename} missing sequence participant {participant}"


def test_governance_invariants_table_ten_points():
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        # Ensure rows 01 through 10 are in the table
        for inv_num in [f"{i:02d}" for i in range(1, 11)]:
            assert f"**{inv_num}**" in text, f"Missing invariant {inv_num} in {filename}"


def test_sibling_ecosystem_matrix_twelve_repos():
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        expected_repos = [
            "ticket-master",
            "lock-master",
            "sync-master",
            "build-your-users-mind",
            "skills",
            "ellmos-controlcenter-mcp",
            "ellmos-homebase-mcp",
            "stacks",
            "convergence-reconciler",
            "ellmos-chat",
            "CareCenter-for-Codex",
            "open-bricks",
        ]
        for repo in expected_repos:
            assert repo in text, f"Missing sibling repository {repo} in {filename}"


def test_security_policy_exists_and_bilingual_parity():
    sec_file = REPO_ROOT / "SECURITY.md"
    assert sec_file.exists(), "SECURITY.md must exist"
    text = sec_file.read_text(encoding="utf-8")

    assert "## English" in text
    assert "## Deutsch" in text
    assert "1.3.x" in text
    assert "security@ellmos.ai" in text
    assert "security@open-bricks.org" in text
    assert "support@lukasgeiger.com" in text
    assert "48 hours" in text or "48 Stunden" in text
    assert "https://github.com/ellmos-ai/agent-ops-stack/security/advisories/new" in text


def test_pyproject_pep621_metadata_and_urls():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    project = data.get("project", {})
    assert project.get("name") == "agent-ops-stack"
    assert project.get("version") == "1.3.4"
    assert "classifiers" in project
    assert any("Python :: 3.10" in c for c in project["classifiers"])
    assert any("Python :: 3.11" in c for c in project["classifiers"])
    assert any("Python :: 3.12" in c for c in project["classifiers"])
    assert any("Python :: 3.13" in c for c in project["classifiers"])

    urls = project.get("urls", {})
    assert "Homepage" in urls
    assert "Documentation" in urls
    assert "Repository" in urls
    assert "Issues" in urls
    assert "Bug Tracker" in urls
    assert "Changelog" in urls
    assert "Security" in urls
    assert "Third-Party Licenses" in urls
    assert "Notice" in urls
    assert "Marketing Log" in urls
    assert "LLM Ready" in urls
    assert "Parent Organization" in urls
    assert "Umbrella Ecosystem" in urls
    assert urls["Notice"].endswith("/NOTICE")
    assert urls["Parent Organization"] == "https://github.com/ellmos-ai"
    assert urls["Umbrella Ecosystem"] == "https://github.com/open-bricks"

    assert "tool" in data and "ruff" in data["tool"]
    select = data["tool"]["ruff"].get("lint", {}).get("select", [])
    for rule in ["E", "F", "W", "I", "UP", "B", "SIM", "C4", "RUF"]:
        assert rule in select, f"Missing ruff rule {rule} in pyproject.toml"


def test_version_parity_across_artifacts():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = pyproject["project"]["version"]
    assert version == "1.3.4"

    changelog_text = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert f"## {version}" in changelog_text

    llms_text = (REPO_ROOT / "llms.txt").read_text(encoding="utf-8")
    assert f"Version: {version}" in llms_text

    sec_text = (REPO_ROOT / "SECURITY.md").read_text(encoding="utf-8")
    assert f"{version.rsplit('.', 1)[0]}.x" in sec_text


def test_gitignore_hygiene_patterns():
    gitignore_file = REPO_ROOT / ".gitignore"
    assert gitignore_file.exists(), ".gitignore must exist"
    text = gitignore_file.read_text(encoding="utf-8")

    # Multi-host sync conflict patterns
    assert "*-conflict-*" in text, "Missing *-conflict-* pattern in .gitignore"
    assert "*.sync-conflict-*" in text, "Missing *.sync-conflict-* pattern in .gitignore"
    assert "*.sync-temp-*" in text, "Missing *.sync-temp-* pattern in .gitignore"
    assert "*.conflict" in text, "Missing *.conflict pattern in .gitignore"
    assert "*-CONFLIT-*" in text, "Missing *-CONFLIT-* pattern in .gitignore"
    assert "* (kopie)*" in text, "Missing * (kopie)* pattern in .gitignore"
    assert "* (copy)*" in text, "Missing * (copy)* pattern in .gitignore"
    assert "*-WORKSTATION*" in text, "Missing *-WORKSTATION* pattern in .gitignore"
    assert "*-WORKSTATION-LG*" in text, "Missing *-WORKSTATION-LG* pattern in .gitignore"
    assert "*-ASUS-GEI*" in text, "Missing *-ASUS-GEI* pattern in .gitignore"

    # Multi-agent lock patterns
    assert "\nLOCK\n" in f"\n{text}\n", "Missing standalone LOCK in .gitignore"
    assert "LOCK.*" in text, "Missing LOCK.* pattern in .gitignore"
    assert "*.lock" in text, "Missing *.lock pattern in .gitignore"
    assert "LOCK*.txt" in text, "Missing LOCK*.txt pattern in .gitignore"
    assert "LOCK.permissions.json" in text, "Missing LOCK.permissions.json in .gitignore"
    assert "uv.lock" in text, "Missing uv.lock in .gitignore"

    # Test & packaging caches
    assert ".pytest_cache/" in text, "Missing .pytest_cache/ in .gitignore"
    assert ".ruff_cache/" in text, "Missing .ruff_cache/ in .gitignore"
    assert ".coverage" in text, "Missing .coverage in .gitignore"
    assert ".coverage.*" in text, "Missing .coverage.* in .gitignore"
    assert "wheelhouse/" in text, "Missing wheelhouse/ in .gitignore"
    assert ".wheel-smoke/" in text, "Missing .wheel-smoke/ in .gitignore"


def test_pytest_configuration_and_flags():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    pytest_opts = data.get("tool", {}).get("pytest", {}).get("ini_options", {})
    assert pytest_opts.get("testpaths") == ["tests"]
    assert "-ra" in pytest_opts.get("addopts", "")
    assert "-v" in pytest_opts.get("addopts", "")


def test_ci_workflow_hardening():
    ci_file = REPO_ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_file.exists(), ".github/workflows/ci.yml must exist"
    text = ci_file.read_text(encoding="utf-8")

    assert "cancel-in-progress: true" in text, "CI must enable cancel-in-progress"
    assert "timeout-minutes: 15" in text, "CI must define 15-minute runaway timeout guardrail"
    assert "permissions:" in text, "CI must define permissions block"
    assert "contents: read" in text, "CI must restrict permissions to contents: read"
    assert "python -m compileall -q tests" in text, "CI must contain bytecode compilation gate"
    assert "pytest -ra -v" in text, "CI must run standardized pytest -ra -v"
    for os_name in ["ubuntu-latest", "windows-latest", "macos-latest"]:
        assert os_name in text, f"CI matrix missing {os_name}"


def test_changelog_release_entry():
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## 1.3.3 (2026-09-12)" in changelog, "CHANGELOG.md missing 1.3.3 release entry"
    assert "Pfad A" in changelog, "CHANGELOG.md 1.3.3 entry must reference Pfad A"


def test_third_party_licenses_inventory():
    lic_file = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
    assert lic_file.exists(), "THIRD_PARTY_LICENSES.md must exist"
    text = lic_file.read_text(encoding="utf-8")

    assert "100% Local-First & Zero Egress" in text
    assert "Unprivileged User-Mode" in text
    assert "Python Standard Library" in text
    assert "PSFL-2.0" in text
    assert "pytest" in text
    assert "ruff" in text
    assert "setuptools" in text
    assert "ticket-master" in text
    assert "lock-master" in text
    assert "sync-master" in text
    assert "build-your-users-mind" in text
    assert "skills" in text
    assert "ellmos-controlcenter-mcp" in text
    assert "ellmos-homebase-mcp" in text
    assert "MIT License" in text


def test_marketing_log_structure_and_personas():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")

    assert "Target Version: 1.3.2" in text
    assert "Autonomous AI Agent Engineers & Platform Architects" in text
    assert "Multi-Device & Cross-Machine Developers" in text
    assert "Enterprise Tooling, Safety & Governance Compliance Officers" in text
    assert "Open-Source AI Tool Builders & MCP Ecosystem Integrators" in text
    assert "INV-LOCAL-01" in text
    assert "INV-SLA-10" in text


def test_llms_txt_structure_and_parity():
    llms_file = REPO_ROOT / "llms.txt"
    assert llms_file.exists(), "llms.txt must exist"
    text = llms_file.read_text(encoding="utf-8")

    assert (
        "Last-checked: 2026-09-29" in text
        or "Last-checked: 2026-09-26" in text
        or "Last-checked: 2026-09-21" in text
    )
    assert "Version: 1.3.4" in text
    assert (
        "49 passed contract tests" in text
        or "42 passed contract tests" in text
        or "37 passed contract tests" in text
    )
    assert "THIRD_PARTY_LICENSES.md" in text
    assert "THIRD_PARTY_LICENSES.txt" in text
    assert "MARKETING-LOG.txt" in text
    assert "NOTICE" in text


def test_banner_assets_and_media_integrity():
    assets_dir = REPO_ROOT / "assets"
    assert assets_dir.exists() and assets_dir.is_dir(), "assets/ directory must exist"

    banner_png = assets_dir / "banner.png"
    banner_svg = assets_dir / "banner.svg"
    assert banner_png.exists() and banner_png.stat().st_size > 0, "assets/banner.png must exist"
    assert banner_svg.exists() and banner_svg.stat().st_size > 0, "assets/banner.svg must exist"

    readme_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")
    assert "assets/banner.png" in readme_en
    assert "assets/banner.svg" in readme_de


def test_ci_timeout_minutes_guardrail():
    ci_file = REPO_ROOT / ".github" / "workflows" / "ci.yml"
    assert ci_file.exists(), ".github/workflows/ci.yml must exist"
    text = ci_file.read_text(encoding="utf-8")
    assert "timeout-minutes: 15" in text, "CI must define 15-minute runaway timeout guardrail"
    assert "permissions:\n  contents: read" in text, (
        "CI must restrict permissions to contents: read"
    )


def test_pep621_llm_ready_and_bug_tracker_urls():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))
    urls = data.get("project", {}).get("urls", {})
    assert "LLM Ready" in urls, "pyproject.toml must define 'LLM Ready' URL"
    assert urls["LLM Ready"].endswith("/llms.txt"), "'LLM Ready' URL must point to llms.txt"
    assert "Bug Tracker" in urls, "pyproject.toml must define 'Bug Tracker' URL"
    assert urls["Bug Tracker"].endswith("/issues"), "'Bug Tracker' URL must point to issues"


def test_ruff_lint_configuration_and_rulesets():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))
    select = data.get("tool", {}).get("ruff", {}).get("lint", {}).get("select", [])
    expected_rules = ["E", "F", "W", "I", "UP", "B", "SIM", "C4", "RUF"]
    for r in expected_rules:
        assert r in select, f"Ruff config missing rule {r}"


def test_extended_gitignore_multi_host_and_lock_defense():
    gitignore_file = REPO_ROOT / ".gitignore"
    assert gitignore_file.exists(), ".gitignore must exist"
    text = gitignore_file.read_text(encoding="utf-8")
    expected_patterns = [
        "* (kopie)*",
        "* (copy)*",
        "*-WORKSTATION*",
        "*-WORKSTATION-LG*",
        "*-ASUS-GEI*",
        "*.orig",
        "uv.lock",
        "!package-lock.json",
        ".coverage.*",
        ".tox/",
        ".turbo/",
        ".nyc_output/",
        ".mypy_cache/",
    ]
    for pattern in expected_patterns:
        assert pattern in text, f"Missing pattern {pattern} in .gitignore"


def test_changelog_recent_pfad_a_entry():
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## 1.3.3 (2026-09-12)" in changelog, "Missing 1.3.3 entry in CHANGELOG.md"
    assert "Pfad A (Repository Hygiene, CI Timeout Hardening & Lock Defense)" in changelog


def test_marketing_log_recent_hygiene_entry():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")
    assert "8. TECHNICAL HYGIENE & AUTOMATION READINESS (v1.3.3 -- 2026-09-12) [Pfad A]" in text
    assert "timeout-minutes: 15" in text


def test_target_personas_four_profiles():
    personas = [
        "[PERSONA-01]",
        "[PERSONA-02]",
        "[PERSONA-03]",
        "[PERSONA-04]",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        for p in personas:
            assert p in text, f"Missing persona {p} in {filename}"


def test_comparative_matrix_ten_dimensions_and_invariants():
    invariants = [
        "INV-LOCAL-01",
        "INV-USER-02",
        "INV-LOCK-03",
        "INV-ROUT-04",
        "INV-AVAT-05",
        "INV-MANI-06",
        "INV-PIN-07",
        "INV-SAND-08",
        "INV-SYNC-09",
        "INV-SLA-10",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        for inv in invariants:
            assert inv in text, f"Missing invariant {inv} in {filename} comparative matrix"


def test_security_model_and_sla_sections():
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "## 14. " in text, f"Missing section 14 in {filename}"
        assert "## 17. " in text, f"Missing section 17 in {filename}"
        assert "48h" in text or "48 hours" in text or "48 Stunden" in text, (
            f"Missing 48h SLA in {filename}"
        )
        assert "5d" in text or "5 business days" in text or "5 Werktagen" in text, (
            f"Missing 5-day triage SLA in {filename}"
        )


def test_changelog_recent_pfad_b_entry():
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## 1.3.4 (2026-09-16)" in changelog, "Missing 1.3.4 entry in CHANGELOG.md"
    assert "Pfad B" in changelog, "CHANGELOG.md 1.3.4 entry must reference Pfad B"


def test_marketing_log_recent_pfad_b_entry():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")
    assert (
        "9. DISCOVERABILITY, 18-POINT NAVIGATION & COMPARATIVE MATRIX AUDIT "
        "(v1.3.4 -- 2026-09-16) [Pfad B]"
    ) in text
    assert "Target Personas & Discoverability" in text


def test_third_party_licenses_audit_2026_09_16():
    lic_file = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
    assert lic_file.exists(), "THIRD_PARTY_LICENSES.md must exist"
    text = lic_file.read_text(encoding="utf-8")
    assert "2026-09-16" in text, "Missing 2026-09-16 audit date in THIRD_PARTY_LICENSES.md"
    assert "2026-09-21" in text, "Missing 2026-09-21 audit date in THIRD_PARTY_LICENSES.md"
    assert "NOTICE" in text, "Missing NOTICE in THIRD_PARTY_LICENSES.md"
    assert "1.3.4" in text, "Missing 1.3.4 version in THIRD_PARTY_LICENSES.md"
    expected_invariants = [
        "INV-LOCAL-01",
        "INV-USER-02",
        "INV-LOCK-03",
        "INV-ROUT-04",
        "INV-AVAT-05",
        "INV-MANI-06",
        "INV-PIN-07",
        "INV-SAND-08",
        "INV-SYNC-09",
        "INV-SLA-10",
    ]
    for inv in expected_invariants:
        assert inv in text, f"Missing invariant {inv} in THIRD_PARTY_LICENSES.md"


def test_notice_attribution_file_exists_and_content():
    notice_file = REPO_ROOT / "NOTICE"
    assert notice_file.exists(), "NOTICE file must exist in repo root"
    text = notice_file.read_text(encoding="utf-8")
    assert "agent-ops-stack" in text
    assert "Lukas Geiger" in text
    assert "ellmos-ai" in text
    assert "open-bricks" in text
    assert "THIRD_PARTY_LICENSES.md" in text


def test_stale_and_welcome_workflows_exist_and_hardened():
    stale_file = REPO_ROOT / ".github" / "workflows" / "stale.yml"
    welcome_file = REPO_ROOT / ".github" / "workflows" / "welcome.yml"
    assert stale_file.exists(), ".github/workflows/stale.yml must exist"
    assert welcome_file.exists(), ".github/workflows/welcome.yml must exist"

    stale_text = stale_file.read_text(encoding="utf-8")
    assert "actions/stale@v9" in stale_text
    assert "timeout-minutes: 10" in stale_text
    assert "cancel-in-progress: true" in stale_text
    assert "issues: write" in stale_text
    assert "pull-requests: write" in stale_text

    welcome_text = welcome_file.read_text(encoding="utf-8")
    assert "actions/first-interaction@v3" in welcome_text
    assert "timeout-minutes: 5" in welcome_text
    assert "cancel-in-progress: true" in welcome_text
    assert "issues: write" in welcome_text
    assert "pull-requests: write" in welcome_text


def test_pyproject_license_files_and_pytest_norecursedirs():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    license_files = data.get("project", {}).get("license-files", [])
    assert "LICENSE" in license_files
    assert "NOTICE" in license_files
    assert "THIRD_PARTY_LICENSES.md" in license_files
    assert "THIRD_PARTY_LICENSES.txt" in license_files

    urls = data.get("project", {}).get("urls", {})
    assert "Notice" in urls
    assert urls["Notice"].endswith("/NOTICE")
    assert "Third-Party Licenses (Text)" in urls
    assert urls["Third-Party Licenses (Text)"].endswith("/THIRD_PARTY_LICENSES.txt")

    pytest_cfg = data.get("tool", {}).get("pytest", {}).get("ini_options", {})
    assert pytest_cfg.get("minversion") == "7.0"
    norecursedirs = pytest_cfg.get("norecursedirs", [])
    for d in [".git", ".pytest_cache", "__pycache__", "build", "dist", ".venv"]:
        assert d in norecursedirs


def test_gitignore_multihost_extended_patterns():
    gitignore_file = REPO_ROOT / ".gitignore"
    assert gitignore_file.exists(), ".gitignore must exist"
    text = gitignore_file.read_text(encoding="utf-8")

    extended_patterns = [
        "*conflicted copy*",
        "* (Kopie)*",
        "* (Copy)*",
        "*-ASUS*",
        "*-LAPTOP*",
        "*-Mac Studio*",
        "*-MacBook*",
        "*.rej",
        "LOCK.user.*",
        "LOCK.until.*",
        "LOCK.condition.*",
        ".automation-lock",
        ".hypothesis/",
    ]
    for pat in extended_patterns:
        assert pat in text, f"Missing extended pattern {pat} in .gitignore"


def test_changelog_unreleased_pfad_a_entry():
    changelog_file = REPO_ROOT / "CHANGELOG.md"
    assert changelog_file.exists(), "CHANGELOG.md must exist"
    text = changelog_file.read_text(encoding="utf-8")

    assert "## [Unreleased]" in text, "CHANGELOG.md must contain ## [Unreleased] section"
    assert "Pfad A" in text, "CHANGELOG.md must reference Pfad A"
    assert "2026-09-21" in text, "CHANGELOG.md must reference 2026-09-21"
    assert "NOTICE" in text, "CHANGELOG.md must reference NOTICE"


def test_marketing_log_pfad_a_section_10():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")

    assert (
        "10. TECHNICAL HYGIENE, CI LIFECYCLE & MULTI-HOST PROTECTION AUDIT "
        "(v1.3.4 -- 2026-09-21) [Pfad A]"
    ) in text
    assert "stale.yml" in text
    assert "welcome.yml" in text
    assert "timeout-minutes: 10" in text
    assert "NOTICE" in text


def test_multi_agent_concurrency_state_diagram():
    expected_states_en = [
        "TaskReceived",
        "TicketRouting",
        "LockCheck",
        "LockAcquired",
        "LockDenied",
        "AmbiguityEvaluation",
        "AvatarConsultation",
        "ToolDiscovery",
        "ContextLoading",
        "TaskExecution",
        "VerificationGates",
        "TicketResolution",
        "LockRelease",
        "SyncAlignment",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "```mermaid\nstateDiagram-v2" in text, f"{filename} missing stateDiagram-v2"
        for state in expected_states_en:
            assert state in text, f"Missing state {state} in {filename}"


def test_component_interoperability_wire_protocols():
    expected_protocols = [
        "lock-master",
        "ticket-master",
        "build-your-users-mind",
        "controlcenter-mcp",
        "homebase-mcp",
        "sync-master",
        "skills",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "Component Interoperability" in text or "Komponenten-Interoperabilität" in text
        for proto in expected_protocols:
            assert proto in text, f"Missing protocol entry {proto} in {filename}"


def test_pyproject_pep621_twenty_keywords_saturation():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    keywords = data.get("project", {}).get("keywords", [])
    assert len(keywords) == 20, f"Expected 20 keywords in pyproject.toml, found {len(keywords)}"
    for kw in [
        "agent-ops",
        "ellmos-ai",
        "local-first",
        "manifest",
        "mcp",
        "multi-agent",
        "agent-coordination",
        "claude-code",
        "cli-agents",
        "codex-cli",
        "mcp-control-plane",
        "agent-orchestration",
        "ai-agents",
        "developer-tools",
        "file-locking",
        "file-sync",
        "antigravity-cli",
        "offline-first",
        "open-bricks",
        "zero-egress",
    ]:
        assert kw in keywords, f"Missing keyword {kw} in pyproject.toml"


def test_third_party_licenses_audit_2026_09_26():
    lic_file = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
    assert lic_file.exists(), "THIRD_PARTY_LICENSES.md must exist"
    text = lic_file.read_text(encoding="utf-8")
    assert "2026-09-26" in text, "Missing 2026-09-26 audit date in THIRD_PARTY_LICENSES.md"
    assert "2026-09-21" in text, "Missing 2026-09-21 audit date in THIRD_PARTY_LICENSES.md"
    assert "2026-09-16" in text, "Missing 2026-09-16 audit date in THIRD_PARTY_LICENSES.md"


def test_marketing_log_pfad_b_section_11():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")

    assert (
        "11. VISUAL LIFECYCLE ARCHITECTURE, INTEROPERABILITY PROTOCOLS & SEO AUDIT "
        "(v1.3.4 -- 2026-09-26) [Pfad B]"
    ) in text
    assert "Multi-Agent Concurrency & State Machine Lifecycle" in text
    assert "Component Interoperability & Communication Wire Protocols" in text
    assert "stateDiagram-v2" in text


def test_auto_assign_workflow_integrity():
    workflow_file = REPO_ROOT / ".github" / "workflows" / "auto-assign.yml"
    assert workflow_file.exists(), ".github/workflows/auto-assign.yml must exist"
    text = workflow_file.read_text(encoding="utf-8")

    assert "actions/github-script@v7" in text
    assert "timeout-minutes: 5" in text
    assert "cancel-in-progress: true" in text
    assert "pull-requests: write" in text
    assert "pull_request_target:" in text


def test_label_sync_workflow_and_labels_yml():
    workflow_file = REPO_ROOT / ".github" / "workflows" / "label-sync.yml"
    assert workflow_file.exists(), ".github/workflows/label-sync.yml must exist"
    text = workflow_file.read_text(encoding="utf-8")

    assert "EndBug/label-sync@v2" in text
    assert "timeout-minutes: 5" in text
    assert "cancel-in-progress: true" in text
    assert "issues: write" in text

    labels_file = REPO_ROOT / ".github" / "labels.yml"
    assert labels_file.exists(), ".github/labels.yml must exist"
    labels_text = labels_file.read_text(encoding="utf-8")
    expected_labels = [
        "bug",
        "enhancement",
        "good first issue",
        "help wanted",
        "documentation",
        "duplicate",
        "wontfix",
        "priority: high",
        "priority: low",
        "needs-triage",
        "stale",
    ]
    for label in expected_labels:
        assert f"name: {label}" in labels_text or f"name: '{label}'" in labels_text, (
            f"Missing standard label {label} in .github/labels.yml"
        )


def test_level_1_sbom_text_companion_and_parity():
    txt_file = REPO_ROOT / "THIRD_PARTY_LICENSES.txt"
    assert txt_file.exists(), "THIRD_PARTY_LICENSES.txt must exist in repo root"
    text = txt_file.read_text(encoding="utf-8")

    assert "THIRD-PARTY LICENSES & LEVEL 1 SBOM NOTICE" in text
    assert "1.3.4" in text
    assert "RunAsInvoker" in text
    assert "Zero-Copyleft Isolation Guarantee" in text

    expected_invariants = [
        "INV-LOCAL-01",
        "INV-USER-02",
        "INV-LOCK-03",
        "INV-ROUT-04",
        "INV-AVAT-05",
        "INV-MANI-06",
        "INV-PIN-07",
        "INV-SAND-08",
        "INV-SYNC-09",
        "INV-SLA-10",
    ]
    for inv in expected_invariants:
        assert inv in text, f"Missing invariant {inv} in THIRD_PARTY_LICENSES.txt"

    notice_text = (REPO_ROOT / "NOTICE").read_text(encoding="utf-8")
    assert "THIRD_PARTY_LICENSES.txt" in notice_text


def test_pytest_basetemp_and_norecursedirs_hardening():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    pytest_cfg = data.get("tool", {}).get("pytest", {}).get("ini_options", {})
    addopts = pytest_cfg.get("addopts", "")
    assert "--basetemp=.pytest_temp" in addopts, (
        "pytest addopts must specify --basetemp=.pytest_temp"
    )

    norecursedirs = pytest_cfg.get("norecursedirs", [])
    assert ".pytest_temp" in norecursedirs, "norecursedirs must include .pytest_temp"
    assert ".pytest_tmp*" in norecursedirs, "norecursedirs must include .pytest_tmp*"


def test_extended_lock_defense_and_pytest_temp_in_gitignore():
    gitignore_file = REPO_ROOT / ".gitignore"
    assert gitignore_file.exists(), ".gitignore must exist"
    text = gitignore_file.read_text(encoding="utf-8")

    expected_patterns = [
        "*-IDEAPAD*",
        "Desktop.ini",
        "ehthumbs.db",
        "*.swo",
        ".pytest_temp/",
        ".pytest_tmp*/",
    ]
    for pat in expected_patterns:
        assert pat in text, f"Missing pattern {pat} in .gitignore"


def test_third_party_licenses_audit_2026_09_29():
    md_file = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
    txt_file = REPO_ROOT / "THIRD_PARTY_LICENSES.txt"
    assert md_file.exists() and txt_file.exists()

    md_text = md_file.read_text(encoding="utf-8")
    txt_text = txt_file.read_text(encoding="utf-8")

    assert "2026-09-29" in md_text, "Missing 2026-09-29 in THIRD_PARTY_LICENSES.md"
    assert "2026-09-29" in txt_text, "Missing 2026-09-29 in THIRD_PARTY_LICENSES.txt"
    assert "THIRD_PARTY_LICENSES.txt" in md_text


def test_marketing_log_pfad_a_section_12():
    mkt_file = REPO_ROOT / "MARKETING-LOG.txt"
    assert mkt_file.exists(), "MARKETING-LOG.txt must exist"
    text = mkt_file.read_text(encoding="utf-8")

    assert (
        "12. TECHNICAL HYGIENE, CI WORKFLOW LIFECYCLE & LEVEL 1 SBOM AUDIT "
        "(v1.3.4 -- 2026-09-29) [Pfad A]"
    ) in text
    assert "auto-assign.yml" in text
    assert "label-sync.yml" in text
    assert "THIRD_PARTY_LICENSES.txt" in text

