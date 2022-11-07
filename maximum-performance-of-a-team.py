import heapq

class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        efficiencySpeed = zip(efficiency, speed)
        efficiencySpeed = sorted(efficiencySpeed, reverse = True)

        result = 0
        
        totalSpeed = 0
        
        pq = []
        heapq.heapify(pq)

        for i in range(n):
            efficiency = efficiencySpeed[i][0]
            speed = efficiencySpeed[i][1]
            heapq.heappush(pq, speed)

            totalSpeed += speed
            if i >= k:
                totalSpeed -= heapq.heappop(pq)
            
            result = max(result, efficiency * totalSpeed)

        return result % (10 ** 9 + 7)


solution = Solution()
print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3))
print(solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4))