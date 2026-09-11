# Installare, recuperare e aggiornare Vistoda

## Prima di installare

Servono Home Assistant OS o Supervised su amd64/aarch64, lo store app del
Supervisor e HACS. Container/Core richiede container provider separati e URL/token
privati configurati manualmente; non dispone dello store app. Tieni disponibile
l'app del produttore e il codice MFA più recente. Controlla lo spazio libero e
crea un backup di Home Assistant prima di abilitare registrazioni.

Scegli i provider usati: Ring per citofoni, Blink per telecamere e clip, EZVIZ
per telecamere supportate. Installa **Vistoda** in HACS e, se usi Blink, anche
**Vistoda Blink**. Riavvia Home Assistant una volta dopo entrambe le installazioni.
Aggiungi questo repository allo store app, installa, configura e avvia le app
scelte. Completa ciascuna integrazione scoperta in Impostazioni → Dispositivi e
servizi. Inserisci le credenziali solo nel flusso dell'integrazione. Per EZVIZ
serve il seriale nelle informazioni dispositivo prima dell'avvio: non è il
codice di verifica.

## Recuperare discovery e accesso

Se la discovery non compare, controlla che l'app provider sia avviata e leggi
la scheda Registro. Verifica installazione HACS e riavvio di Home Assistant.
Ricarica l'integrazione presente oppure riavvia una volta il provider per
ripubblicare la discovery. Mantieni private le porte API.

Per autorizzazione scaduta usa il flusso di riconnessione account, conservando
l'integrazione per mantenere dispositivi, entità e dashboard. Dopo un codice
Blink rifiutato, reinserisci le credenziali e usa solo il codice appena richiesto.
Se il produttore limita le richieste, attendi il periodo indicato. Controlla nome
e posizione dei citofoni Ring: apertura e cronologia devono usare lo stesso ingresso.

Per assistenza raccogli versioni HA/integrazione/app e ID richiesta dell'errore.
Scarica la diagnostica dal menu dell'integrazione quando disponibile, controlla
e oscura i dati prima di condividerli. Non allegare credenziali, token, seriali
o media privati.

## Aggiornamento e rollback

Leggi le note di rilascio e le versioni compatibili. Crea un backup contenente
Home Assistant e le app provider, scaricalo su un altro dispositivo e annota
versioni e destinazioni archivio. Aggiorna prima le app provider, poi le
integrazioni HACS corrispondenti; riavvia Home Assistant una volta. Verifica app
avviate, inventario memorizzato, discovery e autorizzazione.

Se l'aggiornamento fallisce, arresta il provider e ripristina insieme il backup
precedente dell'app e di Home Assistant: credenziali e registri devono restare
coerenti con l'adapter. Non ricostruire o sovrascrivere tag immutabili. Dopo il
restore potrebbe servire riconnettere l'account se il token precedente è scaduto.

## Backup e ripristino

Il backup app contiene `/data` privato, incluse credenziali e registrazioni
predefinite. Custodiscilo come un segreto. Archivi spostati su media/share/rete
richiedono backup separati; il backup app non ne garantisce l'inclusione.
Su un nuovo host ripristina e verifica prima gli archivi esterni, poi Home
Assistant e le app corrispondenti. Controlla inventario e conteggi archivio.
Prova periodicamente il restore su un'istanza isolata con provider arrestati,
così non compete per sessioni o aziona dispositivi.

## Disinstallazione

Scarica le registrazioni da conservare e verifica che si aprano. Crea un ultimo
backup, arresta l'app, rimuovi l'integrazione, disinstalla l'app e infine rimuovi
i componenti HACS inutilizzati. Conserva Vistoda se serve ad altri provider.
La disinstallazione può eliminare i dati privati; il recupero richiede il backup.
I file esterni restano nella destinazione configurata finché non vengono rimossi
esplicitamente. Revoca la sessione Vistoda dall'app del produttore se ritiri l'accesso.

## Verifica dei rilasci

Ogni rilascio usa un tag versione esatto e non sovrascrivibile. Il catalogo viene
pubblicato solo dopo verifica di disponibilità pubblica, entrambe le architetture,
digest, firma e provenienza esatta delle immagini. L'allegato `release-evidence.json`
riporta digest immutabili e commit sorgente. Una verifica fallita blocca il rilascio.
