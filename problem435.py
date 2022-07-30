from decimal import *


getcontext().prec = 50


def seq_sum(a1, q, n, m):
    if q < 0:
        if n % 2 == 1:
            return (a1 + seq_sum(a1 * (q + q ** 2), q ** 2, n // 2, m)) % m
        else:
            return seq_sum(a1 * (1 + q), q ** 2, n // 2, m)
    res = a1 / (q - 1)
    i = 1
    j = q % m
    while i <= n:
        if n & i != 0:
            res = res * j % m
        i *= 2
        j = j ** 2 % m
    return (res - a1 / (q - 1)) % m


sqrt5 = Decimal(5) ** Decimal(0.5)
phi = (1 + sqrt5) / 2
psi = (1 - sqrt5) / 2


def f(n, x, m):
    return (seq_sum(x * phi / sqrt5, x * phi, n, m) + seq_sum(-1 * x * psi / sqrt5, x * psi, n, m)) % m


def g(n, x, m):
    return round(sum([f(n, i, m) for i in range(1, x + 1)]) % m)


def iter_squaring(x, n, m, s):
    res = s
    i = 1
    j = x % m
    while i <= n:
        if n & i != 0:
            res = res * j % m
        i *= 2
        j = j ** 2 % m
    return res


def seq_sum2(a1, q, n, m):
    if q < 0:
        if n % 2 == 1:
            return (a1 + seq_sum(a1 * (q + q )))
    return (iter_squaring(q, n, m, a1 / (q - 1)) - a1 / (q - 1)) % m


def fib(n):
    return (phi ** n - psi ** n) / sqrt5


def f2(n, x, m):
    return sum([fib(i) * x ** i for i in range(1, n + 1)]) % m
