def calculateIsland(grid, rows, cols, x, y):
    # print('calculateIsland')

    result = 1
    grid[x][y] = 0

    # print('x = ' + str(x))
    # print('y = ' + str(y))
    # print()

    if y + 1 < cols and grid[x][y + 1] == 1:
        result += calculateIsland(grid, rows, cols, x, y + 1)
    
    if x + 1 < rows and grid[x + 1][y] == 1:
        result += calculateIsland(grid, rows, cols, x + 1, y)

    if y - 1 >= 0 and grid[x][y - 1] == 1:
        result += calculateIsland(grid, rows, cols, x, y - 1)

    if x - 1 >= 0 and grid[x - 1][y] == 1:
        result += calculateIsland(grid, rows, cols, x - 1, y)
    
    # print('result = ' + str(result))

    return result



def maxAreaOfIsland(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    maxArea = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                maxArea = max(calculateIsland(grid, rows, cols, i, j), maxArea)
                # print('maxArea = ' + str(maxArea))

    return maxArea


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))

grid = [[0,0,0,0,0,0,0,0]]
print(maxAreaOfIsland(grid))