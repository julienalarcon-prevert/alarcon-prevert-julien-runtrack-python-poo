class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def set_details(self, marque=None, modele=None, annee=None):
        if marque: self.__marque = marque
        if modele: self.__modele = modele
        if annee: self.__annee = annee

    def get_etat_complet(self):
        return {
            "Marque": self.__marque,
            "Modèle": self.__modele,
            "Année": self.__annee,
            "KM": self.__kilometrage,
            "Réservoir": self.__reservoir,
            "En marche": self.__en_marche
        }

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre...")
        else:
            print("Panne d'essence : Réservoir trop bas !")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")
