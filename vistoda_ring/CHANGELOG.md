# Changelog

## 0.11.0

- Add the native encrypted FCM listener for Intercom ding and unlock events.
- Expose a private cursor/long-poll contract plus aggregate push health metrics.
- Reset consumers safely across app/Core restarts without replaying queued calls.
- Keep the official Home Assistant Ring event source as a deduplicated canary fallback.
- Sign and attest the immutable multi-architecture image digest.

## 0.10.0

- Explain every recording destination and its exact Home Assistant OS path.
- Add fail-closed NFS/Samba storage through HAOS-managed Media or Share mounts.
- Distinguish local `/share` from network storage in configuration and docs.

## 0.9.1

- Keep the 0.9.0 selectable recording archive contract.
- Simplify the relay session lifecycle without changing its wire behavior.

## 0.9.0

- Add private, app-config, media and share destinations for Ring recordings.
- Migrate generated archive files with copy verification and fail-closed conflicts.
- Publish the effective display path to the authenticated Vistoda panel.

## 0.8.3

- Add privacy-safe request correlation and classified HTTP failure logs.

## 0.8.2

- Restore private permissions on the Ring session before the app starts.

## 0.8.1

- Preserve writable `/data` ownership across Supervisor backup restores.

## 0.8.0

- Add private Supervisor discovery and native Home Assistant enrollment.
- Package full-duplex audio, controls and bounded local recordings as an app.
