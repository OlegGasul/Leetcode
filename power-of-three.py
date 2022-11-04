class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True

        if n < 3:
            return False
        
        if n % 9 == 0:
            return self.isPowerOfThree(n // 9)
        
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)

        return False

solution = Solution()
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(0))
print(solution.isPowerOfThree(-1))
print(solution.isPowerOfThree(81))