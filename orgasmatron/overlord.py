from dungeon_type import DungeonType
from factory.dungeon_builder import DungeonBuilder, DungeonLevelBuilder


class DungeonOverlord:
    def __init__(self, challenge_raiting):
        self.challege_raiting = challenge_raiting

    def populate_room_with_monsters(self):
        pass

    def populate_room_with_items(self):
        pass

    def build_dungeon(self):
        dungeon = DungeonBuilder(self).with_dungeon_level_builders([
            DungeonLevelBuilder(DungeonType.SIMPLE, height=90, width=160).with_room_sizes(6,10).with_max_rooms(30)
        ]).build_dungeon()

        return dungeon