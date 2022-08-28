def maxScore(s: str) -> int:
    length = len(s)
    dp = [0] * (length + 1)

    for i in range(length):
        dp[i] = dp[i - 1] + (1 if s[i] == '0' else 0)

    maximum = 0

    ones = 0
    for i in reversed(range(1, length)):
        if s[i] == '1':
            ones += 1

        maximum = max(dp[i - 1] + ones, maximum)

    return maximum


print(maxScore("011101"))