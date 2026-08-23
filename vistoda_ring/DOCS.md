# Vistoda Ring

Choose a short Home Assistant alias, install and start the app, then open the
automatically discovered **Vistoda Ring** flow. Enter the Ring account email and
password. If Ring sends an SMS, enter only the newest six-digit code.

The app stores the rotating Ring session and local call archive in its private
persistent data volume. Home Assistant receives only a private workload token
through Supervisor discovery. The token, bridge URL and port are not user
configuration fields.

Port 8775 is private by default. Use the standalone Vistoda Ring container for
advanced SceneTrove or native-client deployments that require a remote bridge.

