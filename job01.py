class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficherpoints(self):
        print(f"Cooordonnées : ({self.x}, {self.y})")
    
    def prtX(self):
        print(f"Coordonnées de X : {self.x}")
    
    def prtY(self):
        print(f"Coordonnées de Y : {self.y}")
    
    def newX(self, newX):
        self.x = newX

    def newY(self, newY):
        self.x = newY
        
point1 = Point(10, 20)
point1.afficherpoints()

point1.newX(50)
point1.prtX()