from dice import DiceClass, Dice
from entity import Entity
from renderable import RenderData


class Player(Entity):

    def __init__(self, char, color):
        super().__init__(char, color)
        self.hit_points = 0

    def render(self, **kargs):
        return RenderData(self.char, foreground_light_color=self.color, foreground_dark_color=self.color, background_light_color=(0,0,0), background_dark_color=(0,0,0))

    def get_hit_dice(self):
        return Dice(DiceClass._1D6)

    def get_hit_modifier(self):
        return 1

    def get_damage_dice(self):
        return Dice(DiceClass._1D4)

    def get_damage_modifier(self):
        return 0

    def get_defense(self):
        return 3

    def get_protection(self):
        return 1