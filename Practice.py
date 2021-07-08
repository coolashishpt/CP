def fun(s, n):
    if n == 0:
        return 0

    return int(s[n-1]) + fun(s, n - 1)


def fun1(n):
    if n ==0:
        return 0
    a = n % 10
    s = n//10
    return a + fun1(s)


print(fun("984", 3))
print(fun1(3))


