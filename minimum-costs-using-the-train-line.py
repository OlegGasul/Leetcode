from collections import defaultdict
import heapq

class DijkstraSolution:
    def minimumCosts(self, regular, express, expressCost: int):
        n = len(regular)
        graph = defaultdict(set)
        
        distances = defaultdict(set)
        visited = set()

        for i in range(n):
            graph[(0, i)].add((0, i + 1, regular[i]))
            graph[(0, i)].add((1, i, expressCost))
            
            graph[(1, i)].add((1, i + 1, express[i]))
            graph[(1, i)].add((0, i, 0))

        pq = []
        pq.append((0, (0, 0)))
        heapq.heapify(pq)

        distances[(0, 0)] = 0
        minDistances = [-1] * (n + 1)

        while pq:
            minValue, node = heapq.heappop(pq)
            visited.add(node)

            for a, b, d in graph[node]:
                if (a, b) in visited:
                    continue

                newDistance = distances[node] + d
                if not (a, b) in distances or newDistance < distances[(a, b)]:
                    distances[(a, b)] = newDistance

                    if minDistances[b] < 0:
                        minDistances[b] = newDistance
                    else:
                        minDistances[b] = min(minDistances[b], newDistance)

                    heapq.heappush(pq, (newDistance, (a, b)))
                    heapq.heapify(pq)
        
        minDistances.pop(0)
        return minDistances

class Solution:
    def minimumCosts(self, regular, express, expressCost: int):
        n = len(regular)
        
        prevRegular = 0
        prevExpress = expressCost

        result = [0] * n

        for i in range(n):
            regularFee = regular[i]
            expressFee = express[i]

            regularToRegular = prevRegular + regularFee
            regularToExpress = prevRegular + expressCost + expressFee
            expressToRegular = prevExpress + regularFee
            expressToExpress = prevExpress + expressFee

            prevRegular = min(regularToRegular, expressToRegular)
            prevExpress = min(regularToExpress, expressToExpress)

            result[i] = min(prevRegular, prevExpress)

        return result
        
solution = Solution()
assert solution.minimumCosts([1, 6, 9, 5], [5, 2, 3, 10], 8) == [1, 7, 14, 19]
assert solution.minimumCosts([11, 5, 13], [7, 10, 6], 3) == [10, 15, 24]