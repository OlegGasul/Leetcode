from collections import Counter

def numberOfPairs(nums):
    result = [0, 0]

    counter = Counter(nums)
    
    for value in counter.values():
        result[0] += value // 2
        result[1] += value % 2

    return result


print(numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
print(numberOfPairs([1, 1]))
print(numberOfPairs([1, 3, 2, 1, 3, 2, 2, 1, 2, 3, 4, 5]))