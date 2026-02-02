class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return f"je m'appelle {self.nom} {self.prenom}"
        
personne1 = Personne("Alarcon prevert", "Julien")  

print(personne1.SePresenter())