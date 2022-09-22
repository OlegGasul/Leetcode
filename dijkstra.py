import heapq

def dijkstra(n, graph, start):
    distances = [float('inf')] * n
    visited = [False] * n
    prev = [None] * n
    distances[start] = 0

    pq = []
    pq.append((0, start))
    heapq.heapify(pq)

    while pq:
        minValue, index = heapq.heappop(pq)
        visited[index] = True

        if index in graph:
            for edge in graph[index]:
                if visited[edge[0]]:
                    continue

                newDistance = distances[index] + edge[1]
                if newDistance < distances[edge[0]]:
                    prev[edge[0]] = index
                    distances[edge[0]] = newDistance
                    heapq.heappush(pq, (newDistance, edge[0]))
                    heapq.heapify(pq)

    return (distances, prev)

def findShortestPath(n, graph, start, end):
    dist, prev = dijkstra(n, graph, start)
    path = []
    if dist[end] == float('inf'):
        return path

    node = end
    while node:
        path.insert(0, node)
        node = prev[node]

    path.insert(0, start)
    return path

print(findShortestPath(5, {
    0: {(1, 4), (2, 1)},
    2: {(1, 2), (3, 5)},
    1: {(3, 1)},
    3: {(4, 3)}
}, 0, 4))