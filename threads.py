import requests
import threading
import time
def scaricaimmagine(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Immagine scaricata con successo da {url}")
    else:
        print("Errore nel download dell'immagine")
    return response.content
#esecuzione senza threading
tempo_inizio = time.perf_counter()
for i in range(5):
    scaricaimmagine("https://picsum.photos/1280/720")
tempo_fine = time.perf_counter()
print(f"Tempo impiegato senza threading: {round(tempo_fine - tempo_inizio,2)} secondi")



# Esecuzione con threading 
tempo_inizio = time.perf_counter()
threads = []
for i in range(5):
    t=threading.Thread(target=scaricaimmagine, args=("https://picsum.photos/1280/720",))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
tempo_fine = time.perf_counter()
print(f"Tempo impiegato con threading: {round(tempo_fine - tempo_inizio,2)} secondi")