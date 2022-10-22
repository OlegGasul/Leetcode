import bisect

def createSortedArray(instructions) -> int:
    if len(instructions) == 0:
        return 0
    
    nums = [instructions[0]]

    result = 0

    for i in range(1, len(instructions)):
        left = bisect.bisect_left(nums, instructions[i])
        right = bisect.bisect_right(nums, instructions[i])

        nums.insert(left, instructions[i])

        if left == 0:
            continue

        if right == len(nums) - 1:
            continue

        result += min(left, len(nums) - right - 1)

    return result


print(createSortedArray([1, 5, 6, 2]))
print(createSortedArray([1, 2, 3, 6, 5, 4]))
print(createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))