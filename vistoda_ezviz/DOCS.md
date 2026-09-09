# Vistoda EZVIZ

Enter the camera serial printed in the EZVIZ app/device information and choose
a short Home Assistant alias. Start the app, then complete the automatically
discovered **Vistoda EZVIZ** account flow.

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
