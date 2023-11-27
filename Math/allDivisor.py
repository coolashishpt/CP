def printAllDivisors(num):

    for divisor in range(1, num+1):
        if num % divisor == 0:
            print(divisor, end=" ")


print(printAllDivisors(100))
