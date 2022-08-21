def arrayChange(nums, operations):
    indexes = {}
    for i in range(len(nums)):
        indexes[nums[i]] = i

    for op in operations:
        nums[indexes[op[0]]] = op[1]
        indexes[op[1]] = indexes[op[0]]

    return nums

print(arrayChange([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]))
print(arrayChange([1, 2], [[1, 3], [2, 1], [3, 2]]))