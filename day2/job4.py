class Student:
    def __init__(self, nom, prenom, num):
        self.__nom = nom
        self.__prenom = prenom
        self.__num = num
        self.__nbcredit = 0
        self.__level = self.__studentEval()
        
    def __studentEval(self):
        if self.__nbcredit >= 90:
            return "Excellent"
        elif self.__nbcredit >= 80:
            return "Très bien"
        elif self.__nbcredit >= 70:
            return "Bien"
        elif self.__nbcredit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
            
    def add_credits(self, value):
        if value > 0:
            self.__nbcredit += value
            self.__level = self.__studentEval()
        else:
            print("Erreur : Le nombre de crédit à ajouter doit être > 0")
            
    def get_credits(self):
        return self.__nbcredit

    def student_info(self):
        print(f"Nom: {self.__nom}\nPrénom: {self.__prenom}\nID: {self.__num}\nNiveau: {self.__level}")
