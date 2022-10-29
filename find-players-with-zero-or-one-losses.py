from collections import Counter

def findWinners(matches):
    counter = Counter()
        
    for w, l in matches:
        counter[l] += 1
        if not w in counter:
            counter[w] = 0
                
    result = [[], []]
        
    mostCommon = counter.most_common()
        
    while mostCommon:
        id, count = mostCommon.pop()
        if count > 1:
            break
                
        result[count].append(id)
        
    result[0].sort()
    result[1].sort()
        
    return result

print(findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print(findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))