import json

class Rubrica:
  '''Rappresenta una rubrica: un dizionario che associa ad ogni nome un dizionario con le sue informazioni
  (giorno, mese, anno, età, sesso, mail), come nell'esercizio 3'''

  @classmethod
  def da_json(cls, nome_file):
    '''Costruisce una rubrica leggendo un file JSON'''
    with open(nome_file, 'r') as in_file:
      dati = json.load(in_file)
    return cls(dati)

  @classmethod
  def da_testo(cls, nome_file):
    '''Costruisce una rubrica leggendo un file di testo, un contatto per riga:
    nome, giorno, mese, anno, età, sesso, mail'''
    dati = {}
    with open(nome_file, 'r') as file_testo:
      for riga in file_testo:
        campi = [campo.strip() for campo in riga.split(',')]
        if len(campi) == 7: ##salta le righe vuote
          dati[campi[0]] = {'giorno': int(campi[1]),
                            'mese': campi[2],
                            'anno': int(campi[3]),
                            'età': int(campi[4]),
                            'sesso': campi[5],
                            'mail': campi[6]}
    return cls(dati)

  def __init__(self, info=None):
    '''Inizializza la rubrica con un dizionario. Se non viene passato nulla, nessuna rubrica e' stata ancora aperta'''
    self.info = info

  def _vuota(self):
    '''Ritorna True se non c'e' nessun contatto (rubrica non aperta o senza elementi)'''
    return self.info == None or len(self.info) == 0

  def elenco_nomi(self):
    '''Ritorna la lista dei nomi dei contatti'''
    if self.info == None:
      return []
    return list(self.info)

  def apri(self, nome_file):
    '''APRI: legge la rubrica da un file, JSON o testo a seconda dell'estensione'''
    if nome_file.endswith('.json'):
      self.info = Rubrica.da_json(nome_file).info
    elif nome_file.endswith('.txt'):
      self.info = Rubrica.da_testo(nome_file).info
    else:
      print('Estensione non valida: usare .json o .txt')
      return
    print(f'Rubrica aperta: {len(self.info)} contatti')

  def aggiungi(self):
    '''AGGIUNGI: chiede i dati e aggiunge un contatto (serve aver prima aperto una rubrica)'''
    if self.info == None:
      print('Prima apri una rubrica')
      return
    nome = input('Nome: ').strip()
    giorno = int(input('Giorno di nascita: '))
    mese = input('Mese di nascita: ').strip()
    anno = int(input('Anno di nascita: '))
    eta = int(input('Età: '))
    sesso = input('Sesso (M/F): ').strip().upper()
    while sesso != 'M' and sesso != 'F':
      sesso = input('Valore non valido. Sesso (M/F): ').strip().upper()
    mail = input('Mail: ').strip()
    self.info[nome] = {'giorno': giorno, 'mese': mese, 'anno': anno, 'età': eta, 'sesso': sesso, 'mail': mail}
    print(f'Contatto {nome} aggiunto')

  def rimuovi(self, nome):
    '''RIMUOVI: elimina il contatto con il nome dato'''
    if self._vuota():
      print('La rubrica è vuota')
    elif nome not in self.info:
      print(f'Il contatto {nome} non esiste in rubrica')
    else:
      del self.info[nome]
      print(f'Contatto {nome} rimosso')

  def stampa(self, nome):
    '''STAMPA: stampa le informazioni del contatto con il nome dato, con il messaggio dell'esercizio 3'''
    if self._vuota():
      print('La rubrica è vuota')
    elif nome not in self.info:
      print(f'Il contatto {nome} non esiste in rubrica')
    else:
      contatto = self.info[nome]
      if contatto['sesso'] == 'M':
        print(f"""Caro {nome},
sei nato il {contatto['giorno']} di {contatto['mese']} del {contatto['anno']} e quindi a breve compirai {contatto['età']} anni.
Ti manderemo gli auguri a {contatto['mail']}""")
      else:
        print(f"""Cara {nome},
sei nata il {contatto['giorno']} di {contatto['mese']} del {contatto['anno']} e quindi a breve compirai {contatto['età']} anni.
Ti manderemo gli auguri a {contatto['mail']}""")

  def salva(self, nome_file):
    '''SALVA: scrive la rubrica su file, JSON o testo a seconda dell'estensione'''
    if self._vuota():
      print('La rubrica è vuota')
    elif nome_file.endswith('.json'):
      with open(nome_file, 'w') as write_file:
        json.dump(self.info, write_file)
      print(f'Rubrica salvata in {nome_file}')
    elif nome_file.endswith('.txt'):
      with open(nome_file, 'w') as file_testo:
        for nome, c in self.info.items():
          file_testo.write(f"{nome}, {c['giorno']}, {c['mese']}, {c['anno']}, {c['età']}, {c['sesso']}, {c['mail']}\n")
      print(f'Rubrica salvata in {nome_file}')
    else:
      print('Estensione non valida: usare .json o .txt')
