from collections import Counter

def areOccurrencesEqual(s: str) -> bool:
    if len(s) == 0:
        return True
    return len(set(Counter(s).values())) == 1

print(areOccurrencesEqual("abacbc"))
print(areOccurrencesEqual("aaabb"))
print(areOccurrencesEqual(""))