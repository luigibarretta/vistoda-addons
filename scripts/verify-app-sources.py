#!/usr/bin/env python3
"""Refuse to publish an app release whose source calls guarded vendor endpoints unsafely.

Each catalog app is fetched at its exact release tag (`v<version>` of the
repository in its config.yaml `url`) and scanned against
contracts/source-guards.json. Comment lines are ignored; a pattern in
executable source must live only in an allowed file that also carries every
required guard marker.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "source-guards.json"
SOURCE_SUFFIXES = {".rs", ".py", ".sh", ".js", ".mjs", ".jq"}
COMMENT = re.compile(r"^\s*(//|#|/\*|\*)")


def code_lines(path: Path) -> list[str]:
    """Executable lines only: line comments and doc comments are skipped."""
    text = path.read_text(encoding="utf-8", errors="replace")
    return [line for line in text.splitlines() if not COMMENT.match(line)]


def check_tree(app: str, root: Path, rules: list[dict]) -> list[str]:
    """Return human-readable violations for one source tree."""
    errors = []
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix in SOURCE_SUFFIXES]
    files = [p for p in files if ".git" not in p.parts and "tests" not in p.parts]
    for rule in rules:
        pattern, allowed = rule["pattern"], set(rule.get("allowed_files", []))
        for path in files:
            relative = path.relative_to(root).as_posix()
            if relative.endswith("_tests.rs") or "/tests" in relative:
                continue
            lines = code_lines(path)
            if not any(pattern in line for line in lines):
                continue
            if relative not in allowed:
                errors.append(f"{app}: {pattern} used outside its guard in {relative}")
                continue
            body = "\n".join(lines)
            for marker in rule.get("required_markers", []):
                if marker not in body:
                    errors.append(f"{app}: {relative} calls {pattern} without guard marker {marker!r}")
    return errors


def app_source(app: str) -> tuple[str, str]:
    config = (ROOT / app / "config.yaml").read_text(encoding="utf-8")
    url = re.search(r"^url:\s*(\S+)\s*$", config, re.M)
    version = re.search(r"^version:\s*(\S+)\s*$", config, re.M)
    if not url or not version:
        raise SystemExit(f"{app}: config.yaml lacks url or version")
    return url.group(1), version.group(1)


def fetch(url: str, version: str, target: Path) -> None:
    subprocess.run(
        ["git", "-c", "advice.detachedHead=false", "clone", "--quiet", "--depth", "1",
         "--branch", f"v{version}", f"{url}.git", str(target)],
        check=True,
        timeout=180,
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tree", nargs=2, metavar=("APP", "PATH"), help="scan a local tree instead")
    args = parser.parse_args(argv)
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if contract.get("schema") != 1:
        raise SystemExit("unsupported source-guard contract schema")
    errors: list[str] = []
    if args.tree:
        app, path = args.tree
        errors = check_tree(app, Path(path), contract["apps"].get(app, []))
    else:
        for app, rules in sorted(contract["apps"].items()):
            if not rules:
                continue
            url, version = app_source(app)
            with tempfile.TemporaryDirectory() as directory:
                fetch(url, version, Path(directory) / "src")
                errors += check_tree(app, Path(directory) / "src", rules)
            print(f"{app} {version}: source guards checked")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
