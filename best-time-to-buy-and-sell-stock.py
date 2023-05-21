class Solution:
    def maxProfit(self, prices) -> int:
        minimum = prices[0]
        
        result = 0
        
        for i in range(1, len(prices)):
            if prices[i] > minimum:
                result = max(result, prices[i] - minimum)
            minimum = min(minimum, prices[i])
            
        return result

solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0