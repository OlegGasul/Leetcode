from collections import Counter

def mostFrequentEven(nums) -> int:
    counter = Counter()
        
    for num in nums:
        if num % 2 == 0:
            counter[num] += 1
                
    mostCommon = counter.most_common()
    if not mostCommon:
        return -1

    value, count = mostCommon[0]
    for i in range(1, len(mostCommon)):
        if mostCommon[i][1] < count:
            break
                
        value = min(value, mostCommon[i][0])
            
    return value

print(mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
print(mostFrequentEven([4, 4, 4, 9, 2, 4]))
print(mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]))