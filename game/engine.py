import tcod as libtcod

from dungeon_type import DungeonType
from factory.dungeon_factory import make_dungeon
from input_handlers import handle_keys
from hellraiser.someone import Someone
from render_functions import clear_all, render_all
from spiral_architect.dungeon.dungeon import Dungeon


class Engine:

    def run(self):
        screen_width = 80
        screen_height = 50
        map_width = 80
        map_height = 45

        player = Someone(int(screen_width / 2), int(screen_height / 2), '@', libtcod.blue)
        npc = Someone(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
        entities = [npc, player]

        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

        con = libtcod.console_new(screen_width, screen_height)

        dungeon = make_dungeon(DungeonType.SIMPLE, map_width, map_height)
        player.x = dungeon.initial_player_x
        player.y = dungeon.initial_player_y

        key = libtcod.Key()
        mouse = libtcod.Mouse()

        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

            render_all(con, entities, dungeon, screen_width, screen_height)
            libtcod.console_flush()

            clear_all(con, entities)

            action = handle_keys(key)

            move = action.get('move')
            exit = action.get('exit')
            fullscreen = action.get('fullscreen')

            if move:
                dx, dy = move
                if not dungeon.is_blocked(player.x + dx, player.y + dy):
                    player.move(dx, dy)
            if exit:
                return True

            if fullscreen:
                libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
