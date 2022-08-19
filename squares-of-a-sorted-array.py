def sortedSquares(nums):
    left = 0
    right = len(nums) - 1

    result = []
    a = abs(nums[left])
    b = abs(nums[right])
        
    while left <= right:
        if a > b:
            result.insert(0, a ** 2)
            left += 1
            if left <= right:
                a = abs(nums[left])
        else:
            result.insert(0, b ** 2)
            right -= 1
            if left <= right:
                b = abs(nums[right])
    
    return result

print(sortedSquares([-10, 2, 3, 4, 5]))
print(sortedSquares([-4, -1, 0, 3, 10]))