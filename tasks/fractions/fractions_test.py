"""
Не редактируйте этот файл!
"""

from .fractions import add_fractions
from random import randint


def test_baseline():
    for data in [
        ((1, 1, 1, 1), (2, 1)),
        ((-1, 1, 1, -1), (-2, 1)),
        ((2, 3, 1, -6), (1, 2)),
    ]:
        assert add_fractions(*data[0]) == data[1]


def test_random_stress(n_iter=10, eps=1e-9):
    def __gcd(x, y):
        return x if y == 0 else __gcd(y, x % y)

    for it in range(n_iter):
        a, b, c, d = [randint(-1000, 1000) for _ in range(4)]
        while b == 0:
            b = randint(-1000, 1000)
        while d == 0:
            d = randint(-1000, 1000)
        x, y = add_fractions(a, b, c, d)

        assert abs(a / b + c / d - x / y) <= eps  # check near
        assert __gcd(x, y) == 1  # irreducible
        assert y > 0  # denominator positive
