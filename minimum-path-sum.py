def minPathSum(grid) -> int:
    n = len(grid)
    m = len(grid[0])

    for i in range(1, m):
        grid[0][i] = grid[0][i - 1] + grid[0][i]

    for i in range(1, n):
        grid[i][0] = grid[i - 1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        
    return grid[-1][-1]

print(minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]]))

print(minPathSum([
    [1, 2, 3],
    [4, 5, 6]]))