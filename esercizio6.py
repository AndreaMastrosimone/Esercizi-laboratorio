import Rubrica ##importa il file Rubrica.py (deve stare nella stessa cartella)

def main():
  '''Chiede in modo interattivo l'azione da svolgere finche' non viene scritto EXIT'''
  rubrica = Rubrica.Rubrica()

  while True:
    print("\nScegliere un'azione: APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA (EXIT per uscire)")
    azione = input().strip().upper()

    if azione == 'APRI':
      nome_file = input('Nome del file da aprire (.json o .txt): ').strip()
      rubrica.apri(nome_file)
    elif azione == 'AGGIUNGI':
      rubrica.aggiungi()
    elif azione == 'RIMUOVI':
      print('Contatti in rubrica:', rubrica.elenco_nomi())
      nome = input('Nome del contatto da rimuovere: ').strip()
      rubrica.rimuovi(nome)
    elif azione == 'SALVA':
      nome_file = input('Nome del file in cui salvare (.json o .txt): ').strip()
      rubrica.salva(nome_file)
    elif azione == 'STAMPA':
      print('Contatti in rubrica:', rubrica.elenco_nomi())
      nome = input('Nome del contatto da stampare: ').strip()
      rubrica.stampa(nome)
    elif azione == 'EXIT':
      print('Uscita dal programma.')
      break
    else:
      print('Azione non valida.')

main()
