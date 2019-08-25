from entity import Entity
from renderable import RenderData


class Monster(Entity):

    def __init__(self, char, color):
        super().__init__(char, color)


    def render(self, **kargs):
        return RenderData(self.char, foreground_light_color=self.color, foreground_dark_color=self.color, background_light_color=(0,0,0), background_dark_color=(0,0,0))
