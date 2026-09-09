# Changelog

## 0.5.4

- Matches the current native Blink REST request-header contract.
- Restores model-aware v2 activity/privacy-zone capability probing.

## 0.5.3

- Adds safe model-feature probes and value-redacted v2 zone schema discovery.
- Preserves the private, authenticated provider boundary for all diagnostics.

## 0.5.2

- Adds an administrator-only, value-redacted camera capability inventory.
- Keeps camera-setting diagnostics bounded to provider field names and JSON types.

## 0.5.1

- Add a redacted, revision-checked camera-settings API for the controls Vistoda
  can verify safely against each Blink camera model.
- Keep unsupported camera models visible with read-only metadata instead of
  failing the entire settings view.
- Validate every write, serialize concurrent changes, verify the vendor
  read-back and attempt rollback when verification fails.

## 0.4.7

- Restore every Blink entity on Home Assistant 2026.9 by using the scoped
  device-registry parent ID contract introduced in Core 2026.8.

## 0.4.6

- Adopt the shared audited Vistoda app bootstrap for Supervisor discovery,
  fail-closed token storage, bounded readiness and engine lifecycle handling.

## 0.4.5

- Reuse the provider's validated bootstrap state so Home Assistant startup does not duplicate a slow cloud refresh.

## 0.4.4

- Report the provider camera inventory in health independently from active live-stream hubs.

## 0.4.3

- Classify the optional Sync Module endpoint and stop warning on its expected 404.
- Silence expected readiness-probe failures during bounded startup.
- Sign and attest the immutable multi-architecture image digest.

## 0.4.2

- Restore private permissions on sealed Blink credentials before app startup.

## 0.4.1

- Preserve writable `/data` ownership across Supervisor backup restores.

## 0.4.0

- Add private Supervisor discovery and standalone Rust provider packaging.
- Preserve existing sealed Blink sessions during managed-app migration.
