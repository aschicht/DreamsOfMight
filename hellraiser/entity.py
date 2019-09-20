from uuid import uuid4

from combat_manager import Combatable
from renderable import Drawable


class Entity(Drawable, Combatable):
    """
    A generic object to represent players, enemies, etc.
    """
    def __init__(self, char, color, x=0, y=0):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.id = uuid4()

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def render(self, **kargs):
        pass

    def get_hit_dice(self):
        pass

    def get_hit_modifier(self):
        pass

    def get_defense(self):
        pass

    def get_protection(self):
        pass

    def take_action(self, engine_model):
        pass