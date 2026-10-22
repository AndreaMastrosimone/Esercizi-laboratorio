import random
import time

##FUNZIONI DELLA LEZIONE
def stessa_diagonale(x0, y0, x1, y1):
  '''Ritorna True se le posizioni (x0, y0) e (x1, y1) sono sulla stessa diagonale'''
  dy = abs(y1 - y0)
  dx = abs(x1 - x0)
  return dx == dy

def incrocia_colonne(posizioni, col):
  '''Ritorna True se la regina in colonna col incrocia la diagonale di una delle regine precedenti'''
  for c in range(col):
    if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
      return True
  return False

##FUNZIONI NUOVE
def is_soluzione(posizioni):
  '''Ritorna True se nessuna regina della lista incrocia le altre'''
  for col in range(len(posizioni)):
    if incrocia_colonne(posizioni, col):
      return False
  return True

def trova_soluzione(N, limite=15):
  '''Mescola la lista [0..N-1] finche' non trova una soluzione. Ritorna la soluzione (come tupla) e il numero di tentativi.
  Se supera il tempo limite (secondi) ritorna None'''
  generatore = random.Random()
  lista = list(range(N))
  tentativi = 0
  inizio = time.time()
  while True:
    generatore.shuffle(lista)
    tentativi = tentativi + 1
    if is_soluzione(lista):
      return tuple(lista), tentativi ##tupla, cosi' e' una copia e non cambia con i prossimi shuffle
    if time.time() - inizio > limite:
      return None, tentativi

def ruota(posizioni):
  '''Ruota la scacchiera di 90 gradi: la regina in (riga, colonna) passa in (colonna, N-1-riga)'''
  N = len(posizioni)
  nuova = [0] * N
  for riga in range(N):
    colonna = posizioni[riga]
    nuova[colonna] = N - 1 - riga
  return tuple(nuova)

def simmetriche(posizioni):
  '''Ritorna le 4 soluzioni: originale, ruotata di 90, di 180 e di 270 gradi'''
  risultato = [posizioni]
  for i in range(3):
    posizioni = ruota(posizioni)
    risultato.append(posizioni)
  return risultato

'''1. Trovate 10 soluzioni con il metodo delle permutazioni: tempo medio per trovare una soluzione
   2. Contate quanti tentativi fa il programma per trovare ogni soluzione'''
somma_tempi = 0
for i in range(10):
  inizio = time.time()
  soluzione, tentativi = trova_soluzione(8)
  durata = time.time() - inizio
  somma_tempi = somma_tempi + durata
  print(f"Soluzione {i+1}: {soluzione} trovata in {tentativi} tentativi")
print(f"Tempo medio per soluzione: {somma_tempi / 10:.4f} secondi")

'''3. Soluzioni "uniche"'''
uniche = []
while len(uniche) < 10:
  soluzione, tentativi = trova_soluzione(8)
  if soluzione not in uniche:
    uniche.append(soluzione)
print("Soluzioni uniche:")
for soluzione in uniche:
  print(soluzione)

'''4. Contare quante volte ogni soluzione e' ripetuta (dizionario: soluzione -> numero di volte)'''
conteggio = {}
for i in range(100):
  soluzione, tentativi = trova_soluzione(8)
  if soluzione in conteggio:
    conteggio[soluzione] = conteggio[soluzione] + 1
  else:
    conteggio[soluzione] = 1
print("Su 100 soluzioni trovate, quelle diverse sono", len(conteggio))
print("Soluzioni ripetute:")
for soluzione, volte in conteggio.items():
  if volte > 1:
    print(f"{soluzione} compare {volte} volte")

'''5. Scacchiera NxN (per N = 2 e N = 3 non esistono soluzioni)'''
N = int(input("Scegli la dimensione N della scacchiera: "))
while N <= 0 or N == 2 or N == 3:
  N = int(input("Per questo valore non esistono soluzioni, riprova: "))
soluzione, tentativi = trova_soluzione(N)
if soluzione == None:
  print("Nessuna soluzione trovata entro 15 secondi")
else:
  print(f"Soluzione per N={N}: {soluzione} ({tentativi} tentativi)")

'''6. N piu' grande per cui si trova una soluzione in meno di 15 secondi (parte da 4 e sale finche' fallisce)'''
N = 4
migliore = 0
while True:
  soluzione, tentativi = trova_soluzione(N, 15)
  if soluzione == None:
    break
  migliore = N
  print(f"N={N}: soluzione trovata in {tentativi} tentativi")
  N = N + 1
print("Il valore di N piu' grande con una soluzione in meno di 15 secondi e'", migliore)

'''7. Soluzioni simmetriche per rotazione di 5 soluzioni uniche per la scacchiera 8x8'''
for soluzione in uniche[:5]:
  print("Soluzione:", soluzione)
  rotazioni = simmetriche(soluzione)
  angolo = 0
  for rot in rotazioni:
    print(f"  ruotata di {angolo} gradi: {rot}")
    angolo = angolo + 90

-----------------------------------
import random
import time

generatore = random.Random()

##FUNZIONI DELLA LEZIONE
def stessa_diagonale(x0, y0, x1, y1):
  '''Ritorna True se le posizioni (x0, y0) e (x1, y1) sono sulla stessa diagonale'''
  dy = abs(y1 - y0)
  dx = abs(x1 - x0)
  return dx == dy

def incrocia_colonne(posizioni, col):
  '''Ritorna True se la regina in colonna col incrocia la diagonale di una delle regine precedenti'''
  for c in range(col):
    if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
      return True
  return False

