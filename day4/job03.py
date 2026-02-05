class Rectangle:
    def __init__(self, long, larg):
        self._long = long
        self._larg = larg
    
    def perimetre(self):
        peri = (self._larg + self._long) * 2
        print(f"Perimetre : {peri}")
        
    def surface(self):
        surface = self._larg * self._long
        print(f"Surface : {surface}")
    
    def set_longeur(self, value):
        self._long = value
        
    def set_larg(self, value):
        self._larg = value
    
    def get_value(self):
        print(f"Longueur : {self._long} Largeur : {self._larg}")
        

class Parallelepipede(Rectangle):
    def __init__(self, long, larg, hauteur):
        super().__init__(long, larg)
        self.hauteur = hauteur
        
    def volume(self):
        volume = (self._long * self._larg * self.hauteur)
        print(f"Volume : {volume}")
        
