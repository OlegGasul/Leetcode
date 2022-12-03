class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

solution = Solution()
assert solution.divisorGame(2) == True
assert solution.divisorGame(3) == False