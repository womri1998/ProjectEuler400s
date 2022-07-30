def evens(n):
    if n < 2:
        return 0
    elif n < 4:
        return 1
    elif n == 4:
        return 2
    else:
        return both(n // 2)


def unevens(n):
    if n < 3:
        return 1
    elif n < 5:
        return 4
    else:
        off = n % 4 == 1 or n % 4 == 2
        if off:
            off = exact(n - (n % 4 - 1)) + 3 * ((n - 3) // 4 == 0)
        return 5 * (unevens((n - 3) // 4 * 2 + 1) - 1) - 3 * both((n - 3) // 4) + off + 4


def both(n):
    return evens(n) + unevens(n)


def exact(n):
    if n == 1:
        return 1
    elif n == 3:
        return 3
    elif n % 2 == 0:
        return exact(n // 2)
    elif n % 4 == 1:
        return 2 * exact((n - 1) // 2 + 1) - exact((n - 1) // 4)
    else:
        return 3 * exact((n - 3) // 2 + 1) - 2 * exact((n - 3) // 4)
