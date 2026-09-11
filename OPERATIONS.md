# Install, recover and maintain Vistoda

## Before installation

Use Home Assistant OS or Supervised on amd64/aarch64 with the Supervisor app
store and HACS available. Home Assistant Container/Core requires standalone
provider containers and manual private URL/token setup; it has no app store.
Keep access to the vendor app and its newest MFA code. Check local free space
before enabling recordings, and create a Home Assistant backup first.

Choose only your providers: Ring for intercoms, Blink for cameras and clips,
EZVIZ for supported cameras. Install **Vistoda** in HACS; for Blink also install
**Vistoda Blink**. Restart Home Assistant once after both HACS installations.
Add this app-store repository, install the selected apps, configure them and
start them. Finish each discovered integration in Settings → Devices & services.
The app configuration is not the account sign-in page: credentials are entered
only in the discovered integration. The EZVIZ serial is required before start;
it is shown in device information and is different from the verification code.

## Discovery and sign-in recovery

If discovery does not appear, confirm the provider app is running and inspect
its Log tab. Confirm HACS integrations were installed and Home Assistant was
restarted. Reload the integration if present; otherwise restart the provider
once to publish discovery again. Keep API ports private.

For expired authorization, use the integration's account reconnection flow;
keep the entry to preserve devices, entity IDs and dashboards. After a rejected
Blink code, enter credentials again and use only the newest requested code.
Do not repeatedly request codes when the vendor reports throttling: wait for
the vendor's retry period. Confirm Ring device names and locations before
selecting the entrance; opening and event history must use that same entrance.

For support, collect the installed HA/integration/app versions and the request
ID from the failed action. Download diagnostics from the integration menu when
available. Review and redact logs and diagnostics before sharing them; never
attach account credentials, workload tokens, device serials or private media.

## Update and rollback

Read release notes for all selected providers and verify they list compatible
integration versions. Create a backup containing Home Assistant and the provider
apps, then download it to a different device. Record installed versions and
storage destinations. Update provider apps first, then the matching HACS
integrations and restart Home Assistant once. Confirm apps are running, cached
inventory is present and discovery/authorization work before enabling new features.

If an update fails, stop the affected provider and restore its pre-update app
backup and matching Home Assistant backup. Restoring both together avoids old
credentials/entity registries with a newer incompatible adapter. Do not rebuild
or overwrite an existing image tag to roll back. Provider sessions may need
reconnection after restore because the vendor can invalidate older rotating tokens.

## Backups and restore

App backups contain private `/data`, including provider credentials and default
recordings. Treat downloaded backups as secrets and store them securely.
Recordings moved to media/share/network storage need a separate backup policy;
an app backup does not guarantee those files are included. Before restoring on
a replacement HAOS host, restore/reconnect external storage and verify it is
mounted, then restore HA and the matching apps. Confirm cached inventory and
archive counts. Test restores periodically on an isolated instance with provider
apps stopped so it cannot compete for production sessions or actuate devices.

## Uninstall

Download wanted recordings and verify the exported files open. Create a final
backup, stop the provider app, remove its integration, uninstall the app, then
remove unused HACS components. Keep Vistoda if other providers use it. App
uninstall may remove private data; recovery requires the backup. External archive
files remain at their configured destination until explicitly removed. Revoke
Vistoda's vendor session using the vendor app if you are retiring access.

## Release verification

Releases use exact version tags and cannot overwrite an existing image. The
catalog publishes only after provider images are publicly readable on both
architectures and their digest, signature and exact source provenance verify.
The catalog release includes `release-evidence.json` with immutable digests and
source commits. A failed verification blocks publication; it is not bypassed
by a branch dispatch. Maintainers run `python scripts/verify-images.py` with
Docker registry access, Cosign and GitHub CLI before publishing catalog metadata.
