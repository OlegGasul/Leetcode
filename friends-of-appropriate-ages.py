def numFriendRequests(ages) -> int:
    length = len(ages)

    counters = [0] * 121
    for age in ages:
        counters[age] += 1

    # print(counters)

    dp = [0] * len(counters)

    for i in range(1, len(counters)):
        dp[i] = dp[i - 1] + counters[i]

    result = 0

    # print(dp)

    for age in set(ages):
        count = counters[age]
        if count == 0:
            continue

        left = (age // 2) + 7
        right = age

        if left >= right:
            continue
        
        result += (dp[right] - dp[left] - 1) * count
    
    return result


print(numFriendRequests([16, 17, 18]))
print(numFriendRequests([16, 16]))
print(numFriendRequests([20, 30, 100, 110, 120]))