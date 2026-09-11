#!/usr/bin/env python3
"""Verify public OCI bytes, both architectures, exact source and signatures."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parents[1]
ACCEPT = ", ".join((
    "application/vnd.oci.image.index.v1+json",
    "application/vnd.oci.image.manifest.v1+json",
    "application/vnd.docker.distribution.manifest.list.v2+json",
    "application/vnd.docker.distribution.manifest.v2+json",
))


def get(url: str, headers: dict | None = None):
    request = urllib.request.Request(url, headers=headers or {})
    return urllib.request.urlopen(request, timeout=30)


def source_revision(repository: str, tag: str) -> str:
    # Anonymous access proves the release source is publicly available.
    with get(f"https://api.github.com/repos/{repository}/git/ref/tags/{tag}") as response:
        source = json.load(response)["object"]
    for _ in range(5):
        if source.get("type") == "commit":
            break
        if source.get("type") != "tag" or not re.fullmatch(r"[0-9a-f]{40}", source["sha"]):
            raise SystemExit("Release ref must resolve to a commit")
        with get(f"https://api.github.com/repos/{repository}/git/tags/{source['sha']}") as response:
            source = json.load(response)["object"]
    if source.get("type") != "commit":
        raise SystemExit("Release tag chain is invalid")
    revision = source["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise SystemExit("Invalid source revision")
    return revision


def verify(provider: str) -> dict:
    config = (ROOT / f"vistoda_{provider}/config.yaml").read_text()
    version = re.search(r"^version: (\S+)$", config, re.MULTILINE).group(1)
    image = re.search(r"^image: (\S+)$", config, re.MULTILINE).group(1)
    name = image.removeprefix("ghcr.io/")
    if image != f"ghcr.io/luigibarretta/vistoda-{provider}-addon":
        raise SystemExit("Unexpected image repository")
    repository = f"luigibarretta/vistoda-{provider}"
    tag = f"v{version}"
    revision = source_revision(repository, tag)
    query = urllib.parse.urlencode({"service": "ghcr.io", "scope": f"repository:{name}:pull"})
    with get(f"https://ghcr.io/token?{query}") as response:
        token = json.load(response)["token"]
    headers = {"Authorization": f"Bearer {token}", "Accept": ACCEPT}
    with get(f"https://ghcr.io/v2/{name}/manifests/{version}", headers) as response:
        raw = response.read()
        digest = response.headers.get("Docker-Content-Digest", "")
    if digest != "sha256:" + hashlib.sha256(raw).hexdigest():
        raise SystemExit(f"{provider}: registry digest does not match manifest bytes")
    manifest = json.loads(raw)
    platforms = {
        f"{entry.get('platform', {}).get('os')}/{entry.get('platform', {}).get('architecture')}": entry["digest"]
        for entry in manifest.get("manifests", [])
        if entry.get("platform", {}).get("os") != "unknown"
    }
    if set(platforms) != {"linux/amd64", "linux/arm64"}:
        raise SystemExit(f"{provider}: exact amd64/arm64 manifest pair required")
    for child_digest in platforms.values():
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", child_digest):
            raise SystemExit("Invalid architecture digest")
        with get(f"https://ghcr.io/v2/{name}/manifests/{child_digest}", headers) as response:
            child = response.read()
        if "sha256:" + hashlib.sha256(child).hexdigest() != child_digest:
            raise SystemExit("Architecture manifest bytes do not match digest")
    immutable = f"{image}@{digest}"
    workflow = f"{repository}/.github/workflows/release.yaml"
    subprocess.run([
        "cosign", "verify", immutable,
        "--certificate-identity", f"https://github.com/{workflow}@refs/tags/{tag}",
        "--certificate-oidc-issuer", "https://token.actions.githubusercontent.com",
    ], check=True, stdout=subprocess.DEVNULL, timeout=120)
    subprocess.run([
        "gh", "attestation", "verify", f"oci://{immutable}",
        "--repo", repository, "--signer-workflow", workflow,
        "--source-ref", f"refs/tags/{tag}", "--source-digest", revision,
        "--deny-self-hosted-runners",
    ], check=True, stdout=subprocess.DEVNULL, timeout=120)
    return {"provider": provider, "version": version, "image": immutable,
            "revision": revision, "platforms": platforms}


if __name__ == "__main__":
    print(json.dumps({"schema": 1, "images": [verify(p) for p in ("ring", "blink", "ezviz")]}, indent=2))
