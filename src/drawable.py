__author__ = 'rumm'

from wrapper import libtcod_painter, libtcod_color


#abstract class defining behaviour for a drawable object
class Drawable:

    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color


    def draw(self, con):
        libtcod_painter.paint_char(con, self.x, self.y, self.char, self.color, libtcod_color.get_black())

    def clear(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

