class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length < 2:
            return 0

        postfixSum = [0] * (length + 1)

        maximum = float('-inf')
        for i in range(length - 2, -1, -1):
            maximum = max(maximum, prices[i + 1])
            
            profit = maximum - prices[i]
            if profit > 0:
                postfixSum[i] = max(profit, postfixSum[i + 1])
            else:
                postfixSum[i] = postfixSum[i + 1]

        result = 0
        minimum = float('inf')

        for i in range(1, length):
            minimum = min(minimum, prices[i - 1])
            
            profit = prices[i] - minimum
            if profit < 0:
                profit = 0
            
            result = max(result, profit + postfixSum[i + 1])

        return result

solution = Solution()
assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0