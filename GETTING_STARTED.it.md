# Iniziare con Vistoda

Questa è la procedura consigliata per Home Assistant OS e Home Assistant
Supervised. Installa soltanto app provider private e non espone telecamere o
citofoni su Internet.

Vistoda porta in un unico pannello Home Assistant le funzioni supportate di Ring
Intercom, Blink ed EZVIZ. Non sostituisce integralmente tutte le app ufficiali:
conservale per il recupero degli account e per le funzioni non supportate indicate
nella [matrice di compatibilità](COMPATIBILITY.md).

## Prima di iniziare

Servono:

- Home Assistant 2026.8.0 o successivo su `amd64` o `aarch64`;
- HACS e accesso allo store delle app di Home Assistant;
- credenziali e codice MFA più recente di ogni provider;
- numero seriale di ogni telecamera EZVIZ da aggiungere;
- un backup aggiornato di Home Assistant.

Home Assistant Container e Core non includono lo store delle app. Usa i
container provider standalone soltanto se sai gestire URL privati, token,
storage e accesso di rete.

## 1. Installa le integrazioni Home Assistant

1. Installa [Vistoda tramite HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-home-assistant&category=integration).
2. Se usi Blink, installa anche [Vistoda Blink tramite HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=luigibarretta&repository=vistoda-blink&category=integration).
3. Riavvia Home Assistant una sola volta dopo le installazioni HACS.

Ring ed EZVIZ usano l'integrazione principale Vistoda. Blink richiede anche il
piccolo adattatore specifico per mantenere stabili entità e servizi esistenti.

## 2. Aggiungi il repository delle app Vistoda

Usa [Aggiungi Vistoda Apps](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fluigibarretta%2Fvistoda-addons),
oppure aggiungi questo URL in **Impostazioni → App → App store → Repository**:

`https://github.com/luigibarretta/vistoda-addons`

Installa soltanto le app provider necessarie. Non pubblicare le loro porte API.

## 3. Configura un provider

### Ring Intercom

1. Installa **Vistoda Ring**.
2. Lascia **Citofoni** vuoto nella configurazione normale, anche se l'account ha
   più ingressi. Puoi mantenere l'alias predefinito.
3. Avvia l'app.
4. Apri **Impostazioni → Dispositivi e servizi** e completa il flusso Vistoda
   Ring rilevato. Inserisci le credenziali Ring e il codice SMS più recente.
5. Seleziona l'ingresso usando nome reale e posizione. Home Assistant proporrà
   gli altri citofoni con ulteriori flussi di configurazione.

Risultato atteso: ogni citofono selezionato possiede una entry Vistoda distinta,
con controlli, cronologia e archivio. La selezione in `/vistoda/ring` limita ogni
azione a quel dispositivo fisico.

Ring usa API consumer sperimentali non supportate da Ring per integrazioni di
terze parti. Il pannello Vistoda conferma l'apertura; button e automazioni Home
Assistant autorizzati possono richiamarla senza una modale interattiva. Nessun
percorso ritenta automaticamente l'azione fisica. Per gli eventi push serve
l'uscita TCP 5228 verso `mtalk.google.com`.

### Blink

1. Verifica che **Vistoda** e **Vistoda Blink** siano installati tramite HACS.
2. Installa e avvia l'app **Vistoda Blink**. Non ha opzioni utente normali.
3. Completa il flusso rilevato usando le credenziali Blink e il codice di
   verifica più recente.

Risultato atteso: la rete Blink e le sue telecamere compaiono come dispositivi
Home Assistant. `/vistoda/blink` mostra gli ultimi snapshot salvati senza
risvegliare ogni telecamera a batteria. Snapshot e live vengono richiesti
esplicitamente.

Il live Walnut/IMMI è supportato. L'audio full-duplex Cayuga/WebRTC rimane
disattivato perché la policy provider dell'account non lo abilita attualmente.

### EZVIZ

1. Installa **Vistoda EZVIZ**.
2. Prima dell'avvio inserisci un alias breve e il seriale. Una telecamera
   standalone usa normalmente il canale `1`; abilita il substream solo se serve.
3. Per più telecamere lascia vuoto il seriale legacy e compila **Più telecamere**
   con alias e coppie seriale/canale univoche.
4. Avvia l'app e completa ogni flusso Vistoda EZVIZ rilevato con credenziali e
   verifica MFA.

Risultato atteso: ogni coppia seriale/canale configurata ha una entry Home
Assistant separata. `/vistoda/ezviz` mostra l'ultimo snapshot salvato senza
generarne uno nuovo finché non lo richiedi.

Audio bidirezionale e accesso diretto alla microSD non sono disponibili senza
un percorso EZVIZ Open Platform utilizzabile. La compatibilità dello stream
dipende dal modello e dal profilo di cifratura.

## 4. Verifica l'installazione

Apri `/vistoda` dal menu laterale e controlla che:

- ogni provider installato risulti disponibile;
- tutte le telecamere e i citofoni attesi siano selezionabili;
- snapshot salvati e valori di stato vengano caricati;
- nei log dell'app provider non compaiano errori ripetuti di autenticazione o riavvio.

Esegui poi un solo test multimediale intenzionale, preferibilmente su una
telecamera alimentata. Non usare apertura del portone, formattazione USB,
eliminazione file o live di telecamere a batteria come test d'installazione.

## Registrazioni e backup di rete

Ogni app possiede un volume dati privato. `/data/recordings` in Ring, Blink ed
EZVIZ indica quindi tre posizioni fisiche distinte. Vistoda mostra il percorso
effettivo e offre riproduzione, download ed eliminazione supportati tramite Home
Assistant.

Per configurare un backup NFS o SMB:

1. Apri **Impostazioni → Sistema → Archiviazione**.
2. Aggiungi uno spazio di rete scrivibile con utilizzo **Media**.
3. Inserisci il nome dello spazio, non l'indirizzo del server o un percorso
   `/media/...`, nelle opzioni Vistoda della entry Blink o EZVIZ.

L'integrazione verifica che la destinazione sia un vero mount di rete scrivibile
con almeno 512 MiB liberi. Non ripiega mai silenziosamente sul disco Home
Assistant. Ring può usare un mount gestito da HAOS anche come archivio primario;
la documentazione dell'app descrive le destinazioni disponibili.

## Problemi comuni

| Sintomo | Controllo |
| --- | --- |
| L'integrazione non viene rilevata | Avvia l'app provider, controlla la scheda Log, verifica l'installazione HACS e riavvia l'app una volta. |
| Login o MFA rifiutato | Avvia un nuovo accesso e usa solo il codice più recente. Interrompi i tentativi se il provider segnala un limite. |
| Manca un dispositivo | Controlla la selezione Ring o la coppia seriale/canale EZVIZ; non indovinare mai un ID fisico. |
| Il live non parte | Verifica modello supportato, assenza di altre sessioni e app in esecuzione. Prova prima una telecamera alimentata. |
| Il backup non è disponibile | Controlla nome esatto dello storage HA, utilizzo Media, mount scrivibile e spazio libero. |
| Una funzione non compare | Controlla le capacità mostrate da Vistoda e la [matrice](COMPATIBILITY.md); i controlli non supportati vengono nascosti. |

Per riconnessione degli account, aggiornamenti, rollback, ripristino e
disinstallazione continua con la [guida operativa](OPERATIONS.it.md).
