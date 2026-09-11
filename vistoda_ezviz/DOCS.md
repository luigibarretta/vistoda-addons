# Vistoda EZVIZ

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

## Più telecamere

Compila **Più telecamere** con alias distinti e coppie seriale/canale distinte.
Home Assistant propone una entry per camera; Vistoda le mostra nella page-view
senza generare snapshot all'apertura. I campi singoli restano compatibili con
le installazioni esistenti.
