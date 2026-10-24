# Changelog

## 0.14.0

- Cameras that send RTP (models other than the CP4, or any camera with video
  encryption on) now play at their real frame rate instead of an assumed
  25 fps, and keep their sound: the camera's AAC audio is carried into Home
  Assistant instead of being dropped.
- Cameras that send RTP without encryption (reported for the CS-C8c) now play
  instead of producing no picture.
- Battery cameras: a live session that stops receiving video is closed after
  the upstream timeout instead of staying open, and the camera is left alone
  for 30 seconds before the next session, so a viewer that reconnects at once
  does not wake it straight away. Live view reports "camera offline" meanwhile.

## 0.13.2

- Fix: since 0.11.0 a fresh camera snapshot failed with an internal error
  whenever EZVIZ handed out its snapshot link over plain HTTP. Plain HTTP is
  now accepted only for EZVIZ's own domains (`ezvizlife.com`, `ezvizru.com`,
  `ezviz.com`); every other host still requires HTTPS, and no EZVIZ login or
  session data is ever sent with these downloads.
- Diagnostics: failed requests now log a short reason (scheme and host only,
  never the full link) instead of just "upstream".

## 0.13.1

- Diagnostics: the app log now also records which camera status fields change
  (for example when a door viewer is mounted on its door base), to find a
  reliable "mounted" signal. Secret, identifying and volatile fields such as
  addresses, network names, times and signal strength are never logged, and no
  extra EZVIZ request is made.

## 0.13.0

- Battery cameras now report whether they are charging and whether they run
  on external power or on battery. The Vistoda integration 0.43.0 shows this
  as a "Charging" sensor next to the battery level.

## 0.12.0

- Diagnostics for the battery power state: the app log now records which
  power and charging fields EZVIZ reports for each camera (field names once,
  and the values of power-related fields when they change), to prepare a
  "charging" entity. No secret is logged and no extra EZVIZ request is made.

## 0.11.0

- Short EZVIZ cloud errors no longer make controls and arming unavailable:
  the last known value is kept for up to ten minutes.
- An EZVIZ session revoked by EZVIZ now asks you to sign in again in Home
  Assistant instead of failing silently, and the app no longer restarts in a
  loop when it cannot renew the session at startup.
- Snapshots are downloaded only over HTTPS.
- Security updates for the TLS libraries.

## 0.10.1

- Stopping the app from Home Assistant now shows it as stopped instead of
  failed. A shutdown that fails, or has to be forced, is still reported as
  an error.

## 0.10.0

- Camera settings, arming (per camera and the account's home/away/sleep
  mode), detection, sensitivity and PTZ now use Vistoda's own EZVIZ login:
  Home Assistant's built-in EZVIZ integration is no longer required.

## 0.9.1

- Never ask the EZVIZ cloud for the device verification code just to show
  the encryption state: that request makes EZVIZ email or text the owner a
  security code. It is now used only when strictly needed to decrypt video
  or pictures, at most once a day per camera. Entering the code printed on
  the camera label avoids it entirely.

## 0.9.0

- Live view of cameras with video encryption on: Vistoda reads the device
  verification code from the EZVIZ account; an optional per-camera
  verification code can be entered if needed.
- Show the microSD card state and the list of recordings stored on it
  (playback is not available yet).

## 0.8.0

- Read EZVIZ alarm events (motion, person, vehicle, doorbell, sound and
  more) with their pictures, so Home Assistant can notify them and show an
  event timeline without the official EZVIZ app. Read-only: messages are
  never marked as read or deleted.

## 0.7.3

- Hold every maintained source file to the 250-line Vistoda budget. Code is
  moved, not rewritten: camera, snapshot, live and recording behavior is unchanged.

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
