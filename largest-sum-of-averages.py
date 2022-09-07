def largestSumOfAverages(nums, K: int) -> float:
    P = [0]
    for x in nums:
        P.append(P[-1] + x)

    def average(i, j):
        return (P[j] - P[i]) / float(j - i)

    length = len(nums)
    dp = [average(i, length) for i in range(length)]

    for k in range(K - 1):
        for i in range(length):
            for j in range(i + 1, length):
                dp[i] = max(dp[i], average(i, j) + dp[j])

    return dp[0]


print(largestSumOfAverages([9, 1, 2, 3, 9], 3))