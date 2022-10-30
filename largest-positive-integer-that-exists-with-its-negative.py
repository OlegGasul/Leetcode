def findMaxK(nums) -> int:
    result = -1
    visited = set()
        
    for num in nums:
        if -num in visited:
            result = max(result, abs(num))
        visited.add(num)
            
    return result

print(findMaxK([-1, 2, -3, 3]))
print(findMaxK([-1, 10, 6, 7, -7, 1]))
print(findMaxK([-10, 8, 6, 7, -2, -3]))