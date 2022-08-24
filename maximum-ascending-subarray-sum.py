def maxAscendingSum(nums) -> int:
    maximum = nums[0]
    current = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current += nums[i]
        else:
            current = nums[i]

        maximum = max(maximum, current)

    return maximum

print(maxAscendingSum([10, 20, 30, 5, 10, 50]))
print(maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))