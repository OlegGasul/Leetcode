def maxIceCream(costs, coins: int) -> int:
    costs.sort()
        
    result = 0
    for cost in costs:
        if cost > coins:
            return result
            
        coins -= cost
        result += 1
        
    return result

print(maxIceCream([1, 3, 2, 4, 1], 7))
print(maxIceCream([10, 6, 8, 7, 7, 8], 5))
print(maxIceCream([1, 6, 3, 1, 2, 5], 20))