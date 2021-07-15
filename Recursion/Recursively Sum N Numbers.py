def Rsum(n):
    if n == 0:
        return 0

    return n + Rsum(n-1)

print(Rsum(4))