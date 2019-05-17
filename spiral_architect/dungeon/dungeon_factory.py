__author__ = 'rumm'

from DreamsOfMight.spiral_architect.dungeon.dungeon_level import Dungeon_level
from DreamsOfMight.engine.wrapper import dice
from dungeon_rect_room import Dungeon_rect_room
from cell import Cell
from DreamsOfMight.engine.wrapper import libtcod_color
from DreamsOfMight.game.config import MAP_HEIGHT, MAP_WIDTH


class Dungeon_factory:

    def __init__(self):
        pass

    def build_dungeon(self):
        dungeon_level = Dungeon_level(MAP_WIDTH, MAP_HEIGHT, "1")

        for r in range(3):
            #random width and height
            w = dice.throw_dice(5, 12)
            h = dice.throw_dice(5, 12)
            #random position without going out of the boundaries of the map
            x = dice.throw_dice(1, dungeon_level.width - w - 2)
            y = dice.throw_dice(1, dungeon_level.height - h - 2)

            #"Rect" class makes rectangles easier to work with
            new_room = Dungeon_rect_room(x, y, w, h)

            #run through the other rooms and see if they intersect with this one
            failed = False
            for other_room in dungeon_level.rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break

            if not failed:
                #this means there are no intersections, so this room is valid

                #"paint" it to the map's tiles
                self._create_room(dungeon_level.map, new_room)

                #center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                if dungeon_level.room_num != 0:
                    #all rooms after the first:
                    #connect it to the previous room with a tunnel

                    #center coordinates of previous room
                    (prev_x, prev_y) = dungeon_level.rooms[dungeon_level.room_num-1].center()

                    #draw a coin (random number that is either 0 or 1)
                    if dice.throw_dice(0, 1) == 1:
                        #first move horizontally, then vertically
                        self._create_h_tunnel(dungeon_level.map, prev_x, new_x, prev_y)
                        self._create_v_tunnel(dungeon_level.map, prev_y, new_y, new_x)
                    else:
                        #first move vertically, then horizontally
                        self._create_v_tunnel(dungeon_level.map, prev_y, new_y, prev_x)
                        self._create_h_tunnel(dungeon_level.map, prev_x, new_x, new_y)
                    self.clear_room(dungeon_level.rooms[dungeon_level.room_num - 1], dungeon_level.map)
                #finally, append the new room to the list
                dungeon_level.rooms.append(new_room)
                dungeon_level.room_num += 1

        self.clear_room(dungeon_level.rooms[dungeon_level.room_num - 1], dungeon_level.map)
        return dungeon_level

    def clear_room(self, room, map):
        for x in range(room.x1 + 1, room.x2 - 1):
            for y in range(room.y1 + 1, room.y2 - 1):
                map[x][y].char = '.'


    def _create_h_tunnel(self, map, x1, x2, y):
        #horizontal tunnel. min() and max() are used in case x1>x2
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map[x][y + 1].blocked = False
            map[x][y + 1].block_sight = False
            map[x][y - 1].blocked = False
            map[x][y - 1].block_sight = False
            map[x][y + 1].char = '#'
            map[x][y - 1].char = '#'
            map[x][y + 1].color = libtcod_color.get_white()
            map[x][y - 1].color = libtcod_color.get_white()
            map[x][y].color = libtcod_color.get_white()
            map[x][y].char = '.'


    def _create_v_tunnel(self, map, y1, y2, x):
        #vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map[x + 1][y].blocked = False
            map[x + 1][y].block_sight = False
            map[x - 1][y].blocked = False
            map[x - 1][y].block_sight = False
            map[x + 1][y].char = '#'
            map[x - 1][y].char = '#'
            map[x + 1][y].color = libtcod_color.get_white()
            map[x - 1][y].color = libtcod_color.get_white()
            map[x][y].color = libtcod_color.get_white()
            map[x][y].char = '.'


    def _create_room(self, map, room):
        for x in range(room.x1, room.x2):
            for y in range(room.y1, room.y2):
                map[x][y]= Cell(x, y, '.', libtcod_color.get_white())

        for x in range(room.x1, room.x2):
            cell = Cell(x, room.y1, '#', libtcod_color.get_white())
            cell.block = True
            map[x][room.y1] = cell

            cell = Cell(x, room.y2, '#', libtcod_color.get_white())
            cell.block = True
            map[x][room.y2] = cell

        for y in range(room.y1, room.y2+1):
            cell = Cell(room.x1, y, '#', libtcod_color.get_white())
            cell.block = True
            map[room.x1][y] = cell

            cell = Cell(room.x2, y, '#', libtcod_color.get_white())
            cell.block = True
            map[room.x2][y] = cell
