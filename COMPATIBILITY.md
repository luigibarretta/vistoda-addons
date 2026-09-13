# Vistoda release compatibility

This page defines the tested release set for the non-Apple Vistoda components.
Install only the providers you use and update provider apps before their Home
Assistant integrations.

## Tested release set

| Component | Version | Required for |
| --- | --- | --- |
| Vistoda Home Assistant integration | `0.31.5` | Ring, Blink, EZVIZ and the unified panel |
| Vistoda Blink Home Assistant integration | `0.18.0` | Blink only |
| Vistoda Ring app | `0.14.1` | Ring Intercom and experimental cameras |
| Vistoda Blink app | `0.18.0` | Blink cameras |
| Vistoda EZVIZ app | `0.7.2` | EZVIZ cameras |
| Vistoda Apps catalog | `0.4.16` | HAOS/Supervised app installation |

The minimum Home Assistant release is `2026.8.0`. CI also tests `2026.9.1`.
Provider images are published for `amd64` and `aarch64`.

Update provider apps before their matching Home Assistant integrations. Vistoda
refuses incompatible versions rather than using an unverified device binding.

## Required components

| Provider | HACS integration | Home Assistant app |
| --- | --- | --- |
| Ring | Vistoda | Vistoda Ring |
| Blink | Vistoda and Vistoda Blink | Vistoda Blink |
| EZVIZ | Vistoda | Vistoda EZVIZ |

## Supported boundary

| Provider | Released functions | Known boundary |
| --- | --- | --- |
| Ring | Multiple intercom selection, status, controls, event history, full-duplex browser audio and local call recordings | Uses experimental consumer APIs not supported by Ring for third parties. Provider changes can interrupt service. |
| Blink | Multiple cameras, stored/manual snapshots, conditional Walnut talk/listen, supported settings and zones, versioned settings backup, cloud/USB/local archives and NFS backup | Simultaneous duplex depends on the provider offer and browser/camera AEC; verify sound and echo on each model. Cayuga remains policy-gated. Settings vary by model. |
| EZVIZ | Multiple cameras, stored/manual snapshots, compatible live streams, local recordings and NFS backup | Talk and direct microSD access are unavailable. Encrypted stream compatibility is not universal. |
| Apple | Separate project | Excluded from this release set and its readiness claims. |

Vistoda hides or disables operations that a provider or device does not report
as supported. The official vendor apps remain necessary for account recovery
and unsupported administration.

Start with the [installation guide](GETTING_STARTED.md). Maintenance and recovery
are covered by [OPERATIONS.md](OPERATIONS.md).
