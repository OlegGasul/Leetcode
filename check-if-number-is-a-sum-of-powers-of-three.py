class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 1:
                n -= 1
            elif n % 3 == 0:
                n //= 3
            else:
                return False

        return True

solution = Solution()
print(solution.checkPowersOfThree(12))
print(solution.checkPowersOfThree(91))