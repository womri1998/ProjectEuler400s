was = {}

# er = even remaining, ur = uneven remaining
def options(er, ur, dif):
    if (tuple(er), tuple(ur), dif) in was:
        return was[(tuple(er), tuple(ur), dif)]
    left = sum(er + ur)
    if left == 0:
        if dif == 0:
            return 1
        else:
            return 0
    tot = 0
    for i in range(5):
        if er[i] != 0:
            temp = er.copy()
            temp[i] -= 1
            tot += options(temp, ur.copy(), (dif + 2 * i * (-1) ** left) % 11)
        if ur[i] != 0:
            temp = ur.copy()
            temp[i] -= 1
            tot += options(er.copy(), temp, (dif + (1 + 2 * i) * (-1) ** left) % 11)
    was[(tuple(er), tuple(ur), dif)] = tot
    return tot


def result():
    res = 0
    er = [2] * 5
    ur = [2] * 5
    for i in range(1, 5):
        temp = er.copy()
        temp[i] -= 1
        res += options(temp, ur, 2 * i)
    for i in range(5):
        temp = ur.copy()
        temp[i] -= 1
        res += options(er, temp, 1 + 2 * i)
    return res
