def repeatedNTimes(nums) -> int:
    n = len(nums) / 2
        
    counts = {}
        
    for i in range(len(nums)):
        if nums[i] not in counts:
            counts[nums[i]] = 0
        counts[nums[i]] += 1
            
        if counts[nums[i]] == n:
            return nums[i]
            
    return -1

print(repeatedNTimes([1, 2, 3, 3]))
print(repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))