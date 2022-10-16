# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

def arrayPairSum(nums) -> int:
    return sum(sorted(nums)[::2])

# [6, 2, 6, 5, 1, 2]
# [6, 6, 5, 2, 2, 1]
print(arrayPairSum([6, 2, 6, 5, 1, 2]))
