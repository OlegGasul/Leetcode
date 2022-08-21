def singleNonDuplicate(nums) -> int:
    length = len(nums)
    if length == 1:
        return nums[0]
    
    for i in range(length):
        if (i == 0 or nums[i] != nums[i - 1]) and (i == length - 1 or nums[i] != nums[i + 1]):
            return nums[i]

print(singleNonDuplicate([1]))
print(singleNonDuplicate([1, 1, 2]))
print(singleNonDuplicate([1, 2, 2]))
print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))