# Vistoda Ring

Choose a short Home Assistant alias, install and start the app, then open the
automatically discovered **Vistoda Ring** flow. Enter the Ring account email and
password. If Ring sends an SMS, enter only the newest six-digit code.

The rotating Ring session always stays in private app data. **Recording
storage** selects where local calls live:

- `private`: `/data/recordings`, private and included in app backups;
- `addon_config`: `/addon_configs/<app slug>/recordings`, user-visible and
  included in app backups;
- `media`: `/media/vistoda-ring`, visible to Home Assistant media tools;
- `share`: `/share/vistoda-ring`, visible to every app with the HAOS share mapped;
- `network`: a live NFS or Samba mount managed by HAOS, under either
  `/media/<name>` or `/share/<name>`.

`share` is local Home Assistant storage by default; it is not an NFS or Samba
share by itself. `addon_config` is the app-owned folder mounted as `/config`
inside Vistoda and exposed to users at
`/addon_configs/10aad50a_vistoda_ring`. It is useful for file access and is
included in the app backup.

For network storage, first use **Settings > System > Storage > Add network
storage** and choose NFS or Samba plus usage **Media** or **Share**. Then select
`network` here and set **HAOS network storage path** to the path HAOS reports,
for example `/media/ring-archive` or `/share/ring-archive`. Vistoda writes into
the `vistoda-ring` subfolder. It verifies that the named path is a live mount;
an absent mount fails closed instead of silently writing to local disk.

Changing the selection copies and verifies every generated archive file before
removing it from the previous destination. A conflict stops the app without
deleting the source. Media and share need an independent backup policy. The
Vistoda Ring panel shows the effective directory and each exact file path.

Home Assistant receives only a private workload token through Supervisor
discovery. The token, bridge URL and port are not user configuration fields.

Port 8775 is private by default. Use the standalone Vistoda Ring container for
advanced SceneTrove or native-client deployments that require a remote bridge.

Failed API requests are correlated by a server-generated `x-request-id` without
logging query values, credentials, device aliases or request bodies. Include
that response ID when reporting a reproducible app error.
