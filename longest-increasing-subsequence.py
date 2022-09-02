def lengthOfLIS(nums) -> int:
    dp = [1 for _ in range(len(nums))]
    result = 1
    dp[0] = 1
        
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                result = max(dp[i], ret)
    
    return result

print(lengthOfLIS([1, 2, 3, 4, 1, 1, 1, 2]))
