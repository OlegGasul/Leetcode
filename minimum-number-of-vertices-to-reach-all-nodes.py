def findSmallestSetOfVertices(n: int, edges):
    nodes = set([i for i in range(n)])
        
    for u, v in edges:
        nodes.discard(v)

    return list(nodes)

print(findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))