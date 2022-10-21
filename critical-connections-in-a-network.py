from collections import defaultdict

def criticalConnections(n: int, connections):
    graph = defaultdict(list)
    for v in connections:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
            
    desc = [None] * n
    lowLink = [None] * n
    
    current = 0
       
    def dfs(node, parent):
        nonlocal current

        if desc[node] is None:
            desc[node] = current
            lowLink[node] = current
            current += 1
            
            for n in graph[node]:
                if desc[n] is None:
                    dfs(n, node)
                    
            lowLink[node] = min([lowLink[i] for i in graph[node] if i != parent] + [lowLink[node]])
                
    dfs(0, None)

    print(lowLink)
    print(desc)
    
    result = []

    for u, v in connections:
        if lowLink[u] > desc[v] or lowLink[v] > desc[u]:
            result.append([u, v])
    
    return result

print(criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
print(criticalConnections(2, [[0, 1]]))