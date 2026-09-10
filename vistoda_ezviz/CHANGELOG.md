# Changelog

## 0.5.0

- Publishes bounded private-spool path and capacity metadata for Vistoda.
- Supports the Vistoda custom-list and selected-deletion archive experience.
- Keeps provider snapshot refresh behind an explicit panel action.

## 0.4.0

- Adds bounded server-side pagination to the standalone recording archive.
- Adds on-demand fragmented-MP4 playback for browser clients while preserving
  the canonical MPEG-PS recording artifact.

## 0.3.5

- Exposes the bounded standalone recording inventory to Vistoda.
- Keeps Vistoda recordings independent from SceneTrove and ready for verified
  Home Assistant-managed NFS backup.

## 0.3.4

- Adopt the shared audited Vistoda app bootstrap for Supervisor discovery,
  fail-closed token storage and bounded readiness.
- Preserve private permissions on restored EZVIZ session state at startup.

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
