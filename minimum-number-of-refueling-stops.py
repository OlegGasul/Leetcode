import heapq

class Solution:
    def minRefuelStops(self, target, tank, stations):
        pq = []
        stations.append([target, float('inf')])

        result = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                result += 1
            
            if tank < 0:
                return -1
            
            heapq.heappush(pq, -capacity)
            prev = location

        return result
            
solution = Solution()
print(solution.minRefuelStops(100, 50, [[25, 25], [50, 50]]))
print(solution.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))
print(solution.minRefuelStops(100, 25, [[25, 25], [50, 25], [75, 25]]))
print(solution.minRefuelStops(100, 1, [[10, 100]]))