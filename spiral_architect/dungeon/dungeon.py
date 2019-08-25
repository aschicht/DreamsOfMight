from uuid import uuid4

from renderable import Renderable
from tile import Tile, VoidTile


class DungeonLevel(Renderable):
    def __init__(self, width, height, room_max_size, room_min_size, max_rooms):
        self.width = width
        self.height = height
        self.room_max_size = room_max_size
        self.room_min_size = room_min_size
        self.max_rooms = max_rooms
        self.tiles = self.initialize_tiles()
        self.entities = []

        self.initial_player_x = 0
        self.initial_player_y = 0
        self.id = uuid4()
        self.upward_stairs = {}
        self.downward_stairs = {}

    def initialize_tiles(self):
        tiles = [[VoidTile() for y in range(self.height)] for x in range(self.width)]

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
           return True, None
        blocking_entities = [entity for entity in self.entities if entity.x == x and entity.y == y]
        if any(blocking_entities):
            return True, blocking_entities[0]
        return False, None

    def handle_action(self, action):
        pass

    def get_tiles(self):
        return self.tiles

    def get_items(self):
        pass

    def get_entities(self):
        return self.entities

    def get_downward_stairs(self):
        return list(self.downward_stairs.values())

    def get_upward_stairs(self):
        return list(self.upward_stairs.values())

    def remove_entity(self, entity):
        self.entities.remove(entity)
