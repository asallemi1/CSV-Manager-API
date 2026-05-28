# CSV Manager API

## Descrizione del progetto

Il progetto consiste nello sviluppo di una REST API in Python tramite Flask per la gestione e l’analisi di file CSV.

L’applicazione permette di caricare un file CSV, elaborarlo tramite diverse operazioni sui dati e restituire il risultato in formato JSON.

La gestione dei dati è implementata secondo i principi della programmazione a oggetti, utilizzando una classe dedicata chiamata `CsvManager`.

---

# Struttura del progetto

Il progetto è stato organizzato nel seguente modo:

* `main.py`
  Contiene l’app Flask e la definizione delle route API.

* `Dockerfile`
  File utilizzato per la containerizzazione dell’applicazione tramite Docker.

* `requirements.txt`
  Contiene tutte le dipendenze del progetto 

* `it/akron/csv_manager/csv_manager.py`
  Contiene la classe `CsvManager` e i relativi metodi per la gestione dei file CSV.

---

# Classe CsvManager

Il file `csv_manager.py` contiene la classe `CsvManager`, responsabile della lettura e manipolazione dei dati CSV tramite Pandas.

Tra le operazioni supportate è possibile implementare:

* visualizzazione dati (`head`, `tail`);
* statistiche descrittive (`info`, `describe`, `shape`, `columns`);
* pivot table

---

# main.py e gestione delle route

Nel file `main.py` sono state importate:

* le librerie necessarie per Flask;
* le librerie per la gestione dei JSON;
* la classe `CsvManager`.

È stata sviluppata un’unica route `/csv` che permette di:

* caricare un file CSV;
* specificare l’operazione da eseguire tramite parametro `action`.

La route supporta sia il metodo `GET` che il metodo `POST`.

Questo approccio consente di:

* passare il percorso del file CSV e l’azione direttamente tramite URL;
* inviare eventuali parametri aggiuntivi tramite JSON personalizzato nel body della richiesta, come nel caso della `pivot table`.

---

# Docker

## Creazione dell’immagine Docker

Da terminale eseguire:

```bash
docker build -t csv-api .
```

## Avvio del container

```bash
docker run -d -p 5000:5000 -v filepath:/data csv-api
```

### Spiegazione del volume

L’opzione:

```bash
-v filepath:/data
```

crea un collegamento tra il path locale, in cui sono contenuti i diversi csv, e la cartella `/data` presente all’interno del container Docker.

In questo modo è possibile caricare facilmente qualsiasi file CSV presente sul path direttamente dall’applicazione.

---

# Utilizzo delle API

Dopo aver avviato il container, è possibile testare le API tramite Rested oppure qualsiasi client HTTP.

Esempio di chiamata:

```bash
http://127.0.0.1:5000/csv?csv=/data/file.csv&action=head
```

In questo esempio:

* `csv` rappresenta il percorso del file CSV all’interno del container;
* `action` rappresenta l’operazione da eseguire.

---
