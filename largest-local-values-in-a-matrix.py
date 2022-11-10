class Solution:
    def largestLocal(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        def maxValue(i, j):
            return max(
                grid[i][j], grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                grid[i][j - 1], grid[i][j + 1],
                grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
            )

        result = []
        for i in range(1, rows - 1):
            result.append([])
            
            for j in range(1, cols - 1):
                result[-1].append(maxValue(i, j))

        return result

solution = Solution()
print(solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
print(solution.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))