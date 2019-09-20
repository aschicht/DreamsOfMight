import math


def distance_to(origin, target):
    dx = target.x - origin.x
    dy = target.y - origin.y
    return math.sqrt(dx ** 2 + dy ** 2)
