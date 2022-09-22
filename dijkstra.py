import heapq

def dijkstra(n, graph, start):
    distances = [float('inf')] * n
    visited = [False] * n
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
                    distances[edge[0]] = newDistance
                    heapq.heappush(pq, (newDistance, edge[0]))
                    heapq.heapify(pq)

    return distances


print(dijkstra(5, {
    0: {(1, 4), (2, 1)},
    2: {(1, 2), (3, 5)},
    1: {(3, 1)},
    3: {(4, 3)}
}, 0))

print(dijkstra(5, {
    0: {(1, 4), (2, 1)},
    2: {(1, 2), (3, 5)},
    1: {(3, 1)},
    3: {(4, 3)}
}, 1))