import heapq

class Solution:
    def trapRainWater(self, heightMap) -> int:
        rows = len(heightMap)
        if rows < 2:
            return 0
        
        cols = len(heightMap[0])
        if cols < 2:
            return 0

        visited = set()
        hq = []

        for j in range(cols):
            heapq.heappush(hq, [heightMap[0][j], 0, j])
            heapq.heappush(hq, [heightMap[rows - 1][j], rows - 1, j])
            visited.add((0, j))
            visited.add((rows - 1, j))
        
        for i in range(1, rows - 1):
            heapq.heappush(hq, [heightMap[i][0], i, 0])
            heapq.heappush(hq, [heightMap[i][cols - 1], i, cols - 1])
            visited.add((i, 0))
            visited.add((i, cols - 1))
        
        result = 0

        while hq:
            height, i, j = heapq.heappop(hq)
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii = i + x
                jj = j + y

                if ii >= 0 and ii < rows and jj >= 0 and jj < cols and not (ii, jj) in visited:
                    result += max(0, height - heightMap[ii][jj])

                    heapq.heappush(hq, [max(height, heightMap[ii][jj]), ii, jj])
                    visited.add((ii, jj))

        return result

solution = Solution()
assert solution.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) == 4
assert solution.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) == 10