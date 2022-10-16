# A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

# For example, these are arithmetic sequences:

# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic:

# 1, 1, 2, 5, 7
# You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

# Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

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
