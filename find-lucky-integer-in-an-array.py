from collections import Counter

def findLucky(arr) -> int:
    counter = Counter(arr)
        
    for key, value in sorted(counter.items(), reverse = True):
        if key == value:
            return key
            
    return -1

print(findLucky([2, 2, 3, 4]))
print(findLucky([1, 2, 2, 3, 3, 3]))
print(findLucky([2, 2, 2, 3, 3]))