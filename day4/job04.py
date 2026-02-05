class Forme:
    def __init__(self, ):
        pass
    
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, larg, long):
        super().__init__()
        self.larg = larg
        self.long = long
    
    def aire(self):
        return self.long * self.larg
