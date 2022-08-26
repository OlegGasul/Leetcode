def isPossible(nums) -> bool:
    values = {}
    values[nums[0]] = 1

    for i in range(1, len(nums)):
        if nums[i - 1] in values:
            values[nums[i - 1]] -= 1
            if values[nums[i - 1]] == 0:
                del values[nums[i - 1]]
        values[nums[i]] = 1

    print(values)

    return nums[-1] in values and values[nums[-1]] == 1 and len(values) == 1

print(isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
print(isPossible([1, 2, 3, 4, 4, 5]))