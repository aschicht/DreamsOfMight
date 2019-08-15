from heimdall import Heimdall
from overlord import Overlord
from world.world import World

"""
Dark Lord is the world controller
"""


class DarkLord:
    def __init__(self):

        self.world = World()
        self.overlords = {}

    def get_map_and_overlord(self, map_id):
        gateway_data = Heimdall.get_gateway(map_id)
        overlord = self.overlords.get(gateway_data.controller_id)
        return overlord, overlord.dungeon_levels_by_id.get(gateway_data.map_id), gateway_data.entry_point_position

    def build_dungeon(self):
        overlord = Overlord()
        overlord.build_dungeon()
        self.overlords[overlord.id] = overlord

    def get_dungeon_level(self):
        return list(self.overlords.values())[0].dungeon_levels[0]

    def get_overlord(self):
        return list(self.overlords.values())[0]
