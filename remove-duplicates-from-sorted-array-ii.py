def removeDuplicates(nums) -> int:
    if len(nums) <= 2:
        return len(nums)
    
    index = 2
    
    while index < len(nums):
        if nums[index] == nums[index - 1] and nums[index] == nums[index - 2]:
            nums.pop(index)
        else:
            index += 1
    
    return index

nums = [1, 1, 2]
print(removeDuplicates(nums))
print(list(nums))

nums = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
print(removeDuplicates(nums))
print(list(nums))

nums = [1]
print(removeDuplicates(nums))
print(list(nums))