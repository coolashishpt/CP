def primFactor(num):

    divisor = 2
    arr = []
    while divisor <= num:
        if num % divisor == 0:
            num = num // divisor
            arr.append(divisor)
        else:
            divisor += 1

    return arr

print(primFactor(1031))
