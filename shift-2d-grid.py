def shiftGrid(grid, k: int):
    queue = []
    count = 0

    rows = len(grid)
    cols = len(grid[0])

    k = k % (rows * cols)
    if k == 0:
        return grid

    for i in range(rows):
        for j in range(cols):
            queue.append(grid[i][j])
            count += 1
            if count == k:
                break

        if count == k:
            break
    
    for i in range(rows):
        for j in range(cols):
            if count > 0:
                count -= 1
                continue
            
            if count == 0:
                # print(queue)
                # print(grid[i][j])
                queue.append(grid[i][j])
                grid[i][j] = queue.pop(0)
                

    for i in range(rows):
        for j in range(cols):
            grid[i][j] = queue.pop(0)
            if len(queue) == 0:
                break

        if len(queue) == 0:
            break

    # print(queue)
    return grid
    

print(shiftGrid([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]], 2))

print(shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))