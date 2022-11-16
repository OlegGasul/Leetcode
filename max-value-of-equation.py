import heapq

class Solution:
    def findMaxValueOfEquation(self, points, k: int) -> int:
        hq = []
        result = -float('inf')
        
        for x, y in points:
            while hq and hq[0][1] < x - k:
                heapq.heappop(hq)
            
            if hq:
                result = max(result, -hq[0][0] + y + x)
            
            heapq.heappush(hq, (x - y, x))
        
        return result

solution = Solution()
print(solution.findMaxValueOfEquation([[1, 3], [2, 0], [5, 10], [6, -10]], 1))