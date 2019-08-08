from dungeon.dungeon import Dungeon
from dungeon_type import DungeonType
from element.rectangle import Rectangle
from factory.element_factory import create_room, create_h_tunnel, create_v_tunnel
from random import randint


def _make_simple_dungeon(dungeon_width, dungeon_height, room_max_size=10, room_min_size=6, max_rooms=30):
    dungeon = Dungeon(dungeon_width, dungeon_height, room_max_size, room_min_size, max_rooms)

    rooms = []
    num_rooms = 0

    for r in range(max_rooms):
        # random width and height
        w = randint(room_min_size, room_max_size)
        h = randint(room_min_size, room_max_size)
        # random position without going out of the boundaries of the map
        x = randint(0, dungeon_width - w - 1)
        y = randint(0, dungeon_height - h - 1)

        # "Rect" class makes rectangles easier to work with
        new_room = Rectangle(x, y, w, h)

        # run through the other rooms and see if they intersect with this one
        for other_room in rooms:
            if new_room.intersect(other_room):
                break
        else:
            # this means there are no intersections, so this room is valid

            # "paint" it to the map's tiles
            create_room(dungeon, new_room)

            # center coordinates of new room, will be useful later
            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                # this is the first room, where the player starts at
                dungeon.initial_player_x = new_x
                dungeon.initial_player_y = new_y
            else:
                # all rooms after the first:
                # connect it to the previous room with a tunnel

                # center coordinates of previous room
                (prev_x, prev_y) = rooms[num_rooms - 1].center()

                # flip a coin (random number that is either 0 or 1)
                if randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    create_h_tunnel(dungeon, prev_x, new_x, prev_y)
                    create_v_tunnel(dungeon, prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(dungeon, prev_y, new_y, prev_x)
                    create_h_tunnel(dungeon, prev_x, new_x, new_y)

                # finally, append the new room to the list
            rooms.append(new_room)
            num_rooms += 1


    return dungeon


def make_dungeon(dungeon_type, dungeon_width, dungeon_height):

    if dungeon_type == DungeonType.SIMPLE:
        return _make_simple_dungeon(dungeon_width, dungeon_height)
