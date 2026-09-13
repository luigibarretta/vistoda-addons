# Get started with Vistoda

This is the recommended installation path for Home Assistant OS and Home
Assistant Supervised. It installs only private provider apps; it does not expose
camera or intercom services to the Internet.

Vistoda brings supported Ring Intercom, Blink and EZVIZ functions into one Home
Assistant panel. It is not a complete replacement for every vendor app. Keep the
official apps available for account recovery and the unsupported functions listed
in the [compatibility matrix](COMPATIBILITY.md).

## Before you start

You need:

- Home Assistant 2026.8.0 or newer on `amd64` or `aarch64`;
- HACS and access to the Home Assistant app store;
- the account credentials and newest MFA code for each provider;
- the serial number of every EZVIZ camera you want to add;
- a current Home Assistant backup.

Home Assistant Container and Core do not have the app store. Use the standalone
provider containers only if you are comfortable managing private URLs, tokens,
storage and network access yourself.

## 1. Install the Home Assistant integrations

1. Install [Vistoda through HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-home-assistant&category=integration).
2. If you use Blink, also install [Vistoda Blink through HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-blink&category=integration).
3. Restart Home Assistant once after the HACS installations.

Ring and EZVIZ use the main Vistoda integration. Blink also needs its small
provider-specific adapter so existing Blink entities and services remain stable.

## 2. Add the Vistoda app repository

Use [Add Vistoda Apps](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fluigibarretta%2Fvistoda-addons),
or add this URL under **Settings → Apps → App store → Repositories**:

`https://github.com/luigibarretta/vistoda-addons`

Install only the provider apps you need. Do not publish their API ports.

## 3. Configure a provider

### Ring Intercom

1. Install **Vistoda Ring**.
2. Leave **Intercoms** empty for normal setup, even when the account has several
   entrances. The default alias can remain unchanged.
3. Start the app.
4. Open **Settings → Devices & services** and complete the discovered Vistoda
   Ring flow. Enter the Ring account credentials and the newest SMS code.
5. Select the entrance by its real device name and location. Home Assistant
   offers other intercoms as additional setup flows.

Expected result: every selected intercom has its own Vistoda entry, controls,
history and recording archive. Selecting one entrance in `/vistoda/ring` scopes
all actions to that physical device.

Ring uses experimental consumer APIs that Ring does not support for third-party
integrations. The Vistoda panel confirms an opening; authorized Home Assistant
buttons and automations can call it without an interactive modal. No path retries
the physical action automatically. Outbound TCP port 5228 to
`mtalk.google.com` is required for native event push.

### Blink

1. Confirm that both **Vistoda** and **Vistoda Blink** are installed through HACS.
2. Install and start the **Vistoda Blink** app. It has no normal user options.
3. Complete the discovered Vistoda Blink flow with the Blink account credentials
   and newest verification code.

Expected result: the Blink network and its cameras appear as Home Assistant
devices. `/vistoda/blink` shows the latest stored snapshots without waking every
battery camera. Request a new snapshot or live view explicitly.

Walnut/IMMI live and conditional talk/listen are supported. Microphone use needs
HTTPS and an explicit browser permission. Simultaneous listening while talking
depends on the provider offer and browser/camera echo cancellation; test it on
your model. Cayuga/WebRTC remains disabled by the enrolled provider policy.

The Blink system card can keep multiple named, all-camera settings backups.
Restore uses provider serial/ID matching and revision checks. Sync Module Wi-Fi
migration, safe eject and removal are shown as unavailable; use the official app
for those recovery-sensitive operations.

### EZVIZ

1. Install **Vistoda EZVIZ**.
2. Before starting it, enter a short alias and the camera serial. A standalone
   camera normally uses channel `1`; enable substream only when wanted.
3. For several cameras, leave the legacy serial empty and fill **Multiple
   cameras** with a unique alias and serial/channel pair for each camera.
4. Start the app and complete every discovered Vistoda EZVIZ flow with the
   account credentials and MFA challenge.

Expected result: every configured serial/channel pair has a separate Home
Assistant entry. `/vistoda/ezviz` displays its most recently stored snapshot and
does not capture a new one until you request it.

Talk and direct microSD browsing are not available without a usable EZVIZ Open
Platform path. Stream compatibility varies by camera and encryption profile.

## 4. Verify the installation

Open `/vistoda` from the Home Assistant sidebar and check that:

- each installed provider reports available;
- every expected camera or intercom can be selected;
- stored snapshots and status values load;
- the provider app log has no repeating authentication or restart error.

Then run one deliberate media test on a powered camera when possible. Do not use
door opening, USB formatting, file deletion or battery-camera live view as an
installation test.

## Recordings and network backup

Each app has its own private data volume. `/data/recordings` in Ring, Blink and
EZVIZ therefore refers to three different physical app-owned locations. Vistoda
shows the effective path and exposes supported playback, download and deletion
through Home Assistant.

To configure NFS or SMB backup:

1. Open **Settings → System → Storage**.
2. Add writable network storage with usage **Media**.
3. Enter that storage name, not its server address or `/media/...` path, in the
   Blink or EZVIZ Vistoda integration options.

The integration verifies that the destination is a real writable network mount
with at least 512 MiB free. It never falls back silently to the Home Assistant
disk. Ring can additionally use a HAOS-managed network mount as its primary call
archive; its app documentation explains the storage choices.

## Common problems

| Symptom | Check |
| --- | --- |
| No discovered integration | Start the provider app, inspect its Log tab, confirm the HACS integration is installed, then restart the app once. |
| Login or MFA rejected | Start a fresh sign-in and use only the newest code. Stop retrying if the provider reports throttling. |
| One device is missing | Check the Ring selection or the EZVIZ serial/channel pair; never guess a physical ID. |
| Live view fails | Confirm the model is supported, no other session owns the camera and the app stays running. Test a powered camera first. |
| Backup is unavailable | Confirm the exact HA network-storage name, Media usage, writable mount and free-space requirement. |
| A feature is absent | Check the capability row in Vistoda and the [compatibility matrix](COMPATIBILITY.md); unsupported controls are intentionally hidden. |

For account reconnection, update order, rollback, backup restore and uninstall,
continue with the [operations guide](OPERATIONS.md).
