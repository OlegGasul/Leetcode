def rob(nums) -> int:
    length = len(nums)

    if length == 1:
        return nums[0]

    if length == 2:
        return max(nums[0], nums[1])

    dp = [0] * len(nums)

    for i in range(length):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


print(rob([2, 7, 9, 3, 1]))
print(rob([1, 2, 3, 1]))