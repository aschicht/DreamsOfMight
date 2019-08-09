from tile import FloorTile, WallTile


def create_room(drawable, room):
    # go through the tiles in the rectangle and make them passable
    for x in [room.x1, room.x2]:
        for y in [room.y1, room.y2]:
            if not isinstance(drawable.tiles[x][y], FloorTile):
                drawable.tiles[x][y] = WallTile()

    for x in range(room.x1, room.x2 + 1):
        for y in range(room.y1, room.y2 + 1):
            if x == room.x1 or y == room.y1 or y == room.y2 or x == room.x2:
                drawable.tiles[x][y] = WallTile()
            else:
                drawable.tiles[x][y] = FloorTile()


def create_h_tunnel(drawable, x1, x2, y):
    for _y in [y - 1, y, y + 1]:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if _y == y:
                drawable.tiles[x][_y] = FloorTile()
            elif not isinstance(drawable.tiles[x][_y], FloorTile):
                drawable.tiles[x][_y] = WallTile()


def create_v_tunnel(drawable, y1, y2, x):
    for _x in [x-1, x, x+1]:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if _x == x:
                drawable.tiles[_x][y] = FloorTile()
            elif not isinstance(drawable.tiles[_x][y], FloorTile):
                drawable.tiles[_x][y] = WallTile()