##FUNZIONI DI SUPPORTO
def is_soluzione(posizioni):
  '''Ritorna True se nessuna regina della lista incrocia le altre'''
  for col in range(len(posizioni)):
    if incrocia_colonne(posizioni, col):
      return False
  return True

def trova_soluzione(N, limite=15):
  '''Mescola la lista [0..N-1] finche' non trova una soluzione.
  Ritorna la soluzione (come tupla) e il numero di tentativi.
  Se supera il tempo limite (in secondi) ritorna None'''
  lista = list(range(N))
  tentativi = 0
  inizio = time.time()
  while True:
    generatore.shuffle(lista)
    tentativi = tentativi + 1
    if is_soluzione(lista):
      return tuple(lista), tentativi ##tupla: e' una copia e non cambia con i prossimi shuffle
    if time.time() - inizio > limite:
      return None, tentativi

##ROTAZIONI (punto 7): ogni funzione RITORNA la nuova soluzione
def rotazione_90(soluzione):
  '''(riga, colonna) -> (colonna, N-1-riga)'''
  N = len(soluzione)
  nuova = [0] * N
  for riga in range(N):
    colonna = soluzione[riga]
    nuova[colonna] = N - 1 - riga
  return tuple(nuova)

def rotazione_180(soluzione):
  '''(riga, colonna) -> (N-1-riga, N-1-colonna)'''
  N = len(soluzione)
  nuova = [0] * N
  for riga in range(N):
    colonna = soluzione[riga]
    nuova[N - 1 - riga] = N - 1 - colonna
  return tuple(nuova)

def rotazione_270(soluzione):
  '''(riga, colonna) -> (N-1-colonna, riga)'''
  N = len(soluzione)
  nuova = [0] * N
  for riga in range(N):
    colonna = soluzione[riga]
    nuova[N - 1 - colonna] = riga
  return tuple(nuova)

def simmetriche(soluzione):
  '''Ritorna le 4 soluzioni: originale, ruotata di 90, di 180 e di 270 gradi'''
  return [soluzione, rotazione_90(soluzione), rotazione_180(soluzione), rotazione_270(soluzione)]

##UNA FUNZIONE PER OGNI PUNTO
def punti_1_2():
  '''1. Tempo medio per trovare una soluzione (10 soluzioni)
     2. Numero di tentativi per ogni soluzione'''
  somma_tempi = 0
  for i in range(10):
    inizio = time.time()
    soluzione, tentativi = trova_soluzione(8)
    somma_tempi = somma_tempi + (time.time() - inizio)
    print(f"Soluzione {i+1}: {soluzione} trovata in {tentativi} tentativi")
  print(f"Tempo medio per soluzione: {somma_tempi / 10:.4f} secondi")

def punto_3(quante):
  '''3. Soluzioni uniche: un set non accetta duplicati. Ritorna il set'''
  uniche = set()
  while len(uniche) < quante:
    soluzione, tentativi = trova_soluzione(8)
    uniche.add(soluzione)
  return uniche

def punto_4(quante):
  '''4. Dizionario soluzione -> quante volte e' stata trovata'''
  conteggio = {}
  for i in range(quante):
    soluzione, tentativi = trova_soluzione(8)
    if soluzione in conteggio:
      conteggio[soluzione] = conteggio[soluzione] + 1
    else:
      conteggio[soluzione] = 1
  print(f"Su {quante} soluzioni trovate, quelle diverse sono {len(conteggio)}")
  for soluzione, volte in conteggio.items():
    if volte > 1:
      print(f"{soluzione} compare {volte} volte")

def punto_5():
  '''5. Scacchiera NxN (per N = 2 e N = 3 non esistono soluzioni)'''
  N = int(input("Scegli la dimensione N della scacchiera: "))
  while N <= 0 or N == 2 or N == 3:
    N = int(input("Per questo valore non esistono soluzioni, riprova: "))
  soluzione, tentativi = trova_soluzione(N)
  if soluzione == None:
    print("Nessuna soluzione trovata entro 15 secondi")
  else:
    print(f"Soluzione per N={N}: {soluzione} ({tentativi} tentativi)")

def punto_6():
  '''6. N piu' grande con una soluzione in meno di 15 secondi: parte da 4 e sale finche' la ricerca supera il limite'''
  N = 4
  migliore = 0
  while True:
    soluzione, tentativi = trova_soluzione(N, 15)
    if soluzione == None:
      break
    migliore = N
    print(f"N={N}: soluzione trovata in {tentativi} tentativi")
    N = N + 1
  print(f"Il valore di N piu' grande con una soluzione in meno di 15 secondi e' {migliore}")

def punto_7(uniche):
  '''7. Le 4 soluzioni simmetriche per rotazione di ogni soluzione unica'''
  for soluzione in uniche:
    print("Soluzione:", soluzione)
    angolo = 0
    for rot in simmetriche(soluzione):
      print(f"  ruotata di {angolo} gradi: {rot}")
      angolo = angolo + 90

def main():
  print("--- Punti 1 e 2 ---")
  punti_1_2()
  print("\n--- Punto 3: 10 soluzioni uniche ---")
  uniche = punto_3(10)
  for soluzione in uniche:
    print(soluzione)
  print("\n--- Punto 4: soluzioni ripetute ---")
  punto_4(100)
  print("\n--- Punto 5 ---")
  punto_5()
  print("\n--- Punto 6 (puo' richiedere un minuto) ---")
  punto_6()
  print("\n--- Punto 7: 5 soluzioni uniche con le rotazioni ---")
  cinque = list(punto_3(5))
  punto_7(cinque)

main()
