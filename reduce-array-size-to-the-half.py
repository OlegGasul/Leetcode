import collections

def minSetSize(arr) -> int:
    counter = collections.Counter(arr)
    
    nums = list(map(lambda x: x[1], counter.most_common()))
    
    toDelete = len(arr) // 2
    result = 0
    for num in nums:
        toDelete -= num
        result += 1
        if toDelete <= 0:
            break

    return result



print(minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(minSetSize([1, 1, 2, 2, 3, 3, 4, 5]))