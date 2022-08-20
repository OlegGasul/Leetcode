# Take a look
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

def splitArrayBy(nums, m, start, end, dp) -> int:
    if m == 1:
        return dp[end - 1] - dp[start - 1]

    minimum = None

    # print()
    # print('splitArrayBy: m = ' + str(m) + ', start = ' + str(start) + ', end = ' + str(end))

    for i in range(start, end - m + 1):
        diff = max(dp[i] - dp[start - 1], splitArrayBy(nums, m - 1, i + 1, end, dp))
        
        if minimum != None:
            minimum = min(minimum, diff)
        else:
            minimum = diff

    return minimum

def splitArray(nums, m: int) -> int:
    if m == 1:
        return sum(nums)
    length = len(nums)
    if length == m:
        return max(nums)

    dp = [0] * length
    dp[0] = nums[0]

    minimum = None

    for i in range(1, length):
        dp[i] = dp[i - 1] + nums[i]

    # print(dp)

    for i in range(length - m + 1):
        diff = max(dp[i], splitArrayBy(nums, m - 1, i + 1, length, dp))
        
        if minimum != None:
            minimum = min(minimum, diff)
        else:
            minimum = diff

    return minimum

print(splitArray([7, 2, 5, 10, 8], 2))
print(splitArray([1, 4, 4], 3))
print(splitArray([1, 2, 3, 4, 5], 2))