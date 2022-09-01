def checkXMatrix(grid) -> bool:
    length = len(grid)

    def checkRow(row, i):
        if grid[row][i] == 0 or grid[row][length - i - 1] == 0:
            return False

        for j in range(i):
            if grid[row][j] != 0:
                return False
        
        for j in range(length - i, length):
            if grid[row][j] != 0:
                return False

        for j in range(i + 1, length - i - 1):
            if grid[row][j] != 0:
                return False

        return True

    for i in range(length // 2):
        if not checkRow(i, i) or not checkRow(length - i - 1, i):
            return False
    
    return True


print(checkXMatrix([
    [2, 0, 0, 0, 1],
    [0, 4, 0, 1, 0],
    [0, 0, 5, 0, 0],
    [0, 5, 0, 2, 0],
    [0, 0, 0, 0, 2]]))

print(checkXMatrix([
    [2, 0, 0, 1],
    [0, 3, 1, 0],
    [0, 5, 2, 0],
    [4, 0, 0, 2]]))

print(checkXMatrix([
    [2, 0, 0, 0, 1],
    [0, 3, 0, 1, 0],
    [0, 0, 2, 0, 0],
    [0, 1, 0, 2, 0],
    [4, 0, 0, 0, 2]]))

print(checkXMatrix([
    [2, 0, 0, 0, 0, 1],
    [0, 3, 0, 0, 1, 0],
    [0, 0, 2, 1, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [4, 0, 0, 0, 0, 1]]))

print(checkXMatrix([
    [2, 0, 1, 1],
    [1, 3, 1, 0],
    [0, 5, 2, 0],
    [4, 1, 0, 2]]))
