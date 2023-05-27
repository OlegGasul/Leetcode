class Solution:
    def closedIsland(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            grid[i][j] = -1

            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newI = i + di
                newJ = j + dj

                if newI < 0 or newI >= rows or newJ < 0 or newJ >= cols:
                    continue
                
                if grid[newI][newJ] != 0:
                    continue
                
                dfs(newI, newJ)

        for j in range(cols):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[rows - 1][j] == 0:
                dfs(rows - 1, j)

        for i in range(1, rows - 1):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][cols - 1] == 0:
                dfs(i, cols - 1)
        
        result = 0

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    result += 1
                    dfs(i, j)
        
        return result

solution = Solution()
assert solution.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2
assert solution.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1
assert solution.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]) == 2