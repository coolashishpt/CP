class Solution:
    def fact(self, n):
        if n == 0:
            return 1

        return n * self.fact(n - 1)


obj = Solution()

print(obj.fact(5))
