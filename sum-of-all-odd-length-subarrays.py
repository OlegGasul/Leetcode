def sumOddLengthSubarrays(arr) -> int:
    length = len(arr)
    dp = [0] * (length + 1)

    result = 0

    for i in range(length):
        dp[i] = dp[i - 1] + arr[i]

    amount = length if length % 2 == 1 else length - 1

    while amount > 0:
        index = amount - 1
        print('index = ' + str(index))

        while index < length:
            print('dp[index] = ' + str(dp[index]))
            result += dp[index] - dp[index - amount]
            index += 1

        amount -= 2


    # print(dp)

    return result

print(sumOddLengthSubarrays([1, 4, 2, 5, 3]))