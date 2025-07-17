# Creer une classe Cercle qui se definit par :
# Un rayon
# Une methode aire (pi r carre)
# Une methode perimetre (2 pi r)

import math

class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon

    def aire(self):
        return (self.rayon*math.pi)**2
    
    def perimetre(self):
        return 2*self.rayon*math.pi
    
cercle_5 = Cercle(5.00)

print(cercle_5.aire())
print(cercle_5.perimetre())