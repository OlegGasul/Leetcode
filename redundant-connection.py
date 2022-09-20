def findRedundantConnection(edges):
    parent = {}

    def find(k):
        if parent[k] != k:
            parent[k] = find(parent[k])
        return parent[k]

    def union(s1, s2):
        parent[s2] = parent[s1]

    result = []

    for edge in edges:
        x = edge[0]
        y = edge[1]

        if not x in parent:
            parent[x] = x
        if not y in parent:
            parent[y] = y
        
        s1 = find(x)
        s2 = find(y)
        if s1 == s2:
            result.append(edge)
        else:
            union(s1, s2)

    return result[-1]

print(findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))