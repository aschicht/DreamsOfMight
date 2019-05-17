__author__ = 'rumm'

class Dungeon_room:
    #a rectangle on the map. used to characterize a room.
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y
        self.doors = []


    def center(self):
        pass

    def intersect(self, other):
        pass
