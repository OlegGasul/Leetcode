import functools

def maxSubsequence(nums, k: int):
    length = len(nums)
    if length == k:
        return nums
        
    dp = [0] * length
    for i in range(length):
        dp[i] = [nums[i], i]
            
    def compare(a, b):
        return b[0] - a[0]
        
    dp = sorted(dp, key = functools.cmp_to_key(compare))
        
    result = dp[0:k]
        
    def compareByIndex(a, b):
        return a[1] - b[1]
        
    result = sorted(result, key = functools.cmp_to_key(compareByIndex))
        
    for i in range(len(result)):
        result[i] = result[i][0]
            
    return result

print(maxSubsequence([2, 1, 3, 3], 2))
print(maxSubsequence([-1, -2, 3, 4], 3))
print(maxSubsequence([3, 4, 3, 3], 2))