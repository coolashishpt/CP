def nCr(n, r):
    if n == r or r == 0:
        return 1

    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(4,1))