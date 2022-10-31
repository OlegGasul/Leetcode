def buildArray(nums):
    result = [0] * len(nums)
        
    for i in range(len(nums)):
        result[i] = nums[nums[i]]
            
    return result

print(buildArray([0, 2, 1, 5, 3, 4]))