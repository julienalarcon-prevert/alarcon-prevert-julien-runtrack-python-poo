class Personne:
    def __init__(self, age = 14):
        self.age = age
        
    def get_age(self):
        print (self.age)
        
    def bonjour(self):
        print("Hello")
    
    def set_age(self, value):
        self.age = value

class Eleve(Personne):
    def __init__(self):
        super().__init__(age=14)
    
    def aller_en_cours(self):
        print("Je vais en cours")
        
    def afficher_age(self):
        print(f"J'ai {self.age} ans ")

class Professeur(Personne):
    def __init__(self, matiere):
        super().__init__(age=40)
        self.__matiere = matiere
    
    def enseigner(self):
        print("Le cours va commencer")
