def maximumSum2(arr) -> int:
    length = len(arr)
    if length == 1:
        return arr[0]
        
    def kadane(nums):
        localMax = 0
        globalMax = float('-inf')
            
        for i in range(len(nums)):
            localMax = max(nums[i], nums[i] + localMax)
            if localMax > globalMax:
                globalMax = localMax
                    
        return globalMax
        
    maximum = kadane(arr)
    
    for i in range(length):
        maximum = max(maximum, kadane(arr[0 : i] + arr[i + 1 : length]))

    return maximum

def maximumSum(nums) -> int:
    length = len(nums)

    if length == 1:
        return nums[0]
    
    maximum = float('-inf')
    total = 0
    allPositives = True

    for i in range(length):
        maximum = max(maximum, nums[i])
        if nums[i] < 0:
            allPositives = False
        total += nums[i]
    
    if allPositives:
        return total
    if maximum <= 0:
        return maximum

    dp = [0] * length
    localMax = 0
    for i in range(length):
        localMax = max(nums[i], nums[i] + localMax)
        dp[i] = localMax

    dp2 = [0] * length
    localMax = 0
    globalMax = float('-inf')
    for i in reversed(range(length)):
        localMax = max(nums[i], nums[i] + localMax)
        if localMax > globalMax:
            globalMax = localMax
        dp2[i] = localMax

    best = globalMax
    for i in range(1, length - 1):
        best = max(best, dp[i - 1] + dp2[i + 1])

    # dp, dp2 - maximums forward and backward using Kadanes algorithm
    # print(dp)
    # print(dp2)

    return best

print(maximumSum([1, -2, 0, 3]))
print(maximumSum([1, 2, 3, 0]))
print(maximumSum([1, -2, -2, 3]))
print(maximumSum([-1, -2, -2, -3]))
print(maximumSum([-1, -2, -2, -3, 0]))
