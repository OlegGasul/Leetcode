def getSumAbsoluteDifferences(nums):
    length = len(nums)
    numSum = sum(nums)
    count = 0
    
    dp = [0] * length
    
    for i in range(len(nums)):
        count += nums[i]
        dp[i] = (nums[i] * (i + 1)) - count + (-nums[i] * (length - (i + 1)) + (numSum - count))
    return dp

print(getSumAbsoluteDifferences([2, 3, 5]))
print(getSumAbsoluteDifferences([1, 4, 6, 8, 10]))