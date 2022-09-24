import heapq
from collections import defaultdict

def findTheCity(n: int, edges, distanceThreshold: int) -> int:
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add((edge[1], edge[2]))
        graph[edge[1]].add((edge[0], edge[2]))
    
    def dijkstra(start):
        distances = [float('inf')] * n
        visited = [False] * n
        distances[start] = 0

        pq = []
        pq.append((0, start))
        heapq.heapify(pq)

        while pq:
            minValue, index = heapq.heappop(pq)
            visited[index] = True

            for edge in graph[index]:
                if visited[edge[0]]:
                    continue
                newDistance = distances[index] + edge[1]
                if newDistance < distances[edge[0]]:
                    distances[edge[0]] = newDistance
                    heapq.heappush(pq, (newDistance, edge[0]))
                    heapq.heapify(pq)

        return distances
    
    result = []
    heapq.heapify(result)
    for node in range(n):
        dist = dijkstra(node)
        
        count = 0
        for i in range(n):
            if i == node:
                continue
            if dist[i] <= distanceThreshold:
                count += 1

        heapq.heappush(result, (count, node))
        heapq.heapify(result)

    minCities = heapq.heappop(result)
    
    maxNode = minCities[1]
    minCities = minCities[0]
    
    while result:
        value = heapq.heappop(result)
        if value[0] > minCities:
            break
        maxNode = value[1]

    return maxNode


print(findTheCity(8, [[3, 6, 5840], [0, 6, 7765], [0, 4, 4017], [0, 3, 3930], [0, 7, 1730],
    [3, 4, 9214], [0, 5, 5861], [2, 6, 2600], [1, 4, 1908], [4, 6, 665], [1, 5, 5140], [5, 7, 6921],
    [2, 7, 5674], [1, 2, 4154], [2, 5, 913], [0, 2, 7125], [6, 7, 6799], [1, 7, 6166], [4, 5, 5878],
    [1, 6, 4816], [1, 3, 5591], [5, 6, 7226], [3, 7, 3901], [3, 5, 9989], [2, 3, 8504], [4, 7, 2366]], 919))
print(findTheCity(6, [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]], 417))
print(findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
print(findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2))