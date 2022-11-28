import bisect

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        difficultyProfit = list(zip(difficulty, profit))
        difficultyProfit.sort()

        difficulty, profit = zip(*difficultyProfit)

        n = len(profit)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(profit[i], dp[i - 1])

        result = 0
        for w in worker:
            index = bisect.bisect_right(difficulty, w) - 1
            if index < 0:
                continue
            
            result += dp[index]
        
        return result

solution = Solution()
print(solution.maxProfitAssignment(
    [2, 4, 6, 8, 10],
    [10, 20, 30, 40, 50],
    [4, 5, 6, 7]))
print(solution.maxProfitAssignment(
    [85, 47, 57],
    [24, 66, 99],
    [40, 25, 25]))