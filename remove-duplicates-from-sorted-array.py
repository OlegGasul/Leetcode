def removeDuplicates(nums) -> int:
    index = 1
    
    while index < len(nums):
        if nums[index] == nums[index - 1]:
            nums.pop(index)
        else:
            index += 1

    return index

nums = [1, 1, 2]
print(removeDuplicates(nums))
print(list(nums))

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
print(list(nums))
