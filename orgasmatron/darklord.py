from config import MAP_HEIGHT, MAP_WIDTH
from dungeon_type import DungeonType
from factory.dungeon_builder import DungeonBuilder, DungeonLevelBuilder


"""
Dark Lord is the world controller
"""
class DarkLord:
    def __init__(self, challenge_raiting):
        self.challege_raiting = challenge_raiting

    def populate_room_with_monsters(self):
        pass

    def populate_room_with_items(self):
        pass

    def build_dungeon(self):
        dungeon = DungeonBuilder(self).with_dungeon_level_builders([
            DungeonLevelBuilder(DungeonType.SIMPLE, height=MAP_HEIGHT, width=MAP_WIDTH).with_room_sizes(6,10).with_max_rooms(30)
                .with_upward_stairs(1).with_downward_stairs(1)
        ]).build_dungeon()

        return dungeon