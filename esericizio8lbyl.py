import random
import json
import os ##serve per controllare se il file esiste, PRIMA di aprirlo

NOME_FILE = 'Parole_impiccato.json'
MAX_ERRORI = 6
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'

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

def solo_lettere(testo):
  '''Ritorna True se il testo non e' vuoto e contiene solo lettere da a a z'''
  if len(testo) == 0:
    return False
  for c in testo:
    if c not in ALFABETO:
      return False
  return True

def carica_parole(nome_file):
  '''Legge la lista di parole dal file JSON controllando PRIMA tutto quello che potrebbe andare storto.
  Ritorna la lista di parole, oppure None se il file non e' utilizzabile'''
  if not os.path.exists(nome_file):
    print(f"Errore: il file {nome_file} non esiste.")
    return None
  if os.path.getsize(nome_file) == 0:
    print(f"Errore: il file {nome_file} e' vuoto.")
    return None
  with open(nome_file, 'r') as in_file:
    contenuto = json.load(in_file)
  if type(contenuto) != list:
    print("Errore: il file deve contenere una lista di parole.")
    return None
  parole = []
  for parola in contenuto:
    if type(parola) == str and solo_lettere(parola.lower()):
      parole.append(parola.lower())
  if len(parole) == 0:
    print("Errore: nel file non c'e' nessuna parola valida.")
    return None
  return parole

def gioca(parole):
  '''Una partita: sceglie una parola a caso e chiede lettere o parole finche' si indovina o finiscono gli errori'''
  parola = random.choice(parole)
  mostra = ['_'] * len(parola)
  lettere_usate = []
  errori = 0
  print(f"\nLa parola ha {len(parola)} lettere. Puoi sbagliare al massimo {MAX_ERRORI} volte.")

  while errori < MAX_ERRORI and '_' in mostra:
    print(STATI[errori])
    print(' '.join(mostra))
    print('Lettere provate:', ', '.join(lettere_usate))
    tentativo = input('Inserisci una lettera o prova a indovinare la parola: ').strip().lower()

    if tentativo == '':
      print('Input vuoto: inserisci almeno una lettera.')
    elif not solo_lettere(tentativo):
      print('Puoi usare solo lettere dalla a alla z.')
    elif len(tentativo) == 1:
      if tentativo in lettere_usate:
        print(f"Hai gia' provato la lettera '{tentativo}'.")
      else:
        lettere_usate.append(tentativo)
        if tentativo in parola:
          for i in range(len(parola)):
            if parola[i] == tentativo:
              mostra[i] = tentativo
          print(f"La lettera '{tentativo}' e' presente!")
        else:
          errori = errori + 1
          print(f"La lettera '{tentativo}' non c'e'.")
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

def main():
  print("Benvenuto al gioco dell'impiccato!")
  parole = carica_parole(NOME_FILE)
  if parole == None:
    return
  ripeti = True
  while ripeti:
    gioca(parole)
    risposta = input("\nVuoi giocare di nuovo? (s/n) ").strip().lower()
    while risposta != 's' and risposta != 'n':
      risposta = input('Rispondi s oppure n: ').strip().lower()
    ripeti = risposta == 's'
  print('Grazie per aver giocato! Arrivederci!')

main()
