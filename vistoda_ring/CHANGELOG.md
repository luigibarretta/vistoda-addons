# Changelog

## 0.17.0

- When Ring does not send an intercom call in real time, the call is now
  reported from the Ring history within seconds instead of two minutes.
- Register for Ring notifications the way the official app does, and renew
  the registration after every Ring session renewal.

## 0.16.1

- Stopping the app from Home Assistant now shows it as stopped instead of
  failed. A shutdown that fails, or has to be forced, is still reported as
  an error.

## 0.16.0

- Show the Intercom unlock type (direct or Ring-to-Open) and the unlock
  duration, so a remote unlock that needs a ring first is explained.

## 0.15.0

- Ask Home Assistant to sign in again when Ring revokes the session, instead
  of failing silently.
- Detect Intercom calls that Ring recorded but never pushed, so Home
  Assistant can report missed calls and a push outage.

## 0.14.6

- Report who unlocked the entrance (Ring user name, handset, access code or
  delivery) so Vistoda Home Assistant 0.36.1 can name them in notifications.
- Extend the redacted activity diagnostic to find why Ring rejects the
  official "Unlock Alerts" settings for this client.

## 0.14.5

- Notify intercom unlocks made from the official Ring app: Ring records them
  only in its event history, which Vistoda now reads every 20 seconds.
- Remove the Ring "Unlock Alerts" opt-in from 0.14.4, which Ring rejects.
- Report history read failures in `vistoda_ring_unlock_history_errors_total`.

## 0.14.4

- Receive intercom unlocks made from the official Ring app: subscribe each
  Intercom to Ring "Unlock Alerts" and recognize the unlock push categories.
- Report the subscription in the `vistoda_ring_push_unlock_alerts_subscribed`
  metric.

## 0.14.3

- Add a read-only, redacted diagnostic of Ring activity feeds to find where
  Ring records intercom unlocks made from the official app.

## 0.14.2

- Keep the Ring push connection alive when one message cannot be decrypted,
  support the standard aes128gcm push encryption and log the reason for push
  failures plus a redacted shape of unrecognized messages for diagnosis.

## 0.14.1

- Recover Ring event notifications when a persisted FCM registration ends cleanly by rotating only the regenerable push registration.
- Preserve account enrollment, intercom bindings, recordings and all device configuration during recovery.

## 0.14.0

- Native camera inventory and bounded H264/PCMU browser signaling, separate from Intercom controls.
- Camera-only accounts can enroll with Vistoda Home Assistant 0.30.2; this version also fixes native camera WebSocket dispatch.
- Experimental: no Ring camera hardware was available for acceptance testing. Camera snapshots, recordings and settings are not included.
- Existing Intercom audio, history and unlock routes are unchanged.

## 0.13.1

- Include the MPL-covered ece source and recipient instructions in both images.
- Preserve existing intercom, audio, unlock, history and recording behavior.

## 0.13.0

- Adds exact multi-intercom configuration, discovery, selection and isolation.
- Binds door, audio, event history and recordings to one verified physical ID.
- Adds a safe authenticated intercom inventory and non-destructive archive migration.

## 0.12.0

- Add bounded, server-paginated Ring Intercom event history for calls, Live View
  sessions and entrance unlocks.
- Publish safe device, Location and city labels without exposing account or
  provider identifiers.
- Keep native full-duplex audio, controls and local recordings unchanged.

## 0.11.1

- Adopt the shared audited Vistoda app bootstrap for Supervisor discovery,
  fail-closed token storage and bounded readiness.
- Preserve private permissions on restored Ring session state at startup.

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
