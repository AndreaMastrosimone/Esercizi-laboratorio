import argparse
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

'''visualizzate il contenuto del dizionario stampando a schermo delle stringhe formattate che contengano la chiave ed il valor di ognuno degli elementi(Esempio: ‘Paolino Paperino’, ‘giorno’ 9, ‘mese’ ‘giugno’, …)'''
def fun1():
  for nome,info in rubrica.items():
   print(f"'{nome}': ", end="") ##end serve per attaccare i print successivi
   for chiave, valore in info.items():
     print(f"'{chiave}' {valore}, ", end="")
   print("\n\n")

'''A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e visualizzate i nomi in ordine crescente di età'''
def fun2():
  lista_eta=[]
  for nome,info in rubrica.items():
   lista_eta.append([info['età'], nome])
  lista_eta.sort()
  print('Lista in ordine crescente di età: ')
  for coppia in lista_eta:
    print(f"-{coppia[1]}")

'''Invertire l’ordine della lista precedentemente costruita e visualizzatela'''
def fun3():
 lista_eta=[]
 for nome,info in rubrica.items():
  lista_eta.append([info['età'], nome])
 lista_eta.sort() ##dato che sono state introdotte le funzioni per l'ultimo punto, devo riprendere la lista
 print('Lista invertita di ordine')
 lista_eta.sort(reverse=True) ## li ordina in senso decrescente.
 for coppia in lista_eta:
  print(f"-{coppia[1]}")

'''Utilizzare la rubrica e scrivere su schermo per OGNI membro della rubrica, il seguente messaggio:
Car[o/a] [Nome],
sei nat[o/a] il [giorno] di [mese] del [anno] e quindi a breve compirai [età] anni.
Ti manderemo gli auguri a [mail]
dove [o/a] deve essere adattato all’attributo [M/F]'''
def fun4():
  for nome,info in rubrica.items():
    if info['sesso']=='M':
      print(f"""Caro {nome},
sei nato il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.
Ti manderemo gli auguri a {info['mail']}""")
    else:
      print(f"""Cara {nome},
sei nata il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.
Ti manderemo gli auguri a {info['mail']}""")
    print("\n\n")

'''Utilizzando args passate in input al vostro programma una chiave [giorno, mese, anno, età, sesso, mail] e visualizzate tutto il contenuto della rubrica (valori)che corrispondono a questa chiave'''
parser =  argparse.ArgumentParser()
parser.add_argument('-k','--chiave', help='Permette di selezionare la chiave da stampare')
parser.add_argument('-n','--nome_esteso', help='Permette di selezionare il nome per stampare il messaggio')
parser.add_argument('-a','--esegui_azione', help='Ti permette di eseguire le opzioni selezionare 1:visualizzazione dizionario,2:visualizzare la lista delle età in ordine crescente,3:visualizzare la lista delle età in ordine decrescente,4:invio del messaggio a ogni membro della rubrica,5:visualizzazione chiave selezionata')
args = parser.parse_args() ##si inserisce solo una volta nel codice.
def fun5():
 scelta = args.chiave
 if args.chiave: ##procede se viene inserito un qualcosa
   if scelta in ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']:
      for nome, info in rubrica.items():
         print(info[scelta])
   else:
      print('Chiave errata.')
 else:
   print("Errore: non hai specificato alcuna chiave!")

'''Utilizzando argparse visualizzate la stringa al punto 4 SOLO per il nome fornito come opzione al vostro programma (esempio: python esercizio_3.py –nome ‘Madoka Ayukawa’ –> esegue punto 4 solo per il nome indicato)'''
nominativo = args.nome_esteso
if args.nome_esteso:##procede se viene inserito un qualcosa
  if nominativo in rubrica.keys():
    info=rubrica[nominativo]
    if info['sesso']=='M':
      print(f"""Caro {nominativo},
sei nato il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.
Ti manderemo gli auguri a {info['mail']}""")
    else :
      print(f"""Cara {nominativo},
sei nata il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.
Ti manderemo gli auguri a {info['mail']}""")
  else:
    print('Nominativo errato.')

'''Utilizzando argparse introducede delle opzioni al vostro programma per eseguire i punti 1, 2, 3, 4, 5 dell’esercizio (esempio: python esercizio_3.py –lista_ordinata –> esegue il punto 2 dell’esercizio)'''
azione=args.esegui_azione
if args.esegui_azione:##se viene inserito il valore...
  match azione:
    case "1":
      fun1()
    case "2":
      fun2()
    case "3":
      fun3()
    case "4":
      fun4()
    case "5":
      fun5()
    case _:
      print("Input non valido!")
    
