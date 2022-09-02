def kLengthApart(nums, k: int) -> bool:
    length = len(nums)
    nums.append(k + 1)
    
    for i in range(length):
        if nums[i] == 1:
            if nums[i - 1] - 1 < k:
                return False
        else:
            nums[i] = nums[i - 1] + 1

    return True

print(kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
print(kLengthApart([1, 0, 0, 1, 0, 1], 2))