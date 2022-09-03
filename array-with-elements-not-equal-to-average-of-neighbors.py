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