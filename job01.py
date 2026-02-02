class Operation:
    def __init__(self, n1=0, n2=0):
        self.nombre1 = n1
        self.nombre2 = n2
        
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat

operation = Operation(12, 5)

somme = operation.addition()
print(somme)