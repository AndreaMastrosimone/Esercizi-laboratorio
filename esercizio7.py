def tabellina(numero):
  '''Generatore: ad ogni next() restituisce il valore successivo della tabellina (0 x numero, 1 x numero, ... 10 x numero)'''
  for i in range(11):
    yield i * numero

def is_numero(testo):
  '''Ritorna True se il testo e' un numero valido: intero o decimale, anche negativo, con il punto o la virgola'''
  testo = testo.replace(',', '.')
  if testo.startswith('-'):
    testo = testo[1:]
  parti = testo.split('.')
  if len(parti) > 2: ##piu' di un punto
    return False
  for parte in parti:
    if not parte.isdecimal(): ##vuoto, lettere e caratteri speciali non vanno bene
      return False
  return True

def leggi_numero(messaggio):
  '''Chiede un numero finche' l'input non e' valido. Ritorna il numero (float) oppure None se l'utente scrive "esci"'''
  testo = input(messaggio).strip().lower()
  while testo != 'esci' and not is_numero(testo):
    testo = input('Errore: devi inserire un numero (oppure "esci" per uscire). Riprova: ').strip().lower()
  if testo == 'esci':
    return None
  return float(testo.replace(',', '.'))

def formatta(numero):
  '''Scrive 7 invece di 7.0 per i numeri interi'''
  if numero == int(numero):
    return str(int(numero))
  return str(numero)

def chiedi_si_no(messaggio):
  '''Chiede si o no finche' la risposta non e' valida. Ritorna True per si, False per no'''
  risposta = input(messaggio).strip().lower()
  while risposta != 'si' and risposta != 'sì' and risposta != 'no':
    risposta = input('Rispondi si oppure no: ').strip().lower()
  return risposta != 'no'

def gioca_tabellina(numero):
  '''Fa indovinare la tabellina del numero. Ritorna: risposte giuste al primo tentativo, errori, se l'utente ha scritto "esci"'''
  giuste = 0
  errori = 0
  i = 0
  for atteso in tabellina(numero):
    risposta = leggi_numero(f"Quanto fa {i} x {formatta(numero)}? ")
    if risposta == None:
      return giuste, errori, True
    primo_tentativo = True
    while round(risposta, 6) != round(atteso, 6): ##round evita errori dei decimali (0.1 x 3 = 0.30000000000000004)
      errori = errori + 1
      primo_tentativo = False
      risposta = leggi_numero('Sbagliato! Riprova: ')
      if risposta == None:
        return giuste, errori, True
    print('Bravo! Hai indovinato!')
    if primo_tentativo:
      giuste = giuste + 1
    i = i + 1
  return giuste, errori, False

def main():
  print('Benvenuto nel gioco delle tabelline! (scrivi "esci" in qualsiasi momento per uscire)')
  nome = input('Come ti chiami? ').strip()
  if nome == '':
    nome = 'giocatore'

  tot_giuste = 0
  tot_errori = 0
  continua = True
  while continua:
    numero = leggi_numero('\nInserisci un numero per generare la tabellina: ')
    if numero == None:
      break
    giuste, errori, uscito = gioca_tabellina(numero)
    tot_giuste = tot_giuste + giuste
    tot_errori = tot_errori + errori
    if uscito:
      break
    continua = chiedi_si_no('\nTabellina completata! Vuoi giocare ancora? (si/no) ')

  print(f"\nGrazie per aver giocato, {nome}!")
  print(f"Hai indovinato {tot_giuste} risposte al primo tentativo e hai sbagliato {tot_errori} volte.")
  print('A presto! (^_^)')

main()
