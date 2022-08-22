def arrayPairSum(nums) -> int:
    return sum(sorted(nums)[::2])

# [6, 2, 6, 5, 1, 2]
# [6, 6, 5, 2, 2, 1]
print(arrayPairSum([6, 2, 6, 5, 1, 2]))