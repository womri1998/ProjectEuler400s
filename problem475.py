was = {}


def f(n, m):  # n % 12 == 0
    trios, pairs, singles = n // 3, 0, 0
    return options(trios, pairs, singles, m)


def options(t, p, s, m):
    if (t, p, s) in was:
        return was[(t, p, s)]
    result = 0
    if t != 0 and s != 0:
        result += (4 * s * options(t - 1, p, s - 1, m)) % m  # 3 to a trio, 1 to a single
    if t != 0 and p != 0:
        result += (4 * p * options(t - 1, p - 1, s + 1, m)) % m  # 3 to a trio, 1 to a pair
        result += (6 * p * options(t - 1, p - 1, s + 1, m)) % m  # 2 to a trio, 2 to a pair
    if p > 1 and s != 0:
        result += (12 * p * (p - 1) * options(t, p - 2, s)) % m  # 2 to a pair, 1 to another, and 1 to a single
    if p > 2 and s != 0:
        result += (24 // 6 * p * (p - 1) * (p - 2) * options(t, p - 3, s + 2, m)) % m  # 1 to each of 3 pairs, 1 to a single
    if p > 1:
        result += (6 * p * (p - 1) // 2 * options(t, p - 2, s, m)) % m  # 2 to each of 2 different pairs
    if t > 1:
        result += (4 * options(t - 2, p - 1, s, m)) % m  # 3 to 1 trio, 1 to another trio
        result += (3 * options(t - 2, p, s - 2, m)) % m  # 2 to each of 2 different trios
    
    x = result % m
    was[(t, p, s)] = x
    return x
