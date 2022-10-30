def search(nums, target: int) -> bool:
    if len(nums) == 0:
        return False
        
    if len(nums) == 1:
        return nums[0] == target
            
    pivot = -1
        
    for i in range(1, len(nums)):
        if nums[i] == target or nums[i - 1] == target:
            return True
            
        if nums[i] < nums[i - 1]:
            pivot = i
            break
                
    if pivot < 0:
        return False
        
    if target < nums[pivot] or target > nums[-1]:
        return False
        
    left = pivot
    right = len(nums) - 1
        
    while left < right:
        middle = left + (right - left) // 2
            
        if nums[middle] == target:
            return True
            
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
                
    return nums[left] == target or nums[right] == target

print(search([4, 5, 6, 7, 0, 1, 2], 1))
print(search([1], 1))
print(search([5], 1))