def findIndex(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right
    else:
        return -1


def searchRange(nums, target: int):
    if len(nums) == 0 or target < nums[0] or target > nums[-1]:
        return [-1, -1]

    index = findIndex(nums, target)
    if index < 0:
        return [-1, -1]

    left = index
    while left - 1 >= 0 and nums[left - 1] == target:
        left -= 1

    right = index
    while right + 1 < len(nums) and nums[right + 1] == target:
        right += 1

    return [left, right]
    

print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 9))