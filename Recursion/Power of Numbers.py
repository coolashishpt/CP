def power(N,R):
    #Your code here
    m = 1000000007
    if N == 0:
        return 1

    if N == 1:
        return N % m

    P = power(N, int(R/2))
    P = (P * P) % m
    if R % 2 == 0:
        return P
    else:
        return ((N % m) * P)%m


print(power(12))
