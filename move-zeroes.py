def moveZeroes(nums) -> None:
    length = len(nums)
    i = 0
    
    while i < length:
        while i < length and nums[i] != 0:
            i += 1

        if i >= length:
            break

        j = i
        while j < length and nums[j] == 0:
            j += 1

        if j >= length:
            break
        
        nums[i], nums[j] = nums[j], nums[i]


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums = [1, 1, 0, 4, 1, 0, 0, 3, 12]
moveZeroes(nums)
print(nums)