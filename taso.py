from kartta import *
import random

class Taso:
    def __init__(self, vaikeus):

        print("taso init: luodaan kartta")
        self.kartta = Kartta()
        print("taso init: superseinita")
        self.superseinita()
        print("taso init: generoi")
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

    def superseinita(self):
        for y in range(50):
            self.kartta[0][y] = SUPERSEINA
        for x in range(80):
            self.kartta[x][0] = SUPERSEINA
        for y in range(50):
            self.kartta[79][y] = SUPERSEINA
        for x in range(80):
            self.kartta[x][49] = SUPERSEINA


    def generoi(self):
        p = (0, -1)
        e = (0, 1)
        i = (1, 0)
        l = (-1, 0)


        x = random.randint(1, 80-2)
        y = random.randint(1, 50-2)

        print("taso generoi: tuhannen looppi alkaa")

    	for _ in range(1000):
            self.kartta[x][y] = SEINA

            suunnat = (p, e, i, l)
            hyvyydet = []
            print("taso generoi: looppi: lasketaan painotukset ja piirretaan SEINAt")
            for s in suunnat:
                kohdex = s[0] + x
                kohdey = s[1] + y
                laskuri = 0
                if self.kartta[kohdex][kohdey] == SUPERSEINA:
                    hyvyydet.append(0)
                    continue
                for naapuri in suunnat:
                    naapurix = naapuri[0] + kohdex
                    naapuriy = naapuri[1] + kohdey
                    if self.kartta[naapurix][naapuriy] == SEINA:
                        laskuri += 1
                hyvyydet.append(5 - laskuri)

            suunta = chooseWeighted(suunnat, hyvyydet)

            xliiku, yliiku = suunta
            x += xliiku
            y += yliiku

        print("taso generoi: looppi loppui")    

def chooseWeighted(jutut, painotukset):
    summa = sum(painotukset)
    acc = 0

    valittu = random.random()

    for i, p in enumerate(painotukset):
        normalisoitu_paino = float(p) / summa
        acc += normalisoitu_paino
        if acc > valittu:
            return jutut[i]


