import zmq
class Tavolo: 
    #n_tavoli = [] #se volgiamo complicare il gioco
    giocatori = []
    info_giocatore_singolo = ["validazione" : False, "richiesta":"","indirizzo": "", "nome" : "", "soldi": ""]
    max_giocatori = 0
    def __init__(self):
        pass
    
    def scelta_metodo(self, diz_giocatore):
        #MANDA RICHIESTA: chiediamo la stringa bit (lista), la convertiamo 
        #in str e prendiamo il parametro "richiesta"
        #
        pass
    #in base alla richiesta (nel dizionario) di ogni giocatore, si procede con 
    #il metodo adeguato: validazione_player(bool), pescata(str), 
    def richiesta_giocatori():
        #MANDA RICHIESTA: per avviare un timer. Poi chiudi.
        #RICEVI RICHIESTA: per il max_giocatori con un for (ache il timer può 
        #mandare la richiesta per dire che l'utente non si è unito, vai avanti).
            #appeni info_giocatore_singolo ("indirizzo" e "nome") a giocatori
            #MANDA RICHIESTA: per un timer solo se non si arriva a max_giocatori
            #else  MANDA RICHIESTA abbaimo tutti i giocatori, il gioco può partire
        #return self.giocatori
        pass
    def 
        
        
    
class Mazziere:
    tutte_le_carte = []