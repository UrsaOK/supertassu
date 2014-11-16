from kartta import *

class Taso:
    def __init__(self, vaikeus):

        self.kartta = Kartta()
        self.generoi()

        self.vaikeus = vaikeus
        self.spawn_vesi = False
        self.spawn_orkki = False
        self.spawn_apina = False
        self.spawn_huutaja = False
        self.spawn_hakkaaja = False
        self.helppo = False

    def alusta_hirviot(self): 
        if self.vaikeus == 1:
            self.helppo = True
        elif self.vaikeus == 2:
            self.spawn_vesi = True
        elif self.vaikeus == 3:
            self.spawn_vesi = True
            self.spawn_orkki = True
        elif self.vaikeus == 4:
            self.spawn_vesi = True
            self.spawn_orkki = True
            self.spawn_apina = True
        elif self.vaikeus == 5:
            self.spawn_vesi = True
            self.spawn_orkki = True
            self.spawn_apina = True
            self.spawn_huutaja = True
        elif self.vaikeus == 6:
            self.spawn_vesi = True
            self.spawn_orkki = True
            self.spawn_apina = True
            self.spawn_huutaja = True
            self.spawn_hakkaaja = True
        else:
            self.helppo = True

    def generoi(self):
    	self.kartta[20][20] = SEINA
