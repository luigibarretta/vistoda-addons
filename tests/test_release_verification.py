"""Fail-closed release tests with deterministic public-registry fixtures."""

import hashlib
import importlib.util
import io
import json
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch


def module(name):
    path = Path(__file__).parents[1] / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


VERIFY = module("verify-images")
PUBLISH = module("publish-release")


class Response(io.BytesIO):
    def __init__(self, value, digest=None):
        super().__init__(json.dumps(value).encode())
        self.headers = {"Docker-Content-Digest": digest or "sha256:" + hashlib.sha256(self.getvalue()).hexdigest()}


class ReleaseTests(unittest.TestCase):
    def registry(self, missing_arm=False, wrong_digest=False):
        child = {"schemaVersion": 2, "config": {"digest": "sha256:" + "a" * 64}}
        raw = json.dumps(child).encode()
        child_digest = "sha256:" + hashlib.sha256(raw).hexdigest()
        manifest = {"manifests": [
            {"platform": {"os": "linux", "architecture": arch}, "digest": child_digest}
            for arch in (["amd64"] if missing_arm else ["amd64", "arm64"])
        ]}

        def get(url, headers=None):
            if "/git/ref/tags/" in url:
                return Response({"object": {"type": "commit", "sha": "b" * 40}})
            if "/token?" in url:
                return Response({"token": "anonymous-public-pull"})
            if child_digest in url:
                return Response(child)
            return Response(manifest, "sha256:" + "0" * 64 if wrong_digest else None)
        return get

    def test_verified_manifest_requires_exact_signature_and_source(self):
        with patch.object(VERIFY, "get", side_effect=self.registry()), patch.object(VERIFY.subprocess, "run") as run:
            result = VERIFY.verify("ring")
        self.assertEqual(set(result["platforms"]), {"linux/amd64", "linux/arm64"})
        self.assertEqual(result["revision"], "b" * 40)
        signature, provenance = [call.args[0] for call in run.call_args_list]
        self.assertIn("--certificate-identity", signature)
        identity = signature[signature.index("--certificate-identity") + 1]
        self.assertEqual(
            identity,
            "https://github.com/luigibarretta/vistoda-ring/"
            ".github/workflows/publish-addon.yaml@refs/tags/"
            f"v{result['version']}",
        )
        self.assertEqual(
            provenance[provenance.index("--signer-workflow") + 1],
            "luigibarretta/vistoda-ring/.github/workflows/publish-addon.yaml",
        )
        self.assertEqual(provenance[provenance.index("--source-digest") + 1], "b" * 40)
        self.assertIn("--deny-self-hosted-runners", provenance)

    def test_missing_architecture_blocks_before_signature(self):
        with patch.object(VERIFY, "get", side_effect=self.registry(missing_arm=True)), patch.object(VERIFY.subprocess, "run") as run:
            with self.assertRaisesRegex(SystemExit, "manifest pair"):
                VERIFY.verify("ring")
        run.assert_not_called()

    def test_bad_digest_blocks_before_signature(self):
        with patch.object(VERIFY, "get", side_effect=self.registry(wrong_digest=True)), patch.object(VERIFY.subprocess, "run") as run:
            with self.assertRaisesRegex(SystemExit, "manifest bytes"):
                VERIFY.verify("ring")
        run.assert_not_called()

    def test_failed_signature_blocks_catalog(self):
        with patch.object(VERIFY, "get", side_effect=self.registry()), patch.object(VERIFY.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "cosign")):
            with self.assertRaises(subprocess.CalledProcessError):
                VERIFY.verify("ring")

    def test_network_error_is_not_an_absent_artifact(self):
        with patch.object(VERIFY, "get", side_effect=TimeoutError()):
            with self.assertRaises(TimeoutError):
                VERIFY.verify("ring")

    def test_catalog_tag_must_equal_checkout_before_api(self):
        version = (PUBLISH.ROOT / "VERSION").read_text().strip()
        with patch("sys.argv", ["publish-release.py", "--tag", f"v{version}", "--dry-run"]), patch.object(PUBLISH.subprocess, "check_output", side_effect=["a" * 40, "b" * 40]):
            with self.assertRaisesRegex(SystemExit, "checked-out commit"):
                PUBLISH.main()

    def test_dirty_catalog_cannot_publish(self):
        version = (PUBLISH.ROOT / "VERSION").read_text().strip()
        with patch("sys.argv", ["publish-release.py", "--tag", f"v{version}", "--dry-run"]), patch.object(PUBLISH.subprocess, "check_output", side_effect=["a" * 40, "a" * 40, " M config.yaml"]):
            with self.assertRaisesRegex(SystemExit, "clean tracked"):
                PUBLISH.main()
