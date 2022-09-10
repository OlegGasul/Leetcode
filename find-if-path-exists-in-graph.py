from collections import defaultdict

def validPath(n: int, edges, source: int, destination: int) -> bool:
    if source == destination:
        return True
    
    graph = defaultdict(set)
        
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    visited = set()

    queue = [source]
    while queue:
        node = queue.pop(0)

        for edge in graph[node]:
            if edge in visited:
                continue
            if edge == destination:
                return True
                
            visited.add(edge)
            queue.append(edge)
    
    return False

print(validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))