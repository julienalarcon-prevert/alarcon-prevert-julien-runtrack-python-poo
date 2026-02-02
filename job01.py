class Animal():
    def __init__(self, age = 0, prenom = "" ):
        self.age = age
        self.prenom = prenom
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()

print(f"Age initial : {mon_animal.age}")

mon_animal.vieillir()
print(f"Age après avoir vieilli: {mon_animal.age}")

mon_animal.nommer("Ouki")
print(f"Le prenom de l'animal est: {mon_animal.prenom}")