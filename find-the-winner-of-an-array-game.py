def getWinner(arr, k: int) -> int:
    length = len(arr)
    if length == 1:
        return arr[0]
    
    dp = [0] * length

    winner = 0
    for i in range(1, length):
        if arr[i] > arr[winner]:
            winner = i
        dp[winner] += 1

        if dp[winner] == k:
            return arr[winner]

    return arr[winner]


print(getWinner([2, 1, 3, 5, 4, 6, 7], 20))
print(getWinner([3, 2, 1], 10))