def getDistances(arr):
    indexes = {}

    for i, x in enumerate(arr):
        if not x in indexes:
            indexes[x] = []
        
        indexes[x].append(i)

    for i, x in enumerate(arr):
        arr[i] = sum(map(lambda index: abs(i - index), indexes[x]))
    
    return arr

print(getDistances([2, 1, 3, 1, 2, 3, 3]))