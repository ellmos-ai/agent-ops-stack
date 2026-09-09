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
        "img.shields.io/badge/version-1.3.1-blue.svg",
        "img.shields.io/badge/CI-GitHub%20Actions-brightgreen.svg",
        "img.shields.io/badge/tests-15%20passed%20%7C%20100%25-brightgreen.svg",
        "img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg",
        "img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg",
        "img.shields.io/badge/architecture-100%25%20Local--First%20%7C%20Zero--Egress-success.svg",
        "img.shields.io/badge/security-Non--Elevation%20%7C%20Sandboxed-informational.svg",
        "img.shields.io/badge/License-MIT-green.svg",
        "img.shields.io/badge/Ecosystem-ellmos--ai-purple.svg",
        "img.shields.io/badge/Umbrella-open--bricks-blue.svg",
        "img.shields.io/badge/LLM--Ready-llms.txt-success.svg",
    ]
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        for badge in expected_badges:
            assert badge in text, f"Missing badge {badge} in {filename}"


def test_quick_navigation_14_points():
    readme_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    # Match numbered markdown list items 1. through 14.
    en_nav_items = re.findall(r"^\d+\.\s+\[.+?\]\(#.+?\)", readme_en, flags=re.MULTILINE)
    de_nav_items = re.findall(r"^\d+\.\s+\[.+?\]\(#.+?\)", readme_de, flags=re.MULTILINE)

    assert len(en_nav_items) == 14, (
        f"README.md must have 14 quick nav items, found {len(en_nav_items)}"
    )
    assert len(de_nav_items) == 14, (
        f"README_de.md must have 14 quick nav items, found {len(de_nav_items)}"
    )

    # Check that major target sections 1 through 14 exist in both
    for section_num in range(1, 15):
        assert f"## {section_num}. " in readme_en, f"Missing section ## {section_num}. in README.md"
        assert f"## {section_num}. " in readme_de, (
            f"Missing section ## {section_num}. in README_de.md"
        )


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
    assert project.get("version") == "1.3.1"
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
    assert "Changelog" in urls
    assert "Security" in urls
    assert "Parent Organization" in urls
    assert "Umbrella Ecosystem" in urls
    assert urls["Parent Organization"] == "https://github.com/ellmos-ai"
    assert urls["Umbrella Ecosystem"] == "https://github.com/open-bricks"

    assert "tool" in data and "ruff" in data["tool"]


def test_version_parity_across_artifacts():
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    version = pyproject["project"]["version"]
    assert version == "1.3.1"

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

    # Multi-agent lock patterns
    assert "\nLOCK\n" in f"\n{text}\n", "Missing standalone LOCK in .gitignore"
    assert "LOCK.*" in text, "Missing LOCK.* pattern in .gitignore"
    assert "*.lock" in text, "Missing *.lock pattern in .gitignore"
    assert "LOCK*.txt" in text, "Missing LOCK*.txt pattern in .gitignore"
    assert "LOCK.permissions.json" in text, "Missing LOCK.permissions.json in .gitignore"

    # Test & packaging caches
    assert ".pytest_cache/" in text, "Missing .pytest_cache/ in .gitignore"
    assert ".ruff_cache/" in text, "Missing .ruff_cache/ in .gitignore"
    assert ".coverage" in text, "Missing .coverage in .gitignore"
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
    assert "python -m compileall -q tests" in text, "CI must contain bytecode compilation gate"
    assert "pytest -ra -v" in text, "CI must run standardized pytest -ra -v"
    for os_name in ["ubuntu-latest", "windows-latest", "macos-latest"]:
        assert os_name in text, f"CI matrix missing {os_name}"


def test_changelog_release_entry():
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "## 1.3.1 (2026-09-09)" in changelog, "CHANGELOG.md missing 1.3.1 release entry"
    assert "Pfad A" in changelog, "CHANGELOG.md 1.3.1 entry must reference Pfad A"
