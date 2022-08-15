def removeDuplicates(nums) -> int:
    prev = None
    index = 0
    
    while index < len(nums):
        item = nums[index]

        if item == prev:
            nums.pop(index)
        else:
            index += 1
        prev = item

    return index

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1]
nums = [1, 1, 2]

print(removeDuplicates(nums))

print(list(nums))
