class CompteBancaire:
    comptes = {}
    def __init__(self, nb_compte, nom, prenom, solde, decouvert):
        self.__nb_compte = nb_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
        decouvert = True
        CompteBancaire.comptes[nb_compte] = self
        
    def get_info(self):
        print(f"Nom : {self.__nom}  Prenom : {self.__prenom} Numéro de compte : {self.__nb_compte} Solde : {self.__solde}")
        
    def get_solde(self):
        return self.__solde
    
    def set_versement(self, value):
        self.__solde += value
        return self.__solde
    
    def set_retrait(self, value):
        if self.__solde <= 0 and self.__decouvert == False or self.__solde < self.__decouvert:
            print("Retrait impossible")
        else :
            self.__solde -= value
        return self.__solde
    
    def set_agios(self):
        if self.__solde <= 0:
            self.__solde - 5
        return self.__solde
    
    def set_virement(self, num_compte, value):
        if num_compte in CompteBancaire.comptes :
            destinataire = CompteBancaire.comptes[num_compte]
            destinataire.set_versement(value)
            print(f"Virement de {value} vers le compte {num_compte} effectuer")
        else :
            print("Numéro de compte inexistant")
    
    def set_virement_to_compte(self, num_compte, num_compte2, value):
        if num_compte in CompteBancaire.comptes :
            destinataire = CompteBancaire.comptes[num_compte]
            destinataire.set_versement(value)
            origin = CompteBancaire.comptes[num_compte2]
            origin.set_retrait(value)
            print(f"{origin} a fait un virement de {value} vers le compte {num_compte} effectuer")
        else :
            print("Numéro de compte inexistant")
            