import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        isq = i ** 2
        while isq <= c:
            b = math.sqrt(c - isq)
            if b // 1 == b:
                return True

            i += 1
            isq = i ** 2

        return False

solution = Solution()
assert solution.judgeSquareSum(5) == True
assert solution.judgeSquareSum(3) == False