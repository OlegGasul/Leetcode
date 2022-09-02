def maxProduct2(nums) -> int:
    length = len(nums)

    if length == 1:
        return nums[0]
    
    dp = [1] * (length + 1)

    zeroIndexes = []
    negativeIndexes = []

    i = 0
    while i < length:
        if nums[i] == 0:
            zeroIndexes.append(i)
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] * nums[i]

        if nums[i] < 0:
            negativeIndexes.append(i)

        i += 1

    if not zeroIndexes and not negativeIndexes:
        return dp[length - 1]
    
    def computeInterval(start, end):
        if start == end:
            return dp[start] // dp[start - 1]

        if start > end:
            return 0
        
        nIndexes = [x for x in negativeIndexes if x >= start and x <= end]

        if len(nIndexes) % 2 == 0:
            return dp[end] // dp[start - 1]

        value1 = dp[nIndexes[-1] - 1] // dp[start - 1]
        value2 = dp[end] // dp[nIndexes[0]]

        return max(value1, value2, 0)
    
    if zeroIndexes:
        start = 0
        values = [0]
        
        i = 0
        while i < len(zeroIndexes):
            values.append(computeInterval(start, zeroIndexes[i] - 1))
            start = zeroIndexes[i] + 1
            i += 1

        values.append(computeInterval(start, length - 1))

        return max(values)

    elif negativeIndexes:
        if len(negativeIndexes) % 2 == 0:
            return dp[length - 1]

        return computeInterval(0, length - 1)

def maxProduct(nums) -> int:
    if not nums:
        return 0
        
    if len(nums) == 1:
        return nums[0]
        
    minSoFar, maxSoFar, maxGlobal = nums[0], nums[0], nums[0]
    
    for i in range(1, len(nums)):
        maxSoFar = max(minSoFar * nums[i], maxSoFar * nums[i], nums[i])
        minSoFar = min(minSoFar * nums[i], maxSoFar * nums[i], nums[i])

        maxGlobal = max(maxGlobal, maxSoFar)

    return maxGlobal

print(maxProduct([-2, 0]))
print(maxProduct([2, 3, -2, 4, 2]))
print(maxProduct([-2, 0, -1]))
print(maxProduct([-4, -3]))
print(maxProduct([2, -1, 2, -1, 1, 0, 2, -1, 2, 0, 8, - 1, 2, -2, 7]))
print(maxProduct([2, 2, 0, 2, 0, 8, 2]))
print(maxProduct([2, 2, -1, 2, 0, 2, -1, 2, 2, -1, 2, 2, 2, 2]))
print(maxProduct([2, 3, -2, 4]))
print(maxProduct([2, 3, 2, 4]))