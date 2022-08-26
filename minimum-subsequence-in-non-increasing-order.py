def minSubsequence(nums):
    nums = sorted(nums, reverse = True)
    
    total = sum(nums)
    collected = 0
    
    for i in range(len(nums)):
        collected += nums[i]
        total -= nums[i]

        if collected > total:
            return nums[0 : i + 1]


print(minSubsequence([4, 3, 10, 9, 8]))