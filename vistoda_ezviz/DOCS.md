# Vistoda EZVIZ

La procedura completa è nella [guida italiana](https://github.com/luigibarretta/vistoda-addons/blob/main/GETTING_STARTED.it.md);
the complete procedure is in the [English setup guide](https://github.com/luigibarretta/vistoda-addons/blob/main/GETTING_STARTED.md).

Enter the camera serial printed in the EZVIZ app/device information and choose
a short Home Assistant alias. Start the app, then complete the automatically
discovered **Vistoda EZVIZ** account flow.

For more than one camera, leave the legacy serial empty and populate **Multiple
cameras**. Every item needs a unique alias and a unique serial/channel pair:

```yaml
cameras:
  - alias: front-door
    serial: DEVICE123
    channel: 1
    substream: false
  - alias: garage
    serial: DEVICE456
    channel: 1
    substream: true
```

Home Assistant then offers each camera as a separate, physically bound entry;
the Vistoda page-view switches between them without requesting snapshots.

The serial is a device identifier, not the six-character verification code.
The EZVIZ account password and any MFA code are requested by Home Assistant and
are never stored in the Vistoda config entry. The rotating cloud session stays
inside the app data volume.

Port 8765 remains private. Use the standalone Vistoda EZVIZ container when an
advanced SceneTrove deployment needs direct access to the media bridge.

Vistoda can record finite 15, 30 or 60 second clips from the live stream. This
standalone archive is separate from SceneTrove and the camera microSD card;
paginated playback, download, confirmed deletion and verified NFS backup are
managed through Home Assistant. Playback is remuxed to browser-compatible MP4
on demand and does not create a duplicate recording.

## Device verification code

Leave **Device verification code** empty in normal use: Vistoda reads the key
from the EZVIZ account. Enter the six-letter code printed on the camera label
only if the live view of an encrypted camera fails; it stays private and never
enters the camera list or the logs. With **Multiple cameras**, set it per item.

## Event history

The app keeps the newest events of each camera with their pictures: 200 by
default, 50 to 2000 with **Events kept per camera**. Pictures of all cameras
share **Maximum picture storage** (256 MiB by default, 64 to 2048); when it is
full the oldest pictures go, while their events stay without a picture.

Events and pictures live on Home Assistant's own disk and are included in its
backups, so high values grow both. Lowering the number of events deletes the
oldest ones at the next start. For a long history use the Vistoda event archive
on network storage, or SceneTrove.
