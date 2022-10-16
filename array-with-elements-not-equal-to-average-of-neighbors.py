# You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.
# 
# More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].
# 
# Return any rearrangement of nums that meets the requirements.

def rearrangeArray(nums):
    nums.sort()
    length = len(nums)
    halvedLength = length // 2
        
    if length % 2 == 1:
        middle = nums[halvedLength]
    else:
        middle = (nums[halvedLength - 1] + nums[halvedLength]) / 2

    smaller = []
    greaterOrEqual = []
        
    for num in nums:
        if num < middle:
            smaller.append(num)
        else:
            greaterOrEqual.append(num)

    result = []

    while smaller or greaterOrEqual:
        if smaller:
            result.append(smaller.pop())
        if greaterOrEqual:
            result.append(greaterOrEqual.pop())

    return result
        
print(rearrangeArray([2, 1, 5, 0]))
print(rearrangeArray([6, 2, 0, 9, 7]))
