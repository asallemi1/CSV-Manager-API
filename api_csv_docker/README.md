Realizzare un’applicazione Python in grado di ricevere in input un file CSV, leggerne il contenuto e gestire i dati tramite programmazione a oggetti.

L’applicazione dovrà:

- leggere un file CSV fornito dall’utente;
- elaborare i dati utilizzando la libreria Pandas;
- restituire i risultati in formato JSON oppure HTML;
- organizzare il codice in più file e/o package Python.

La logica principale dovrà essere implementata in una classe dedicata chiamata `CsvManager`, responsabile della lettura, gestione e manipolazione dei dati CSV.

L’applicazione dovrà supportare le seguenti operazioni sui dati:

- visualizzazione delle prime 5 righe (`head`);
- visualizzazione delle ultime 5 righe (`tail`);
- informazioni su colonne e tipi di dato (`info`);
- statistiche descrittive (`describe`);
- dimensioni del DataFrame (`shape`);
- elenco delle colonne (`columns`);
- filtering tramite:
    - nome colonna,
    - operatore,
    - valore;
- ordinamento dei dati (`sorting`);
- gestione dei valori mancanti:
    - rimozione (`dropna`);
    - sostituzione (`fillna`);
- raggruppamento dei dati (`groupby`);
- unione di DataFrame (`merge`);
- creazione di pivot table (`pivot table`).

NB: non ci sono tutte le operazioni.

