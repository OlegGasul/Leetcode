def maxSum(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
        
    if rows < 3 or cols < 3:
        return -1
        
    result = 0
        
    for i in range(rows - 2):
        sumTop = grid[i][0] + grid[i][1] + grid[i][2]
        sumBottom = grid[i + 2][0] + grid[i + 2][1] + grid[i + 2][2]
            
        total = sumTop + grid[i + 1][1] + sumBottom
        result = max(result, total)
            
        for j in range(1, cols - 2):
            sumTop -= grid[i][j - 1]
            sumTop += grid[i][j + 2]
                
            sumBottom -= grid[i + 2][j - 1]
            sumBottom += grid[i + 2][j + 2]
                
            total = sumTop + grid[i + 1][j + 1] + sumBottom
            result = max(result, total)
                
    return result

print(maxSum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]))
print(maxSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))