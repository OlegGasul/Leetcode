def gridIllumination(n: int, lamps, queries):
    grid = [[0 for _ in range(n)] for _ in range(n)]
        
    for k in range(len(lamps)):
        lamp = lamps[k]
            
        grid[lamp[0]][lamp[1]] = 1
        for i in range(n):
            grid[lamp[0]][i] = 1
            grid[i][lamp[1]] = 1
                
        i = lamp[0]
        j = lamp[1]
            
        while i < n and j < n:
            grid[i][j] = 1
            i += 1
            j += 1
                
        i = lamp[0]
        j = lamp[1]
            
        while i >= 0 and j >= 0:
            grid[i][j] = 1
            i -= 1
            j -= 1
        
    def turnOn(i, j):
        if j + 1 < n:
            grid[i][j + 1] = 0
        if i + 1 < n:
            grid[i + 1][j] = 0
        if j - 1 >= 0:
            grid[i][j - 1] = 0
        if i - 1 >= 0:
            grid[i - 1][j] = 0
            
        if i + 1 < n and j + 1 < n:
            grid[i + 1][j + 1] = 0
        if i + 1 < n and j - 1 >= 0:
            grid[i + 1][j - 1] = 0
        if i - 1 >= 0 and j - 1 >= 0:
            grid[i - 1][j - 1] = 0
        if i - 1 >= 0 and j + 1 < n:
            grid[i - 1][j + 1] = 0
    
    result = []
    
    for query in queries:
        result.append(grid[query[0]][query[1]])
            
        if grid[query[0]][query[1]] == 1:
            turnOn(query[0], query[1])
    
    return result

print(gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]))
print(gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 1]]))
print(gridIllumination(5, [[0, 0], [0, 4]], [[0, 4], [0, 1], [1, 4]]))