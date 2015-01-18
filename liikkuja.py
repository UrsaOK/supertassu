from merkki import Sprite

class Liikkuja(Sprite):
    def __init__(self, x, y, merkki, taso):
        print("liikkuja init")
        super(Liikkuja, self).__init__(x, y, merkki)
        self.taso = taso

    def liiku(self, suunta):
        print("liikkuja liiku")
        uusix = self.x + suunta[0]
        uusiy = self.y + suunta[1]
        if self.taso.kartta[uusix][uusiy].tyhja:
            self.x = uusix
            self.y = uusiy
            return True
        else:
            return False