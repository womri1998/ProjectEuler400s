def iter_squaring(x, y, m):
    res = 1
    i = 1
    j = x % m
    while i <= y:
        if y & i != 0:
            res = mod_mul(res, j, m)
        i *= 2
        j = mod_mul(j, j, m)
    return res


def mod_mul(x, y, m):
    res = 0
    i = 1
    j = x % m
    while i <= y:
        if y & i != 0:
            res += j
            res %= m
        i *= 2
        j *= 2
        j %= m
    return res


def factorial_mod(n, m):
    res = 1
    for i in range(2, n + 1):
        res = mod_mul(res, i, m)
    return res


was = {}


def t(n, i):
    if i == 7 or i == -1:
        return 0
    elif n == 0:
        return 1
    elif (n, i) in was:
        return was[(n, i)]
    else:
        #x = sum([t(n - 1, i) for i in range(1, i + 1)]) + (7 - i) * t(n - 1, i + 1)
        x = t(n, i - 1) + (7 - i) * t(n - 1, i + 1) - (7 - i) * t(n - 1, i + 1)
        was[(n, i)] = x
        return x

#t(n, 0) = 7 * t(n - 1, 1)
#if 7 > i > 0: t(n, i) = t(n, i - 1) + (7 - i) * t(n - 1, i + 1) - (7 - i) * t(n - 1, i + 1)
