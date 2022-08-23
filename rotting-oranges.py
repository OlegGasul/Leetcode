def orangesRotting(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])

    freshes = 0
    rotten = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                freshes += 1
            elif grid[i][j] == 2:
                rotten.append(tuple((i, j)))

    def rotOrange(i, j, newRotten):
        nonlocal freshes
        
        if i < rows and i >= 0 and j < cols and j >= 0 and grid[i][j] == 1:
            grid[i][j] = 2
            newRotten.append(tuple((i, j)))
            freshes -= 1
    
    minutes = 0
    while rotten and freshes > 0:
        newRotten = []

        while rotten:
            coords = rotten.pop()
            i = coords[0]
            j = coords[1]
        
            rotOrange(i, j + 1, newRotten)
            rotOrange(i + 1, j, newRotten)
            rotOrange(i, j - 1, newRotten)
            rotOrange(i - 1, j, newRotten)
        
        minutes += 1

        rotten = newRotten

    return minutes if freshes == 0 else -1

print(orangesRotting([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]]))

print(orangesRotting([
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]]))
