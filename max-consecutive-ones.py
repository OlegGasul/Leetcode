def findMaxConsecutiveOnes(nums) -> int:
    length = len(nums)
    nums.append(0)

    result = 0

    for i in range(length):
        if nums[i] == 1:
            nums[i] = nums[i] + nums[i - 1]
            result = max(result, nums[i])

    return result


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))