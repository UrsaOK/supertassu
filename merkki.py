import libtcodpy as libtcod

class Merkki(object):
    def __init__(self, merkki):
        self.merkki = merkki
    def draw(self, puskuri, x, y):
        libtcod.console_put_char(puskuri, x, y, self.merkki, libtcod.BKGND_NONE)

class Sprite(Merkki):
    def __init__(self, x, y, merkki):
        super(Sprite, self).__init__(merkki)
        self.x = x
        self.y = y

    def draw(self, puskuri):
    	super(Sprite, self).draw(puskuri, self.x, self.y)
