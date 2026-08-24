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
- `share`: `/share/vistoda-ring`, convenient for Samba-managed exports.

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
