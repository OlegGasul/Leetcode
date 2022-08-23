import functools

def maxNonOverlapping(nums, target: int) -> int:
    length = len(nums)
    intervals = []
    
    dp = [0] * (length + 1)
    dp[0] = nums[0]
    if nums[0] == target:
        intervals.append([0, 0])
    
    for i in range(1, length):
        dp[i] = dp[i - 1] + nums[i]
        if nums[i] == target:
            intervals.append([i, i])

    # print('nums = ' + str(nums))
    # print('dp = ' + str(dp))
    
    left = 0
    right = 0

    while right < length:
        current = dp[right] - dp[left - 1] if left != right else nums[left]
        if current == target:
            intervals.append([left, right])

        if left == right:
            right += 1
        elif current < target:
            if dp[left - 1] < 0:
                left += 1
            else:
                right += 1
        else:
            left += 1
    
    
    def compare(a, b):
        if a[0] == b[0]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]
    intervals = sorted(intervals, key = functools.cmp_to_key(compare))
    print(intervals)

    i = 1
    while i < len(intervals):
        if intervals[i][0] >= intervals[i - 1][0] and intervals[i][0] <= intervals[i - 1][1]:
            if (intervals[i][1] - intervals[i][0]) - (intervals[i - 1][1] - intervals[i - 1][0]) >= 0:
                intervals.pop(i)
            else:
                intervals.pop(i - 1)
        else:
            i += 1

    print(intervals)

    return len(intervals)


# print(maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], 6))
# print(maxNonOverlapping([1, 1, 1, 1, 1], 2))
# print(maxNonOverlapping([-5, 5, -4, 5, 4], 5))
# print(maxNonOverlapping([0, 0, 0], 0))
# print(maxNonOverlapping([1, 1, 1, 1, 1], 2))
print(maxNonOverlapping([-1, -2, 8, -3, 8, -5, 5, -4, 5, 4, 1], 5))