def twoSum(nums, target):
    lookup = {}
    
    for position, number in enumerate(nums):
        if target - number in lookup:
            return lookup[target - number], position
        else: lookup[number] = position

print(twoSum([2, 7, 11, 15], 9))