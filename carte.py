import random
from collections import namedtuple
 
"""
class Partita(Giocatore):
    lista_giocatori = []
    def __init__(self,num,nome,carta):
        for i in range(num):
            self.lista_giocatori.append(Giocatore(nome, carta))
  """
class Mazzo:
    simboli = ['\u2666','\u2665','\u2663','\u2660'] #Quadri, Cuori, Fiori, Picche
    Reali = ["J","Q", "K"]
    mazzo_carte = []
    
    def __init__(self,numero_mazzi):
        Carta = namedtuple('Valore', ['Simbolo', 'Tipo'])
        for mazzi in range(numero_mazzi):
            for simbolo in self.simboli:
                carta = Carta(1,['A',simbolo])
                self.mazzo_carte.append(carta)
                for i in range(2,11):
                    carta = Carta(i,[str(i),simbolo])
                    self.mazzo_carte.append(carta)
                for reale in self.Reali:
                    carta = Carta(10,[reale,simbolo])
                    self.mazzo_carte.append(carta)
        random.shuffle(self.mazzo_carte)

    def get_mazzo(self):
        return self.mazzo_carte

    
    def stampa_mazzo(self):
        for carta in self.mazzo_carte:
            print(carta[1][0],' di ',carta[1][1], ' vale ' ,carta[0])
    def estrai(self):
        l_mazzo = len(self.mazzo_carte) - 1
        l_inizio = 0
        
        num_estratto = random.randint(l_inizio, l_mazzo)
        return self.mazzo_carte.pop(num_estratto)
    

class Giocatore:
    
    carte = []
    somma = 0
    def __init__(self,nome,carta):
        self.nome = nome
        self.carte.append(carta)
        self.somma += carta[0]
        
    def hit(self,carta):
        self.carte.append(carta)
        self.somma += carta[0]
        print("Hai totalizzato , ",self.somma," punti")
        if self.somma == 21:
            print("BlackJack!")
            return False,0
        elif self.somma > 21:
            print("Oh no ", self.nome, " hai sballato!")
            return False,1

            
class Mazziere:
    carte = []
    somma = 0
    def __init__(self,carta):
        self.carte.append(carta)
        self.somma +=carta[0]
        
    def hit(self,carta):
        self.carte.append(carta)
        self.somma += carta[0]
        if self.somma <= 17:
            #if True, keep hitting
            return True
        else:
            #else, stop
            return False
mazzo = Mazzo(2)
#for carta in mazzo.mazzo_carte:
#    print(carta[1][0],' di ',carta[1][1], ' vale ' ,carta[0])
# Ad ogni giocatore si estrae una carte, gli si chiede il nome e lo si assegna
carta = mazzo.estrai()

Davide = Giocatore("Davide",carta)
carta = mazzo.estrai()
Davide.hit(carta)
var = True
check = 0
while var != False:
    print("Ciao, ",Davide.nome," hai ", Davide.somma, " punti\n     ")
    scelta = int(input("Premi 0 per pescare o 1 per fermarti \n    "))
    if scelta == 0:
        carta = mazzo.estrai()
        var,check = Davide.hit(carta)
        
    else:
        var = False