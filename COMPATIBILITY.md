# Vistoda release compatibility

This page defines the tested release set for the non-Apple Vistoda components.
Install only the providers you use and update provider apps before their Home
Assistant integrations.

## Tested release set

| Component | Version | Required for |
| --- | --- | --- |
| Vistoda Home Assistant integration | `0.26.0` | Ring, EZVIZ and the unified panel |
| Vistoda Blink Home Assistant integration | `0.13.3` | Blink only |
| Vistoda Ring app | `0.13.0` | Ring Intercom |
| Vistoda Blink app | `0.13.3` | Blink cameras |
| Vistoda EZVIZ app | `0.7.0` | EZVIZ cameras |
| Vistoda Apps catalog | `0.4.0` | HAOS/Supervised app installation |

The minimum Home Assistant release is `2026.8.0`. CI also tests `2026.9.1`.
Provider images are published for `amd64` and `aarch64`.

When upgrading this release set, install Vistoda EZVIZ `0.7.0` before Vistoda
`0.26.0`. The integration rejects an older EZVIZ app instead of using an
unverified camera binding.

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
| Blink | Multiple cameras, stored/manual snapshots, Walnut live, supported settings and zones, cloud/USB/local archives and NFS backup | Cayuga/WebRTC microphone and full-duplex talk are disabled by current provider policy. Settings vary by model. |
| EZVIZ | Multiple cameras, stored/manual snapshots, compatible live streams, local recordings and NFS backup | Talk and direct microSD access are unavailable. Encrypted stream compatibility is not universal. |
| Apple | Separate project | Excluded from this release set and its readiness claims. |

Vistoda hides or disables operations that a provider or device does not report
as supported. The official vendor apps remain necessary for account recovery
and unsupported administration.

Start with the [installation guide](GETTING_STARTED.md). Maintenance and recovery
are covered by [OPERATIONS.md](OPERATIONS.md).
