class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        
    def get_info_vehicule(self):
        print(f"Marque : {self.marque} Modele : {self.modele} Année : {self.annee} Prix : {self.prix}")
        
    def demarrer(self):
        print("Attention, je roule")
        

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, porte=4):
        super().__init__(marque, modele, annee, prix)
        self.porte = porte
        
    def get_new_info(self):
        super().get_info_vehicule()
        print(f"{self.porte}")
    
    def demarrer(self):
        print("Attention la voiture roule")
        
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue
    
    def get_info_moto(self):
        super().get_info_vehicule()
        print(f"{self.roue}")
        
    def demarrer(self):
        print("Attention la moto roule")