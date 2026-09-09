# Changelog

## 0.10.0

- Adds server-paginated Blink local and Sync Module USB inventories.
- Supports signed playback, download and Home Assistant-managed NFS backup of
  provider-owned USB clips without modifying the source support.

## 0.9.2

- Install the process-level Ring crypto provider before the REST and native
  WebSocket TLS clients coexist, preventing a signaling probe process abort.

## 0.9.1

- Trust the native `active` and `memory_full` Sync Module states even when
  Blink's compatibility `enabled` flag lags behind.
- Parse both numeric and string private Ring device IDs.
- Build signaling identity from the shared `ringUserId` and return bounded,
  secret-free WebSocket failure diagnostics without starting media.

## 0.9.0

- Adds read-only Sync Module USB status, clip inventory and authenticated
  downloads without delete, eject, format or mount controls.
- Adopts the current Blink v4 homescreen and its audio capability fields.
- Adds a signaling-only WebRTC 4.1 authentication probe; full-duplex media
  remains gated until SDP, ICE, uplink and recovery pass a live canary.

## 0.8.0

- Records finite 15–60 second standalone clips from the shared live stream.
- Exposes a bounded, checksummed per-camera archive for Vistoda download,
  deletion and Home Assistant-managed NFS backup.
- Replaces the failing Blink cloud record action that produced false motion
  notifications.

## 0.7.0

- Adds revision-checked native activity and privacy zone controls for verified
  v1 cameras, with provider read-back and automatic rollback.
- Exposes the Blink speaker-volume scale from 1 to 8 on supported Mini cameras.
- Rejects unsupported Owl/Mini v2 zone schemas instead of showing fabricated
  defaults.

## 0.6.0

- Adds model-aware camera name, IR, status LED, rotation, Photo Capture and
  temperature-alert controls with provider read-back verification.
- Preserves stable camera aliases across provider-side renames.
- Corrects Mini clip and retrigger fields and reports unverified controls as
  read-only.
- Discovers the camera-specific activity-zone schema without exposing mask
  values.

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
