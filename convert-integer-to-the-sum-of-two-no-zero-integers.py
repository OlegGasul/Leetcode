class Solution:
    def getNoZeroIntegers(self, n: int):
        a = 1
        b = n - a

        def check(val):
            return not "0" in set(list(str(val)))
        
        while a <= n // 2:
            b = n - a

            if check(a) and check(b):
                return [a, b]

            a += 1

        return [-1, -1]

solution = Solution()
print(solution.getNoZeroIntegers(2))
print(solution.getNoZeroIntegers(11))
print(solution.getNoZeroIntegers(550))