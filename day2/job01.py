class Livre:
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nbpages(self):
        return self.__nbpages
    
    def set_titre(self, nwtitre):
        self.__titre = nwtitre
    
    def set_auteur(self, nwauteur):
        self.__auteur = nwauteur
    
    def set_nbpages(self, nwnbpages):
        if isinstance(nwnbpages, int) and nwnbpages > 0:
            self.__nbpages = nwnbpages
        else:
            print("Error : Must use integer")
        