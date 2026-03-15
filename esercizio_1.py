##scrivete una funzione di controllo, is_pari(n), che accetti come parametro un numero intero e restituisca True se il numero è pari, False altrimenti.
def is_pari(n): 
  if n%2==0 :
    return True
  else :
    return False

##Create una funzione di generazione che chieda all’utente un numero intero positivo e lo restituisca come risultato della funzione. Se l’utente inserisce un numero non valido (es. negativo o zero), il ciclo deve continuare a richiederlo finché l’input non è corretto.
def generator():
  n=int(input("seleziona un intero positivo"))
  while n<=0 :
    print("valore errato, riprovare")
    n=int(input("seleziona un intero positivo"))
  return n

  ##Scrivete una funzione che usando il numero scelto dall’utente, generi una lista seguendo questa regola: se il numero è pari, va diviso per 2; se è dispari, va moltiplicato per 3 e aggiunto 1. Il processo va ripetuto finchè si arriva a 1 o la lista abbia piu’ di 100 numeri
  def do_something (n):
    valori=[] 
    valori.append(n)
    while n!=1 and len(valori)<100:
      if n%2==0:
        n=n//2
      else:
        n=(n*3)+1
      valori.append(n)
    return valori

##Scrivete una funzione analizza_sequenza(lista) che riceva la lista generata e restituisca tre valori: il valore massimo raggiunto, la lunghezza della sequenza e la somma di tutti i numeri.
def analizza_sequenza(valori):
  d=valori[0]
  k=0
  for i in range (len(valori)):
    if d<valori[i]:
      d=valori[i]
    k=k+valori[i]
  return d,k,len(valori)


##Scrivete una funzione ricerca(lista) che scorra la lista e stampi solo i numeri della sequenza che sono divisibili per 5. Se non ce ne sono, va stampato un messaggio dedicato.
def ricerca(valori):
  divisibili_per_5=[]
  for i in range (len(valori)):
    if valori[i]%5==0:
     divisibili_per_5.append(valori[i])
     print(valori[i])
  if len(divisibili_per_5)==0:
    print("lista vuota")

##Unite il tutto in un main program che chieda all’inizio all’utente quanti numeri vuole testare. Usate uno o più loop per chiedere all’utente i numeri da analizzare e per eseguire i punti precedenti per ogni numero. Alla fine stampate un riepilogo che mostri quale numero iniziale ha generato la sequenza più lunga.
def main():
  quanti=int(input("su quanti numeri vuoi testare il programma?"))
  lunghezza_max=0
  n_max=0
  for i in range (quanti):
    n_iniziale=generator()
    pari=is_pari(n_iniziale)
    lista=do_something(n_iniziale)
    massimo,somma,lunghezza=analizza_sequenza(lista)
    ricerca(lista)
    if lunghezza>lunghezza_max:
      lunghezza_max=lunghezza
      n_max=n_iniziale
  print("La sequenza più lunga è di...")
  print(lunghezza_max)
  print("Che deriva da...")
  print(n_max)
  
    




          
        
