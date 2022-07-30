import math
from fractions import Fraction


def color_chance(total, this, choose):
    return 1 - Fraction(math.factorial(total - this) // math.factorial(total - this - choose), math.factorial(total) // math.factorial(total - choose))


def expected():
    return float(7 * color_chance(70, 10, 20))
