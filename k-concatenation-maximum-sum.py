def kConcatenationMaxSum(arr, k: int) -> int:
    length = len(arr)
    localMax = globalMax = total = 0

    for i in range(length if k == 1 else length * 2):
        n = arr[i % length]
        
        localMax = max(n, localMax + n)
        globalMax = max(globalMax, localMax)

        if i <= length - 1:
            total += arr[i]

    return (globalMax + ((k - 2) * max(0, total) if k > 1 else 0)) % (10 ** 9 + 7)

    
print(kConcatenationMaxSum([1, -2, 1], 5))
print(kConcatenationMaxSum([10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000], 100000))
print(kConcatenationMaxSum([-9, 13, 4, -16, -12, -16, 3, -7, 5, -16, 16, 8, -1, -13, 15, 3], 6))
print(kConcatenationMaxSum([-1, -2], 7))
