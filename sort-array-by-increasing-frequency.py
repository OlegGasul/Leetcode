from collections import Counter
from functools import cmp_to_key

def frequencySort(nums):
    counter = Counter(nums)
    
    def compare(a, b):
        return b - a if counter[a] == counter[b] else counter[a] - counter[b]
    return sorted(nums, key = cmp_to_key(compare))


print(frequencySort([1, 1, 2, 2, 2, 3]))
print(frequencySort([2, 3, 1, 3, 2]))