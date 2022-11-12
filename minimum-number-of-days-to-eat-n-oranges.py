class Solution:
    def minDays(self, n: int) -> int:
        memo = {}

        def getMinDays(n):
            if n <= 2:
                return n
            
            if n in memo:
                return memo[n]

            memo[n] = 1 + min(n % 2 + getMinDays(n // 2), n % 3 + getMinDays(n // 3))
            return memo[n]

        return getMinDays(n)

solution = Solution()
print(solution.minDays(10))
print(solution.minDays(6))