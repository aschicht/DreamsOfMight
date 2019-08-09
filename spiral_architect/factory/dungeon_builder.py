from dungeon.dungeon import Dungeon
from dungeon_type import DungeonType
from element.rectangle import Rectangle
from factory.element_factory import create_room, create_h_tunnel, create_v_tunnel
from random import randint

from factory.helper import smooth_edges
from tile import WallTile


class DungeonBuilder:
    def __init__(self, type, height=50, width=80):
        self.type = type
        self.height = height
        self.width = width
        self.max_rooms = 30
        self.room_max_size = 10
        self.room_min_size = 6
        self.rooms = []
        self.num_rooms = 0
        self.dungeon = None

    def _build_simple_dungeon(self):
        self.dungeon = Dungeon(self.width, self.height, self.room_max_size, self.room_min_size, self.max_rooms)

        for r in range(self.max_rooms):
            self._simple_dungeon_step()

        return self.dungeon

    def _build_simple_dungeon_in_steps(self):
        if not self.dungeon:
            self.dungeon = Dungeon(self.width, self.height, self.room_max_size, self.room_min_size, self.max_rooms)

        self._simple_dungeon_step()

        return self.dungeon

    def _simple_dungeon_step(self):
        # random width and height
        w = randint(self.room_min_size, self.room_max_size)
        h = randint(self.room_min_size, self.room_max_size)
        # random position without going out of the boundaries of the map
        x = randint(0, self.width - w - 1)
        y = randint(0, self.height - h - 1)
        # "Rect" class makes rectangles easier to work with
        new_room = Rectangle(x, y, w, h)
        # run through the other rooms and see if they intersect with this one
        for other_room in self.rooms:
            if new_room.intersect(other_room):
                break
        else:
            # this means there are no intersections, so this room is valid

            # "paint" it to the map's tiles
            create_room(self.dungeon, new_room)

            # center coordinates of new room, will be useful later
            (new_x, new_y) = new_room.center()

            if self.num_rooms == 0:
                # this is the first room, where the player starts at
                self.dungeon.initial_player_x = new_x
                self.dungeon.initial_player_y = new_y
            else:
                # all rooms after the first:
                # connect it to the previous room with a tunnel

                # center coordinates of previous room
                (prev_x, prev_y) = self.rooms[self.num_rooms - 1].center()

                # flip a coin (random number that is either 0 or 1)
                if randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    create_h_tunnel(self.dungeon, prev_x, new_x, prev_y)
                    create_v_tunnel(self.dungeon, prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(self.dungeon, prev_y, new_y, prev_x)
                    create_h_tunnel(self.dungeon, prev_x, new_x, new_y)

            # finally, append the new room to the list
            self.rooms.append(new_room)
            self.num_rooms += 1

    def build_dungeon(self):

        if self.type == DungeonType.SIMPLE:
            return self._build_simple_dungeon()

    def build_dungeon_in_steps(self):
        if self.type == DungeonType.SIMPLE:
            return self, self._build_simple_dungeon_in_steps()

    def with_max_rooms(self, max_rooms):
        self.max_rooms = max_rooms
        return self

    def with_room_sizes(self, min, max):
        self.room_max_size = max
        self.room_min_size = min
        return self