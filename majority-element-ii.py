from collections import Counter

def majorityElement(nums):
    length = len(nums)

    if length <= 2:
        return list(set(nums))

    counter = Counter(nums)

    minCount = length // 3 + 1
    result = []

    for pair in counter.most_common():
        if pair[1] >= minCount:
            result.append(pair[0])

    return result

print(majorityElement([3, 2, 3]))
print(majorityElement([2, 1]))
print(majorityElement([1]))