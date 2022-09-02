def minimumAbsDifference(arr):
    if len(arr) < 2:
        return []
        
    minimum = float('inf')
    arr.sort()
    
    pairs = {}
        
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        if diff < minimum:
            minimum = diff
            
        if diff not in pairs:
            pairs[diff] = []
        pairs[diff].append([arr[i - 1], arr[i]])
    
    return pairs[minimum]

print(minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))