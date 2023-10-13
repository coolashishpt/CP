from GCD_HCF import GCD


def LCM(numOne, numTwo):

    return (numOne * numTwo) // GCD(numOne, numTwo).optimizedGCD()

print(LCM(4, 6))
