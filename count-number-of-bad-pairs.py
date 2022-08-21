import collections

def countBadPairs(nums) -> int:
    dp = [0] * len(nums)

    for i in range(len(nums)):
        dp[i] = nums[i] - i

    counter = collections.Counter(dp)
    result = 0
    for x in counter.items():
        if x[1] > 1:
            n = x[1] - 1
            result += int((n * (n + 1)) / 2)

    n = len(nums) - 1
    result = int((n * (n + 1)) / 2) - result
    
    return result

print(countBadPairs([4, 1, 3, 3]))
print(countBadPairs([4, 1, 2, 3, 4]))
print(countBadPairs([4, 3, 4, 5, 6, 7, 4]))

# 2, 2, 2, 2, 2
# 1, 2, 3, 4, 5
