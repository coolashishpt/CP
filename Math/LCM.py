from GCD_HCF import GCD

def LCM(numOne, numTwo):

    return (numOne * numTwo) // GCD.optimizedGCD(numOne, numTwo)

print(LCM(4, 6))
