from uuid import uuid4

from tile import Tile, VoidTile


class DungeonLevel:
    def __init__(self, width, height, room_max_size, room_min_size, max_rooms):
        self.width = width
        self.height = height
        self.room_max_size = room_max_size
        self.room_min_size = room_min_size
        self.max_rooms = max_rooms
        self.tiles = self.initialize_tiles()

        self.initial_player_x = 0
        self.initial_player_y = 0
        self.id = uuid4()

    def initialize_tiles(self):
        tiles = [[VoidTile() for y in range(self.height)] for x in range(self.width)]

        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False

    def handle_action(self, action):
        pass


class Dungeon:
    def __init__(self, overlord):
        self.dungeon_levels=[]
        self.dungeon_levels_by_id = {}
        self.overlord = overlord
        self.current_level = 0
        self.id = uuid4()

    def add_dungeon_level(self, dungeon_level):
        self.dungeon_levels_by_id[dungeon_level.id] = dungeon_level
        self.dungeon_levels.append(dungeon_level)

