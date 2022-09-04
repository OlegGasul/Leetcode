def getMaxLen(nums) -> int:
    length = len(nums)
    
    intervals = [[0, 0, []]]
    allZeros = True
    
    for i in range(length):
        if nums[i] == 0:
            intervals.append([i + 1, i + 1, []])
        else:
            intervals[-1][1] = i
            if nums[i] < 0:
                intervals[-1][2].append(i)
            allZeros = False

    if allZeros:
        return 0

    def getMaxLenInterval(interval):
        if len(interval[2]) % 2 == 0:
            return interval[1] - interval[0] + 1
        return max((interval[2][-1] - 1) - interval[0] + 1, interval[1] - (interval[2][0] + 1) + 1)

    maximum = float('-inf')
    for interval in intervals:
        maximum = max(maximum, getMaxLenInterval(interval))

    return maximum

print(getMaxLen([-1, 2]))
print(getMaxLen([0, 0, 0, 0, 0]))
print(getMaxLen([1, -2, -3, 4]))
print(getMaxLen([0, 1, -2, -3, -4]))
print(getMaxLen([-1, -2, -3, 0, 1]))
