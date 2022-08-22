def minimumDifference(nums, k: int) -> int:
    length = len(nums)
    if length == 1:
        return 0
    
    nums = sorted(nums)
    
    minimum = None
    for i in range(k - 1, length):
        diff = nums[i] - nums[i - k + 1]
        if minimum == None:
            minimum = diff
        else:
            minimum = min(diff, minimum)

    return minimum

print(minimumDifference([9, 4, 1, 7], 2))
print(minimumDifference([90], 1))