from collections import defaultdict

def smallestStringWithSwaps(s: str, pairs) -> str:
    graph = defaultdict(list)

    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    parent = [i for i in range(len(s))]
    
    def find(k):
        if parent[k] != k:
            parent[k] = find(parent[k])
        return parent[k]

    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        
        if s1 != s2:
            parent[s2] = parent[s1]

    for u, v in pairs:
        union(u, v)

    groups = defaultdict(list)
    for i in range(len(s)):
        groups[find(i)].append(s[i])

    for id in groups.keys(): 
        groups[id].sort(reverse = True)
    
    result = []
    for i in range(len(s)): 
        result.append(groups[find(i)].pop())

    return ''.join(result)


print(smallestStringWithSwaps("cba", [[0, 1], [1, 2]]))
print(smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
print(smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))