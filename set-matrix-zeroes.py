def setZeroes(matrix) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    
    rowValues = [1] * rows
    colValues = [1] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowValues[i] = 0
                colValues[j] = 0

    for i in range(rows):
        for j in range(cols):
            if rowValues[i] == 0 or colValues[j] == 0:
                matrix[i][j] = 0

    print(matrix)


setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]]
)

setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]]
)