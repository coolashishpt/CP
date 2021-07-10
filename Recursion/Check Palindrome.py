def isPalin(n):
    def rev(n):
        if n < 10:
            return str(n)

        div = n // 10
        mod = n % 10
        string = str(mod) + str(rev(div))

        return string

    reverse = rev(n)

    if reverse == str(n):
        return 1
    else:
        return 0


class Solution:
    pass


obj = Solution()
print(isPalin(9))


