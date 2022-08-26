def hIndex(citations) -> int:
    citations.sort()

    length = len(citations)
    result = 0
    
    for i in reversed(range(length)):
        count = length - i
        
        if count >= citations[i]:
            result = max(result, citations[i])
        else:
            result = max(result, count)

    return result


print(hIndex([0, 1, 3, 5, 6, 10]))
print(hIndex([0, 1, 3, 5, 6]))
print(hIndex([0, 1, 3, 5, 6, 10, 20, 25]))
print(hIndex([1, 3, 1]))
print(hIndex([100]))
# [0, 1, 3, 5, 6, 10]