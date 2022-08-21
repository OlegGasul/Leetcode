import functools

def getStrongest(arr, k: int):
    length = len(arr)
    sortedArr = sorted(arr)
    
    median = sortedArr[(length - 1) // 2]
    
    dp = [0] * length

    for i in range(length):
        dp[i] = [abs(arr[i] - median), arr[i]]
    
    def compare(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        else:
            return b[0] - a[0]

    result = sorted(dp, key = functools.cmp_to_key(compare))
    return list(map(lambda x: x[1], result[0 : k]))

print(getStrongest([6, 7, 11, 7, 6, 8], 2))