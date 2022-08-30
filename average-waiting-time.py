def averageWaitingTime(customers) -> float:
    length = len(customers)
    dp = [0] * (length + 1)
    dp[-1] = customers[0][0]

    result = 0
    for i in range(length):
        dp[i] = max(dp[i - 1], customers[i][0]) + customers[i][1]
        result += dp[i] - customers[i][0]

    return result / length

print(averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
print(averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))