__author__ = 'rumm'

from DreamsOfMight.game.drawable import Drawable

class Cell(Drawable):
    def __init__(self, x, y, char, color):
        Drawable.__init__(self, x, y, char, color)
        self.block = False

