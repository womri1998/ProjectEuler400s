import math


input = "thereisasyetinsufficientdataforameaningfulanswer"


def to_dict(w):
    d = {}
    for c in w:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def arrangments(a):
    res = math.factorial(sum(a))
    for x in a:
        res //= math.factorial(x)
    return res


def lex_ord(w, d):
    for c in w[:-1]:
        d[c] -= 1
    count = 0
    for c in d:
        if ord(c) < ord(w[-1]) and d[c] > 0:
            d2 = d.copy()
            d2[c] -= 1
            print(d, '\n', d2, '\n', w[:-1] + c)
            count += arrangments(d2.values())
    return count
