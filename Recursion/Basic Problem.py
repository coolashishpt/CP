def add(n):
    if n == 1:
        return 1

    return n + add(n - 1)


def sqr(n):
    if n == 0:
        return 1

    return 3 * sqr(n - 1)


print(add(5))
print(sqr(4))
