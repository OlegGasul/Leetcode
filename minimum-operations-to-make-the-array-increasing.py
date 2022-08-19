def minOperations(nums) -> int:
    length = len(nums)
    if length == 0:
        return 0

    count = 0
    prev = nums[0]

    for i in range(1, length):
        if nums[i] <= prev:
            incr = prev - nums[i] + 1
            prev = nums[i] + incr
            count += incr
        else:
            prev = nums[i]

    return count

print(minOperations([1, 1, 1]))
print(minOperations([1, 5, 2, 4, 1]))