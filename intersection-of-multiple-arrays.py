import collections

def intersection(nums):
    length = len(nums)
    counter = collections.Counter()

    for i in range(length):
        for j in range(len(nums[i])):
            counter[nums[i][j]] += 1

    result = []
    for num, count in counter.items():
        if count == length:
            result.append(num)

    return sorted(result)

print(intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))