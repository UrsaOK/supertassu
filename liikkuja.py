from merkki import Merkki

class Liikkuja(Merkki):
    def __init__(self, x, y, merkki, taso):
        super(self, Liikkuja).__init__(x, y, merkki)
        self.taso = taso

    def liiku(self, suunta):
        uusix = self.x + suunta[0]
        uusix = self.y + suunta[1]
        if self.taso.kartta[uusix][uusiy].tyhja:
            self.x = uusix
            self.y = uusiy
            return True
        else:
            return False