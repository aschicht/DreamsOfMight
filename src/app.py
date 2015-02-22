__author__ = 'rumm'

from dungeon.dungeon_factory import Dungeon_factory
import libtcodpy as libtcod
from config import MAP_WIDTH, MAP_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH


class App:
    def __init__(self):
        self.d_factory = Dungeon_factory()
        self.level = self.d_factory.build_dungeon()

    def run(self):
        libtcod.console_set_custom_font('celtic_garamond_10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'root', False)
        libtcod.sys_set_fps(20)
        con = libtcod.console_new(MAP_WIDTH, MAP_HEIGHT)
        i = 0
        while not libtcod.console_is_window_closed():

            #render the screen
            self.level.draw(con)

            libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
            libtcod.console_flush()

            #erase all objects at their old locations, before they move
            #for object in objects:
            #    object.clear()

            #handle keys and exit game if needed
            exit = self._handle_keys()
            i += 1
            print(i)
            if exit:
                break

    def _handle_keys(self):
        #key = libtcod.console_check_for_keypress()  #real-time
        key = libtcod.console_wait_for_keypress(True)  #turn-based

        if key.vk == libtcod.KEY_ENTER and key.lalt:
            #Alt+Enter: toggle fullscreen
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        elif key.vk == libtcod.KEY_ESCAPE:
            return True  #exit game


        elif key.vk == libtcod.KEY_SPACE:
            self.level = self.d_factory.build_dungeon()


            #movement keys
        #if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        #    player.move(0, -1)

        #elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        #    player.move(0, 1)

        #elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        #    player.move(-1, 0)

        #elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        #    player.move(1, 0)

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
