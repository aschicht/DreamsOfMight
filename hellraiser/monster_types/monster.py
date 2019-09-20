import tcod as libtcod

import utils
from entity import Entity
from renderable import RenderData


class Monster(Entity):

    def __init__(self, char, color, hit_dice, hit_mod, defense, protection):
        super().__init__(char, color)
        self.hit_points = 0
        self.hit_dice = hit_dice
        self.hit_modifier = hit_mod
        self.defense = defense
        self.protection = protection


    def render(self, **kargs):
        return RenderData(self.char, foreground_light_color=self.color, foreground_dark_color=self.color, background_light_color=(0,0,0), background_dark_color=(0,0,0))

    def get_hit_dice(self):
        return self.hit_dice

    def get_hit_modifier(self):
        return self.hit_modifier

    def get_defense(self):
        return self.defense

    def get_protection(self):
        return self.protection

    def take_action(self, engine_model):
        if libtcod.map_is_in_fov(engine_model.fov_map, self.x, self.y):

            if utils.distance_to(self, engine_model.player) >= 2:
                self.move_astar(engine_model.player, engine_model.current_map.entities, engine_model.current_map)

            elif engine_model.player.hit_points > 0:
                pass

    def move_towards(self, x, y, game_map, entities):
        pass

    def move_astar(self, target, entities, game_map):
        # Create a FOV map that has the dimensions of the map
        fov = libtcod.map_new(game_map.width, game_map.height)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                libtcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].block_sight,
                                           not game_map.tiles[x1][y1].blocked)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function anyway
        for entity in entities:
            if entity.blocks and entity != self and entity != target:
                # Set the tile as a wall so it must be navigated around
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = libtcod.path_new_using_map(fov, 1.41)

        # Compute the path between self's coordinates and the target's coordinates
        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        # The path size matters if you want the monster to use alternative longer paths (for example through other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if there's an alternative path really far away
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self's coordinates to the next path tile
                self.x = x
                self.y = y
        else:
            # Keep the old move function as a backup so that if there are no paths (for example another monster blocks a corridor)
            # it will still try to move towards the player (closer to the corridor opening)
            self.move_towards(target.x, target.y, game_map, entities)

            # Delete the path to free memory
        libtcod.path_delete(my_path)