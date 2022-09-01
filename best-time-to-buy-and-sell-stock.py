def maxProfit(prices) -> int:
    length = len(prices)
    dp = [0] * length
    dp[0] = prices[0]
        
    result = -1
        
    for i in range(1, length):
        if prices[i] > dp[i - 1]:
            result = max(result, prices[i] - dp[i - 1])
        dp[i] = min(prices[i], dp[i - 1])
            
    return result if result > 0 else 0

print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))