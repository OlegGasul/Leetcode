from collections import Counter

def mostFrequent(nums, key: int) -> int:
    counter = Counter()

    for i in range(len(nums) - 1):
        if nums[i] == key:
            counter[nums[i + 1]] += 1

    return counter.most_common(1)[0][0]


print(mostFrequent([1, 100, 200, 1, 100], 1))