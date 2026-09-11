# Vistoda Ring

Choose a short Home Assistant alias, install and start the app, then open the
automatically discovered **Vistoda Ring** flow. Enter the Ring account email and
password. If Ring sends an SMS, enter only the newest six-digit code.

## Multiple entrances

Keep **Intercoms** empty for normal setup, including accounts with several
entrances. Complete login/SMS, then select the actual intercom by name/location
in Home Assistant. Vistoda creates deterministic `intercom-<id>` routes and
offers the other entrances through follow-up discovery. You do not need to find
or copy numeric IDs. Existing single-device routes and their flat archives remain
available for compatibility; an unbound route cannot choose between several devices.

Advanced users can set **Intercoms** to preserve custom aliases for verified
physical IDs. This optional override is not required for multi-intercom setup:

```yaml
alias: entrance
intercoms:
  - alias: entrance
    device_id: 100000001
  - alias: side-gate
    device_id: 100000002
recording_storage: private
```

The IDs above are examples: replace them with verified Ring device IDs. A name,
location ID, MAC address or guessed ID is not a binding. Use the device identity
reported by Vistoda or the existing Ring integration; keep it private. The list
supports at most 32 entrances. Duplicate aliases/IDs and missing IDs prevent
startup. The list overrides generated aliases for its devices; it does not
restrict which account devices can be discovered. The top alias is only a
discovery preference when it belongs to the published inventory.

After enrollment, an app restart fetches the bounded private inventory and
publishes one Supervisor discovery containing only aliases and string device IDs,
never account names or locations. Before enrollment or when inventory is
unavailable, static bootstrap discovery lets Home Assistant resume setup.
Choose the
entrance in Vistoda before opening, viewing history or starting audio. Every
alias shares the enrolled account session but has its own physical destination
and recording directory `device-<id>`. Renaming an alias keeps that archive;
assigning a different device ID selects a different archive. Removed devices'
directories are retained for backup and can be restored with the same binding.

Existing unbound recordings have no recorded physical identity. When switching
to explicit bindings, they remain untouched at the archive root and are not
silently assigned to an entrance. Export them before switching or retain the
backup for manual, verified archival handling.

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
Storage changes preserve every `device-<id>` directory, including currently
disabled devices, and legacy root files. All copies are checked before any
source is retired. Conflicting files, symlinks or unknown subdirectories stop
migration and preserve source data. A failed migration leaves the old storage
selection marker active; resolve the conflict before retrying.

## Più citofoni

Lascia **Citofoni** vuoto anche con più ingressi: completa login/SMS e scegli
il citofono reale per nome e posizione. Gli alias `intercom-<id>` sono automatici
e Home Assistant propone gli altri ingressi, senza copiare ID. La lista manuale
serve solo per alias personalizzati avanzati con ID verificati; gli ID
dell'esempio non sono reali. Seleziona sempre l'ingresso in Vistoda: apertura,
cronologia e audio restano associati allo stesso citofono.

Gli archivi esplicitamente associati sono salvati in `device-<id>`: rinominare
l'alias conserva i file, assegnare un altro ID apre un archivio diverso. I file
del vecchio archivio senza identità rimangono nella radice; esportali prima del
passaggio. La modifica della destinazione copia e verifica tutte le directory
prima di ritirare i sorgenti. Conflitti e collegamenti simbolici bloccano la
migrazione, senza eliminare i file sorgenti.

Home Assistant receives only a private workload token through Supervisor
discovery. The token, bridge URL and port are not user configuration fields.

Port 8775 is private by default. Use the standalone Vistoda Ring container for
advanced SceneTrove or native-client deployments that require a remote bridge.

Failed API requests are correlated by a server-generated `x-request-id` without
logging query values, credentials, device aliases or request bodies. Include
that response ID when reporting a reproducible app error.
