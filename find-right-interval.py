import functools

def findRightInterval(intervals):
    length = len(intervals)
    
    dp = [0] * length

    for i in range(length):
        dp[i] = [intervals[i][0], i]

    def compare(a, b): return a[0] - b[0]
    dp = sorted(dp, key = functools.cmp_to_key(compare))

    # print(dp)

    def findInterval(value):
        nonlocal length
        nonlocal dp
        
        left = 0
        right = len(dp) - 1

        while left <= right:
            index = left + (right - left) // 2
        
            if dp[index][0] == value:
                return dp[index][1]
        
            if dp[index][0] > value:
                right = index - 1
            else:
                left = index + 1

        return dp[left][1] if left >= 0 and left < length else -1
    
    result = [-1] * length
    for i in range(length):
        result[i] = findInterval(intervals[i][1])

    return result

print(findRightInterval([[3, 4], [2, 3], [1, 2]]))
print(findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]))
print(findRightInterval([[3, 4], [2, 3], [1, 2]]))