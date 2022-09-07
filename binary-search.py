def search(nums, target: int) -> int:
    length = len(nums)
        
    left = 0
    right = length - 1
        
    while left < right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
            
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
                
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
        
    return -1

print(search([-1, 0, 3, 5, 9, 12], 12))