from math import inf

def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    
    maximum = -inf
    amount = 0

    for i in range(len(nums)):
        amount += nums[i]
        if nums[i] > amount:
            amount = nums[i]

        maximum = max(maximum, amount)

    return maximum

    

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))