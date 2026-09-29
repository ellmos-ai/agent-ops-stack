# Third-Party Licenses & Transparency Notice

> **Project:** `ellmos-ai/agent-ops-stack`<br>
> **Version:** `1.3.4`<br>
> **Audited:** 2026-09-29 (Pfad A Re-audit; previous audits 2026-09-26, 2026-09-21, 2026-09-16)<br>
> **Repository License:** [MIT License](LICENSE)<br>
> **Attribution & SBOM:** [NOTICE](NOTICE) | [Plain Text SBOM Companion](THIRD_PARTY_LICENSES.txt)<br>
> **Architecture & Privacy:** 100% Local-First, Zero-Egress by default, Unprivileged User-Mode (`RunAsInvoker`)

---

## Executive Summary & Compliance Assurance

`agent-ops-stack` is engineered as a declarative, manifest-driven composition layer for multi-agent CLI coordination. The repository itself contains **zero mandatory runtime dependencies** beyond the standard Python runtime and POSIX shell utilities.

All direct, optional, and development dependencies utilized in `agent-ops-stack` are distributed under strictly **permissive open-source licenses** (MIT, Apache-2.0, PSFL). There are **zero copyleft, GPL, or AGPL dependencies** in the core composition or packaging harness, ensuring maximum flexibility for enterprise engineering teams, multi-agent frameworks, and autonomous developer workflows.

Furthermore, `agent-ops-stack` strictly guarantees compliance across ten canonical governance and runtime invariants:

| Invariant ID | Name | Architectural Guarantee | Compliance Status |
|:---:|:---|:---|:---:|
| **INV-LOCAL-01** | 100% Local-First & Zero Egress | Manifest parsing and coordination run 100% offline; zero telemetry. | :white_check_mark: Verified |
| **INV-USER-02** | Unprivileged User-Mode | Runs under standard user rights (`RunAsInvoker`); zero root/admin elevation. | :white_check_mark: Verified |
| **INV-LOCK-03** | Fail-Closed Lock Integrity | Mutating operations halt immediately upon active `LOCK*.txt` files. | :white_check_mark: Verified |
| **INV-ROUT-04** | Structured Ticket Routing | Problem reports and tasks are dispatched through `ticket-master`. | :white_check_mark: Verified |
| **INV-AVAT-05** | Empirical Decision-Avatar | Operator absence resolves ambiguity via `build-your-users-mind`. | :white_check_mark: Verified |
| **INV-MANI-06** | Deterministic Manifest Blueprint | Manifest schema `ellmos-stack-manifest-v1` governs all wiring. | :white_check_mark: Verified |
| **INV-PIN-07** | Immutable Release-Tag Pinning | Composed sources reference immutable tags; zero unpinned branch drift. | :white_check_mark: Verified |
| **INV-SAND-08** | Sandboxed Installer Boundary | `install.sh` clones exclusively into gitignored `./modules/`. | :white_check_mark: Verified |
| **INV-SYNC-09** | Cross-Device Slot-Gated Sync | Multi-host file sync relies on dedicated `sync-master` host slots. | :white_check_mark: Verified |
| **INV-SLA-10** | 48h Security & Triage SLA | Security disclosures acknowledged within 48h; triage within 5 days. | :white_check_mark: Verified |

---

## Runtime Dependency Matrix

| Package / Tool | Role / Functional Scope | License | Project Repository / Upstream |
|:---|:---|:---|:---|
| **Python Standard Library** | Manifest validation, metadata contracts, path resolution (`json`, `re`, `pathlib`, `tomllib`, `typing`) | [PSFL-2.0](https://docs.python.org/3/license.html) | [python/cpython](https://github.com/python/cpython) |
| **POSIX Shell / Git** | Declarative installer script (`install.sh`), repository cloning into `./modules/` | System / GPL / MIT | System tools |

---

## Composed Modules (Referenced via Manifest)

The seven composed modules orchestrated by `agent-ops.manifest.json` are independently maintained open-source repositories:

| Module Name | Repository | Kind / Role | License |
|:---|:---|:---|:---|
| **ticket-master** | [dev-bricks/ticket-master](https://github.com/dev-bricks/ticket-master) | `coordination` (ticket-routing) | MIT License |
| **lock-master** | [dev-bricks/lock-master](https://github.com/dev-bricks/lock-master) | `coordination` (file locking) | MIT License |
| **sync-master** | [dev-bricks/sync-master](https://github.com/dev-bricks/sync-master) | `sync` (machine slot file-sync) | MIT License |
| **build-your-users-mind** | [ellmos-ai/build-your-users-mind](https://github.com/ellmos-ai/build-your-users-mind) | `decision` (decision-avatar) | MIT License |
| **skills** | [ellmos-ai/skills](https://github.com/ellmos-ai/skills) | `skills` (reusable skill pack) | MIT License |
| **ellmos-controlcenter-mcp**| [ellmos-ai/ellmos-controlcenter-mcp](https://github.com/ellmos-ai/ellmos-controlcenter-mcp) | `mcp` (control plane) | MIT License |
| **ellmos-homebase-mcp** | [ellmos-ai/ellmos-homebase-mcp](https://github.com/ellmos-ai/ellmos-homebase-mcp) | `mcp` (runtime & memory facade) | MIT License |

---

## Development & Quality Assurance Tooling

| Package | Usage & Purpose | License | Source / Upstream |
|:---|:---|:---|:---|
| **pytest** | Automated test runner, contract verification suites, mock fixtures | [MIT](https://github.com/pytest-dev/pytest/blob/main/LICENSE) | [pytest-dev/pytest](https://github.com/pytest-dev/pytest) |
| **ruff** | High-performance Python linter and code formatting enforcement | [MIT / Apache-2.0](https://github.com/astral-sh/ruff/blob/main/LICENSE-MIT) | [astral-sh/ruff](https://github.com/astral-sh/ruff) |
| **setuptools** | Standard package build backend (PEP 517 / PEP 621 compliant) | [MIT](https://github.com/pypa/setuptools/blob/main/LICENSE) | [pypa/setuptools](https://github.com/pypa/setuptools) |

---

## Full License Texts (Excerpts & Notices)

### 1. Python Software Foundation License Version 2 (PSFL-2.0)
Python standard library modules (e.g. `json`, `re`, `pathlib`, `tomllib`, `typing`) are used under the PSF License Agreement.  
Copyright (c) 2001-2026 Python Software Foundation. All rights reserved.

### 2. MIT License (MIT)
Used by `pytest`, `ruff`, `setuptools`, and all composed stack modules.

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  
>  
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  
>  
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### 3. Apache License Version 2.0 (Apache-2.0)
Co-licensed by `ruff`.

> Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at:  
> http://www.apache.org/licenses/LICENSE-2.0  
> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
