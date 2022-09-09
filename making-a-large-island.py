from collections import Counter

def largestIsland(grid) -> int:
    n = len(grid)

    islands = {}
    id = 2
    squares = Counter()

    def markIsland(i, j, id):
        grid[i][j] = id
        squares[id] += 1
        
        if j + 1 < n and grid[i][j + 1] == 1:
            markIsland(i, j + 1, id)
        if i + 1 < n and grid[i + 1][j] == 1:
            markIsland(i + 1, j, id)
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            markIsland(i, j - 1, id)
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            markIsland(i - 1, j, id)

    hasZero = False

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                markIsland(i, j, id)
                id += 1
            elif grid[i][j] == 0:
                hasZero = True

    if len(squares.keys()) == 1:
        id = list(squares.keys())[0]
        if hasZero:
            squares[id] += 1
        
        print(squares[id])
        return squares[id]

    result = float('-inf')
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                ids = set()

                if j + 1 < n and grid[i][j + 1] > 1:
                    ids.add(grid[i][j + 1])
                if i + 1 < n and grid[i + 1][j] > 1:
                    ids.add(grid[i + 1][j])
                if j - 1 >= 0 and grid[i][j - 1] > 1:
                    ids.add(grid[i][j - 1])
                if i - 1 >= 0 and grid[i - 1][j] > 1:
                    ids.add(grid[i - 1][j])

                square = 0
                for id in ids:
                    square += squares[id]
                square += 1

                result = max(result, square)
                
    return result

print(largestIsland([[0, 0], [0, 1]]))
print(largestIsland([
    [1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0]
]))
print(largestIsland([[1, 1], [1, 1]]))
print(largestIsland([[1, 1], [1, 0]]))
print(largestIsland([[0, 0], [0, 0]]))
print(largestIsland([[1, 0], [0, 1]]))