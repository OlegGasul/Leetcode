def numSubarrayProductLessThanK(nums, k: int) -> int:
    if k <= 1:
        return 0
    
    left, right = 0, 0
    
    result = 0
    product = 1
        
    while right < len(nums):
        product = product * nums[right]
        
        while product >= k:
            product /= nums[left]
            left += 1
        
        result += right - left + 1
        right += 1
    
    return result


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))