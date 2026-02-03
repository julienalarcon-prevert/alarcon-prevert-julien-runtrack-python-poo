class Rectangle: 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def set_long(self, value):
        if value > 0:
            self.__longueur = value
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, value):
        if value > 0:
            self.__largeur = value
