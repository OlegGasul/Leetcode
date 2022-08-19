def equalPairs(grid) -> int:
    length = len(grid)
    count = 0

    rows = {}

    for i in range(0, length):
        h = hash(tuple(grid[i]))
        if h in rows:
            rows[h] += 1
        else:
            rows[h] = 1

    for col in range(0, length):
        values = []

        for row in range(0, length):
            values.append(grid[row][col])
        
        h = hash(tuple(values))
        if h in rows:
            count += rows[h]
    
    return count



print(equalPairs([
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7]]))
    
print(equalPairs([
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2]]))

print(equalPairs([
    [13, 13],
    [13, 13]]))
