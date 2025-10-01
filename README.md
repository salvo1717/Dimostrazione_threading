# 🚀 Confronto Efficienza Thread in Python
### Esempio con Download di Immagini I/O-Bound

Questo progetto dimostra l'efficacia dell'utilizzo dei thread in Python per migliorare drasticamente le performance di operazioni **I/O-bound**, come il download di file da internet.

Il programma confronta il tempo di esecuzione di due script:
1.  **Sequenziale**: Scarica una serie di immagini una dopo l'altra.
2.  **Multithreading**: Scarica le stesse immagini contemporaneamente, assegnando ogni download a un thread separato.



---

## 💡 Concetti Chiave Dimostrati

* **Threading in Python**: Utilizzo del modulo `threading` per creare, avviare e gestire thread.
* **Operazioni I/O-Bound**: Si evidenzia come i thread siano ideali per compiti in cui il programma passa la maggior parte del tempo ad "aspettare" una risorsa esterna (in questo caso, la risposta di un server web).
* **Global Interpreter Lock (GIL)**: Anche se il GIL impedisce a più thread di eseguire bytecode Python simultaneamente, viene rilasciato durante le operazioni di I/O. Questo progetto ne dimostra l'effetto pratico: mentre un thread attende la rete, il sistema operativo può eseguire un altro thread, ottenendo un parallelismo effettivo.
* **Misurazione delle Performance**: Utilizzo di `time.perf_counter()` per un confronto accurato dei tempi di esecuzione.

---

## 🛠️ Installazione e Avvio

Per eseguire questo progetto sul tuo computer, segui questi passaggi.

### Prerequisiti
* Python 3.7+

### Installazione

1.  **Clona il repository**
    ```bash
    git clone https://github.com/salvo1717/Dimostrazione_threading.git
    cd Dimostrazione_threading
    ```

2.  **Installa le dipendenze**
    Il progetto richiede la libreria `requests`. Importala attraverso il comando:
    ```bash
    python -m pip install requests

### Utilizzo

Esegui lo script principale dalla riga di comando:
```bash
python threads.py
