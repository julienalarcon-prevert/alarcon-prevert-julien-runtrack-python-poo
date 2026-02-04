class Tache:
    def __init__(self, titre, description, status="à faire"):
        self.titre = titre
        self.description = description
        self.status = status

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée.")
        
    def supprimerTache(self, titre_recherche):
        for t in self.taches:
            if t.titre == titre_recherche:
                self.taches.remove(t)
                print(f"Tâche '{titre_recherche}' supprimée.")
                return
        print("Erreur : Titre introuvable pour suppression.")

    def marquerCommeFinie(self, titre_recherche):
        for t in self.taches:
            if t.titre == titre_recherche:
                t.status = "terminer"
                print(f"La tâche '{titre_recherche}' est marquée comme finie.")
                return
        print("Erreur : Titre introuvable.")
        
    def afficherListe(self):
        print("\n--- Liste de toutes les tâches ---")
        for t in self.taches:
            print(f"[{t.status}] {t.titre} : {t.description}")
        return self.taches

    def filterListe(self, statut_filtre):
        resultat = []
        for t in self.taches:
            if t.status == statut_filtre:
                resultat.append(t)
        
        print(f"\n--- Tâches avec le statut : {statut_filtre} ---")
        for t in resultat:
            print(f"[{t.status}] {t.titre}")
        return resultat

t1 = Tache("Courses", "Acheter du pain")
t2 = Tache("Sport", "Faire 30min de cardio")
t3 = Tache("Ménage", "Passer l'aspirateur")

ma_gestion = ListeDeTaches()

ma_gestion.ajouterTache(t1)
ma_gestion.ajouterTache(t2)
ma_gestion.ajouterTache(t3)

ma_gestion.supprimerTache("Ménage")

ma_gestion.marquerCommeFinie("Sport")

ma_gestion.afficherListe()

ma_gestion.filterListe("à faire")