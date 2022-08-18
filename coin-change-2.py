def change(amount: int, coins) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[-1]


print(change(5, [1, 2, 5]))
print(change(3, [2]))
print(change(10, [10]))