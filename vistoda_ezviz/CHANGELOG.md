# Changelog

## 0.3.3

- Silence expected readiness-probe failures during bounded startup.
- Sign and attest the immutable multi-architecture image digest.

## 0.3.2

- Restore private permissions on the EZVIZ session before the app starts.

## 0.3.1

- Preserve writable `/data` ownership across Supervisor backup restores.

## 0.3.0

- Add private Supervisor discovery and native Home Assistant enrollment.
- Publish the existing Rust media core as a signed multi-architecture app.
