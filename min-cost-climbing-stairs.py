def minCostClimbingStairs(cost) -> int:
    dp1, dp2 = cost[0] if len(cost) > 0 else 0, cost[1] if len(cost) > 1 else 0
    
    for i in range(2, len(cost)):
        current = cost[i] + min(dp1, dp2)
        
        dp1, dp2 = dp2, current
    
    return min(dp1, dp2)

print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))