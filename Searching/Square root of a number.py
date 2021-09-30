def floorsqrt(x):
    if x == 1 or x == 0:
        return x

    elif x == 2:
        return 1

    else:
        for i in range(2, x):

            if (i ** 2) == x:

                return i

            elif i ** 2 > x:
                return i - 1

def sqrt(n):

    low = 0
    high = n

    while low <= high:

        mid = (low + high) // 2

        if mid ** 2 > n:
            high = mid -1

        else:
            if mid ** 2 == n or (mid ** 2 < n < (mid + 1) ** 2):
                return mid

            else:
                low = mid + 1

print(floorsqrt(5))
