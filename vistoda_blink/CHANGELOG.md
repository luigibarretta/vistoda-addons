# Changelog

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
