def minimumSum(num: int) -> int:
    nums = sorted(map(int, list(str(num))))
    return int(str(nums[0]) + str(nums[2])) + int(str(nums[1]) + str(nums[3]))

print(minimumSum(2932))