def largest(n):
    for i in range(1, n):
        if (i ** 2 + i) % n == 0:
            print((-1 * i) % n)
