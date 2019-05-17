__author__ = 'rumm'

import tcod as libtcod

def throw_dice(min, max):
    return libtcod.random_get_int(0, min, max)