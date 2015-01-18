from merkki import Merkki

class Ruutu:
    def __init__(self, merkki, tyhja):
        print("ruutu init")
        self.merkki = Merkki(merkki)
        self.tyhja = tyhja
   
OVI = Ruutu(".", True)
TYHJA = Ruutu(" ", True)
SEINA = Ruutu("#", False)
SUPERSEINA = Ruutu("?", False)

class Kartta(list):
    def __init__(self):
        print("kartta init")
        super(Kartta, self).__init__()
        self.leveys = 80
        self.korkeus = 50
        for x in range(self.leveys):
            self.append([TYHJA] * self.korkeus)


    def draw(self, mihin):
        print("kartta draw")
        for x in range(self.leveys):
            for y in range(self.korkeus):
                self[x][y].merkki.draw(mihin, x, y)

