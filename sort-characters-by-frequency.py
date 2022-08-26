from collections import Counter

def frequencySort(s: str) -> str:
    counter = Counter(s)

    result = ""
    for pair in counter.most_common():
        result += pair[0] * pair[1]

    return result

print(frequencySort("Aabb"))
print(frequencySort("cccaaa"))