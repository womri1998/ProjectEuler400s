from math import atan, pi, cos, sin


def norm_and_angle(a, b):
    return (a ** 2 + b ** 2) ** 0.5, atan(a / b)


def antiderivative_cos_4(x):
    return (12 * x + 8 * sin(2 * x) + sin(4 * x)) / 32


def result(a, b):
    r, theta = norm_and_angle(a, b)
    res = 2 * pi / 3 * r ** 3
    first = cos(theta) * (cos(theta) ** 4 - 2 * cos(pi / 2 + 2 * theta) ** 4 + cos(pi + theta) ** 4) / 4
    second = sin(theta) * (2 * antiderivative_cos_4(pi / 2 + 2 * theta) - antiderivative_cos_4(theta) - antiderivative_cos_4(pi + theta))
    return res * (first + second)
