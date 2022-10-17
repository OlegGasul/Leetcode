def rangeSum(nums, n: int, left: int, right: int) -> int:
  result = []
  for i in range(len(nums)):
    cum = 0
    for j in range(i, len(nums)):
      cum += nums[j]
      result.append(cum)
  
  result.sort()

  return sum(result[left - 1 : right]) % (10 ** 9 + 7)


print(rangeSum([1, 2, 3, 4], 4, 1, 5))