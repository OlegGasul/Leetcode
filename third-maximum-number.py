def thirdMax(nums) -> int:
    nums = sorted(list(set(nums)))
    if len(nums) < 3:
        return nums[-1]
        
    return nums[-3]

print(thirdMax([3, 2, 1]))
print(thirdMax([2, 2, 3, 1]))