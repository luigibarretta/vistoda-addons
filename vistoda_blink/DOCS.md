# Vistoda Blink

Install and start the app, then complete the automatically discovered
**Vistoda Blink** flow under Settings → Devices & services. Enter the email and
password used by the Blink app and, when requested, the newest verification
code sent by Blink.

The official Blink integration is not required. Vistoda owns one independent
rotating session and exposes native Home Assistant entities and services.

The Vistoda Blink panel opens the camera through browser-native WebRTC. Camera
audio and the local microphone have separate controls, start disabled and are
released when the live closes or the panel changes camera. Only one Vistoda
session may own a camera or browser microphone at a time.

Vistoda reads the real provider state for each supported camera setting. On
verified v1 cameras it also manages the native 20×15 activity grid and up to
two privacy zones with revision checks, provider read-back and rollback. Zone
controls stay unavailable on Owl/Mini v2 devices while Blink rejects the
enrolled route; no empty or guessed configuration is displayed.

Vistoda can also record finite 15, 30 or 60 second clips from the shared live
stream. Its standalone archive is distinct from Blink cloud clips and Sync
Module USB storage. Download, confirmed deletion and verified NFS backup are
managed from the Vistoda camera page through Home Assistant. The Sync Module
USB archive has a separate paginated list with playback, download and
checksum-verified NFS copy. Administrators may delete selected exact clips or
format compatible media only after the explicit destructive confirmation;
Vistoda does not expose eject or mount operations.

The app API remains private to the Supervisor network. Do not publish port
8099 unless an advanced external consumer has a separately reviewed need.
