import tcod as libtcod

from actionable import Action
from dungeon_type import DungeonType
from factory.dungeon_builder import DungeonLevelBuilder
from field_of_view import initialize_fov, recompute_fov
from handlers.input_handlers import InputHandler
from hellraiser.someone import Someone
from darklord import DarkLord
from render_functions import clear_all, render_all, render_all_without_fov
from tile_type import TileType
from world.world import World


class EngineModel:
    def __init__(self):
        self.screen_width = 160
        self.screen_height = 80
        self.map_width = 160
        self.map_height = 70
        self.fov_recompute = True
        self.player = Someone(int(self.screen_width / 2), int(self.screen_height / 2), '@', libtcod.blue)
        self.entities = [self.player]
        self.world = World()
        self.dungeon = DarkLord(1).build_dungeon()
        self.current_map = self.dungeon.dungeon_levels[0]
        self.fov_map = initialize_fov(self.dungeon.dungeon_levels[0])
        self.input_handler = InputHandler(self)
        self.exit = False

class Engine:

    def __init__(self):
        self.model = EngineModel()

    def run(self):

        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(self.model.screen_width, self.model.screen_height, 'libtcod tutorial revised', False)

        con = libtcod.console_new(self.model.screen_width, self.model.screen_height)

        self.model.player.x = self.model.dungeon.dungeon_levels[0].initial_player_x
        self.model.player.y = self.model.dungeon.dungeon_levels[0].initial_player_y

        key = libtcod.Key()
        mouse = libtcod.Mouse()

        while not libtcod.console_is_window_closed():

            if self.model.fov_recompute:
                recompute_fov(self.model.fov_map, self.model.player.x, self.model.player.y, 10)

            render_all(con, self.model.entities, self.model.dungeon.dungeon_levels[0], self.model.screen_width,
                       self.model.screen_height, self.model.fov_recompute, self.model.fov_map)

            self.model.fov_recompute = False

            clear_all(con, self.model.entities)

            libtcod.console_flush()
            libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)
            self.model.input_handler.handle_keys(key)

            if self.model.exit:
                return True

    def run_step_dungeon(self):
        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        libtcod.console_init_root(self.model.screen_width, self.model.screen_height, 'libtcod tutorial revised', False)

        con = libtcod.console_new(self.model.screen_width, self.model.screen_height)

        self.model.player.x = self.model.dungeon.dungeon_levels[0].initial_player_x
        self.model.player.y = self.model.dungeon.dungeon_levels[0].initial_player_y

        builder, dungeon = DungeonLevelBuilder(DungeonType.SIMPLE, self.model.map_height, self.model.map_width)\
                    .with_max_rooms(30)\
                    .with_room_sizes(6,10)\
                    .build_dungeon_level_in_steps()

        key = libtcod.Key()
        mouse = libtcod.Mouse()

        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

            render_all_without_fov(con, self.model.entities, dungeon, self.model.screen_width, self.model.screen_height)

            clear_all(con, self.model.entities)
            libtcod.console_flush()
            libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)

            if key.vk == libtcod.KEY_SPACE:
                builder.build_dungeon_level_in_steps()

            # if move:
            #     dx, dy = move
            #     if not dungeon.is_blocked(player.x + dx, player.y + dy):
            #         player.move(dx, dy)
            if exit:
                return True

            # if fullscreen:
            #     libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
