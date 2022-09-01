def maximumDifference(nums) -> int:
    length = len(nums)
    dp = [0] * length
    dp[0] = nums[0]
        
    result = -1
        
    for i in range(1, length):
        if nums[i] > dp[i - 1]:
            result = max(result, nums[i] - dp[i - 1])
        dp[i] = min(nums[i], dp[i - 1])
            
    return result

print(maximumDifference([7, 1, 5, 4]))
print(maximumDifference([9, 4, 3, 2]))
print(maximumDifference([1, 5, 2, 10]))