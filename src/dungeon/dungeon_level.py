__author__ = 'rumm'

from mapable import Mapable


class Dungeon_level(Mapable):

    def __init__(self, width, height, id):
        Mapable.__init__(self, width, height, id)

        self.rooms = []
        self.room_num = 0

