import tcod as libtcod

from dungeon_type import DungeonType
from factory.dungeon_builder import DungeonBuilder
from field_of_view import initialize_fov, recompute_fov
from input_handlers import handle_keys
from hellraiser.someone import Someone
from render_functions import clear_all, render_all, render_all_without_fov


class Engine:

    def run(self):
        screen_width = 160
        screen_height = 80
        map_width = 160
        map_height = 70
        fov_recompute = True

        player = Someone(int(screen_width / 2), int(screen_height / 2), '@', libtcod.blue)
        entities = [player]

        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

        con = libtcod.console_new(screen_width, screen_height)

        dungeon = DungeonBuilder(DungeonType.SIMPLE, map_height, map_width)\
                        .with_max_rooms(30)\
                        .with_room_sizes(6, 10)\
                        .build_dungeon()

        fov_map = initialize_fov(dungeon)
        player.x = dungeon.initial_player_x
        player.y = dungeon.initial_player_y

        key = libtcod.Key()
        mouse = libtcod.Mouse()

        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

            if fov_recompute:
                recompute_fov(fov_map, player.x, player.y, 10)

            render_all(con, entities, dungeon, screen_width, screen_height, fov_recompute, fov_map)
            fov_recompute = False

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
                    fov_recompute = True
            if exit:
                return True

            if fullscreen:
                libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    def run_step_dungeon(self):
        screen_width = 160
        screen_height = 80
        map_width = 160
        map_height = 70

        player = Someone(int(screen_width / 2), int(screen_height / 2), '@', libtcod.blue)
        entities = [player]

        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)

        con = libtcod.console_new(screen_width, screen_height)

        builder, dungeon = DungeonBuilder(DungeonType.SIMPLE, map_height, map_width)\
                    .with_max_rooms(30)\
                    .with_room_sizes(6,10)\
                    .build_dungeon_in_steps()

        player.x = dungeon.initial_player_x
        player.y = dungeon.initial_player_y

        key = libtcod.Key()
        mouse = libtcod.Mouse()

        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

            render_all_without_fov(con, entities, dungeon, screen_width, screen_height)
            libtcod.console_flush()

            clear_all(con, entities)

            action = handle_keys(key)

            move = action.get('move')
            exit = action.get('exit')
            fullscreen = action.get('fullscreen')
            step = action.get('step')

            if step:
                builder.build_dungeon_in_steps()

            if move:
                dx, dy = move
                if not dungeon.is_blocked(player.x + dx, player.y + dy):
                    player.move(dx, dy)
            if exit:
                return True

            if fullscreen:
                libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
