def minStartValue(nums) -> int:
    value = nums[0]
    minimum = nums[0]
        
    for i in range(1, len(nums)):
        value += nums[i]
        minimum = min(minimum, value)
            
        
    if minimum >= 0:
        return 1
    else:
        return abs(minimum) + 1


print(minStartValue([-3, 2, -3, 4, 2]))