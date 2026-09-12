#!/usr/bin/env python3
"""Dependency-free repository contract checks."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
APPS = ("vistoda_blink", "vistoda_ezviz", "vistoda_ring")
EXPECTED_VERSIONS = {
    "vistoda_blink": "0.15.3",
    "vistoda_ezviz": "0.7.1",
    "vistoda_ring": "0.13.1",
}
IMAGE = re.compile(r"^image: ghcr\.io/luigibarretta/vistoda-[a-z]+-addon$", re.MULTILINE)
VERSION = re.compile(r"^version: [0-9]+\.[0-9]+\.[0-9]+$", re.MULTILINE)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def check_app(name: str) -> None:
    directory = ROOT / name
    config = (directory / "config.yaml").read_text(encoding="utf-8")
    require(VERSION.search(config) is not None, f"{name}: invalid version")
    version = re.search(r"^version: ([0-9]+\.[0-9]+\.[0-9]+)$", config, re.MULTILINE)
    require(version is not None, f"{name}: version missing")
    require(version.group(1) == EXPECTED_VERSIONS[name], f"{name}: release matrix drift")
    changelog = (directory / "CHANGELOG.md").read_text(encoding="utf-8")
    require(f"## {EXPECTED_VERSIONS[name]}" in changelog, f"{name}: changelog drift")
    require(IMAGE.search(config) is not None, f"{name}: invalid image")
    require("  - amd64\n  - aarch64\n" in config, f"{name}: multiarch missing")
    require("hassio_api: true" in config, f"{name}: Supervisor discovery unavailable")
    require("tcp: null" in config, f"{name}: provider port must stay private")
    require((directory / "DOCS.md").is_file(), f"{name}: DOCS.md missing")
    for asset, expected_size in (("icon.png", 128), ("logo.png", 300)):
        image = (directory / asset).read_bytes()
        require(image.startswith(b"\x89PNG\r\n\x1a\n"), f"{name}: {asset} is not PNG")
        width = int.from_bytes(image[16:20], "big")
        height = int.from_bytes(image[20:24], "big")
        require(
            width == height == expected_size,
            f"{name}: {asset} must be {expected_size}px square",
        )
        require(len(image) <= 2 * 1024 * 1024, f"{name}: {asset} exceeds 2 MiB")
    if name == "vistoda_ring":
        require("intercoms: []" in config, "Ring legacy single-device default missing")
        require("device_id: int(1,9007199254740991)" in config, "Ring explicit device bindings missing")
        require("recording_storage: private" in config, "Ring storage default missing")
        require(
            "recording_storage: list(private|addon_config|media|share|network)" in config,
            "Ring storage choices missing",
        )
        require(
            "recording_network_mount: str?" in config,
            "Ring network mount missing",
        )
        for mount in ("addon_config", "media", "share"):
            require(f"  - type: {mount}\n    read_only: false" in config, f"{mount} RW map missing")
    if name == "vistoda_ezviz":
        require("cameras: []" in config, "EZVIZ legacy single-device default missing")
        require("camera_serial: match(^[A-Za-z0-9]*$)" in config, "EZVIZ legacy serial must be optional")
        require("camera_channel: int(1,256)" in config, "EZVIZ channel must be bounded")
        require("substream: bool" in config, "EZVIZ substream option missing")
        require("alias: match(^[A-Za-z0-9_-]{1,64}$)" in config, "EZVIZ camera aliases must be bounded")
        require("serial: match(^[A-Za-z0-9]+$)" in config, "EZVIZ list serial must be non-empty")
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
