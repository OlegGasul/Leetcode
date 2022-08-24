def findDisappearedNumbers(nums):
    length = len(nums)
    i = 0
    result = []

    while i < length:
        correct = nums[i] - 1
        while nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
            correct = nums[i] - 1
        
        i += 1

    for i in range(length):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result
    

print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([1, 1]))
