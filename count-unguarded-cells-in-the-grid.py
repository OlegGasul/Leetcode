def countUnguarded(m: int, n: int, guards, walls) -> int:
    size = m * n

    visible = set()
    unguarded = size - (len(guards) + len(walls))

    grid = [[0 for x in range(n)] for y in range(m)] 

    for wall in walls:
        grid[wall[0]][wall[1]] = 1

    for guard in guards:
        grid[guard[0]][guard[1]] = 2

    for guard in guards:
        guardI = guard[0]
        guardJ = guard[1]

        # Right
        j = guardJ + 1
        while j < n:
            if grid[guardI][j] > 0:
                break
            visible.add((guardI, j))
            j += 1

        # Left
        j = guardJ - 1
        while j >= 0:
            if grid[guardI][j] > 0:
                break
            visible.add((guardI, j))
            j -= 1

        # Down
        i = guardI + 1
        while i < m:
            if grid[i][guardJ] > 0:
                break
            visible.add((i, guardJ))
            i += 1

        # Top
        i = guardI - 1
        while i >= 0:
            if grid[i][guardJ] > 0:
                break
            visible.add((i, guardJ))
            i -= 1

    return unguarded - len(visible)

print(countUnguarded(2, 7, [[1, 5], [1, 1], [1, 6], [0, 2]], [[0, 6], [0, 3], [0, 5]]))
# print(countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))