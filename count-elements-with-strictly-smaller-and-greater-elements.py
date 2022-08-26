from collections import Counter

def countElements(nums) -> int:
    counter = Counter(sorted(nums))
    values = list(counter.values())
    return sum(values[1:len(values) - 1])


print(countElements([-3, 100, 3, 3, 90]))
print(countElements([11, 7, 2, 15]))