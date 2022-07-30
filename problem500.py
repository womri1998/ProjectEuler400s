import math


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


primes = gen_primes(10 ** 6)


def divisors(n):
    res = (len(n)) ** n[-1]
    for i in range(1, len(n) - 1):
        res *= (i + 1) ** (n[i] - n[i + 1])
    return res


def next(n):
