# Naive Solution
def trailingZeros(nums):

    res = 1
    for num in range(2, nums+1):
        res *= num
    print(res)
    ans = 0
    while res > 0:
        if res % 10 == 0:
            ans += 1
        else:
            break

        res = res // 10

    return ans

# Optimize Solution

def trailingZerosOptimizeV1(nums):
    res = 0
    while nums >= 5:
        nums //= 5
        res += nums

    return res
print(trailingZeros(50))

print(trailingZerosOptimizeV1(50))
