def smallestEqual(nums) -> int:
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
            
    return -1

print(smallestEqual([0, 1, 2]))
print(smallestEqual([4, 3, 2, 1]))