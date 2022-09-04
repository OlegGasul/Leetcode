def getMaxLen(nums) -> int:
    length = len(nums)
    dp = [1] * (length + 1)

    intervals = [[0, 0, []]]
    negativeIndecies = {}

    for i in range(length):
        if nums[i] == 0:
            dp[i] = 1
            intervals.append([i + 1, i + 1, []])
        else:
            intervals[-1][1] = i
            if nums[i] < 0:
                intervals[-1][2].append(i)
            dp[i] = dp[i - 1] * nums[i]

    def getMaxLenInInterval(interval):
        if len(interval[2]) % 2 == 0:
            return dp[interval[1]] // dp[interval[0] - 1]

        return max(
            dp[interval[2][-1] - 1] // dp[interval[0] - 1],
            dp[interval[1]] // dp[interval[2][0]])

    maximum = float('-inf')
    for interval in intervals:
        maximum = max(maximum, getMaxLenInInterval(interval))

    return maximum

print(getMaxLen([-1, -2, -3, 0, 1]))
print(getMaxLen([-1, -2, -4, -5, 0, 10, -1, 2, -1, 3, -2, 1]))
print(getMaxLen([-1, 2, 1, -1, 0, -2, 1, 0, -2, -3, 4, -5]))