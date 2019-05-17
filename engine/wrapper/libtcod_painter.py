__author__ = 'rumm'

import tcod as libtcod

def paint_char(con, x, y, char, color, bk_color):
    #libtcod.console_set_default_foreground(con, color)
    #libtcod.console_put_char_ex(con, x, y, '#', libtcod.Color(255,255,255), libtcod.Color(0,0,0))
    libtcod.console_put_char_ex(con, x, y, char, color, bk_color)