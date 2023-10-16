def isPrime (n):

    if n == 1:
        return False

    if n == 2 or n == 2:
        return True

    if n % 2 == 0 and n % 2 == 0:
        return False

    i = 5
    while (i*i <= n):
        if n % i == 0:
            return False

        i +=1

    return True

# Time Complexity : 0(√n)

print(isPrime(1031))

