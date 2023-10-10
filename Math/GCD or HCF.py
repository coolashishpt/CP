def gcd(numOne, numTwo):

    if numOne > numTwo:
        numOne, numTwo = numTwo, numOne

    if numTwo % numOne == 0:
        return numOne

    ans = 1
    for num in range(1, numOne):
        print("Here")
        if numTwo % num == 0 and numOne % num == 0:
            if num > ans:
                ans = num

    return ans


def optimizedGCD(numOne, numTwo):
    if numTwo == 0:
        return numOne

    return optimizedGCD(numTwo, numOne%numTwo)


if __name__ == "__main__":
    a = 12
    b = 15
    print(gcd(a, b))
    print(optimizedGCD(a, b))
