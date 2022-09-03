def minElements(nums, limit: int, goal: int) -> int:
    n = abs(sum(nums) - goal)
    result = abs(sum(nums) - goal) // limit
    if n % limit > 0:
        result += 1
    
    return result

print(minElements([1, -1, 1], 3, -4))
print(minElements([1, -10, 9, 1], 100, 0))