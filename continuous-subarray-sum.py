def checkSubarraySum(nums, k: int) -> bool:
    values = {}
    length = len(nums)
    preSum = 0

    for i in range(length):
        preSum = (preSum + nums[i]) % k
        
        if preSum in values:
            if i - values[preSum] >= 2:
                return True
        else:
            values[preSum] = i

    return False

print(checkSubarraySum([2, 3, 6, 10, 5], 9))
print(checkSubarraySum([23, 2, 6, 4, 7], 13))
print(checkSubarraySum([23, 2, 6, 4, 7], 6))