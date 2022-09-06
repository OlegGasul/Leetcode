def minIncrementForUnique(nums) -> int:
    nums.sort()
        
    visited = set()
    visited.add(nums[0])
        
    result = 0
        
    for i in range(1, len(nums)):
        if nums[i] in visited:
            newValue = nums[i - 1] + 1
            result += newValue - nums[i]
            nums[i] = newValue
                
        visited.add(nums[i])
                
    return result

print(minIncrementForUnique([1, 2, 2]))
print(minIncrementForUnique([3, 2, 1, 2, 1, 7]))