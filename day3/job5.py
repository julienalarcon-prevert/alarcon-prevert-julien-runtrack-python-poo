import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
        
    def attaquer(self, adversaire):
        degats = random.randint(10, 20)
        adversaire.vie -= degats
        
        if adversaire.vie < 0:
            adversaire.vie = 0
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats}")
        
    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisir_lvl(self):
        print("Choisisez la difficulté (1: Facile, 2: Moyen 3: Difficile)")
        choix = input("Entrez le numéro de votre choix")
        
        self.niveau = choix
    
    def verif_sante(self, p1, p2):
        print(f"{p1.nom} a {p1.vie} point de vie")
        print(f"{p2.nom} a {p2.vie} points de vie")
        
    def verif_winner(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("L'ennemi a gagné !")
        elif ennemi.vie <= 0:
            print("Le joueur a gagné")
        else : 
            return 0
    
    def launch_game(self):
        self.choisir_lvl()
        
        if self.niveau == "1":
            joueur = Personnage("Heros", 100)
            ennemi = Personnage("Goblin", 50)
        
        if self.niveau == "2":
            joueur = Personnage("Héros", 100)
            ennemi = Personnage("Orc", 100)
        
        if self.niveau == "3":
            joueur = Personnage("Héros", 80)
            ennemi = Personnage("Chef Orc", 100)
        
        print(f"\n Le combat commence contre {ennemi.nom}")
            
        while joueur.est_vivant() and ennemi.est_vivant():
            input("\n Appuyez sur entrée pour attaquer")
            joueur.attaquer(ennemi)
            
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            
            self.verif_sante(joueur, ennemi)
            
        self.verif_winner(joueur, ennemi)
    
mon_jeu = Jeu()
mon_jeu.launch_game()