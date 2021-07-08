def count(n):
    if n < 10:
        return 1
    l = n // 10
    s = n % 10
    return len([s]) + count(l)


print(count(112231))
