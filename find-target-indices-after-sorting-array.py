def targetIndices(nums, target: int):
    lessNumbers = 0
    targetNumbers = 0

    for i in range(len(nums)):
        if nums[i] < target:
            lessNumbers += 1
        elif nums[i] == target:
            targetNumbers += 1

    if targetNumbers == 0:
        return []

    return list(range(lessNumbers, lessNumbers + targetNumbers))
    
# [1, 2, 5, 2, 3]
# [1, 2, 2, 3, 5]
print(targetIndices([1, 2, 5, 2, 3], 2))
print(targetIndices([1, 2, 5, 2, 3], 3))