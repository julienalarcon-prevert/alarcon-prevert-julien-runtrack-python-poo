class Ville:
    def __init__(self, nom, nbhabitant):
        self.__nom = nom
        self.__nbhabitant = nbhabitant
    
    def get_nb_habitant(self):
        return self.__nbhabitant

    def ajouter_habitant(self):
        self.__nbhabitant += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()
    
    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()
    

paris = Ville("Paris", 1_000_000)
print("Habitants à Paris :", paris.get_nb_habitant())

marseille = Ville("Marseille", 861_635)
print("Habitants à Marseille :", marseille.get_nb_habitant())

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


print("Habitants à Paris après arrivées :", paris.get_nb_habitant())
print("Habitants à Marseille après arrivées :", marseille.get_nb_habitant())

    