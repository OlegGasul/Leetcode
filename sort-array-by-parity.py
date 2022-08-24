def sortArrayByParity(nums):
    result = []

    length = len(nums)
    left = 0
    right = length - 1

    for i in range(length):
        if nums[i] % 2 == 0:
            result.insert(left, nums[i])
            left += 1
        else:
            result.insert(right, nums[i])
            right -= 1

    return result


print(sortArrayByParity([3, 1, 2, 4]))