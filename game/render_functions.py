import tcod as libtcod


def render_all(con, entities, game_map, screen_width, screen_height):
    # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            tile = game_map.tiles[x][y]
            libtcod.console_set_char_background(con, x, y, libtcod.black, libtcod.BKGND_SET)
            libtcod.console_set_default_foreground(con, tile.render()[1].value.rgb)
            libtcod.console_put_char(con, x, y, tile.render()[0], libtcod.BKGND_NONE)

    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)