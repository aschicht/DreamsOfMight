
"""
Overlord is the dungeon controller
"""
from uuid import uuid4

from config import MAP_HEIGHT, MAP_WIDTH
from dungeon_type import DungeonType
from factory.dungeon_builder import DungeonLevelBuilder
from heimdall import Heimdall


class Overlord:

    def __init__(self):
        self.dungeon_levels = []
        self.dungeon_levels_by_id = {}
        self.id = uuid4()

    def build_dungeon(self):
        level_1 = DungeonLevelBuilder(DungeonType.SIMPLE, height=MAP_HEIGHT, width=MAP_WIDTH).with_room_sizes(6,10).with_max_rooms(30)\
            .with_upward_stairs(0).with_downward_stairs(1).build_dungeon_level()

        self.dungeon_levels.append(level_1)
        self.dungeon_levels_by_id[level_1.id] = level_1

        level_2 = DungeonLevelBuilder(DungeonType.SIMPLE, height=MAP_HEIGHT, width=MAP_WIDTH).with_room_sizes(6,10).with_max_rooms(30)\
            .with_upward_stairs(1).with_downward_stairs(0).build_dungeon_level()

        self.dungeon_levels.append(level_2)
        self.dungeon_levels_by_id[level_2.id] = level_2

        self.wire_levels(level_1, level_2)

    def wire_levels(self, upper_level, bottom_level):
        downward_stairs = upper_level.get_downward_stairs()
        upward_stairs = bottom_level.get_upward_stairs()

        Heimdall.add_gateway(downward_stairs[0].tile.id, self.id, bottom_level.id, upward_stairs[0].position)
        Heimdall.add_gateway(upward_stairs[0].tile.id, self.id, upper_level.id, downward_stairs[0].position)
