import collections
from enum import Enum
from random import randint

InnerDice = collections.namedtuple('InnerDice', ['dice_quantity', 'dice_sides', 'position'])

class DiceClass(Enum):

    _1D2 = InnerDice(dice_quantity=1, dice_sides=2, position=0)
    _1D4 = InnerDice(dice_quantity=1, dice_sides=2, position=1)
    _1D6 = InnerDice(dice_quantity=1, dice_sides=2, position=2)
    _1D8 = InnerDice(dice_quantity=1, dice_sides=2, position=3)
    _2D4 = InnerDice(dice_quantity=1, dice_sides=2, position=4)
    _1D10 = InnerDice(dice_quantity=1, dice_sides=2, position=5)
    _1D12 = InnerDice(dice_quantity=1, dice_sides=2, position=6)
    _2D6 = InnerDice(dice_quantity=1, dice_sides=2, position=7)
    _3D4 = InnerDice(dice_quantity=1, dice_sides=2, position=8)
    _2D8 = InnerDice(dice_quantity=1, dice_sides=2, position=9)
    _4D4 = InnerDice(dice_quantity=1, dice_sides=2, position=10)
    _3D6 = InnerDice(dice_quantity=1, dice_sides=2, position=11)
    _1D20 = InnerDice(dice_quantity=1, dice_sides=2, position=12)
    _2D10 = InnerDice(dice_quantity=1, dice_sides=2, position=13)
    _5D4 = InnerDice(dice_quantity=1, dice_sides=2, position=14)
    _2D12 = InnerDice(dice_quantity=1, dice_sides=2, position=15)
    _3D8 = InnerDice(dice_quantity=1, dice_sides=2, position=16)
    _4D6 = InnerDice(dice_quantity=1, dice_sides=2, position=17)
    _6D4 = InnerDice(dice_quantity=1, dice_sides=2, position=18)
    _7D4 = InnerDice(dice_quantity=1, dice_sides=2, position=19)
    _3D10 = InnerDice(dice_quantity=1, dice_sides=2, position=20)
    _5D6 = InnerDice(dice_quantity=1, dice_sides=2, position=21)
    _4D8 = InnerDice(dice_quantity=1, dice_sides=2, position=22)
    _8D4 = InnerDice(dice_quantity=1, dice_sides=2, position=23)

    dice_progression = [_1D2, _1D4, _1D6, _1D8, _2D4, _1D10, _1D12, _2D6, _3D4, _2D8, _4D4, _3D6, _1D20, _2D10, _5D4,
                        _2D12, _3D8, _4D6, _6D4, _7D4, _3D10, _5D6, _4D8, _8D4]


class Dice:

    def __init__(self, dice_class):
        self.dice_class = dice_class

    def roll(self, modifier):
        r = 0
        for i in range(self.dice_class.value.dice_quantity):
            r = r + randint(0, self.dice_class.value.dice_sides)
        r = r + modifier
        return r if r >= 0 else 0
