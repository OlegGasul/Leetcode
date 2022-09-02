def findPairs(nums, k: int) -> int:
    visited = set()
    unique = set()
        
    for i in range(len(nums)):
        if nums[i] - k in visited:
            values = [nums[i], nums[i] - k]
            values.sort()
            unique.add(tuple(values))

            
        if nums[i] + k in visited:
            values = [nums[i], nums[i] + k]
            values.sort()
            unique.add(tuple(values))
            
        if not nums[i] in visited:
            visited.add(nums[i])
                
    return len(unique)

print(findPairs([3, 1, 4, 1, 5], 2))
print(findPairs([1, 2, 3, 4, 5], 1))