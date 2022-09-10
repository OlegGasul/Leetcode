def findCenter(edges) -> int:
    if len(edges) == 0:
        return -1
        
    a = set(edges[0])
    for i in range(1, len(edges)):
        a = a.intersection(edges[i])
            
    return list(a)[0]

print(findCenter([[1, 2], [2, 3], [4, 2]]))
print(findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))