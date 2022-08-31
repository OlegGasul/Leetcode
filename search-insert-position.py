def searchInsert(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1
        
    if target < nums[left]:
        return 0
    elif target > nums[right]:
        return len(nums)
        
    while left < right:
        middle = left + (right - left) // 2
        value = nums[middle]
            
        if value == target:
            return middle
            
        if value < target:
            left = middle + 1
        else:
            right = middle
                
    return right

print(searchInsert([1, 3, 5, 6], 2))