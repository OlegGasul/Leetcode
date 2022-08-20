def waysToSplitArray(nums) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = dp[i - 1] + nums[i]

    result = 0

    for i in range(len(nums) - 1):
        if dp[i] >= dp[-1] - dp[i]:
            result += 1

    return result

print(waysToSplitArray([10, 4, -8, 7]))