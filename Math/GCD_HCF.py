class GCD():
    def gcd(numOne, numTwo):

        if numOne > numTwo:
            numOne, numTwo = numTwo, numOne

        if numTwo % numOne == 0:
            return numOne

        ans = 1
        for num in range(1, numOne):
            if numTwo % num == 0 and numOne % num == 0:
                if num > ans:
                    ans = num

        return ans


    def optimizedGCD(numOne, numTwo):
        if numTwo == 0:
            return numOne

        return GCD.optimizedGCD(numTwo, numOne%numTwo)


if __name__ == "__main__":
    a = 27
    b = 15
    print(GCD.gcd(a, b))
    print(GCD.optimizedGCD(a, b))
