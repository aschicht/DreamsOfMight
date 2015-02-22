__author__ = 'rumm'

import libtcodpy as libtcod

def throw_dice(min, max):
    return libtcod.random_get_int(0, min, max)