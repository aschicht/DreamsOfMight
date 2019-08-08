from tile_color import TileColor
from tile_type import TileType


class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    def __init__(self, blocked, tile_type=TileType.VOID):
        self.blocked = blocked
        self.tile_type = tile_type

    def render(self):
        pass


class WallTile(Tile):

    def __init__(self):
        super().__init__(True, TileType.WALL)

    def render(self):
        return '#', TileColor.DARK_GREY


class VoidTile(Tile):

    def __init__(self,):
        super().__init__(True, TileType.VOID)

    def render(self):
        return ' ', TileColor.BLACK


class FloorTile(Tile):
    def __init__(self):
        super().__init__(False, TileType.FLOOR)

    def render(self):
        return '.', TileColor.WHITE