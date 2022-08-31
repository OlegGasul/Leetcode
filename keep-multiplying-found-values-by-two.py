def findFinalValue(nums, original: int) -> int:
    visited = set()
    
    for i in range(len(nums)):
        while original in visited:
            visited.discard(original)
            original *= 2
                
        if nums[i] == original:
            original *= 2
        visited.add(nums[i])

    while original in visited:
        visited.discard(original)
        original *= 2

    return original

print(findFinalValue([24, 5, 12, 3, 6, 1], 3))
print(findFinalValue([4, 2], 2))