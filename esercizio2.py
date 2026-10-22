testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

'''Contate le righe non vuote che compongono l’estratto'''
diviso=testo.split('\n') ##contiene alcuni elementi che sono 'il nulla' che si trovava fra i due spazi. ##si poteva usare .splitlines()
count=0
for i in diviso: ## signfica per ogni i che è un valore in diviso
  if i!= "": 
    count=count+1
print('Le righe non vuote sono',count)

'''Contate le parole che compongono l’estratto'''
parole=testo.split()
print('Il totale delle parole è',len(parole))

'''Contate i caratteri alfanumerici che compongono l’estratto'''
alfanumerici="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
caratteri=0
for i in testo:
    if i in alfanumerici:
      caratteri=caratteri+1
print('Il numero di caratteri è: ',caratteri)

'''Chiedere all’utente una lettera e contate quante volte compare nel testo'''
alfabeto="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter=input('Scegli una lettera')
while letter not in alfabeto or len(letter)!=1:
  letter=input('Carattere non valido. Selezionare una lettera')
print('conteggio: ',testo.count(letter))

'''Sostituite tutte le parole day, water e about con la parola PYTHON in tutti i versi'''
new_testo=[]
for i in parole:
  if i.lower() not in ["day","water","about"]: ##sistemare quando c'è tipo water,??
    new_testo.append(i)
  else :
    new_testo.append("PYTHON")

'''Riscrivete il testo in modo che tutte le parole in posizione dispari siano scritte in maiuscolo'''
testo_upper=[]
j=0
for i in parole:
  j=j+1
  if j%2!=0:
    testo_upper.append(i.upper())
  else:
    testo_upper.append(i)

'''Riscrivere il testo invertendo l’ordine delle frasi dal basso all’alto.'''
testo_contrario=[]
for i in range(len(diviso)-1,-1,-1): ##primo -1 perchè vogliamo includere lo 0, secondo -1 per decrementare
  testo_contrario.append(diviso[i])

'''Riscrivete il testo in modo che il secondo verso di ogni strofa sia scritto a specchio (cioè al contrario carattere per carattere: Ad esempio, questa frase’ –> ‘esarf atseuq ,oipmese dA’)'''
versi_puliti=[]
for riga in diviso:
  if riga != "": ## li mettiamo solo se non iniziano col nulla, quindi non sono i versi vuoti.
    versi_puliti.append(riga)
testo_modificato=[]
count=0
for riga in versi_puliti:
  if count%4==1:
    testo_modificato.append(riga[::-1]) ##slicing negativo
  else:
    testo_modificato.append(riga)
  count=count+1
for riga in testo_modificato:
  print(riga)
  
'''Trovate eventuali parole che compaiono in tutte le strofe'''
lista_strofe=testo.split("\n\n")
strofa1 = set(lista_strofe[0].lower().split())
strofa2 = set(lista_strofe[1].lower().split())
strofa3 = set(lista_strofe[2].lower().split())
strofa4 = set(lista_strofe[3].lower().split())
parole_comuni = strofa1 & strofa2 & strofa3 & strofa4


'''Create la lista univoca di tutte le parole che compaiono nel testo, ordinatela per lunghezza delle parole e visualizzatela'''
tot_parole= strofa1|strofa2|strofa3|strofa4
lista_univoca=[]
for parola in tot_parole:
  lista_univoca.append(parola)
lista_univoca.sort(key=len)
print("Visualizzazione lista parole: ", lista_univoca)

'''Create un dizionario che mappi OGNI carattere (chiave) con la sua occorrenza nel testo (valore) e visualizzatelo'''
dizionario_conteggio = {}
for carattere in testo:
  if carattere in dizionario_conteggio:
    dizionario_conteggio[carattere]=dizionario_conteggio[carattere]+1 ##con la notazione[] capisce che quando siamo a dx ci si rifersice al value
  else :
    dizionario_conteggio[carattere]=1
print("Il dizionario dei caratteri è: ", dizionario_conteggio)

'''Create un dizionario come il precedente per i soli caratteri alfanumerici (no caratteri speciali), ignorando maiuscole e minuscole'''
testo_minuscolo = testo.lower()
dizionario_alfanum={}
for carattere in testo_minuscolo:
  if carattere in alfanumerici:
    if carattere in dizionario_alfanum:
      dizionario_alfanum[carattere]=dizionario_alfanum[carattere]+1
    else:
      dizionario_alfanum[carattere]=1
print("Il dizionario puramente alfanumerico è: ", dizionario_alfanum)
  


  



