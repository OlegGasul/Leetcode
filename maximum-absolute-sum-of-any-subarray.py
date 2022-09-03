def maxAbsoluteSum(nums) -> int:
    localMin = 0
    globalMin = float('inf')
    localMax = 0
    globalMax = float('-inf')
    
    for i in range(len(nums)):
        localMin = min(nums[i], nums[i] + localMin)
        if localMin < globalMin:
            globalMin = localMin
        localMax = max(nums[i], nums[i] + localMax)
        if localMax > globalMax:
            globalMax = localMax

    return max(abs(globalMin), abs(globalMax))

print(maxAbsoluteSum([1, -3, 2, 3, -4]))
print(maxAbsoluteSum([2, -5, 1, -4, 3, -2]))