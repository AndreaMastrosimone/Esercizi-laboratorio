import random
import json

NOME_FILE = 'Parole_impiccato.json'
MAX_ERRORI = 6
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
SCELTE = {'s': True, 'n': False}

STATI = [
"""
  +---+
  |   |
  |
  |
  |
  |
=========""",
"""
  +---+
  |   |
  |   O
  |
  |
  |
=========""",
"""
  +---+
  |   |
  |   O
  |   |
  |
  |
=========""",
"""
  +---+
  |   |
  |   O
  |  /|
  |
  |
=========""",
"""
  +---+
  |   |
  |   O
  |  /|\\
  |
  |
=========""",
"""
  +---+
  |   |
  |   O
  |  /|\\
  |  /
  |
=========""",
"""
  +---+
  |   |
  |   O
  |  /|\\
  |  / \\
  |
========="""
]

def controlla(testo):
  '''Non ritorna niente: se qualcosa non va solleva un'eccezione.
  IndexError se il testo e' vuoto, ValueError se contiene qualcosa che non e' una lettera da a a z'''
  testo[0] ##se il testo e' vuoto: IndexError
  for c in testo:
    ALFABETO.index(c) ##se c non e' una lettera: ValueError

def carica_parole(nome_file):
  '''Prova a leggere la lista di parole dal file JSON e gestisce gli errori man mano che capitano.
  Ritorna la lista di parole, oppure None se il file non e' utilizzabile'''
  try:
    with open(nome_file, 'r') as in_file:
      contenuto = json.load(in_file)
    contenuto[0] ##se la lista e' vuota: IndexError (se non e' una lista: KeyError o TypeError)
    parole = []
    for parola in contenuto:
      controlla(parola.lower()) ##se la parola non e' fatta solo di lettere: ValueError o IndexError (AttributeError se non e' una stringa)
      parole.append(parola.lower())
  except FileNotFoundError:
    print(f"Errore: il file {nome_file} non esiste.")
    return None
  except json.JSONDecodeError:
    print(f"Errore: il file {nome_file} non e' un JSON valido.")
    return None
  except (KeyError, TypeError, AttributeError, ValueError, IndexError):
    print(f"Errore: {nome_file} deve contenere una lista non vuota di parole fatte solo di lettere.")
    return None
  return parole

def gioca(parole):
  '''Una partita: sceglie una parola a caso e chiede lettere o parole finche' si indovina o finiscono gli errori'''
  parola = random.choice(parole)

  ##dizionario lettera -> lista delle posizioni in cui compare (come l'esempio del dizionario della lezione)
  posizioni = {}
  for i in range(len(parola)):
    try:
      posizioni[parola[i]].append(i)
    except KeyError:
      posizioni[parola[i]] = [i]

  mostra = ['_'] * len(parola)
  usate = {}
  errori = 0
  print(f"\nLa parola ha {len(parola)} lettere. Puoi sbagliare al massimo {MAX_ERRORI} volte.")

  while errori < MAX_ERRORI and '_' in mostra:
    print(STATI[errori])
    print(' '.join(mostra))
    print('Lettere provate:', ', '.join(usate))
    tentativo = input('Inserisci una lettera o prova a indovinare la parola: ').strip().lower()

    try:
      controlla(tentativo)
    except IndexError:
      print('Input vuoto: inserisci almeno una lettera.')
      continue
    except ValueError:
      print('Puoi usare solo lettere dalla a alla z.')
      continue

    if len(tentativo) == 1:
      try:
        usate[tentativo]
      except KeyError:
        usate[tentativo] = True ##lettera nuova: la segno come provata
      else:
        print(f"Hai gia' provato la lettera '{tentativo}'.")
        continue

      try:
        indici = posizioni[tentativo]
      except KeyError:
        errori = errori + 1
        print(f"La lettera '{tentativo}' non c'e'.")
      else:
        for i in indici:
          mostra[i] = tentativo
        print(f"La lettera '{tentativo}' e' presente!")
    else:
      if tentativo == parola:
        mostra = list(parola)
      else:
        errori = errori + 1
        print(f"'{tentativo}' non e' la parola giusta.")

  if '_' not in mostra:
    print(f"\nComplimenti! Hai indovinato la parola '{parola}' con {errori} errori!")
  else:
    print(STATI[errori])
    print(f"\nMi dispiace, hai esaurito i tentativi. La parola era '{parola}'.")

def chiedi_ripetere():
  '''Chiede s o n finche' la risposta non e' valida. Ritorna True per s, False per n'''
  while True:
    try:
      return SCELTE[input("\nVuoi giocare di nuovo? (s/n) ").strip().lower()]
    except KeyError:
      print('Rispondi s oppure n.')

def main():
  print("Benvenuto al gioco dell'impiccato!")
  parole = carica_parole(NOME_FILE)
  if parole == None:
    return
  try:
    ripeti = True
    while ripeti:
      gioca(parole)
      ripeti = chiedi_ripetere()
    print('Grazie per aver giocato! Arrivederci!')
  except (KeyboardInterrupt, EOFError): ##Ctrl+C o input terminato
    print('\nGioco interrotto. Arrivederci!')

main()
