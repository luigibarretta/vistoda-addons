# Changelog

## 0.15.1

- Align the AAC ADTS buffer-fullness field with native Walnut packets without
  changing audio payloads, frame lengths or counters. Offline decoded audio is
  identical; this is compatibility hardening, not proof of speaker audibility.
- Use Vistoda for Home Assistant 0.28.0 for conditional microphone controls.
  Listening pauses while talking; simultaneous full duplex is not claimed.

## 0.15.0

- Add an authenticated, exclusive Walnut microphone channel alongside the
  existing Home Assistant video subscriber; no replacement video player.
- Encode explicit PCM capture to the offered AAC format with bounded queues,
  freshness deadlines and immediate revocation on stop or disconnect.
- Bundle the minimal LGPL FFmpeg executable and its corresponding source.
- This is the microphone transport release, not a full-duplex certification.
  Camera speaker output requires acoustic validation; the observed Mini offer
  requires listening to pause while talking. Camera settings and media are unchanged.

## 0.14.1

- Close the IMMI keepalive writer together with the live reader on timeout,
  protocol failure and loss of the last viewer.
- Observe the first audio-format offer during an explicitly requested live,
  without transmitting audio or enabling the microphone.
- Preserve verified TLS, existing playback, recordings and camera settings.
  Walnut full-duplex remains under validation, not advertised as available.

## 0.14.0

- Verify IMMI TLS with authenticated Blink certificate identities or standard
  public trust; reject unknown certificates without an insecure fallback.
- Read and edit native per-camera temperature alerts and thresholds, preserving
  calibration and verifying upstream state. Explicit paired setup for unset limits.
- Requires Vistoda Home Assistant 0.27.0 for the temperature editor in HA units.
  Native Blink push delivery still requires the Blink app's notification permission.

## 0.13.3

- Preserves stable camera aliases across provider inventory reorder and temporary
  removal, without allowing a new camera to inherit a reserved identity.
- Publishes each alarm panel's Blink network identity so multi-Sync-Module
  controls remain scoped to the selected camera.

## 0.13.2

- Restarts a consumed OTP challenge from credentials with clear EN/IT guidance.
- Adopts the hardened shared provider lifecycle, immutable release and license gates.

## 0.13.1

- Publishes Blink Android 59.1's typed preferred live transport for each camera.
- Selects Walnut before WebRTC signaling while the official Cayuga feature is
  still `InProgress`, avoiding unsupported `SESSION_SETUP_FAILED` attempts.
- Keeps the bounded Cayuga implementation gated for a future official rollout
  without advertising unverified full-duplex audio.

## 0.13.0

- Matches Blink Android's one-way Cayuga-to-Walnut fallback for cameras without
  a shared Ring device identity and provider legacy-device close code 38.
- Keeps unrelated WebRTC failures fail-closed while allowing the user to open
  the existing compatible IMMI live explicitly.
- Releases the exclusive WebRTC publisher before Home Assistant starts the
  compatible live path and never exposes provider credentials or close text.

## 0.12.5

- Resolves Blink WebRTC signaling with the canonical shared Ring identity
  returned by the provider instead of reusing Blink's unrelated account ID.
- Reconciles an encrypted stored identity when the provider rotates or corrects
  it, while keeping identifiers and credentials out of logs and diagnostics.

## 0.12.4

- Relays the provider's terminal WebRTC event before closing the local socket,
  preserving its safe numeric reason code for diagnostics and user feedback.
- Records the provider close code in privacy-safe lifecycle telemetry without
  logging device IDs, media negotiation payloads or credentials.

## 0.12.3

- Preserves provider heartbeat updates even when they do not produce a browser
  event, preventing healthy WebRTC sessions from expiring after two pings.
- Accepts the official pre-session close and microphone-override shapes while
  continuing to reject mismatched session identities.
- Adds value-free signaling lifecycle diagnostics without logging private
  camera IDs, SDP, ICE candidates or credentials.

## 0.12.1

- Adds owner-bound browser WebRTC live sessions with independent speaker and
  microphone controls, native SDP/ICE signaling and provider heartbeats.
- Shares an exclusive per-camera lease with legacy live and recording paths,
  plus a Vistoda-wide browser microphone lock shared with Ring.
- Bounds negotiation, messages, candidates and teardown and fails closed on
  unsupported Blink content encryption or microphone override cooldowns.

## 0.11.0

- Adds exact current-manifest USB clip deletion for administrators.
- Shows the available-space percentage and compatible-media formatting behind
  a destructive warning and exact typed confirmation.
- Publishes the standalone archive's actual private add-on path to Vistoda.

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
