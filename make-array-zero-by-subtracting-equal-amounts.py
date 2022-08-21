def minimumOperations(nums) -> int:
    if len(nums) == 1:
        return 1 if nums[0] > 0 else 0
    
    nums = sorted(nums)
    if nums[-1] == 0:
        return 0

    left = 0
    right = len(nums) - 1
        
    count = 0
    
    while left < right:
        while nums[left] == 0 and left < right:
            left += 1
        
        i = right
        while i >= left:
            nums[i] -= nums[left]
            if nums[i] == 0 and left < i:
                left = i
            i -= 1

        count += 1
            
    return count

print(minimumOperations([1, 5, 0, 3, 5]))
print(minimumOperations([1, 52, 10, 23, 5]))
print(minimumOperations([1]))
print(minimumOperations([0]))