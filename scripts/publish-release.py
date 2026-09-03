#!/usr/bin/env python3
"""Publish an existing immutable catalog tag through GitHub or Gitea."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parents[1]


def request(url: str, token: str, method: str = "GET", payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "vistoda-addons-release",
    }
    return urllib.request.urlopen(
        urllib.request.Request(url, data=data, headers=headers, method=method),
        timeout=30,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise SystemExit("VERSION must be SemVer")
    if args.tag != f"v{version}":
        raise SystemExit(f"release tag {args.tag!r} does not match VERSION {version}")

    subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={ROOT}",
            "rev-parse",
            "--verify",
            f"refs/tags/{args.tag}^{{commit}}",
        ],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )

    repository = os.environ.get("GITHUB_REPOSITORY", "")
    api_url = os.environ.get("GITHUB_API_URL", "").rstrip("/")
    if repository.count("/") != 1 or not api_url.startswith(("http://", "https://")):
        raise SystemExit("GITHUB_REPOSITORY and GITHUB_API_URL are required")
    if args.dry_run:
        print(f"Release contract passed for {repository} {args.tag}")
        return

    token = os.environ.get("FORGE_TOKEN", "")
    if not token:
        raise SystemExit("FORGE_TOKEN is required")
    owner, repo = (urllib.parse.quote(part, safe="") for part in repository.split("/"))
    encoded_tag = urllib.parse.quote(args.tag, safe="")
    base = f"{api_url}/repos/{owner}/{repo}/releases"
    try:
        with request(f"{base}/tags/{encoded_tag}", token) as response:
            existing = json.load(response)
        if existing.get("tag_name") != args.tag or existing.get("draft"):
            raise SystemExit("existing release metadata does not match the immutable tag")
        print(f"Release {args.tag} already exists and is published")
        return
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise

    payload = {
        "tag_name": args.tag,
        "name": args.tag,
        "body": f"Vistoda Apps catalog {args.tag}",
        "draft": False,
        "prerelease": False,
    }
    if api_url == "https://api.github.com":
        payload["generate_release_notes"] = True
    with request(base, token, method="POST", payload=payload) as response:
        if response.status != 201:
            raise SystemExit(f"release API returned HTTP {response.status}")
    print(f"Published immutable release {args.tag}")


if __name__ == "__main__":
    main()
