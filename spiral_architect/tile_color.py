from collections import namedtuple
from enum import Enum


Color = namedtuple('Color', ['value', 'displayString', 'rgb'])


class TileColor(Enum):

    BLACK = Color(0, 'BLACK', (0, 0, 0))
    WHITE = Color(1, 'WHITE', (255, 255, 255))
    DARK_GREY = Color(2, 'DARK_GREY', (64, 64, 64))
    LIGHT_ORANGE = Color(3, 'LIGHT_ORANGE', (255, 166, 77))
    LIGHT_RED = Color(4, 'LIGHT_RED', (230, 115, 0))
    LIGHT_GREY = Color(5, 'LIGHT_GREY', (128, 128, 128))
    DARK_BLUE = Color(6, 'DARK_BLUE', (38, 38, 115))
