__author__ = 'rumm'

import libtcodpy as libtcod

def get_color(r,g,b):
    return libtcod.Color(r,g,b)

def get_black():
    return get_color(0,0,0)

def get_white():
    return get_color(255,255,255)
