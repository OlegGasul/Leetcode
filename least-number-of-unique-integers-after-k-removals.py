from collections import Counter

def findLeastNumOfUniqueInts(arr, k: int):
    counter = Counter(arr)
        
    mostCommon = counter.most_common()

    i = len(mostCommon) - 1
    while k and mostCommon:
        if mostCommon[i][1] > k:
            break
        else:
            k -= mostCommon[i][1]
        i -= 1

    return i + 1

print(findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))