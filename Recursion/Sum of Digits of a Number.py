def sum(n):
    if n == 0:
        return 0

    l = n // 10
    s = n % 10
    return s + sum(l)

print(sum(2345))