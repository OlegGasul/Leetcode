from collections import defaultdict

def reachableNodes(n: int, edges, restricted) -> int:
    graph = defaultdict(set)

    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    visited = set()
    restricted = set(restricted)

    queue = [0]

    while queue:
        node = queue.pop(0)
        visited.add(node)

        for edge in graph[node]:
            if edge in restricted or edge in visited:
                continue

            queue.append(edge)

    
    return len(visited)
            


print(reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))
print(reachableNodes(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]))