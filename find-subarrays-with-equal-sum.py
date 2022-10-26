def findSubarrays(nums) -> bool:
    if len(nums) < 3:
        return False
        
    sums = set()
        
    for i in range(1, len(nums)):
        current = nums[i] + nums[i - 1]
        if current in sums:
            return True
            
        sums.add(current)
            
    return False

print(findSubarrays([4, 2, 4]))
print(findSubarrays([1, 2, 3, 4, 5]))
print(findSubarrays([0, 0, 0]))