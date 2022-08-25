from collections import Counter

def hasGroupsSizeX(deck) -> bool:
    if len(deck) < 2:
        return False
    
    counter = Counter(deck)
    div = min(counter.values())
    if div < 2:
        return False
    
    for i in range(2, div + 1):
        if all(val % i == 0 for val in counter.values()):
            return True
    
    return False

print(hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
print(hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
print(hasGroupsSizeX([0, 0, 0, 1, 1, 1, 2, 2, 2]))
print(hasGroupsSizeX([0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
print(hasGroupsSizeX([0, 0, 0, 0, 0, 1, 1, 2, 3, 4]))
print(hasGroupsSizeX([0, 0, 1, 1, 1, 1, 2, 2, 3, 4]))
print(hasGroupsSizeX([0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
print(hasGroupsSizeX([1, 1, 1, 1, 1, 0, 0, 0]))
print(hasGroupsSizeX([0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))

