from tile_type import TileType


def smooth_edges(drawable, smooth_with_class_name):
    for x in range(0, drawable.width):
        for y in range(0, drawable.height):
            tile = drawable.tiles[x][y]
            if tile.tile_type == TileType.VOID:
                directions = [(i,j) for (i,j) in [(x+1, y), (x, y-1), (x-1, y), (x, y+1)] if (i >= 0 and j >= 0 and i < drawable.width and j < drawable.height)]
                h = 0
                for d in directions:
                    if drawable.tiles[d[0]][d[1]].tile_type == TileType.WALL:
                        h = h+1

                if h == 2:
                    drawable.tiles[x][y] = smooth_with_class_name()
