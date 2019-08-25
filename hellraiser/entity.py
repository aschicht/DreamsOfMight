from uuid import uuid4

from renderable import Drawable


class Entity(Drawable):
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