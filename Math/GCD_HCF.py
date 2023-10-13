class GCD:
    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def gcd(self):

        if self.numOne > self.numTwo:
            self.numOne, self.numTwo = self.numTwo, self.numOne

        if self.numTwo % self.numOne == 0:
            return self.numOne

        ans = 1
        for num in range(1, self.numOne):
            if self.numTwo % num == 0 and self.numOne % num == 0:
                if num > ans:
                    ans = num

        return ans

    def optimizedGCD(self):
        """
        # optimized way to find GCD

        def func(n1, n2):
            if n2 == 0:
                return n1

            return func(n2, n1 % n2)

        """
        if self.numTwo == 0:
            return self.numOne

        Recursive = GCD(self.numTwo, self.numOne % self.numTwo)
        return Recursive.optimizedGCD()


if __name__ == "__main__":
    a = 27
    b = 15
    G = GCD(a, b)
    print(G.gcd())
    print(G.optimizedGCD())
