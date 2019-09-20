import collections
from enum import Enum

import tcod as libtcod

from combat_manager import CombatManager


class HandlerType(Enum):
    MAP_HANDLER = 0
    INVENTORY_HANDLER = 1


class InputHandlerActionType(Enum):
    CLEAR_STACK = 0
    NEED_MORE_EVENTS = 1
    SWITCH_TO_MAP_CONSOLE = 2
    SWITCH_TO_INVENTORY_CONSOLE = 3
    ACTION = 4

class ActionType(Enum):
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    USE = 4
    QUIT = 5
    DUNGEON_STEP = 6
    TRAVEL = 7


InputHandlerAction = collections.namedtuple('InputHandlerAction', ['action_type', 'action'])


class ConsoleEventHandler:

    def handle_event(self, event_stack):
        pass


class ConsoleActionHandler:

    def handle_action(self, action):
        pass


class InputHandler:
    def __init__(self, engine_model):
        self.engine_model = engine_model
        self.current_event_handler = HandlerType.MAP_HANDLER
        self.event_stack = []
        self.handlers = {
            HandlerType.MAP_HANDLER: MapConsoleHandler(engine_model)
        }
        #TODO: add event and action history for post mortem

    def handle_keys(self, key):

        self.event_stack.append(key)
        input_handler_action = self.handlers[self.current_event_handler].handle_event(self.event_stack)

        if input_handler_action.action_type == InputHandlerActionType.CLEAR_STACK:
            self.event_stack.clear()
        elif input_handler_action.action_type == InputHandlerActionType.SWITCH_TO_MAP_CONSOLE:
            pass
        elif input_handler_action.action_type == InputHandlerActionType.SWITCH_TO_INVENTORY_CONSOLE:
            pass
        elif input_handler_action.action_type == InputHandlerActionType.ACTION:
            self.event_stack.clear()
            self.handlers[self.current_event_handler].handle_action(input_handler_action.action)


class MapConsoleHandler(ConsoleEventHandler, ConsoleActionHandler):

    def __init__(self, engine_model):
        self.engine_model = engine_model
        self.one_key_dict = {
            (libtcod.KEY_UP) : ActionType.MOVE_UP,
            (libtcod.KEY_DOWN): ActionType.MOVE_DOWN,
            (libtcod.KEY_LEFT): ActionType.MOVE_LEFT,
            (libtcod.KEY_RIGHT): ActionType.MOVE_RIGHT,
            (libtcod.KEY_ESCAPE): ActionType.QUIT,
        }

    def handle_event(self, event_stack):
        action = None
        if self.one_key_dict.get(event_stack[0].vk):
            action = self.one_key_dict[event_stack[0].vk]
            return InputHandlerAction(InputHandlerActionType.ACTION, action)

        if event_stack[0].vk == libtcod.KEY_CHAR:
            if chr(event_stack[0].c) == 'u':
                return InputHandlerAction(InputHandlerActionType.ACTION, ActionType.USE)
            if chr(event_stack[0].c) == '<':
                return InputHandlerAction(InputHandlerActionType.ACTION, ActionType.TRAVEL)

        return InputHandlerAction(InputHandlerActionType.CLEAR_STACK, None)

    def handle_action(self, action):

        if action == ActionType.MOVE_UP or action == ActionType.MOVE_DOWN or action == ActionType.MOVE_LEFT \
                or action == ActionType.MOVE_RIGHT:
            self.move_player(action)
        elif action == ActionType.QUIT:
            self.engine_model.exit = True
        elif action == ActionType.USE:
            print("use")
        elif action == ActionType.TRAVEL:
            gateway_tile = self.engine_model.current_map.tiles[self.engine_model.player.x][self.engine_model.player.y]
            self.engine_model.switch_map(gateway_tile.id)

    def move_player(self, action):
        player = self.engine_model.player
        map = self.engine_model.current_map
        dx = 0
        dy = 0
        if action == ActionType.MOVE_UP:
            dy = -1
        elif action == ActionType.MOVE_DOWN:
            dy = 1
        elif action == ActionType.MOVE_LEFT:
            dx = -1
        elif action == ActionType.MOVE_RIGHT:
            dx = 1

        blocked, entity = map.is_blocked(player.x + dx, player.y + dy)
        if not blocked:
            player.move(dx, dy)
            self.engine_model.fov_recompute = True
        elif entity:
            self.attack(player, entity)
        else:
            print('Ouch!')

    def attack(self, player, entity):
        damage = CombatManager.fight(player, entity)
        if damage == 0:
            pass
        elif entity.hit_points - damage <= 0:
            print('killed')
            self.engine_model.current_map.entities.remove(entity)
            self.engine_model.fov_recompute = True
        else:
            print('It is still standing!')
            entity.hit_points = entity.hit_points - damage
