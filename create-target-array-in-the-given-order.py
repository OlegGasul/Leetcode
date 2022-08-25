def createTargetArray(nums, index):
    result = []
    
    for i in range(len(nums)):
        result.insert(index[i], nums[i])
        
    return result


print(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))