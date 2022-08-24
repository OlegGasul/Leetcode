# https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDisappearedNumbers(nums):
    length = len(nums)
    i = 0
    result = []

    while i < length:
        correctPos = nums[i] - 1
        while 1 <= nums[i] <= length and nums[i] != nums[correctPos]:
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i] - 1
        
        i += 1

    for i in range(length):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result
    

# print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
# print(findDisappearedNumbers([1, 4, 25, 10, 25]))
# print(findDisappearedNumbers([1, 1, 2]))
print(findDisappearedNumbers([5, 10]))

# [4, 3, 2, 7, 8, 2, 3, 1]
# [3, 2, 3, 4, 8, 2, 7, 1]