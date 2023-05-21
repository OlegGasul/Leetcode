import heapq

class Solution:
    def shortestPath(self, grid, k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows == 1 and cols == 1:
            return 0

        dp = [[{} for j in range(cols)] for i in range(rows)]

        pq = [(0, 0, 0, k)]

        result = float('inf')

        while pq:
            dist, i, j, currentK = heapq.heappop(pq)
            newDist = dist + 1

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newI, newJ = i + di, j + dj
                if newI < 0 or newI >= rows or newJ < 0 or newJ >= cols:
                    continue
                
                if grid[i][j] == 1 and currentK == 0:
                    continue
                
                if grid[i][j] == 1:
                    newK = currentK - 1
                else:
                    newK = currentK
                
                distMap = dp[newI][newJ]
                if newK in distMap and distMap[newK] <= newDist:
                    continue
                distMap[newK] = newDist
                
                if newI == rows - 1 and newJ == cols - 1:
                    result = min(result, newDist)
                else:
                    heapq.heappush(pq, (newDist, newI, newJ, newK))


        return result if result != float('inf') else -1

solution = Solution()
assert solution.shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1) == 6
assert solution.shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1) == -1