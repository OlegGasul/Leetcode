class Solution:
    def minOperations(self, n: int) -> int:
        result = 0

        for i in range(n // 2):
            result += n - (2 * i + 1)

        return result

solution = Solution()
print(solution.minOperations(3))
print(solution.minOperations(6))