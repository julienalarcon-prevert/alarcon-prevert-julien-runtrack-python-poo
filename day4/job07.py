import random

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur
        
    def get_valeur(self):
        return 0
class CarteNumber(Carte):
    def __init__(self, couleur, valeur):
        super().__init__(couleur, valeur)
    
    def get_valeur(self):
        return int(self.valeur)

class Figure(Carte):
    def __init__(self, couleur, valeur):
        super().__init__(couleur, valeur)
    
    def get_valeur(self):
        return 10
    
class As(Carte):
    def __init__(self, couleur, valeur):
        super().__init__(couleur, valeur)
    
    def get_valeur(self):
        return 11
        
class Jeu:
    def __init__(self):
        self.couleur = ["Coeur", "Carreau", "Trèfle", "Pique"]
        self.valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.paquet = []
        
    def creer_paquet(self):
        for c in self.couleur:
            for v in self.valeur:
                if v in ["Valet", "Dame", "Roi"]:
                    self.paquet.append(Figure(c,v))
                elif v == "As":
                    self.paquet.append(As(c, v))
                else : 
                    self.paquet.append(CarteNumber(c, v))
    
    def shuffle(self):
        random.shuffle(self.paquet)          
    
    def distrib(self):
        return self.paquet.pop()          

class Hand:
    def __init__(self):
        self.carte = []
        
    def add_carte(self, carte):
        self.carte.append(carte)
        
    def get_valeur(self):
        score = 0
        nb_as = 0
        
        for c in self.carte:
            score += c.get_valeur()
            if isinstance(c, As):
                nb_as += 1
        
        while score > 21 and nb_as > 0:
            score -= 10
            nb_as -= 1
        return score
    
class Main:
    def __init__(self):
        self.mon_jeu = Jeu()
        self.mon_jeu.creer_paquet()
        self.mon_jeu.shuffle()
        
        self.main_joueur = Hand()
        self.main_croupier = Hand()
    
    def play(self):
        for i in range(2):
            self.main_joueur.add_carte(self.mon_jeu.distrib())
            self.main_croupier.add_carte(self.mon_jeu.distrib())
            
        while self.main_joueur.get_valeur() < 21:
            print(f"Votre score ", self.main_joueur.get_valeur())
            reponse = input("Voulez vous (T)irer ou (R)ester")
            
            if reponse == "T":
                self.main_joueur.add_carte(self.mon_jeu.distrib())
            elif reponse == "R":
                break
        
        if self.main_joueur.get_valeur() > 21:
            print("Score : ", self.main_joueur.get_valeur())
        
        if self.main_joueur.get_valeur() <= 21:
            while self.main_croupier.get_valeur() < 17:
                self.main_croupier.add_carte(self.mon_jeu.distrib())
                
        score_j = self.main_joueur.get_valeur()
        score_c = self.main_croupier.get_valeur()
        
        print(f"Score final -> Joueur = ", score_j, "Croupier : ", score_c)
        
        if score_j > 21:
            print("Vous avez perdu")
            
        elif score_c > 21:
            print("Le croupier a perdu")
            
        elif score_j > score_c:
            print("Vous avez gagné")
        
        elif score_j < score_c:
            print("Le croupier a gagné")
            
        else : 
            print("Egalité")
            
partie = Main()
partie.play()