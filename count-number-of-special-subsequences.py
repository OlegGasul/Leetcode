def countSpecialSubsequences(nums) -> int:
    zero = 0
    zeroOne = 0
    zeroOneTwo = 0
    
    for i in range(len(nums)):
        value = nums[i]

        if value == 0:
            zero = 2 * zero + 1
        elif value == 1:
            zeroOne = 2 * zeroOne + zero
        elif value == 2:
            zeroOneTwo = 2 * zeroOneTwo + zeroOne
    
    return (zeroOneTwo) % (10 ** 9 + 7)

print(countSpecialSubsequences([0, 1, 2, 0, 1, 2]))