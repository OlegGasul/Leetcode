from collections import Counter

def topKFrequent(nums, k: int):
    counter = Counter(nums)
    
    result = []
    for pair in counter.most_common(k):
        result.append(pair[0])

    return result

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))