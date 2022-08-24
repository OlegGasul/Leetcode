def smallestRangeI(nums, k: int) -> int:
    length = len(nums)

    minimum = nums[0]
    maximum = nums[0]

    for i in range(1, length):
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])

    result = (maximum - k) - (minimum + k)
    return result if result > 0 else 0


print(smallestRangeI([1, 3, 6], 3))
print(smallestRangeI([1, 3, 6, 10], 3))