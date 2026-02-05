class Joueur:
    def __init__(self, nom, numero, position, nb_but, nb_passed, crtj, crtr):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_but = nb_but
        self.nb_passed = nb_passed
        self.crtj = crtj
        self.crtr = crtr
    
    def set_but(self):
        self.nb_but += 1
    
    def set_passed(self):
        self.nb_passed += 1
    
    def  set_crtj(self):
        self.crtj += 1
        
    def set_crtr(self):
        self.crtr += 1
        
    def get_info(self):
        return print (f"\nNom : {self.nom},\n numéro : {self.numero},\n position : {self.position},\n but marqués : {self.nb_but},\n passe décisives : {self.nb_passed},\n Carton jaune : {self.crtj},\n carton rouge : {self.crtr}")
    
class Equipe:
    def __init__(self, nom, liste = None):
        self.nom = nom
        if liste is None:
            self.liste = []
        else : 
            self.liste = liste
            
    def add_joueur(self, new_player):
        self.liste.append(new_player)
    
    def afficher_stat_joueur(self):
        for joueur in self.liste:
            joueur.get_info()
    
    def new_stats(self, name_joueur, action):
        for joueur in self.liste:
            if joueur.nom == name_joueur:
                if action == "but":
                    joueur.set_but()
                elif action == "pass":
                    joueur.set_passed()
                elif action == "jaune":
                    joueur.set_crtj()
                elif action == "Rouge":
                    joueur.set_crtr()
                else : 
                    print("Choix impossible")
    