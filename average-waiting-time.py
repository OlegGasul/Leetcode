# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

# arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

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
