def minPairSum(nums) -> int:
    nums = sorted(nums)
        
    length = len(nums)
    halvedLength = length // 2
        
    result = float('-inf')
    for i in range(halvedLength):
        result = max(result, nums[i] + nums[length - i - 1])
            
    return result

print(minPairSum([3, 5, 2, 3]))
print(minPairSum([3, 5, 4, 2, 4, 6]))