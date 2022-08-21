def findMiddleIndex(nums) -> int:
    dp = [0] * len(nums)
    length = len(nums)
    
    dp[0] = nums[0]
    for i in range(1, length):
        dp[i] = nums[i] + dp[i - 1]

    for i in range(length):
        left = dp[i - 1] if i > 0 else 0
        right = dp[-1] - dp[i] if i < length - 1 else 0
        if left == right:
            return i

    return -1

print(findMiddleIndex([2, 3, -1, 8, 4]))
print(findMiddleIndex([1, -1, 4]))
print(findMiddleIndex([2, 5]))