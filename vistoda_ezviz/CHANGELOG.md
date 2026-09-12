# Changelog

## 0.7.2

- Allow backend recording pages of up to 100 clips for the shared Vistoda
  10/25/50/100 selector. Video files and archive storage are unchanged.

## 0.7.1

- Preserve the complete MIT license and attribution for cloud-cam-viewer adaptations.
- Include runtime package/license inventory and corresponding Debian sources.
- Preserve existing camera, snapshot, live and recording behavior.

## 0.7.0

- Configures up to 64 cameras in one app while preserving the legacy
  single-camera options and publishing one discovery device per alias.
- Exposes an authenticated serial/channel identity contract so Vistoda can pin
  every Home Assistant entry to the intended physical camera.
- Validates configuration with an executable legacy/multi-camera renderer and
  rejects duplicate aliases or physical sources before startup.

## 0.6.1

- Fixes startup when the optional substream setting is disabled.
- Validates both enabled and disabled boolean values before publishing discovery.

## 0.6.0

- Adds exact NVR channel, substream and bounded full VTM inventory selection.
- Supports compatible encrypted H.264/HEVC RTP as fail-closed MPEG-TS media.
- Preserves actual PS/TS recording types through playback, download and backup.

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
