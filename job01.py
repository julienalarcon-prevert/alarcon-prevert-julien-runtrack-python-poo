import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changer_rayon(self, new_rayon):
        self.rayon = new_rayon
    
    def afficher_infos(self):
        print(f"Cercle de rayon : {self.rayon}")
    
    def diametre(self):
        return self.rayon * 2
    
    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon * self.rayon)
    
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)
