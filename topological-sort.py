def topologicalSort(n, graph):
    visited = set()
    ordering = [0] * n

    def dfs(node, visitedNodes):
        visited.add(node)

        if node in graph:
            for edge in graph[node]:
                if not edge in visited:
                    dfs(edge, visitedNodes)

        visitedNodes.append(node)

    i = n - 1

    for node in range(n):
        if not node in visited:
            visitedNodes = []
            dfs(node, visitedNodes)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i -= 1

    return ordering

print(topologicalSort(5, {
    0: {1, 2},
    1: {3},
    2: {3},
    3: {4}
}))