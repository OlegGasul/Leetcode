def reductionOperations(nums) -> int:
    nums.sort()
        
    dp = [0] * len(nums)
        
    for i in range(1, len(nums)):
        dp[i] = dp[i - 1] + (1 if nums[i] > nums[i - 1] else 0)

    print(dp)
        
    return sum(dp)

print(reductionOperations([1, 1, 2, 2, 3]))