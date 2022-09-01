from collections import Counter

def uniqueOccurrences(arr) -> bool:
    counter = Counter(arr)
    values = counter.values()
    return len(set(values)) == len(values)

print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))