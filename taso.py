from kartta import *
import random

class Taso:
    def __init__(self, vaikeus):

        self.kartta = Kartta()
#       self.kiinni = False
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
        p = (0, -1)
        e = (0, 1)
        i = (1, 0)
        l = (-1, 0)

        x = random.randint(1, 80)
        y = random.randint(1, 50)

    	for _ in range(50):
            self.kartta[x][y] = SUPERSEINA

            suunnat = (p, e, i, l)
            hyvyydet = (1, 1, 1, 1)

            suunta = chooseWeighted(suunnat, hyvyydet)

            xliiku, yliiku = suunta
            x += xliiku
            y += yliiku

def chooseWeighted(jutut, painotukset):
    summa = sum(painotukset)
    acc = 0

    valittu = random.random()

    for i, p in enumerate(painotukset):
        normalisoitu_paino = float(p) / summa
        acc += normalisoitu_paino
        if acc > valittu:
            return jutut[i]


