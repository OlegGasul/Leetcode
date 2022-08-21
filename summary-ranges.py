def summaryRanges(nums):
    if len(nums) == 0:
        return []
    
    if len(nums) == 1:
        return [str(nums[0])]
    
    result = []
    
    start = 0
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) > 1:
            if start == i - 1:
                result.append(str(nums[start]))
            else:
               result.append(str(nums[start]) + '->' + str(nums[i - 1])) 
            start = i

    if start == len(nums) - 1:
        result.append(str(nums[start]))
    else:
        result.append(str(nums[start]) + '->' + str(nums[-1]))

    return result

print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([]))