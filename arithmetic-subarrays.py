import functools

def checkIfArithmetic(nums):
    nums = sorted(nums)
    diff = nums[1] - nums[0]

    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] != diff:
            return False

    return True

def checkArithmeticSubarrays(nums, left, right):
    result = []

    dp = {}
    
    for i in range(len(left)):
        first = left[i]
        last = right[i]

        if (first, last) in dp:
            result.append(dp[(first, last)])
        else:
            isArithmetic = checkIfArithmetic(nums[first : last + 1])
            dp[(first, last)] = isArithmetic
            result.append(isArithmetic)

    return result
    

print(checkArithmeticSubarrays(
    [4, 6, 5, 9, 3, 7],
    [0, 0, 2],
    [2, 3, 5]))

print(checkArithmeticSubarrays(
    [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0],
    [5, 4, 3, 2, 4, 7, 6, 1, 7],
    [6, 5, 6, 3, 7, 10, 7, 4, 10]))
