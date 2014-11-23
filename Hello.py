import libtcodpy as libtcod
import random
import traceback
import time
from taso import Taso
from liikkuja import Liikkuja

def main():

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

#    libtcod.console_set_fullscreen(True)


    taso = Taso(0)
    pelaaja = Liikkuja(1, 1, '@', taso)


    while not libtcod.console_is_window_closed():
     
        libtcod.console_set_default_foreground(0, libtcod.white)

        taso.kartta.draw(0)

        pelaaja.draw(0)
        libtcod.console_flush()

        nappula = libtcod.console_wait_for_keypress(True)

        if nappula.vk == libtcod.KEY_ESCAPE:
            return
        elif nappula.vk == libtcod.KEY_RIGHT:
            pelaaja.liiku((1, 0))
        elif nappula.vk == libtcod.KEY_LEFT:
            pelaaja.liiku((-1, 0))
        elif nappula.vk == libtcod.KEY_UP:
            pelaaja.liiku((0, -1))
        elif nappula.vk == libtcod.KEY_DOWN:
            pelaaja.liiku((0, 1))

try:
    main()
except Exception,e:
    print traceback.print_exc()
    raw_input()
