def dominantIndex(nums) -> int:
    maximum = -1
    maximumIndex = -1
    length = len(nums)
        
    for i in range(length):
        if nums[i] > maximum:
            maximum = nums[i]
            maximumIndex = i
        
    for i in range(maximumIndex + 1, length):
        if 2 * nums[i] > maximum:
            return -1
            
    for i in range(maximumIndex):
        if 2 * nums[i] > maximum:
            return -1
            
    return maximumIndex

print(dominantIndex([3, 6, 1, 0]))
print(dominantIndex([1, 2, 3, 4]))