def findIndexInLis(lis, value):
    left = 0
    right = len(lis) - 1

    while left <= right:
        index = left + (right - left) // 2
        middle = lis[index]

        if value == middle:
            return index

        if value > middle:
            left = index + 1
        else:
            right = index - 1

    return left

def lengthOfLIS(nums, start, end) -> int:
    lis = [nums[start]]

    for i in range(start + 1, end):
        if nums[i] > lis[-1]:
            lis.append(nums[i])
        else:
            index = findIndexInLis(lis, nums[i])
            lis[index] = nums[i]

        print(lis)

    return len(lis)


print(lengthOfLIS([10, 100, 101, 102, 103, 104, 9, 2, 5, 3, 7, 8, 9, 10, 101, 18], 0, 3))
