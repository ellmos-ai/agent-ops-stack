#!/usr/bin/env bash
# install.sh — reads agent-ops.manifest.json and clones/wires every listed module.
#
# The manifest IS the blueprint: this script has no stack-specific logic beyond
# "read the manifest, clone what it lists, print how it's wired." Adding, removing,
# or repointing a module means editing agent-ops.manifest.json, not this script.
#
# Usage:
#   ./install.sh [target-dir]
#
# Requires: git, and either `jq` or `python3` to parse the manifest JSON.

set -euo pipefail

MANIFEST="$(dirname "$0")/agent-ops.manifest.json"
TARGET="${1:-modules}"

if [ ! -f "$MANIFEST" ]; then
  echo "error: manifest not found at $MANIFEST" >&2
  exit 1
fi

mkdir -p "$TARGET"

# --- JSON access helpers -----------------------------------------------------
# Prefer jq; fall back to python3 so the script works with either toolchain.

if command -v jq >/dev/null 2>&1; then
  # `tr -d '\r'` guards against Windows-native jq builds emitting CRLF.
  json_names()  { jq -r '.modules[].name' "$MANIFEST" | tr -d '\r'; }
  json_field()  { jq -r --arg n "$1" --arg f "$2" '.modules[] | select(.name==$n) | .[$f] // empty' "$MANIFEST" | tr -d '\r'; }
  json_repo()   { jq -r --arg n "$1" '.modules[] | select(.name==$n) | .source.repo' "$MANIFEST" | tr -d '\r'; }
  json_ref()    { jq -r --arg n "$1" '.modules[] | select(.name==$n) | (.source.ref // "main")' "$MANIFEST" | tr -d '\r'; }
  json_provides() { jq -r --arg n "$1" '.modules[] | select(.name==$n) | (.wiring.provides // []) | join(", ")' "$MANIFEST" | tr -d '\r'; }
  json_consumes() { jq -r --arg n "$1" '.modules[] | select(.name==$n) | (.wiring.consumes // []) | join(", ")' "$MANIFEST" | tr -d '\r'; }
elif command -v python3 >/dev/null 2>&1; then
  # Windows-native python3 builds print CRLF line endings even under Git Bash;
  # strip stray \r so word-splitting/`-d`-comparisons below don't break paths/URLs.
  _py() {
    PYTHONIOENCODING=utf-8 python3 -c "
import json, sys
m = json.load(open(r'$MANIFEST', encoding='utf-8'))
name = sys.argv[1] if len(sys.argv) > 1 else None
field = sys.argv[2] if len(sys.argv) > 2 else None
for mod in m['modules']:
    if name is None:
        print(mod['name'])
        continue
    if mod['name'] != name:
        continue
    if field == 'repo':
        print(mod['source']['repo'])
    elif field == 'ref':
        print(mod['source'].get('ref', 'main'))
    elif field == 'provides':
        print(', '.join(mod.get('wiring', {}).get('provides', [])))
    elif field == 'consumes':
        print(', '.join(mod.get('wiring', {}).get('consumes', [])))
" "$@" | tr -d '\r'
  }
  json_names()    { _py; }
  json_repo()     { _py "$1" repo; }
  json_ref()      { _py "$1" ref; }
  json_provides() { _py "$1" provides; }
  json_consumes() { _py "$1" consumes; }
else
  echo "error: need either 'jq' or 'python3' on PATH to read the manifest" >&2
  exit 1
fi

# --- Clone + wire --------------------------------------------------------------

echo "agent-ops-stack: installing into '$TARGET/' from $(basename "$MANIFEST")"
echo

for name in $(json_names); do
  repo="$(json_repo "$name")"
  ref="$(json_ref "$name")"
  dest="$TARGET/$name"

  if [ -d "$dest/.git" ]; then
    echo "[$name] already present at $dest — skipping clone (run 'git -C \"$dest\" pull' to update)"
  else
    echo "[$name] cloning https://github.com/$repo (ref: $ref) -> $dest"
    git clone --quiet --branch "$ref" "https://github.com/$repo.git" "$dest"
  fi
done

echo
echo "--- Wiring summary -------------------------------------------------------"
for name in $(json_names); do
  provides="$(json_provides "$name")"
  consumes="$(json_consumes "$name")"
  printf '%-24s provides: %-40s consumes: %s\n' "$name" "${provides:-—}" "${consumes:-—}"
done

echo
echo "Done. See README.md for how each module's provided capability is meant to be"
echo "consumed by the others (MCP registration, skill installation, etc. still"
echo "needs each module's own setup steps — this installer only fetches and"
echo "reports the wiring, it does not register MCP servers or deploy skills)."
