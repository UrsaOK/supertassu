import libtcodpy as libtcod
import random
import time

class Merkki:
    def __init__(self, x, y, merkki):
        self.x = x
        self.y = y
        self.merkki = merkki
    def draw(self, mihin):
        libtcod.console_put_char(mihin, self.x, self.y, self.merkki, libtcod.BKGND_NONE)

class Ruutu:
    def __init__(self, merkki, tyhja):
        self.merkki = merkki
        self.tyhja = tyhja

OVI = Ruutu(".", True)
TYHJA = Ruutu(" ", True)
SEINA = Ruutu("#", False)
SUPERSEINA = Ruutu("?", False)
class Kartta(list):
    def __init__(self):
        super(Kartta, self).__init__()
        self.leveys = 80
        self.korkeus = 50
        for x in range(self.leveys):
            self.append([TYHJA] * self.korkeus)


    def draw(self):
        for x in range(self.leveys):
            for y in range(self.korkeus):
                libtcod.console_put_char(0, x, y, self[x][y].merkki, libtcod.BKGND_NONE)


class Generoi:
    def __init__(self, vaikeus):
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

#    def piirra(self):

 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
 
LIMIT_FPS = 20  #20 frames-per-second maximum
 

print("[INFO] Tervetuloa peliin.")
time.sleep(1)
print("[INFO] Sammuta peli painamalla ESC.")
x = raw_input("[INFO] Paina ENTER startataksesi.")

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
 
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROQUELIKE', False)
 
libtcod.sys_set_fps(LIMIT_FPS)

# time.sleep(10)

print("[INFO] Setting Full Screen")

libtcod.console_set_fullscreen(True)


pelaaja = Merkki(1, 1, '@')

kartta = Kartta()

while not libtcod.console_is_window_closed():
 
    libtcod.console_set_default_foreground(0, libtcod.white)

    kartta.draw()

    pelaaja.draw(0)
    libtcod.console_flush()

    nappula = libtcod.console_wait_for_keypress(True)

    if nappula.vk == libtcod.KEY_ESCAPE:
        break
    elif nappula.vk == libtcod.KEY_RIGHT:
        pelaaja.x += 1
        time.sleep(0.1)
    elif nappula.vk == libtcod.KEY_LEFT:
        pelaaja.x -= 1
        time.sleep(0.1)
    elif nappula.vk == libtcod.KEY_UP:
        pelaaja.y -= 1
        time.sleep(0.1)
    elif nappula.vk == libtcod.KEY_DOWN:
        pelaaja.y += 1
        time.sleep(0.1) 