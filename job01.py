class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = TVA
    
    def calculerprixttc(self):
        return self.prixHT * (1 + self.tva / 100)
    
    def modifiernom(self, newnom):
        self.nom = newnom
        
    def modifierprix(self, newprix):
        self.prixHT = newprix
    
    def obtenirnom(self):
        return self.nom
    
    def obtenirprixht(self):
        return self.prixHT
    
    def obtenirtva(self):
        return self.tva
    
    def afficher(self):
        return f"Produit: {self.nom} | HT: {self.prixHT} | TVA: {self.tva}% | TTC: {self.calculerprixttc()}"
