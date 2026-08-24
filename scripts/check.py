#!/usr/bin/env python3
"""Dependency-free repository contract checks."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
APPS = ("vistoda_blink", "vistoda_ezviz", "vistoda_ring")
IMAGE = re.compile(r"^image: ghcr\.io/luigibarretta/vistoda-[a-z]+-addon$", re.MULTILINE)
VERSION = re.compile(r"^version: [0-9]+\.[0-9]+\.[0-9]+$", re.MULTILINE)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def check_app(name: str) -> None:
    directory = ROOT / name
    config = (directory / "config.yaml").read_text(encoding="utf-8")
    require(VERSION.search(config) is not None, f"{name}: invalid version")
    require(IMAGE.search(config) is not None, f"{name}: invalid image")
    require("  - amd64\n  - aarch64\n" in config, f"{name}: multiarch missing")
    require("hassio_api: true" in config, f"{name}: Supervisor discovery unavailable")
    require("tcp: null" in config, f"{name}: provider port must stay private")
    require((directory / "DOCS.md").is_file(), f"{name}: DOCS.md missing")
    if name == "vistoda_ring":
        require("recording_storage: private" in config, "Ring storage default missing")
        require(
            "recording_storage: list(private|addon_config|media|share)" in config,
            "Ring storage choices missing",
        )
        for mount in ("addon_config", "media", "share"):
            require(f"  - type: {mount}\n    read_only: false" in config, f"{mount} RW map missing")
    for language in ("en", "it"):
        require(
            (directory / "translations" / f"{language}.yaml").is_file(),
            f"{name}: {language} translation missing",
        )


def check_loc() -> None:
    suffixes = {".json", ".md", ".py", ".yaml", ".yml"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in suffixes and ".git" not in path.parts:
            lines = len(path.read_text(encoding="utf-8").splitlines())
            require(lines <= 250, f"{path.relative_to(ROOT)} exceeds 250 LOC: {lines}")


def main() -> None:
    require((ROOT / "repository.yaml").is_file(), "repository.yaml missing")
    for app in APPS:
        check_app(app)
    check_loc()
    print("Vistoda Apps repository contracts passed")


if __name__ == "__main__":
    main()
