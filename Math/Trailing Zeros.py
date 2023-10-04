def trailingZeros(nums):

    res = 1
    for num in range(1, nums+1):
        res *= num

    ans = 0
    while res > 0:
        if res % 10 == 0:
            ans += 1
        else:
            break

        res = res // 10

    return ans

print(trailingZeros(0))

