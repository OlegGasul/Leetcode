def isMonotonic(nums) -> bool:
    length = len(nums)
    if length == 1:
        return True

    isIncreasing = nums[0] <= nums[length - 1]

    for i in range(1, length):
        if isIncreasing:
            if nums[i] < nums[i - 1]:
                return False
        elif nums[i] > nums[i - 1]:
            return False

    return True

print(isMonotonic([1, 2, 2, 3]))
print(isMonotonic([6, 5, 4, 4]))
print(isMonotonic([1, 3, 2]))
