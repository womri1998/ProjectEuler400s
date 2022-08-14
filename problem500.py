from fractions import Fraction
from math import log, ceil
from modulo import mod


MODULO = 500500507
TARGET = 2 ** 500500
PRINT_DISTANCE = 100


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


class MostDivisible:
    def __init__(self, primes: list[int]):
        self._primes = primes
        self.divisors = 1
        self.powers = [0]
        self.value = mod(1, MODULO)
        self.next_print = PRINT_DISTANCE

    def ratio(self, index: int) -> Fraction:
        ratio = Fraction(1, self._primes[index])
        power = self.powers[index]
        ratio *= Fraction(1, power + 1)
        return ratio

    def next(self):
        if self.powers[-1] != 0:
            self.powers.append(0)
        index = max((i for i in range(len(self.powers))), key=lambda i: self.ratio(i))
        self.divisors *= self.powers[index] + 2
        self.divisors //= self.powers[index] + 1
        self.value *= self._primes[index]
        self.powers[index] += 1

    def find_target(self, target: int) -> int:
        while self.divisors < target:
            self.next()
            if log(self.divisors, 2) > self.next_print:
                print(self.next_print)
                self.next_print += PRINT_DISTANCE
        return self.value.residue


def divisors(n):
    res = (len(n)) ** n[-1]
    for i in range(1, len(n) - 1):
        res *= (i + 1) ** (n[i] - n[i + 1])
    return res


def main():
    primes = gen_primes(10 ** 6)
    solver = MostDivisible(primes)
    print(solver.find_target(TARGET))


if __name__ == "__main__":
    main()
