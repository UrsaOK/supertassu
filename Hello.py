import libtcodpy as libtcod
import random
import traceback
import time
from taso import Taso
from liikkuja import Liikkuja
import getpass

####################################################################
#                     ROQUELIKE - BY SUPERTASSU                    #
#                       http://supertassu.org                      #
#                http://github.com/UrsaOK/supertassu               #
####################################################################

def main():

    #actual size of the window
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
     
    LIMIT_FPS = 20  #20 frames-per-second maximum

    raw_input("[INFO] Paina ENTER startataksesi.")

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
     
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'ROQUELIKE', False)
     
    libtcod.sys_set_fps(LIMIT_FPS)


    taso = Taso(0)
    pelaaja = Liikkuja(1, 1, '@', taso)

    print("[DEBUG] LOOPPI ALKAA")

    while not libtcod.console_is_window_closed():
     
        libtcod.console_set_default_foreground(0, libtcod.white)

        print("[DEBUG] DRAW FUNKTIOTA KUTSUTAAN")

        taso.kartta.draw(0)

        pelaaja.draw(0)
        libtcod.console_flush()

        print("[DEBUG] odotetaan nappulaa")

        nappula = libtcod.console_wait_for_keypress(True)

        print("[DEBUG] Nappula saatu")

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
        else:
            print("tuntematon nappain, ei virheita")

try:
    main()
except Exception,e:
    print traceback.print_exc()
    raw_input()
