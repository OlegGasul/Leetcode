def getMinDistance(nums, target: int, start: int) -> int:
    length = len(nums)
    i = start
        
    if i < 0:
        i = 0
    elif i > length - 1:
        i = length - 1
        
    diffs = []
        
    j = i - 1
    while j >= 0:
        if nums[j] == target:
            diffs.append(abs(j - start))
            break
        j -= 1
        
    if diffs and diffs[0] == 0:
        return 0
        
    j = i
    while j < length:
        if nums[j] == target:
            diffs.append(abs(j - start))
            break
        j += 1
            
    if not diffs:
        return -1
        
    return min(diffs)

print(getMinDistance([1, 2, 3, 4, 5], 3, 5))
print(getMinDistance([1], 1, 0))
print(getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0))