from collections import defaultdict
import heapq

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        graph = defaultdict(set)
        directDistances = defaultdict(int)

        for u, v, dist in edgeList:
            graph[u].add(v)
            directDistances[(u, v)] = dist
            
            graph[v].add(u)

        for u in graph:
            edges = graph[u]

            for v in edges:
                if (v, u) in directDistances:
                    continue
                directDistances[(v, u)] = directDistances[(u, v)]

        shortests = {}
        
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
                
                for v in graph[index]:
                    if visited[v]:
                        continue

                    newDistance = distances[index] + directDistances[(index, v)]
                    if newDistance < distances[v]:
                        distances[v] = newDistance
                        heapq.heappush(pq, (newDistance, v))
                        heapq.heapify(pq)

            return distances

        result = []
        for u, v, limit in queries:
            if not u in shortests:
                shortests[u] = dijkstra(u)
            print(shortests)
            
            result.append(shortests[u][v] < limit)

        return result

solution = Solution()
print(solution.distanceLimitedPathsExist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]))
print(solution.distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]))