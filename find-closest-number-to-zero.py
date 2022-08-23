def findClosestNumber(nums) -> int:
    result = nums[0]
    minimum = abs(nums[0])

    for i in range(1, len(nums)):
        if abs(nums[i]) < minimum:
            minimum = abs(nums[i])
            result = nums[i]
        elif abs(nums[i]) == minimum and nums[i] > 0:
            result = nums[i]
    
    return result


print(findClosestNumber([-4, -2, 1, 4, 8]))
print(findClosestNumber([2, -1, 1]))
print(findClosestNumber([-100000, -100000]))