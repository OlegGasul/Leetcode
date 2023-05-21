class Solution:
    def maxProfit(self, prices) -> int:
        mins = []
        maxes = []

        prices.insert(0, float('inf'))
        prices.append(float('-inf'))
        prev = prices[0]

        for i in range(1, len(prices) - 1):
            if prices[i] < prev and prices[i] < prices[i + 1]:
                mins.append(prices[i])
            elif prices[i] > prev and prices[i] > prices[i + 1]:
                maxes.append(prices[i])
            
            if prices[i + 1] != prices[i]:
                prev = prices[i]

        if not mins or not maxes:
            return 0
        
        result = 0
        while mins and maxes:
            result += maxes.pop() - mins.pop()
        
        return result

solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert solution.maxProfit([1, 2, 3, 4, 5]) == 4
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0