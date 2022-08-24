def firstMissingPositive(nums) -> int:
    length = len(nums)
    
    for i in range(length):
        correctPos = nums[i] - 1
        while 1 <= nums[i] <= length and nums[i] != nums[correctPos]:
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i] - 1
                
    print(nums)

    for i in range(length):
        if i + 1 != nums[i]:
            return i + 1
    
    return length + 1


print(firstMissingPositive([1, 2, 3, 4, 5, 6, 100, 200, 7]))