class Livre:
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = True
        
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
            
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre {self.__titre} à été emprunté")
        else : 
            print(f"{self.__titre} à été emprunté")
            
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"le livre {self.__titre} à été rendu")
        else:
            print(f"Ce live est déja présent")
            