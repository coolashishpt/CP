# Naive Solution

from datetime import datetime

# record current timestamp
def trailingZeros(nums):
    start = datetime.now()
    res = 1
    for num in range(2, nums+1):
        res *= num
    ans = 0
    while res > 0:
        if res % 10 == 0:
            ans += 1
        else:
            break

        res = res // 10
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")
    return ans

# Optimize Solution

def trailingZerosOptimizeV1(nums):
    start = datetime.now()
    res = 0
    while nums >= 5:
        nums //= 5
        res += nums
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")
    return res

num = 22510
print(trailingZeros(num))

print(trailingZerosOptimizeV1(num))
