__author__ = 'rumm'

from cell import Cell
from DreamsOfMight.engine.wrapper import libtcod_painter
from DreamsOfMight.engine.wrapper import libtcod_color

class Mapable:
    def __init__(self, width, height, id):
        self.id = id
        self.width = width
        self.height = height
        self.map = [[
            Cell(x, y, ' ', libtcod_color.get_color(0,0,0))
            for y in range(height)]
            for x in range(width)
        ]

    def draw(self, con):

        for x in range(self.width):
            for y in range(self.height):

                cell = self.map[x][y]
                cell.draw(con)