"""The catalog refuses app sources that call guarded vendor endpoints unsafely."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_app_sources", ROOT / "scripts/verify-app-sources.py")
guards = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guards)
RULES = json.loads((ROOT / "contracts/source-guards.json").read_text(encoding="utf-8"))["apps"]


def tree(files: dict[str, str]) -> tempfile.TemporaryDirectory:
    directory = tempfile.TemporaryDirectory()
    for name, text in files.items():
        path = Path(directory.name) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return directory


GUARDED = """
impl T {
    async fn camera_key(&self) { self.cloud_keys.fetch(serial, now, || self.raw()).await }
    async fn raw(&self) { let url = format!("https://{}/api/device/query/encryptkey", api); }
}
"""


class SourceGuardTests(unittest.TestCase):
    def check(self, files):
        with tree(files) as root:
            return guards.check_tree("vistoda_ezviz", Path(root), RULES["vistoda_ezviz"])

    def test_0_9_0_shape_is_rejected(self):
        # 0.9.0 built the encryptkey request in the shared client, reachable from polls.
        errors = self.check({"src/transport/client.rs": 'let u = format!("https://{}/api/device/query/encryptkey", a);'})
        self.assertTrue(any("outside its guard" in error for error in errors))

    def test_guarded_module_passes(self):
        self.assertEqual(self.check({"src/transport/cloud_key.rs": GUARDED}), [])

    def test_allowed_file_without_guard_is_rejected(self):
        errors = self.check({"src/transport/cloud_key.rs": 'format!("https://{}/api/device/query/encryptkey", a)'})
        self.assertTrue(any("without guard marker" in error for error in errors))

    def test_comments_and_tests_do_not_count(self):
        files = {
            "src/device/key.rs": "//! the value returned by `/api/device/query/encryptkey`\n",
            "src/device/tests.rs": 'const URL: &str = "/api/device/query/encryptkey";\n',
            "tests/api.rs": 'const URL: &str = "encryptedInfo/risk";\n',
        }
        self.assertEqual(self.check(files), [])

    def test_security_toggles_are_never_allowed(self):
        errors = self.check({"src/transport/device.rs": 'let p = "v3/devices/encryptedInfo/risk";'})
        self.assertTrue(any("encryptedInfo/risk" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
