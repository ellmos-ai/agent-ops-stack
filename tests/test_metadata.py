"""Automated metadata, discoverability, documentation, and parity contract tests."""

import json
import re
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

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


def test_security_policy_exists_and_bilingual_parity():
    sec_file = REPO_ROOT / "SECURITY.md"
    assert sec_file.exists(), "SECURITY.md must exist"
    text = sec_file.read_text(encoding="utf-8")

    assert "## English" in text
    assert "## Deutsch" in text
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
    assert version in llms_text


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

    for name in (
        "ticket-master",
        "lock-master",
        "sync-master",
        "build-your-users-mind",
        "skills",
        "ellmos-controlcenter-mcp",
        "ellmos-homebase-mcp",
    ):
        assert name in text
    assert len(re.findall(r"blob/[0-9a-f]{40}/LICENSE", text)) == 7




def test_llms_txt_structure_and_parity():
    llms_file = REPO_ROOT / "llms.txt"
    assert llms_file.exists(), "llms.txt must exist"
    text = llms_file.read_text(encoding="utf-8")

    assert "agent-ops.manifest.json" in text
    assert "install.sh" in text
    assert "THIRD_PARTY_LICENSES.md" in text
    assert "## Related projects" in text
    assert "## Security and license boundaries" in text


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
    assert "assets/banner.png" in readme_de


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










def test_security_model_and_sla_sections():
    for filename in ["README.md", "README_de.md"]:
        text = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "## 14. " in text, f"Missing section 14 in {filename}"
        assert "## 17. " in text, f"Missing section 17 in {filename}"








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






def test_contributing_guidelines_exist_and_bilingual_parity():
    contrib_file = REPO_ROOT / "CONTRIBUTING.md"
    assert contrib_file.exists(), "CONTRIBUTING.md must exist in repository root"
    text = contrib_file.read_text(encoding="utf-8")

    assert "[English](#english)" in text
    assert "[Deutsch](#deutsch)" in text
    assert '<a id="english"></a>' in text
    assert '<a id="deutsch"></a>' in text


def test_pep621_contributing_and_sbom_urls():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))

    urls = data.get("project", {}).get("urls", {})
    assert "Contributing" in urls
    assert urls["Contributing"].endswith("/CONTRIBUTING.md")
    assert "Third-Party Licenses" in urls
    assert urls["Third-Party Licenses"].endswith("/THIRD_PARTY_LICENSES.md")
    assert "Third-Party Licenses (Text)" in urls
    assert urls["Third-Party Licenses (Text)"].endswith("/THIRD_PARTY_LICENSES.txt")

    pytest_opts = data.get("tool", {}).get("pytest", {}).get("ini_options", {})
    norecursedirs = pytest_opts.get("norecursedirs", [])
    assert ".turbo" in norecursedirs
    assert ".nyc_output" in norecursedirs


def test_extended_lock_defense_and_multihost_tokens():
    gitignore_file = REPO_ROOT / ".gitignore"
    assert gitignore_file.exists(), ".gitignore must exist"
    text = gitignore_file.read_text(encoding="utf-8")

    expected_patterns = [
        "LOCK.dev.*",
        "LOCK.antigravity.*",
        "LOCK.bugsearch.*",
        "TASKPLAN_*.md",
        "*-TASKPLAN*",
    ]
    for pat in expected_patterns:
        assert pat in text, f"Missing pattern {pat} in .gitignore"








def test_version_freeze_discipline_t_20260920():
    pyproject_file = REPO_ROOT / "pyproject.toml"
    assert pyproject_file.exists()
    data = tomllib.loads(pyproject_file.read_text(encoding="utf-8"))
    assert data["project"]["version"] == "1.3.4", (
        "Version must remain strictly 1.3.4 per T-20260920-167562623"
    )

    manifest_file = REPO_ROOT / "agent-ops.manifest.json"
    assert manifest_file.exists()
    mdata = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert mdata["name"] == "agent-ops-stack"




def test_quick_navigation_numeric_sec_anchors_parity():
    readme_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    readme_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    for num in range(1, 19):
        anchor = f'id="sec-{num:02d}"'
        assert anchor in readme_en, f"Missing {anchor} in README.md"
        assert anchor in readme_de, f"Missing {anchor} in README_de.md"
