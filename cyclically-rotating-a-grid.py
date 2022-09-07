def rotateGrid(grid, k: int):
    rows = len(grid)
    cols = len(grid[0])
        
    def pullLevel(level):
        nums = []
            
        for i in range(level, rows - level - 1):
            nums.append(grid[i][level])
            
        for j in range(level, cols - level - 1):
            nums.append(grid[rows - level - 1][j])
                
        for i in reversed(range(level + 1, rows - level)):
            nums.append(grid[i][cols - level - 1])
                
        for j in reversed(range(level + 1, cols - level)):
            nums.append(grid[level][j])
        
        return nums

    def fillLevel(level, nums):
        for i in range(level, rows - level - 1):
            grid[i][level] = nums.pop(0)
            
        for j in range(level, cols - level - 1):
            grid[rows - level - 1][j] = nums.pop(0)
                
        for i in reversed(range(level + 1, rows - level)):
            grid[i][cols - level - 1] = nums.pop(0)
                
        for j in reversed(range(level + 1, cols - level)):
            grid[level][j] = nums.pop(0)

    for i in range(min(rows, cols) // 2):
        nums = pullLevel(i)
        length = len(nums)
        
        fillLevel(i, nums[length - k % length : length] + nums[0 : length - k % length])
    
    return grid

print(rotateGrid([
    [10, 1, 4, 8],
    [6, 6, 3, 10],
    [7, 4, 7, 10],
    [1, 10, 6, 1],
    [2, 1, 1, 10],
    [3, 8, 9, 2],
    [7, 1, 10, 10],
    [7, 1, 4, 9],
    [2, 2, 4, 2],
    [10, 7, 5, 10]], 1))

print(rotateGrid([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]], 2))

print(rotateGrid([
    [40, 10],
    [30, 20]], 10))