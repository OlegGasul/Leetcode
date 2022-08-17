def findMin(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    left, right = 0, len(nums) - 1
    result = nums[0]

    while left <= right:
        if nums[left] < nums[right]:
            return min(result, nums[left])
        
        middle = (left + right) // 2
        result = min(result, nums[middle])

        if nums[middle] >= nums[left]:
            left = middle + 1
        else:
            right = middle - 1

    return result

# print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([0, 1, 2, 4, 5, 6, 7]))
print(findMin([7, 0, 1, 2, 4, 5, 6]))
