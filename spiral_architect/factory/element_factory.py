from tile import FloorTile, WallTile
from tile_type import TileType


def create_room(drawable, room):
    for x in range(room.x1, room.x2 + 1):
        for y in range(room.y1, room.y2 + 1):
            if (x == room.x1 or y == room.y1 or y == room.y2 or x == room.x2) \
                    and drawable.tiles[x][y].tile_type != TileType.FLOOR:
                drawable.tiles[x][y] = WallTile()
            else:
                drawable.tiles[x][y] = FloorTile()


def create_h_tunnel(drawable, x1, x2, y):
    for _y in [y - 1, y, y + 1]:
        for x in range(min(x1, x2)-1, max(x1, x2) + 2):
            if _y == y and not x > max(x1,x2) and not x < min(x1,x2):
                drawable.tiles[x][_y] = FloorTile()
            elif drawable.tiles[x][_y].tile_type != TileType.FLOOR:
                drawable.tiles[x][_y] = WallTile()


def create_v_tunnel(drawable, y1, y2, x):
    for _x in [x-1, x, x+1]:
        for y in range(min(y1, y2)-1, max(y1, y2) + 2):
            if _x == x and not y > max(y1,y2) and not y < min(y1,y2):
                drawable.tiles[_x][y] = FloorTile()
            elif drawable.tiles[_x][y].tile_type != TileType.FLOOR:
                drawable.tiles[_x][y] = WallTile()
