def maximumSum(nums) -> int:
    length = len(nums)
    
    values = {}
    maximum = -1

    for i in range(length):
        value = sum(list(map(int, list(str(nums[i])))))
        if not value in values:
            values[value] = []
        values[value] += [nums[i]]

        if len(values[value]) > 1:
            values[value] = sorted(values[value], reverse = True)[0:2]
            maximum = max(maximum, sum(values[value]))
    
    return maximum


print(maximumSum([18, 43, 36, 13, 7]))
print(maximumSum([18, 43, 36, 72, 13, 100, 7]))
print(maximumSum([10, 12, 19, 14]))