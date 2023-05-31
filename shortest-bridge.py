import heapq

class Solution:
    def shortestBridge(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, border):
            grid[i][j] = -2

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newI, newJ = i + di, j + dj
                if newI < 0 or newI >= rows or newJ < 0 or newJ >= cols or grid[newI][newJ] == -2:
                    continue
                
                if grid[newI][newJ] == 0:
                    if not (1, newI, newJ) in border:
                        border.add((1, newI, newJ))
                    continue

                dfs(newI, newJ, border)
        
        islands = 0
        borders = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    islands += 1
                    
                    border = set()
                    dfs(i, j, border)
                    borders.append(border)

                    if islands == 2:
                        break

        if islands != 2:
            return -1
        
        pq = list(borders[0])

        for dist, i, j in pq:
            grid[i][j] = dist

        while pq:
            dist, i, j = heapq.heappop(pq)
            grid[i][j] = dist

            newDist = dist + 1

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newI, newJ = i + di, j + dj
                if newI < 0 or newI >= rows or newJ < 0 or newJ >= cols or grid[newI][newJ] == -2:
                    continue

                if grid[newI][newJ] == 0 or (grid[newI][newJ] > 0 and grid[newI][newJ] > newDist):
                    grid[newI][newJ] = newDist
                    heapq.heappush(pq, (newDist, newI, newJ))
        
        result = float('inf')

        for dist, i, j in borders[1]:
            if grid[i][j] > 0:
                result = min(result, grid[i][j])

        return result

solution = Solution()
assert solution.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
assert solution.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1