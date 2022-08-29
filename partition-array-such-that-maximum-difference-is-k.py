def partitionArray(nums, k: int) -> int:
    nums = sorted(nums)
    if nums[-1] - nums[0] < k:
        return 1

    length = len(nums)
    
    left = 0
    right = 0
    counter = 0

    while right < length:
        if nums[right] - nums[left] <= k:
            if right == length - 1:
                counter += 1
                break
            right += 1
        else:
            counter += 1
            left = right 

    return counter
    

print(partitionArray([1, 2, 3, 5, 6], 2))
print(partitionArray([2, 2, 4, 5], 0))