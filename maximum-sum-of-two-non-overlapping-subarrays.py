def maxSumTwoNoOverlap(nums, firstLen: int, secondLen: int) -> int:
    length = len(nums)
    dp = [0] * (length + 1)

    for i in range(length):
        dp[i] = dp[i - 1] + nums[i]

    def findBestSecondInterval(start, end):
        if end - start < secondLen:
            return 0

        maximum = float('-inf')
        for i in range(start + secondLen - 1, end):
            maximum = max(maximum, dp[i] - dp[i - secondLen])

        return maximum

    maximum = float('-inf')
    for i in range(firstLen - 1, length):
        left = findBestSecondInterval(0, i - firstLen + 1)
        right = findBestSecondInterval(i + 1, length)

        maximum = max(maximum, max(left, right) + dp[i] - dp[i - firstLen])

    return maximum

print(maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
print(maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
print(maxSumTwoNoOverlap([1, 0, 3], 1, 2))