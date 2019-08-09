from drawable import RenderData, Drawable
from tile_color import TileColor
from tile_type import TileType

class Tile(Drawable):
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    def __init__(self, blocked, block_sight=True, tile_type=TileType.VOID):
        self.blocked = blocked
        self.tile_type = tile_type
        self.block_sight = block_sight
        self.explored = False

    def render(self, **kargs):
        pass


class WallTile(Tile):

    def __init__(self):
        super().__init__(True, True, TileType.WALL)

    def render(self, **kargs):
        return RenderData('#', TileColor.DARK_GREY, TileColor.DARK_GREY, TileColor.BLACK, TileColor.BLACK)


class VoidTile(Tile):

    def __init__(self,):
        super().__init__(True, True, TileType.VOID)

    def render(self, **kargs):
        return RenderData(' ', TileColor.BLACK, TileColor.BLACK, TileColor.BLACK, TileColor.BLACK)


class FloorTile(Tile):
    def __init__(self):
        super().__init__(False, False, TileType.FLOOR)

    def render(self, **kargs):
        return RenderData('.', TileColor.LIGHT_ORANGE, TileColor.WHITE, TileColor.BLACK, TileColor.BLACK)