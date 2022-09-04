def minSubArrayLen(target: int, nums) -> int:
    length = len(nums)
    if length == 0:
        return 0
        
    left = 0
    right = 0
    minimum = float('inf')
    total = nums[0]
        
    while right < length:
        if total >= target:
            minimum = min(minimum, right - left + 1)
            total -= nums[left]
            left += 1
        else:
            right += 1
            if right < length:
                total += nums[right]
            
        if left > right:
            right = left
    
    return minimum if minimum < float('inf') else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(4, [1, 4, 4]))