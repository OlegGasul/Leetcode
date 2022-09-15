from collections import defaultdict

def makeConnected(n: int, connections) -> int:
    def dfs(i):
        if i in seen:
            return 0
        seen.add(i)
        for j in graph[i]:
            dfs(j)
        return 1
        
    if len(connections) < n - 1:
        return -1
    
    graph, seen = defaultdict(set), set()
    
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
        
    return sum(dfs(i) for i in range(n)) - 1

print(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))