import collections

def countNicePairs(nums) -> int:
    length = len(nums)
    dp = [0] * length

    for i in range(length):
        dp[i] = nums[i] - int(''.join(reversed(list(str(nums[i])))))

    counter = collections.Counter(dp)
    result = 0
    for x in counter.items():
        if x[1] > 1:
            n = x[1] - 1
            result += (n * (n + 1)) // 2

    return result

print(countNicePairs([42, 11, 1, 97]))
print(countNicePairs([13, 10, 35, 24, 76]))