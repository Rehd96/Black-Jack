import random
from collections import namedtuple
 

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
        #random.shuffle(self.mazzo_carte)

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
    
mazzo = Mazzo(1)
for carta in mazzo.mazzo_carte:
    print(carta[1][0],' di ',carta[1][1], ' vale ' ,carta[0])