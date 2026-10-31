# Third-party license inventory

**Checked:** 2026-10-12
**Scope:** Direct `LICENSE` files at the exact source commits selected by `agent-ops.manifest.json` on the date above.

## What this inventory covers

The root repository's [`LICENSE`](LICENSE) is MIT and applies to this repository. The installer fetches independent repositories; it does not vendor their files in this source tree. The table records only each selected source commit's direct `LICENSE` file. It does not cover transitive dependencies, complete source contents, provider CLIs, system tools, compatibility, or later changes to a moving ref. This is a bounded source check, not a complete SBOM or a legal certification.

| Manifest name | Selected commit | Direct license text |
| --- | --- | --- |
| `ticket-master` | [`c68e16b`](https://github.com/dev-bricks/ticket-master/blob/c68e16b98497cb78ba1f84f363e9c3960009e98f/LICENSE) | MIT |
| `lock-master` | [`4513064`](https://github.com/dev-bricks/lock-master/blob/4513064c84cac963a86d23cab97fa8c69049b380/LICENSE) | MIT |
| `sync-master` | [`ed1ebf2`](https://github.com/dev-bricks/sync-master/blob/ed1ebf283bcb239d3fe52e2cdf74d7dc2e95e60c/LICENSE) | MIT |
| `build-your-users-mind` | [`e3843a4`](https://github.com/ellmos-ai/build-your-users-mind/blob/e3843a4fa58e75f38a90de2fb426c5d37c0b6ec7/LICENSE) | MIT |
| `skills` | [`3f87a45`](https://github.com/ellmos-ai/skills/blob/3f87a456a18282ed8d07bd5634587c4da261dea3/LICENSE) | MIT |
| `controlcenter-mcp` | [`ab21204`](https://github.com/ellmos-ai/ellmos-controlcenter-mcp/blob/ab2120464823d36f705031da701d630b889858a5/LICENSE) | MIT |
| `homebase-mcp` | [`0fbd06b`](https://github.com/ellmos-ai/ellmos-homebase-mcp/blob/0fbd06b3511facf3d669ab0ef5f17b6d535824b1/LICENSE) | MIT |
| `clutch` | [`67c5b72`](https://github.com/ellmos-ai/clutch/blob/67c5b72fd2ea6d1e91e47f363d8ab9f951b9fd44/LICENSE) | MIT |

The `clutch` row was checked on 2026-10-31; the other rows on the date above. The direct license files above contain MIT license text. Their licensing applies to the respective upstream projects and does not establish compatibility, code provenance, or the license of every dependency they may use.

## External tools and development dependencies

The installer requires Git and either `jq` or Python 3. These are external tools, not bundled libraries. Git maintains its own license in [COPYING](https://github.com/git/git/blob/master/COPYING). The Python project metadata declares a test extra (`pytest`, `ruff`, and conditional `tomli`) and uses setuptools as its build backend. Those tools and their transitive dependencies retain their own licenses; this file does not enumerate their dependency trees.

## Statutory references

The MIT project license is included unchanged. Whether statutory provisions such as sections 516 or 521 BGB apply depends on the legal relationship and applicable law. This inventory does not classify every use as a gift and makes no blanket statement about liability.

See the plain-text companion [`THIRD_PARTY_LICENSES.txt`](THIRD_PARTY_LICENSES.txt) for a compact list of the same scope and source links.
