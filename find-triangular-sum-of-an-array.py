def triangularSum(nums) -> int:
    if len(nums) == 0:
        return 0
    
    while len(nums) > 1:
        for i in range(1, len(nums)):
            nums[i - 1] = (nums[i] + nums[i - 1]) % 10

        nums.pop(-1)
    
    return nums.pop()

print(triangularSum([1, 2, 3, 4, 5]))