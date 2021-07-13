def pow(n, p):
    if p == 0:
        return 1

    pow(n, p - 1)
    return n ** p


print(pow(2, 9))


