import functools

def smallerNumbersThanCurrent(nums):
    length = len(nums)

    indexes = {}

    for i in range(length):
        if not nums[i] in indexes:
            indexes[nums[i]] = []
        indexes[nums[i]] += [i]

    # print(indexes)

    nums = sorted(nums, reverse = True)

    # print(nums)
    
    result = [0] * length

    for i in range(1, length):
        if nums[i] != nums[i - 1]:
            count = length - i
            for index in indexes[nums[i - 1]]:
                result[index] = count

    return result

print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(smallerNumbersThanCurrent([6, 5, 4, 8]))
print(smallerNumbersThanCurrent([7, 7, 7, 7]))