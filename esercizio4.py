import argparse
import json
 
rubrica = {
  'Paolino Paperino': {'giorno': 9,
                      'mese': 'giugno',
                      'anno': 1934,
                      'età': 93,
                      'sesso': 'M',
                      'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1,
                'mese': 'marzo',
                'anno': 1980,
                'età': 46,
                'sesso': 'M',
                'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}
 
##opzioni da linea di comando: ogni opzione, se presente, vale True
parser = argparse.ArgumentParser()
parser.add_argument('-t','--scrivi_testo', action='store_true', help='Crea il file rubrica.txt')
parser.add_argument('-j','--scrivi_json', action='store_true', help='Crea il file rubrica.json')
parser.add_argument('-l','--leggi_json', action='store_true', help='Legge rubrica.json e ne visualizza il contenuto')
args = parser.parse_args()
 
'''Opzione per generare un file di testo rubrica.txt: un elemento per riga, informazioni separate da virgole'''
if args.scrivi_testo:
  with open('rubrica.txt', 'w') as file_testo:
    for nome, info in rubrica.items():
      file_testo.write(f"{nome}, {info['giorno']}, {info['mese']}, {info['anno']}, {info['età']}, {info['sesso']}, {info['mail']}\n")
 
'''Creare un file JSON che contiene la rubrica con la stessa struttura del dizionario'''
if args.scrivi_json:
  with open('rubrica.json', 'w') as write_file:
    json.dump(rubrica, write_file)
 
'''Leggere la rubrica dal file JSON e visualizzare tutto il contenuto'''
if args.leggi_json:
  with open('rubrica.json', 'r') as in_file:
    rubrica_letta = json.load(in_file)
  print(rubrica_letta)
